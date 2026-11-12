# BURROW ZERO — Prototype Research Catalog v0.1

**Status:** Concrete authoring baseline; all 34 named nodes from Research & Technology Tree. Not simulation or playtest evidence.  
**Authority:** Canonical Rules and `RESEARCH_TECH_TREE_V0.1.md` own progression principles; this catalog owns stable IDs, prototype costs, prerequisites and exact node effects.  
**Slice:** only SUR-01 is required for extended 2–4h slice. Other nodes are later content, not an instruction to implement every branch now.

## 1. Shared contracts

Costs below are **Research Data (RD)** unless additional existing items are listed. Consume cost once on research start, reserve one Lab queue position and worker; progress pauses without power/worker and resumes without charging again. One node cannot be queued twice. Cancel before completion refunds 100% reserved resources and grants no effect/discovery; cancel/restart never preserves elapsed research time. Queue means waiting jobs, not concurrent throughput: each Lab performs one active research job. Finished effects persist once and never compound on reload.

Times are baseline active time at Lab L1 before its speed multiplier. Apply Lab speed once; worker contributes eligibility, not a second undocumented speed multiplier. General tiers: I CCL5, II CCL6, III CCL7–8, IV CCL9, V CCL10+. Faction special gates are explicit below. A discovery is durable knowledge, not a consumed item, unless cost column explicitly names a consumed item. No PvP win or PvP-exclusive material required.

`None` in prerequisite means no prior research node. Discovery may occur before owning a Lab. Optional discovery-gated nodes remain silhouettes until discovered; tell player a source category. Maximum normal chain is **three nodes**, matching the main Research prerequisite rule, and no irrelevant branch prerequisite. Sidegrade faction nodes do not require permanent allegiance or purchase at a faction store; Trusted/Allied reputation unlocks the relevant contract directly.

## 2. Survival

| ID / node | Tier; CCL; Lab min | Prior research | Cost | Base time | Exact effect | Discovery/source available before research |
|---|---|---|---:|---|---|---|
| SUR-01 Efficient Hydroponics | I; 5; L1 | None | 8 RD | 5 min | Hydroponics normal Food output ×1.10; applies once before common output multipliers | Complete first Hydroponics build at CCL1–2 |
| SUR-02 Water Reclamation | I; 5; L1 | None | 8 RD | 5 min | Water Treatment normal output ×1.10 | Restore starting Water Treatment |
| SUR-03 Expanded Battery | I; 5; L1 | None | 10 RD | 10 min | Battery capacity ×1.20; does not fill added capacity or increase charge rate | Build a Battery; base recipe already available |
| SUR-04 Emergency Rationing | I; 5; L1 | None | 8 RD | 5 min | Delay Food shortage penalty transitions by 1h: first band 0–2h, next 2–5h, crisis5h+; no effect on consumption/Water or emergency recovery guarantees | First Food warning preview; can deliberately preview warning without reaching shortage |
| SUR-05 Medical Sterilization | II; 6; L2 | None | 20 RD, Chemicals 4 | 20 min | Clinic Infection treatment base duration ×0.80; no bonus to field healing/revive | Extract Hospital Pharmacy medical manifest; optional normal Hospital exists at CCL4 |

## 3. Expedition

| ID / node | Tier; CCL; Lab min | Prior research | Cost | Base time | Exact effect | Discovery/source available before research |
|---|---|---|---|---|---|---|
| EXP-01 Field Packing | I; 5; L1 | None | 10 RD | 10 min | Existing 5-Supply recipe becomes Food4 + Water5 + Scrap2, still2min; Command emergency queue retains original recipe, preventing two bonuses | Craft one normal Supply batch at Command/Workshop |
| EXP-02 Deep Scan | I; 5; L1 | None | 12 RD | 15 min | Existing Deep Scout gains +5 percentage points confidence, capped90%; does not gate basic Deep Scout availability | Complete a Deep Scout using Radio L1; no research prerequisite for that scout |
| EXP-03 Cargo Harness | II; 6; L2 | EXP-01 | 20 RD, Components5 | 20 min | Squad Cargo +2 CU total, not per unit, including squad3/4/5 | Complete one successful extraction |
| EXP-04 Emergency Extraction | II; 6; L2 | EXP-01 | 25 RD, Components5 | 30 min | Unlock Emergency Beacon recipe: Scrap10 + Components5 + Chemicals2, Workshop5min, stack1; opens only the exits explicitly marked beacon-compatible by mission | Observe an emergency-exit sign in any normal Warehouse/Hospital; no Beacon needed to observe |
| EXP-05 Route Analysis | III; 7; L3 | EXP-02 | 40 RD | 1h | Bad travel-event probability ×0.90 after base chance and before final cap; no effect on positive events or max travel time | Return from any two non-tutorial missions; no bad event must actually occur |

## 4. Combat

| ID / node | Tier; CCL; Lab min | Prior research | Cost | Base time | Exact effect | Discovery/source available before research |
|---|---|---|---|---|---|---|
| COM-01 Ballistic Calibration | I; 5; L1 | None | 12 RD, Components3 | 10 min | Unlock existing Stabilized modifier for a ballistic weapon: +6 percentage points Accuracy, obey cap98%; install once for Scrap8 + Components4, Workshop3min; uses its one Major Modifier slot | Extract one ballistic weapon or use starting Rifle |
| COM-02 Energy Focusing | II; 6; L2 | None | 20 RD, Components5 | 20 min | Laser Focus cap20%→24%; +4%/sec rate and reset-on-switch unchanged | Extract/equip a Laser from normal Lab/Military/contract source; research not needed to acquire it |
| COM-03 Blast Control | II; 6; L2 | None | 20 RD, Chemicals4 | 20 min | Frag secondary-target damage ×1.10; primary55 and target limit/radius unchanged; no bonus to Rocket or EMP | Use one Frag in any mission; starting stock is sufficient |
| COM-04 Combat Triage | I; 5; L1 | None | 12 RD, Chemicals4 | 10 min | Medkit use-action duration ×0.80; does not alter heal amount, revive count or healing cooldown | Use a Medkit and extract; tutorial stock supplies it |
| COM-05 Tactical Doctrine | III; 7; L3 | COM-01 | 40 RD, Military Data2 | 1h | Add Support First preset: valid revealed Support enemies first, then lowest currentHP, then stable enemyID tie-break; manual focus overrides until target invalid | Observe Support enemy; Military Data from CCL5–6 Military Depot contract, not PvP |

## 5. Security

| ID / node | Tier; CCL; Lab min | Prior research | Cost | Base time | Exact effect | Discovery/source available before research |
|---|---|---|---|---|---|---|
| SEC-01 Reinforced Doors | II; 6; L2 | None | 20 RD, Components5 | 20 min | Unlock Door MkII: same8 Capacity/1PU, HP150/Armor25. Upgrade existing MkI for15 Scrap/5 Components/2min; choose fail-open/fail-closed. Installed-defense data owned by Security§17; objective/extraction path remains valid | Inspect any standard Door; starting Silo door qualifies |
| SEC-02 Sensor Network | II; 6; L2 | None | 20 RD, Components5 | 20 min | Unlock Sensor Node,5 Capacity/1PU; build15 Scrap/5 Components/2min; records entry once/room and adds10 Alarm. Also unlock Backup Cell per Security§7/17 | Build Security L1 and inspect its overlay |
| SEC-03 Automated Turret | II; 6; L2 | SEC-02 | 25 RD, Components8 | 30 min | Unlock player Sentry Turret MkI,15 Capacity/3PU; build35 Scrap/12 Components/4min, HP140/Armor25,12 Ballistic/1sec. Enemy Auto Turret MkII remains a different entity; Security§17 owns full stats | Encounter normal Mechanical threat in Warehouse or Military Depot; neither needs a player Turret |
| SEC-04 Alarm Logic | III; 7; L3 | SEC-02 | 40 RD, Military Data2 | 1h | One-time choice of response threshold70 or80 instead of75; show tradeoff in editor; threshold never spawns more than one response wave; switch freely outside an active raid | Complete Silo09 NPC tutorial raid; NPC Alarm is available without this player research |
| SEC-05 Response Doctrine | III; 8; L3 | SEC-04 | 50 RD, Military Data3 | 90min | Allow response squad to stage in one validated adjacent room at threshold, without exceeding squad cap or duplicating stationed defenders; retain one-wave limit | Complete any second NPC raid; can be same archetype after refresh, no PvP requirement |

## 6. Engineering

| ID / node | Tier; CCL; Lab min | Prior research | Cost | Base time | Exact effect | Discovery/source available before research |
|---|---|---|---|---|---|---|
| ENG-01 Workshop Tooling | I; 5; L1 | None | 10 RD, Components3 | 10min | Workshop craft-speed ×1.10; timer duration = base / speed; does not multiply item yield | Finish one Workshop craft |
| ENG-02 Salvage Recovery | II; 6; L2 | ENG-01 | 20 RD, Components5 | 20min | Gear salvage recovery +5 percentage points (Civilian30→35%, Industrial35→40%, Military40→45%, Advanced45→50%, Prototype50→55%); round each material down; special rolls unchanged | Salvage one nonunique duplicate; initial loot/contract can provide Civilian gear without this node |
| ENG-03 Power Management | I; 5; L1 | None | 10 RD | 10min | Unlock custom room load-shedding order; emergency life-support floor cannot be disabled accidentally and mandatory path validation still applies | Open default power-priority panel; no shortage required |
| ENG-04 Drone Systems | III; 7; L3 | ENG-03 | 40 RD, Components8 | 1h | Unlock Scout Drone utility: Scrap20 + Components12, Workshop6min; Deep Scout +8 percentage points cap90%; one adjacent-room reveal/mission; mission anti-drone action may consume it. Defense Drone12Capacity/2PU, build30 Scrap/12 Components/4min; Security§17 owns installed-defense data | Extract Mechanical salvage from Warehouse/Depot; no Drone needed for source |
| ENG-05 Prototype Fabrication | IV; 9; L3 | ENG-01 | 80 RD, Prototype Core1 | 3h | Grants fabrication license required to build Prototype Forge and use known Prototype blueprints; does not grant free Forge/blueprint/gear | Prototype Core guaranteed progression path from Hard boss/NPC lab objective; no Forge needed to earn it |

## 7. Xenobiology

These are optional risk-bearing sidegrades. Do not create a new currency for Exposure; use the existing Alien Exposure state. Exposure values/effects follow its canonical implementation contract, and equip tooltips preview changes before confirmation. Items retain existing gear slots and never exceed resistance caps. No Xenobiology node is required to acquire the first Alien sample/material.

| ID / node | Tier; CCL; Lab min | Prior research | Cost | Base time | Exact effect | Discovery/source available before research |
|---|---|---|---|---|---|---|
| XEN-01 Alien Tissue Analysis | V; 10; L4 | None | 120 RD, Alien Material2 | 8h | Analyze one known Alien sample to advance its Bestiary by one knowledge tier, never beyond Researched; action costs1 sample +5RD, Lab10min; no automatic knowledge of unknown enemies. Handling adds1 Exposure per analysis | Extract first Alien tissue from CCL9–10 anomaly, combat or story; no Xenobiology gear needed |
| XEN-02 Exposure Monitoring | V; 10; L4 | XEN-01 | 120 RD, Alien Material2 | 8h | Display exact current Exposure, band boundaries and predicted change for known gear/actions; monitoring itself adds0 Exposure | First Alien Exposure warning or first sample, both available before node |
| XEN-03 Adaptive Material | V; 10; L4 | XEN-01 | 140 RD, Alien Material4 | 10h | Unlock Adaptive Hazmat sidegrade recipe: Scrap35 + Components10 + Chemicals8 + Alien Material3, Xenobiology10min; Hazmat base armor12/Bio45%, add Energy15%; attack-speed -5%; adds5 Exposure per deployment. Caps apply | Extract Alien shell material through Alien tissue objective; no adaptive gear required |
| XEN-04 Neural Interface | V; 10; L4 | XEN-02 | 140 RD, Alien Material4 | 10h | Alien utility recipe: Components12 + Alien Material3 + Research Data10, Xenobiology12min; +10% Tech Effect for bearer while equipped, +5 Exposure per deployment; occupies one existing Utility slot | Read Alien terminal with manual story translation; Engineer only speeds interaction, no Interface needed |
| XEN-05 Artifact Theory | V; 11; L5 | XEN-03 | 160 RD, Alien Material5 | 12h | Unlock artifact blueprint research actions and source hints; consumes no artifact, grants no raw stat bonus/Artifact itself, adds0 Exposure | Recover Artifact fragment from guaranteed late-PvE story objective; finding fragment needs no Artifact research |

## 8. Faction / Special

These nodes are alternate options; no node substitutes for a mandatory CCL item or blocks core story. Reputation gates are checked once when starting research; losing reputation later does not erase completed research. No faction token is introduced here.

| ID / faction node | CCL; Lab min | Prior research | Cost | Base time | Exact effect | Discovery/source |
|---|---|---|---|---|---|---|
| FAC-01 Continuity — Security Protocol | 7; L3 | None | 35 RD, Military Data2 | 1h | Door MkII security sidegrade may add +10% breach time with +1 activePU; does not stack a second generic Door upgrade; same8 Capacity. Toggle per door outside active raid | Continuity Trusted20 + complete “Door Audit” PvE contract; normal Door/Lab available beforehand; SEC-01 required only to install on MkII, not to learn node |
| FAC-02 Archivists — Archive Compression | 7; L3 | None | 35 RD | 1h | Data/Blueprint field-loot stacks weigh 0.5CU instead of1CU, round total cargo up at mission boundary; never protects from extraction loss, increases RD yield or changes physical-material weight | Archivists Trusted20 + retrieve a Data Center archive through PvE; no Compression needed |
| FAC-03 Earthborn — Surface Conditioning | 7; L3 | None | 35 RD, Chemicals4 | 1h | Allow hazard training stance: bearer gains +10 percentage points Bio/Rad resistance and -5% attack speed for one mission; choose at preparation, free to remove afterward, no midmission switching; obey caps | Earthborn Trusted20 + surface route survey; route has a hazard-free extraction alternative |
| FAC-04 Ascendants — Hybrid Interface | 10; L4 | XEN-02 | 100 RD, Alien Material3 | 8h | Optional Neural Interface sidegrade: Tech Effect bonus15% instead of10%, deployment Exposure8 instead of5; same Utility slot; not stackable with normal Interface and still requires its recipe/installation materials | Ascendants Trusted20 + Alien terminal contract; neither reputation nor contract requires equipped Neural Interface; XEN-04 license required to craft either variant |

Free Settlements have logistics/trade/recruitment contracts in Factions; the branch source document names no dedicated research node, so this catalog does not invent a fifth mandatory faction tech.

## 9. Prerequisite and source audit

- Longest research path is SEC-02 → SEC-04 → SEC-05 (2 links), or XEN-01 → XEN-02 → XEN-04 (2 links). All others are shorter; gates on recipe installation do not silently become research prerequisites.
- No source requires the item it unlocks: first Laser/Core/sample/Artifact fragment are loot or PvE contract paths, not crafting products of the gated node. If a required later source is not yet implemented, node remains **NOT IMPLEMENTED**, never mark tested or inject free rewards silently.
- Prototype Core source must obey boss guaranteed-progression protection; Alien Material has PvE/NPC alternatives; no Resource Site contest/PvP-only dependency.
- A node consumes RD/material once, records effect once, has one stable ID, explicit source hint, CCL/Lab gate and base time. Lower tiers remain available after CCL advancement.
- New recipe effects here reuse existing weapons/armor/utility families and existing resources. They are concrete content baselines; they do not certify final power balance, final backend behavior or completion of the research UI.
- Minimum slice acceptance: earn22 Data through authored path, spend10 on CCL5 and8 on SUR-01, observe4 remaining, Food normal baseline10→11/h before other applicable modifiers, reopen/reload and observe no repeated cost or second+10% application.
