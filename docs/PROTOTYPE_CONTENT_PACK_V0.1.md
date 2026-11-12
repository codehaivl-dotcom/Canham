# BURROW ZERO — Playable Prototype Content Pack v0.1

**Status:** Authorable prototype baseline, not playtest or balance evidence.  
**Scope:** deterministic first 2h; extended 2–4h slice.  
**Authority:** Canonical Rules wins; this pack owns the authored IDs, tutorial grants and repair ledger below. Normal new-building costs still use Silo Buildings. No repeated grant on replay/reload.

## 1. Fixed starting roster

All are named anthropomorphic pandas, level 1, Morale 60, Fatigue 0, healthy. Stats order is COM / END / AGI / PER / INT / TEC / MED / RES; every stat is 1–10 and every total is 32–44. Profession is an affinity, not a locked class. Three pre-trained combat roles are tutorial grants, not Training Room prerequisites.

| ID | Name | Stats | Total | Profession / trait | Initial assignment |
|---|---|---|---:|---|---|
| SUR-001 | Bảo | 7 / 8 / 4 / 4 / 3 / 4 / 2 / 6 | 38 | Security / Tough | Vanguard, Front |
| SUR-002 | Linh | 7 / 5 / 7 / 6 / 3 / 3 / 2 / 5 | 38 | Civilian Generalist / Steady Hands | Assault, Mid |
| SUR-003 | Mai | 3 / 5 / 4 / 5 / 7 / 4 / 8 / 5 | 41 | Doctor / Calm | Medic, Back |
| SUR-004 | Nam | 3 / 6 / 4 / 4 / 6 / 8 / 3 / 5 | 39 | Engineer / Mechanic | Generator worker |
| SUR-005 | An | 3 / 5 / 4 / 4 / 7 / 5 / 3 / 6 | 37 | Civilian Generalist / Fast Learner | Hydroponics worker |
| SUR-006 | Vy | 4 / 5 / 6 / 8 / 5 / 4 / 3 / 5 | 40 | Scout / Keen Eye | Water worker; no combat role yet |

Before Hydroponics opens, An clears debris. Generator output does not scale with worker efficiency; keep Nam on maintenance. Water/Hydro need one worker for normal output, have staffed output floor 1.0× and positive cap 1.35×, and produce 50% output when unstaffed. Empty Living/Storage do not need workers to retain beds/capacity. Radio Quick Scout needs one worker; use Vy temporarily and preview the Water contribution change. Workshop also needs one available worker while crafting. The first two scout sequences are 20 seconds each; UI previews the change. No worker is simultaneously deployed and producing.

Starting owned gear: one Shotgun (Bảo), one Assault Rifle (Linh), four C-9 Civilian Pistols (Mai/Nam/An/Vy), six Civilian Jackets, four Medkits and two Frag Grenades. These are existing item archetypes at base weapon-table values, not higher-tier example-item overrides. Mai carries two Medkits, Bảo two Medkits, Linh two Frags; unused slots are empty. No Revival Injector, paid item or mandatory Engineer utility is required. No ammunition stockpile is introduced.

## 2. Authored encounter rules

Tutorial House/Warehouse use existing Crawler/Spitter/Rifleman archetypes. Because their published enemy table is a level 8–12 reference, these authored level-1 encounters multiply **base HP by 0.55 and base direct/ability damage by 0.40**, rounded up. This replaces the Easy HP/damage multiplier; never multiply both. Other enemy behavior/resistance/attack intervals remain unchanged. No variants, elites, reinforcements, timed doors or travel ambushes in these two missions. These numbers require later simulation and playtest.

First adjacent sector: two tutorial Crawlers; no loot grant, free first excavation/stabilization, then Hydroponics uses normal build cost. First-hour safety follows Tutorial: a lethal hit causes SAFE_DOWN; only a full protected squad wipe causes automatic safe return, otherwise finish the room or choose extraction, never permanent death. Retry uses the same authored node and deterministic content. Banked reward IDs never respawn. After successful partial extraction, cleared rooms stay cleared and unbanked/dropped pickups remain reacquirable at their authored location. After failed extraction, clear progress resets and every unbanked pickup/cache/rescue objective respawns with the same ID and outcome; already banked pickups/rescued residents do not. Pending rescue cannot disappear because its room was cleared. Departure Supply and consumed items are never restored. Quick Scout neither rerolls nor refreshes these maps.

Mission graph must always preserve a return path to entrance. Locked optional doors have a free manual bypass, never require an unavailable recipe, survivor or consumable. Rescue survivors add one Cargo Unit and do not fight before reaching home. Do not count a rescued character as an active squad member or raise cap 3.

## 3. House — HSE-TUT-01, “A Light in the Kitchen”

Distance 2 km; Easy; squad cap 3. Supply = 6 deployment + 1 Quick Scout = **7 total**. Round trip travel is 69 seconds each way. Active-play target 3–6 minutes, not measured evidence. Quick Scout returns a civilian/biological hint, never full enemy/layout knowledge.

Graph: `H1 Entrance → H2 Living → H3 Kitchen`; branch `H2 → H4 Bedroom`. H1 remains the extraction point throughout.

| Room | Encounter / interaction | Fixed reward ID and content |
|---|---|---|
| H1 Entrance | No enemy; explain return route | None |
| H2 Living | 2 tutorial Crawlers | HSE-LOOT-01: Scrap 100, Components 45 |
| H3 Kitchen | No enemy; unlock pantry manually | HSE-LOOT-02: Food 20, Water 24, Chemicals 30, Research Data 2 |
| H4 Bedroom | 1 tutorial Crawler, wounded Tùng; apply a free scene bandage, not a consumed Medkit | HSE-CACHE-01 and SUR-007 rescue flag (passenger1CU) |

SUR-007 **Tùng**: 4 / 6 / 4 / 5 / 5 / 6 / 4 / 5 = **39**; Mechanic, Team Player, level 1. Arrives with a narrative minor bruise and no combat penalty; can work after returning. Separately, the first complete House extraction applies one **Tutorial bruising** to Bảo if he has no existing injury: a recovery tag without an additional permanent stat penalty; a single free 3-minute Clinic treatment clears it. Never stack this scripted injury or spend an Injector. This provides an actual recovery tutorial without random incapacitation.

HSE-CACHE-01 opens only after extraction, exactly five cards: Scrap 60; Medkit ×2; Credits 100; Components 30; Standard Weapon Blueprint Fragment ×1. It is a single Field Loot object weighing 3 CU until return. Loose stack limit here is 100 units per common resource per CU; Knowledge/Data bundle weighs 1 CU. Maximum House load is 5 common stacks + 1 knowledge bundle + 3 cache + 1 rescued passenger = **10 CU**, below squad-3 cap 12.

**Total House reward, including cache:** Scrap 160, Components 75, Chemicals 30, Food 20, Water 24, Research Data 2, Credits 100, Medkits 2, one Standard Weapon Blueprint Fragment, Tùng. The cache is not an additional duplicate grant. Main objective = rescue Tùng and extract; optional partial extraction remains successful for already held loot. First-clear flag `FC-HSE-TUT-01` records the one-time cache/rescue contract, not a second reward pool.

## 4. Warehouse — WHS-TUT-01, “Parts for Tomorrow”

Distance 4 km; Easy; squad 3. Supply = 6 deployment + 1 Quick Scout = **7 total**. Travel 93 seconds each way. Swarm/AOE hint, no exact enemy list. Graph: `W1 Loading → W2 Storage → W3 Office → W4 Security`; optional branch `W2 → W5 Cold Storage → W6 Maintenance`. Extraction remains W1.

| Room | Encounter / interaction | Fixed reward |
|---|---|---|
| W1 Loading | No enemy | None |
| W2 Storage | 4 tutorial Crawlers; teach Shotgun cone or one optional Frag | WHS-LOOT-01: Scrap 100, Components 35 |
| W3 Office | 1 tutorial Rifleman | WHS-LOOT-02: Scrap 100, Components 35, Research Data 10 |
| W4 Security | Noncombat terminal, manual reset always available | WHS-CACHE-01; main objective parts manifest |
| W5 Cold Storage | 2 tutorial Crawlers | WHS-LOOT-03: Food 10, Water 12, Chemicals 30 |
| W6 Maintenance | Locked side door; free 10-second manual release, or faster TEC interaction | Rescue SUR-008; no extra gear drop |

SUR-008 **Hạnh**: 5 / 6 / 5 / 4 / 4 / 7 / 3 / 6 = **40**; Technician, Mechanic, level 1. Healthy, untrained combat role. No resident recruitment roll. Rescue reaches eight residents; Living L2 provides ten beds.

WHS-CACHE-01: Scrap 100; Medkits 2; Credits 150; Components 60; Standard Weapon Blueprint Fragment 1. Weighs 3 CU. Loose cargo = Scrap two stacks, Components one, Chemicals one, Food one, Water one, Data one = 7 CU; cache adds3 and rescued passenger1 = **11 CU**. Nothing exceeds 12 CU or needs an Armory first.

**Total Warehouse reward, including cache:** Scrap 300, Components 130, Chemicals 30, Food 10, Water 12, Research Data 10, Credits 150, Medkits 2, one Standard Weapon Blueprint Fragment, Hạnh. Main objective = manifest + extract; W5–W6 are optional. `FC-WHS-TUT-01` marks the same single cache grant. Remaining unclaimed optional rooms stay available without refreshing cleared loot.

## 5. Hospital — HSP-SLICE-01, “The Quiet Ward”

Optional after CCL4; 4 km; Medium; squad 3. Supply = 7 deployment + 1 Quick Scout = **8 total**. Authored low-level package replaces Medium stat multiplier with base HP ×0.75, damage ×0.65; level-1 players are warned to recover/train first. No boss required; optional depth is not part of first-2h completion.

Graph: `P1 Reception → P2 Ward → P3 Pharmacy → P4 Storage`; branch `P2 → P5 Surgery → P6 ICU → P7 Morgue → P8 Lab`. Return always possible to P1. Pharmacy has no keyed door. P5 warns that deeper rooms are optional; no collapse or bio damage before the warning. All pickups are unique IDs `HSP-LOOT-Pn` and require extraction.

| Room | Encounter / hazard | Fixed pickup |
|---|---|---|
| P1 | Safe entrance | None |
| P2 | 2 Crawlers | Scrap 20 |
| P3 | 1 Spitter | Chemicals 30, Medkits 2; main medical manifest |
| P4 | Safe storage | Components 20, Research Data 10 |
| P5 | 2 Crawlers + 1 Spitter | Chemicals 10 |
| P6 | Safe bedside interaction | Research Data 10 |
| P7 | 1 Mutated Brute; warning and retreat before entry | Scrap 20, Components 10 |
| P8 | No extra enemy; close vent via free manual valve | Research Data 10, Standard Weapon Blueprint Fragment 1 |

Full-clear totals: Scrap 40, Components 30, Chemicals 40, Research Data 30, Medkits 2, one fragment. Max cargo: three common stacks + one Data stack + one Medkit stack + one fragment bundle = **6 CU**. No random boss, alien gear or hidden mandatory revive drop. First-clear ID `FC-HSP-SLICE-01` records knowledge/source discovery only; no unlisted bonus. A Pharmacy-only extraction is a valid main-objective success and can support recovery. Failed extraction uses normal rules; main manifest can be reacquired on a later retry if never banked.

## 6. Tutorial repair and reward ledger

`S` = Scrap, `C` = Components, `Ch` = Chemicals. Start: **300 S / 120 C / 40 Ch**, Food 100, Water 120, Supply 20, Credits 500, Data 0, residents 6. Existing Storage operates with +250 capacity for each common category. These are repairs to pre-existing tutorial rooms, explicitly cheaper than constructing new rooms. Balances mean stored plus unexpired Return Inbox entitlement; inbox resources must be claimed before spending. Initial Scrap 300 is grandfathered above the 250 category cap until spent; never delete its excess. Warehouse reward can overflow into the Return Inbox: spend from storage, then claim the remainder. Every debit below requires enough claimed stock; the ledger never makes inbox stock automatically spendable.

| Step | Change S / C / Ch | Balance S / C / Ch |
|---|---|---|
| Generator repair | -20 / -5 / 0 | 280 / 115 / 40 |
| Water repair | -20 / -5 / 0 | 260 / 110 / 40 |
| Living repair | -10 / 0 / 0 | 250 / 110 / 40 |
| Free first sector; Hydro L1 build | -80 / -15 / -10 | 170 / 95 / 30 |
| CCL2 | -20 / -5 / 0 | 150 / 90 / 30 |
| CCL3 | -30 / -10 / 0 | 120 / 80 / 30 |
| Radio repair before House Quick Scout | -20 / -10 / 0 | 100 / 70 / 30 |
| House all pickups + its cache, once | +160 / +75 / +30 | 260 / 145 / 60 |
| Workshop repair | -30 / -10 / -5 | 230 / 135 / 55 |
| First Workshop craft: 5 Supply (-5 Food/-6 Water,2min) | -2 / 0 / 0 | 228 / 135 / 55 |
| CCL4 | -40 / -10 / 0 | 188 / 125 / 55 |
| Clinic repair | -30 / -10 / -10 | 158 / 115 / 45 |
| Training repair | -20 / -5 / 0 | 138 / 110 / 45 |
| Living L1→L2 normal upgrade | -90 / -15 / 0 | 48 / 95 / 45 |
| Warehouse all pickups + its cache, once | +300 / +130 / +30 | 348 / 225 / 75 |
| Generator L1→L2 normal upgrade | -120 / -38 / 0 | 228 / 187 / 75 |
| Old Sensor sector depth -3 excavation + stabilization | -50 / -5 / 0 | 178 / 182 / 75 |
| Choose Restore old Sensor | -20 / -5 / 0 | **158 / 177 / 75** |

Sensor alternative Convert: no restore cost, no salvage reward; final **178 S / 182 C / 75 Ch**, blank controlled sector. Restore gives +5 percentage points to Radio confidence, still capped; it is not required for story signal or range. Both choices complete the tutorial. Radio is repaired once before House; minute 50–65 teaches searching with it, not a second repair charge.

Repair times: Generator/Water 30 sec each, Living 20 sec, Radio 60 sec, Workshop/Clinic 90 sec each, Training 60 sec; CCL2/3 upgrades30sec each; CCL4 upgrade1min. Repairs require one available worker, release worker at completion, and do not require the repaired room to be powered while under repair. Baseline new building/upgrade times remain in Buildings; two-hour checkpoints are targets, not automatic time skips.

House + Warehouse spend **14 Supply**; the required first Workshop craft adds5, leaving **11**. Its -5Food/-6Water/-2Scrap cost is included above. Optional Hospital then spends8, leaving3; do not craft or charge the same batch twice. Optional Hospital loot/spending is excluded from the main ledger. No paid currency or loot sale needed. Food/Water production and consumption are continuous, not lump-sum mission grants: the ledger above excludes both. With at most eight residents over two hours, consumption is at most 16 Food/19.2 Water before bonuses; the fixed loot adds30 Food/36Water and required packing spends5Food/6Water. Thus this route has a reserve even without counting production. Stockpile caps/overflow must still be honored; the ledger tracks cumulative entitlement, and cannot justify deleting overflow or bypassing its UI.

## 7. Extended slice: 2–4h, CCL5 / squad 4

First two hours end at CCL4, squad 3, 7–8 residents, recovered injury and signal hook. No CCL5/research is required for that checkpoint. The 18.4 km signal is a **nondeployable story hint**, an explicit antenna-event exception to normal scan radius; no free Radio L2/range unlock.

Extended objective `SLICE-ARCHIVE-01` uses Hospital P3/P4 medical manifest + data bundle. If Hospital is skipped, an authored Warehouse side-office follow-up offers the same unique objective bundle after a short 2-Crawler encounter, costing the same 8 Supply; it shares the claim ID, never pays twice. Its additional one-time completion reward is **200 Scrap, 80 Components, 10 Research Data**, paid after extraction. This is a curated slice grant, not repeatable economy income. Follow-up uses existing Warehouse rooms, no new biome.

CCL5 requirements follow Prototype Progression: CCL4, Warehouse objective clear, GeneratorL2 and LivingL2; cost **200 Scrap, 75 Components, 10 Data**, time5minutes. The authored extended slice additionally targets eight residents and completion of `SLICE-ARCHIVE-01` to demonstrate the branch and provide an affordable route; these are slice acceptance targets, not extra account-wide CCL gates. Build Research Lab L1 at normal cost **140 S / 50 C / 10 Ch**, 8 minutes. Generator L2 + Core gives 40 PU; active core rooms plus Clinic/Training/Research fit at or below 37 PU (suspend Workshop/Radio when idle if needed). Research `SUR-01 Efficient Hydroponics` costs 8 Data, 5 minutes. Data House2 + Warehouse10 + archive10 =22, minus CCL5 10 and research8 leaves4, even without counting Hospital Data.

The main ledger's 158 S /177 C /75 Ch plus archive200/80 leaves enough for CCL5 and Lab: **18 S /132 C /65 Ch** before optional Hospital/packing costs. Squad cap becomes4; choose Nam as Engineer trainee using IMPLEMENTATION_BASELINE_V0.1.md Training rules (5min, no fee; role respec at this prototype stage is free). A fourth member expands team options, not automatic completion of future combat tests. Extended-slice exit = CCL5, four legal squad slots, Lab powered, SUR-01 completed, one legal four-unit loadout, no negative inventory or unclaimed required grant. Main campaign after this remains separately gated.

## 8. Authoring and QA acceptance

- Every pickup/cache/first-clear/rescue/grant has its stable ID; atomically record extraction outcome and claimed IDs. Reconnect/reopen cannot duplicate grants, rescue Tùng/Hạnh twice or reroll remaining rooms.
- Complete both branch choices and a partial extract/retry. No key, enemy, resource or survivor needed for progression is behind the feature it unlocks.
- Confirm all six roster sums and eight stat fields; deploying the three fighters leaves exactly three initial production workers.
- Verify House/Warehouse supply totals, both cache contents included once, legal cargo <=12, beds 6→10 before overflow grace ends and initial gear available before Armory.
- Verify Radio before first Scout, CCL4 after first return, CCL5 only in extended slice; nondeployable 18.4km signal does not bypass future NPC Silo unlock.
- Timings, TTK and player comprehension remain **NOT VERIFIED** until implementation/playtest. Scripted outcomes are fixtures, not evidence of final balance.

## 9. Optional experiments — not required scope

1. **History keepsake:** append one short survivor-authored line after a first rescue or first retreat. Use existing History log; no new stat or reward.
2. **Emergency job preset:** one action assigns healthy idle residents to life support with a visible preview. Uses existing job rules and does not clone workers.
3. **Intel clue cards:** show two concise observed clues after a partial extraction, using Bestiary/Intel already earned. No extra currency or guaranteed full-map reveal.



