# BURROW ZERO — Gap Regression QA v0.1

**Date:** 2026-11-12  
**Scope:** regression requirements derived from GAP-01–14 in [Independent Audit](INDEPENDENT_AUDIT_2026-11-12.md).  
**Execution status:** **NOT RUN**. This is a test design, not evidence of a working build or balance approval.

## Evidence and execution rules

- Read [Canonical Rules](CANONICAL_RULES_V0.1.md) and the dedicated current contract before executing. The historical audit describes the original gaps and does not override corrected specifications.
- Record build/commit, fixture version, seed, simulation clock, action/event log, inventory/roster before and after, and observed result for each execution.
- All rows start **NOT RUN**. Change a row to PASS/FAIL/BLOCKED only with linked execution evidence. A document review alone cannot make a runtime test PASS.
- Use a controllable clock and deterministic random seed. “Reload” means terminate the client/process and reopen the same persistent account, not create a fresh account.
- Values described as “documented baseline” must be copied from the implemented contract into the fixture before testing; absent values make the test BLOCKED, not permission for the tester to invent a rule.
- Test fixtures may use setup tools to construct state, but progression walkthroughs must not use debug unlocks or resource grants during execution.

## Fixtures

| ID | Setup |
|---|---|
| F-NEW | Fresh tutorial account: CCL1, six curated survivors, starting resources and rooms from Economy/Buildings; no purchases or prior unlocks. |
| F-DEATH | Non-tutorial PvE mission, three named survivors, fixed enemy damage and recoverable encounter, one Revival Injector, visible cargo and equipment ledger. |
| F-REST | Three survivors with Fatigue81; one injured, one Trauma, one healthy; ClinicL1 with controllable power, beds and treatment resources. |
| F-RECOVER | Silo with damaged/offline Generator, zero Battery, minimal Food/Water/Supply/materials, no combat-ready expedition squad; Emergency Core intact. |
| F-SITE | CCL6 PvE-only account with no PvP consent, first neutral site cleared, required claim resources, no Claim Beacon initially. |
| F-PVP | CCL8 accounts A/B/C, explicit consent states, eligible match bands, known stockpiles, account-wide loss ledger and fixed raid snapshots. |
| F-REWARD | Fixed expedition seed with material loot, cache, first-clear reward, Blueprint progress and one injury; supports interrupting each settlement step. |
| F-DAMAGE | Fixed weapon/raw hit100, no armor/buffs/crits; enemies with resistance values including former −30%/−35% rows. |
| F-SITE-TIME | Owned TierI site, known output modifiers, empty local buffer; collect and production clocks controllable. |

## Regression matrix

| Test / requirement | Fixture | Steps | Expected result | Status |
|---|---|---|---|---|
| QA-01A / GAP-01: lethal state | F-DEATH | Apply lethal damage; inspect transition; repeat with each documented lethal/recovery exception. | Exactly one documented state per event; HP, body, gear, deploy eligibility and recovery deadline match the same transition. No ambiguous DOWN/DEAD interpretation. | NOT RUN |
| QA-01B / GAP-01: revive and second lethal | F-DEATH | Revive once; apply second lethal; attempt second field revive; attempt extraction with body. | One successful field revive per survivor/mission; second attempt cannot duplicate use or bypass cap. Body extraction follows explicit carrier/cargo rules; gear has exactly one owner. | NOT RUN |
| QA-01C / GAP-01: abandonment and wipe | F-DEATH | Branch from same seed: abandon body; extract body; wipe squad. Inspect roster, inventory and rescue state. | Each branch resolves once to documented permanent/recoverable/lost state. Wipe creates no alive carrier, duplicate equipment or free resurrection. Body return does not silently imply immediate full recovery. | NOT RUN |
| QA-02A / GAP-02: rest and treatment clock | F-REST | Rest to just before/at redeploy threshold; occupy all Clinic beds; remove power; restore power; repeat with offline interval. | Baseline recovery is calculable; queue, costs, progress suspension and offline elapsed time match contract. No healing through an unpowered/full Clinic unless explicitly allowed. | NOT RUN |
| QA-02B / GAP-02: Emergency bypass | F-REST | Attempt Emergency redeploy repeatedly; reload; compare fatigue, HP, penalties and eligibility. | Emergency has explicit eligibility/cost/consequence and cannot be reset through reload or toggling assignment. No unlimited free fatigue removal. | NOT RUN |
| QA-02C / GAP-02: playable return loop | F-NEW | Complete two short runs and one curated failed run using baseline treatment/rest; inspect next actions. | At least one documented recovery or expedition action remains achievable without premium aid; no required survivor is trapped indefinitely by missing recovery rule. | NOT RUN |
| QA-03 / GAP-03: Scout operational sequence | F-NEW | Follow onboarding in order until first and second Quick Scout; inspect Radio state and all required currencies. | Radio/scouting facility is operational before each required Scout. No hidden facility grant or debug unlock; later Radio objective describes a distinct upgrade/scan milestone. | NOT RUN |
| QA-04 / GAP-04: slice manifest | F-NEW | Compare tutorial endpoint and integrated-slice endpoint; play each manifest to completion. | Each has one authoritative CCL/squad/system checklist. Tutorial completion and extended-slice completion are distinct if endpoints differ; research/squad4 are required only at the declared endpoint. | NOT RUN |
| QA-05A / GAP-05: interrupted mission | F-REWARD | Force-close after Deploy debit, at lethal hit, after room clear, and during extraction; resume each state. | Mission/consumables/deaths/loot remain at committed state. Reload cannot reroll, refund a committed deployment, undo lethal resolution or replay rewards. | NOT RUN |
| QA-05B / GAP-05: interrupted reward | F-REWARD | Force-close before/after return settlement and each cache reveal; replay settlement/claim request. | Same cache contents return, reveal order changes no contents, and each inventory/progression/first-clear award is credited at most once. Already committed loot cannot disappear. | NOT RUN |
| QA-05C / GAP-05: expiry and suspension | F-REWARD | Suspend within temporary target; advance clock across expiry and suspension limit; resume or abandon. | Target protection/suspension expiry and automatic resolution follow documented rules; clients cannot freeze world resources indefinitely or escape consequences by remaining disconnected. | NOT RUN |
| QA-06 / GAP-06: Emergency Core fallback | F-RECOVER | Disable Generator and exhaust Battery; inspect emergency load shedding; execute documented restoration path. | Emergency state has an explicit power budget and achievable recovery path. Water/Food guarantees do not assume simultaneously powered loads exceeding available PU. | NOT RUN |
| QA-07A / GAP-07: depleted economy comeback | F-RECOVER | Set Food/Water/Supply0; apply relevant shortage durations, fatigue and injuries; execute recovery. | At least one no-premium, no-combat-ready-squad route restores survival/logistics. Penalty stacking and life-support exemptions match contract; no self-maintaining production deficit blocks all actions. | NOT RUN |
| QA-07B / GAP-07: recovery grant abuse | F-RECOVER | Repeat reconnect, clock-boundary crossing, room toggles and resource spending around emergency recovery eligibility. | Any rescue grant/action honors documented cooldown/account limits and resource caps; no duplication or profitable recycle loop. | NOT RUN |
| QA-07C / GAP-07: offline event order | F-RECOVER | Simulate eight hours once and as eight one-hour intervals, including storage-full, shortage and power changes. | Equivalent time/events produce equivalent state within documented rounding. Production resumes after consumption frees capacity; stockpiles never go negative. | NOT RUN |
| QA-08A / GAP-08: first Claim Beacon | F-SITE | Obtain Beacon through documented PvE source/recipe; claim site without PvP. | All inputs/unlocks exist at CCL6; Beacon/source information is visible; first claim is possible without a PvP-exclusive item. | NOT RUN |
| QA-08B / GAP-08: interrupted claim | F-SITE | Interrupt before start, during claim, after success; replay success; abandon/capture branch. | Resource/Beacon reservation, consumption and refunds follow one rule; exactly one owner and no duplicate Beacon/refund. | NOT RUN |
| QA-09 / GAP-09: consent eligibility | F-SITE, F-PVP | Try Silo raid and site plunder/disrupt/capture against CCL6/7, CCL8 unconsented, opted-in, shielded and PvE-instance owners; attempt revenge/reclaim. | Each action matches published eligibility matrix. Site ownership does not silently opt a PvE-only player into attack eligibility. Revenge cannot bypass consent/CCL protections. | NOT RUN |
| QA-10A / GAP-10: loss limits | F-PVP | Attack B with each eligible resource category and compare exposed pool, remaining daily budget and actual extracted loot. | Per-resource caps and non-stealable categories use explicit units and a reproducible snapshot. Defender debit and attacker credit derive from the same settlement. | NOT RUN |
| QA-10B / GAP-10: concurrent settlement | F-PVP | A/C start attacks on B together; one fails extraction; one succeeds; cross daily-cap boundary. | Reservations/commit/release never exceed account-wide cap or create resources; failed extraction follows documented debit policy; rollover cannot double available budget. | NOT RUN |
| QA-10C / GAP-10: snapshot and reservation expiry | F-PVP | Start raid; defender changes layout/gear/resources; attacker disconnects until reservation expires; send stale settlement. | Raid uses one documented immutable snapshot; stale settlement cannot debit new state or bypass shield/cap. Expired reservation cannot grief-lock defender or settle twice. | NOT RUN |
| QA-11 / GAP-11: defense cap | F-PVP | At first PvP unlock and each later defense milestone, assign cap and cap+1; compare offense squad cap. | Exactly one documented defense cap per milestone; UI, defender snapshot and simulation agree; excess assignment is rejected explicitly. | NOT RUN |
| QA-12 / GAP-12: resistance validation | F-DAMAGE | Validate every enemy resistance row; hit former out-of-band enemies; compare computed damage with worked example. | Data fits declared bounds or named explicit exceptions; damage formula applies the same rule. No silent clamp/table disagreement. | NOT RUN |
| QA-13 / GAP-13: Engineering navigation | Appropriate research-unlocked account | Open Research by each supported navigation/input mode; locate Engineering nodes; switch VI/EN. | Engineering exists as a branch or explicitly documented merged group; every node is reachable and displays requirements/effect/source hint. | NOT RUN |
| QA-14 / GAP-14: collection cadence | F-SITE-TIME | Simulate sessions eight and twelve hours apart; fill buffer; collect; repeat with logistics upgrade and offline cap. | Buffer/overflow/collection rules are explicit; no auto-deletion without documented UI. Measured output loss and required check-ins are recorded for pacing review rather than presumed balanced. | NOT RUN |

## Acceptance and handoff

- Document closure: every GAP-01–14 maps to one explicit rule, a deliberately scoped deferral with a milestone, or a measurable playtest hypothesis. Document closure is separate from runtime verification.
- Vertical-slice runtime exit: required tests QA-01–07 and QA-12–13 have evidence; no unresolved critical loss/duplication, inaccessible tutorial action or recovery deadlock. Tests for deferred features remain NOT RUN with their feature milestone recorded.
- Resource Site/PvP exit: QA-08–11 must run before those features become player-accessible. QA-14 requires observed cadence feedback before claiming collection pacing is validated.
- A QA report must state tested scope, unresolved failures, evidence links and unexecuted tests. Never call this matrix a runtime sign-off by itself.

## Independent document rereview — 2026-11-12

**Method:** read concrete revised Recovery, Mission Session, Progression, Content Pack, Research Catalog, Implementation Baseline, Campaign Catalog and PvP/site contracts; compare critical source rules and walk the CCL gate chain. This is static document review. All execution statuses in the matrix remain **NOT RUN**.

The revised documents provide explicit contracts for the original gaps: deterministic death/body ownership, timed treatment/rest, Radio before Scout, separate tutorial/extended-slice endpoints, immutable reward settlement, emergency power and survival recovery, obtainable Claim Beacons, explicit permanent PvP consent, shared per-resource loss budgets, defense cap5, bounded resistance, seven research branches and eight-hour site collection. These additions close the missing-rule category only after the cross-document corrections below are verified.

Independent rereview raised four concrete follow-ups to the author:

1. CH02 must award the shared archive bundle when its manifest is banked, before the separate CCL5 completion check; deferring that grant to chapter completion creates a cost/reward cycle.
2. The five-slot formation rule must permit the authored squad3 Vanguard Front / Assault Mid / Medic Back loadout, or the authored loadout must change explicitly.
3. Enemy Full Resistance Matrix must match the corrected detailed tables: Auto Turret, Repair Drone and War Machine Electric resistance all −25%.
4. Finite authored pickup IDs must distinguish field acquisition from permanent banking. Failed extraction must not permanently erase a required unbanked cache/manifest/rescue reward; partial success must not respawn already banked rewards.

Earlier rereview checks also requested a consistent Generator25%-integrity example (16PU + Core8 =24PU), PvP timeout only when currently at a cleared valid exit, and defender assignment exclusivity. These were observed corrected in the working documents. Runtime behavior and balance remain unverified.

CCL source-chain review found independent pre-gate routes: Authorization at5→CCL6, Hive Core6→7, NPC09/RadioL3 at7→8, AI Core8→9, Neural Core9→10, Archive10→11 and a repeat Archive for12. This is dependency analysis, not proof that encounter difficulty or elapsed playtime is viable.

### Final verification of rereview follow-ups

**Verdict: DOCUMENT CLOSURE ACCEPTED for GAP-01–14, within the declared prototype scope. Runtime QA: NOT RUN.**

| Follow-up | Verified final evidence | Document result |
|---|---|---|
| CH02 cost/reward cycle | Campaign Contract Catalog §1 explicitly banks the shared archive reward before CCL5, then completes CH02 at CCL5 with no second grant | Resolved |
| Tutorial legal formation | Implementation Baseline §2 permits any legal 3/4/5 occupied slots with one Front; explicitly permits Vanguard Front, Assault Mid, Medic Back | Resolved |
| Resistance summary drift | Enemy Full Resistance Matrix rows Auto Turret, Repair Drone and War Machine match detailed Electric values −25% | Resolved |
| Finite authored reward loss | Content Pack §2 resets failed unbanked pickups/cache/rescue with same ID/outcome, preserves banked IDs, and charges spent Supply/consumables normally | Resolved |

The matrix contains **25 executable regression cases**, all still NOT RUN. The acceptance above means the reviewed missing-rule gaps now have concrete, mutually reconciled design answers; it does not certify final balance, completed content, engineering architecture, runtime correctness or absence of other future gaps. GAP-14 pacing remains a playtest hypothesis even though buffer/collection rules are now specified. Static whitespace validation (`git diff --check`) passed at rereview.
