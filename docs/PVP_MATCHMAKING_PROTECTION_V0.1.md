# BURROW ZERO — PvP Matchmaking, Protection, Loss & Revenge v0.1

**Status:** Prototype policy baseline

---

# 1. Goals

Matchmaking should:

- avoid high-level crushing new players;
- preserve target variety;
- create fair but not perfectly mirrored fights;
- prevent repeated harassment.

---

# 2. Match Score

All values below are deterministic prototype matchmaking measures, not player-facing gear rarity or combat balance claims.

```
UnitPower = floor(MaxHP / 10 + 2 * WeaponBaseDPS + Armor / 2)
SquadPower = sum(UnitPower of selected defense squad)
TechTier = highest unlocked general research tier (0 if none; I=1,...V=5)
MatchScore = 1000 * HighestCCL + PeakDefenseRating + PeakSquadPower
             + 25 * TechTier + floor(CurrentPvPRating / 20)
```

Use HP after permanent gear/role bonuses but before temporary injuries/buffs, WeaponBaseDPS = damage/interval from the equipped primary weapon (ignore crit/AOE/temporary buffs), Armor = equipped armor value. Empty defense slots score0. Compute on every permanent roster/gear/defense change; retain timestamped maxima over the last7 real days. Historical CCL/TechTier never decrease. No total account wealth input.

Search at0–59sec requires highest CCL±1, PeakDefenseRating ratio0.8–1.2 (use max(1,rating) in denominator), and rating difference≤300. At60–119sec expand defense ratio0.6–1.4/rating difference≤600. At120sec remove only these two soft bands. Never relax CCL, consent, shield, Alliance, cooldown or incoming-lock predicates. Eligible candidates sort by absolute MatchScore difference, then oldest last-targeted timestamp, then stable accountID; offer at most3. If none, return “No eligible target” without charge/Supply cost.

Example: CCL8, PeakDefenseRating100, PeakSquadPower400, TechTierIII, rating1,000 → MatchScore8625. A CCL10 target is always excluded despite a smaller score difference.

---

# 3. Defense Rating

```
DefenseRating = 2 * total installed defense Capacity cost
                + 5 * highest Security Room level
                + 10 * BackupCellCount
                + 5 * completed security research nodes
```

Count legal built objects even if temporarily disabled/unpowered, count Backup Cells separately only when built, and cap completed security-node contribution at25. Guards' survivor stats belong to SquadPower, never count them twice here. Invalid/unpublished layouts cannot enter the target pool. Matchmaking uses the7day peak rating, not the lower live value; removing defenses cannot immediately sandbag. Guard-post capacity counts as infrastructure, not another survivor. This rating selects peers; actual combat uses the accepted live defense snapshot.

---

# 4. Eligibility, Consent & Raid Charges

PvP participation is an explicit account choice. At CCL8, after completing one NPC Silo Raid, the player may confirm **Enable PvP**. The confirmation explains that both Silo and contested sites become attackable, attackers risk real unit death, and opt-in is permanent for this prototype account. Unlocking CCL8, scouting, claiming a private PvE site, or opening the PvP screen never opts in. The player can stay PvE-only forever.

| Account state | Private PvE sites | Attack/be attacked: player Silo | Attack/be attacked: contested site |
|---|---|---|---|
| CCL1–5 | Not claimable | No | No |
| CCL6–7 | Yes | No | No |
| CCL8+, not opted in | Yes | No | No |
| CCL8+, opted in, shield active | Yes | Incoming blocked; launching offense ends own shield | Same |
| CCL8+, opted in, no shield | Yes | Yes, subject to all predicates below | Same |

A PvP attack is accepted only if both accounts are CCL8+, opted in, within CCL ±1, not current Alliance members, and the defender has no shield or active incoming raid. Site attacks additionally require a contested node owned by that defender; private PvE nodes are never player targets. Revenge/reclaim uses the same predicates. Search expansion may relax Defense Rating/rating bands, never CCL or consent safety bounds.

Charges start at 3/3 when PvP is enabled at CCL8 or later. Both Silo and contested-site attacks share the same pool: cap 3, +1 charge per 4 real hours while below cap; regeneration stops at cap. No paid charge purchases or above-cap grants in this baseline.

On accepted deployment, one charge and mission Supply are reserved; debit at departure. A server-side rejection before departure releases both. Cancel, defeat, timeout or failed extraction after departure does not refund deployment cost. Scout alone never consumes a Raid Charge. An account may have only one outgoing PvP raid at a time. An incoming raid may overlap an outgoing raid only with disjoint survivor/gear assignments; the persistent defense assignment rules in SILO_DEFENSE_SECURITY apply. Selected Silo defenders cannot depart unless explicitly unassigned before any incoming lock.

---

# 5. Protection States

All shields protect the entire account: Silo and every contested site. Private PvE sites remain protected independently of opt-in/shields. Shields block new incoming deployments; an already accepted raid finishes against its reserved snapshot.

- **New Player Protection:** permanent until explicit opt-in; opt-in alone removes this state but does not start an attack.
- **Post-Loss:** 2h after committed theft or defender injury/disruption; 6h after Command breach or successful contested-site capture. A failed attack with no defender consequence gives no loss shield.
- **Chain Protection:** after the second resolved incoming attack within rolling 8h, grant 8h regardless of outcome. Attack history includes site and Silo raids and is never cleared by launching offense.
- **New contested ownership:** successful claim/capture grants 6h account shield.

At settlement, shield expiry = max(existing expiry, settlement time + each applicable duration). Repeated raids cannot shorten a shield. The second-attack 8h shield is therefore active before any third deployment can be accepted. Launching any offensive PvP attack voluntarily ends the attacker's timed shield only after deployment is accepted. Browsing, scouting and a rejected deployment do not remove it. Shields use real time and do not pause with the 8h economy offline cap.

No Revenge, Reclaim, rank-only attack or seasonal mode bypasses consent, shield, incoming-lock or CCL checks in this baseline.

---

# 6. Same-Target Cooldown

An accepted deployment starts a 24h directional attacker→defender cooldown across ALL assets. Switching from Silo to site, abandoning or failing extraction cannot reset it. The only exception is one valid Revenge token described below; no special-event bypass in the baseline.

---

# 7. Revenge / Reclaim

After a resolved non-revenge player attack, the defender receives one account-pair Revenge token, expiring 24h after settlement. The report shows attacker, objective, breached rooms, losses and approximate squad. A lost contested site additionally gives 2h priority reclaim intel; this identifies the node but grants no shield bypass or free capture.

A token grants one targeted attempt, free Quick Scout, +10 percentage points Scout confidence subject to the normal 72%/90% caps, and no matchmaking search. It does not waive charge, Supply, CCL, consent, shield, Alliance or active-raid checks. Consume the token at accepted departure; rejection preserves it. Expiry may occur before the target's shield ends; no guaranteed counterattack is promised.

---

# 8. Revenge Chain Limit

A attacks B → B may Revenge A → chain ends. A revenge settlement creates no new Revenge token. One token cannot be used against multiple sites or retried after failure. Normal pair cooldown and rolling loss ledgers still apply.

---

# 9. Rating & System Rewards

Initial rating1,000 at opt-in; floor0, no upper cap. A completed objective counts as success only with successful extraction. Partial extraction with objective incomplete gives no system reward or rating gain, but keeps legally carried theft. Defender rating changes are zero-sum with attacker rating except rating-floor truncation.

| Objective | Success base rating gain | Combat Data | Credits | Encrypted Combat Cache |
|---|---:|---:|---:|---:|
| Silo Resource Raid | 8 | 1 | 20 | 0 |
| Silo Intelligence Raid | 12 | 3 | 25 | 0 |
| Silo Sabotage | 10 | 2 | 20 | 0 |
| Silo Blueprint Hunt | 16 | 2 | 30 | 1 |
| Silo Command Assault | 20 | 4 | 40 | 1 |
| Site Plunder | 8 | 1 | 15 | 0 |
| Site Disrupt | 10 | 2 | 20 | 0 |
| Site Capture | 14 | 2 | 25 | 0 |

At accepted departure snapshot both ratings. Success gain = max(1, BaseGain + clamp(floor((defenderRating-attackerRating)/100),-4,+4)); defender loses the same amount up to floor0. Objective incomplete, failed extraction, abandon or failed timeout: attacker loses8 (floored0), defender gains that actual amount, no system rewards. Valid partial extraction with incomplete objective also uses this−8 result. Auto-extraction at the deadline follows the same objective/extraction predicates, not an automatic win. No rating change for rejection before departure.

All listed currencies/caches are system grants, not theft. Blueprint Hunt cache rolls via REWARD_REVEAL_CACHE; no guaranteed specific blueprint. Grant exactly once in the successful extraction receipt. No rewards are issued for individual defender kills, repeated room entries or a second settlement message.

---

# 10. Leagues

| Current seasonal rating | League |
|---|---|
| 0–799 | Rust |
| 800–1199 | Iron |
| 1200–1599 | Steel |
| 1600–1999 | Titanium |
| 2000–2399 | Prototype |
| 2400+ | Zero |

At season start set opted-in accounts to1,000; preserve match peaks, consent, charge timers, shields, cooldowns and loss ledger. League displays current rating; season-end award is one cosmetic banner/title at the highest league reached, once per season. No league-exclusive combat item or resource grant in this baseline. Non-opted-in accounts have no PvP rating/league and remain fully eligible for PvE seasonal content.

---

# 11. Resource Exposure, Rolling Loss Cap & Settlement

Only Scrap, Components and Chemicals can be stolen. Food, Water, Supply, Credits, all Data, Energy Cells, Reactor Material, Prototype Core, Alien Material, blueprint fragments, progression items, gear and survivors are non-stealable. PvP Combat Data/cache/Credits are system-generated rewards, never debited from the defender.

Fixed prototype caps per defender account and per resource over rolling 24 real hours:

| Highest CCL reached | Scrap | Components | Chemicals |
|---|---:|---:|---:|
| 8 | 60 | 20 | 12 |
| 9 | 75 | 25 | 15 |
| 10 | 90 | 30 | 18 |
| 11 | 105 | 35 | 21 |
| 12 | 120 | 40 | 24 |

Caps are tunable baselines, not percentages of observed production. They cover combined Silo and all site theft. Upgrading CCL changes the ceiling but does not reset the ledger. Each entry expires exactly 24h after its successful-extraction timestamp; midnight has no reset.

For resource r at accepted deployment:

```
RemainingCap[r] = max(0, Cap[CCL,r] - committed losses in (now-24h, now] - active reservations[r])
UnreservedStock[r] = max(0, stock at the attacked asset - existing spending/theft reservations)
SiloExposure[r] = min(floor(0.10 * UnreservedStock[r]), RemainingCap[r])
SiteExposure[r] = min(floor(0.10 * UnreservedStock[r]), floor(2 * site hourly output[r]), RemainingCap[r])
```

A Silo raid cannot access site buffers. A site raid cannot access main Silo stock or another site. At zero exposure, rank/intelligence/sabotage objectives remain possible under all protection rules; resource objectives are disabled. Cargo may further reduce the amount actually carried out.

**Atomic raid lifecycle:**

1. Accept deployment by checking all eligibility predicates, taking one incoming lock for the defender ACCOUNT (Silo + all sites), snapshotting layout/defense, and reserving exposure and remaining loss cap under a unique raid ID. A second simultaneous deployment is rejected with no cost. Reserved stock remains defender-owned but cannot be spent, collected or transferred during the raid.
2. Maximum active raid duration is 15 real minutes from departure, including outbound travel. Suspend does not stop this PvP clock. At the deadline, accept normal extraction automatically only if the squad is currently at a cleared valid exit with escort/cargo requirements satisfied; otherwise resolve failed extraction. An extraction already accepted remains successful. Return travel may continue after that deadline, using normal travel rules.
3. Only successful extraction atomically debits the actual carried amount from defender stock, records that amount in the rolling loss ledger, credits attacker permanent inventory exactly once, applies permitted objective effects/shields, and releases unused reservations and incoming lock. The extraction result is final; later return travel cannot revoke or duplicate committed raid loot.
4. Failure, abandon or a timeout that fails extraction releases ALL theft reservations and the incoming lock, with no defender resource debit or attacker loot credit. Apply only temporary defense consequences recorded by combat and their shield; capture/sabotage objective effects require successful extraction. Successful capture transfers control only at this same extraction transaction; unlooted residual buffer is returned to its prior owner through overflow handling, not gifted to the captor.
5. Reconnect/retry of any settlement returns its recorded result. It cannot roll new rewards, spend twice, or extend the 15m deadline. System-rejected/corrupt raids release reservations; the charge/Supply refund policy above applies only if departure never occurred.

**Worked checks:** CCL8 defender has 1,000 unreserved Scrap and 40 Scrap stolen 23h ago. Silo exposure = min(100,60-40)=20. Attacker carries 12 and extracts: stock falls by 12, ledger becomes52, unused8 releases. A failed extraction instead keeps all stock and ledger40. A simultaneous site attack is rejected. When the original40 entry reaches exactly24h old, it leaves the rolling window; the12 entry remains, so remaining cap becomes48, not60.

At a Scrapyard with buffer144 Scrap and output18/h, otherwise unused CCL8 cap: exposure=min(14,36,60)=14. A Chemicals site cannot expose Scrap; an Alien site exposes zero Alien Material.

---

# 12. Protection of New Progress

Recently crafted or first-clear unique rewards:

- cannot be stolen.

Blueprint ownership:
- never stolen.

Survivors:
- never stolen.

---

# 13. Smurf / Sandbag Prevention

Use lifetime highest CCL/TechTier and rolling7day PeakDefenseRating/PeakSquadPower from §2. Peak history is retained even when gear is removed, rooms powered off, roster unassigned or a season resets. No arbitrary “recent window” is left to implementation. Account resets cannot transfer resources or rewards to an existing account.

---

# 14. Inactivity

After7 real days without login, remove the account from new player-target searches. Accepted raids still settle normally. Do not expose dormant accounts as farmable player targets; NPC Silo content uses independent NPC rewards/state. Login restores eligibility subject to the same consent/shields and peak history.

---

# 15. Anti-Collusion

Current Alliance members cannot raid each other. Former members remain ineligible against each other for24h after either leaves. Count accepted raids between each unordered account pair over rolling7days, across Silo/site/Revenge. After2 accepted pair raids, reject further deployments between that pair until one entry leaves the7day window; no charge/Supply debit. This pair limit also applies to Revenge/reclaim and cannot be bypassed through another site. Display the remaining cooldown before deployment. Suspected automation/feeding may be logged for review; no hidden automatic punishment beyond these explicit limits.

---

# 16. Battle Log

Defender sees:

- timestamp;
- attacker;
- objective;
- result;
- route;
- alarm peak;
- loot lost;
- defense injuries;
- replay summary/event log later.

Not full deterministic replay required in MVP.

---

# 17. Success Criteria

System works if:

- new players are protected;
- strong players still find worthwhile targets;
- no one can zero another account;
- revenge feels satisfying;
- repeated harassment is structurally limited.
