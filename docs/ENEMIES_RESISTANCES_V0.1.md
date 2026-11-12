# BURROW ZERO — Enemies & Resistances v0.1

**Status:** Prototype balance baseline  
**Dependency:** [UNITS_ITEMS_V0.1.md](./UNITS_ITEMS_V0.1.md)  
**Important:** toàn bộ con số dưới đây dùng để dựng combat simulation. Chưa phải live balance cuối cùng.

---

# 1. Balance Reference

Reference band dùng cho bảng này:

- player level khoảng **8–12**;
- Tier 1–2 weapon;
- squad 3–4;
- khoảng 180–230 HP / unit;
- effective squad DPS khoảng 55–90 tùy loadout;
- combat room thường 15–45 giây;
- elite room 35–75 giây;
- boss encounter 60–120+ giây.

Không balance enemy riêng lẻ chỉ để tạo một TTK đẹp. Mục tiêu là **encounter composition**.

---

# 2. Threat Families

MVP có 4 family chính:

## Infected

Identity:

- số lượng;
- áp lực cận chiến;
- Bio hazard;
- mutation;
- thường yếu hơn với Fire;
- Chemical/Bio thường kém hiệu quả.

## Raider / hostile survivor

Identity:

- weapon tương tự người chơi;
- cover / target priority;
- Marksman / Breacher / Tech support;
- resistance khá trung tính;
- khó đoán bằng damage-type counter đơn giản.

## Mechanical

Identity:

- Armor cao;
- Fire/Bio kém hiệu quả;
- Electric/EMP rất có giá trị;
- Repair/support tạo priority target.

## Alien

Identity:

- profile khác nhau mạnh;
- nhiều mechanic lạ;
- không có một damage type luôn thắng;
- một số có Energy resistance cao;
- một số lại yếu Fire / Electric;
- Intel về Alien thường kém chính xác hơn.

---

# 3. Enemy Combat Roles

Enemy không chỉ có melee / ranged.

Prototype roles:

| Role | Chức năng |
|---|---|
| Swarm | số lượng, ép AOE |
| Bruiser | HP cao, Front pressure |
| Ranged | gây damage từ xa |
| Assassin | nhảy / target backline |
| Support | heal, shield, spawn, buff |
| Controller | poison, fear, disable, area denial |
| Tank | Armor/resist cao |
| Elite | nhiều mechanic kết hợp |
| Boss | phase + objective riêng |

---

# 4. Resistance Contract

Resistance nằm trong band:

```
-25% = vulnerability mạnh
  0% = neutral
 25% = resistant
 50% = strong resistance
 70% = severe resistance
 80% = prototype cap thông thường
```

Damage thực nhận:

```
Final × (1 - Resistance)
```

Ví dụ 70% Energy Resistance:

```
100 Energy → 30 damage
```

Không dùng immunity phổ biến.

Mechanical có thể có 80% Chemical/Bio, nhưng vẫn không phải 100%.

---

# 5. Armor Contract

Armor dùng công thức trong Units & Items:

```
Armor Reduction = Armor / (Armor + 120)
```

Armor chủ yếu ảnh hưởng Ballistic/direct physical.

Resistance vẫn là lớp matchup riêng.

---

# 6. Threat Cost / Encounter Budget

Mỗi enemy có **Threat Cost (TC)**.

TC không hiển thị cho player. Đây là tool cho encounter generator.

Prototype room budget:

| Difficulty | Typical TC | Peak room TC |
|---|---:|---:|
| Easy | 7–11 | 13 |
| Medium | 12–18 | 21 |
| Hard | 19–27 | 31 |
| Extreme | 28–38 | 44 |

Difficulty không chỉ tăng TC.

Nó còn có thể thêm:

- hazard;
- hidden reinforcement;
- worse extraction;
- elite chance;
- room modifier;
- incomplete intel.

---

# 7. Active Enemy Limit

Để combat vẫn đọc được theo phong cách Fallout Shelter:

- standard active enemies: **1–6**;
- swarm room: tối đa **8** visible nếu silhouette nhỏ;
- nếu encounter lớn hơn, dùng **waves**;
- boss adds nên giữ tổng active entity dễ đọc.

Không biến room thành 20 model chồng lên nhau.

---

# 8. INFECTION FAMILY

## INF-01 — Crawler

**Role:** Swarm / Front pressure

| Stat | Value |
|---|---:|
| HP | 70 |
| Damage | 8 |
| Attack Interval | 0.80s |
| Armor | 0 |
| Threat Cost | 2 |

Behavior:

- lao Front;
- ưu tiên target gần nhất;
- thường xuất hiện 2–5 con;
- dễ stagger.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 0% | -10% | -20% | 0% | 60% |

Purpose:

- dạy AOE;
- Rocket/Shotgun/Flamethrower có cảm giác mạnh;
- single-target Laser vẫn giết được nhưng inefficient.

---

## INF-02 — Spitter

**Role:** Ranged / Bio pressure

| Stat | Value |
|---|---:|
| HP | 95 |
| Damage | 11 |
| Attack Interval | 1.30s |
| Armor | 0 |
| Threat Cost | 3 |

Ability:

**Acid Spit**
- 20% chance áp Corrode;
- Corrode: -10 Armor trong 6 sec.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 5% | 0% | -15% | 0% | 70% |

Behavior:

- đứng Mid/Back;
- target Front nhưng có thể đổi sang Medic nếu Front bị down.

---

## INF-03 — Bloated

**Role:** Bruiser / Death hazard

| Stat | Value |
|---|---:|
| HP | 185 |
| Damage | 16 |
| Attack Interval | 1.55s |
| Armor | 8 |
| Threat Cost | 4 |

Ability:

**Rupture**
- khi chết gây 22 Bio damage trong vùng gần;
- có telegraph ngắn;
- có thể stagger trước khi nổ.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 5% | 0% | 20% | 5% | 0% | 65% |

Design:

Rocket vẫn gây damage tốt nhưng nổ chết nhiều Bloated cùng lúc có thể gây chain hazard.

---

## INF-04 — Mutated Brute

**Role:** Bruiser / Tank

| Stat | Value |
|---|---:|
| HP | 325 |
| Damage | 24 |
| Attack Interval | 1.50s |
| Armor | 25 |
| Threat Cost | 6 |

Ability:

**Heavy Slam**
- mỗi 8 sec;
- 26 damage;
- stagger Front.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 10% | 0% | 15% | -15% | 0% | 55% |

Purpose:

- single-target weapon có giá trị;
- Sniper/Laser xử lý tốt hơn pure swarm weapon.

---

## INF-05 — Hive Carrier

**Role:** Support / Spawn

| Stat | Value |
|---|---:|
| HP | 230 |
| Damage | 9 |
| Attack Interval | 1.10s |
| Armor | 10 |
| Threat Cost | 5 |

Ability:

**Brood Release**
- ở 65% HP: spawn 1 Crawler;
- ở 30% HP: spawn 1–2 Crawler;
- mỗi trigger chỉ xảy ra một lần.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 5% | 5% | -25% | 0% | 75% |

Priority lesson:

> giết Support sớm hay clear swarm trước?

---

# 9. RAIDER / HOSTILE SURVIVOR FAMILY

## HUM-01 — Scavenger Rifleman

**Role:** General ranged

| Stat | Value |
|---|---:|
| HP | 135 |
| Damage | 14 |
| Attack Interval | 0.90s |
| Armor | 8 |
| Threat Cost | 3 |

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 0% | 0% | 0% | 0% | 0% |

Behavior:

- generalist;
- dùng để baseline combat;
- có thể focus target đang thấp HP ở Hard.

---

## HUM-02 — Breacher

**Role:** Assault / Front breaker

| Stat | Value |
|---|---:|
| HP | 185 |
| Damage | 28 |
| Attack Interval | 1.55s |
| Armor | 15 |
| Threat Cost | 4 |

Ability:

**Breach Rush**
- đầu encounter lao Front;
- first hit +25% damage.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 5% | 0% | 0% | 0% | 0% | 0% |

---

## HUM-03 — Marksman

**Role:** Backline threat

| Stat | Value |
|---|---:|
| HP | 115 |
| Damage | 42 |
| Attack Interval | 2.20s |
| Armor | 5 |
| Threat Cost | 4 |

Ability:

**Marked Shot**
- every third attack ưu tiên Back/Mid;
- +15% crit.

Resistance: neutral toàn bộ.

Design:

- fragile;
- dangerous nếu ignored;
- tạo lý do focus target.

---

## HUM-04 — Tech Raider

**Role:** Support / Controller

| Stat | Value |
|---|---:|
| HP | 155 |
| Damage | 10 |
| Attack Interval | 1.00s |
| Armor | 12 |
| Threat Cost | 5 |

Ability:

**Jammer**
- mỗi 10 sec;
- giảm Accuracy squad 10% trong 5 sec.

**Deploy Shield Drone**
- 1 lần;
- cho ally thấp HP shield 50.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 0% | 0% | 0% | -10% | 0% |

Electric vulnerability phản ánh thiết bị mang trên người, không biến Tech Raider thành robot.

---

# 10. MECHANICAL FAMILY

## MEC-01 — Sentry Drone

**Role:** Fast ranged

| Stat | Value |
|---|---:|
| HP | 105 |
| Damage | 12 |
| Attack Interval | 0.75s |
| Armor | 20 |
| Threat Cost | 3 |

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 20% | 10% | 0% | 65% | -25% | 80% |

EMP:

- Disable threshold thấp;
- EMP Grenade disable 4 sec thay vì 3.

---

## MEC-02 — Security Bot

**Role:** Mechanical Tank

| Stat | Value |
|---|---:|
| HP | 245 |
| Damage | 20 |
| Attack Interval | 1.20s |
| Armor | 45 |
| Threat Cost | 6 |

Ability:

**Guard Protocol**
- +20% aggro;
- bảo vệ Mechanical support phía sau.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 30% | 15% | 10% | 70% | -20% | 80% |

---

## MEC-03 — Auto Turret Mk II

**Role:** Stationary DPS

| Stat | Value |
|---|---:|
| HP | 180 |
| Damage | 16 |
| Attack Interval | 0.65s |
| Armor | 35 |
| Threat Cost | 5 |

Behavior:

- stationary;
- không chase;
- accuracy cao;
- có thể disable bằng environment hack.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 25% | 10% | 0% | 80% | -25% | 80% |

Design:

Engineer có thể thắng encounter bằng interaction thay vì pure DPS.

---

## MEC-04 — Repair Drone

**Role:** Support / Priority target

| Stat | Value |
|---|---:|
| HP | 120 |
| Damage | 5 |
| Attack Interval | 1.50s |
| Armor | 15 |
| Threat Cost | 4 |

Ability:

**Repair Beam**
- heal Mechanical ally 18 HP/sec trong 3 sec;
- cooldown 8 sec.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 15% | 5% | -5% | 60% | -25% | 80% |

---

# 11. ALIEN FAMILY

## ALN-01 — Stalker

**Role:** Assassin

| Stat | Value |
|---|---:|
| HP | 145 |
| Damage | 18 |
| Attack Interval | 0.90s |
| Armor | 8 |
| Threat Cost | 4 |

Ability:

**Shadow Leap**
- một lần mỗi encounter;
- nhảy vào Back;
- first hit +20%.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 15% | 0% | 0% | 5% | 40% |

---

## ALN-02 — Crystal Beast

**Role:** Energy-resistant Bruiser

| Stat | Value |
|---|---:|
| HP | 305 |
| Damage | 22 |
| Attack Interval | 1.30s |
| Armor | 25 |
| Threat Cost | 7 |

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 10% | 70% | 25% | 35% | 20% | 50% |

Đây là canonical example cho **wrong weapon still works**.

Laser vẫn gây 30% damage sau resistance.

---

## ALN-03 — Spore Weaver

**Role:** Controller / Bio zone

| Stat | Value |
|---|---:|
| HP | 175 |
| Damage | 10 |
| Attack Interval | 1.00s |
| Armor | 5 |
| Threat Cost | 5 |

Ability:

**Spore Cloud**
- mỗi 9 sec;
- room zone 6 sec;
- Bio damage 4/sec;
- Antidote/Hazmat counter tốt.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 0% | 0% | -25% | 0% | 80% |

---

## ALN-04 — Rift Hound

**Role:** Fast Bruiser

| Stat | Value |
|---|---:|
| HP | 215 |
| Damage | 20 |
| Attack Interval | 0.80s |
| Armor | 12 |
| Threat Cost | 5 |

Ability:

**Phase Dash**
- 20% chance né một projectile hit;
- cooldown nội bộ 4 sec.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 5% | 25% | 10% | 5% | -5% | 30% |

---

## ALN-05 — Void Caster

**Role:** Ranged Controller / Shield

| Stat | Value |
|---|---:|
| HP | 165 |
| Shield | 120 |
| Damage | 26 |
| Attack Interval | 1.80s |
| Armor | 5 |
| Threat Cost | 6 |

Ability:

**Distortion Field**
- khi Shield còn active:
  - ally gần nhận +10% Energy resistance.

Shield interaction:

- Electric/EMP gây +40% buildup vào Shield;
- khi Shield break: stagger 2 sec.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 40% | 5% | 10% | -15% | 45% |

---

# 12. ELITES

Elite có mechanic rõ và không nên spawn như common enemy.

## ELT-01 — Alpha Brute

**Family:** Infected  
**Role:** Elite Bruiser / Fear

| Stat | Value |
|---|---:|
| HP | 680 |
| Damage | 32 |
| Attack Interval | 1.30s |
| Armor | 45 |
| Threat Cost | 14 |

Abilities:

**Roar**
- mỗi 14 sec;
- Resolve check;
- fail → -15% attack speed 5 sec.

**Ground Slam**
- Front/Mid AOE 35 damage;
- 9 sec cooldown.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 15% | 5% | 15% | -15% | 0% | 65% |

---

## ELT-02 — Warden Mech

**Family:** Mechanical  
**Role:** Elite Tank / Shield

| Stat | Value |
|---|---:|
| HP | 800 |
| Shield | 220 |
| Damage | 25 |
| Attack Interval | 1.00s |
| Armor | 70 |
| Threat Cost | 17 |

Abilities:

**Shield Cycle**
- Shield hồi 80 nếu không bị hit 5 sec.

**Suppression Burst**
- giảm Accuracy target 12% trong 4 sec.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 35% | 20% | 5% | 75% | -25% | 80% |

EMP là counter mạnh nhưng không bắt buộc tuyệt đối.

---

## ELT-03 — Phase Hunter

**Family:** Alien  
**Role:** Elite Assassin

| Stat | Value |
|---|---:|
| HP | 560 |
| Damage | 29 |
| Attack Interval | 1.00s |
| Armor | 20 |
| Threat Cost | 15 |

Abilities:

**Phase**
- mỗi 10 sec;
- untargetable 1.2 sec;
- sau đó xuất hiện ở Mid/Back.

**Marked Prey**
- chọn unit có HP thấp nhất;
- +15% damage vào target đó trong 6 sec.

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 0% | 50% | 10% | 5% | -10% | 45% |

---

# 13. BOSSES

Boss không chỉ là enemy HP lớn.

Mỗi boss có:

- phase;
- target priority;
- adds / environment;
- loot identity;
- preparation lesson.

---

## BOSS-01 — Hive Mother

**Family:** Infected / Alien Bio  
**Location:** Hospital deep lab / Nest / Bio facility

| Stat | Value |
|---|---:|
| HP | 2,700 |
| Damage | 24 |
| Attack Interval | 1.10s |
| Armor | 30 |
| Boss Budget | Fixed |

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 10% | 10% | 10% | -10% | 5% | 80% |

### Phase 1 — Nest Defense

100–70% HP:

- basic attack;
- spawn 2 Crawler mỗi 18 sec.

### Phase 2 — Acid Brood

70–35%:

- Spore/Acid zone;
- spawn 1 Spitter + 1 Crawler;
- room pressure tăng.

### Phase 3 — Frenzy

35–0%:

- attack interval giảm 15%;
- ngừng spawn;
- Slam mỗi 8 sec.

Preparation lesson:

- AOE giúp xử lý add;
- Fire mạnh nhưng không mandatory;
- pure single-target team vẫn thắng nếu quản lý add tốt.

Drops:

- Chitin Core;
- Bio Sample;
- Revival Component chance;
- Bio Weapon Blueprint fragment.

---

## BOSS-02 — War Machine A-17

**Family:** Mechanical  
**Location:** Military Depot / NPC Silo / Factory

| Stat | Value |
|---|---:|
| HP | 3,600 |
| Shield | 450 |
| Damage | 28 |
| Attack Interval | 1.00s |
| Armor | 85 |

Resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 40% | 25% | 10% | 80% | -25% | 80% |

### Phase 1 — Shielded

- Shield active;
- dual cannon;
- Repair Drone spawn ở 75%.

### Phase 2 — Armor Open

Shield break lần đầu:

- weak point exposed 12 sec;
- Armor hiệu quả giảm 35%;
- EMP có thể kéo dài exposure +3 sec.

### Phase 3 — Overheat

<35% HP:

- Fire resistance giảm từ 80% → 40%;
- attack speed +20%;
- room hazard pulses.

Preparation lesson:

- EMP rất tốt;
- Explosive vẫn viable;
- Ballistic team không bị 0 damage nhưng mất nhiều thời gian.

Drops:

- Military AI Core;
- Servo;
- Prototype Capacitor;
- Heavy Weapon Blueprint fragment.

---

## BOSS-03 — Fallen Visitor

**Family:** Alien  
**Location:** Alien Crash Site / Deep Research Sector

| Stat | Value |
|---|---:|
| HP | 3,100 |
| Shield | 600 |
| Damage | 31 |
| Attack Interval | 1.25s |
| Armor | 35 |

Base resistance:

| Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---:|---:|---:|---:|---:|---:|
| 10% | 55% | 15% | 15% | 0% | 60% |

### Adaptive Shell

Mỗi 20 sec:

- boss phân tích damage type gây nhiều damage nhất;
- +20% resistance với type đó;
- -15% resistance với damage type ngẫu nhiên khác;
- clamp every resistance after adaptation to[−25%,80%];
- telegraph rõ.

Mục tiêu:

> team mixed damage có lợi, nhưng specialized team vẫn có thể thắng bằng timing/consumable.

### Phase Shift

50% HP:

- teleport;
- spawn 2 Stalker;
- Shield 250 tái tạo một lần.

Drops:

- Alien Crystal;
- Neural Core;
- Unknown Data;
- Artifact Blueprint fragment.

---

# 14. Full Resistance Matrix

Values = damage reduction.

| Enemy | Ballistic | Energy | Explosive | Fire | Electric | Bio |
|---|---:|---:|---:|---:|---:|---:|
| Crawler | 0 | 0 | -10 | -20 | 0 | 60 |
| Spitter | 0 | 5 | 0 | -15 | 0 | 70 |
| Bloated | 5 | 0 | 20 | 5 | 0 | 65 |
| Mutated Brute | 10 | 0 | 15 | -15 | 0 | 55 |
| Hive Carrier | 0 | 5 | 5 | -25 | 0 | 75 |
| Rifleman | 0 | 0 | 0 | 0 | 0 | 0 |
| Breacher | 5 | 0 | 0 | 0 | 0 | 0 |
| Marksman | 0 | 0 | 0 | 0 | 0 | 0 |
| Tech Raider | 0 | 0 | 0 | 0 | -10 | 0 |
| Sentry Drone | 20 | 10 | 0 | 65 | -25 | 80 |
| Security Bot | 30 | 15 | 10 | 70 | -20 | 80 |
| Auto Turret | 25 | 10 | 0 | 80 | -25 | 80 |
| Repair Drone | 15 | 5 | -5 | 60 | -25 | 80 |
| Stalker | 0 | 15 | 0 | 0 | 5 | 40 |
| Crystal Beast | 10 | 70 | 25 | 35 | 20 | 50 |
| Spore Weaver | 0 | 0 | 0 | -25 | 0 | 80 |
| Rift Hound | 5 | 25 | 10 | 5 | -5 | 30 |
| Void Caster | 0 | 40 | 5 | 10 | -15 | 45 |
| Alpha Brute | 15 | 5 | 15 | -15 | 0 | 65 |
| Warden Mech | 35 | 20 | 5 | 75 | -25 | 80 |
| Phase Hunter | 0 | 50 | 10 | 5 | -10 | 45 |
| Hive Mother | 10 | 10 | 10 | -10 | 5 | 80 |
| War Machine A-17 | 40 | 25 | 10 | 80→40 | -25 | 80 |
| Fallen Visitor | 10 | 55 | 15 | 15 | 0 | 60 |

---

# 15. Weapon × Enemy Family Matchup

Legend:

- **++** strong;
- **+** favorable;
- **0** safe/neutral;
- **-** weak;
- **--** severe mismatch nhưng vẫn usable.

| Weapon | Infected | Raider | Mechanical | Alien |
|---|---|---|---|---|
| Pistol | 0 | 0 | - | 0 |
| SMG | 0 | + | - | 0 |
| Assault Rifle | 0 | + | 0/- | 0 |
| Shotgun | + swarm | + close | - | 0 |
| Laser Rifle | + brute | 0/+ | 0 | varies, Crystal -- |
| Sniper | + elite | + marksman | 0 | + elite |
| Rocket | ++ swarm | + | + | 0/+ |
| Flamethrower | ++ | 0/+ | -- | varies |
| EMP Rifle | - | 0 | ++ | + shielded |

Không có hàng nào luôn ++.

---

# 16. Encounter Composition Rules

Generator không được random enemy hoàn toàn.

Mỗi room chọn:

```
PRIMARY ROLE
+
SECONDARY PRESSURE
+
OPTIONAL SUPPORT
```

Ví dụ:

### Infected Medium

```
1 Mutated Brute (6 TC)
2 Crawler       (4 TC)
1 Spitter       (3 TC)

Total = 13 TC
```

### Mechanical Medium

```
1 Security Bot  (6)
1 Repair Drone  (4)
1 Sentry Drone  (3)

Total = 13
```

### Raider Hard

```
2 Rifleman      (6)
1 Breacher      (4)
1 Marksman      (4)
1 Tech Raider   (5)

Total = 19
```

Nhờ đó encounter có tactical shape.

---

# 17. Anti-Frustration Composition Rules

Không sinh các tổ hợp sau ở content bình thường:

- 3+ Marksman cùng lúc;
- 2+ Repair Drone nếu không có line-of-sight counter;
- 2 Elite trong cùng room dưới Hard;
- chain stun khiến squad mất quyền điều khiển >4 sec;
- 100% enemy cùng severe resistance với một damage type mà Intel đã báo ngược hoàn toàn;
- spawn add vô hạn.

Bất định phải tạo tension, không tạo cảm giác game gian lận.

---

# 18. Difficulty Modifier

Difficulty tăng chủ yếu bằng **budget + mechanic**, không phải stat inflation.

Prototype stat multiplier:

| Difficulty | Enemy HP | Enemy Damage |
|---|---:|---:|
| Easy | 0.90× | 0.90× |
| Medium | 1.00× | 1.00× |
| Hard | 1.10× | 1.10× |
| Extreme | 1.18× | 1.18× |

Ngoài ra:

### Easy
- ít Support;
- ít hazard;
- Intel đáng tin hơn.

### Medium
- baseline.

### Hard
- + elite chance;
- mixed family / hazard;
- reinforcement chance;
- extraction phức tạp hơn.

### Extreme
- elite/boss;
- room modifier;
- hidden sector;
- lower Intel confidence;
- retreat có thể khó hơn.

---

# 19. TTK Targets

TTK = time to kill khi squad focus một target cùng tier.

## Regular

Correct/neutral loadout:

- Swarm: 1.5–3 sec;
- Ranged: 2–4 sec;
- Support: 3–6 sec;
- Bruiser: 5–9 sec;
- Tank: 7–12 sec.

Severe mismatch:

- khoảng **1.5×–2.5× TTK**;
- không hướng tới 5×–10× trừ boss mechanic có telegraph.

## Elite

- correct loadout: 15–30 sec;
- poor loadout: 25–50 sec.

## Boss

Same-tier squad:

- 60–120 sec;
- wrong composition có thể 120–180 sec hoặc buộc extract;
- boss không nên chỉ là HP sponge: phase phải làm TTK có ý nghĩa.

---

# 20. Room Damage Targets

Một encounter đúng tier với Balanced Squad:

### Easy

- mất 0–10% tổng squad HP nếu chơi tốt.

### Medium

- mất 5–20%;
- đôi khi dùng Medkit.

### Hard

- mất 15–35%;
- consumable thường cần;
- sai target priority có thể làm 1 unit Down/Dead.

### Extreme

- có thể mất unit dù preparation tốt;
- retreat là outcome bình thường.

Những con số này sẽ được xác nhận bằng simulation.

---

# 21. Target Priority AI

Prototype priority:

## Swarm/Bruiser

1. Front;
2. nearest;
3. taunted target.

## Ranged

1. Front;
2. wounded Mid;
3. random valid.

## Assassin

1. Back;
2. lowest HP;
3. Medic/Engineer weighted.

## Support

- ưu tiên heal/shield ally;
- attack chỉ khi support action cooldown.

## Tank

- Front pressure;
- aggro manipulation.

AI không nên luôn perfect-focus Medic, nếu không formation mất ý nghĩa và combat quá punitive.

---

# 22. Status Effects Baseline

## Burn

- DOT;
- Mechanical thường resist cao;
- Infected thường yếu.

## Corrode

- giảm Armor;
- dùng bởi Bio/Acid enemy.

## EMP Disable

- Mechanical/Shield;
- dừng attack/ability;
- duration có diminishing return trên Elite/Boss.

## Stagger

- delay attack cycle;
- Elite/Boss resistance cao.

## Fear

- giảm attack speed/accuracy;
- RES counter.

## Poison/Bio

- DOT / heal penalty;
- Hazmat / Antidote counter.

---

# 23. Boss CC Rules

Để tránh stun-lock:

- Boss nhận Stagger duration ×0.35;
- EMP boss duration ×0.40;
- repeated same CC trong 8 sec giảm thêm 50%;
- vulnerability window có thể được mở bằng mechanic thay vì stun trực tiếp.

Boss vẫn phản ứng với build đúng, nhưng không bị vô hiệu hóa toàn trận.

---

# 24. Location Affinity

Không khóa cứng, chỉ tăng xác suất.

| Location | Common Threat |
|---|---|
| House | Infected / Raider |
| Warehouse | Infected / Raider / Mechanical |
| Hospital | Infected / Bio Alien |
| Military Depot | Mechanical / Raider |
| Research Lab | Mechanical / Alien / Infected |
| Metro | Infected / Raider / Alien |
| Resource Site | varies by site |
| NPC Silo | Raider / Mechanical / mixed |
| Alien Crash | Alien |

Một Hospital vẫn có thể chứa robot security.  
Một Military Depot vẫn có thể bị Alien chiếm.

---

# 25. Intel Hint Language

Scout không nên nói:

> “Crystal Beast, Energy Resistance 70%.”

Thay vào đó:

```
Mineralized biological signature detected.
Energy reflection unusually high.
Confidence: 63%
```

Player có thể suy ra:

> có khả năng Energy không tốt.

Deep Scout có thể rõ hơn:

```
Observed energy weapon impact:
LOW EFFECTIVENESS
Confidence: 78%
```

Không hiển thị exact resistance trước khi player đã gặp / research enemy đủ nhiều.

---

# 26. Bestiary Knowledge Progression

Sau khi gặp enemy, Silo lưu Bestiary.

Knowledge tiers:

### Unknown
- silhouette / family hint.

### Observed
- behavior;
- estimated HP class;
- likely weakness.

### Analyzed
- resistance band;
- ability details.

### Researched
- gần exact values;
- loot/component;
- tactical recommendation.

Điều này tạo progression thông tin mà không phá Imperfect Intel của từng location.

---

# 27. Encounter Variants

Một archetype có modifier:

- Armored;
- Frenzied;
- Diseased;
- Shielded;
- Alpha;
- Corrupted;
- Experimental.

Ví dụ:

```
ARMORED SPITTER
+25 Armor
-10% movement/attack rate
```

Hoặc:

```
FRENZIED CRAWLER
+20% attack speed
-15% HP
```

Không modifier nào được đảo hoàn toàn identity của enemy.

---

# 28. Loot Identity

Enemy drops không thay thế location loot.

Examples:

### Infected
- Bio Sample;
- gland;
- contaminated tissue.

### Raider
- weapon parts;
- gear;
- intel.

### Mechanical
- electronics;
- servo;
- circuit;
- AI fragment rare.

### Alien
- alien tissue;
- crystal;
- neural material;
- artifact fragment rare.

Boss drop progression item theo GDD.

---

# 29. Prototype Encounter Set

Để simulation bước sau, test ít nhất 12 room scenario:

1. 4 Crawler;
2. 1 Brute + 2 Crawler;
3. 1 Carrier + 2 Crawler + 1 Spitter;
4. 2 Rifleman + 1 Breacher;
5. 1 Marksman + 2 Rifleman;
6. 1 Tech Raider + 1 Breacher + 2 Rifleman;
7. 1 Security Bot + 1 Sentry Drone;
8. 1 Security Bot + 1 Repair Drone + 1 Drone;
9. 1 Crystal Beast + 1 Stalker;
10. 1 Spore Weaver + 2 Rift Hound;
11. 1 Void Caster + 2 Stalker;
12. 1 Elite encounter cho mỗi family.

Sau đó chạy 3 team:

- Balanced;
- Specialized đúng matchup;
- Wrong-loadout.

---

# 30. Success Criteria

Enemy system đạt yêu cầu khi:

1. player nhìn behavior và hiểu target priority;
2. AOE thật sự có giá trị khi swarm;
3. Laser thật sự có giá trị với single target nhưng gặp matchup xấu;
4. EMP thật sự thay đổi trận với Mechanical;
5. Assault Rifle vẫn là safe pick khi Intel kém;
6. wrong weapon không tạo 0 damage;
7. specialized team nhanh hơn khi đoán đúng;
8. balanced team ổn định hơn khi Intel sai;
9. retreat vẫn là lựa chọn hợp lệ;
10. boss cần preparation nhưng không bắt buộc một weapon cụ thể.

---

# 31. Next Step

Bước tiếp theo:

> **COMBAT_SIMULATION_V0.1**

Cần mô phỏng:

- player formulas;
- weapon accuracy/crit;
- armor;
- resistance;
- AOE;
- DOT;
- enemy DPS;
- heal;
- revive;
- squad 3/4/5;
- encounter budget.

Output cần trả lời bằng số:

- TTK thực tế;
- HP loss;
- consumable usage;
- matchup advantage;
- wrong-loadout penalty;
- boss duration.

Nếu simulation cho thấy một weapon hoặc enemy vượt xa target, chỉnh baseline trước khi thiết kế Loot/Crafting economy.
