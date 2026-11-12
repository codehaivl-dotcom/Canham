"""Run reproducible combat sweeps, analytic stat tables and authored-room chains."""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import statistics
import time

from simulation.combat import CombatSimulator, expected_weapon_dps, load_catalog, make_squad, mitigate

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'simulation'/'results'
LOADOUTS=('balanced','anti_swarm','anti_mechanical','energy','ballistic','fire','sniper')

def quantile(values,p):
    if not values:return None
    values=sorted(values);index=(len(values)-1)*p;lo=int(index);hi=min(lo+1,len(values)-1)
    return round(values[lo]+(values[hi]-values[lo])*(index-lo),4)

def wilson(wins,n):
    if not n:return [0,1]
    z=1.96;p=wins/n;den=1+z*z/n
    center=(p+z*z/(2*n))/den;half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return [round(center-half,6),round(center+half,6)]

def aggregate(results,**labels):
    wins=[r for r in results if r['victory']]
    n=len(results)
    return {**labels,'runs':n,'wins':len(wins),'win_rate':round(len(wins)/n,5),
            'win_rate_ci95':wilson(len(wins),n),'win_duration_p10':quantile([r['duration'] for r in wins],.1),
            'win_duration_p50':quantile([r['duration'] for r in wins],.5),'win_duration_p90':quantile([r['duration'] for r in wins],.9),
            'all_duration_p50':quantile([r['duration'] for r in results],.5),
            'hp_loss_mean':round(statistics.mean(r['hp_loss_fraction'] for r in results),5),
            'win_hp_loss_mean':round(statistics.mean(r['hp_loss_fraction'] for r in wins),5) if wins else None,
            'downs_mean':round(statistics.mean(r['downs'] for r in results),4),
            'revives_mean':round(statistics.mean(r['new_revives'] for r in results),4),
            'medkits_mean':round(statistics.mean(r['items_used'].get('medkit',0) for r in results),4),
            'timeouts':sum(r['outcome']=='timeout' for r in results),
            'max_active_enemies':max(r['max_active_enemies'] for r in results)}

def dump_csv(path,rows):
    if not rows:return
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def stat_tables(c):
    dps=[]
    stats={k:5 for k in ('COM','END','AGI','PER','INT','TEC','MED','RES')}
    for wid,w in c['weapons'].items():
        for eid,enemy in c['enemies'].items():
            for tier,mult in [('civilian',1),('industrial',1.05),('military',1.12),('advanced',1.2),('prototype',1.28),('alien_upper_numeric',1.35)]:
                weapon=deepcopy(w);weapon['damage']*=mult
                dps.append({'weapon':wid,'enemy':eid,'tier':tier,'tier_multiplier':mult,
                            'primary_direct_dps':round(expected_weapon_dps(weapon,stats,'none','mid',enemy),5)})
    armor=[]
    for aid,a in c['armor'].items():
        for dtype in ('ballistic','energy','explosive','fire','electric','bio'):
            received=mitigate(100,a.get('armor',0),a.get('resistances',{}).get(dtype,0),dtype)
            armor.append({'armor':aid,'incoming_type':dtype,'damage_from_raw100':received,
                          'effective_hp_multiplier':round(100/received,5),'attack_speed_multiplier':a.get('attack_speed_multiplier',1)})
    characters=[]
    for survivor in c['roster']:
        for level in (1,10,20,50):
            hp=(100+survivor['stats']['END']*12+(level-1)*5)*(1.2 if survivor.get('role')=='vanguard' else 1)
            # Profession/trait effects are reported separately from base+role to avoid silently claiming coverage.
            characters.append({'survivor':survivor['id'],'name':survivor['name'],'level':level,
                               'base_plus_role_hp':round(hp,2),'stat_total':sum(survivor['stats'].values()),
                               'xp_threshold':25*(level-1)*level,'trait_applied':False})
    return dps,armor,characters

def mission_chains(c,seeds):
    """Carry HP/items/casualties across actual combat rooms, no free per-room heal."""
    stages=[('house',[['crawler','crawler'],['crawler']],.55,.40),
            ('warehouse',[['crawler']*4,['rifleman'],['crawler']*2],.55,.40),
            ('hospital',[['crawler','crawler'],['spitter'],['crawler','crawler','spitter'],['mutated_brute']],.75,.65)]
    rows=[]
    for stage,rooms,hps,dmg in stages:
        results=[]
        for seed in range(seeds):
            squad=deepcopy(c['roster'][:3])
            squad[0]['traits']=['tough'];squad[1]['traits']=['steady_hands'];squad[2]['traits']=['calm']
            squad[0]['consumables']={'medkit':2};squad[1]['consumables']={'frag_grenade':2};squad[2]['consumables']={'medkit':2}
            initial_hp=None;duration=0;downs=0;used=Counter();last=None
            for room_index,enemies in enumerate(rooms):
                for p in squad:
                    # Injury effects/clinic between separate missions are not inferred in a room chain.
                    p.setdefault('level',1)
                result=CombatSimulator(c,100000+seed*20+room_index).run(squad,enemies,
                       difficulty='medium' if stage=='hospital' else 'easy',
                       overrides={'enemy_hp_multiplier':hps,'enemy_damage_multiplier':dmg,
                                  'tutorial_protected':stage!='hospital','item_policy':'aggressive'})
                if initial_hp is None:initial_hp=sum(x['max_hp'] for x in result['survivors'])
                duration+=result['duration'];downs+=result['downs'];used.update(result['items_used']);last=result
                states={x['id']:x for x in result['survivors']}
                if not result['victory']:break
                for p in squad:
                    state=states[p['id']]
                    # Tutorial SAFE_DOWN rises after encounter per Recovery; HP30%, not a full heal.
                    p['hp']=state['max_hp']*.30 if state['state']=='SAFE_DOWN' else state['hp']
                    p['state']='ACTIVE' if state['state']=='SAFE_DOWN' else state['state']
                    p['revive_count']=state['revive_count'];p['consumables']=state['consumables']
            last['duration']=round(duration,2);last['downs']=downs;last['items_used']=dict(used)
            last['hp_loss_fraction']=1-sum(x['hp'] for x in last['survivors'])/initial_hp
            results.append(last)
        rows.append(aggregate(results,scenario=stage,category='authored_chain',squad_size=3,level=1,loadout='authored',difficulty='authored'))
    return rows

def run(seeds=20,base_seed=20261112,quick=False):
    started=time.perf_counter();OUT.mkdir(parents=True,exist_ok=True)
    c=load_catalog();rows=[];traces={};n=0
    for encounter in c['encounters']:
        for size in (3,4,5):
            for loadout in LOADOUTS:
                results=[]
                for iteration in range(seeds):
                    result=CombatSimulator(c,base_seed+iteration).run(make_squad(c,size,10,loadout),encounter['enemies'],difficulty='medium')
                    results.append(result);n+=1
                    if size==4 and loadout=='balanced' and iteration==0:traces[encounter['id']]=result
                rows.append(aggregate(results,scenario=encounter['id'],category=encounter['category'],squad_size=size,level=10,loadout=loadout,difficulty='medium'))
        print(f"combat {encounter['id']}: {n} battles",flush=True)
    if not quick:
        for encounter in c['encounters']:
            for size in (3,4,5):
                for difficulty in ('easy','hard','extreme'):
                    results=[CombatSimulator(c,base_seed+i).run(make_squad(c,size,10),encounter['enemies'],difficulty) for i in range(max(5,seeds//2))]
                    n+=len(results)
                    rows.append(aggregate(results,scenario=encounter['id'],category=encounter['category'],squad_size=size,level=10,loadout='balanced',difficulty=difficulty))
                for level in (1,20,50):
                    results=[CombatSimulator(c,base_seed+i).run(make_squad(c,size,level),encounter['enemies']) for i in range(max(5,seeds//2))]
                    n+=len(results)
                    rows.append(aggregate(results,scenario=encounter['id'],category=encounter['category'],squad_size=size,level=level,loadout='balanced',difficulty='medium'))
    chains=mission_chains(c,seeds);n+=len(chains)*seeds
    dps,armor,characters=stat_tables(c)
    dump_csv(OUT/'combat_matrix.csv',rows);dump_csv(OUT/'weapon_matchups.csv',dps)
    dump_csv(OUT/'armor_matchups.csv',armor);dump_csv(OUT/'character_stats.csv',characters);dump_csv(OUT/'authored_mission_chains.csv',chains)
    (OUT/'combat_traces.json').write_text(json.dumps(traces,ensure_ascii=False,indent=2),encoding='utf-8')
    findings=[]
    for row in rows:
        if row['level']!=10 or row['difficulty']!='medium' or row['loadout']!='balanced':continue
        low,high={'regular':(15,45),'elite':(15,30),'boss':(60,120)}[row['category']]
        duration=row['win_duration_p50']
        if row['win_rate']<.8:findings.append({'priority':'P1','scenario':row['scenario'],'squad_size':row['squad_size'],'issue':'win_rate_below_80pct','actual':row['win_rate'],'target':'diagnostic threshold; not a design guarantee'})
        if duration is not None and not low<=duration<=high:
            findings.append({'priority':'P2','scenario':row['scenario'],'squad_size':row['squad_size'],'issue':'duration_outside_target','actual':duration,'target':[low,high]})
        if row['category']=='regular' and row['win_hp_loss_mean'] is not None and not .05<=row['win_hp_loss_mean']<=.2:
            findings.append({'priority':'P2','scenario':row['scenario'],'squad_size':row['squad_size'],'issue':'hp_loss_outside_medium_target','actual':row['win_hp_loss_mean'],'target':[.05,.2]})
    payload={'metadata':{'seed':base_seed,'seeds_per_primary_cell':seeds,'python':platform.python_version(),
              'catalog_sha256':hashlib.sha256((ROOT/'simulation/data/combat.json').read_bytes()).hexdigest(),
              'combat_source_sha256':hashlib.sha256((ROOT/'simulation/combat.py').read_bytes()).hexdigest(),
              'source_commit_base':'2aa6a080f8a463bf931023af5a67e08f7f6cd4d7','source_worktree':'locally modified; hashes pin exact inputs',
              'battles':n,'matrix_cells':len(rows),'elapsed_seconds':round(time.perf_counter()-started,2),'mode':'quick' if quick else 'full'},
             'summary':{'health':'CONCERNS' if findings else 'HEALTHY_WITHIN_MODEL','outliers':len(findings),
                        'weapon_matchup_rows':len(dps),'armor_matchup_rows':len(armor),'character_stat_rows':len(characters)},
             'matrix':rows,'authored_chains':chains,'findings':findings,
             'coverage':{'implemented':['fixed0.1s attacks/accuracy/crit','armor/resistance/shield','9baseweapon profiles','6armor archetypes',
                '6role base passives','24enemy archetypes incl timed/threshold abilities','3boss phases/adds/weakpoints/adaptation',
                'target priorities/slot AOE','burn/bio/corrode/EMP/stagger/fear','heal/one field revive/trauma/down/bleedout/wipe',
                'authored room chains with carried HP/consumables','level/tier/armor/DPS sweeps'],
                'not_fully_modeled':['all trait/perk/relationship effects','all Alien/Artifact item mechanics','visual telegraph reactions/navigation',
                   'player learning/manual focus timings','whole-campaign time-to-complete','actual client/backend crash/network behavior'],
                'assumptions':traces[next(iter(traces))]['model_assumptions'] if traces else []}}
    (OUT/'combat_summary.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# Combat Simulation Results','',f"Mode: {payload['metadata']['mode']}; {n:,} battles; seed {base_seed}; {seeds} seeds/primary cell.",
           '', '**Headless model results, not runtime gameplay QA or final balance approval.**',
           '',f"Health: **{payload['summary']['health']}**. {len(findings)} target/diagnostic deviations. Unmodified design baselines; no auto-tuning to force a pass.",
           '', '## Balanced squad, level10, medium', '', '| Encounter | Squad | Win% | 95% CI | Win TTK p50 | Win HP loss | Downs/run | Medkits/run |',
           '|---|---:|---:|---|---:|---:|---:|---:|']
    for r in rows:
        if r['level']==10 and r['difficulty']=='medium' and r['loadout']=='balanced':
            lines.append(f"| {r['scenario']} | {r['squad_size']} | {100*r['win_rate']:.1f} | {r['win_rate_ci95']} | {r['win_duration_p50']} | {r['win_hp_loss_mean']} | {r['downs_mean']} | {r['medkits_mean']} |")
    lines+=['','Win TTK/HP metrics are conditional on victories; all-duration/win rate include failures in CSV/JSON. Small samples have wide confidence intervals.','',
            '## Authored room chains (no reset between rooms)','','| Mission | Win% | Win duration p50 | HP loss mean |','|---|---:|---:|---:|']
    for r in chains:lines.append(f"| {r['scenario']} | {100*r['win_rate']:.1f} | {r['win_duration_p50']} | {r['hp_loss_mean']:.3f} |")
    lines+=['','## Model limitations','']+['- '+x for x in payload['coverage']['not_fully_modeled']]
    lines+=['','See combat_summary.json for source hashes, complete findings and coverage; combat_matrix.csv for every cell; combat_traces.json for17 replayable event logs.','']
    (OUT/'COMBAT_REPORT.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'battles':n,'cells':len(rows),'outliers':len(findings),'seconds':payload['metadata']['elapsed_seconds']}),flush=True)
    return payload

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--seeds',type=int,default=20);parser.add_argument('--seed',type=int,default=20261112);parser.add_argument('--quick',action='store_true')
    args=parser.parse_args()
    if args.seeds<1:parser.error('--seeds must be positive')
    run(args.seeds,args.seed,args.quick)
