# CĂN HẦM / ECHO SILO — Reward Reveal, Cache & Survivor Signal v0.1

**Status:** Direction lock + prototype baseline  
**Purpose:** tạo cảm giác mở thưởng mạnh như Fallout Shelter nhưng không biến game thành hero-gacha hoặc paid RNG.

---

# 1. Core Rule

Game có **card-style reward reveal**.

Nhưng hệ thống này là:

> **reward presentation + discovery**

không phải:

> **pay-to-win gacha progression**.

Đã khóa:

- có lật thẻ / decrypt / reveal reward;
- item có rarity presentation;
- cache gắn với fiction/location;
- survivor không dùng rarity kiểu Common/Rare/Epic/Legendary;
- không bán exclusive combat survivor qua paid RNG;
- không khóa progression bắt buộc sau loot box;
- mọi item quan trọng phải có gameplay source khác.

---

# 2. PvE First Principle

PvE phải tự đứng vững như một game hoàn chỉnh.

Player không chơi PvP vẫn có thể tiến rất sâu qua:

- Silo expansion;
- exploration;
- contracts;
- bosses;
- crafting;
- Bestiary;
- blueprint;
- survivor rescue;
- resource sites PvE;
- story/faction;
- seasonal PvE content.

PvP là lớp đối kháng / economy pressure / prestige.

PvP không phải hệ thống dùng để cứu một PvE thiếu content.

---

# 3. Cache Families

## Supply Cache

Nguồn:

- objectives;
- normal PvE;
- House/Warehouse;
- contracts.

Typical:

- common materials;
- Supply;
- consumables;
- Credits;
- low/mid gear.

Không có survivor.

## Medical Cache

Nguồn:

- Hospital;
- Clinic contract;
- Bio mission.

Typical:

- Chemicals;
- Medkit;
- Antidote;
- Rad Injector;
- medical component;
- Revival component rare.

Không có survivor.

## Military Cache

Nguồn:

- Military Depot;
- military boss;
- NPC Silo;
- high-risk contract.

Typical:

- weapon;
- armor;
- Components;
- Military Data;
- Blueprint Fragment;
- rare Prototype component.

Không có survivor.

## Research Cache

Nguồn:

- Research Lab;
- Data Center;
- faction science mission.

Typical:

- Research Data;
- electronics;
- blueprint;
- Bestiary sample;
- encrypted data.

## Alien Container

Nguồn:

- Alien Crash;
- Alien Nest;
- anomaly;
- alien boss.

Typical:

- Alien Material;
- Unknown Data;
- alien utility;
- artifact fragment.

Có Alien Exposure / anomaly fiction.

## Encrypted Combat Cache

Nguồn:

- NPC Silo challenge;
- PvP;
- defense contract.

Typical:

- Combat Data;
- weapon/armor;
- military/prototype material.

Không chứa exclusive paid-only power.

---

# 4. Reward Reveal Flow

Example:

```
RECOVERED MILITARY CACHE

[ ? ] [ ? ] [ ? ] [ ? ] [ ? ]

TAP TO DECRYPT
```

Reveal:

```
SCRAP ×45

MEDKIT ×2

MILITARY DATA ×3

M-4 SERVICE RIFLE

GAUSS BLUEPRINT FRAGMENT
1 / 8
```

Reveal có thể:

- tap từng card;
- reveal all;
- auto-skip sau khi player đã quen.

Animation không được làm player chờ lâu bắt buộc.

---

# 5. Cache Quality

Cache không phải một loot box vô danh từ menu.

Mỗi cache có context:

```
MILITARY CACHE

Origin:
Site M-17

Integrity:
83%

Security:
Encrypted

Quality:
MILITARY
```

Loot pool phụ thuộc:

- source location;
- difficulty;
- objective;
- boss/elite;
- first clear;
- cache integrity/quality.

Player hiểu **vì sao box này có loại đồ này**.

---

# 6. Reward Slot Contract

Prototype 5-card cache.

Normal cache:

- 1 guaranteed material;
- 1 guaranteed consumable/utility;
- 1 currency/data slot;
- 1 gear/material flex slot;
- 1 rare flex slot.

High-tier cache có thể có 6–7 cards.

Không cho kết quả kiểu:

> 5 card đều là 10 Scrap.

Mỗi cache phải có tối thiểu một reward có perceived value cao hơn common filler.

---

# 7. Rarity Presentation

Item rarity visual:

- Civilian — neutral/white;
- Industrial — blue;
- Military — purple;
- Advanced — violet/deep blue;
- Prototype — orange;
- Alien — cyan/iridescent;
- Artifact — red-gold / unique treatment.

Exact UI colors sẽ khóa trong Art Direction.

**Survivor không dùng rarity color.**

Không có:

- SSR human;
- Legendary human;
- 5-star human.

Con người được đánh giá bằng:

- stats;
- profession;
- traits;
- history;
- role;
- condition.

---

# 8. Survivor Acquisition Uses Fiction, Not Loot Boxes

Survivor đến từ:

- rescue;
- distress signal;
- radio applicant;
- faction/story;
- Cryo Chamber;
- abandoned Silo;
- world event.

Không trộn survivor vào Supply/Military cache.

---

# 9. Distress Signal Reveal

Example:

```
DISTRESS SIGNAL

3 LIFE SIGNS IDENTIFIED

[ Minh Tran ]
Engineer
TEC 8
Trait: Paranoid

[ Eva Morel ]
Medic
MED 7
Trait: Calm

[ Owen Hale ]
Scout
PER 8
Trait: Reckless

Choose rescue priority:
[ MINH ]
[ EVA ]
[ OWEN ]
```

Player có agency.

Không phải blind random summon.

Một số event chỉ có 1 survivor; một số event cho lựa chọn.

---

# 10. Cryo Pod Reveal

Rare Silo/deep facility discovery:

```
CRYO CHAMBER
3 PODS ACTIVE
```

Sau clear/restore:

```
POD 02 OPENED

Dr. Elina Voss
Researcher

INT 9
TEC 7

Trait:
Old World Scientist
```

Giá trị đến từ:

- nơi tìm thấy;
- lịch sử;
- trait/stat;
- story.

Không từ rarity label.

---

# 11. Survivor Selection Balance

Khi event cho 3 survivor:

- không có một candidate objectively vượt xa toàn bộ;
- mỗi người mạnh theo hướng khác;
- trait có trade-off;
- player chọn theo nhu cầu Silo/squad.

Ví dụ:

Engineer mạnh base.

Medic cứu expedition.

Scout cải thiện intel.

Đây là **choice reward**, không phải gacha rarity.

---

# 12. Cache Sources

Cache chủ yếu kiếm bằng gameplay:

- Objective;
- Contract;
- First Clear;
- Boss;
- Hidden Room;
- Sector restoration;
- Faction reputation;
- PvP system reward;
- Seasonal PvE.

Nếu monetization sau này dùng cache:

- không chứa exclusive power;
- không chứa exclusive survivor;
- không bypass boss/PvP/contested progression;
- odds phải minh bạch nếu luật/platform yêu cầu;
- cosmetic cache nên tách khỏi gameplay cache.

Core design không phụ thuộc paid cache.

---

# 13. Direct Drop Still Exists

Cache không thay thế loot ngoài world.

Player vẫn có thể:

- nhặt weapon trực tiếp;
- loot medicine;
- lấy material;
- tìm blueprint fragment;
- craft item;
- nhận contract reward.

Ví dụ cùng M-4 Service Rifle có thể đến từ:

- direct loot;
- Military Cache;
- crafting;
- contract.

Không có item core nào chỉ có một đường RNG duy nhất.

---

# 14. Cache and Extraction

Cache tìm trong dungeon là **Field Loot** cho tới khi extract.

Nếu failed extraction:

- cache mất như field loot bình thường;
- trừ khi một special mechanic bảo vệ nó.

Điều này làm cache trong tay tạo greed tension:

> “Mình vừa nhặt Military Cache. Có đi boss nữa không?”

---

# 15. Secure Data Case Interaction — EXPERIMENT

Nếu system này được test:

- bảo vệ 1 Blueprint/Data item;
- không bảo vệ unopened Military Cache;
- không bảo vệ full gear;
- chiếm utility slot.

Không làm cache trở thành loot không thể mất.

---

# 16. Post-Run Reward Rhythm

Một expedition tốt có rhythm:

```
RETURN TO SILO
↓
SHOW SURVIVORS / INJURIES
↓
SHOW RAW LOOT
↓
OPEN SPECIAL CACHE
↓
BLUEPRINT / BESTIARY / CONTRACT PROGRESS
↓
CHOOSE NEXT ACTION
```

Cache reveal là climax nhỏ của reward phase.

Không che mất consequence như injury/death.

---

# 17. PvE Reward Coverage

PvE reward pool phải đủ rộng để player không cần PvP cho basic enjoyment:

PvE có thể cấp:

- all survival resources;
- all common/advanced construction materials;
- most standard/military gear;
- most consumables;
- Research Data;
- many blueprints;
- survivor;
- boss-exclusive items;
- Alien progression.

PvP có:

- Combat Data;
- PvP-specific cosmetic/prestige;
- some alternate blueprint/progression sources;
- contested efficiency advantage.

Không khóa toàn bộ endgame power sau bắt buộc PvP.

---

# 18. PvP Reward Philosophy

PvP nên cho:

- prestige;
- Combat Data;
- Encrypted Combat Cache;
- ranking/season;
- resource efficiency;
- alternate progression.

Không nên:

- có một “best weapon” chỉ PvP player mới có;
- cho attacker cướp unique survivor;
- xóa progression defender.

---

# 19. Anti-Gacha Rules

Locked:

1. Không hero rarity.
2. Không paid random exclusive survivor.
3. Không duplicate survivor shard system.
4. Không cần pull 5 bản cùng một survivor để upgrade.
5. Không paid cache là nguồn duy nhất của blueprint/weapon.
6. Không progression chính dựa vào random box.
7. Reward reveal phải gắn với gameplay fiction.
8. Randomness tạo excitement, không tạo paywall.

---

# 20. Success Criteria

System thành công khi:

1. mở cache tạo cảm giác mong chờ;
2. player biết cache đến từ đâu;
3. rarity item dễ đọc;
4. survivor vẫn cảm giác là con người;
5. PvE có reward loop đủ mạnh;
6. cache làm extraction tension tăng;
7. player không cảm thấy đang chơi hero-gacha;
8. gameplay source luôn quan trọng hơn shop.
