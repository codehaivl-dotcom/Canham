# CĂN HẦM — Design Audit v0.3

**Date:** 2026-11-12  
**Scope:** audit toàn bộ design docs hiện có trước khi bước sâu vào prototype/balance.

---

# 1. Brand status — LOCKED

The previous naming audit is superseded.

**Official game name:** BURROW ZERO  
**Official slogan:** Deep Below. Far Beyond.  
**Initial languages:** Vietnamese + English.  
**Primary survivor art:** panda mascot, simple AI-first low-poly 3D.

Canonical brand spec:

[BRAND_LOCALIZATION_V0.1.md](./BRAND_LOCALIZATION_V0.1.md)

Final commercial trademark/store/domain clearance remains a pre-launch task.

---

# 2. Những hệ thống đã có đủ direction

## A. Game Vision — GOOD

Đã khóa:

- Silo home base;
- expedition;
- PvE;
- boss;
- PvP;
- contested resource;
- imperfect intel;
- extraction;
- death/revive;
- alien exposure;
- noise;
- faction/alliance direction.

## B. World Targets — GOOD FOR PROTOTYPE

Đã có archetype:

- House;
- Warehouse;
- Hospital;
- Military Depot;
- Research Lab;
- Metro;
- Resource Site;
- NPC Silo;
- Player Silo;
- Alien Crash post-MVP.

Đã có:

- room band;
- threat;
- loot affinity;
- objective;
- extraction;
- procedural rule.

## C. Units / Weapons / Items — GOOD BASELINE

Đã có:

- 8 stats;
- level;
- roles;
- squad 3 → 4 → 5;
- formation;
- 9 weapon classes;
- armor;
- utility;
- consumables;
- revival;
- damage formula baseline.

## D. Enemy / Resistance — GOOD BASELINE

Đã có:

- 24 archetype;
- full resistance matrix;
- Threat Cost;
- AI priority;
- elites;
- bosses;
- encounter budget;
- TTK target.

---

# 3. P0 — Thiếu trước khi prototype economy/base

## P0.1 Silo Building Stats — MISSING → NOW DRAFTED

Trước audit chỉ có tên phòng, chưa có:

- Power use/output;
- production/hour;
- storage;
- beds;
- queue;
- level;
- build cost;
- build time;
- CCL gate.

Đã bổ sung tại:

[SILO_BUILDINGS_V0.1.md](./SILO_BUILDINGS_V0.1.md)

## P0.2 Currency / Resource / Power Economy — MISSING → NOW DRAFTED

Trước audit chưa định nghĩa rõ:

- currency;
- source/sink;
- Food/Water consumption;
- Power grid;
- Battery;
- expedition Supply;
- strategic materials;
- starting economy.

Đã bổ sung tại:

[ECONOMY_RESOURCES_V0.1.md](./ECONOMY_RESOURCES_V0.1.md)

## P0.3 Combat Simulation — MISSING

Hiện ta có rất nhiều con số nhưng chưa chạy simulation.

Cần:

- Monte Carlo / deterministic encounter sim;
- TTK;
- HP loss;
- wrong-loadout penalty;
- healing;
- AOE;
- boss length;
- squad 3/4/5.

Không nên khóa live balance trước bước này.

## P0.4 Crafting / Loot tables — MISSING

Ta đã có loot affinity nhưng chưa có:

- exact drop weight;
- item salvage value;
- recipe;
- blueprint fragment requirement;
- upgrade cost;
- repair;
- inventory weight/capacity.

Đây là dependency trực tiếp của economy.

---

# 4. P1 — Thiếu để Vertical Slice hoàn chỉnh

## P1.1 Scout formula

Đã có philosophy nhưng chưa có:

- Quick Scout cost/time;
- Deep Scout cost/time;
- exact confidence formula;
- Scout stat contribution;
- Drone contribution;
- false-negative band.

## P1.2 Expedition travel

Chưa khóa:

- travel time;
- Supply cost exact formula;
- distance impact;
- random travel encounter;
- return travel;
- offline behavior.

## P1.3 Population system

Chưa có đủ:

- recruit rate;
- survivor quality;
- population cap progression;
- morale formula;
- hunger/dehydration penalties;
- worker assignment output;
- death impact;
- relationship effect.

## P1.4 Trait / Perk catalog

Hiện chỉ có ví dụ.

Cần ít nhất:

- 20–30 traits;
- positive/negative/mixed;
- 20–30 combat perks;
- role progression.

## P1.5 Silo sector expansion generation

Đã có concept “clear rồi mới chiếm” nhưng chưa có:

- sector size;
- expansion cost;
- hidden sector probability;
- room-restoration probability;
- threat scaling theo depth/CCL.

## P1.6 Mimic

GDD có Mimic/infiltration nhưng Enemy spec chưa có Mimic prototype.

Cần tách:

- combat Mimic;
- hidden colonist Mimic;
- investigation event.

---

# 5. P2 — Thiếu cho shared-world / live game

## PvP

Direction tốt nhưng chưa có exact:

- matchmaking score;
- protection/shield;
- attacker attempts;
- exposed resources;
- defender loss;
- ranking;
- season;
- anti-abuse.

## Resource Site

Đã có lifecycle nhưng chưa có:

- capture time;
- output/day;
- worker scaling;
- discovery chance;
- defense cap;
- contest window.

## World Map

Chưa có:

- region size;
- spawn density;
- refresh;
- persistent vs temporary target;
- travel graph;
- fog radius;
- relocation.

## Faction

Chưa có:

- reputation thresholds;
- faction store;
- exclusive gear;
- hostility;
- faction mission generation.

## Alliance

Chưa có:

- size;
- roles;
- projects;
- shared resources;
- alliance PvE;
- alliance PvP.

---

# 6. P3 — Production / product design chưa cần khóa ngay

- art direction;
- UI/UX wireframes;
- sound direction;
- narrative campaign;
- tutorial;
- quests/dailies;
- achievements;
- monetization detail;
- analytics;
- backend authority;
- anti-cheat;
- save/version migration;
- localization;
- accessibility;
- notifications.

Những phần này quan trọng nhưng không nên chặn combat/base prototype.

---

# 7. Audit conclusion

Sau audit, thứ tự hợp lý hơn là:

```
VISION ✓
WORLD TARGETS ✓
UNITS / ITEMS ✓
ENEMIES ✓
    ↓
ECONOMY / RESOURCES ✓ baseline
SILO BUILDINGS ✓ baseline
    ↓
COMBAT SIMULATION
    ↓
CRAFTING / LOOT
    ↓
POPULATION / TRAITS
    ↓
SCOUT / TRAVEL
    ↓
SILO EXPANSION
    ↓
RESOURCE SITES
    ↓
NPC SILO RAID
    ↓
VERTICAL SLICE
    ↓
PVP / SHARED WORLD
```

Lý do đưa Economy + Building lên trước simulation integration:

> Combat có thể cân riêng bằng số, nhưng vertical slice không thể tồn tại nếu người chơi chưa có lý do kinh tế để xây phòng, sản xuất, tiêu thụ và đi expedition.

---

# 8. Current readiness score

Đánh giá design readiness, không phải code readiness:

| Area | Readiness |
|---|---:|
| Game vision | 90% |
| Combat concept | 85% |
| Unit/item baseline | 80% |
| Enemy baseline | 85% |
| World target design | 80% |
| Silo buildings | 70% |
| Economy/resources | 70% |
| Loot/crafting | 35% |
| Population | 30% |
| Scout/travel | 40% |
| Resource territory | 40% |
| PvP | 45% |
| World map | 35% |
| Narrative content | 30% |

Overall pre-production design readiness:

**~62%**

Đủ để bắt đầu prototype combat/base nhỏ, chưa đủ để build full game.


---

# 9. Market research bổ sung

Chi tiết:

[MARKET_RESEARCH_V0.1.md](./MARKET_RESEARCH_V0.1.md)

Các reference quan trọng:

- **Escape from Duckov** — extraction greed, layered progression, fixed map identity + variable run, quest-driven system onboarding.
- **Bunker Buster** — competitor gần nhất về bunker + power/life support + research + fortress raid/PvP.
- **Last Fortress: Underground** — underground base + survivor jobs + squad synergy + world/alliance.
- **Zero City** — shelter + equipped squad + PvP attacks.
- **System Arrival** — expedition → supply → underground bunker progression.
- **AETHUS** — exploration/crafting và narrative reason to dig deeper.

Differentiation phải giữ:

1. named survivors có attachment/death;
2. imperfect intel;
3. room-by-room expedition;
4. extraction/retreat;
5. Silo expansion phải clear sector;
6. weapon soft-counter/formation;
7. base-as-dungeon asynchronous PvP;
8. contested resource sites.

Combat Simulation: **NOT STARTED**.


---

# 10. Gap closure update

Sau audit, các gap P0/P1 sau đã được lấp bằng spec baseline:

- Loot/Crafting/Blueprint;
- Population/Jobs/Morale/Fatigue;
- Trait/Perk;
- Scout confidence;
- Travel time/risk;
- Contract-driven onboarding;
- Silo excavation;
- sector challenge/control;
- Restore vs Convert old facility;
- anti-RNG progression;
- source clarity;
- multi-axis run rewards.

Files:

- [LOOT_CRAFTING_V0.1.md](./LOOT_CRAFTING_V0.1.md)
- [POPULATION_TRAITS_V0.1.md](./POPULATION_TRAITS_V0.1.md)
- [SCOUT_TRAVEL_CONTRACTS_V0.1.md](./SCOUT_TRAVEL_CONTRACTS_V0.1.md)
- [SILO_EXPANSION_V0.1.md](./SILO_EXPANSION_V0.1.md)
- [LESSONS_APPLIED_V0.1.md](./LESSONS_APPLIED_V0.1.md)

## Revised readiness estimate

| Area | Readiness |
|---|---:|
| Game vision | 92% |
| Combat concept | 85% |
| Unit/item baseline | 82% |
| Enemy baseline | 85% |
| World target design | 82% |
| Silo buildings | 75% |
| Economy/resources | 75% |
| Loot/crafting | 70% |
| Population/jobs/traits | 68% |
| Scout/travel/contracts | 70% |
| Silo expansion | 78% |
| Resource territory | 40% |
| PvP | 45% |
| World map | 35% |

Overall design readiness now roughly **72%** for a vertical-slice pre-production package.

Major remaining design gaps:

1. Resource Site exact contest/output/defense rules;
2. NPC Silo Raid flow and alarm/reinforcement;
3. PvP exact loss/protection/matchmaking;
4. World Map spawn/refresh/region model;
5. Faction/Alliance exact systems;
6. Combat Simulation.

Combat Simulation remains **NOT STARTED**.


---

# 11. Major gap closure — 2026-11-12

The previously missing gameplay/product systems now have dedicated baseline specs:

| Area | File | Status |
|---|---|---|
| Resource Site capture/contest | RESOURCE_SITES_V0.1.md | ✅ |
| NPC Silo Raid | NPC_SILO_RAID_V0.1.md | ✅ |
| Player PvP Raid | PLAYER_PVP_RAID_V0.1.md | ✅ |
| Matchmaking/protection/loss/revenge | PVP_MATCHMAKING_PROTECTION_V0.1.md | ✅ |
| World Map/regions/refresh | WORLD_MAP_REGIONS_V0.1.md | ✅ |
| Factions | FACTIONS_V0.1.md | ✅ |
| Alliance/Coalition | ALLIANCE_COALITION_V0.1.md | ✅ |
| Mimic/Infiltration | MIMIC_INFILTRATION_V0.1.md | ✅ |
| Story campaign/chapters | STORY_CAMPAIGN_V0.1.md | ✅ |
| First 1–2h tutorial | TUTORIAL_FIRST_2H_V0.1.md | ✅ |
| Full UI/UX navigation | UI_UX_NAVIGATION_V0.1.md | ✅ |
| Sound/music direction | SOUND_MUSIC_V0.1.md | ✅ |
| Seasons/endgame | SEASONS_ENDGAME_V0.1.md | ✅ |

## Revised readiness excluding Combat Simulation

| Area | Readiness |
|---|---:|
| Game vision | 95% |
| Core PvE loop | 92% |
| Silo/base systems | 88% |
| Units/items/enemies | 85% |
| Loot/economy/population | 82% |
| World targets/map | 88% |
| Resource territory | 82% |
| NPC raid | 85% |
| Player PvP policy | 82% |
| Faction/Alliance | 75% |
| Story/tutorial | 82% |
| UI/UX | 80% |
| Sound direction | 75% |
| Season/endgame | 75% |
| Brand/localization | 90% |

Overall game-design documentation readiness excluding Combat Simulation:

**~87–90%**

There are no longer major undefined core gameplay loops.

Remaining gaps are mostly production-depth rather than concept-depth:

1. Art Production/asset specification;
2. exact numerical/content tuning;
3. technical architecture/backend/save;
4. detailed monetization/store economy;
5. analytics/telemetry;
6. final story dialogue/content;
7. Combat Simulation — intentionally not started.
