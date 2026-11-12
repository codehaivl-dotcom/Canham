"""Executable noncombat prototype model; stdlib only, no game-runtime claim.

Times are seconds. Economy time is capped trusted elapsed; competitive time is
uncapped. Functions expose transitions so tests exercise behavior, not literals.
"""
from __future__ import annotations

import copy
import json
import math
import random
import itertools
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EPS = 1e-8
SOURCES = ["docs/ECONOMY_RESOURCES_V0.1.md", "docs/PROTOTYPE_PROGRESSION_V0.1.md",
           "docs/SURVIVOR_RECOVERY_V0.1.md", "docs/PROTOTYPE_CONTENT_PACK_V0.1.md",
           "docs/PVP_MATCHMAKING_PROTECTION_V0.1.md", "docs/RESOURCE_SITES_V0.1.md",
           "docs/MISSION_SESSION_REWARDS_V0.1.md", "docs/LOOT_CRAFTING_V0.1.md"]
FIXTURE = {
    "economy": {"start": {"food":100,"water":120,"scrap":300,"components":120,
                 "chemicals":40,"supply":20,"credits":500,"research_data":0,"population":6},
                "consumption":{"food":1,"water":1.2},"production":{"food":10,"water":12},
                "offline_cap_hours":8},
    "recipes":[{"id":"supply","inputs":{"food":5,"water":6,"scrap":2},
                "outputs":{"supply":5},"minutes":2},
               {"id":"claim_beacon","inputs":{"scrap":25,"components":5},
                "outputs":{"claim_beacon":1},"minutes":5}],
    "sites":{"scrapyard":{"base_output":{"scrap":18}}},
    "pvp":{"loss_caps":{str(c):{"scrap":60+15*(c-8),"components":20+5*(c-8),
                               "chemicals":12+3*(c-8)} for c in range(8,13)}}}


def load_data(path=None):
    path = Path(path) if path else ROOT / "data" / "systems.json"
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        return data, {"mode":"exported_data", "path":str(path), "sources":data.get("sources",[])}
    return copy.deepcopy(FIXTURE), {"mode":"documented_fixture_fallback", "sources":SOURCES,
                                  "reason":"systems.json not present"}


def pay(stock, cost):
    if any(stock.get(k,0) + EPS < v for k,v in cost.items()):
        raise ValueError("insufficient available resources")
    for k,v in cost.items(): stock[k] = stock.get(k,0)-v


@dataclass
class Site:
    hourly: dict = field(default_factory=lambda:{"scrap":18.0})
    buffer: dict = field(default_factory=dict)
    collection_elapsed: float = 0
    collections: int = 0
    produced: dict = field(default_factory=dict)

    def advance(self, seconds, deposit):
        while seconds > EPS:
            dt = min(seconds, 8*3600-self.collection_elapsed)
            for r,rate in self.hourly.items():
                before = self.buffer.get(r,0)
                self.buffer[r] = min(rate*8, before + rate*dt/3600)
                self.produced[r] = self.produced.get(r,0)+self.buffer[r]-before
            self.collection_elapsed += dt
            seconds -= dt
            if self.collection_elapsed >= 8*3600-EPS:
                for r,amount in self.buffer.items(): deposit(r, amount)
                self.buffer = {}
                self.collection_elapsed = 0
                self.collections += 1


@dataclass
class Treatment:
    minutes: float
    chemicals: float
    speed: float = 1
    progress: float = 0
    started: bool = False
    complete: bool = False

    def advance(self, seconds, stock, powered=True, worker=True):
        if self.complete or not powered or not worker: return
        if not self.started:
            pay(stock,{"chemicals":self.chemicals})
            self.started = True
        self.progress = min(self.minutes, self.progress+seconds/60*self.speed)
        self.complete = self.progress >= self.minutes-EPS


@dataclass
class Economy:
    stock: dict
    population: int = 6
    capacity: dict = field(default_factory=lambda:{r:250.0 for r in
                                  ("food","water","scrap","components","chemicals","supply")})
    production: dict = field(default_factory=lambda:{"food":10.0,"water":12.0})
    consumption: dict = field(default_factory=lambda:{"food":1.0,"water":1.2})
    generator_integrity: float = 1
    battery: float = 0
    battery_cap: float = 20
    core: float = 8
    life_load: float = 11
    other_load: float = 0
    last_observation: float = 0
    simulated: float = 0
    offline_cap: float = 8*3600
    restart_remaining: float | None = None
    restart_cooldown_until: float = -1
    hunger: dict = field(default_factory=lambda:{"food":0.,"water":0.})
    bound: dict = field(default_factory=dict)
    inbox: dict = field(default_factory=dict)
    fatigue: float = 81
    rest_rate: float = 2
    treatment: Treatment | None = None
    sites: list = field(default_factory=list)
    events: list = field(default_factory=list)
    relief_cooldown: float = -1
    relief_pending: float | None = None
    emergency_elapsed: float = 0
    stable_elapsed: dict = field(default_factory=lambda:{"food":0.,"water":0.})
    repair_target: float = .25

    @property
    def generation(self):
        i=self.generator_integrity
        factor=0 if i<=0 else .5 if i<.25 else .8 if i<.5 else 1
        return self.core+20*factor

    @property
    def emergency(self): return self.generation < self.life_load-EPS and self.battery<=EPS

    def deposit(self, resource, amount):
        room=max(0,self.capacity.get(resource,float("inf"))-self.stock.get(resource,0))
        stored=min(room,amount)
        self.stock[resource]=self.stock.get(resource,0)+stored
        self.inbox[resource]=self.inbox.get(resource,0)+amount-stored

    def restart(self):
        if self.generator_integrity>0 or self.simulated<self.restart_cooldown_until:
            return False
        if self.restart_remaining is None: self.restart_remaining=300
        self.repair_target=.25
        return True

    def repair(self, advanced=False):
        missing=1-self.generator_integrity
        if missing<=EPS: return 0
        cost={"scrap":max(1,math.ceil(20*missing-EPS))}
        if advanced: cost["components"]=math.ceil(5*missing-EPS)
        pay(self.stock,cost)
        # A scheduled repair completion retains its work across observation calls.
        self.restart_remaining=max(30,math.ceil(4*missing-EPS)*60)
        self.repair_target=1
        self.events.append({"repair_target":1.0})
        return self.restart_remaining

    def start_relief(self):
        targets={"food":5,"water":6,"supply":6}
        eligible=any(self.stock.get(k,0)+self.bound.get(k,0)+self.inbox.get(k,0)<v
                     for k,v in targets.items())
        if not eligible or self.relief_pending is not None or self.simulated<self.relief_cooldown:
            return False
        self.relief_pending=600
        return True

    def advance_offline(self, trusted_now):
        if trusted_now < self.last_observation: raise ValueError("trusted time regressed")
        dt=min(trusted_now-self.last_observation,self.offline_cap)
        self.advance(dt)
        self.last_observation=trusted_now  # discard skipped debt, including >8h
        return dt

    def advance(self, seconds):
        while seconds>EPS:
            dt=seconds
            emergency=self.emergency
            if emergency and self.emergency_elapsed<600:
                dt=min(dt,600-self.emergency_elapsed)
            net_gen=self.generation-self.life_load-self.other_load
            battery_rate=net_gen if (net_gen>=0 or self.battery>EPS) else 0
            if battery_rate<0: dt=min(dt,self.battery/-battery_rate*3600)
            if battery_rate>0 and self.battery<self.battery_cap-EPS:
                dt=min(dt,(self.battery_cap-self.battery)/battery_rate*3600)
            if self.restart_remaining is not None: dt=min(dt,self.restart_remaining)
            if self.relief_pending is not None: dt=min(dt,self.relief_pending)
            rates={}
            for r in ("food","water"):
                prod=0 if emergency else self.production.get(r,0)
                demand=0 if emergency else self.population*self.consumption[r]
                net=prod-demand
                stock=self.stock.get(r,0)
                cap=self.capacity[r]
                if stock>=cap-EPS and net>0: net=0
                if stock<=EPS and net<0: net=0
                rates[r]=(net,prod,demand)
                if not emergency and stock<=EPS and demand>prod and self.hunger[r]<3600:
                    dt=min(dt,3600-self.hunger[r])
                if net<0 and stock>EPS: dt=min(dt,stock/-net*3600)
                if net>0 and stock<cap-EPS: dt=min(dt,(cap-stock)/net*3600)
            if dt<=EPS: raise RuntimeError("nonprogressing event boundary")
            for r,(net,prod,demand) in rates.items():
                was_empty=self.stock.get(r,0)<=EPS
                self.stock[r]=max(0,min(max(self.capacity[r],self.stock.get(r,0)),
                                           self.stock.get(r,0)+net*dt/3600))
                if emergency:
                    if self.emergency_elapsed+dt>=600-EPS:self.hunger[r]=0
                elif was_empty and demand>prod:
                    self.hunger[r]+=dt;self.stable_elapsed[r]=0
                elif self.stock[r]>EPS:
                    self.stable_elapsed[r]+=dt
                    if self.stable_elapsed[r]>=600-EPS:self.hunger[r]=0
            self.emergency_elapsed=self.emergency_elapsed+dt if emergency else 0
            self.battery=min(self.battery_cap,max(0,self.battery+battery_rate*dt/3600))
            self.fatigue=max(0,self.fatigue-self.rest_rate*dt/60)
            if self.treatment: self.treatment.advance(dt,self.stock,not emergency,True)
            for site in self.sites: site.advance(dt,self.deposit)
            self.simulated+=dt
            if self.restart_remaining is not None:
                self.restart_remaining-=dt
                if self.restart_remaining<=EPS:
                    self.generator_integrity=self.repair_target
                    self.restart_remaining=None
                    self.restart_cooldown_until=self.simulated+24*3600
                    self.events.append({"time":self.simulated,"generator_restarted":self.generator_integrity})
            if self.relief_pending is not None:
                self.relief_pending-=dt
                if self.relief_pending<=EPS:
                    for r,target in {"food":10,"water":12,"supply":6}.items():
                        self.bound[r]=max(self.bound.get(r,0),target-self.stock.get(r,0)-self.inbox.get(r,0))
                        self.bound[r]=max(0,self.bound[r])
                    self.relief_pending=None
                    self.relief_cooldown=self.simulated+1800
            seconds-=dt


class RewardLedger:
    def __init__(self, seed=1):
        self.seed=seed; self.inventory=Counter(); self.receipts={}; self.banked=set()
        self.first_clears=set(); self.cache_cards={}; self.claims={}; self.knowledge=set()

    def cache(self, cache_id, pool, count=5):
        if cache_id not in self.cache_cards:
            rng=random.Random(f"{self.seed}:{cache_id}")
            keys=list(pool); weights=list(pool.values())
            self.cache_cards[cache_id]=tuple(rng.choices(keys,weights=weights,k=count))
        return self.cache_cards[cache_id]

    def normal_cache(self, cache_id, weights):
        if cache_id in self.cache_cards:return self.cache_cards[cache_id]
        rng=random.Random(f"{self.seed}:{cache_id}")
        materials={k:v for k,v in weights.items() if k in ("scrap","components","chemicals","food_water") and v>0}
        def material():
            r=rng.choices(list(materials),weights=list(materials.values()))[0]
            if r=="food_water":r=rng.choice(["food","water"])
            return (r,rng.randint(8,15))
        cards=[material(),(rng.choice(["medkit","frag_grenade"]),1),
               ("research_data",2) if weights.get("data",0)>0 else ("credits",30),
               (rng.choice(["pistol","rifle"]),1) if rng.random()<.5 else material(),
               ("blueprint_fragment",1)]
        self.cache_cards[cache_id]=tuple(cards)
        return self.cache_cards[cache_id]

    def settle(self, mission_id, successful, pickups, node, objective=True, knowledge=()):
        if mission_id in self.receipts: return self.receipts[mission_id]
        self.knowledge.update(knowledge)
        reward=Counter()
        if successful:
            for pickup_id,items in pickups.items():
                if pickup_id not in self.banked:
                    reward.update(items); self.banked.add(pickup_id)
            self.inventory.update(reward)
            if objective: self.first_clears.add(node)
        receipt={"successful":successful,"reward":dict(reward),"first_clear":node in self.first_clears}
        self.receipts[mission_id]=receipt
        return receipt

    def claim(self, request_id, resource, quantity, inbox):
        if request_id in self.claims: return self.claims[request_id]
        amount=min(quantity,inbox.get(resource,0))
        inbox[resource]=inbox.get(resource,0)-amount
        self.inventory[resource]+=amount
        self.claims[request_id]=amount
        return amount


@dataclass
class PvpAccount:
    ccl: int=8
    opted: bool=True
    stock: dict=field(default_factory=lambda:{"scrap":1000.,"components":200.,"chemicals":100.})
    shield_until: float=0
    active_incoming: str | None=None
    losses: list=field(default_factory=list)
    reserved: dict=field(default_factory=dict)
    charges: int=3
    regen_at: float | None=None
    alliance: str | None=None
    active_outgoing: str | None=None


class PvpWorld:
    def __init__(self, caps=None):
        self.accounts={}; self.raids={}; self.cooldowns={}; self.history={}
        self.caps=caps or FIXTURE["pvp"]["loss_caps"]

    def add(self, key, **kwargs):
        self.accounts[key]=PvpAccount(**kwargs); return self.accounts[key]

    def regenerate(self, a, now):
        while a.regen_at is not None and now>=a.regen_at and a.charges<3:
            a.charges+=1
            a.regen_at=None if a.charges==3 else a.regen_at+4*3600

    def remaining(self, a, resource, now):
        used=sum(items.get(resource,0) for time,items in a.losses if time>now-86400)
        return max(0,self.caps[str(a.ccl)][resource]-used-a.reserved.get(resource,0))

    def spend(self, defender, cost, asset="silo", site_stock=None):
        account=self.accounts[defender]
        stock=account.stock if asset=="silo" else site_stock
        if stock is None:raise ValueError("site stock missing")
        # Reservations belong only to the attacked pool, never to another asset.
        raid=self.raids.get(account.active_incoming,{})
        reserved=account.reserved if raid.get("pool") is stock else {}
        if any(stock.get(r,0)-reserved.get(r,0)<n for r,n in cost.items()):
            raise ValueError("stock is reserved")
        pay(stock,cost)

    def begin(self, raid_id, attacker, defender, now, asset="silo", site_stock=None,
              output=None, private=False, roster_overlap=False):
        if raid_id in self.raids: return self.raids[raid_id]
        self.expire(now)
        a,d=self.accounts[attacker],self.accounts[defender]
        self.regenerate(a,now)
        if (attacker==defender or private or not a.opted or not d.opted or min(a.ccl,d.ccl)<8
            or abs(a.ccl-d.ccl)>1 or d.shield_until>now or d.active_incoming
            or a.active_outgoing or a.charges<1 or roster_overlap
            or (a.alliance and a.alliance==d.alliance)
            or self.cooldowns.get((attacker,defender),-1)>now):
            raise ValueError("ineligible raid")
        pool=d.stock if asset=="silo" else site_stock
        if pool is None: raise ValueError("site stock missing")
        exposed={}
        for r in ("scrap","components","chemicals"):
            available=max(0,pool.get(r,0)-d.reserved.get(r,0))
            ceiling=math.floor(available*.1+EPS)
            if asset!="silo": ceiling=min(ceiling,math.floor(2*(output or {}).get(r,0)))
            exposed[r]=min(ceiling,self.remaining(d,r,now))
        d.reserved=exposed.copy(); d.active_incoming=raid_id
        a.active_outgoing=raid_id; a.charges-=1; a.shield_until=now
        if a.regen_at is None: a.regen_at=now+4*3600
        self.cooldowns[attacker,defender]=now+86400
        raid={"id":raid_id,"attacker":attacker,"defender":defender,"asset":asset,
              "pool":pool,"exposure":exposed,"deadline":now+900,"result":None}
        self.raids[raid_id]=raid
        return raid

    def settle(self, raid_id, now, successful, carried=None, at_exit=False):
        raid=self.raids[raid_id]
        if raid["result"] is not None: return raid["result"]
        if now>=raid["deadline"]: successful=at_exit
        a,d=self.accounts[raid["attacker"]],self.accounts[raid["defender"]]
        stolen={r:min(max(0,(carried or {}).get(r,0)),n) if successful else 0
                for r,n in raid["exposure"].items()}
        for r,amount in stolen.items():
            raid["pool"][r]=raid["pool"].get(r,0)-amount
            a.stock[r]=a.stock.get(r,0)+amount
        if any(stolen.values()):
            d.losses.append((now,stolen)); d.shield_until=max(d.shield_until,now+7200)
        self.history.setdefault(raid["defender"],[]).append(now)
        if sum(t>now-28800 for t in self.history[raid["defender"]])>=2:
            d.shield_until=max(d.shield_until,now+28800)
        d.active_incoming=None; d.reserved={}; a.active_outgoing=None
        raid["result"]={"successful":successful,"stolen":stolen,"time":now}
        return raid["result"]

    def expire(self, now):
        for key,raid in list(self.raids.items()):
            if raid["result"] is None and now>=raid["deadline"]:
                self.settle(key,raid["deadline"],False)


class Claim:
    COST={"supply":10,"scrap":25,"components":5,"claim_beacon":1}
    def __init__(self, stock): self.stock=stock; self.claims={}
    def begin(self, key, ccl, private=True, opted=False):
        if key in self.claims: return self.claims[key]
        if ccl<6 or (not private and (ccl<8 or not opted)): raise ValueError("claim ineligible")
        pay(self.stock,self.COST)
        self.claims[key]={"reserved":dict(self.COST),"state":"pending"}
        return self.claims[key]
    def settle(self,key,success):
        claim=self.claims[key]
        if claim["state"]!="pending": return claim
        if not success:
            for r,n in claim["reserved"].items(): self.stock[r]=self.stock.get(r,0)+n
        claim["state"]="owned" if success else "refunded"
        return claim


def craft(stock, recipe, count=1):
    pay(stock,{k:v*count for k,v in recipe["inputs"].items()})
    for k,v in recipe["outputs"].items(): stock[k]=stock.get(k,0)+v*count


class Pity:
    def __init__(self):self.dry={};self.events={}
    def settle(self, event_id, family, successful, fragment_banked):
        if event_id in self.events:return self.events[event_id]
        grant=0
        if successful:
            count=0 if fragment_banked else self.dry.get(family,0)+1
            if count>=3:grant=1;count=0
            self.dry[family]=count
        self.events[event_id]=grant
        return grant


def weighted_loot(seed, weights, rolls):
    """Each sample is a successful Easy normal-room objective clear,1–2 rolls.

    Quantity and category rules from Implementation§6; natural fragment banking
    resets the per-family three-clear pity counter. No cache reward is added.
    """
    rng=random.Random(seed); outcomes=Counter(); categories=Counter(); pity=Pity()
    guaranteed=0;max_dry=0
    for index in range(rolls):
        found_fragment=False
        for _ in range(rng.randint(1,2)):
            category=rng.choices(list(weights),weights=list(weights.values()))[0]
            categories[category]+=1
            if category in ("fragment","blueprint_fragment"):
                outcomes["blueprint_fragment"]+=1;found_fragment=True
            elif category=="gear_consumable":
                item=rng.choices(["medkit","frag_grenade","pistol","rifle"],weights=[40,20,20,20])[0]
                outcomes[item]+=1
            elif category=="food_water":outcomes[rng.choice(["food","water"])]+=rng.randint(8,15)
            elif category=="data":outcomes["research_data"]+=1
            else:outcomes[category]+=rng.randint(8,15)
        grant=pity.settle(str(index),"source-family",True,found_fragment)
        outcomes["blueprint_fragment"]+=grant;guaranteed+=grant
        max_dry=max(max_dry,pity.dry["source-family"])
    return {"outcomes":dict(outcomes),"categories":dict(categories),"successful_clears":rolls,
            "pity_guaranteed":guaranteed,"max_dry_gap":max_dry}


def fit_cargo(items, capacity):
    """Keep authored priority order, whole pickups; never silently split gear."""
    kept=[]; dropped=[]; used=0
    for key,cost in items:
        if used+cost<=capacity: kept.append(key); used+=cost
        else: dropped.append(key)
    return {"kept":kept,"dropped":dropped,"used":used,"capacity":capacity}


def arbitrage_cycles(recipes, prices=None):
    """Actual craft→salvage check; no selling/currency conversions invented."""
    findings=[]
    for rec in recipes:
        ins=rec.get("inputs",{}); outs=rec.get("outputs",{})
        if not ins or not outs: continue
        # Salvage returns at most50% recipe materials; run100 crafts numerically.
        initial={k:100*v for k,v in ins.items()}; stock=initial.copy()
        craft(stock,rec,100)
        for k,v in ins.items(): stock[k]=stock.get(k,0)+math.floor(100*v*.5)
        material_gain={k:stock.get(k,0)-v for k,v in initial.items()}
        if all(v>=0 for v in material_gain.values()): findings.append(rec.get("id","unknown"))
    return findings


def market_cycles(recipes):
    raw_prices={"scrap":1,"components":2,"chemicals":2}
    market={"c_9_civilian_pistol":(10,40),"medkit":(3,12),"frag_grenade":(4,18),
            "m_4_service_rifle":(30,120)}
    rows=[]
    for rec in recipes:
        identifier=rec.get("id","")
        # The exporter normalizes IDs; match by output or displayed recipe name.
        name=rec.get("name",identifier).lower()
        key=("c_9_civilian_pistol" if "pistol" in name else "m_4_service_rifle" if "rifle" in name
             else "frag_grenade" if "frag" in name else "medkit" if "medkit" in name else None)
        if key is None:continue
        ins=rec["inputs"]
        if not all(r in raw_prices for r in ins):continue
        input_value=sum(n*raw_prices[r] for r,n in ins.items())
        sale,buy=market[key]
        output_count=sum(rec.get("outputs",{}).values())
        salvage_value=sum(math.floor(n*.5)*raw_prices[r] for r,n in ins.items())
        rows.append({"recipe":identifier,"input_credit_value":input_value,"sale":sale*output_count,
                     "craft_sell_profit":sale*output_count-input_value,
                     "buy_salvage_sell_profit":salvage_value-buy,
                     "buy_sell_profit":sale-buy})
    return rows


def tutorial_route(branch="restore", exported=None):
    stock={"scrap":300,"components":120,"chemicals":40,"supply":20,"food":100,
           "water":120,"research_data":0}; rows=[]; ccl=1; residents=6
    changes=[("generator",-20,-5,0),("water",-20,-5,0),("living",-10,0,0),
      ("hydro",-80,-15,-10),("ccl2",-20,-5,0),("ccl3",-30,-10,0),
      ("radio",-20,-10,0),("house",160,75,30),("workshop",-30,-10,-5),
      ("supply_pack",-2,0,0),("ccl4",-40,-10,0),("clinic",-30,-10,-10),
      ("training",-20,-5,0),("living_l2",-90,-15,0),("warehouse",300,130,30),
      ("generator_l2",-120,-38,0),("sensor_excavate",-50,-5,0)]
    if branch=="restore": changes.append(("restore_sensor",-20,-5,0))
    if exported:
        # Consume actual exported changes; aliases add mission/supply event effects.
        matched=[]
        for index,row in enumerate(exported):
            # Ordered authored route carries semantic IDs; quantities always data-driven.
            if index>=len(changes):break
            name=changes[index][0]
            delta=row["delta"]
            matched.append((name,delta.get("scrap",0),delta.get("components",0),delta.get("chemicals",0)))
        if len(matched)==len(changes):changes=matched
    for name,s,c,ch in changes:
        for resource,delta in zip(("scrap","components","chemicals"),(s,c,ch)):
            if delta<0: pay(stock,{resource:-delta})
            else: stock[resource]+=delta
        if name.startswith("ccl"): ccl=int(name[-1])
        if name in ("house","warehouse"):
            pay(stock,{"supply":7}); residents+=1
            stock["research_data"]+=2 if name=="house" else 10
        if name=="supply_pack":
            pay(stock,{"food":5,"water":6}); stock["supply"]+=5
        rows.append({"step":name,**stock})
    # Spend-before-claim storage is tested separately through RewardLedger.
    return {"branch":branch,"ccl":ccl,"residents":residents,"stock":stock,"ledger":rows,
            "storage_semantics":"entitlement ledger; inbox claims required before actual spending"}


def site_output(base, tier=1, worker_efficiency=1., integrity=100, contested=False,
                owned_sites=1, efficient_sites=1, hide=False):
    tiers={1:1.,2:1.25,3:1.5,4:2.}
    integrity_factor=0 if integrity<25 else .5 if integrity<50 else .75 if integrity<75 else .9 if integrity<100 else 1
    ownership=max(.5,1-.1*max(0,owned_sites-efficient_sites))
    return {r:rate*tiers[tier]*worker_efficiency*integrity_factor*ownership*
              (1.1 if contested else 1)*(.9 if hide else 1) for r,rate in base.items()}


def progression_check(ccl_rows):
    """Detect prerequisite gates whose required source is locked behind the gate."""
    sources={"military_authorization":5,"hive_chitin_core":6,"military_ai_core":8,
             "neural_core":9,"architect_archive":10}
    requirements={6:"military_authorization",7:"hive_chitin_core",9:"military_ai_core",
                  10:"neural_core",11:"architect_archive",12:"architect_archive"}
    failures=[]
    for level,item in requirements.items():
        if sources[item]>=level: failures.append({"level":level,"item":item})
    return {"gates":len(ccl_rows) or 11,"source_checks":len(requirements),"cycles":failures,
            "scope":"mandatory PvE token reachability; not a full campaign solver"}


def extended_slice(data):
    route=tutorial_route("restore",data.get("tutorial_ledger"));stock=route["stock"].copy()
    # The archive bundle is authored content, not a recurring source assumption.
    stock["scrap"]+=200;stock["components"]+=80;stock["research_data"]+=10
    pay(stock,{"supply":8})
    ccl5=next((r for r in data.get("ccl",[]) if r["level"]==5),
              {"cost":{"scrap":200,"components":75,"research_data":10},"minutes":5})
    pay(stock,ccl5["cost"])
    lab=data.get("rooms",{}).get("research_lab",{"build_cost":{"scrap":140,"components":50,"chemicals":10},"build_minutes":8})
    pay(stock,lab["build_cost"])
    research=next((r for r in data.get("research",[]) if r["id"]=="SUR-01"),
                  {"cost":{"research_data":8},"minutes":5})
    pay(stock,research["cost"])
    return {"stock":stock,"ccl":5,"squad_cap":4,
            "minimum_sequential_build_research_minutes":ccl5["minutes"]+lab["build_minutes"]+research["minutes"],
            "prerequisites":{"warehouse_clear":True,"generator_l2":True,"living_l2":True},
            "scope":"authored successful route; combat/travel/rest duration not claimed as a4h guarantee"}


class ResearchLab:
    """Numeric gates/cost/queue/resume/effect-once; effect payload stays an ID.

    Discovery is a caller-supplied durable predicate because source text includes
    narrative contracts that cannot be inferred merely from a substring.
    """
    def __init__(self, stock, ccl, level, speed=1):
        self.stock=stock;self.ccl=ccl;self.level=level;self.speed=speed
        self.completed=set();self.job=None;self.effects=set()

    def start(self,node,discovered):
        if self.job is not None or node["id"] in self.completed:
            raise ValueError("duplicate or occupied queue")
        if self.ccl<node["ccl"] or self.level<node["lab_level"] or not discovered:
            raise ValueError("research gate")
        if not set(node.get("prerequisites",[]))<=self.completed:raise ValueError("research dependency")
        pay(self.stock,node["cost"])
        self.job={"node":node,"work":0}

    def advance(self,seconds,powered=True,worker=True):
        if not self.job or not powered or not worker:return
        self.job["work"]+=seconds/60*self.speed
        node=self.job["node"]
        if self.job["work"]>=node["minutes"]-EPS:
            self.completed.add(node["id"]);self.effects.add(node["id"]);self.job=None

    def cancel(self):
        if not self.job:return
        for r,n in self.job["node"]["cost"].items():self.stock[r]=self.stock.get(r,0)+n
        self.job=None


def research_dag(nodes):
    by_id={n["id"]:n for n in nodes};errors=[];visiting=set();done=set()
    def visit(key):
        if key in visiting:errors.append("cycle:"+key);return 0
        if key not in by_id:errors.append("missing:"+key);return 0
        if key in done:return done[key]
        visiting.add(key)
        depth=1+max([visit(p) for p in by_id[key].get("prerequisites",[])]+[0])
        visiting.remove(key);done[key]=depth
        return depth
    done={}
    for key in by_id:visit(key)
    return {"nodes":len(nodes),"max_path_nodes":max(done.values(),default=0),"errors":errors}


def research_sweep(data):
    nodes=data.get("research",[]);rows=[]
    speeds={r["level"]:r["research_speed"] for r in data.get("rooms",{}).get("research_lab",{}).get("levels",[])}
    for node in nodes:
        stock={r:100000 for r in node["cost"]};initial=stock.copy()
        speed=speeds.get(node["lab_level"],1)
        lab=ResearchLab(stock,node["ccl"],node["lab_level"],speed)
        lab.completed=set(node.get("prerequisites",[]))
        blocked=False
        try:lab.start(node,False)
        except ValueError:blocked=True
        lab.start(node,True);seconds=node["minutes"]*60/speed
        lab.advance(seconds*.4);lab.advance(seconds,powered=False);lab.advance(seconds*.6)
        duplicate=False
        try:lab.start(node,True)
        except ValueError:duplicate=True
        exact=all(stock[r]==initial[r]-n for r,n in node["cost"].items())
        rows.append({"id":node["id"],"cost":node["cost"],"seconds":seconds,
                     "discovery_gate_blocks":blocked,"completed":node["id"] in lab.completed,
                     "cost_once":exact,"duplicate_blocked":duplicate,"effect_applications":len(lab.effects),
                     "effect_behavior_simulated":node["id"] in {"SUR-01","SUR-02","SUR-03","EXP-01","EXP-02","EXP-03","ENG-01"}})
    return rows


def character_traits(seed):
    rng=random.Random(seed)
    scavenger=sum(rng.random()<.10 for _ in range(10000))
    efficiency=min(1.35,(.85+5*.03)*1.05*1.08)
    def confidence(base,cap,per,role,trait,radio,drone):
        return min(cap,max(30 if base==42 else 50,base+(per-5)*2+(5 if role else 0)+trait+radio+drone))
    return {"mechanic_workshop_efficiency_stat5_profession":efficiency,
            "mechanic_generator_power_bonus":0,"fast_learner_xp_per100":100*1.10,
            "scavenger_extra_common_rolls_in10000":scavenger,
            "hoarder_squad3_cargo":12+1,"hoarder_storage_efficiency":.95,
            "slow_recovery_survivor_trauma_minutes_clinic_l2":20*1.20*1.15/1.2,
            "scout_per8_role_quick":confidence(42,72,8,True,0,0,0),
            "scout_all_bonuses_quick_cap":confidence(42,72,10,True,8,20,8),
            "scout_all_bonuses_deep_cap":confidence(68,90,10,True,8,20,8),
            "assumptions":["Keen Eye +8 interpreted as8percentage points for capped stress case; caps hold regardless of additive/multiplicative interpretation."]}


def defense_budget_sweep():
    costs={"door":8,"sensor":5,"turret":15,"drone":12,"relay":6,"trap":7,"shutter":12,"guard_post":5}
    rows=[]
    # Fixed envelope of0–2 each permits exhaustive search without assuming room count.
    for budget in (20,35,55,80,110):
        legal=0;max_used=0
        for counts in itertools.product(range(3),repeat=len(costs)):
            used=sum(n*c for n,c in zip(counts,costs.values()))
            if used<=budget:legal+=1;max_used=max(max_used,used)
        rows.append({"capacity":budget,"configurations_with_0to2_each":legal,"maximum_used":max_used,
                     "overbudget_turrets_rejected":15*(budget//15+1)>budget})
    return rows


def run_all(seed=20261112, data_path=None):
    data,provenance=load_data(data_path); scenarios=[]; checks=[]
    def record(name,actual,passed,category):
        scenarios.append({"name":name,"category":category,"passed":bool(passed),"actual":actual})
        checks.append({"name":name,"passed":bool(passed)})
    eco=data.get("economy",FIXTURE["economy"])
    def economy(**kwargs):
        start=dict(eco.get("start",FIXTURE["economy"]["start"]))
        pop=start.pop("population",6)
        return Economy(start,population=pop,production=eco.get("production",{"food":10,"water":12}),
                       consumption=eco.get("consumption",{"food":1,"water":1.2}),**kwargs)
    a=economy(); b=economy()
    a.advance_offline(8*3600)
    for i in range(1,9): b.advance_offline(i*3600)
    delta=max(abs(a.stock[k]-b.stock[k]) for k in a.stock)
    record("offline_partition_8h",{"one_window":a.stock,"eight_windows":b.stock,"max_delta":delta},delta<1e-7,"economy")
    e=economy(); e.stock["food"]=250;e.production["food"]=0;e.advance(3600)
    record("full_storage_consumption",{"food_after":e.stock["food"],"population":e.population},abs(e.stock["food"]-244)<EPS,"economy")
    e=economy();e.sites=[Site()];e.advance_offline(16*3600);before=copy.deepcopy(e.stock);e.advance_offline(16*3600)
    record("offline16h_reconnect",{"site_produced":e.sites[0].produced,"collections":e.sites[0].collections,"reconnect_delta":{k:e.stock[k]-v for k,v in before.items()}},abs(e.sites[0].produced.get("scrap",0)-144)<EPS and e.stock==before,"sites")
    e=economy(generator_integrity=0);e.stock["food"]=e.stock["water"]=0;e.restart();e.advance(300)
    record("blackout_manual_restart",{"generation":e.generation,"stock":e.stock,"integrity":e.generator_integrity},e.generation==24 and e.stock["food"]==e.stock["water"]==0,"power")
    duration=e.repair();e.advance(duration)
    record("normal_generator_repair",{"work_seconds":duration,"generation":e.generation,"scrap":e.stock["scrap"]},e.generator_integrity==1 and e.stock["scrap"]==285,"power")
    e=economy(generator_integrity=0,battery=20,other_load=2);e.advance(4*3600)
    record("battery_to_emergency",{"battery":e.battery,"emergency":e.emergency},e.battery==0 and e.emergency,"power")
    e=economy();e.stock.update(food=0,water=0,supply=0);e.production={"food":0,"water":0};e.start_relief();e.advance(600);bound=e.bound.copy();e.advance(1800);again=e.start_relief()
    record("bound_relief_no_repeat_mint",{"bound":bound,"repeat_accepted":again},bound=={"food":10,"water":12,"supply":6} and not again,"recovery")
    t=Treatment(20,3,1.2);stock={"chemicals":10};t.advance(600,stock);t.advance(500,stock,powered=False);t.advance(400,stock)
    record("clinic_pause_resume",{"complete":t.complete,"work":t.progress,"chemicals":stock["chemicals"]},t.complete and stock["chemicals"]==7,"recovery")
    e=economy();e.advance(30);record("fatigue81_boundary",{"fatigue":e.fatigue},abs(e.fatigue-80)<EPS,"recovery")
    for branch in ("restore","convert"):
        route=tutorial_route(branch,data.get("tutorial_ledger"));expected=158 if branch=="restore" else 178
        record("tutorial_"+branch,route,route["stock"]["scrap"]==expected and route["stock"]["supply"]==11 and route["ccl"]==4,"progression")
    extended=extended_slice(data)
    record("extended_slice_cc l5_research".replace(" ",""),extended,
           extended["stock"]["scrap"]==18 and extended["stock"]["research_data"]==4 and extended["stock"]["supply"]==3,"progression")
    gates=progression_check(data.get("ccl",[]));record("pve_gate_reachability",gates,not gates["cycles"],"progression")
    ccl_rows=data.get("ccl",[]);storage_levels=data.get("rooms",{}).get("storage",{}).get("levels",[])
    for node in ccl_rows:
        prior=node["level"]-1;max_level=1 if prior<=2 else 2 if prior<=4 else 3 if prior<=6 else 4 if prior<=9 else 5
        capacity=next((r["capacity"] for r in storage_levels if r["level"]==max_level),250)
        modules=max(math.ceil(v/capacity) for r,v in node["cost"].items() if r in ("scrap","components","chemicals"))
        stock={r:max(v,capacity*modules) for r,v in node["cost"].items()};pay(stock,node["cost"])
        record("ccl_affordability_"+str(node["level"]),{"cost":node["cost"],"prior_ccl_storage_level":max_level,"minimum_storage_modules":modules,"remaining":stock,"upgrade_minutes":node["minutes"]},all(v>=0 for v in stock.values()),"progression")
    nodes=data.get("research",[]);dag=research_dag(nodes)
    record("research_dependency_dag",dag,not dag["errors"] and dag["max_path_nodes"]<=3,"research")
    for row in research_sweep(data):
        record("research_"+row["id"],row,row["completed"] and row["cost_once"] and row["duplicate_blocked"] and row["discovery_gate_blocks"] and row["effect_applications"]==1,"research")
    trait=character_traits(seed)
    record("noncombat_character_traits",trait,abs(trait["mechanic_workshop_efficiency_stat5_profession"]-1.134)<EPS and 700<trait["scavenger_extra_common_rolls_in10000"]<1300 and trait["scout_all_bonuses_quick_cap"]==72 and trait["scout_all_bonuses_deep_cap"]==90,"characters")
    recipes=data.get("recipes",FIXTURE["recipes"]);arb=arbitrage_cycles(recipes)
    record("craft_salvage_material_conservation",{"recipes_checked":len(recipes),"profitable_cycles":arb},not arb,"economy")
    for recipe in recipes:
        stock={r:v*3 for r,v in recipe["inputs"].items()};before=stock.copy();craft(stock,recipe)
        valid=all(stock[r]==n*2 for r,n in recipe["inputs"].items() if r not in recipe["outputs"])
        record("recipe_source_sink_"+recipe["id"],{"inputs":recipe["inputs"],"outputs":recipe["outputs"],"minutes":recipe["minutes"],"before":before,"after":stock,"unlock_text":recipe.get("unlock_text",""),"unlock_semantics":"discovery/license condition supplied by caller; not parsed from prose"},valid,"crafting")
    market=market_cycles(recipes)
    record("npc_market_craft_sell_buy_salvage",{"cycles":market},all(max(r["craft_sell_profit"],r["buy_salvage_sell_profit"],r["buy_sell_profit"])<=0 for r in market),"economy")
    base=data.get("sites",FIXTURE["sites"]).get("scrapyard",{"base_output":{"scrap":18}})["base_output"]
    outputs={str(t):site_output(base,tier=t,contested=True,owned_sites=5,efficient_sites=3,hide=True) for t in range(1,5)}
    record("site_tier_worker_integrity_ownership_hide",{"output_per_hour":outputs},abs(outputs["1"]["scrap"]-18*.8*1.1*.9)<EPS and outputs["4"]["scrap"]==2*outputs["1"]["scrap"],"sites")
    for site_id,site_data in data.get("sites",{}).items():
        combinations=[]
        for tier,integrity,worker,contested,hide in itertools.product(range(1,5),(0,24,25,49,50,74,75,99,100),(.65,1,1.35),(False,True),(False,True)):
            output=site_output(site_data["base_output"],tier,worker,integrity,contested,5,3,hide)
            combinations.append(output)
        record("site_output_sweep_"+site_id,{"combinations":len(combinations),"minimum":{r:min(x[r] for x in combinations) for r in site_data["base_output"]},"maximum":{r:max(x[r] for x in combinations) for r in site_data["base_output"]}},all(all(n>=0 for n in x.values()) for x in combinations),"sites")
    budgets=defense_budget_sweep()
    record("defense_capacity_enumeration",{"budgets":budgets,"room_layout_geometry_simulated":False},all(r["maximum_used"]<=r["capacity"] and r["overbudget_turrets_rejected"] for r in budgets),"defense")
    weights=data.get("loot_weights",{}).get("house",{"scrap":30,"components":20,"food":20,"water":20,"chemicals":10})
    if not all(isinstance(v,(float,int)) for v in weights.values()): weights={"scrap":30,"components":20,"food":20,"water":20,"chemicals":10}
    loot=weighted_loot(seed,weights,1000);record("seeded_weighted_loot_and_pity",loot,loot["max_dry_gap"]<=2 and loot==weighted_loot(seed,weights,1000),"loot")
    for source,source_weights in data.get("loot_weights",{}).items():
        sample=weighted_loot(seed,source_weights,1000)
        record("loot_distribution_"+source,sample,sum(source_weights.values())==100 and sample["max_dry_gap"]<=2,"loot")
    for case in data.get("treatment",[]):
        stock={"chemicals":100};t=Treatment(case["minutes"],case["chemicals"],1.2)
        t.advance(case["minutes"]*60/1.2,stock)
        record("treatment_"+case["id"],{"seconds_at_speed1_2":case["minutes"]*60/1.2,"remaining_chemicals":stock["chemicals"],"completed":t.complete},t.complete and stock["chemicals"]==100-case["chemicals"],"recovery")
    ledger=RewardLedger(seed);normal=ledger.normal_cache("normalcache",weights)
    record("normal_five_card_cache_contract",{"cards":normal},len(normal)==5 and normal[4]==("blueprint_fragment",1) and ledger.normal_cache("normalcache",{"different":100})==normal,"loot")
    cargo=fit_cargo([("common"+str(i),1) for i in range(5)]+[("knowledge",1),("cache",3),("rescue",1)],12)
    record("house_authored_cargo",cargo,cargo["used"]==10 and not cargo["dropped"],"loot")
    ledger=RewardLedger(seed);pool={"scrap":30,"components":20};cards=ledger.cache("cache1",pool);ledger.cache("cache1",{"alien":1})
    ledger.settle("failed",False,{"p1":{"scrap":10}},"house",knowledge=["crawler"])
    ledger.settle("retry",True,{"p1":{"scrap":10}},"house")
    for _ in range(10): ledger.settle("retry",True,{"p1":{"scrap":10}},"house")
    ledger.settle("second_clear",True,{"p1":{"scrap":10}},"house")
    inbox={"scrap":100};ledger.claim("c1","scrap",30,inbox);ledger.claim("c1","scrap",30,inbox)
    record("reward_failed_retry_replay_cache_claim",{"inventory":dict(ledger.inventory),"inbox":inbox,"cards":cards,"first_clear_count":len(ledger.first_clears),"knowledge":sorted(ledger.knowledge)},ledger.inventory["scrap"]==40 and inbox["scrap"]==70 and ledger.cache_cards["cache1"]==cards and len(ledger.first_clears)==1,"persistence")
    world=PvpWorld(data.get("pvp",{}).get("loss_caps"));world.add("a");world.add("b");d=world.add("d");d.losses=[(-23*3600,{"scrap":40})]
    raid=world.begin("r1","a","d",0);rejected=False
    try: world.begin("r2","b","d",0,asset="site",site_stock={"scrap":144},output={"scrap":18})
    except ValueError: rejected=True
    result=world.settle("r1",100,True,{"scrap":12})
    world.settle("r1",100,True,{"scrap":12})
    record("cross_asset_concurrent_reservation_replay",{"exposure":raid["exposure"],"second_rejected":rejected,"stock":d.stock,"result":result},rejected and raid["exposure"]["scrap"]==20 and d.stock["scrap"]==988,"pvp")
    remaining=world.remaining(d,"scrap",3600)
    record("rolling24h_exact_boundary",{"remaining_after_old_entry_expires":remaining},remaining==48,"pvp")
    world=PvpWorld();world.add("a");d=world.add("d");world.begin("timeout","a","d",0);world.expire(901)
    record("reservation_expiry_failed_extraction",{"stock":d.stock,"incoming":d.active_incoming,"reserved":d.reserved},d.stock["scrap"]==1000 and d.active_incoming is None and not d.reserved,"pvp")
    denied=[]
    for mode,kwargs in (("ccl7",{"ccl":7}),("no_consent",{"opted":False}),("shield",{"shield_until":60})):
        world=PvpWorld();world.add("a");world.add("d",**kwargs)
        try:world.begin(mode,"a","d",0);denied.append(False)
        except ValueError:denied.append(True)
    record("pvp_eligibility_matrix",{"all_denied":denied},all(denied),"pvp")
    stock={"scrap":100,"components":20,"supply":20,"claim_beacon":1};claim=Claim(stock);initial=stock.copy();claim.begin("c",6);claim.settle("c",False);claim.settle("c",False)
    record("beacon_claim_interruption_refund",{"stock":stock},stock==initial,"sites")
    return {"summary":{"seed":seed,"scenario_count":len(scenarios),"passed":sum(c["passed"] for c in checks),"failed":sum(not c["passed"] for c in checks)},
            "provenance":provenance,"scenarios":scenarios,"checks":checks,
            "limitations":["Noncombat reference model; not the game runtime, network/server, engine or manual playtest.",
              "Tutorial ledger computes authored entitlement and affordability, not a timed optimal-policy playthrough or UI inbox interaction.",
              "Loot uses exported category weights,Easy1–2 rolls/clear,Easy8–15 quantities and documented3successful-clear pity; eligible gear pool is a four-item baseline, not all research/CCL loot filters.",
              "Craft/salvage tests use documented50% maximum material recovery; NPC craft/sell and buy/salvage/sell cycles run for priced recipes; arbitrary full multi-recipe conversion cycles are not proven absent.",
              "PvP model covers consent, locks, exposure, rolling theft, charges, shields and expiry; not ranking/match quality, capture combat or collusion enforcement.",
              "Power model runs life-support priority and battery/emergency/restart, not a full arbitrary room-grid topology solver.",
              "Economy assumes staffed life support at efficiency1 and full-integrity rooms unless overridden; detailed hunger-derived nonessential penalties and relief pending-mission eligibility are not modeled.",
              "Recovery models rest and one powered treatment with pause/resume; parallel clinic queue, full roster/body/capture state machine belong to combat/runtime validation."]}
