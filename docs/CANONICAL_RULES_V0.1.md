# BURROW ZERO — Canonical Rules / Source of Truth v0.1

**Status:** HIGHEST-PRIORITY DESIGN REFERENCE  
**Date:** 2026-11-12

This file exists to prevent contradictions caused by design being developed across many iterations.

If two documents conflict, use this precedence:

1. **CANONICAL_RULES_V0.1.md**
2. newest dedicated system spec for that system
3. GAME_DESIGN_V0.1.md / GDD
4. DESIGN_PLAN.md
5. research/audit/history documents

Research files describe influences, not binding gameplay rules.

Implementation baseline owners (2026-11-12 revision):

- [Survivor Recovery](SURVIVOR_RECOVERY_V0.1.md): death/body/gear, treatment/rest, staffing.
- [Mission Sessions](MISSION_SESSION_REWARDS_V0.1.md): quit/resume, extraction settlement, cache/inbox.
- [Progression](PROTOTYPE_PROGRESSION_V0.1.md): CCL costs/source routes, emergency economy/offline timing.
- [Content Pack](PROTOTYPE_CONTENT_PACK_V0.1.md): roster, authored tutorial missions/grants/repair ledger.
- [Research Catalog](PROTOTYPE_RESEARCH_CATALOG_V0.1.md): node IDs/effects/costs/gates.
- [Implementation Baseline](IMPLEMENTATION_BASELINE_V0.1.md): prototype input/targeting/actions/status/XP.
- [Campaign Contract Catalog](CAMPAIGN_CONTRACTS_V0.1.md): chapter prerequisites, guaranteed sources and replayable objectives.

These are tunable implementation baselines, not runtime/balance evidence. Historical audits remain snapshots of their recorded commits; current closure is tracked in GAP_CLOSURE_2026-11-12.md.

---

# 1. Brand

Game:

**BURROW ZERO**

Slogan:

**Deep Below. Far Beyond.**

Initial languages:

- Vietnamese;
- English.

---

# 2. Canonical Inhabitants

Standard survivor characters are **anthropomorphic panda survivors**.

They are not temporary cosmetic replacements for human characters.

Player-facing narrative should prefer:

- survivor;
- Silo resident;
- settlement;
- old-world civilization;
- faction;
- unknown Silo signal.

Avoid species-specific legacy wording such as:

- humanity;
- human survivor;
- human signal;

unless intentionally referring to historical legacy text that has not yet been rewritten.

Hostile civilized enemies are **Raiders / hostile survivor factions**, visually panda-derived.

Alien creatures remain non-panda.

---

# 3. Art

Canonical art direction:

- simple AI-first low-poly 3D;
- panda mascot survivors;
- shared survivor rig;
- shallow isometric / 2.5D gameplay camera;
- approximately 25–35° downward view for expedition;
- primitive-friendly modular assets.

Canonical production spec:

[ART_PRODUCTION_V0.1.md](./ART_PRODUCTION_V0.1.md)

---

# 4. PvE / PvP Relationship

**PvE is a complete game path.**

PvP is:

- competitive;
- prestigious;
- economically useful;
- an alternate source of some progression.

PvP is **not required** for core story completion or baseline endgame viability.

No mandatory CCL upgrade requires a PvP-only item.

If an item has a PvP source, core progression must have a PvE/NPC/contested alternative unless the item is explicitly cosmetic/prestige-only.

---

# 5. CCL Progression — CANONICAL

| CCL | Main unlock |
|---|---|
| 1 | Survival rooms |
| 2 | Surface Gate + squad cap 3 + basic expedition |
| 3 | Radio/Scout + Workshop |
| 4 | Clinic/Training + Medium targets |
| 5 | Research Lab + **squad cap 4** |
| 6 | Security/Armory + Resource Site capture |
| 7 | Network + NPC Silo + broader Silo signals |
| 8 | Player PvP + **squad cap 5** |
| 9 | Advanced Tech / Prototype Forge |
| 10 | Alien Tech / Xenobiology |
| 11 | Coalition systems |
| 12 | Surface Return / endgame |

Standard room max level:

| CCL | Room max |
|---|---|
| 1–2 | L1 |
| 3–4 | L2 |
| 5–6 | L3 |
| 7–9 | L4 |
| 10–12 | L5 |

Prototype CCL2–12 cost/prerequisite table is specified in PROTOTYPE_PROGRESSION_V0.1.md; final live tuning remains open. First2h endsCCL4/squad3; extended2–4h slice addsCCL5/squad4/LabL1/one research. Tutorial repair prices are explicit one-time exceptions, not normal construction costs.

---

# 6. Squad

Canonical standard squad progression:

```
CCL2 → 3
CCL5 → 4
CCL8 → 5
```

Standard combat cap:

**5**

Special modes may use different limits only if explicitly specified.

---

# 7. Combat Death Exception

General rule:

- actively deployed attacker/PvE units can suffer real death;
- revive uses rare revival mechanics.

Exception:

- offline asynchronous PvP defenders cannot permanently die from normal defense resolution;
- Resource Site workers cannot permanently die from normal offline contest resolution.

They may receive:
- Injury;
- Fatigue;
- recovery time.

This exception protects named-survivor attachment from offline punishment.

Normal lethal transition: DOWN60simulation seconds, then DEAD_RECOVERABLE; one field Injector revive/unit/mission. Second lethal hit skips DOWN. Body2CU/one living escort; recovered body requires Clinic service, not automatic resurrection. Wipe/unescorted body causes permanent loss. Tutorial SAFE_DOWN and protected defender15min recovery use explicit Recovery contract.

---

# 8. Resource Site Output — CANONICAL BASELINE

Use [ECONOMY_RESOURCES_V0.1.md](./ECONOMY_RESOURCES_V0.1.md) for base outputs.

| Site | Base output |
|---|---:|
| Scrapyard | 18 Scrap/h |
| Chemical Plant | 8 Chemicals/h |
| Solar Farm | 8 Energy Cells/h |
| Water Facility | 30 Water/h |
| Uranium Mine | 3 Reactor Material/h |
| Data Center | 6 Research Data/h |
| Military Salvage | 5 Components/h + rare military roll |
| Alien Crater | 2 Alien Material/h |

Examples in older location documents are illustrative only and do not override this table.

---

# 9. Power / Survival

Starting:

- Emergency Core: +8 PU;
- first Generator L1: +20 PU;
- Population: 6;
- Food: 100;
- Water: 120.

Consumption baseline:

```
Food = 1.0 / survivor / hour
Water = 1.2 / survivor / hour
```

Hydroponics L1:

```
10 Food/h
```

Water Treatment L1:

```
12 Water/h
```

---

Core8PU emergency mode: Command2+Water3+Food3, consumption waived, no spendable emergency resource output. Manual Restart/bounded relief and comeback actions are specified in PROTOTYPE_PROGRESSION_V0.1.md. Survival production is exempt from hunger/dehydration/morale/fatigue negative efficiency; power/integrity still apply. All background clocks share8h offline window; no random offline survival deaths.

# 10. Scout

Scout never reaches 100% certainty.

Canonical caps:

- Quick Scout: 30–72%;
- Deep Scout: 50–90%.

Exact enemy list, complete layout and exact loot remain hidden.

---

# 11. PvP

Canonical PvP model:

- asynchronous;
- CCL8 unlock;
- hidden/progressive layout reveal;
- same combat language as PvE;
- attacker can retreat;
- defender cannot be zeroed.

Normal defender loss cannot include:

- permanent room loss;
- CCL loss;
- unique survivor loss;
- blueprint ownership loss.

Silo/site PvP requires both accounts CCL8+ and explicit persistent account opt-in; NPC PvE never opts in. Private PvE sites at all tiers never convert to contested. Shared shields/caps/one incoming reservation cover all PvP assets. PvP defense cap5 fromCCL8; PvE defenseCCL6–7 cap4. Only Scrap/Components/Chemicals can be stolen; survival and strategic materials never stolen. Rolling24h per-resource caps forCCL8..12 are respectively60/20/12,75/25/15,90/30/18,105/35/21,120/40/24; exposed pool≤10%unreserved stock. PvP deadline15real min from departure; timeout only auto-extracts if squad currently at cleared valid exit and escort/cargo valid. Reservation/settlement details owned by PvPProtection.

All site buffers8h output; free automatic collection from first site every8simulated production hours, shared offline8h cap. Beacon source/cost/refund owned by ResourceSites, accessible without PvP.

---

# 12. World

World Map consists of:

- Regions;
- persistent nodes;
- semi-persistent nodes;
- temporary nodes;
- faction influence;
- Resource Sites;
- NPC/player Silo signals.

No real-GPS dependency.

---

# 13. Factions

Initial canonical factions:

1. Continuity
2. Free Settlements
3. Earthborn
4. Archivists
5. Ascendants

Faction technology is primarily sidegrade/option expansion, not mandatory best-in-slot power.

---

# 14. Story Structure

Canonical campaign structure:

- **Prologue: Wake**
- **8 main chapters**

Chapter 1 through Chapter 8 follow after the Prologue.

This resolves the earlier wording that called Chapter 0–8 "8 chapters."

---

# 15. Season

Season baseline:

```
8–12 weeks
```

No persistent Silo wipe.

---

# 16. Alliance

Coalition baseline:

```
20 members
```

Full Coalition systems unlock around CCL11.

Solo players retain viable core/endgame PvE.

---

# 17. Reward / Gacha Rule

Reward-card reveal is allowed.

Hero/survivor gacha is not.

No:

- survivor rarity stars;
- duplicate survivor shards;
- paid RNG exclusive combat survivor;
- paid RNG exclusive mandatory power.

---

# 18. Simulation Status

**Combat Simulation has NOT started.**

All combat/economy numeric values labeled prototype/baseline remain tunable.

Do not interpret absence of simulation as permission to invent alternate numbers in implementation.

Use documented baselines until revised.

---

# 19. Unresolved Product Decisions

Still intentionally unresolved:

- exact active-control density in combat;
- final monetization/pricing model;
- final live CCL balance (prototype table exists);
- final drop rates/tuning;
- final platform release order;
- technical backend/save architecture.

These are not contradictions; they are open decisions. Prototype combat control is concrete: deploy formation, autoattacks, manual focus/consumable, PvE tactical pause; active abilities and manual midfight reposition OFF. Final density remains playtest-dependent. Gameplay consequences of save/disconnect are already specified; backend/vendor choice may not silently change those rules.
