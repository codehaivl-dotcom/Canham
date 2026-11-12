# BURROW ZERO — Silo Buildings & Power v0.1

**Status:** Prototype baseline  
**Dependency:** [ECONOMY_RESOURCES_V0.1.md](./ECONOMY_RESOURCES_V0.1.md)

---

# 1. Room Level Contract

Standard room có:

```
Level 1 → Level 5
```

Room max level theo CCL:

| CCL | Standard Room Max |
|---|---:|
| 1–2 | L1 |
| 3–4 | L2 |
| 5–6 | L3 |
| 7–9 | L4 |
| 10–12 | L5 |

Command Core dùng CCL riêng, không dùng Room L1–5.

---

# 2. Upgrade Cost Rule

Mỗi room có **Base Cost = L1 cost**.

Upgrade multipliers:

| Target level | Cost multiplier | Time multiplier |
|---|---:|---:|
| L1 build | 1.0× | 1.0× |
| L2 | 1.5× | 2.0× |
| L3 | 2.5× | 4.0× |
| L4 | 4.0× | 7.0× |
| L5 | 6.5× | 11.0× |

Round resource cost lên số nguyên.

Advanced room L4/L5 có thể thêm strategic material; không áp vào MVP trước balance.

---

# 3. Command Core / CCL

CCL là progression trung tâm.

| CCL | Main unlock |
|---|---|
| 1 | Survival rooms |
| 2 | Surface Gate + squad 3 + basic expedition |
| 3 | Radio/Scout + Workshop |
| 4 | Clinic/Training + Medium target |
| 5 | Research Lab + **squad cap 4** |
| 6 | Security/Armory + Resource Site capture |
| 7 | Network + NPC Silo + player signal |
| 8 | PvP Conflict + **squad cap 5** |
| 9 | Advanced Tech / Prototype Forge |
| 10 | Alien Tech / Xenobiology |
| 11 | Coalition systems |
| 12 | Surface Return / endgame |

Exact upgrade cost của CCL sẽ được chốt sau economy/content tuning; hiện dùng baseline trong các spec canonical.

Không nâng CCL chỉ bằng Credits.

---

# 4. Emergency Core

Starting infrastructure.

- Power: +8 PU;
- cannot upgrade;
- cannot be destroyed permanently;
- đủ duy trì tutorial life support;
- không đủ cho Silo phát triển.

Mục đích tránh soft-lock nếu Generator bị offline.

---

# 5. Generator

| Level | Power output | Base |
|---|---:|---|
| L1 | 20 PU |  |
| L2 | 32 PU |  |
| L3 | 46 PU |  |
| L4 | 62 PU |  |
| L5 | 80 PU |  |

Base cost L1:

- Scrap 80;
- Components 25;
- Build 2 min.

No fuel consumption trong MVP.

Late-game Reactor là building/upgrade family khác, không phải Generator L6.

---

# 6. Battery Bank

| Level | Reserve |
|---|---:|
| L1 | 20 PUh |
| L2 | 35 PUh |
| L3 | 55 PUh |
| L4 | 80 PUh |
| L5 | 110 PUh |

Power load:

- 0 PU passive;
- charge dùng surplus tự động.

Base cost:

- Scrap 50;
- Components 20;
- Build 1 min.

---

# 7. Water Treatment

| Level | Water/h | Power |
|---|---:|---:|
| L1 | 12 | 4 |
| L2 | 20 | 6 |
| L3 | 30 | 8 |
| L4 | 42 | 10 |
| L5 | 56 | 13 |

Base cost:

- Scrap 70;
- Components 20;
- Build 2 min.

---

# 8. Hydroponics

| Level | Food/h | Power |
|---|---:|---:|
| L1 | 10 | 5 |
| L2 | 17 | 7 |
| L3 | 26 | 9 |
| L4 | 36 | 12 |
| L5 | 48 | 15 |

Base cost:

- Scrap 80;
- Components 15;
- Chemicals 10;
- Build 3 min.

---

# 9. Living Quarters

| Level | Beds | Power |
|---|---:|---:|
| L1 | 6 | 1 |
| L2 | 10 | 1 |
| L3 | 14 | 2 |
| L4 | 18 | 2 |
| L5 | 24 | 3 |

Base cost:

- Scrap 60;
- Components 10;
- Build 2 min.

Population cannot exceed total beds except temporary rescue overflow.

Overflow survivors phải được housed trong grace period hoặc Morale penalty.

---

# 10. General Storage

| Level | Common capacity bonus | Power |
|---|---:|---:|
| L1 | +250 | 1 |
| L2 | +450 | 1 |
| L3 | +700 | 2 |
| L4 | +1000 | 2 |
| L5 | +1400 | 3 |

Base cost:

- Scrap 50;
- Components 10;
- Build 1 min.

Capacity áp riêng cho mỗi common stockpile category trong prototype để UI dễ hiểu.

Có thể chuyển sang shared capacity sau UX test.

---

# 11. Workshop

| Level | Craft speed | Queue | Power |
|---|---:|---:|---:|
| L1 | 1.00× | 1 | 4 |
| L2 | 1.15× | 1 | 5 |
| L3 | 1.35× | 2 | 6 |
| L4 | 1.60× | 2 | 8 |
| L5 | 1.90× | 3 | 10 |

Base cost:

- Scrap 100;
- Components 30;
- Chemicals 5;
- Build 5 min.

Functions:

- Supply;
- weapon;
- armor;
- consumable;
- repair;
- salvage.

---

# 12. Clinic

| Level | Beds | Heal speed | Power |
|---|---:|---:|---:|
| L1 | 2 | 1.00× | 4 |
| L2 | 3 | 1.20× | 5 |
| L3 | 4 | 1.45× | 6 |
| L4 | 5 | 1.75× | 7 |
| L5 | 6 | 2.10× | 8 |

Base cost:

- Scrap 90;
- Components 25;
- Chemicals 20;
- Build 5 min.

Clinic handles:

- injury;
- Trauma;
- infection;
- post-expedition recovery.

Dead unit không auto-revive ở Clinic nếu death condition đã khóa permanent loss.

---

# 13. Training Room

| Level | Slots | Training speed | Power |
|---|---:|---:|---:|
| L1 | 2 | 1.00× | 3 |
| L2 | 3 | 1.15× | 4 |
| L3 | 4 | 1.35× | 5 |
| L4 | 5 | 1.60× | 6 |
| L5 | 6 | 1.90× | 7 |

Base cost:

- Scrap 80;
- Components 20;
- Build 4 min.

Training:

- stat training;
- role proficiency;
- perk unlock later.

Không dùng Training để tạo level vô hạn offline.

---

# 14. Research Lab

| Level | Research speed | Queue | Power |
|---|---:|---:|---:|
| L1 | 1.00× | 1 | 6 |
| L2 | 1.20× | 1 | 8 |
| L3 | 1.45× | 2 | 10 |
| L4 | 1.75× | 2 | 12 |
| L5 | 2.10× | 3 | 15 |

Base cost:

- Scrap 140;
- Components 50;
- Chemicals 10;
- Build 8 min.

Uses Research Data.

Research unlocks capability; không tự tạo Research Data đáng kể.

---

# 15. Radio / Scout Center

| Level | Search radius | Intel bonus | Power |
|---|---:|---:|---:|
| L1 | 8 km | +0% | 4 |
| L2 | 15 km | +5% | 6 |
| L3 | 25 km | +10% | 8 |
| L4 | 40 km | +15% | 10 |
| L5 | 60 km | +20% | 13 |

Base cost:

- Scrap 110;
- Components 40;
- Build 5 min.

Functions:

- target search;
- Quick Scout;
- Deep Scout;
- human signal detection;
- later alliance/network.

Intel bonus không thể đưa confidence lên 100%.

---

# 16. Security Room

| Level | Defense Capacity | Power |
|---|---:|---:|
| L1 | +20 | 3 |
| L2 | +35 | 4 |
| L3 | +55 | 6 |
| L4 | +80 | 8 |
| L5 | +110 | 10 |

Base cost:

- Scrap 100;
- Components 35;
- Build 4 min.

Defense Capacity dùng cho:

- turret;
- door;
- sensor;
- drone;
- guard post.

Không cho spam defense vô hạn.

---

# 17. Armory

| Level | Gear capacity | Loadout prep bonus | Power |
|---|---:|---:|---:|
| L1 | 20 | 0% | 3 |
| L2 | 35 | +5% | 4 |
| L3 | 55 | +10% | 5 |
| L4 | 80 | +15% | 6 |
| L5 | 110 | +20% | 8 |

Base cost:

- Scrap 120;
- Components 40;
- Build 6 min.

Gear capacity tính weapon/armor special inventory.

Không thay General Storage.

---

# 18. Recycler

| Level | Scrap/h | Power |
|---|---:|---:|
| L1 | 2 | 3 |
| L2 | 4 | 4 |
| L3 | 7 | 5 |
| L4 | 10 | 6 |
| L5 | 14 | 8 |

Base cost:

- Scrap 70;
- Components 25;
- Build 4 min.

Recycler tạo ít Scrap từ waste.

Không được mạnh đến mức làm expedition Warehouse/Scrapyard vô nghĩa.

---

# 19. Surface Gate / Airlock

Không upgrade theo L1–5 ở MVP.

Functions:

- deployment;
- return;
- quarantine check;
- raid entrance.

Power:

- 2 PU active baseline.

CCL2 unlock.

Later upgrades có thể:

- giảm deployment time;
- emergency seal;
- contamination control;
- extra extraction prep.

---

# 20. Prototype Forge

CCL9.

Không cần full number ở MVP đầu.

Role:

- Prototype gear;
- boss component;
- advanced blueprint.

Power target baseline:

- 12–18 PU khi active.

Không idle consume full load nếu không craft.

---

# 21. Xenobiology Lab

CCL10.

Role:

- Alien Material;
- Exposure management;
- Alien gear;
- Bestiary advanced research.

Power target:

- 12–18 PU active.

Có thể tăng Signal/Noise.

---

# 22. Room Active vs Idle Power

Để grid thú vị hơn mà không quá phức tạp:

Production room dùng listed Power liên tục.

Craft/research special room:

- Idle = 40% listed load;
- Active = 100%.

Ví dụ Workshop L3:

```
Idle = ~2.4 PU
Crafting = 6 PU
```

UI round display nhưng simulation có thể dùng decimal.

---

# 23. Build State

Room states:

- OFFLINE;
- BUILDING;
- ACTIVE;
- IDLE;
- UNPOWERED;
- DAMAGED;
- DISABLED;
- CONTESTED;
- CONTAMINATED.

State ảnh hưởng output rõ ràng.

---

# 24. Damage / Repair Baseline

PvE internal event/PvP có thể damage room.

Prototype health:

```
Room Integrity = 100%
```

At:

- <75%: no penalty;
- <50%: output -20%;
- <25%: output -50%;
- 0%: disabled, không destroyed permanently.

Repair dùng:

- Scrap;
- Components nếu advanced;
- worker/time.

Defender không mất building đã xây.

---

# 25. CCL Upgrade Principle

CCL upgrade cần 4 loại requirement:

1. population/stability;
2. room milestone;
3. common materials;
4. từ mid-game: external progression item.

Example CCL5 → CCL6:

- Population ≥ 18;
- Generator ≥ L3;
- Workshop ≥ L2;
- Research Lab ≥ L1;
- Scrap;
- Components;
- 1 Military Authorization item.

Exact CCL cost table sẽ làm sau Loot/Crafting economy.

---

# 26. Starting Layout

Prototype:

```
SURFACE
[Airlock]

LEVEL -1
[Command Core] [Generator]

LEVEL -2
[Water] [Living]

LEVEL -3
[Storage] [UNKNOWN SECTOR]

LEVEL -4
[SEALED] [SEALED]
```

Tutorial flow:

1. activate Emergency Core;
2. repair Generator;
3. restore Water;
4. house 6 survivors;
5. clear first UNKNOWN sector;
6. build Hydroponics;
7. unlock Surface Gate / first expedition.

---

# 27. First 60-minute Power Target

Early example after several rooms:

```
Emergency Core   +8
Generator L1    +20
-------------------
Generation       28 PU

Command Core     -2
Water L1         -4
Hydro L1         -5
Living L1        -1
Storage L1       -1
Workshop L1      -4
Radio L1         -4
Airlock          -2
-------------------
Load             23 PU

Reserve           5 PU
```

Reserve ≈22%.

Player có room để mở Clinic/Training nhưng sẽ sớm cần Generator L2 hoặc power-management decision.

Đây là intentional pressure.

---

# 28. Building Success Criteria

Building economy đạt yêu cầu khi:

1. Power thật sự buộc player ưu tiên room;
2. upgrade room có ý nghĩa khác ngoài +10%;
3. Food/Water scale với population;
4. Silo không tự sản xuất strategic material;
5. Generator không trở thành “luôn upgrade đầu tiên” vô điều kiện;
6. room damage có hậu quả nhưng không xóa progress;
7. CCL unlock tạo milestone rõ;
8. squad cap 4/5 gắn với Silo progression.
