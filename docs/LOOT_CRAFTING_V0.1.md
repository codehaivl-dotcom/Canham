# BURROW ZERO — Loot, Crafting & Blueprint Economy v0.1

**Status:** Prototype baseline  
**Research influence:** extraction progression / base-useful loot / directed source clarity.  
**Rule:** Combat Simulation vẫn chưa thực hiện.

---

# 1. Loot Philosophy

Mỗi expedition phải có khả năng tạo tiến triển trên nhiều trục, không chỉ “drop được súng hiếm hay không”.

Một run có thể mang về:

- vật liệu xây Silo;
- vật liệu craft;
- gear;
- Blueprint Fragment;
- Research Data;
- Bestiary Sample;
- contract item;
- strategic material;
- survivor;
- world intel.

Mục tiêu:

> Một run không có Legendary vẫn có thể là một run có giá trị.

---

# 2. Loot Ownership

Loot nhặt trong mission ở trạng thái:

```
FIELD LOOT
```

Chỉ chuyển thành permanent inventory sau:

```
SUCCESSFUL EXTRACTION
```

Nếu squad failed extraction:

- normal field loot mất;
- equipped gear follows explicit escort/body/wipe rules in [SURVIVOR_RECOVERY_V0.1.md](SURVIVOR_RECOVERY_V0.1.md);
- mission-specific protected items chỉ tồn tại nếu rule nói rõ.

Điều này giữ extraction tension.

---

# 3. Loot Classes

## A. Common Materials

- Scrap
- Components
- Chemicals

## B. Survival / Logistics

- Food
- Water
- Supply components

## C. Equipment

- Weapon
- Armor
- Utility
- Consumable

## D. Knowledge

- Research Data
- Bestiary Sample
- Intel Cache
- Encryption Key

## E. Progression

- Blueprint Fragment
- Military Data
- Prototype Core
- Reactor Material
- Alien Material
- Combat Data

## F. Mission / Narrative

- key item;
- log;
- faction proof;
- signal component;
- rescue objective.

---

# 4. Field Cargo

Không dùng inventory kiểu Tetris ở MVP.

Prototype:

| Squad size | Base Cargo Units |
|---|---:|
| 1 (comeback) | 4 |
| 2 (comeback) | 8 |
| 3 | 12 |
| 4 | 16 |
| 5 | 20 |

Item load:

- small/common stack: 1;
- standard gear: 2;
- heavy weapon/large component: 3;
- mission key item: 0–1 tùy objective.

Cargo tạo decision:

> mang khẩu súng nặng về hay bỏ nó để lấy Components + Chemicals?

Không tính consumable đã mang vào mission vào cargo trừ loot mới. Body/DOWN2CU, rescued passenger1CU; one escort/living member. Fixed cargo cap at departure. Return overflow, first-clear atomicity and retry-safe settlement: MISSION_SESSION_REWARDS_V0.1.md.

---

# 5. Loot Affinity

Location tăng xác suất, không guarantee.

| Location | High | Medium | Rare chance |
|---|---|---|---|
| House | Food, Scrap | Medicine | Civilian cache / survivor |
| Warehouse | Scrap, Components | Tools | Prototype shipment |
| Hospital | Chemicals, Medicine | Research | Revival component |
| Military Depot | Weapon, Armor | Military Data | Blueprint |
| Research Lab | Research Data, Components | Chemicals | Prototype/Alien sample |
| Metro | Mixed salvage | Survivor/Intel | Hidden bunker |
| NPC Silo | Strategic mixed | Gear | Blueprint/Core |
| Alien Site | Alien Material | Research | Artifact |

---

# 6. Room Loot Budget

Prototype loot rolls:

| Difficulty | Normal room | High-value room |
|---|---:|---:|
| Easy | 1–2 rolls | 2–3 |
| Medium | 2–3 | 3–4 |
| Hard | 2–4 | 4–5 |
| Extreme | 3–5 | 5–7 |

Roll không đồng nghĩa item đơn lẻ; một roll có thể là material stack.

Deep room có quality multiplier nhưng cũng tăng encounter risk.

---

# 7. Rarity

Gear rarity:

- Civilian
- Industrial
- Military
- Advanced
- Prototype
- Alien
- Artifact

Rarity không được biến thành một Power Score tuyến tính.

Một Military weapon đúng matchup vẫn có thể tốt hơn Prototype weapon sai matchup.

---

# 8. Blueprint Progression

Blueprint mở quyền craft item family.

Prototype fragment requirement:

| Blueprint tier | Fragments |
|---|---:|
| Standard | 3 |
| Advanced | 5 |
| Prototype | 8 |
| Alien | 8 + Alien Research requirement |
| Artifact | 12 + unique progression item |

Blueprint Fragment phải có **source identity**.

Ví dụ:

```
GAUSS RIFLE BLUEPRINT
2 / 8

Likely sources:
- Military Research Facility
- War Machine A-17
- High-risk Military Depot
```

Không bắt player tra wiki để biết đi đâu.

---

# 9. Bad-Luck Protection

Boss/progression item không phụ thuộc hoàn toàn RNG.

Ví dụ War Machine A-17:

Guaranteed mỗi clear:

- 1 War Machine Data Fragment;
- 1 boss material roll.

Chance:

- bonus fragment;
- direct Prototype Capacitor;
- weapon/armor;
- rare full blueprint.

Nếu recipe cần 5 War Machine Data thì player chắc chắn tiến sau mỗi kill.

RNG quyết định **tốc độ tiến**, không quyết định **có được tiến hay không**.

---

# 10. First-Clear Reward

Mỗi named location / boss tier có first-clear bonus.

Ví dụ:

- Research Data;
- guaranteed blueprint fragment;
- permanent Bestiary progress;
- unique story item.

Mục tiêu:

- khuyến khích khám phá nhiều target;
- giảm farm một map tối ưu mãi.

---

# 11. Duplicate Gear

Gear duplicate có 4 lựa chọn:

- equip survivor khác;
- store;
- sell for Credits;
- salvage.

Salvage baseline:

| Tier | Material recovery |
|---|---:|
| Civilian | 30% recipe value |
| Industrial | 35% |
| Military | 40% |
| Advanced | 45% |
| Prototype | 50% + rare component chance |

Không salvage Artifact thành generic Scrap vô nghĩa; Artifact có unique research/salvage path.

---

# 12. Crafting Categories

Workshop craft:

- Supply;
- Consumable;
- Weapon;
- Armor;
- Utility;
- Repair component.

Prototype Forge:

- Prototype gear.

Xenobiology:

- Alien gear;
- biological utility.

---

# 13. Prototype Recipes

## 5 Supply

- Food 5
- Water 6
- Scrap 2
- 2 min

## Medkit

- Chemicals 4
- Scrap 1
- 2 min

## Frag Grenade

- Scrap 6
- Chemicals 2
- Components 1
- 3 min

## EMP Grenade

- Components 5
- Chemicals 2
- Scrap 2
- 4 min

## C-9 Civilian Pistol

- Scrap 18
- Components 4
- 5 min

## M-4 Service Rifle

Requires Standard weapon blueprint.

- Scrap 30
- Components 12
- 10 min

## Combat Armor

- Scrap 35
- Components 10
- Chemicals 4
- 12 min

## Revival Injector

Requires Clinic L2 + COM-04 Combat Triage research. Crafted at Clinic with one worker and a free treatment slot; same queue ownership and persistence rules as recovery, not a second free Workshop queue.

- Chemicals 12
- Components 4
- Research Data 2
- 8 min

Exact values cần economy test sau.

---

# 14. Repair

Không dùng permanent weapon destruction trong MVP.

Gear condition sau mission có thể giảm nhẹ nếu system này được bật.

Repair dùng:

- Scrap;
- Components;
- Workshop time.

Nếu durability tạo chore nhiều hơn decision thì bỏ hoàn toàn.

**Durability chưa khóa.**

---

# 15. Item Source Clarity

Tooltip luôn có Knowledge-based hint:

```
PROTOTYPE CAPACITOR

Known sources:
Military Research Facility   HIGH
War Machine-type enemy       HIGH
Military Depot               LOW
Unknown                      ?
```

Hint mạnh dần theo Bestiary/Research.

Đây là bài học trực tiếp từ extraction RPG: player cần biết hướng tìm mà không cần exact drop table.

---

# 16. Multi-Axis Run Progress

Post-run screen không chỉ hiện loot.

```
EXPEDITION RESULT

Recovered Loot       +...
Unit XP               +...
Bestiary              42% → 51%
Research Data         +8
Contract              2/3
Map Intel             +1 sector
Blueprint             3/8
```

Một chuyến đi có thể đáng giá dù không có rare gear.

---

# 17. Secure Data Case — EXPERIMENT

Bài học từ extraction game về giảm frustration.

Utility item:

**Secure Data Case**

- chiếm 1 Utility slot của squad;
- bảo vệ đúng **1 Data/Blueprint-class item** nếu failed extraction;
- không bảo vệ weapon;
- không bảo vệ armor;
- không bảo vệ strategic bulk material;
- charge bị tiêu hao khi kích hoạt.

Mục tiêu:

> đổi combat utility lấy insurance.

**Chưa khóa cho MVP.** Test sau Loot/Extraction prototype.

---

# 18. Anti-Grind Rules

- progression boss có guaranteed fragment;
- first-clear bonus;
- source hint rõ;
- nhiều location có overlapping source nhỏ;
- duplicate gear salvage được;
- contract không yêu cầu rare RNG item nếu không có pity;
- không ép cùng một dungeon 20 lần chỉ để mở main progression.

---

# 19. Success Criteria

Loot/Crafting đạt khi:

1. player luôn biết loot này dùng để làm gì;
2. location type gợi đúng hướng resource;
3. run thất bại sâu vẫn tạo bài học/knowledge;
4. extraction còn tension;
5. blueprint hiếm nhưng không RNG tuyệt vọng;
6. crafting nối trực tiếp expedition với Silo;
7. không có một currency mua được mọi thứ.
