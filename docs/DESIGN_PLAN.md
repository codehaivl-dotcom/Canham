# BURROW ZERO — Design & Production Plan

> **Deep Below. Far Beyond.**

**Status:** Pre-production design  
**Initial languages:** Vietnamese + English  
**Art:** AI-first simple low-poly 3D, panda survivor mascot


---

## 0. Luật gốc đã khóa

Nguồn: [GAME_DESIGN_V0.1.md](./GAME_DESIGN_V0.1.md) — nội dung hiện tại là GDD v0.2.

Đã khóa:

- mỗi người chơi sở hữu một Silo;
- Silo có progression trung tâm CCL;
- 10–20 giờ đầu ưu tiên PvE;
- squad progression 3 → 4 → 5, cap 5;
- combat dễ đọc kiểu Fallout Shelter, nhưng sâu hơn ở preparation / formation / gear;
- weapon có damage profile khác nhau, không chỉ DPS;
- soft-counter: cầm sai súng vẫn gây damage;
- unit có thể chết thật, revive cần item;
- scout chỉ cung cấp thông tin xác suất;
- mission không bắt buộc clear 100%;
- retreat / extraction là quyết định chiến thuật;
- mở rộng Silo phải clear và giành quyền kiểm soát sector;
- Boss / PvP / contested content cung cấp một phần progression hiếm;
- PvP là asynchronous Silo infiltration và ưu tiên matchmaking ngang cấp.

---

# 1. World Target / Dungeon Framework — DRAFTED

Chi tiết: [WORLD_TARGETS_V0.1.md](./WORLD_TARGETS_V0.1.md)

Mục tiêu:

- định nghĩa toàn bộ target người chơi có thể scout / explore / attack / capture;
- chuẩn hóa size, room count, loot affinity, threat, hazard, objective, extraction;
- tạo khác biệt rõ giữa House, Warehouse, Hospital, Military Depot, Research Lab, Metro, Resource Site và Silo;
- location có identity rõ nhưng layout/threat/loot không bao giờ biết chính xác 100%;
- World Map có ba trụ:
  1. **Dungeon** để khám phá;
  2. **Resource Site** để khai thác / tranh chấp;
  3. **Silo** để PvP / strategic progression.

### MVP target set

1. Abandoned House
2. Logistics Warehouse
3. Hospital
4. Military Depot
5. Research Laboratory
6. Metro / Tunnel
7. Resource Site
8. NPC Silo

Sau MVP:

- Factory;
- Prison;
- Mall;
- Data Center;
- Mine;
- Airport;
- Alien Crash Site;
- Alien Nest;
- Underground City;
- Player Silo;
- World Boss Zone.

---

# 2. Unit & Item System — DRAFTED

Chi tiết: [UNITS_ITEMS_V0.1.md](./UNITS_ITEMS_V0.1.md)

Đã thiết kế prototype baseline cho:

- 8 core stats;
- derived combat stats;
- 6 combat roles;
- level progression;
- squad cap;
- formation;
- weapon classes;
- damage/resistance formula;
- armor;
- utility gear;
- consumables;
- revive;
- item tiers;
- sample weapon/item values.

**Lưu ý:** các con số trong tài liệu này là baseline để prototype, không phải final live balance.

---

# 3. Enemy & Resistance Matrix — DRAFTED

Chi tiết: [ENEMIES_RESISTANCES_V0.1.md](./ENEMIES_RESISTANCES_V0.1.md)

Đã có:

- 24 enemy prototype;
- 5 Infected;
- 4 Human/Raider;
- 4 Mechanical;
- 5 Alien;
- 3 Elite;
- 3 Boss;
- HP / damage / attack interval / armor;
- full resistance matrix theo 6 damage type;
- Threat Cost + encounter budget;
- target priority AI;
- status effect baseline;
- boss CC rules;
- difficulty multiplier;
- TTK target;
- Bestiary knowledge progression;
- Scout hint language;
- 12 encounter chuẩn để simulation.

Nguyên tắc giữ nguyên:

- không có hard counter phổ biến;
- wrong weapon vẫn gây damage;
- encounter difficulty đến từ composition + mechanic nhiều hơn raw stat inflation.

---

# 4. Economy / Resources — DRAFTED

Chi tiết: [ECONOMY_RESOURCES_V0.1.md](./ECONOMY_RESOURCES_V0.1.md)

Đã có baseline:

- Food / Water consumption;
- Power generation/load;
- Battery reserve;
- Credits;
- Scrap / Components / Chemicals;
- Research Data;
- Supply;
- strategic resources;
- starting economy;
- resource-site production;
- source/sink philosophy.

---

# 5. Silo Buildings / Power — DRAFTED

Chi tiết: [SILO_BUILDINGS_V0.1.md](./SILO_BUILDINGS_V0.1.md)

Đã có:

- CCL 1–12 unlock direction;
- squad cap 4 tại CCL5;
- squad cap 5 tại CCL8;
- room L1–L5;
- Power output/load;
- Food/Water production;
- beds/storage;
- Workshop/Clinic/Training/Research;
- Radio/Scout;
- Security/Armory;
- build cost/time baseline;
- room state/damage/repair.

---

# 6. Market / Competitor Research — DRAFTED

Chi tiết: [MARKET_RESEARCH_V0.1.md](./MARKET_RESEARCH_V0.1.md)

Đã research:

- Fallout Shelter;
- Last Fortress: Underground;
- Zero City;
- Escape from Duckov;
- Bunker Buster;
- System Arrival;
- AETHUS;
- bunker/underground watchlist.

Kết luận:

- chưa tìm thấy game ghép đúng toàn bộ Silo + named squad + imperfect intel + extraction + resource conflict + PvP dungeon;
- Bunker Buster là competitor gần nhất ở bunker/power/PvP;
- Duckov là reference mạnh nhất cho extraction greed loop và layered progression;
- cần giữ differentiation bằng named squad, room-by-room expedition, base-as-dungeon PvP và contested resources.

**Combat Simulation vẫn chưa bắt đầu.**

---

# 7. Combat Simulation & Encounter Budget — NEXT

Sau Enemy table:

- damage equation;
- accuracy;
- crit;
- resistance;
- armor;
- AOE falloff;
- DOT;
- heal;
- revive;
- aggro;
- formation;
- target priority;
- room capacity;
- encounter budget.

Cần test:

- squad 3;
- squad 4;
- squad 5;
- balanced team;
- specialized team;
- wrong-loadout team.

Mục tiêu:

> specialized team thắng nhanh khi đoán đúng; balanced team chịu sai intel tốt hơn; wrong-loadout team vẫn có cơ hội extract.

---

# 8. Loot / Crafting / Blueprint Economy

Thiết kế chính xác:

- resource list;
- loot tables theo location;
- rarity;
- drop bands;
- blueprint fragments;
- crafting recipes;
- boss-exclusive materials;
- PvP-exclusive / contested materials;
- salvage;
- item upgrade;
- inventory capacity.

Phải đảm bảo:

- không có một location duy nhất farm được tất cả;
- người chơi có lý do đi nhiều loại dungeon;
- rare progression thúc đẩy risk, không ép PvP tuyệt đối.

---

# 9. Silo Architecture & Progression — PARTIAL

Thiết kế:

- CCL 1–12 hoặc số cấp cuối cùng;
- room grid / module dimensions;
- power;
- water;
- food;
- population;
- storage;
- clinic;
- workshop;
- research;
- security;
- scout;
- command;
- expansion sector;
- hidden room;
- restoration room;
- defense capacity.

Cần xác định chính xác:

- mỗi CCL mở gì;
- squad slot 4 và 5 mở ở đâu;
- room upgrade cap;
- build time/cost;
- sector-clear difficulty.

---

# 10. Scout / Intel System

Thiết kế:

- Quick Scout;
- Deep Scout;
- intel confidence;
- false negative / hidden sector;
- revealed room range;
- detected threat family;
- detected loot affinity;
- scout cost;
- drone;
- Scout-role bonuses.

Không bao giờ reveal 100%.

---

# 11. Expedition Flow

Full state machine:

```
DISCOVER
→ SCOUT
→ PREPARE
→ DEPLOY
→ ENTER
→ CLEAR ROOM
→ LOOT
→ CHOOSE ROUTE
→ CONTINUE / RETREAT
→ EXTRACT
→ RETURN
→ HEAL / REPAIR / RESEARCH
```

Cần UI state cho:

- dead unit;
- revive;
- inventory full;
- hidden room;
- locked door;
- boss warning;
- retreat;
- failed extraction.

---

# 12. Resource Sites & Territory

Thiết kế:

- Clear;
- Capture;
- Deploy workers;
- Production;
- Noise;
- Discoverability;
- Defense;
- Contest;
- Loss / recapture.

Resource sites ban đầu:

- Scrapyard;
- Chemical Plant;
- Solar Farm;
- Water Facility;
- Uranium Mine;
- Data Center;
- Military Salvage Yard;
- Alien Crater.

---

# 13. PvP Silo Raid

Thiết kế sau khi PvE combat ổn.

Cần:

- matchmaking;
- scout;
- hidden layout;
- alarm;
- reinforcement;
- objective types;
- loot cap;
- defender protection;
- resource raid;
- intelligence raid;
- blueprint hunt;
- sabotage;
- full assault;
- extraction.

PvP phải sử dụng cùng combat language với PvE.

---

# 14. World Map

Cần định nghĩa:

- fog of war;
- region;
- search radius;
- target spawning;
- persistent target;
- temporary target;
- contested target;
- NPC faction;
- player silo discovery;
- travel time;
- travel risk;
- world event.

---

# 15. Vertical Slice

Vertical slice đầu tiên chưa cần MMO.

Phải có:

- Silo nhỏ;
- 6 room types;
- squad 3;
- unlock squad 4 trong slice nếu khả thi;
- House;
- Warehouse;
- Research Lab;
- Resource Site;
- NPC Silo;
- ít nhất 8 weapon classes;
- 4 armor archetypes;
- 10 consumables;
- 10–15 enemy archetypes;
- scout;
- imperfect intel;
- death/revive;
- extraction;
- loot;
- crafting;
- sector clearance.

Hook cuối:

```
UNKNOWN HUMAN SILO SIGNAL DETECTED
Distance: 18.4 km
Status: ACTIVE
[SCAN]
```

---

# 16. Thứ tự triển khai khuyến nghị

```
GAME VISION
   ↓
WORLD TARGETS
   ↓
UNITS & ITEMS
   ↓
ENEMIES & RESISTANCES
   ↓
ECONOMY / SILO BUILDINGS
   ↓
COMBAT SIMULATION
   ↓
LOOT / CRAFTING
   ↓
SILO PROGRESSION
   ↓
SCOUT / EXPEDITION
   ↓
RESOURCE SITES
   ↓
NPC SILO RAID
   ↓
VERTICAL SLICE
   ↓
PLAYER PVP
   ↓
PERSISTENT WORLD
```

Nguyên tắc: **không xây MMO/world backend trước khi room combat + preparation + extraction đã chứng minh là vui.**


---

# 17. Loot / Crafting / Blueprint — DRAFTED

Chi tiết: [LOOT_CRAFTING_V0.1.md](./LOOT_CRAFTING_V0.1.md)

Đã có:

- field loot ownership;
- cargo baseline;
- loot affinity;
- room loot budget;
- rarity;
- blueprint fragment requirements;
- guaranteed boss progress / bad-luck protection;
- first-clear reward;
- salvage;
- prototype recipes;
- source clarity;
- multi-axis run progression;
- Secure Data Case experiment.

---

# 18. Population / Jobs / Traits / Perks — DRAFTED

Chi tiết: [POPULATION_TRAITS_V0.1.md](./POPULATION_TRAITS_V0.1.md)

Đã có:

- recruitment;
- population cap;
- room-job stat affinity;
- worker efficiency formula;
- Morale;
- Fatigue;
- death impact;
- trait catalog;
- role perk examples;
- lightweight relationships;
- survivor history;
- roster rotation.

---

# 19. Scout / Travel / Contracts — DRAFTED

Chi tiết: [SCOUT_TRAVEL_CONTRACTS_V0.1.md](./SCOUT_TRAVEL_CONTRACTS_V0.1.md)

Đã có:

- Radio Search;
- Quick/Deep Scout;
- confidence formula;
- Drone bonus;
- travel time;
- travel risk;
- Supply;
- extraction accessibility;
- contract-driven onboarding;
- target expiry.

---

# 20. Silo Expansion / Sector Control — DRAFTED

Chi tiết: [SILO_EXPANSION_V0.1.md](./SILO_EXPANSION_V0.1.md)

Đã có:

- excavation loop;
- depth bands;
- excavation cost/time;
- sector discovery table;
- challenge types;
- control states;
- Convert vs Restore;
- special restorable rooms;
- Seal Sector;
- PvP layout implications;
- anti-frustration pacing.

---

# 21. Lessons Applied — DRAFTED

Chi tiết: [LESSONS_APPLIED_V0.1.md](./LESSONS_APPLIED_V0.1.md)

Đã ghi rõ:

- cái gì học từ Duckov / Fallout Shelter / Last Fortress / Bunker Buster / System Arrival;
- cái gì không học;
- những trụ signature phải bảo vệ.

---

# 22. Current next step

**Combat Simulation vẫn NOT STARTED.**

Sau khi chủ dự án muốn tiếp tục, hai hướng hợp lý nhất:

1. Resource Site exact numbers + contest rules;
2. NPC Silo Raid exact flow / defender AI / alarm.

Combat Simulation có thể làm sau khi hai nhánh trên đủ context.


---

# 23. Reward Reveal / Cache / Survivor Signal — LOCKED DIRECTION

Chi tiết: [REWARD_REVEAL_CACHE_V0.1.md](./REWARD_REVEAL_CACHE_V0.1.md)

Đã khóa:

- card-style reward reveal;
- Supply / Medical / Military / Research / Alien / Combat cache;
- cache quality gắn với source location;
- item rarity presentation;
- survivor không có Common/Rare/Epic/Legendary;
- survivor đến từ Rescue / Distress / Radio / Cryo / Story;
- Distress Signal có thể cho player chọn survivor;
- Cryo Pod là rare discovery;
- direct loot/crafting vẫn tồn tại;
- cache tìm trong dungeon vẫn phải extract;
- PvE tự đủ content và progression;
- PvP là lớp đối kháng/prestige/economy, không bắt buộc để game thú vị;
- anti-gacha rules;
- paid RNG không được là nguồn exclusive power.

Combat Simulation vẫn **NOT STARTED**.
