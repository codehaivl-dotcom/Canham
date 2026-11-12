# BURROW ZERO — Silo Expansion & Sector Control v0.1

**Status:** Prototype baseline  
**Core rule:** đào thấy không đồng nghĩa sở hữu.

---

# 1. Expansion Loop

```
SELECT ADJACENT ROCK
→ EXCAVATE
→ DISCOVER SECTOR
→ ASSESS
→ CLEAR / STABILIZE / RESTORE
→ ESTABLISH CONTROL
→ CONVERT OR RESTORE
→ CONNECT POWER / LIFE SUPPORT
```

Mỗi expansion có ít nhất một thử thách.

Không có:

> pay Scrap → room magically appears.

---

# 2. Sector Footprint

Prototype grid:

- 1 standard sector = 1 room footprint;
- special sector có thể chiếm 2–3 footprint;
- vertical shafts/elevator là connector.

Không khóa visual grid cuối cùng trước UI prototype.

---

# 3. Depth Bands

| Depth | Risk | Typical discovery |
|---|---|---|
| -1 to -3 | Low | debris, utility, civilian/pre-war |
| -4 to -6 | Low–Medium | military/service, infected |
| -7 to -10 | Medium | lab, reactor, bunker |
| -11 to -15 | High | old strategic facilities, alien trace |
| -16+ | High/Extreme | anomaly, deep structure, endgame |

Depth tăng mystery/risk chứ không chỉ HP.

---

# 4. Excavation Baseline

| Depth band | Scrap | Components | Time |
|---|---:|---:|---:|
| -1 to -3 | 40 | 0 | 1 min |
| -4 to -6 | 70 | 5 | 2 min |
| -7 to -10 | 110 | 10 | 4 min |
| -11 to -15 | 170 | 20 | 7 min |
| -16+ | 250 | 35 | 10 min |

Exact economy cần test sau.

---

# 5. Sector Discovery Table

Prototype weighted baseline:

| Discovery | Chance |
|---|---:|
| Collapsed/structural sector | 25% |
| Pre-war ordinary room | 20% |
| Utility conduit / infrastructure | 15% |
| Hostile nest | 15% |
| Old military/service room | 10% |
| Cache / sealed storage | 7% |
| Research/anomaly room | 5% |
| Alien trace/structure | 3% |

Chance shift theo depth/CCL/story.

Không roll hoàn toàn độc lập; generator cần bảo đảm pacing.

---

# 6. Every Sector Has a Challenge

## Structural

- clear debris;
- reinforce wall;
- repair ventilation;
- spend Scrap/time.

## Technical

- restore power;
- hack terminal;
- repair pump;
- Engineer/TEC helps.

## Environmental

- gas;
- radiation;
- flooded;
- contamination.

## Combat

- infected;
- robot;
- raider;
- alien.

## Multi-step

- restore lights;
- fight;
- seal breach;
- hold control terminal.

“Empty room” vẫn cần stabilization.

---

# 7. Sector States

```
UNEXCAVATED
→ DISCOVERED
→ UNSAFE
→ CLEARED
→ STABILIZED
→ CONTROLLED
→ ACTIVE
```

Special states:

- CONTAMINATED;
- SEALED;
- DAMAGED;
- CONTESTED;
- ANOMALOUS.

---

# 8. Control Requirement

Sector controlled khi:

1. hostile removed / bypassed;
2. hazard below safe threshold;
3. structure stabilized;
4. connection to Silo established;
5. optional control terminal secured.

Chỉ CONTROLLED sector mới cho build/restore.

---

# 9. Convert vs Restore

Nếu gặp pre-war facility:

### Convert

- phá/dọn;
- nhận buildable blank room;
- một phần salvage.

### Restore

- giữ original function;
- cần repair/material;
- có unique bonus;
- có thể có drawback.

Ví dụ:

**Old Military Medbay**

Restore:
- Clinic recovery +10%;
- power use cao hơn standard Clinic;
- không relocate.

Convert:
- lấy Scrap/Components;
- xây bất kỳ room standard.

---

# 10. Special Restorable Rooms

Examples:

- Pre-war Reactor;
- Military Medbay;
- Data Archive;
- Old Armory;
- Water Reservoir;
- Sensor Array;
- Cryo Chamber;
- Quarantine Lab;
- Alien Chamber.

Không tất cả đều objectively better.

---

# 11. Hidden Connection

Một sector có thể reveal:

- side tunnel;
- sealed elevator;
- ventilation shaft;
- deep shaft;
- old transit line.

Điều này có thể mở:

- shortcut trong Silo;
- new expansion branch;
- raid vulnerability;
- secret world target.

Base layout có history, không chỉ player-drawn grid.

---

# 12. Sector Threat Scaling

Prototype:

```
Threat Score =
Depth Band
+ CCL Progression
+ Special Sector Modifier
+ Story Modifier
```

Không scale tuyệt đối theo player power.

Một deep room có thể quá khó → player Seal Sector và quay lại sau.

---

# 13. Seal Sector

Player luôn có lựa chọn:

```
[SEAL]
```

Effect:

- đóng access;
- threat không lan trong normal state;
- room không usable;
- có thể reopen later.

Một số anomaly/event có thể phá seal nhưng phải là special event rõ.

---

# 14. Expansion Reward

Ngoài room space, expansion có thể cho:

- salvage;
- unique facility;
- lore;
- survivor;
- blueprint;
- shortcut;
- hidden world signal;
- Bestiary encounter.

Nhờ vậy mở rộng Silo cũng là exploration progression.

---

# 15. Expansion and PvP

Player Silo layout về sau dùng làm raid dungeon.

Natural discovered sectors tạo:

- chokepoint;
- alternate path;
- vulnerable tunnel;
- secret utility route.

Player build choices + geological history cùng tạo defense map.

Đây là signature differentiation.

---

# 16. Anti-Frustration

Generator không được:

- chặn toàn bộ expansion bằng boss quá mạnh;
- roll 4 hostile sector liên tiếp đầu game;
- bắt strategic material hiếm chỉ để có bed/food room;
- tạo dead-end không có cách mở branch mới.

Pacing guarantee:

- mỗi 3 discovered sectors đầu game có ít nhất 1 low-risk expansion;
- tutorial expansion outcome deterministic.

---

# 17. First Expansion Sequence

Curated:

```
UNKNOWN SECTOR
↓
Debris + 2 Crawler
↓
restore emergency lights
↓
clear contamination
↓
SECTOR CONTROLLED
↓
choose Hydroponics build
```

Dạy toàn bộ loop bằng gameplay.

---

# 18. Success Criteria

Expansion đạt khi:

1. mở base có suspense;
2. không phải mọi sector đều combat;
3. Engineer/Hazmat/combat squad đều có lúc hữu ích;
4. player có thể seal content quá khó;
5. discovered old room tạo lựa chọn Restore vs Convert;
6. layout của Silo có câu chuyện riêng.
