# BURROW ZERO — Design Audit v0.4

> Historical audit snapshot, not current readiness/sign-off. The 2026-11-12 remediation is tracked in [GAP_CLOSURE_2026-11-12.md](GAP_CLOSURE_2026-11-12.md); runtime tests remain NOT RUN.


**Date:** 2026-11-12  
**Scope:** full document consistency audit after multi-turn design expansion.  
**Excluded by request:** Combat Simulation execution.

---

# 1. Audit Result

The project now has a dedicated baseline spec for every major gameplay/product area required to describe BURROW ZERO end-to-end.

Current design-document readiness excluding Combat Simulation:

**~94–96% concept/system completeness**

The remaining work is mainly:

- tuning;
- implementation architecture;
- content production;
- monetization decisions;
- final narrative copy.

---

# 2. New Production Docs Added During This Audit

## Art

- ART_PRODUCTION_V0.1.md
- VISUAL_SCREEN_TARGETS_V0.1.md

## Previously hidden gameplay gaps

- RESEARCH_TECH_TREE_V0.1.md
- SILO_DEFENSE_SECURITY_V0.1.md

## Online safety gap

- SOCIAL_PLAYER_SAFETY_V0.1.md

## Cross-document governance

- CANONICAL_RULES_V0.1.md

These were missing even though related mechanics were mentioned in other documents.

---

# 3. Cross-Document Conflicts Found and Resolved

## A. CCL progression conflict — FIXED

Old GDD:

- CCL2 Workshop/Clinic;
- CCL4 Expedition.

Newer Silo spec:

- CCL2 Surface Gate + squad 3;
- CCL3 Radio/Scout + Workshop;
- CCL4 Clinic/Training;
- CCL5 squad 4;
- CCL8 squad 5.

Resolution:

**SILO_BUILDINGS + CANONICAL_RULES are authoritative.**

GDD was updated to the same table.

---

## B. Squad unlock conflict — FIXED

UNITS_ITEMS previously said exact CCL milestones were still undefined.

Resolution:

```
CCL2 = 3
CCL5 = 4
CCL8 = 5
```

UNITS_ITEMS and GDD updated.

---

## C. Tutorial used Scout before canonical unlock — FIXED

Tutorial first expedition used Quick Scout but did not explain how Radio/Scout was unlocked.

Resolution:

Curated onboarding now explicitly advances:

- CCL1 start;
- CCL2 life-support milestone;
- CCL3 before first full expedition;
- CCL4 after first return.

---

## D. Resource Site output conflict — FIXED

WORLD_TARGETS example:

- Uranium Mine = 12 Ore/hour.

ECONOMY canonical:

- Uranium Mine = 3 Reactor Material/hour.

Resolution:

Economy table is canonical.

WORLD_TARGETS example updated.

---

## E. PvP accidentally looked mandatory — FIXED

Old GDD included:

- PvP research token in possible CCL requirements;
- language implying some progression could require PvP.

This conflicted with the newer product direction:

> PvE must be complete by itself.

Resolution:

- no CCL requires PvP-only item;
- PvP is alternate/competitive progression;
- core PvE/endgame has PvE route;
- PvP-only mandatory power is disallowed.

---

## F. Death rule conflicted with async defense — FIXED

Old GDD:

> death is real in every combat.

New PvP policy:

offline defender cannot permanently lose named survivor.

Resolution:

- active PvE/attacker deployment can have real death;
- offline PvP defender and Resource Site workers are protected from permanent death;
- Injury/Fatigue still apply.

---

## G. Panda art vs human lore — FIXED

Art/brand established panda survivors, while old story still said:

- humanity;
- human signal;
- Human/Raider family.

Resolution:

Canonical inhabitants are anthropomorphic panda survivors.

Key docs now prefer:

- survivor;
- Silo signal;
- old-world civilization;
- Raider / hostile survivor faction.

Legacy research/history wording may remain where it is discussing old concepts.

---

## H. Story chapter count mismatch — FIXED

Story said "8 Chapters" but listed Chapter 0 through Chapter 8.

Resolution:

- 1 Prologue: Wake;
- 8 main chapters.

---

## I. GDD unresolved list was stale — FIXED

GDD still listed the following as unresolved:

- side-view vs isometric;
- squad slot milestones;
- number of CCL;
- PvP target selection;
- season duration;
- alliance size.

These are now resolved:

- camera: shallow isometric / 2.5D;
- squad: CCL2/5/8;
- CCL: 12 baseline;
- PvP target selection: matchmaking spec;
- season: 8–12 weeks;
- Alliance: 20 members baseline.

Only genuinely open decisions remain.

---

## J. Combat Data had a non-game source — FIXED

ECONOMY listed "combat simulation events" as a source.

Simulation is a design/testing process, not player content.

Resolution:

Combat Data now comes from:

- PvP;
- NPC Silo challenge;
- tactical/security contracts;
- selected contested events.

---

# 4. Major System Coverage

| System | Status |
|---|---|
| Brand / slogan | ✅ |
| VI + EN localization | ✅ |
| Panda AI-first art | ✅ |
| Art production budgets | ✅ |
| 10 visual screen targets | ✅ |
| Silo / rooms / Power | ✅ |
| Silo expansion | ✅ |
| Silo defense | ✅ |
| Economy/resources | ✅ |
| Research tree | ✅ |
| Survivors/jobs/traits | ✅ |
| Unit/items/weapons | ✅ |
| Enemy/boss/resistance | ✅ baseline |
| World targets/dungeons | ✅ |
| Scout/travel/contracts | ✅ |
| Loot/crafting/blueprints | ✅ |
| Cache/card reveal | ✅ |
| Resource Sites | ✅ |
| World Map/regions | ✅ |
| NPC Silo Raid | ✅ |
| Player PvP Raid | ✅ |
| Matchmaking/protection/revenge | ✅ |
| Factions | ✅ |
| Alliance | ✅ |
| Mimic/infiltration | ✅ |
| Story campaign | ✅ |
| First 1–2h tutorial | ✅ |
| UI/UX navigation | ✅ |
| Sound/music | ✅ |
| Social/block/report/chat | ✅ |
| Seasons/endgame | ✅ |
| Combat Simulation | ⏸ intentionally not started |

---

# 5. Source-of-Truth Problem — FIXED

Because the project grew through many conversations, old and new rules existed in parallel.

New rule:

[CANONICAL_RULES_V0.1.md](./CANONICAL_RULES_V0.1.md)

Precedence:

1. CANONICAL_RULES
2. newest dedicated system spec
3. GDD
4. DESIGN_PLAN
5. research/audit/history

This must be followed by all agents.

---

# 6. Remaining Design Gaps — Intentional / Non-Blocking

## A. Active Combat Control Density

Still open:

- number of active abilities;
- exact retarget frequency;
- reposition timing.

This should be decided after playable combat exists.

## B. Exact Numeric Tuning

Still open:

- final CCL costs;
- final drop rates;
- exact resource-site production tuning;
- final weapon/enemy numbers.

Baselines exist.

## C. Monetization

Direction exists:

- anti-P2W;
- cosmetics;
- optional Season Pass;
- no hero-gacha.

Still missing:

- exact business model;
- prices;
- premium currency decision;
- store layout.

This requires product/business decision, not automatic design invention.

## D. Technical Architecture

Not design-complete:

- backend authority;
- save model;
- sync/conflict;
- anti-cheat;
- deployment;
- matchmaking infrastructure.

This is engineering architecture, not a gameplay-design gap.

## E. Analytics / Telemetry

Still needs implementation plan:

- tutorial funnel;
- mission abandon/extract;
- resource bottleneck;
- death/revive;
- PvP fairness;
- retention.

## F. Final Content Production

Still needs:

- final dialogue;
- named survivors;
- final faction writing;
- full item tables;
- full mission pool;
- season scripts.

System rules already exist.

## G. Platform Order

PC/mobile/controller/touch support direction exists.

Launch platform priority is not yet locked.

---

# 7. Risk Audit

## Highest design risk

**Scope.**

BURROW ZERO now has enough systems for a large game.

Do not implement all systems simultaneously.

Vertical slice must prove:

```
SILO
→ PREPARE
→ EXPEDITION
→ COMBAT
→ LOOT
→ EXTRACT
→ RETURN
→ UPGRADE
```

before persistent-world complexity.

## Second risk

**AI art inconsistency.**

Mitigation:

- ART_PRODUCTION is binding;
- shared panda body;
- shared rig;
- modular kits;
- primitive ceiling.

## Third risk

**Too many currencies/systems shown too early.**

Mitigation:

- tutorial reveals systems gradually;
- basic early UI shows Power/Water/Food/Scrap;
- strategic currencies appear later.

## Fourth risk

**PvP overwhelming PvE identity.**

Mitigation:

PvE remains complete and story/endgame viable.

---

# 8. Current Readiness by Area

| Area | Readiness |
|---|---:|
| Core product vision | 97% |
| Brand / art direction | 95% |
| PvE systems | 94% |
| Silo/economy/research | 92% |
| Survivor/loot progression | 90% |
| World/Resource Sites | 90% |
| Raid/PvP policy | 88% |
| Narrative/onboarding | 88% |
| Faction/Alliance/live | 82% |
| UI/UX/audio/social | 85% |

Overall excluding Combat Simulation:

**~94–96% at concept/system-spec level.**

This does **not** mean 95% of production is complete. It means the game can now be described coherently without major gameplay-system holes.

---

# 9. Recommended Next Non-Simulation Work

1. build primitive panda base rig;
2. build one Silo room kit;
3. reproduce Main Silo concept in-engine;
4. build one expedition room;
5. implement the first 30 minutes of tutorial;
6. only then expand asset library.

Avoid writing many more speculative systems unless implementation exposes a missing rule.

---

# 10. Audit Conclusion

The multi-turn gap problem is now substantially controlled.

The most important improvement is not another feature document; it is the new **source-of-truth discipline**.

Future agents should begin with:

1. README;
2. CANONICAL_RULES;
3. relevant dedicated spec;
4. GDD only for broader context.

Combat Simulation remains intentionally excluded and NOT STARTED.
