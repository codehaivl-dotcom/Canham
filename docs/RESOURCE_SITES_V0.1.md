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
→ CONTESTED
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

# 4. Site Tiers

| Tier | Typical CCL | Output | Discoverability | Contest pressure |
|---|---|---|---|---|
| I | 5–6 | low | low | mostly PvE |
| II | 6–8 | medium | medium | PvE + occasional player |
| III | 8–10 | high | high | regular conflict |
| IV | 10–12 | strategic | very high | contested/endgame |

Tier is fixed by world node, not scaled to player.

---

# 5. Clear & Claim

Before ownership:

- clear local threat;
- restore control node;
- repair basic infrastructure;
- spend one Claim Beacon.

Prototype claim cost:

- 10 Supply;
- 25 Scrap;
- 5 Components;
- 1 Claim Beacon.

Claim time:

- Tier I: 1 min;
- Tier II: 2 min;
- Tier III: 4 min;
- Tier IV: 6 min.

Claim process can be interrupted by PvE event but not by instant remote PvP.

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

Examples:

- Mine: END + TEC;
- Data Center: INT + TEC;
- Water: TEC + INT;
- Salvage: TEC + COM.

Workers remain unavailable for normal Silo jobs while assigned.

They are not permanently killed by offline PvP defense.

---

# 7. Production

Base output from Economy spec remains baseline.

Actual output:

```
Final Output =
Base Output
× Worker Efficiency
× Site Integrity
× Control Modifier
```

Prototype integrity:

- 100%: full;
- 75–99%: 90%;
- 50–74%: 75%;
- 25–49%: 50%;
- <25%: offline.

---

# 8. Storage at Site

Sites have local buffer to create raid risk.

Prototype storage:

- Tier I: 4h output;
- Tier II: 6h;
- Tier III: 8h;
- Tier IV: 8h.

Player can collect manually or via later logistics tech.

Uncollected local buffer is the primary resource exposed to raids.

Main Silo storage is not directly emptied by a site raid.

---

# 9. Noise / Signal

Every active site has Signal.

```
Signal =
Base Site Signal
+ Production Load
+ Defense Systems
- Concealment
```

Signal bands:

- LOW;
- MEDIUM;
- HIGH;
- EXTREME.

Higher output tends to increase Signal.

This creates:

> produce more ↔ become easier to find.

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
- mine/trap later.

Defense Capacity by tier:

| Tier | Defense Capacity |
|---|---:|
| I | 20 |
| II | 35 |
| III | 55 |
| IV | 80 |

Defense uses same language as Silo defense but scaled down.

---

# 12. Contest Window

A discovered enemy site can be attacked if:

- attacker is eligible by matchmaking region/band;
- site is not under immediate protection;
- attacker has Raid Charge;
- site is not currently resolving another attack.

No real-time simultaneous combat required.

Async model.

---

# 13. Raid Outcomes

Attacker objectives:

### Plunder
Take part of local buffer.

### Disrupt
Damage integrity / pause production.

### Capture
Only available if site is vulnerable enough.

Capture requires:
- successful raid;
- control node objective;
- Claim Beacon;
- defender protection rules satisfied.

---

# 14. Capture Protection

Newly captured site gets:

```
Protection: 6 hours
```

Protection ends early if owner manually attacks another player's site from that node.

A site cannot chain-flip repeatedly every few minutes.

After losing site:

- original owner gets 2h reclaim priority intel;
- can launch Revenge/Reclaim with reduced scout cost.

---

# 15. Loss Rules

Losing a Resource Site does NOT:

- kill assigned survivors permanently;
- remove Silo buildings;
- steal stored main-base resources.

Assigned survivors return injured/fatigued after defeat.

Attacker may take:

- part of local buffer;
- small strategic reward;
- site control if Capture objective.

---

# 16. Plunder Cap

Prototype:

```
Max plunder = min(30% local buffer, 2h site output)
```

Tier IV strategic material:

- lower percentage cap;
- hard daily cap.

Prevents one attack from wiping days of progress.

---

# 17. Multi-Site Ownership

Soft cap:

| CCL | Efficient sites |
|---|---:|
| 6 | 1 |
| 7 | 2 |
| 8–9 | 3 |
| 10+ | 4 |

Beyond soft cap:

- worker cost rises;
- Signal rises;
- output efficiency falls.

No hard cap needed initially.

---

# 18. Abandon

Player can abandon:

- workers return;
- stored buffer collected up to cargo/logistics cap;
- node becomes neutral after cooldown;
- no penalty except lost opportunity.

Useful when site becomes too expensive to defend.

---

# 19. PvE-only Access

Players who avoid PvP still get Resource Site gameplay through:

- neutral sites;
- faction-controlled sites;
- temporary PvE sites;
- instanced low-tier sites.

High-tier contested sites give efficiency/prestige, not mandatory survival progression.

---

# 20. Success Criteria

Resource Sites work if:

1. there is a real reason to hold them;
2. worker allocation matters;
3. high output creates exposure;
4. PvP arises from economy;
5. defeat hurts but does not erase progress;
6. PvE-only players still have viable progression.
