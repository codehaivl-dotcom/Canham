# BURROW ZERO — Gap Closure & Content Delivery

**Date:** 2026-11-12. Original audit baseline commit: `2aa6a080f8a463bf931023af5a67e08f7f6cd4d7`.
**Status:** Remediation authored locally; document consistency review and static validation recorded below. Runtime QA, combat simulation and playtest remain **NOT RUN**.

## 1. Scope and authority

User authorized fixing all fourteen independent-audit gaps and filling missing implementation content, with independent QA and ideas. Existing canonical direction remains: panda survivors, PvE complete without PvP, preparation/extraction, no hero-gacha/P2W. New tables are prototype baselines, not final live tuning.

Historical audits remain available with snapshot banners. Their original findings/line references identify the pre-remediation state; use current section links below for implementation. No percentage readiness estimate replaces measurable entry/exit criteria.

## 2. Closure matrix

“Specified” means a concrete document contract now exists. It does not mean an implemented build passed its acceptance tests.

| Gap | Document remediation | Authoritative current evidence | Runtime verification |
|---|---|---|---|
| GAP-01 death/body | Specified lethal state table, bleedout, one field revive, escort/cargo, wipe, base recovery and tutorial/defender exceptions | [Recovery](SURVIVOR_RECOVERY_V0.1.md), Units§22, GDD§34–35 | QA-01A/B/C NOT RUN |
| GAP-02 recovery | Specified rest rates, fatigue bands, timed/costed Clinic, offline queues, Emergency rescue and fallback staffing | [Recovery](SURVIVOR_RECOVERY_V0.1.md) | QA-02A/B/C NOT RUN |
| GAP-03 Scout ordering | Radio repaired before first Quick Scout; later beat teaches existing scan; repair cost/time included once | [Tutorial](TUTORIAL_FIRST_2H_V0.1.md), [Content](PROTOTYPE_CONTENT_PACK_V0.1.md) | QA-03 NOT RUN |
| GAP-04 slice scope | First2h CCL4/squad3; extended2–4h CCL5/squad4/Lab/one research; explicit costs and source fixtures | [Plan](DESIGN_PLAN.md), [Progression](PROTOTYPE_PROGRESSION_V0.1.md), Content§7 | QA-04 NOT RUN |
| GAP-05 sessions/rewards | Persisted outcomes, PvE pause/PvP deadline, extraction transaction, first-clear/claims, immutable cache and overflow inbox | [Mission Session](MISSION_SESSION_REWARDS_V0.1.md) | QA-05A/B/C NOT RUN |
| GAP-06 emergency power | Explicit8PU emergency loads, consumption waiver, automatic Manual Restart and repair band arithmetic | Progression§3, Buildings§4/24 | QA-06 NOT RUN |
| GAP-07 survival comeback | Life-support negative-modifier exemption, bounded relief, manual salvage, no-squad fallback and event-based offline timing | Progression§3–4, Economy§6–7 | QA-07A/B/C NOT RUN |
| GAP-08 Beacon | Guaranteed first source, CCL6 Command recipe, separately listed claim inputs, reservation/refund/consume predicates | [Resource Sites](RESOURCE_SITES_V0.1.md)§5 | QA-08A/B NOT RUN |
| GAP-09 consent | Explicit opt-in, all-tier private PvE sites, contested eligibility, shared account shield/lock, no revenge bypass | [PvP Protection](PVP_MATCHMAKING_PROTECTION_V0.1.md)§4–8 | QA-09 variants NOT RUN |
| GAP-10 loss cap | Fixed per-resource rolling24h caps, combined site/Silo reservations, actual extract debit and atomic release | PvP Protection§11 | QA-10 variants NOT RUN |
| GAP-11 defense cap | PvP5 fromCCL8; PvE4 atCCL6–7; real exclusive assignments, no duplicated gear | [Player Raid](PLAYER_PVP_RAID_V0.1.md)§4/8, [Security](SILO_DEFENSE_SECURITY_V0.1.md)§5 | QA-11 NOT RUN |
| GAP-12 resistance | All−30/−35 detail and summary-matrix values aligned to−25floor; adaptation clamp and damage example | [Enemy](ENEMIES_RESISTANCES_V0.1.md), [Implementation](IMPLEMENTATION_BASELINE_V0.1.md)§3 | QA-12 NOT RUN |
| GAP-13 Engineering UI | Engineering added to research navigation, seven branches remain canonical | [UI](UI_UX_NAVIGATION_V0.1.md)§13, [Research Catalog](PROTOTYPE_RESEARCH_CATALOG_V0.1.md) | QA-13 NOT RUN |
| GAP-14 site cadence | All buffers8h, free default automatic collection from first claim, same offline cap, overflow/no-deletion behavior | Resource Sites§7–8 | QA-14 variants NOT RUN |

## 3. Missing content filled

- Six named starting pandas and two authored rescues, legal stat totals/gear/jobs and no hidden worker clones.
- House4rooms, Warehouse6rooms, Hospital8rooms: graph, encounters, exits, pickups, cargo, rewards and retry identity.
- Tutorial repair/upgrade/reward ledger and extended slice affordability, Supply/ResearchData accounting.
- CCL2–12 cost/time/prerequisites; guaranteed private PvE boss/key sources with refresh rules.
- Thirty-four named research nodes: IDs, gates, prerequisites, costs, time, exact effect and source; matching recipe references.
- Prototype combat control, hit/armor/shield/status/action timing, boss add limits, XP thresholds and Training.
- Normal archetype loot weights/cache slots, blueprint pity, common sales and source clarity.
- Prologue+eight chapter contracts, faction intro/reputation/recovery, Mimic tutorial and Exposure baseline.
- PvP matchmaking/rating/league/reward/collusion arithmetic; site tier/Signal/soft-cap and defense construction/combat data.
- [QA regression matrix](QA_GAP_REGRESSION_V0.1.md) with fixtures and evidence rules. Optional ideas are listed separately in Content§9 and have no mandatory progression dependency.

## 4. Validation and limits

Run `python tools/validate_design_docs.py` from repository root. Checks local Markdown file targets, roster legality/totals, every tutorial ledger balance, extended affordability/Supply, all34 unique research IDs and prerequisite depth/cycles, loot weight totals, removed obsolete resistance data, Engineering navigation and NOT RUN runtime labels. Also run `git diff --check`.

Final local check: **68/68 static checks passed**, including file and section-link targets; `git diff --check` passed. Independent QA verdict: **DOCUMENT CLOSURE ACCEPTED for GAP-01–14 within prototype scope**, recorded in [QA rereview](QA_GAP_REGRESSION_V0.1.md). Its25 regression cases remain NOT RUN. The four follow-ups found during remediation—CH02 grant ordering, formation legality, resistance summary data and failed finite-loot retry—were corrected and independently rechecked.

These static checks can catch authoring errors. They cannot prove TTK, feel, session pacing, persistence correctness, backend security or anti-collusion effectiveness. GAP-14 collection rules are specified; actual player cadence remains a playtest hypothesis. No runtime PASS or live-balance claim is made.

## 5. Remaining production work

No original audit gap is deferred merely because its behavior is inconvenient to specify. Implementation and verification remain separate work: build core slice, run regression matrix, run combat/economy simulations, playtest pacing/accessibility/localization, and tune baselines from evidence. Architecture must choose engine/provider/storage while implementing the already specified gameplay invariants. Commercial pricing/platform order, final dialogue/asset production and full late-season/Coalition authored content remain explicit later product/production milestones; this change does not claim to deliver a finished game.
