# BURROW ZERO — Population, Jobs, Traits & Perks v0.1

**Status:** Prototype baseline  
**Goal:** survivor phải có giá trị cả trong Silo lẫn expedition.

---

# 1. Population Philosophy

Survivor không phải “hero card”.

Mỗi người có:

- tên;
- level;
- 8 stats;
- profession affinity;
- combat role;
- 1–2 traits;
- gear;
- condition;
- work assignment;
- history;
- optional relationship tags.

Không dùng rarity màu để quyết định toàn bộ giá trị con người.

---

# 2. Population Cap

```
Population Cap = Total Beds
```

Temporary rescue overflow:

- grace period 2 real hours;
- sau đó Morale giảm nếu chưa có đủ bed.

Không xóa survivor tự động.

---

# 3. Recruitment Sources

## Rescue

Nguồn chính đầu game.

- House;
- Hospital;
- Metro;
- NPC event.

## Radio Applicant

Radio L2+.

- xuất hiện candidate định kỳ;
- player xem basic info trước khi nhận;
- không phải gacha trả tiền.

## Faction / Contract

Mid-game.

Một số survivor join vì reputation/story.

## Birth / Family

Không cần trong MVP.

Có thể thêm sau nếu simulation dân số cần long-term organic growth.

---

# 4. Starting Population

Prototype:

6 survivor.

Composition đảm bảo tutorial không soft-lock:

- 1 Tech-oriented;
- 1 Medical-oriented;
- 1 Combat-oriented;
- 1 Perception-oriented;
- 2 generalists.

Không random hoàn toàn starting roster.

---

# 5. Job Efficiency

Mỗi room có 1–2 Relevant Stats.

Prototype:

```
Base Worker Efficiency =
0.85 + RelevantStat × 0.03
```

Stat 5 → 1.00×  
Stat 8 → 1.09×

Sau đó:

```
Final Efficiency =
Base
× Morale Modifier
× Trait Modifier
× Room/Tech Modifier
```

Soft cap prototype:

```
0.65× – 1.35×
```

Không để một survivor giỏi tạo production gấp 3 lần.

---

# 6. Room Stat Affinity

| Room | Primary | Secondary |
|---|---|---|
| Generator | TEC | END |
| Water | TEC | INT |
| Hydroponics | INT | END |
| Workshop | TEC | COM |
| Clinic | MED | INT |
| Research | INT | TEC |
| Radio/Scout | PER | INT |
| Security | COM | PER |
| Training | COM | INT |
| Recycler | END | TEC |

Player bắt đầu học con người qua công việc, không chỉ combat.

---

# 7. Profession Affinity

Profession không khóa role.

Examples:

- Engineer;
- Doctor;
- Researcher;
- Soldier;
- Mechanic;
- Scout;
- Farmer;
- Technician;
- Security;
- Civilian Generalist.

Profession bonus nhỏ, khoảng:

```
+5% room efficiency
```

khi làm đúng nhóm nghề.

Combat role được train riêng.

---

# 8. Morale

Scale:

```
0–100
```

Starting neutral:

```
60
```

Bands:

| Morale | Effect |
|---|---|
| 80–100 | +5% work efficiency, +5% Resolve check |
| 50–79 | neutral |
| 30–49 | -5% work efficiency |
| 10–29 | -15% work, slower recovery |
| 0–9 | crisis/event risk |

Morale không được tụt vì player offline vài giờ bình thường.

---

# 9. Morale Sources

Positive:

- Food/Water stable;
- successful expedition;
- rescue;
- comfortable housing;
- recreation later;
- relationship event;
- faction/story success.

Negative:

- hunger/dehydration;
- overcrowding;
- death of known survivor;
- repeated failed expedition;
- contaminated room;
- injury;
- internal conflict.

---

# 10. Fatigue

Expedition tạo Fatigue.

Prototype:

- short mission: +10;
- medium: +20;
- long/hard: +30–40.

Scale 0–100.

At >60:

- -5% attack speed;
- -5% work efficiency.

At >80:

- -10% combat efficiency;
- cannot immediately redeploy unless Emergency.

Rest:

- Living / Recreation;
- Clinic if injured.

Không dùng fatigue để ép wait quá lâu; mục tiêu là rotate roster.

---

# 11. Death Impact

Permanent death phải có social impact.

Prototype:

- toàn Silo: -3 Morale temporary;
- same expedition squad survivors: -8;
- Bonded survivor: additional -10.

Penalty decay theo thời gian / positive event.

Không để một death tạo death spiral không cứu được.

---

# 12. Trait Structure

Trait có 3 loại:

- Positive;
- Negative;
- Mixed.

Một survivor bình thường:

- 1 trait;
- rare history survivor có thể 2;
- maximum 3 active natural traits.

Không roll 8 affix nhỏ.

---

# 13. Positive Traits

## Field Medic
+20% Medkit effect.

## Calm
+15% Fear resistance.

## Mechanic
+8% Workshop/Generator efficiency.

## Keen Eye
+8% detection / Scout contribution.

## Tough
+8% Max HP.

## Fast Learner
+10% XP.

## Scavenger
+10% chance tìm extra common loot roll.

## Steady Hands
+5% weapon accuracy.

## Team Player
+3 Morale cho squad sau successful extraction.

## Night Owl
+8% efficiency trong night-cycle event nếu system bật.

---

# 14. Negative Traits

## Claustrophobic
-8 Morale khi ở Silo quá lâu; +3 Morale sau expedition.

## Reckless
+5% damage; +10% damage received.

## Fragile
-8% Max HP.

## Slow Recovery
Clinic time +20%.

## Nervous
Fear/psychic resistance -15%.

## Hoarder
+1 Cargo Unit personal contribution; Storage work -5%.

## Short Temper
internal conflict event chance tăng.

## Tech Illiterate
TEC interaction -15%.

---

# 15. Mixed Traits

## Paranoid
+15% Mimic/anomaly detection;
-5 Morale khi overcrowded.

## Alien Touched
+10% Alien gear efficiency;
Alien Exposure +20%.

## Veteran
+5% damage/accuracy;
death of squadmate Morale impact +50%.

## Survivor
below 30% HP: +10% damage resistance;
Clinic recovery +15% time.

## Adrenaline Junkie
Hard/Extreme mission +8% attack speed;
Easy mission -5 Morale reward.

## Pacifist
Human enemy damage -10%;
Medical/Negotiation event bonus.

---

# 16. Combat Perk Milestones

Perks không random hoàn toàn.

Prototype perk choice ở:

- Level 10;
- Level 20;
- Level 30;
- Level 40.

Level 50 có mastery later.

---

# 17. Role Perk Examples

## Vanguard

- Hold Line: +15% aggro, +5% damage reduction while Front.
- Last Wall: once/room survive lethal hit at 1 HP.
- Shock Guard: stagger attacker after shield break.

## Assault

- Focus Fire: +8% damage to target hit by another squadmate.
- Quick Reload: attack interval -6%.
- Finisher: +15% damage to enemy below 25% HP.

## Scout

- First Read: reveal one enemy resistance hint at room start.
- Pathfinder: Travel event risk -10%.
- Weak Point: +8% crit vs Observed/Analyzed enemy.

## Engineer

- Remote Override: one turret/device interaction faster.
- EMP Expert: EMP duration +15%.
- Field Repair: once/room restore small shield/robot utility.

## Medic

- Combat Triage: Medkit use time -25%.
- Stable Revival: revived unit Trauma penalty reduced.
- Preventive Dose: squad Bio resistance +8%.

## Heavy/Specialist

- Blast Control: AOE secondary damage +10%.
- Suppression: heavy hit reduces enemy accuracy briefly.
- Load Bearer: heavy weapon Supply penalty -1.

---

# 18. Relationships — LIGHTWEIGHT MVP

Không làm life-sim sâu ngay.

MVP chỉ cần tags:

- Bonded;
- Rival;
- Mentor;
- Family/Partner later.

Bond có thể sinh sau nhiều mission cùng nhau.

Effects nhỏ:

- Bonded pair: +3 Resolve khi cùng squad;
- death/injury impact lớn hơn;
- occasional event.

Không cho relationship trở thành mandatory min-max.

---

# 19. Survivor History

History log:

- missions survived;
- bosses killed;
- times revived;
- injuries;
- discoveries;
- PvP raids;
- rescued allies.

History chủ yếu tạo attachment.

Một số milestone có thể mở title/cosmetic/perk nhẹ.

---

# 20. Roster Rotation

Mục tiêu của Fatigue/Injury/Jobs:

> player nuôi 15–30 survivor đa dạng thay vì chỉ 5 người mạnh nhất.

Không dùng hard lock.

Player vẫn có thể dùng “đội ruột”, nhưng sẽ có lý do phát triển đội B/C.

---

# 21. Success Criteria

Population system đạt khi:

1. player nhớ tên một số survivor;
2. survivor hữu ích cả ở base và expedition;
3. death có cảm xúc nhưng không phá account;
4. roster lớn có lý do tồn tại;
5. không biến thành hero-gacha;
6. trait tạo câu chuyện và trade-off, không chỉ +2% stat.
