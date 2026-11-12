# BURROW ZERO — Scout, Travel & Contracts v0.1

**Status:** Prototype baseline  
**Research influence:** directed progression + forgiving-but-meaningful extraction.

---

# 1. Discovery Flow

```
RADIO SEARCH
→ TARGET DISCOVERED
→ QUICK SCOUT / DEEP SCOUT
→ PREPARE
→ TRAVEL
→ ENTER
→ EXPLORE
→ EXTRACT
→ RETURN
```

Scout giảm uncertainty, không xóa uncertainty.

---

# 2. Radio Search

Player chọn:

- difficulty band;
- preferred loot;
- search radius.

Search không guarantee target hoàn hảo.

Prototype search time:

| Radius | Time |
|---|---:|
| 0–8 km | 30 sec |
| 9–15 km | 60 sec |
| 16–25 km | 90 sec |
| 26–40 km | 2 min |
| 41–60 km | 3 min |

Không có pay-to-skip trong core design.

---

# 3. Quick Scout

Purpose:

- cheap;
- nhanh;
- cho đủ thông tin để tránh blind deployment.

Base:

- Time: 20 sec;
- Cost: 1 Supply;
- Base Confidence: 42%.

Có thể reveal:

- Size band;
- Threat band;
- 1 likely loot category;
- 1 threat signal;
- obvious hazard.

Không reveal hidden sector.

---

# 4. Deep Scout

Base:

- Time: 90 sec;
- Cost: 2 Supply;
- Radio active power;
- optional Scout/Drone contribution;
- Base Confidence: 68%.

Có thể reveal:

- estimated room band;
- 2–3 threat signals;
- likely hazard;
- loot quality band;
- one route/entrance hint;
- boss/anomaly possibility;
- hidden area suspicion.

Không reveal exact enemy/resistance/loot.

---

# 5. Confidence Formula

Prototype:

```
Confidence =
Base
+ Radio Bonus
+ Scout Contribution
+ Drone Bonus
- Target Obscurity
- Interference
```

Caps:

```
Quick Scout: 30–72%
Deep Scout:  50–90%
```

Không bao giờ 100%.

Scout contribution:

```
(PER - 5) × 2%
+ Scout Role 5 percentage points (once; same bonus as Units role)
+ relevant Trait
```

---

# 6. Intel Error Philosophy

Game không nên “nói dối” trắng trợn quá thường xuyên.

Confidence thấp chủ yếu gây:

- khoảng ước tính rộng;
- hidden room không thấy;
- secondary threat không thấy;
- hazard intensity sai band;
- loot quality estimate lệch.

Ví dụ tốt:

```
Biological activity: HIGH
Mechanical activity: LOW / uncertain
```

không phải:

```
NO ROBOTS
```

rồi spawn 10 robot.

---

# 7. Drone Scout

Utility/Scout tool.

Bonus prototype:

- Deep Scout +8% confidence;
- có thể reveal 1 route node;
- risk bị mất nếu anti-drone/interference.

Drone không tự động trả exact map.

---

# 8. Travel Time

Prototype one-way:

```
Travel Time =
45 sec + 12 sec × Distance(km)
```

Cap:

```
10 min
```

Examples:

- 5 km → 1m45;
- 10 km → 2m45;
- 25 km → 5m45;
- 50 km → 10m cap.

Mục tiêu:

- distance có ý nghĩa;
- không biến game thành chờ 45 phút.

---

# 9. Travel Risk

Base chance có event:

```
5% + 0.5% × Distance(km)
```

Cap 25%.

Event rolled once and persisted at departure; resolved on arrival/return, no online-at-exact-second requirement. Secured loot/body cannot be lost on return. See MISSION_SESSION_REWARDS_V0.1.md.

Possible:

- minor ambush (outbound HP loss≤10%currentHP, cannot down; return nonlethal fiction);
- route delay;
- found cache;
- survivor signal;
- weather;
- no event.

Scout/Pathfinder giảm bad-event chance.

---

# 10. Travel Supply

Dùng formula Economy spec:

```
2
+ Squad Size
+ ceil(Distance / 5)
+ Heavy Load
+ Difficulty
```

Supply tính round-trip logistics baseline.

Emergency extraction có thể tăng thêm Supply/Beacon cost.

---

# 11. Extraction Accessibility

Bài học từ Duckov:

> turning back phải là lựa chọn hợp lệ, đặc biệt đầu game.

Normal dungeon:

- có thể quay lại entrance sau khi clear route;
- một số map có secondary exit;
- higher difficulty có thể collapse/lock route nhưng phải telegraph.

Không thiết kế mọi mission như hardcore one-way extraction.

---

# 12. Contracts = Onboarding

Không tutorial hệ thống chỉ bằng popup.

Contract dẫn player tới mechanic.

Early chain:

1. **Restore Water** → Water Treatment.
2. **We Need Food** → Hydroponics.
3. **First Signal** → Radio.
4. **Scavenge Supplies** → House.
5. **Parts for the Workshop** → Warehouse.
6. **Someone Is Hurt** → Hospital.
7. **Encrypted Broadcast** → Research Lab.
8. **Old Military Code** → Military Depot.
9. **Unknown Silo Signal** → NPC Silo.

Player học world target bằng nhu cầu thật của Silo.

---

# 13. Contract Layers

## Silo Need

Generated từ thiếu hụt / progression.

- medicine;
- component;
- research data;
- rescue.

## Story Signal

Curated narrative.

- first survivor contact;
- alien anomaly;
- faction;
- hidden structure.

## Faction Contract

Mid-game.

- recovery;
- escort abstracted;
- clear/capture;
- investigation.

## World Opportunity

Temporary.

- crash;
- rare convoy;
- contested site;
- distress signal.

---

# 14. Anti-Chore Contract Rules

Không:

- daily “kill 20 enemies” lặp vô nghĩa;
- yêu cầu rare RNG item không pity;
- ép log in mỗi 2 giờ;
- contract thất bại làm mất main progression.

Có:

- 2–4 meaningful contracts;
- progress overlap tự nhiên;
- contract chỉ hướng tới content, không bắt grind.

---

# 15. Target Expiry

Persistent:

- major building;
- known bunker;
- NPC Silo;
- discovered resource site.

Temporary:

- crash;
- distress signal;
- convoy/cache;
- anomaly.

Temporary lifetime prototype:

- 2–8 real hours tùy event.

Không expire target trong lúc squad đang travel/inside.

---

# 16. Post-Run Discovery

Một run có thể mở:

- new route;
- new world node;
- faction clue;
- hidden location;
- Bestiary knowledge.

Exploration tự mở exploration.

---

# 17. Success Criteria

Scout/Travel đạt khi:

1. scout đáng dùng nhưng không mandatory mọi run;
2. Deep Scout có giá nhưng không cho đáp án;
3. player có thể quay đầu sớm;
4. distance tạo logistics decision;
5. contracts dẫn player qua hệ thống tự nhiên;
6. không có wait timer vô lý.
