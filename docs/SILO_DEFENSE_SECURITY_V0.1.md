# BURROW ZERO — Silo Defense & Security v0.1

**Status:** PvE/PvP defense baseline  
**Unlock:** Security/Armory at CCL6

---

# 1. Principle

Defense must use the same readable systems as expedition combat.

The player designs:

- route pressure;
- detection;
- delay;
- response.

Not an unbeatable trap maze.

---

# 2. Defense Capacity

Security Room provides Defense Capacity.

Canonical capacity from Silo Buildings:

| Security Level | Capacity |
|---|---:|
| L1 | 20 |
| L2 | 35 |
| L3 | 55 |
| L4 | 80 |
| L5 | 110 |

Placed defenses consume this budget.

---

# 3. Defense Catalog

## Reinforced Door

Cost:
- 8 Capacity.

Role:
- delay;
- route control.

Power:
- 1 PU when active lock.

Can be:
- hacked;
- breached;
- powered down.

---

## Sensor Node

Cost:
- 5 Capacity.

Role:
- reveal attacker;
- increase Alarm.

Power:
- 1 PU.

Counter:
- Scout/Engineer;
- power cut.

---

## Sentry Turret

Cost:
- 15 Capacity.

Role:
- ranged damage.

Power:
- 3 PU.

Counter:
- EMP;
- hack;
- power cut;
- direct destruction.

---

## Defense Drone

Cost:
- 12 Capacity.

Role:
- mobile pressure / support.

Power:
- 2 PU charging/active abstraction.

Counter:
- EMP;
- anti-drone utility.

---

## Alarm Relay

Cost:
- 6 Capacity.

Role:
- faster Alarm gain;
- response coordination.

Power:
- 1 PU.

Can be disabled.

---

## Shock Trap

Cost:
- 7 Capacity.

Role:
- short Electric/Stagger event.

Single-use per raid baseline.

Counter:
- Scout detection;
- Engineer disarm.

---

## Blast Shutter

Cost:
- 12 Capacity.

Role:
- temporary route lock;
- stronger than normal door.

Power:
- 2 PU.

Cannot create impossible path.

---

# 4. Guard Posts

A room may be designated as Guard Post.

Cost:
- 5 Capacity.

Effect:
- improves defender starting position;
- modest Alarm response bonus.

Does not create extra survivor.

---

# 5. Defense Squad

Player selects defense squad.

| CCL | Defense survivor cap | Allowed use |
|---|---:|---|
| 6–7 | 4 | PvE internal/story defense only |
| 8–12 | 5 | PvE; asynchronous PvP only after explicit account opt-in |

There is no3/4/5 early/mid/late PvP defense ladder. First CCL8 PvP supports5 defenders immediately. Empty slots create no free units. Defense is a persistent exclusive assignment for combat deployment: a selected defender may perform a Silo base job but cannot depart on expedition, an outgoing PvP raid, or a Resource Site worker/guard assignment while selected. Explicitly unassign first; unassignment and gear transfer are blocked during an incoming raid lock. Resource Site workers/guards and expedition-deployed survivors cannot be assigned to Silo defense. The account may attack while being attacked only with a distinct unassigned squad and distinct gear; no survivor/gear can exist in both snapshots.

Accepted incoming PvP snapshots the selected squad/gear/room topology. Selected defenders remain unavailable for outbound deployment throughout their defense assignment, not merely while an incoming raid exists; they may continue base jobs. Subsequent layout/gear edits affect the next snapshot only. The account-wide incoming raid lock prevents concurrent Silo/site defense conflicts. Apply real survivor Injury/Fatigue exactly once at settlement; snapshot death never permanently removes a defender.

Offline defense:
- AI controlled;
- no permanent death;
- Injury/Fatigue possible.

---

# 6. Power Dependency

Defenses depend on Power.

If attacker disables power:

- turret may shut down;
- sensors weaken;
- electronic doors change fail state;
- backup power may preserve selected systems.

Player may set emergency priority.

---

# 7. Backup Power

Backup Cell unlocks with Security research Sensor Network (no separate unnamed research node). Build cost30 Scrap/10 Components,3min; uses10 Defense Capacity and1 minor slot in its room. Maximum1 per Silo/site. No idle PU. On main power loss it supplies up to4PU of selected electronic defenses for60 combat seconds per raid, then drains. Order selected by player before snapshot; default Sensor→Door→Turret→Drone, stable objectID tie break. Recharge automatically between raids over15 real minutes, no material/fuel payment. A new incoming snapshot during recharge receives proportional remaining seconds, never a fresh60sec. Local site integrated supply uses the same60sec backup if its control terminal is disabled. No infinite power or dedicated module-slot alternative.

---

# 8. Room Limits

To preserve readability:

- max 1 major defense (Turret, Defense Drone or Blast Shutter) per standard room;
- max 2 minor defense elements (Door, Sensor, Alarm Relay, Shock Trap, Guard Post or Backup Cell);
- no stacking 5 turrets in one doorway.

---

# 9. Mandatory Path Rule

Every raid layout must preserve at least one valid path to primary objective.

Defense may:

- delay;
- branch;
- punish;

but not create unreachable Command Core.

Validator should check path graph.

---

# 10. Trap Information

Attacker Scout may reveal:

- likely sensor;
- high security room;
- power wing.

Never exact full defense list.

Inside raid, detected trap telegraphs before activation when Scout/utility succeeds.

---

# 11. Defense Damage

Destroyed defense in raid is temporary state.

After raid, a disabled/damaged installed defense restores to100% HP over15 simulated recovery minutes, free, independently of Clinic. Other installed defenses remain usable. Repair time advances within the8h offline window, then freezes. Scrap repair is not required; paid/manual instant-repair is absent. Repeated settlement cannot reset or lengthen the same damage event. Snapshot changes are never copied as permanent deletion.

No permanent loss of purchased defense.

---

# 12. Security Upgrade Philosophy

Higher tier adds:
- new behavior;
- resilience;
- detection;

not only HP.

Current prototype upgrade is Door Mk II, defined numerically in §17 with explicit research and fail-state selection. Future turret upgrades are deferred rather than implied unlocked items.

---

# 13. PvE Use

Defense systems also matter in:

- internal Silo events;
- alien intrusion;
- Mimic incident;
- story defense mission.

This prevents defense investment from being PvP-only.

---

# 14. UI

Security overlay shows:

- Defense Capacity used;
- Power load;
- path;
- Alarm nodes;
- defense squad;
- weak points.

Simple:

```
CAPACITY 43 / 55
POWER 8 PU
ALARM RELAYS 2
DEFENSE SQUAD 5/5 (CCL8 opted-in)
```

---

# 15. Success Criteria

Defense succeeds if:

1. defender layout has personality;
2. attacker has counters;
3. Power matters;
4. no impossible maze;
5. investment helps PvE too;
6. offline loss is recoverable.


# 16. Defense Eligibility Checks

1. CCL6 Security can assign4 for PvE but cannot make a Silo/site player-attackable.
2. CCL8 without PvP opt-in can assign5 for PvE; no incoming player raid is accepted.
3. CCL8 opted in:5 is the same cap shown in Security and PvP mission preparation.
4. A survivor working at a site cannot also be a Silo guard; a persistently assigned Silo defender cannot depart until explicitly unassigned outside an incoming lock.
5. Changing squad/gear after raid acceptance preserves the incoming snapshot; injury settlement changes the real survivor once, even after reconnect/retry.
6. Account shield blocks new Silo AND contested-site raids, including Revenge. Private PvE sites are never exposed by defense assignment.

Refer to PVP_MATCHMAKING_PROTECTION for the exact acceptance transaction and shields.


# 17. Build, Research & Combat Baseline

These values are prototype data pending combat simulation. Build requires a CONTROLLED room/site, available capacity and listed materials; reserve at start, consume once at completion; cancel refunds reserved inputs. Relocate only outside incoming lock; no salvage/material-generation loop.

| Defense | Unlock | Scrap | Components | Build min | HP | Armor |
|---|---|---:|---:|---:|---:|---:|
| Door Mk I | CCL6 Security | 20 | 5 | 2 | 100 | 20 |
| Sensor Node | Sensor Network | 15 | 5 | 2 | 50 | 0 |
| Sentry Turret Mk I | Automated Turret | 35 | 12 | 4 | 140 | 25 |
| Defense Drone | Drone Systems | 30 | 12 | 4 | 100 | 15 |
| Alarm Relay | Alarm Logic | 15 | 6 | 2 | 60 | 5 |
| Shock Trap | CCL6 Security | 12 | 4 | 1 | 30 | 0 |
| Blast Shutter | Reinforced Doors | 30 | 10 | 3 | 160 | 30 |
| Guard Post | CCL6 Security | 10 | 2 | 1 | No extra combat object | — |
| Backup Cell | Sensor Network | 30 | 10 | 3 | 60 | 10 |

Research branches belong to RESEARCH_TECH_TREE; node IDs/costs/prerequisites belong to PROTOTYPE_RESEARCH_CATALOG. Door Mk II requires Reinforced Doors: upgrade one Mk I for15 Scrap/5 Components/2min; HP150/Armor25, same8 Capacity/1PU, choose fail-open or fail-closed before publishing. Mk I defaults fail-open. Blast Shutter defaults fail-open. Power-loss fail-closed remains hackable/breachable, never an invulnerable path obstruction. No Turret Mk II player upgrade in this baseline; enemy Auto Turret Mk II is a separate encounter entity, not a research promise.

Turret Mk I attacks for12 Ballistic every1.0sec, Accuracy85%, Crit5% at1.5×. Defense Drone attacks for8 Ballistic every0.8sec, Accuracy80%, Crit0. All use unit armor formula and Mechanical resistance profile Ballistic20/Energy10/Explosive0/Fire65/Electric−25/Bio80 percent; nonattacking electronic devices use the same profile. Doors/shutters use neutral resistance0 to all types. EMP disables electronic defenses3sec; Disable cannot stack duration, refreshes to max remaining3sec. Door/shutter retain their fail state under EMP. HP0 disables through settlement and invokes §11 recovery.

Shock Trap fires once per raid on first hostile entry after a1sec visible telegraph:20 Electric damage to frontmost living attacker and1sec stagger. Sensor detects entry and adds10 Alarm once/room; Alarm Relay adds5 to that event (max1 relay per room). Guard Post puts one selected existing guard in front formation and reduces that guard's first damage hit by10%; no free stat/HP boost or duplicate guard. Guard stats and equipment are exactly the assigned survivor's normal formulas. Guards occupy the defense squad/site-guard cap.

Engineer interaction with detected device/door:6sec divided by Tech Effect Multiplier (including role bonus); succeeds deterministically if user remains ACTIVE and uninterrupted. Damage/stagger interrupts without consuming a charge; retry restarts. A hacked sensor/relay/turret stays disabled for this raid; a hacked door opens. Non-Engineer may breach a door by attacking HP using normal damage, so every mandatory path remains possible without a mandatory specialist. Detection: Sensor/Trap is automatically revealed by an ACTIVE Scout in that room, otherwise after its1sec telegraph; no undefined RNG detection roll in this baseline. Other trap-hint scout information remains imperfect before entry.

Power priority/fail-state and guard assignment are visible in the Security overlay before publish. Path validation checks entry→objective→exit with all doors either hackable OR destructible, including power-off states. If invalid, block publishing, keep the last valid defense layout and explain the disconnected room. A Silo without a prior valid published layout remains a generated unobstructed path with existing rooms/assigned survivors, never immune to attacks because of an invalid edit.
