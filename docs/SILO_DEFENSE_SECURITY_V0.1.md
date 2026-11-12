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

Cap follows PvP spec:

- up to current standard squad cap.

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

Security research can unlock Backup Cell.

Capacity:
- 10 Defense Capacity equivalent or dedicated module slot.

Effect:
- powers limited security systems after main outage for a short raid window.

No infinite power.

---

# 8. Room Limits

To preserve readability:

- max 1 major defense per standard room;
- max 2 minor defense elements;
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

After raid:
- automatically restored over repair time;
- may cost small Scrap if heavily damaged.

No permanent loss of purchased defense.

---

# 12. Security Upgrade Philosophy

Higher tier adds:
- new behavior;
- resilience;
- detection;

not only HP.

Example:

Door Mk II:
- stronger;
- has emergency fail-open/fail-closed choice.

Turret Mk II:
- better targeting / resistance;
- not simply 2× DPS.

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
DEFENSE SQUAD 4/4
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
