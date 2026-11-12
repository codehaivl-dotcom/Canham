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

Exact CCL material costs remain tuning work.

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
- exact CCL upgrade costs;
- final drop rates/tuning;
- final platform release order;
- technical backend/save architecture.

These are not contradictions; they are open decisions.
