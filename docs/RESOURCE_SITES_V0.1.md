# BURROW ZERO — Resource Sites & Contest v0.1

**Status:** Prototype design baseline  
**Scope:** capture, production, defense, discovery and contest of external resource sites.

---

# 1. Purpose

Resource Sites are the bridge between PvE economy and PvP conflict.

They must answer:

> "Why would another Silo care about the same place I care about?"

A Resource Site is not a one-time dungeon. It is a temporary strategic asset.

---

# 2. Lifecycle

```
DISCOVER
→ SCOUT
→ CLEAR
→ CLAIM
→ STABILIZE
→ DEPLOY WORKERS
→ PRODUCE
→ DEFEND / HIDE / FORTIFY
→ PVE CHALLENGE / OPTIONAL CONTESTED-PVP RAID
→ RETAIN / LOSE / ABANDON
```

Player may abandon voluntarily.

---

# 3. Site Types

| Site | Main output | Risk identity |
|---|---|---|
| Scrapyard | Scrap | common, low risk |
| Chemical Plant | Chemicals | toxic hazard |
| Water Facility | Water | strategic utility |
| Solar Farm | Energy Cells | exposed, easy to detect |
| Data Center | Research Data | tech defense |
| Military Salvage Yard | Components + Military Data | high defense |
| Uranium Mine | Reactor Material | rare, noisy |
| Alien Crater | Alien Material | extreme signal |

---

# 4. Site Tiers & Ownership Mode

| Tier | Earliest CCL | TierMultiplier | Worker slots | Defense Capacity |
|---|---:|---:|---:|---:|
| I | 6 | 1.00× | 2 | 20 |
| II | 7 | 1.25× | 3 | 35 |
| III | 8 | 1.50× | 4 | 55 |
| IV | 10 | 2.00× | 5 | 80 |

Tier and mode are fixed on node generation, never scaled to the visiting player. Economy base outputs are Tier I values. Access also requires the material's normal story/research progression; an early Tier I node does not grant early Alien tech.

Every node displays one immutable ownership mode before deployment:

- **Private PvE:** account-instanced; no other player can discover, raid, capture or convert it to contested. Remains private after claim and after optional account PvP opt-in. All tiers and strategic material families have private PvE routes as their story gates open.
- **Contested PvP:** only CCL8+ opted-in accounts may discover actionable ownership, claim or attack. Neutral contested nodes remain in this mode after claim. Claimed contested sites use the complete account-wide PvP eligibility, shields, charges and loss ledger in PVP_MATCHMAKING_PROTECTION.

PvE-only play is permanent and viable. Contested nodes offer rivalry/prestige and a 1.10× economic-efficiency output control modifier, not unique progression or exclusive mandatory materials.

---

# 5. Clear, Claim & Claim Beacon

Claim requires CCL6+, accessible tier, cleared local threat, restored control terminal, basic infrastructure and all tier worker slots available before production begins. Private PvE claim never spends a Raid Charge or opts into PvP. Claiming a neutral contested node requires account PvP eligibility and grants its ownership shield on success; it spends claim resources but no attack charge because no player defender exists.

**Beacon acquisition:** the CCL6 objective “Secure an External Supply” grants one Claim Beacon directly, guaranteed once per account, after showing the claim tutorial. From CCL6, Command Core emergency crafting always offers 1 Claim Beacon = 25 Scrap + 5 Components, 5 minutes, queue1 shared with emergency Supply packing. No Workshop, research, PvP, RNG drop or premium payment is required.

**Claim action cost:** 10 Supply + 25 Scrap + 5 Components + 1 already-owned Claim Beacon. Beacon recipe cost is paid only when crafting that item; the claim panel never charges that recipe a second time. Thus a crafted Beacon plus one claim costs a total50 Scrap/10 Components/10 Supply; using the guaranteed first Beacon costs25 Scrap/5 Components/10 Supply.

Reserve all action inputs atomically when claim begins. Consume once only when claim completes successfully. Cancel, interruption, target invalidation or a failed control event releases the reserved inputs including the Beacon. Previously spent expedition Supply/consumables are not refunded. Reconnect resumes the same claim ID; retry cannot duplicate ownership or rewards.

| Tier | Claim time |
|---|---:|
| I | 1 min |
| II | 2 min |
| III | 4 min |
| IV | 6 min |

PvE events can interrupt claim. A claim transaction locks that node; another claim cannot race it. Hostile player capture uses one reserved Beacon plus the same claim-action resources, and consumes them only at successful capture settlement; the attack's Raid Charge/Supply remain separate.

---

# 6. Workers

Each site needs deployed survivors.

Prototype:

| Tier | Worker slots |
|---|---:|
| I | 2 |
| II | 3 |
| III | 4 |
| IV | 5 |

Worker efficiency uses relevant base stats.

| Site | Primary | Secondary |
|---|---|---|
| Scrapyard | TEC | END |
| Chemical Plant | TEC | INT |
| Water Facility | TEC | INT |
| Solar Farm | TEC | INT |
| Data Center | INT | TEC |
| Military Salvage Yard | TEC | COM |
| Uranium Mine | END | TEC |
| Alien Crater | INT | RES |

Workers remain unavailable for normal Silo jobs, Silo defense or expedition while assigned. Guards use up to2 additional exclusive survivor slots (not worker slots); they retain their real level, stats and equipped gear, with normal unit formulas and AI targeting. No NPC guard stat generation or bonus copy. Cannot assign the same survivor/gear at two sites. A raid snapshot locks site assignments until settlement; unassign/recall is unavailable during that lock.

They are not permanently killed by offline PvP defense.

---

# 7. Production

```
Final Output[r]/h = Economy Base Output[r]/h * Tier Multiplier
                     * Mean Worker Efficiency * Integrity Modifier * Control Modifier * OwnershipEfficiency
```

All required worker slots must be occupied by available living survivors; otherwise output0. Mean Worker Efficiency uses the Population job-efficiency contract, with relevant stat = arithmetic mean of the site Primary and Secondary stats from §6; average final efficiency across all occupied required slots. Private PvE Control Modifier=1.00; contested=1.10. OwnershipEfficiency is §17; Hide factor is0.90 when §9 Hide selected, otherwise1.00, multiplied last. No bonus is applied twice. Integrity is measured on0–100:

| Integrity | Modifier |
|---|---:|
| 100 | 1.00 |
| 75 to <100 | 0.90 |
| 50 to <75 | 0.75 |
| 25 to <50 | 0.50 |
| 0 to <25 | 0 |

Track fractional production internally; display whole units and keep remainder. Site production, worker consumption and auto-collection advance in the same first8 real hours after last active session as Silo offline economy, then freeze until return. Reopening does not replay already processed time. PvP clocks/shields continue in real time even after economy freezes.

---

# 8. Storage, Collection & Overflow

All tiers hold **8 hours of their full-integrity output at current staffing/tier/control/ownership/Hide modifiers**. Capacity is recalculated when modifiers change; existing contents are never deleted if the new capacity is smaller. Production pauses for a full resource buffer; stored stock remains collectible. Fractions remain in the production accumulator.

From the first claimed site, free automatic collection is enabled by default every8 simulated production hours, with a visible “Collect now” option. Collection needs no extra worker, Supply, journey, technology or online check-in. Manual collection resets that site's next8h interval and does not accelerate production. At the exact offline boundary, process production up to8h, then due collection, then freeze; one long offline absence does not simulate successive8h windows. Example: TierI private Scrapyard, efficiency1, integrity100, yields144 Scrap over8h and auto-transfers144 once. Returning after16h gives the same144, not288.

The account can disable automatic collection deliberately; UI warns that the buffer will fill. Theft-reserved portions cannot be collected. Transfer available stock and retain the reservation at the site. Once raid settlement releases reservations, an overdue automatic collection runs immediately during an active production window; beyond the offline cap it waits until login.

Collected stock above Silo capacity enters a protected **Return Inbox** overflow inbox. It cannot be stolen, spent or used for crafting until player chooses Store (when room exists), Sell or Discard. No expiry or auto-deletion. Site inbox entries do not count toward the three uncleared mission-return manifest limit in MISSION_SESSION_REWARDS_V0.1.md, but cannot bypass the site buffer or first8h offline production cap. New site production still follows its normal local capacity. Show the overflow warning and one combined collection summary, never repeated timer alerts. Site raids expose only their own local unreserved buffer, never this inbox or main Silo storage.

---

# 9. Noise / Signal

```
Signal = clamp(BaseSignal + 5 * TierIndex
               + ceil(10 * TierMultiplier * MeanWorkerEfficiency * ControlModifier)
               + ceil(InstalledDefenseCapacityCost / 5)
               + 10 * ExcessSites - Concealment, 0, 100)
```

TierIndex I=0/II=1/III=2/IV=3; TierMultiplier is §4. Concealment=10 while “Hide” is selected, otherwise0. Hide costs no resource but multiplies production by0.90; expose this as a separate output factor, never change the economic ControlModifier. Switching Hide updates output/signal immediately without resetting collection timers. Production term=0 when offline/unworked. Installed defenses count while built even when unpowered.

| Site | BaseSignal |
|---|---:|
| Scrapyard | 10 |
| Chemical Plant | 20 |
| Water Facility | 15 |
| Solar Farm | 30 |
| Data Center | 25 |
| Military Salvage Yard | 30 |
| Uranium Mine | 40 |
| Alien Crater | 50 |

Signal0–24 LOW,25–49 MEDIUM,50–74 HIGH,75–100 EXTREME. Discovery ranking among otherwise legal contested targets uses higher Signal first, then distance, then nodeID. A completed Radio Search returns up to3 eligible nodes in range by that order; if none, no contested signature. This signal ordering never bypasses PvP consent/CCL/shield/private-mode checks. Private nodes use signal only for PvE event flavor in this prototype; it never exposes them to players.

Example: contested TierI Scrapyard, efficiency1, no defenses/excess, Visible →10+ceil(11)=21 LOW. Hide →11 LOW and output19.8×0.90=17.82 Scrap/h.

---

# 10. Discovery by Other Players

A player does not see every owned site globally.

Discovery sources:

- Radio Scan;
- World Intel;
- faction rumors;
- route proximity;
- high Signal;
- PvP revenge intel.

Discovery result is imperfect:

```
ACTIVE RESOURCE SIGNATURE
Type: likely Industrial
Owner strength: estimated
Output: unknown
Defense: partial
```

---

# 11. Defense

Defense uses a small site-specific budget.

Options:

- 1–2 guards;
- turret;
- reinforced gate;
- sensor;
- alarm;
- drone;
- Shock Trap from the security catalog; no additional mine item in this baseline.

Defense Capacity by tier:

| Tier | Defense Capacity |
|---|---:|
| I | 20 |
| II | 35 |
| III | 55 |
| IV | 80 |

Defense uses the exact SILO_DEFENSE_SECURITY catalog capacity/build/combat values, within the smaller site budget; no free Power grid dependency at a site: installed security has a local integrated supply, so its listed Power is descriptive equivalent rather than extra Silo load. Disabling the site terminal shuts electronic defenses off for10sec; Engineer interaction takes5sec and succeeds deterministically after the room is cleared. Site guards follow exclusive assignments in §6; workers do not add free combat bodies. Site capacity cannot be pooled with Silo capacity.

---

# 12. Contest Window

Only a contested node can receive a player raid. Both accounts must be CCL8+, explicitly opted in, within the hard CCL±1 band and outside the same Alliance. Defender account shields and the shared single-incoming-raid lock cover Silo AND every site. Attacker requires one shared Raid Charge and Supply; one outgoing PvP raid per account. Full predicates, reservation,15m attack deadline and successful-extraction settlement are defined in PVP_MATCHMAKING_PROTECTION §4–11.

CCL6–7 owners and CCL8 non-opted-in owners have only private PvE ownership. Taking a neutral private site never removes protection. PvE opponents/events may challenge private ownership under PvE rules; no player can do so, including through Revenge or shared intel.

---

# 13. Raid Outcomes

Choose exactly one objective before deployment:

- **Plunder:** extract eligible Scrap/Components/Chemicals, within §16 and account cap. No capture or sabotage.
- **Disrupt:** control the terminal and extract; integrity loses20 percentage points, floored25, and production pauses15 real minutes. Repeated disruption uses max remaining pause, never additive stacking. No theft/capture.
- **Capture:** defeat site defenders, secure control terminal, complete the tier claim time and successfully extract. Reserve §5 claim resources/Beacon at deployment. Consume them and transfer ownership only in the extraction transaction. Failure/interruption releases claim reservations; spent attack deployment costs remain spent. No plunder or extra defender resource reward.

Capture is available against an eligible unshielded contested owner; no separate undefined “vulnerable enough” state. Workers return safely to prior owner with Fatigue +20 and PROTECTED_INJURED (15 min free recovery) under SURVIVOR_RECOVERY_V0.1.md; no body or gear loss. Existing unlooted buffer belongs to the prior owner and transfers to main storage/Return Inbox at settlement. Captor starts with empty buffer, integrity100 and must assign its own workers. No free worker or stored-output transfer.

---

# 14. Capture Protection

Successful contested claim/capture grants the new owner's entire account a6h shield; applies to its Silo and all contested sites. The losing owner receives6h post-capture shield. Use maximum with any longer current/chain shield, never replace with a shorter duration. Launching an accepted offensive PvP deployment ends the launcher's timed shield across all assets.

Original owner receives2h reclaim-priority intel and a normal24h Revenge token. Intel does not bypass the new owner's6h shield; the token may be used later if still valid and eligible. Every reclaim spends a normal Raid Charge and claim inputs and follows consent, CCL, Alliance, cooldown and incoming-lock checks. Private PvE sites never participate in this cycle.

---

# 15. Loss Rules

Losing a contested site cannot kill assigned workers/guards permanently, remove Silo buildings or debit main-base stock. Defender site units return with Fatigue +20 and PROTECTED_INJURED (15 min free recovery, no body/gear loss); loot/ownership effects occur only after successful attacker extraction. Defenders remain ineligible for a new assignment until the settlement and normal recovery rules permit it.

Only §13's selected objective is applied. Strategic resources and all survival resources are non-stealable. Combat Data/Credits/cache prestige rewards are system-generated and never subtracted from the defender. Failed extraction gives no capture, plunder or disruption-objective reward.

---

# 16. Plunder Cap

Use the shared per-resource rolling24h loss ledger in PVP_MATCHMAKING_PROTECTION §11. Eligible local stock is only Scrap, Components and Chemicals:

```
SiteExposure[r] = min(floor(10% * unreserved local buffer[r]),
                      floor(2 * current hourly site output[r]),
                      remaining account rolling24h cap[r])
```

Everything else, including Alien Material and Reactor Material, has exposure0. No30% exception or separate strategic daily cap exists. Silo/site raids cannot stack separate account budgets.

Example: efficiency1 TierI private Scrapyard cannot be player-raided at all. Equivalent contested Scrapyard output19.8/h with buffer158 and unused CCL8 Scrap cap60 exposes min(15,39,60)=15; carrying10 and successfully extracting debits10 once. Failed extraction debits0. Collection/spending cannot access reserved15 until settlement releases it.

---

# 17. Multi-Site Ownership

Soft cap:

| CCL | Efficient sites |
|---|---:|
| 6 | 1 |
| 7 | 2 |
| 8–9 | 3 |
| 10+ | 4 |

Count all owned productive sites (private and contested) against the same account soft cap. `ExcessSites = max(0, OwnedSiteCount - EfficientSitesAtCCL)`; include claimed sites even if workers removed, hidden or temporarily offline, so toggling staffing cannot evade it.

`OwnershipEfficiency = max(0.50, 1 - 0.10 * ExcessSites)` applies to every owned site's output. Required worker slots remain the fixed §4 values; there is no additional undefined worker-cost multiplier. Signal gets+10 per excess site via §9. No hard ownership cap in this prototype.

Example: CCL6 owns3 sites, efficient cap1 →ExcessSites2, output factor0.80 and Signal+20 at each site. Abandoning one restores factor0.90, without deleting already stored output. Apply changes prospectively at the ownership event timestamp.

---

# 18. Abandon

Abandon is available outside an active incoming raid/claim transaction. It returns workers and transfers all unreserved local contents through normal storage/Return Inbox handling, with no Supply/cargo tax. The site becomes neutral after1 real hour; private PvE mode remains private. No reward or Beacon refund for voluntarily relinquishing completed ownership. During a raid, the button explains that abandonment must wait for settlement; it cannot cancel a defender loss reservation.

---

# 19. PvE-only Access & Acceptance Examples

Private PvE sites exist across all tiers/material families as their progression gates open. Neutral/faction/private opportunity labels never secretly convert a private node into a contested asset. An opted-in player may still choose exclusively private sites; PvP opt-in affects the Silo and explicitly contested sites only.

Required document-level acceptance cases:

1. CCL6 account completes guaranteed Beacon objective, clears TierI private site and claims with10 Supply/25 Scrap/5 Components/1 Beacon. No PvP or research prerequisite.
2. Interrupt claim at50%: release all claim inputs, ownership stays neutral. Repeat completion message: no double consumption.
3. CCL7 site is not discoverable as a player attack target. CCL8 without opt-in is still protected. Opt-in does not convert any existing private sites.
4. Opted-in CCL8 holds a contested site; its6h ownership shield blocks Silo/site/Revenge attacks. A rejected attack does not spend charge or remove shield.
5. Two incoming attacks at different assets: only one accepted; loss reservations and24h cap remain shared.
6. At8h offline TierI production is collected once;16h absence generates only8h output. Full main storage preserves collection in Return Inbox.
7. Failed capture refunds reserved Beacon/claim resources, keeps old owner/buffer and gives no objective reward. Successful capture transfers unlooted buffer to old owner, not attacker.

These are expected behavior for implementation QA, not claims that a runtime build has passed.

---

# 20. Success Criteria

Resource Sites work if:

1. there is a real reason to hold them;
2. worker allocation matters;
3. high output creates exposure;
4. PvP arises from economy;
5. defeat hurts but does not erase progress;
6. PvE-only players still have viable progression.
