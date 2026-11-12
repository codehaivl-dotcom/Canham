"""Fixed-step combat model. Assumptions/unsupported features are reported explicitly."""
from __future__ import annotations

from collections import Counter, deque
from copy import deepcopy
from dataclasses import dataclass, field
import json
from pathlib import Path
import random
import re

DATA = Path(__file__).parent / 'data'
TYPES = ('ballistic', 'energy', 'explosive', 'fire', 'electric', 'bio')
DIFFICULTY = {'easy': .9, 'medium': 1., 'hard': 1.1, 'extreme': 1.18}

def clamp(x, low, high):
    return max(low, min(high, x))

def slug(name):
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

def load_catalog():
    return json.loads((DATA / 'combat.json').read_text(encoding='utf-8'))

def mitigate(raw, armor, resistance, damage_type):
    if raw <= 0:
        return 0.
    armor = max(0., armor)
    effective = armor if damage_type in ('ballistic', 'physical') else armor/2 if damage_type == 'explosive' else 0.
    return round(max(1., raw * 120/(120+effective) * (1-clamp(resistance, -.25, .8))), 2)

def _role(value):
    return slug(value).split('_')[0]

def _formation(value):
    return str(value).lower().split('_')[0]

def _tags(conf,key='traits'):
    values=conf.get(key,[])
    if isinstance(values,str):values=[values]
    if key=='traits' and conf.get('profession_trait_text'):
        values=[*values,conf['profession_trait_text'].split('/')[-1].strip()]
    return {slug(str(v)) for v in values}

def _weapon_mod(weapon, stats, role, formation, enemy=None):
    wid = weapon.get('id', '')
    name = (wid + ' ' + weapon.get('name', '')).lower()
    role = _role(role)
    formation = _formation(formation)
    damage = 1+(stats.get('COM',5)-5)*.03
    speed = 1+(stats.get('AGI',5)-5)*.025
    accuracy = weapon.get('accuracy', .85)+(stats.get('PER',5)-5)*.02
    crit = weapon.get('crit', .05)+max(0,stats.get('PER',5)-5)*.01
    if role == 'assault':
        damage *= 1.08
        speed *= 1.05
    if role == 'scout':
        crit += .05
    if 'smg' in name and formation in ('front','mid'):
        damage *= 1.1
    if 'shotgun' in name and formation == 'front':
        damage *= 1.1
    if 'sniper' in name:
        accuracy += .05 if formation=='back' else -.10 if formation=='front' else 0
        if enemy and (enemy.get('category') in ('elite','boss') or enemy.get('is_boss') or enemy.get('is_elite')):
            damage *= 1.2
    return damage, clamp(speed,.5,2), clamp(accuracy,.55,.98), clamp(crit,0,1)

def expected_weapon_dps(weapon, stats, role='none', formation='mid', enemy=None):
    """Initial direct primary-target DPS, excludes ramp, DOT, AOE and control value."""
    enemy = enemy or {}
    dmg,speed,accuracy,crit = _weapon_mod(weapon,stats,role,formation,enemy)
    dtype=weapon.get('damage_type','ballistic')
    resist=enemy.get('resistances',{}).get(dtype,0)
    base=weapon['damage']*dmg
    # Expected value applies mitigation separately to crit/noncrit (floor/rounding).
    hit=(1-crit)*mitigate(base,enemy.get('armor',0),resist,dtype)+crit*mitigate(base*1.5,enemy.get('armor',0),resist,dtype)
    return hit*accuracy*speed/weapon['interval']

def _key(catalog, group, candidates):
    for c in candidates:
        if c in catalog[group]: return c
    for key,value in catalog[group].items():
        if any(slug(c)==slug(value.get('name','')) for c in candidates): return key
    raise KeyError((group,candidates))

def make_squad(catalog, size=3, level=10, loadout='balanced', tier_multiplier=1.):
    if size not in (1,2,3,4,5): raise ValueError('Squad size must be 1..5')
    roles=['vanguard','assault','medic','engineer','heavy']
    weapons={
        'balanced':['shotgun','assault_rifle','pistol','smg','rocket_launcher'],
        'anti_swarm':['shotgun','flamethrower','assault_rifle','flamethrower','rocket_launcher'],
        'anti_mechanical':['assault_rifle','rocket_launcher','assault_rifle','emp_rifle','rocket_launcher'],
        'energy':['laser_rifle']*5,
        'ballistic':['assault_rifle']*5,
        'fire':['flamethrower']*5,
        'sniper':['sniper_rifle']*5,
    }
    if loadout not in weapons: raise ValueError(f'Unknown loadout {loadout}')
    squad=[]
    for i in range(size):
        role=roles[i]
        stats={k:5 for k in ('COM','END','AGI','PER','INT','TEC','MED','RES')}
        stats.update(COM=6,END=6,PER=6)
        if role=='medic': stats.update(MED=8,COM=4)
        if role=='engineer': stats.update(TEC=8)
        armor=_key(catalog,'armor',['combat_armor'] if i==0 else ['civilian_jacket'])
        weapon=_key(catalog,'weapons',[weapons[loadout][i]])
        squad.append({'id':f'squad_{i+1}','name':role,'role':role,'stats':stats,'level':level,
                      'weapon':weapon,'armor':armor,'formation':['front','mid','back','mid','back'][i],
                      'tier_multiplier':tier_multiplier,'consumables':{'medkit':2,'revival_injector':1} if i==2 else {}})
    return squad

@dataclass
class Entity:
    id: str
    source: str
    side: str
    data: dict
    hp: float
    max_hp: float
    armor: float
    resistances: dict
    formation: str
    role: str = 'none'
    stats: dict = field(default_factory=dict)
    weapon: dict = field(default_factory=dict)
    state: str = 'ACTIVE'
    shield: float = 0.
    next_attack: float = 0.
    attacks: int = 0
    consumables: dict = field(default_factory=dict)
    action: dict | None = None
    item_ready: float = 0.
    medkit_ready: float = 0.
    revive_count: int = 0
    bleedout: float = float('inf')
    controlled_until: float = 0.
    cc_start: float = -100.
    immune_until: float = 0.
    cc_history: dict = field(default_factory=dict)
    statuses: dict = field(default_factory=dict)
    flags: set = field(default_factory=set)
    timers: dict = field(default_factory=dict)
    phase: int = 1
    focus_target: str | None = None
    focus_since: float = 0.
    last_hit: float = -100.
    recent_damage: list = field(default_factory=list)
    damage_dealt: float = 0.
    damage_taken: float = 0.
    healing: float = 0.

    @property
    def active(self): return self.state=='ACTIVE' and self.hp>0

class CombatSimulator:
    def __init__(self,catalog=None,seed=1):
        self.catalog=catalog or load_catalog()
        self.seed=seed

    def log(self,kind,actor=None,target=None,amount=0,**kw):
        self.events.append({'time':round(self.t,2),'kind':kind,'actor':actor.id if isinstance(actor,Entity) else actor,
                            'target':target.id if isinstance(target,Entity) else target,'amount':round(amount,2),**kw})

    def _players(self,squad):
        result=[]
        for i,conf in enumerate(squad):
            s=conf.get('stats',{k:5 for k in ('COM','END','AGI','PER','MED','TEC','RES','INT')})
            role=_role(conf.get('role','none'))
            armor=deepcopy(self.catalog['armor'].get(conf.get('armor'),{})) if isinstance(conf.get('armor'),str) else deepcopy(conf.get('armor',{}))
            weapon=deepcopy(self.catalog['weapons'][conf['weapon']]) if isinstance(conf.get('weapon'),str) else deepcopy(conf['weapon'])
            weapon['damage']*=conf.get('tier_multiplier',1.)
            hp=conf.get('max_hp',(100+s.get('END',5)*12+(conf.get('level',1)-1)*5)*(1.2 if role=='vanguard' else 1))
            traits=_tags(conf)
            if 'tough' in traits: hp*=1.08
            if 'fragile' in traits: hp*=.92
            e=Entity(conf.get('id',f'p{i}'),conf.get('id',f'p{i}'),'player',deepcopy(conf),conf.get('hp',hp),hp,
                     armor.get('armor',0),deepcopy(armor.get('resistances',{})),_formation(conf.get('formation','mid')),
                     role,s,weapon,conf.get('state','ACTIVE'),conf.get('shield',0),
                     consumables=deepcopy(conf.get('consumables',{})),revive_count=conf.get('revive_count',0))
            e.data['armor_speed']=armor.get('attack_speed_multiplier',1.)
            e.data['ballistic_armor_multiplier']=armor.get('effects',{}).get('ballistic_armor_multiplier',1.)
            e.data['trait_tags']=sorted(traits)
            e.data['perk_tags']=sorted(_tags(conf,'perks'))
            if 'shield_module' in _tags(conf,'utilities'):
                e.resistances['energy']=e.resistances.get('energy',0)+.1;e.shield+=e.max_hp*.05
            e.next_attack=self._interval(e)
            if e.state=='DOWN': e.bleedout=60
            result.append(e)
        return result

    def _enemy(self,eid,index):
        data=deepcopy(self.catalog['enemies'][eid])
        hp=data['hp']*self.hp_scale
        role=data.get('role','').lower()
        formation=data.get('formation','back' if any(x in role for x in ('ranged','support','controller')) else 'front')
        e=Entity(f'e{index}_{eid}',eid,'enemy',data,hp,hp,data.get('armor',0),deepcopy(data.get('resistances',{})),formation,
                 role=role,shield=data.get('shield',0)*self.hp_scale)
        e.next_attack=data.get('interval',1)
        return e

    def living(self,side): return [e for e in self.entities if e.side==side and e.active]

    def _interval(self,e):
        if e.side=='player':
            _,speed,_,_=_weapon_mod(e.weapon,e.stats,e.role,e.formation)
            speed*=e.data.get('armor_speed',1.)
            if 'trauma' in e.flags: speed*=.9
            if e.statuses.get('fear',0)>self.t: speed*=.85
            if e.statuses.get('stim',0)>self.t: speed*=1.15
            if 'adrenaline_junkie' in e.data.get('trait_tags',[]) and self.difficulty in ('hard','extreme'):speed*=1.08
            if 'quick_reload' in e.data.get('perk_tags',[]):speed/=.94
            speed*=e.data.get('attack_speed_multiplier',1.)
            return e.weapon['interval']/clamp(speed,.5,2.)
        speed=1.
        if 'hive_mother' in e.source and e.phase==3: speed/= .85
        if 'war_machine' in e.source and e.phase==3: speed*=1.2
        return e.data.get('interval',1.)/speed

    def _target(self,e):
        enemies=self.living('enemy' if e.side=='player' else 'player')
        enemies=[x for x in enemies if x.statuses.get('untargetable',0)<=self.t]
        if not enemies:return None
        if e.side=='player':
            if self.policy=='support_first':
                enemies.sort(key=lambda x:('support' not in x.role,x.hp,x.id))
            else: enemies.sort(key=lambda x:(x.hp,x.id))
            return enemies[0]
        if any(x in e.source for x in ('stalker','phase_hunter')) or ('marksman' in e.source and (e.attacks+1)%3==0):
            back=[x for x in enemies if x.formation=='back']
            return min(back or enemies,key=lambda x:(x.hp,x.id))
        if self.difficulty in ('hard','extreme') and 'rifleman' in e.source:
            return min(enemies,key=lambda x:(x.hp,x.id))
        front=[x for x in enemies if x.formation=='front']
        eligible=front or enemies
        weights=[(1.25 if x.role=='vanguard' else 1)*(1.25 if x.formation=='front' else .8 if x.formation=='back' else 1) for x in eligible]
        return self.rng.choices(eligible,weights=weights,k=1)[0]

    def _damage(self,actor,target,raw,dtype='ballistic',direct=True,critical=False):
        if not target.active or target.statuses.get('untargetable',0)>self.t:return
        armor=target.armor-(10 if target.statuses.get('corrode',0)>self.t else 0)
        if dtype=='ballistic':armor*=target.data.get('ballistic_armor_multiplier',1.)
        if target.statuses.get('weak_point',0)>self.t:armor*=.65
        resistance=target.resistances.get(dtype,0)
        if target.side=='enemy' and dtype=='energy' and any('void_caster' in x.source and x.shield>0 and x.formation==target.formation for x in self.living('enemy')):
            resistance+=.1
        if dtype=='bio' and target.statuses.get('antidote',0)>self.t:resistance+=.3
        if dtype=='rad' and target.statuses.get('rad_protection',0)>self.t:resistance+=.4
        traits=target.data.get('trait_tags',[])
        perks=target.data.get('perk_tags',[])
        if 'reckless' in traits:raw*=1.10
        if 'survivor' in traits and target.hp/target.max_hp<.3:raw*=.90
        if 'hold_line' in perks and target.formation=='front':raw*=.95
        if direct:amount=mitigate(raw,armor,resistance,dtype)
        else:amount=round(max(0,raw*(1-clamp(resistance,-.25,.8))),2)
        shield_before=target.shield
        shield_hit=min(target.shield,amount)
        target.shield-=shield_hit
        hp_hit=min(target.hp,max(0,amount-shield_hit))
        target.hp=max(0,target.hp-hp_hit)
        target.damage_taken+=hp_hit
        target.last_hit=self.t
        if actor:actor.damage_dealt+=hp_hit+shield_hit
        target.data['last_damage_actor']=actor.id if actor else None
        target.recent_damage.append((self.t,dtype,hp_hit+shield_hit))
        self.log('damage',actor,target,hp_hit+shield_hit,damage_type=dtype,hp_damage=round(hp_hit,2),shield_damage=round(shield_hit,2),critical=critical)
        if shield_before>0 and target.shield<=0:
            self.log('shield_break',actor,target)
            if 'void_caster' in target.source:self._cc(target,'stagger',2.)
            if 'war_machine' in target.source and 'first_shield_break' not in target.flags:
                target.flags.add('first_shield_break');target.statuses['weak_point']=self.t+12;target.phase=max(2,target.phase)
        if target.hp<=0:
            if target.side=='player':
                if 'last_wall' in perks and 'last_wall_used' not in target.flags:
                    target.hp=1.;target.flags.add('last_wall_used');self.log('last_wall',actor,target,1);return
                if self.tutorial:
                    target.state='SAFE_DOWN';self.log('safe_down',actor,target)
                elif target.revive_count==0:
                    target.state='DOWN';target.bleedout=self.t+60;self.log('down',actor,target)
                else:
                    target.state='DEAD_RECOVERABLE';self.log('body',actor,target)
            else:
                target.state='DEAD';self.log('enemy_death',actor,target)
                self.death_queue.append(target)
            # Invalidate immediately; no attack from a source killed earlier in the tick.
            # Ready attacks were batched before damage, so their already-fired hits still resolve.

    def _heal(self,actor,target,amount):
        if not target.active:return
        actual=min(max(0,target.max_hp-target.hp),amount)
        target.hp+=actual
        if actor:actor.healing+=actual
        self.log('heal',actor,target,actual)

    def _cc(self,target,kind,duration):
        if not target.active or self.t<target.immune_until:return
        if kind=='stagger':
            if target.role=='vanguard':duration*=.85
            if target.data.get('stagger_resistance',0):duration*=1-target.data['stagger_resistance']
        if target.data.get('category')=='boss' or target.data.get('is_boss'):
            duration*=.4 if kind=='emp' else .35
        if self.t-target.cc_history.get(kind,-100)<8:duration*=.5
        target.cc_history[kind]=self.t
        if self.t>=target.controlled_until:target.cc_start=self.t
        end=min(target.cc_start+4,self.t+max(.1,duration))
        old_control=target.controlled_until
        target.controlled_until=max(target.controlled_until,end)
        # Pause readiness once per newly added duration, not once every update.
        target.next_attack+=max(0,target.controlled_until-max(self.t,old_control))
        self.log('control',None,target,target.controlled_until-self.t,effect=kind)
        if end>=target.cc_start+4-1e-8:target.immune_until=end+2
        if kind=='emp' and target.statuses.get('weak_point',0)>self.t and 'war_machine' in target.source and 'weakpoint_extended' not in target.flags:
            target.flags.add('weakpoint_extended');target.statuses['weak_point']+=3

    def _aoe(self,primary,profile,shape='rocket'):
        pool=[x for x in self.living(primary.side) if x.id!=primary.id and x.statuses.get('untargetable',0)<=self.t]
        rows={'front':0,'mid':1,'back':2}
        pool=[x for x in pool if x.formation==primary.formation or (shape=='rocket' and abs(rows.get(x.formation,1)-rows.get(primary.formation,1))<=1)]
        pool.sort(key=lambda x:(abs(rows.get(x.formation,1)-rows.get(primary.formation,1)),x.id))
        return list(zip([primary]+pool,profile))

    def _attack(self,e,target):
        if e.side=='player':
            w=e.weapon;name=(w.get('id','')+' '+w.get('name','')).lower()
            dmg,speed,acc,crit=_weapon_mod(w,e.stats,e.role,e.formation,target.data)
            if e.statuses.get('jam',0)>self.t:acc-=.1
            if e.statuses.get('fear',0)>self.t:acc-=.0
            if 'sniper' in name and any(x.formation=='front' and self._melee(x) for x in self.living('enemy')):acc-=.10
            if e.role=='scout':
                e.data.setdefault('first_target',target.id)
                if e.data['first_target']==target.id:acc+=.10
            if 'trauma' in e.flags:dmg*=.85
            if e.statuses.get('stim',0)>self.t:dmg*=1.15
            traits=e.data.get('trait_tags',[]);perks=e.data.get('perk_tags',[])
            if 'steady_hands' in traits:acc+=.05
            if 'veteran' in traits:dmg*=1.05;acc+=.05
            if 'reckless' in traits:dmg*=1.05
            if 'pacifist' in traits and target.data.get('family')=='raider':dmg*=.90
            if 'adrenaline_junkie' in traits and self.difficulty in ('hard','extreme'):pass # speed belongs in interval only
            if 'finisher' in perks and target.hp/target.max_hp<.25:dmg*=1.15
            if 'focus_fire' in perks and target.data.get('last_damage_actor') not in (None,e.id):dmg*=1.08
            if 'weak_point' in perks and e.data.get('knowledge_tier') in ('observed','analyzed','researched'):crit+=.08
            if 'laser' in name:
                if e.focus_target!=target.id:e.focus_target=target.id;e.focus_since=self.t
                dmg*=1+min(.20,.04*(self.t-e.focus_since))
            profile=[1]
            shape='cone'
            if 'shotgun' in name:profile=[1,.45,.25]
            elif 'rocket' in name:profile=[1,.60,.45,.30];shape='rocket'
            elif 'flamethrower' in name:profile=[1,.60,.60]
            for victim,factor in self._aoe(target,profile,shape):
                self.total_attacks+=1
                if self.rng.random()>clamp(acc,.55,.98):self.log('miss',e,victim);continue
                if 'rift_hound' in victim.source and self.t>=victim.timers.get('dodge_ready',0) and self.rng.random()<.2:
                    victim.timers['dodge_ready']=self.t+4;self.log('dodge',victim,e);continue
                critical=self.rng.random()<crit
                self._damage(e,victim,w['damage']*dmg*factor*(1.5 if critical else 1),w.get('damage_type','ballistic'),critical=critical)
                if victim.active and 'flamethrower' in name:
                    victim.statuses['burn']=self.t+4;victim.timers.setdefault('burn_tick',self.t+1)
                    victim.data['burn_actor']=e.id
                if victim.active and 'emp' in name and (self._mechanical(victim) or victim.shield>0):
                    count=victim.data.get('buildup',0)+1;victim.data['buildup']=count
                    threshold=3 if self._mechanical(victim) else 4
                    if count>=threshold:
                        victim.data['buildup']=0
                        tech=(1+(e.stats.get('TEC',5)-5)*.05)*(1.2 if e.role=='engineer' else 1)
                        if 'emp_expert' in perks:tech*=1.15
                        self._cc(victim,'emp',2.5*tech)
                if victim.active and 'rocket' in name:self._cc(victim,'stagger',.5*(1.15 if e.role=='heavy' else 1))
        else:
            acc=e.data.get('accuracy',.85)
            if e.statuses.get('smoke',0)>self.t:acc-=.2
            if self.rng.random()>clamp(acc,.55,.98):self.log('miss',e,target)
            else:
                dmg=e.data['damage']*self.damage_scale
                crit=e.data.get('crit',.05)
                if 'breacher' in e.source and e.attacks==0:dmg*=1.25
                if 'stalker' in e.source and e.attacks==0:dmg*=1.20
                if 'marksman' in e.source and (e.attacks+1)%3==0:crit+=.15
                if 'phase_hunter' in e.source and e.statuses.get('marked',0)>self.t:dmg*=1.15
                critical=self.rng.random()<crit
                self._damage(e,target,dmg*(1.5 if critical else 1),e.data.get('damage_type','ballistic'),critical=critical)
                if target.active and 'spitter' in e.source and self.rng.random()<.2:target.statuses['corrode']=self.t+6
        e.attacks+=1

    @staticmethod
    def _mechanical(e):
        return e.data.get('family','').lower() in ('mechanical','robot') or any(x in e.source for x in ('drone','bot','turret','mech','war_machine'))

    @staticmethod
    def _melee(e):
        return any(x in e.source for x in ('crawler','brute','bloated','stalker','hound','crystal','hunter','breacher'))

    def _due(self,e,key,interval):
        if self.t+1e-8<e.timers.get(key,interval):return False
        e.timers[key]=self.t+interval
        return True

    def _spawn(self,source,actor):
        if source not in self.catalog['enemies']:
            self.unsupported.add(f'spawn_catalog:{source}');return
        if len(self.living('enemy'))>=self.active_cap:
            self.log('spawn_skipped',actor,None,reason='active_cap');return
        self.spawn_serial+=1
        e=self._enemy(source,self.spawn_serial+100)
        e.next_attack=self.t+e.data['interval']
        self.entities.append(e);self.log('spawn',actor,e)
        self.max_active_enemies=max(self.max_active_enemies,len(self.living('enemy')))

    def _ability(self,e):
        if not e.active or self.t<e.controlled_until:return
        eid=e.source
        ratio=e.hp/e.max_hp
        players=self.living('player')
        if not players:return
        if 'bloated' in eid:return
        if 'hive_carrier' in eid:
            for threshold,num in ((.65,1),(.30,2)):
                key=f'brood{threshold}'
                if ratio<=threshold and key not in e.flags:
                    e.flags.add(key)
                    for _ in range(num):self._spawn('crawler',e)
        if 'repair_drone' in eid:
            if self._due(e,'repair',8):e.statuses['repair_beam']=self.t+3;e.timers['repair_tick']=self.t+1
            if e.statuses.get('repair_beam',0)>=self.t and self._due(e,'repair_tick',1):
                allies=[x for x in self.living('enemy') if x.id!=e.id and self._mechanical(x)]
                if allies:self._heal(e,min(allies,key=lambda x:(x.hp/x.max_hp,x.id)),18)
        if 'mutated_brute' in eid and self._due(e,'slam',8):
            target=self._target(e)
            if target:self._damage(e,target,26*self.damage_scale)
        if 'tech_raider' in eid:
            if self._due(e,'jam',10):
                for p in players:p.statuses['jam']=self.t+5
                self.log('jam',e)
            if 'shield_drone' not in e.flags:
                allies=[x for x in self.living('enemy') if x.hp<x.max_hp]
                if allies:
                    e.flags.add('shield_drone');victim=min(allies,key=lambda x:(x.hp,x.id));victim.shield+=50
                    self.log('shield_grant',e,victim,50)
        if 'spore_weaver' in eid and self._due(e,'spore',9):
            for p in players:p.statuses['spore']=self.t+6;p.timers.setdefault('spore_tick',self.t+1);p.data['spore_actor']=e.id
        if 'alpha_brute' in eid:
            if self._due(e,'roar',14):
                for p in players:
                    chance=clamp(.5+(p.stats.get('RES',5)-5)*.05,.25,.9)
                    if 'calm' in p.data.get('trait_tags',[]):chance=min(.95,chance+.15)
                    if 'nervous' in p.data.get('trait_tags',[]):chance=max(0,chance-.15)
                    if 'steady_resolve' in p.data.get('perk_tags',[]):chance=min(.95,chance+.05)
                    if self.rng.random()>chance:p.statuses['fear']=self.t+5
                self.log('roar',e)
            if self._due(e,'slam',9):
                for p in players:
                    if p.formation in ('front','mid'):self._damage(e,p,35*self.damage_scale)
        if 'warden_mech' in eid and self.t-e.last_hit>=5 and self._due(e,'shield_regen',5):
            old=e.shield;e.shield=min(e.data.get('shield',220)*self.hp_scale,e.shield+80)
            self.log('shield_regen',e,e,e.shield-old)
        if 'phase_hunter' in eid:
            if self._due(e,'phase',10):
                e.statuses['untargetable']=self.t+1.2;e.statuses['marked']=self.t+7.2;e.next_attack=max(e.next_attack,self.t+1.2)
                self.log('phase',e)
        if 'hive_mother' in eid:
            phase=1 if ratio>.7 else 2 if ratio>.35 else 3
            if phase!=e.phase:
                e.phase=phase;e.timers['boss_spawn']=self.t+18;self.log('boss_phase',e,None,phase=phase)
            if e.phase in (1,2) and e.data.get('spawn_waves',0)<3 and self._due(e,'boss_spawn',18):
                e.data['spawn_waves']=e.data.get('spawn_waves',0)+1
                for add in (['crawler','crawler'] if e.phase==1 else ['spitter','crawler']):self._spawn(add,e)
            if e.phase==2 and self._due(e,'zone',12):
                for p in players:p.statuses['spore']=self.t+6;p.timers.setdefault('spore_tick',self.t+1);p.data['spore_actor']=e.id
            if e.phase==3 and self._due(e,'slam',8):
                for p in players:
                    if p.formation in ('front','mid'):self._damage(e,p,35*self.damage_scale)
        if 'war_machine' in eid:
            if ratio<=.75 and 'repair_spawn' not in e.flags:e.flags.add('repair_spawn');self._spawn('repair_drone',e)
            if ratio<.35 and e.phase!=3:e.phase=3;e.resistances['fire']=.4;self.log('boss_phase',e,None,phase=3)
            if e.phase==3 and self._due(e,'pulse',10):
                for p in players:self._damage(e,p,6*self.damage_scale,'fire')
        if 'fallen_visitor' in eid:
            if ratio<=.5 and 'phase_shift' not in e.flags:
                e.flags.add('phase_shift');e.phase=2;e.shield+=250
                for _ in range(2):self._spawn('stalker',e)
                self.log('boss_phase',e,None,phase=2)
            if self._due(e,'adapt',20):
                totals=Counter()
                e.recent_damage=[x for x in e.recent_damage if x[0]>self.t-20]
                for _,dtype,amount in e.recent_damage:totals[dtype]+=amount
                if totals:
                    dominant=sorted(totals,key=lambda k:(-totals[k],k))[0]
                    other=self.rng.choice([x for x in TYPES if x!=dominant])
                    e.resistances[dominant]=clamp(e.resistances.get(dominant,0)+.2,-.25,.8)
                    e.resistances[other]=clamp(e.resistances.get(other,0)-.15,-.25,.8)
                    self.log('adapt',e,None,resistances=deepcopy(e.resistances))

    def _items(self,e):
        if e.action or not e.active or self.t<e.item_ready or self.t<e.controlled_until:return
        players=self.living('player')
        down=[p for p in self.entities if p.side=='player' and p.state=='DOWN' and p.revive_count==0]
        if down and e.consumables.get('revival_injector',0)>0:
            e.action={'kind':'revival_injector','target':min(down,key=lambda p:(p.bleedout,p.id)).id,'end':self.t+3*(.75 if e.role=='medic' else 1)}
        elif e.consumables.get('medkit',0)>0 and self.t>=e.medkit_ready:
            hurt=[p for p in players if p.hp/p.max_hp<=.55]
            if hurt:e.action={'kind':'medkit','target':min(hurt,key=lambda p:(p.hp/p.max_hp,p.id)).id,'end':self.t+2}
        elif self.item_policy=='aggressive':
            enemies=self.living('enemy')
            target=self._target(e)
            for item in ('emp_grenade','frag_grenade','combat_stim','smoke_charge','antidote'):
                if e.consumables.get(item,0)<=0 or not target:continue
                if item=='emp_grenade' and not any(self._mechanical(x) for x in enemies):continue
                if item=='frag_grenade' and len(enemies)<2:continue
                if item=='combat_stim' and e.statuses.get('stim',0)>self.t:continue
                if item=='antidote' and not (e.statuses.get('spore',0)>self.t or e.statuses.get('poison',0)>self.t):continue
                e.action={'kind':item,'target':e.id if item in ('combat_stim','antidote') else target.id,'end':self.t+1};break
        if e.action:self.log('item_start',e,e.action['target'],item=e.action['kind'])

    def _complete_item(self,e):
        if not e.action:return
        action=e.action
        if not e.active:
            self.log('item_cancel',e,action['target'],item=action['kind']);e.action=None;return
        if self.t<e.controlled_until:
            action['end']+=.1
            return
        if self.t+1e-8<action['end']:return
        target=next((x for x in self.entities if x.id==action['target']),None)
        item=action['kind']
        e.action=None
        valid=target and ((item=='revival_injector' and target.state=='DOWN' and target.revive_count==0 and self.t<target.bleedout) or (item!='revival_injector' and target.active))
        if not valid:self.log('item_cancel',e,action['target'],item=item);return
        e.consumables[item]-=1;self.items_used[item]+=1;e.item_ready=self.t+2
        if item=='revival_injector':
            target.state='ACTIVE';target.hp=target.max_hp*(.4 if e.role=='medic' else .3);target.revive_count+=1;target.flags.add('trauma');target.next_attack=self.t+self._interval(target)
            self.log('revive',e,target,target.hp)
        elif item=='medkit':
            power=.35*target.max_hp*(1+(e.stats.get('MED',5)-5)*.05)*(1.25 if e.role=='medic' else 1)
            if 'field_medic' in e.data.get('trait_tags',[]):power*=1.20
            self._heal(e,target,power);e.medkit_ready=self.t+5
        elif item in ('frag_grenade','emp_grenade'):
            dtype='explosive' if item=='frag_grenade' else 'electric'
            for victim,factor in self._aoe(target,[1,.6,.45,.3],'rocket'):
                self._damage(e,victim,(55 if item=='frag_grenade' else 20)*factor,dtype)
                if item=='emp_grenade' and victim.active and self._mechanical(victim):
                    duration=4 if 'sentry_drone' in victim.source else 3
                    duration*=(1+(e.stats.get('TEC',5)-5)*.05)*(1.2 if e.role=='engineer' else 1)
                    self._cc(victim,'emp',duration)
        elif item=='combat_stim':target.statuses['stim']=self.t+15
        elif item=='smoke_charge':
            for enemy in self.living('enemy'):enemy.statuses['smoke']=self.t+8
        elif item=='antidote':
            target.statuses['poison']=0;target.statuses['spore']=0;target.statuses['antidote']=self.t+20
        self.log('item_complete',e,target,item=item)

    def run(self,squad,enemies,difficulty='medium',max_seconds=240,policy='auto',enable_consumables=True,overrides=None):
        if difficulty not in DIFFICULTY:raise ValueError(difficulty)
        overrides=overrides or {}
        self.rng=random.Random(self.seed);self.t=0.;self.entities=[];self.events=[];self.death_queue=deque()
        self.items_used=Counter();self.total_attacks=0;self.spawn_serial=0;self.unsupported=set()
        self.policy=policy;self.difficulty=difficulty;self.tutorial=overrides.get('tutorial_protected',False)
        self.item_policy=overrides.get('item_policy','healing')
        self.hp_scale=overrides.get('enemy_hp_multiplier',DIFFICULTY[difficulty])
        self.damage_scale=overrides.get('enemy_damage_multiplier',DIFFICULTY[difficulty])
        self.active_cap=overrides.get('active_enemy_cap',8 if len(enemies)>6 or any('mother' in x or 'visitor' in x or 'war_machine' in x for x in enemies) else 6)
        if len(enemies)>self.active_cap:raise ValueError('Initial active enemies exceed room cap; author waves explicitly')
        self.entities=self._players(deepcopy(squad))+[self._enemy(eid,i) for i,eid in enumerate(enemies)]
        self.initial_hp=sum(e.max_hp for e in self.entities if e.side=='player')
        self.max_active_enemies=len(enemies)
        outcome='timeout'
        ticks=int(max_seconds*10)+1
        for tick in range(ticks):
            self.t=round(tick/10,1)
            # Transient DOT and bleedout before this tick's new ready attacks.
            for e in list(self.entities):
                if e.state=='DOWN' and self.t>=e.bleedout:e.state='DEAD_RECOVERABLE';self.log('bleedout',None,e)
                if not e.active:continue
                for status,dtype,raw in (('burn','fire',3),('spore','bio',4),('poison','bio',4)):
                    if e.statuses.get(status,0)>=self.t and status in e.statuses and self._due(e,status+'_tick',1):
                        actor=next((x for x in self.entities if x.id==e.data.get(status+'_actor')),None)
                        self._damage(actor,e,raw*(self.damage_scale if status=='spore' else 1),dtype,direct=False)
            for e in list(self.entities):
                if e.side=='enemy':self._ability(e)
            # Snapshot ready attackers so simultaneously fired shots still land on a dead source's tick.
            ready=[]
            for e in list(self.entities):
                if not e.active or self.t<e.controlled_until:continue
                if e.side=='enemy' and e.statuses.get('repair_beam',0)>self.t:
                    e.next_attack+=.1
                    continue
                if e.side=='player' and enable_consumables:self._items(e)
                if e.action:
                    e.next_attack+=.1
                    continue
                if self.t+1e-8>=e.next_attack:
                    target=self._target(e)
                    if target:ready.append((e,target));e.next_attack+=self._interval(e)
            for e,target in ready:
                if target.active:self._attack(e,target)
            while self.death_queue:
                dead=self.death_queue.popleft()
                if 'bloated' in dead.source:
                    for p in self.living('player'):
                        if p.formation=='front':self._damage(dead,p,22*self.damage_scale,'bio')
            for e in self.entities:
                if e.side=='player':self._complete_item(e)
            if not self.living('player'):
                outcome='protected_return' if self.tutorial else 'wipe';break
            if not self.living('enemy'):
                outcome='victory';break
        players=[e for e in self.entities if e.side=='player']
        # Room outcome is not extraction: never silently convert DOWN into a permanent loss on victory.
        survivors=[{'id':e.id,'hp':round(e.hp,2),'max_hp':round(e.max_hp,2),'state':e.state,'revive_count':e.revive_count,
                    'trauma':'trauma' in e.flags,'consumables':e.consumables,'damage_dealt':round(e.damage_dealt,2),'healing':round(e.healing,2)} for e in players]
        return {'seed':self.seed,'outcome':outcome,'victory':outcome=='victory','duration':self.t,
                'hp_loss_fraction':round(1-sum(e.hp for e in players)/max(1,self.initial_hp),6),
                'downs':sum(x['kind']=='down' for x in self.events),'revives':sum(e.revive_count for e in players),
                'new_revives':sum(x['kind']=='revive' for x in self.events),'items_used':dict(self.items_used),
                'survivors':survivors,'enemies':[{'id':e.id,'source':e.source,'hp':round(e.hp,2),'state':e.state,'shield':round(e.shield,2),'phase':e.phase,'resistances':e.resistances} for e in self.entities if e.side=='enemy'],
                'max_active_enemies':self.max_active_enemies,'events':self.events,
                'unsupported':sorted(self.unsupported | {'unconfigured_trait_perk_relationship_effects','alien_artifact_unique_mechanics','navigation_and_human_telegraph_reactions'}),
                'model_assumptions':['Unspecified enemy base accuracy/crit default to0.85/0.05; see data provenance.',
                                     'Room-based slots approximate spatial range; no NavMesh or animation timing.',
                                     'Automated consumable policy is a test controller, not promised player skill.',
                                     'War Machine weak-point EMP extension is limited to one +3s extension per exposure window (ambiguous in source).',
                                     'Generic squads omit trainable perks/relationship/morale/Alien gear effects unless explicitly configured.']}
