# BURROW ZERO — World Targets / Dungeon Design v0.1

**Status:** Prototype design baseline  
**Scope:** địa điểm người chơi scout, explore, attack, clear, capture hoặc raid.

---

# 1. Location Blueprint

Mọi location dùng chung schema:

| Field | Ý nghĩa |
|---|---|
| Location Type | House, Warehouse, Hospital, Silo... |
| Size | Tiny / Small / Medium / Large / Complex |
| Room Band | số phòng dự kiến |
| Threat Band | 1–5 |
| Threat Family | Raider / Infected / Robot / Alien... |
| Hazard | Gas, Radiation, Fire, Bio, Electric... |
| Loot Affinity | nhóm loot có xác suất cao |
| Intel Quality | độ tin cậy của Scout |
| Objective | Explore / Clear / Loot / Kill / Capture / Hold |
| Extraction | điều kiện / đường thoát |
| Rare Event | boss, survivor, cache, anomaly... |
| Control State | Unexplored / Cleared / Controlled / Contested |

Target card không được cho biết chính xác enemy/loot/layout.

Authored first-slice graphs/loot/fixtures are in [PROTOTYPE_CONTENT_PACK_V0.1.md](PROTOTYPE_CONTENT_PACK_V0.1.md); later guaranteed progression encounters are in [CAMPAIGN_CONTRACTS_V0.1.md](CAMPAIGN_CONTRACTS_V0.1.md). Archetype room bands below are normal-generation targets; explicitly smaller curated tutorial/contract graphs are exceptions, not alternate normal distributions.

---

# 2. Location Size

| Size | Room band | Typical squad |
|---|---:|---:|
| Tiny | 2–4 | 3 |
| Small | 4–7 | 3 |
| Medium | 7–11 | 3–4 |
| Large | 11–16 | 4–5 |
| Complex | 16–25+ | 5 |

**Size không đồng nghĩa Difficulty.**

Một Small alien nest có thể nguy hiểm hơn Large civilian warehouse.

---

# 3. Procedural Rule

Không random hoàn toàn.

```
LOCATION ARCHETYPE
      +
ROOM POOL
      +
LAYOUT RULE
      +
THREAT PACKAGE
      +
HAZARD PACKAGE
      +
LOOT PACKAGE
      +
RARE EVENT
```

Ví dụ Hospital vẫn phải có cảm giác là Hospital.

Room pool có thể gồm Reception, Ward, Pharmacy, Surgery, ICU, Morgue, Laboratory.

Nhưng:

- route thay đổi;
- phòng bị khóa thay đổi;
- threat thay đổi;
- hazard thay đổi;
- boss có thể có hoặc không;
- hidden room có thể có hoặc không;
- basement có thể có hoặc không.

Người chơi học archetype nhưng không thuộc lòng map.

---

# 4. MVP — Abandoned House

**Role:** dungeon entry-level / civilian scavenging.

Prototype baseline:

| Property | Value |
|---|---|
| Size | Tiny–Small |
| Rooms | 3–7 |
| Threat | 1–2 |
| Squad | 3 |
| Main loot | Food, civilian medicine, basic material |
| Secondary | basic weapon, clothing, utility |
| Rare | survivor, prepper cache, hidden basement |

Room pool:

- Entrance;
- Living Room;
- Kitchen;
- Bedroom;
- Bathroom;
- Garage;
- Basement;
- Attic.

Example:

```
Entrance
   ↓
Living Room
 ├── Kitchen
 ├── Bedroom
 │     └── Bathroom
 └── Basement ???
```

Rare basement possibilities:

- food cache;
- civilian gun safe;
- generator;
- survivor;
- infected nest;
- hidden tunnel.

House phải nhanh: khoảng 3–6 phút active play cho full clear prototype.

---

# 5. MVP — Logistics Warehouse

**Role:** industrial resource farming + AOE combat showcase.

| Property | Value |
|---|---|
| Size | Small–Medium |
| Rooms | 6–11 |
| Threat | 2–3 |
| Squad | 3–4 |
| Main loot | Metal, electronics, industrial parts |
| Secondary | tools, fuel cell, weapon parts |
| Rare | secured container, prototype shipment |

Room pool:

- Loading Bay;
- Main Storage;
- Office;
- Security Room;
- Cold Storage;
- Container Area;
- Maintenance;
- Basement.

Example:

```
Loading Bay
    ↓
Main Storage
 ├──── Office
 │       └── Security
 ├──── Cold Storage
 └──── Container Area
          ↓
       Basement
```

Combat identity:

- Main Storage có room capacity lớn;
- swarm encounter có xác suất cao hơn;
- AOE weapon có giá trị;
- Security / Maintenance có thể xuất hiện robot hoặc turret.

---

# 6. MVP — Hospital

**Role:** medicine + biological risk.

| Property | Value |
|---|---|
| Size | Medium–Large |
| Rooms | 8–14 |
| Threat | 2–4 |
| Squad | 3–5 |
| Main loot | Medicine, medical equipment |
| Secondary | bio research, chemicals |
| Rare | advanced medkit, revival component, bio blueprint |

Room pool:

- Reception;
- Emergency Ward;
- Pharmacy;
- Surgery;
- ICU;
- Storage;
- Isolation;
- Morgue;
- Laboratory.

Example:

```
Reception
    ↓
Emergency Ward
 ├── Pharmacy
 ├── Surgery
 │     └── ICU
 └── Elevator
        ↓
      Morgue
        ↓
     Laboratory ???
```

Design:

- Pharmacy là optional high-value branch;
- Bio hazard tăng ở tầng sâu;
- Morgue/Lab có boss chance;
- player có thể loot Pharmacy rồi extract;
- full clear không bắt buộc.

---

# 7. MVP — Military Depot

**Role:** weapons / armor / military data.

| Property | Value |
|---|---|
| Size | Medium–Large |
| Rooms | 8–14 |
| Threat | 3–4 |
| Squad | 4–5 |
| Main loot | Weapon, armor, ammo abstraction / weapon parts |
| Secondary | military data, electronics |
| Rare | advanced weapon, blueprint fragment, authorization chip |

Room pool:

- Checkpoint;
- Barracks;
- Generator;
- Security;
- Armory;
- Command Room;
- Secure Vault;
- Vehicle Bay.

Example:

```
Checkpoint
    ↓
Barracks
 ├── Generator
 ├── Security
 │     ↓
 │   Armory
 └── Command Room
       ↓
    Secure Vault
```

Route decision:

- destroy Generator → giảm turret nhưng có thể khóa powered door;
- hack Security → mở Armory / disable alarm;
- push Command → đường nhanh nhưng resistance cao;
- Secure Vault là optional reward branch.

Engineer có giá trị cao nhưng không bắt buộc 100%.

---

# 8. MVP — Research Laboratory

**Role:** research data / blueprint / prototype component.

| Property | Value |
|---|---|
| Size | Medium–Large |
| Rooms | 8–15 |
| Threat | 3–5 |
| Squad | 4–5 |
| Main loot | Research Data |
| Secondary | electronics, chemical, prototype parts |
| Rare | blueprint, alien sample, prototype core |

Room pool:

- Lobby;
- Security;
- Server Room;
- Research Wing;
- Prototype Lab;
- Quarantine;
- Power;
- Deep Sector.

Example:

```
Lobby
 ↓
Security
 ↓
Research Wing
 ├── Server Room
 ├── Prototype Lab
 └── Quarantine
       ↓
     UNKNOWN
```

Research Lab là archetype showcase cho imperfect intel.

Electromagnetic activity không đảm bảo toàn bộ enemy là robot.

---

# 9. MVP — Metro / Tunnel

**Role:** branching route / ambush / rescue / long expedition.

| Property | Value |
|---|---|
| Size | Medium–Complex |
| Rooms | 10–18 |
| Threat | 2–5 |
| Squad | 3–5 |
| Main loot | mixed salvage |
| Secondary | survivor, utility, old-world cache |
| Rare | hidden bunker, abandoned train cargo, rescue target |

Room/node pool:

- Station;
- Platform;
- Train;
- Tunnel;
- Service Room;
- Maintenance;
- Control Room;
- Collapsed Sector;
- Hidden Bunker.

Example:

```
Station
  ↓
Platform
 ├──── Tunnel A
 │       ↓
 │   Service Room
 └──── Tunnel B
         ↓
    Abandoned Train
         ↓
        ???
```

Metro identity:

- nhiều route;
- ambush;
- map dài;
- extraction route có thể thay đổi;
- rất phù hợp Lost / Rescue mission.

---

# 10. MVP — Resource Site

**Role:** clear → capture → produce → defend / contest.

Canonical detailed Resource Site rules: [RESOURCE_SITES_V0.1.md](./RESOURCE_SITES_V0.1.md). Economy output values come from [ECONOMY_RESOURCES_V0.1.md](./ECONOMY_RESOURCES_V0.1.md).

Resource Site không phải dungeon loot một lần.

Lifecycle:

```
DISCOVER
→ SCOUT
→ CLEAR
→ CAPTURE
→ DEPLOY WORKERS
→ PRODUCE
→ DEFEND / CONTEST
→ LOSE / RECAPTURE
```

Prototype site types:

| Site | Output |
|---|---|
| Scrapyard | Metal |
| Chemical Plant | Chemical |
| Solar Farm | Energy Cell |
| Water Facility | Water |
| Uranium Mine | Reactor Material |
| Data Center | Research Data |
| Military Salvage Yard | Weapon Component |
| Alien Crater | Alien Material |

Example:

```
OLD URANIUM MINE

Status: CONTROLLED
Output: 3 Reactor Material/hour (canonical baseline before worker/integrity modifiers)
Workers: 3
Noise: HIGH
Security: LOW
```

Trade-off:

- output cao → Noise / discoverability cao hơn;
- site hiếm có khả năng bị Silo khác scout;
- contested resource tạo lý do PvP tự nhiên.

Không phải “đánh PvP vì có nút Attack”, mà vì hai bên cùng cần tài nguyên.

---

# 11. NPC Silo

**Role:** tutorial / mid-game bridge sang PvP Silo Raid.

| Property | Value |
|---|---|
| Size | Large–Complex |
| Rooms | 10–20 |
| Threat | 3–5 |
| Squad | 4–5 |
| Main loot | mixed strategic |
| Rare | military data, blueprint, survivor, core component |

Room pool:

- Surface Entrance;
- Security;
- Living;
- Power;
- Clinic;
- Workshop;
- Storage;
- Armory;
- Command;
- Deep Sector.

Example:

```
Entrance
 ↓
Security
 ↓
Living
 ├── Power
 ├── Clinic
 ↓
Command
 ↓
Deep Sector
```

NPC Silo dạy cùng language với Player Silo raid.

---

# 12. Player Silo

**Role:** asynchronous PvP dungeon.

Attacker không nhìn toàn bộ layout trước trận.

Scout example:

```
SILO CCL 8

Known:
Entrance
2 Security sectors
Power signature EAST
Population ~60

Unknown:
Vault
Command Core route
Defense squad
```

Map reveal dần khi attacker tiến vào.

**PvP cũng là exploration.**

Attacker có thể:

- raid resource;
- lấy intelligence;
- hunt blueprint;
- sabotage;
- push Command Core;
- extract sớm.

---

# 13. Alien Crash Site — Post-MVP

**Role:** high-risk exotic dungeon.

```
UNKNOWN OBJECT
CRASH SITE A-17

Size: UNKNOWN
Radiation: HIGH
Biological signal: UNKNOWN
Energy signal: EXTREME
```

Room concepts:

- Impact Zone;
- Hull Breach;
- Cargo Chamber;
- Organic Chamber;
- Energy Core;
- Sealed Compartment.

Alien site có độ bất định cao nhất.

Layout có thể collapse / shift / unlock theo encounter.

---

# 14. Target Card UI Contract

Target card prototype:

```
OLD LOGISTICS WAREHOUSE

Distance       8.4 km
Size           MEDIUM
Threat         ★★★☆☆
Intel          58%

Likely loot:
Metal          HIGH
Electronics    MEDIUM
Weapon         LOW

Detected:
Biological activity
Unknown lower sector

Squad recommendation:
3–4

[SCOUT]
[DEPLOY]
```

Không hiển thị:

- exact enemy count;
- exact resistance;
- exact boss;
- exact loot amount;
- complete layout.

---

# 15. Loot Affinity, không phải guarantee

Location type chỉ tăng xác suất.

Ví dụ Hospital:

- Medicine: HIGH;
- Chemical: MEDIUM;
- Weapon: LOW;
- Research: LOW–MEDIUM.

Nhưng vẫn có thể:

- không tìm thấy medicine ở một nhánh chưa clear;
- tìm súng của security;
- tìm hidden military cache;
- gặp survivor;
- gặp rare anomaly.

Điều này giữ exploration thật sự.

---

# 16. Rare Event Layer

Mỗi dungeon có thể roll 0–2 rare event tùy size/difficulty.

Prototype event:

- Hidden Cache;
- Survivor;
- Lost Squad Signal;
- Secret Room;
- Mini-boss;
- Boss;
- Faction Encounter;
- Mimic;
- Prototype Shipment;
- Alien Anomaly;
- Collapse;
- Power Restoration;
- Locked Vault.

Rare event không nên luôn được Scout reveal.

---

# 17. Objective Types

Location có thể sinh objective:

### Explore
đi sâu / reveal map.

### Scavenge
lấy đủ giá trị loot rồi extract.

### Clear
diệt threat chính.

### Recover
lấy item / data cụ thể.

### Rescue
tìm survivor / unit.

### Kill
hạ elite / boss.

### Capture
giành quyền kiểm soát site.

### Hold
giữ phòng / terminal trong thời gian.

### Raid
đột nhập Silo.

Mỗi archetype chỉ dùng objective phù hợp.

---

# 18. Extraction Contract

Không phải dungeon nào cũng cho rút giống nhau. Prototype curated House/Warehouse/Hospital always preserve a cleared path back to entry; generated path validator verifies objective and extraction reachable without a mandatory specialist/key absent from the map. One-way/collapse mechanics excluded from first slice. Session, body/cargo and force-close rules: MISSION_SESSION_REWARDS_V0.1.md and SURVIVOR_RECOVERY_V0.1.md.

### Normal
quay về entrance.

### Emergency
dùng Emergency Beacon / exit phụ.

### One-way Depth
đi sâu thì entrance bị khóa/collapse; phải tìm exit khác.

### Silo Raid
attacker phải quay về extraction route hoặc mở emergency exit.

Extraction complexity tăng theo difficulty, không chỉ enemy HP.

---

# 19. MVP success criterion

World Target system đạt yêu cầu khi tester nhìn:

- House;
- Warehouse;
- Hospital;
- Military Depot;
- Research Lab;

và tự có ý tưởng khác nhau về:

- team nên mang;
- weapon nên mang;
- consumable nên mang;
- loot kỳ vọng;
- lúc nào nên rút.

Nhưng tester **không được biết chắc** encounter cụ thể trước khi vào.
