# CĂN HẦM — Units, Weapons & Items v0.1

**Status:** Prototype balance baseline  
**Important:** số liệu dưới đây dùng để dựng combat prototype. Chưa phải live balance cuối cùng.

---

# 1. Combat Scale

Mục tiêu:

- combat dễ đọc;
- mỗi unit có giá trị;
- squad 3–5;
- room combat thường kéo khoảng 15–45 giây;
- boss room kéo dài hơn;
- sai loadout làm trận khó hơn nhưng không biến thành 0 damage.

Prototype level cap: **50**.

MVP có thể chỉ test level 1–20.

---

# 2. Core Unit Stats

Mỗi stat tự nhiên nằm trong band **1–10** trước gear/perk.

| Stat | Viết tắt | Tác dụng chính |
|---|---|---|
| Combat | COM | weapon handling / base damage efficiency |
| Endurance | END | HP / injury resistance |
| Agility | AGI | attack speed / reposition |
| Perception | PER | accuracy / crit / detection |
| Intelligence | INT | research / tactical ability |
| Tech | TEC | hacking / robot / device |
| Medical | MED | heal / revive |
| Resolve | RES | morale / fear / psychic resistance |

Một survivor bình thường level 1 có tổng khoảng **32–44 điểm**.

Không dùng rarity để quyết định toàn bộ sức mạnh unit.

Unit tốt đến từ:

- stat distribution;
- traits;
- role;
- training;
- gear;
- combat history.

---

# 3. Base Derived Stats

Prototype formulas:

### Max HP

```
HP = 100 + END × 12 + (Level - 1) × 5
```

Ví dụ Level 1 END 5:

```
160 HP
```

Level 20 END 7:

```
279 HP
```

### Base damage efficiency

```
Damage Multiplier = 1 + (COM - 5) × 0.03
```

COM 3 → 0.94×  
COM 5 → 1.00×  
COM 8 → 1.09×

Stats giúp rõ nhưng không được nghiền nát gear choice.

### Attack speed

```
Attack Speed Multiplier = 1 + (AGI - 5) × 0.025
```

AGI 9 ≈ +10%.

### Accuracy

```
Final Accuracy = Weapon Accuracy + (PER - 5) × 2%
```

Cap prototype:

```
55% ≤ Accuracy ≤ 98%
```

### Critical Chance

```
Crit = Weapon Crit + max(0, PER - 5) × 1%
```

Critical damage baseline:

```
1.5×
```

### Medical Power

```
Heal Multiplier = 1 + (MED - 5) × 0.05
```

### Tech Power

TEC ảnh hưởng:

- hack time;
- turret disable;
- EMP duration;
- robot utility;
- technical interaction.

Prototype:

```
Tech Effect Multiplier = 1 + (TEC - 5) × 0.05
```

### Resolve

RES giảm:

- panic;
- psychic damage;
- morale loss;
- flee / disruption effects.

Không dùng RES như generic magic defense.

---

# 4. Level Progression

Level tăng bằng combat / expedition XP.

Prototype:

- Level 1–10: nhanh;
- 11–30: trung bình;
- 31–50: chậm.

Mỗi level:

- +5 base HP thông qua formula;
- tăng nhẹ secondary progression.

Mỗi **5 level**, unit nhận:

- +1 trainable stat point;

hoặc:

- perk choice tại milestone nhất định.

Không tăng tất cả stat mỗi level để tránh inflation quá mạnh.

---

# 5. Roles

Role là combat training, không phải class khóa cứng tuyệt đối.

## Vanguard

Passive prototype:

- +20% Max HP;
- +25% aggro weight;
- +15% stagger resistance.

Thích hợp:

- Heavy / Combat Armor;
- Shotgun;
- shield utility.

## Assault

Passive:

- +8% weapon damage;
- +5% reload / attack-cycle efficiency.

General DPS.

## Scout

Passive:

- +5% crit;
- +10% accuracy với first target;
- +15% Scout Intel contribution.

## Engineer

Passive:

- +20% Tech Effect;
- hack / disable nhanh hơn;
- EMP duration +20%.

## Medic

Passive:

- +25% healing;
- revive action nhanh hơn 25%;
- revived unit nhận thêm +10% HP.

## Heavy / Specialist

Passive:

- +15% AOE / stagger effect;
- heavy weapon penalty giảm 50%.

Role này có thể tách Heavy và Specialist sau prototype.

---

# 6. Squad Size

Đã khóa:

```
Early     3
Mid       4
Late      5
Max       5
```

Không tăng quá 5 trong standard combat.

Mốc CCL chính xác sẽ thiết kế trong Silo Progression.

---

# 7. Formation

Prototype:

```
          FRONT
          [ 1 ]

       [ 2 ] [ 3 ]

       [ 4 ] [ 5 ]
          BACK
```

Effects prototype:

### Front

- aggro weight +25%;
- melee exposure +25%;
- shotgun effectiveness +10%;
- sniper accuracy -10%.

### Mid

- neutral.

### Back

- aggro weight -20%;
- sniper accuracy +5%;
- melee damage received +15% nếu bị flank.

Không biến formation thành grid tactical game.

---

# 8. Damage Formula

Prototype:

```
Raw = Weapon Base Damage
    × COM Multiplier
    × Role Modifier
    × Buff/Debuff

After Accuracy:
Hit or Miss

After Armor:
Damage × ArmorMultiplier

After Resistance:
Damage × (1 - Resistance)

Final Damage:
max(1, result)
```

Resistance prototype cap:

```
-25% vulnerability
to
80% resistance
```

Hard immunity chỉ dành cho mechanic đặc biệt hiếm.

---

# 9. Armor Formula

Armor chủ yếu giảm direct physical / ballistic damage.

Prototype:

```
Armor Reduction = Armor / (Armor + 120)
```

Examples:

| Armor | Reduction |
|---:|---:|
| 10 | 7.7% |
| 25 | 17.2% |
| 40 | 25.0% |
| 60 | 33.3% |
| 100 | 45.5% |

Energy / Fire / Electric / Bio phụ thuộc nhiều hơn vào resistance riêng.

---

# 10. Damage Types

Prototype types:

- Ballistic;
- Energy;
- Explosive;
- Fire;
- Electric/EMP;
- Chemical/Bio.

Không phải mọi weapon cần một type thuần; một số item có mixed profile.

---

# 11. Weapon Baseline

Các giá trị dưới đây giả định item Tier 1–2, không phải endgame.

| Weapon | Dmg/Hit | Interval | Base DPS | Accuracy | Crit | Identity |
|---|---:|---:|---:|---:|---:|---|
| Pistol | 17 | 0.90s | 18.9 | 86% | 5% | backup / cheap |
| SMG | 10 | 0.38s | 26.3 | 76% | 4% | close-mid sustained |
| Assault Rifle | 16 | 0.62s | 25.8 | 82% | 5% | safe generalist |
| Shotgun | 34 | 1.25s | 27.2 | 78% | 4% | close cone |
| Laser Rifle | 11 | 0.40s | 27.5 | 88% | 5% | single focus |
| Sniper Rifle | 52 | 1.90s | 27.4 | 92% | 12% | elite/boss burst |
| Rocket Launcher | 56 | 2.50s | 22.4 | 80% | 3% | AOE burst |
| Flamethrower | 7 | 0.25s | 28.0 | 90% | 0% | cone + DOT |
| EMP Rifle | 9 | 0.70s | 12.9 | 86% | 2% | disable / anti-system |

DPS không phản ánh toàn bộ sức mạnh vì effect khác nhau.

---

# 12. Weapon Effects

## Pistol

- không penalty formation;
- low deployment cost;
- good sidearm;
- không có specialty mạnh.

## SMG

- +10% damage ở Front/Mid;
- -15% accuracy ở range xa;
- suppress nhẹ.

## Assault Rifle

- không matchup quá tệ;
- không bonus lớn;
- lựa chọn tốt khi Intel thấp.

## Shotgun

Prototype cone:

- primary target: 100%;
- target thứ 2 trong cone: 45%;
- target thứ 3: 25%.

Front position:

- +10% final damage.

## Laser Rifle

Focus mechanic:

```
same target continuously:
+4% damage / second
cap +20%
```

Đổi target reset Focus.

Laser mạnh với single target nhưng kém swarm.

## Sniper Rifle

- +20% damage vs Elite/Boss;
- Back position +5% accuracy;
- bị pressure nếu enemy vào close range.

## Rocket Launcher

Explosion:

- primary: 100%;
- nearby target 2: 60%;
- nearby target 3: 45%;
- nearby target 4: 30%.

Stagger cao.

Reload/attack cycle dài.

## Flamethrower

Cone:

- primary: 100%;
- up to 2 nearby targets: 60%.

Burn:

```
3 damage / second × 4 sec
```

Refresh duration, không stack vô hạn.

## EMP Rifle

Raw damage thấp.

Against Mechanical / Shielded:

- EMP buildup;
- đủ threshold → Disable 2.5s baseline;
- Engineer tăng duration.

Organic target vẫn nhận raw damage thấp.

---

# 13. Soft Counter Rule

Ví dụ Crystal Beast:

| Damage type | Resistance |
|---|---:|
| Ballistic | 10% |
| Energy | 70% |
| Explosive | 25% |
| Fire | 35% |
| Electric | 20% |

Laser vẫn gây:

```
30% damage sau resistance
```

Không hiện IMMUNE trừ mechanic đặc biệt.

---

# 14. Weapon Tier Scaling

Tier tăng không chỉ tăng damage.

Prototype numeric band:

| Tier | Raw stat budget so với Tier 1 |
|---|---:|
| Civilian | 1.00× |
| Industrial | 1.05× |
| Military | 1.12× |
| Advanced | 1.20× |
| Prototype | 1.28× |
| Alien | 1.25–1.35× + trade-off |
| Artifact | unique, không dùng scaling thuần |

Mục tiêu:

một Military Assault Rifle đúng matchup vẫn có thể tốt hơn Prototype weapon sai matchup.

---

# 15. Example Weapon Items

## C-9 Civilian Pistol

- Damage 17;
- Interval 0.90;
- Accuracy 86%;
- common;
- repair/craft rẻ.

## M-4 Service Rifle

- Damage 18;
- Interval 0.62;
- Accuracy 83%;
- Military;
- stable general-purpose.

## LX-3 Laser Carbine

- Damage 13;
- Interval 0.40;
- Focus cap +20%;
- Energy;
- Advanced.

## HSR-12 Marksman Rifle

- Damage 60;
- Interval 1.90;
- +20% vs Elite/Boss;
- Military/Advanced.

## R-7 Breach Launcher

- Damage 64;
- Interval 2.55;
- Explosive;
- AOE profile 100/60/45/30;
- Military.

## PYR-2 Incinerator

- Damage 8/tick;
- 0.25 sec;
- Fire;
- cone + Burn;
- Advanced.

---

# 16. Armor Archetypes

| Armor | Armor | Special | Penalty |
|---|---:|---|---|
| Civilian Jacket | 6 | none | none |
| Light Scout Armor | 15 | +5% reposition, +5 PER checks | none |
| Combat Armor | 30 | +10% Ballistic Resist | -3% attack speed |
| Heavy Armor | 48 | +15% stagger resist | -8% attack speed |
| Hazmat Suit | 12 | +45% Bio/Rad Resist | -5% Armor vs ballistic |
| Insulated Suit | 18 | +35% Electric/Energy Resist | none |

Armor resistance được áp sau generic armor nếu phù hợp.

---

# 17. Armor Upgrade Philosophy

Upgrade armor có thể tăng:

- Armor;
- specific resistance;
- utility slot;
- injury resistance.

Không chỉ tăng HP.

Prototype gear upgrade:

```
Mk I → Mk II → Mk III
```

Mỗi bước khoảng:

- +6–10% numeric value;

và milestone có thể mở modifier.

---

# 18. Utility Items

## Tactical Scanner

- +10% Scout confidence nếu unit tham gia scout;
- trong dungeon: reveal threat hint của room kế bên một lần.

## Portable Shield

- tạo shield = 25% Max HP;
- duration 10 sec;
- cooldown / charge giới hạn.

## Breaching Tool

- mở một số locked door;
- giảm nhu cầu phá cửa bằng combat.

## Drone

- reveal 1 adjacent room;
- có xác suất bị destroy nếu room có anti-drone.

## Bio Scanner

- tăng chance phát hiện infection / mimic clue;
- +15% Bio hazard detection.

## Shield Module

- +10% Energy resist;
- +5% Max HP shield layer nếu armor hỗ trợ.

---

# 19. Consumable Slots

Prototype:

- mỗi unit: **2 consumable slots**;
- mỗi slot chứa một item type;
- stack size tùy item.

Squad 3 → tối đa 6 slot.  
Squad 5 → tối đa 10 slot.

Điều này làm squad lớn có thêm carrying flexibility nhưng cũng tăng supply cost.

---

# 20. Consumables

| Item | Effect | Stack |
|---|---|---:|
| Medkit | heal 35% Max HP | 2 |
| Combat Stim | +15% dmg, +15% attack speed, 15 sec | 2 |
| Antidote | remove Poison/Bio + 30% Bio resist 20 sec | 2 |
| Rad Injector | giảm Radiation / +40% Rad resist 30 sec | 2 |
| Frag Grenade | 55 Explosive AOE | 2 |
| EMP Grenade | 20 Electric + Disable Mechanical 3 sec | 2 |
| Smoke Charge | enemy accuracy -20% trong room, 8 sec | 2 |
| Breach Charge | phá một door / gây 40 explosive near door | 1 |
| Emergency Beacon | mở emergency extraction nếu location cho phép | 1 |
| Revival Injector | revive unit | 1 |

---

# 21. Medkit

Base:

```
Heal = 35% Max HP × Heal Multiplier
```

Medic role:

+25% heal.

Ví dụ 240 HP target, MED 7 Medic:

```
Base = 84
MED multiplier = 1.10
Medic role = 1.25

Heal ≈ 116 HP
```

Cap healing không vượt Max HP.

---

# 22. Revival Injector

Rare consumable.

Prototype effect:

- target phải DEAD/DOWN và body còn recoverable;
- revive với 30% Max HP;
- Medic role revive → 40% Max HP;
- unit nhận **Trauma**:
  - -15% damage;
  - -10% attack speed;
  - kéo dài đến khi về Clinic.

Không thể spam revive cùng một unit vô hạn.

Prototype rule:

```
1 successful field revive / unit / mission
```

Lần chết tiếp theo phải extract body hoặc mất unit tùy encounter.

---

# 23. Injury

Khi unit bị hạ / nhận heavy damage có thể roll Injury.

Prototype injuries:

- Fracture: -10% AGI effective;
- Concussion: -10% accuracy;
- Burn: -10% Max HP;
- Infection: periodic HP/morale penalty;
- Trauma: combat penalty sau revive.

Clinic chữa theo thời gian/resource.

---

# 24. Item Quality / Affixes

Không dùng affix spam kiểu +1.3% vô nghĩa.

Prototype item có tối đa:

- 1 Major Modifier;
- 1 Minor Modifier;

ở tier cao.

Ví dụ:

### Stabilized

+6% accuracy.

### Reinforced

+8 Armor.

### Overcharged

+10% Energy damage, +8% Heat/Noise.

### Lightweight

-5% attack interval penalty / hoặc giảm mobility penalty.

### Corrosive

thêm DOT nhỏ, nhưng durability/deployment cost cao hơn nếu hệ thống đó được bật.

---

# 25. Alien Item Trade-off

Alien gear không chỉ mạnh miễn phí.

Ví dụ:

## Neural Beam

- +25% single-target damage;
- Energy;
- mỗi room tăng Alien Exposure.

## Living Armor

- tự heal 1% HP / 5 sec;
- Bio resist cao;
- tăng infection/anomaly event risk.

Alien item phải khiến người chơi cân nhắc Power vs Humanity / Exposure.

---

# 26. Inventory Philosophy

Không track từng viên đạn trong MVP.

Lý do:

- tránh inventory micromanagement;
- focus vào team/weapon/consumable;
- heavy weapon có thể cân bằng bằng deployment cost / attack cycle / Noise thay vì bullet count.

Sau prototype có thể thêm special ammo như item modifier, nhưng không phải core loop ban đầu.

---

# 27. Deployment Cost

Mission có Supply Cost dựa trên:

- số unit;
- armor weight;
- heavy weapon;
- consumable;
- distance.

Prototype abstract unit:

```
Supply
```

Không dùng để ngăn chơi, chỉ tạo trade-off giữa squad 3 và squad 5.

---

# 28. Prototype Team Examples

## Balanced 3

```
Vanguard — Shotgun — Combat Armor
Assault  — Assault Rifle — Light Armor
Medic    — Pistol — Hazmat
```

Strength:

- chịu sai intel tốt;
- heal;
- mixed range.

Weakness:

- hack yếu;
- boss DPS trung bình.

## Tech 4

```
Vanguard — Shotgun
Assault  — Laser
Engineer — SMG + EMP
Medic    — Assault Rifle
```

Strong:

- robot;
- military depot;
- research lab.

Weak:

- swarm lớn nếu không mang AOE.

## Heavy 5

```
Vanguard — Shotgun
Assault  — Laser
Heavy    — Rocket Launcher
Engineer — EMP Rifle
Medic    — Assault Rifle
```

Strong:

- mixed encounters;
- AOE + single target;
- tech support.

Cost:

- supply cao;
- Noise cao;
- overkill với Small target.

---

# 29. Prototype Balance Targets

Room encounter bình thường, đúng tier:

### Balanced squad

- mất 5–20% tổng squad HP;
- ít phải dùng consumable ở Easy;
- Medium bắt đầu dùng item;
- Hard có khả năng mất unit nếu sai quyết định.

### Wrong-loadout squad

Không phải auto-lose.

Target:

- clear time +30–80%;
- consumable usage tăng;
- injury risk tăng;
- có thể phải partial-clear / extract.

### Specialized squad đúng matchup

- clear nhanh hơn balanced khoảng 15–35%;
- nhưng variance cao nếu encounter bất ngờ.

---

# 30. Những con số chưa khóa

Cần combat simulation để xác nhận:

- HP growth;
- exact role bonus;
- armor denominator 120;
- attack interval;
- crit;
- AOE falloff;
- consumable strength;
- revive penalty;
- resistance cap;
- item tier scaling.

**Các công thức này là testable baseline, không phải final balance.**

---

# 31. Next dependency

Để balance Units & Items đúng, bước kế tiếp phải là:

> **ENEMIES & RESISTANCES v0.1**

Cần ít nhất:

- 5 Infected;
- 4 Human/Raider;
- 4 Robot;
- 5 Alien;
- 3 Elite;
- 3 Boss;

và matrix resistance để kiểm tra Assault Rifle, Laser, Rocket, Fire, EMP có thật sự tạo lựa chọn khác nhau hay không.
