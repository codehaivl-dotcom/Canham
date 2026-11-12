# BURROW ZERO — Economy & Resources v0.1

**Status:** Prototype baseline  
**Rule:** số liệu là baseline để test, chưa phải final economy.

---

# 1. Economy Philosophy

Economy phải buộc người chơi ra ngoài nhưng không tạo quá nhiều currency.

Ba lớp:

1. **Survival** — Food, Water, Power.
2. **Construction/Crafting** — Scrap, Components, Chemicals, Credits.
3. **Progression/Conflict** — Research Data và strategic materials.

Không có một “gold” duy nhất mua được mọi thứ.

---

# 2. Player-facing Resources

## Survival

### Power

- flow resource;
- đo bằng **Power Units (PU)**;
- Generator tạo PU capacity;
- room tiêu thụ PU;
- Battery giữ reserve khi grid thiếu.

### Food

- stockpile;
- dân cư tiêu thụ theo thời gian.

### Water

- stockpile;
- dân cư tiêu thụ theo thời gian.

## Core materials

### Scrap

Dùng:

- xây;
- upgrade;
- craft cơ khí;
- repair.

### Components

Electronics/machinery abstraction.

Dùng:

- advanced room;
- weapon;
- defense;
- tech.

### Chemicals

Dùng:

- Clinic;
- Medkit;
- antidote;
- Bio/Rad gear;
- research.

### Credits

Soft currency của trade network.

Dùng:

- NPC market;
- recruit service;
- training/respec;
- trade fee;
- một số service.

**Credits không thay thế Scrap/Components khi xây base.**

### Research Data

Dùng mở:

- tech node;
- advanced recipe;
- room unlock;
- Bestiary analysis.

## Expedition

### Supply

Abstract deployment resource bao gồm:

- food pack;
- water;
- battery;
- logistics;
- field consumables cơ bản.

Không track từng hộp ration.

---

# 3. Strategic Resources

Không spam inventory. Chỉ dùng khi progression cần.

### Military Data

Nguồn:

- Military Depot;
- NPC Silo;
- PvP;
- military boss.

Dùng:

- military blueprint;
- security upgrade;
- advanced weapon.

### Reactor Material

Nguồn:

- Uranium Mine;
- reactor site;
- boss/event.

Dùng:

- late Generator/Reactor;
- advanced Power tech.

### Prototype Core

Nguồn:

- Hard/Extreme;
- elite/boss;
- prototype lab.

Dùng:

- Prototype gear;
- Prototype Forge.

### Alien Material

Nguồn:

- Alien site;
- alien boss;
- contested crater.

Dùng:

- Alien Tech;
- Xenobiology;
- Artifact research.

### Combat Data

Nguồn:

- PvP;
- NPC Silo challenge;
- tactical/security contracts;
- selected contested events.

Dùng:

- PvP/security research;
- tactical upgrades.

### Blueprint Fragment

Không phải currency chung.

Mỗi blueprint family có fragment riêng hoặc category-specific fragment.

---

# 4. Starting Economy

Prototype new Silo:

| Resource | Start |
|---|---:|
| Credits | 500 |
| Food | 100 |
| Water | 120 |
| Scrap | 300 |
| Components | 120 |
| Chemicals | 40 |
| Research Data | 0 |
| Supply | 20 |
| Population | 6 |

Starting Power:

- Emergency Core: **8 PU**;
- first Generator tutorial: +20 PU.

Emergency Core không upgrade và không đủ chạy Silo phát triển.

---

# 5. Population Consumption

Prototype per survivor / real hour:

```
Food  = 1.0 / hour
Water = 1.2 / hour
```

Ví dụ Population 10:

```
Food demand  = 10 / h
Water demand = 12 / h
```

Đây là lý do Hydroponics L1 = 10 Food/h và Water Treatment L1 = 12 Water/h.

---

# 6. Hunger / Dehydration

Không giết dân ngay khi kho về 0.

## Food = 0

0–1h:

- Morale loss.

1–4h:

- production -15%;
- healing -10%.

4h+:

- production -30%;
- combat deployment blocked cho exhausted civilian unit;
- health event chance.

## Water = 0

Nghiêm trọng hơn.

0–1h:

- Morale loss.

1–3h:

- production -25%;
- Clinic efficiency -25%.

3h+:

- injury/health event;
- combat readiness penalty.

Không thiết kế starvation như punishment khi người chơi offline qua đêm; offline cap/protection cần giữ economy sane.

---

# 7. Offline Production

Prototype:

- production tiếp tục **8 real hours** offline;
- consumption cũng chạy trong cùng window;
- nếu storage đầy, production dừng;
- không để Food/Water âm.

Có thể tăng offline cap bằng Command/Storage tech sau này, nhưng không monetize kiểu bắt buộc.

---

# 8. Power Grid

Công thức:

```
Net Power = Total Generation - Active Room Load
```

Recommended reserve:

```
Generation ≥ Load × 1.15
```

UI:

```
POWER

Generation  46 PU
Load        38 PU
Reserve     +8 PU
Battery     72%
```

---

# 9. Battery

Battery không tăng generation.

Nó giữ **Power-hours (PUh)**.

Ví dụ:

```
Battery = 20 PUh
Power deficit = 5 PU

Runtime ≈ 4 hours
```

Battery dùng khi:

- Generator bị phá;
- raid sabotage;
- room overload;
- temporary event.

---

# 10. Load Shedding

Khi Battery hết và Load > Generation:

Auto priority:

### Priority 1 — Life Support

- Water;
- basic Food;
- Clinic emergency;
- Command Core.

### Priority 2 — Security

- doors;
- alarms;
- essential defense.

### Priority 3 — Production

- Workshop;
- Training;
- Research;
- Recycler.

### Priority 4 — Luxury / optional

- morale room;
- cosmetic lighting;
- nonessential systems.

Player có thể chỉnh priority sau khi unlock Power Management.

---

# 11. Food Production

Hydroponics baseline:

```
L1 = 10 Food/h
```

Một L1 support ~10 survivor nếu chạy liên tục.

Production có thể bị ảnh hưởng bởi:

- worker efficiency;
- Power;
- room damage;
- event.

Không dùng worker stat bonus trong v0.1 economy formula cho đến Population spec.

---

# 12. Water Production

Water Treatment:

```
L1 = 12 Water/h
```

Support ~10 survivor.

Water nên là resource căng hơn Food một chút để tạo priority.

---

# 13. Supply Cost

Prototype formula:

```
Supply Cost =
2
+ Squad Size
+ ceil(Distance km / 5)
+ Heavy Load Modifier
+ Difficulty Modifier
```

Heavy Load:

- Rocket/Heavy Armor team: +1 đến +3.

Difficulty:

- Easy: +0
- Medium: +1
- Hard: +2
- Extreme: +4

Example:

3-unit Medium mission, 8 km, no heavy:

```
2 + 3 + 2 + 0 + 1 = 8 Supply
```

Supply được craft từ Food/Water/common material sau khi Workshop mở.

---

# 14. Supply Crafting Baseline

Prototype recipe:

```
5 Supply =
5 Food
6 Water
2 Scrap
```

Craft time:

```
2 minutes
```

Workshop không bắt buộc để tạo tutorial Supply nhỏ; Command Core có emergency packing queue 1.

---

# 15. Credits — Sources

Sources:

- mission reward;
- NPC contract;
- sell loot;
- trade;
- daily/weekly objective;
- faction job;
- PvP system reward.

Credits không drop thành đống vô lý từ quái.

---

# 16. Credits — Sinks

- NPC purchases;
- recruit contract;
- training;
- respec;
- market listing/trade fee;
- advanced service;
- cosmetic/local customization bằng soft currency.

Không dùng Credits để:

- revive vô hạn;
- bypass boss component;
- mua Artifact trực tiếp.

---

# 17. Core Material Sources

| Resource | Primary source |
|---|---|
| Scrap | House/Warehouse/Scrapyard |
| Components | Warehouse/Lab/Military |
| Chemicals | Hospital/Lab/Chem Plant |
| Research Data | Lab/Data Center/Quest |
| Credits | Contract/Trade |
| Supply | Craft/Silo logistics |

Location affinity chứ không guarantee.

---

# 18. Storage

Common stockpile categories:

- Food;
- Water;
- Scrap;
- Components;
- Chemicals;
- Supply.

Credits/Data không dùng physical storage cap trong MVP.

Storage full:

- production dừng;
- expedition loot vẫn có thể mang về nhưng phải salvage/sell/discard overflow.

Không xóa loot tự động.

---

# 19. Economy Pressure Targets

New player:

- 30–60 phút đầu không thiếu Food/Water nghiêm trọng;
- phải xây production sớm;
- expedition đầu tiên do curiosity/tutorial, không phải starvation.

Mid-game:

- internal production đủ basic survival;
- external world cần cho advanced progression.

Late-game:

- Silo tự chủ Food/Water;
- bottleneck chuyển sang strategic material / blueprint / contested content.

Đây là progression bắt buộc:

> Survival scarcity → Industrial scarcity → Strategic scarcity.

---

# 20. Resource Site Baseline Output

Prototype controlled site:

| Site | Output |
|---|---:|
| Scrapyard | 18 Scrap/h |
| Chemical Plant | 8 Chemicals/h |
| Solar Farm | 8 Energy Cells/h* |
| Water Facility | 30 Water/h |
| Uranium Mine | 3 Reactor Material/h |
| Data Center | 6 Research Data/h |
| Military Salvage | 5 Components/h + rare military roll |
| Alien Crater | 2 Alien Material/h |

*Energy Cell là field/strategic item; không cộng trực tiếp vào live grid nếu site ở xa.

Strategic site output chắc chắn phải giảm/điều chỉnh sau economy simulation.

---

# 21. Economy Anti-Snowball

PvP/resource control không được giúp người thắng snowball vô hạn.

Controls:

- site worker requirement;
- defense cost;
- Noise;
- diminishing control efficiency khi giữ nhiều site;
- PvP matchmaking;
- exposed-resource cap;
- strategic resource storage protection.

---

# 22. Premium Currency

**Không thiết kế trong v0.1.**

Nếu game monetization cần premium currency sau này:

- cosmetic;
- decoration;
- convenience có giới hạn.

Không đưa premium currency vào core economy trước khi core loop đã vui.

---

# 23. Economy Success Criteria

Economy đạt yêu cầu khi:

1. player hiểu ngay Food/Water/Power;
2. không phải học 15 currency trong tutorial;
3. basic survival tự chủ được;
4. advanced tech buộc expedition;
5. resource site có giá trị nhưng không bắt buộc 24/7;
6. PvP không phải nguồn duy nhất của progression;
7. strategic resource không thể mua thẳng bằng Credits;
8. storage và Power tạo decision nhưng không thành chores.
