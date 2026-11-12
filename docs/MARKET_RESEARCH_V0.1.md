# CĂN HẦM / ECHO SILO — Market & Competitor Research v0.1

**Date:** 2026-11-12  
**Status:** Research only — không thay đổi combat simulation/balance.  
**Purpose:** xác định game tương tự, khoảng trống thị trường và mechanic đáng học hỏi.

---

# 1. Executive conclusion

Không tìm thấy một game hiện tại ghép đúng toàn bộ tổ hợp của Căn Hầm:

- underground cutaway Silo management;
- named survivors có giá trị lâu dài;
- squad 3 → 4 → 5;
- Fallout-Shelter-like readable combat;
- preparation/formation/weapon matchup;
- imperfect intel;
- room-by-room expedition;
- extraction / retreat;
- Silo expansion phải clear hostile sector;
- boss/rare blueprint progression;
- contested resource site;
- mỗi player có một Silo;
- asynchronous PvP biến Silo defender thành dungeon.

Nhưng **từng mảng của concept đã có đối thủ mạnh**.

Các game cần theo dõi sát nhất:

1. Escape from Duckov;
2. Bunker Buster;
3. Last Fortress: Underground;
4. Zero City;
5. System Arrival;
6. Fallout Shelter;
7. AETHUS.

---

# 2. Escape from Duckov — game “duck” đáng học nhất

**Developer:** Team Soda  
**Publisher:** bilibili  
**Release:** 2025-10-16  
**Core:** PvE extraction survival RPG, top-down shooter, hideout/base building.

Sources:

- Steam: https://store.steampowered.com/app/3167020/Escape_From_DACCOF/
- PC Gamer: https://www.pcgamer.com/games/third-person-shooter/escape-from-duckov-might-look-like-a-parody-but-its-a-full-fledged-full-featured-singleplayer-bottling-of-extraction-shooter-juice/
- Steam Community reviews: https://steamcommunity.com/app/3167020/reviews/

## 2.1 Vì sao Duckov quan trọng với Căn Hầm

Không phải vì duck/shooter.

Nó chứng minh loop sau rất hấp dẫn:

```
PREPARE
→ LEAVE SAFE BASE
→ EXPLORE
→ FIGHT
→ LOOT
→ BECOME GREEDY
→ DECIDE CONTINUE / EXTRACT
→ RETURN
→ USE LOOT FOR PERMANENT PROGRESSION
→ UNLOCK DEEPER CONTENT
```

Đây gần như chính xác tension loop mà Căn Hầm đang hướng tới, chỉ khác combat model.

Steam mô tả:

- scavenge resources;
- build hideout;
- upgrade gear;
- five maps;
- changing loot;
- changing enemies;
- shifting weather;
- each raid có variation.

PC Gamer ghi nhận loot được dùng để:

- build base facilities;
- craft items;
- upgrade vendors;
- complete quests.

## 2.2 Điều đáng học số 1 — Greed curve

Một expedition hay phải liên tục đặt câu hỏi:

> “Đồ tôi đã kiếm được có đủ để rút chưa?”

Căn Hầm đã có Partial Clear/Extraction. Duckov củng cố rằng đây phải là **core emotion**, không phải nút phụ.

Trong Căn Hầm:

```
Room 1–3
Safe / expected loot

Room 4–6
Better loot / higher attrition

Room 7+
Rare / Boss / hidden room
but squad condition worsening
```

Player tự tạo tension bằng lòng tham.

## 2.3 Điều đáng học số 2 — Layered progression

Community reviews thường khen nhiều lớp progression:

- character;
- gear;
- base;
- NPC;
- map;
- crafting;
- quests;
- exploration.

Căn Hầm cũng nên tránh một progression bar duy nhất.

Một expedition có thể tiến cùng lúc:

- Unit XP;
- gear;
- Silo materials;
- Research Data;
- Bestiary;
- quest/contract;
- blueprint;
- world-map intel.

Ngay cả không ra rare gun, run vẫn nên có vài loại tiến bộ.

## 2.4 Điều đáng học số 3 — Quest dẫn người chơi tới hệ thống

PC Gamer đánh giá quest của Duckov tạo directed progression: quest dần đưa player tới vùng mới, crafting/vendor economy mới.

Áp dụng:

Không nên tutorial bằng 20 popup.

Contract/quest tự dẫn:

```
Need medicine
→ Hospital

Need Components
→ Warehouse

Need Military Data
→ Military Depot

Need strange sample
→ Research Lab / Alien Site
```

Quest là lý do để học location archetype.

## 2.5 Điều đáng học số 4 — Fixed identity + variable run

Duckov có map rõ nhưng loot/enemy/weather biến đổi.

Điều này rất gần nguyên tắc ta đã khóa:

```
LOCATION ARCHETYPE
+
VARIABLE THREAT
+
VARIABLE HAZARD
+
VARIABLE LOOT
+
RARE EVENT
```

Không procedural vô nghĩa.

Hospital vẫn là Hospital.

Nhưng player không biết chính xác Hospital hôm nay chứa gì.

## 2.6 Điều đáng học số 5 — Accessibility

Duckov có multiple difficulty presets và custom difficulty.

Extraction không nhất thiết chỉ dành cho hardcore audience.

Căn Hầm cũng nên giữ:

- Easy vẫn có death/revive rules;
- nhưng Intel tốt hơn;
- lower encounter budget;
- extraction dễ hơn;
- player có thời gian học.

Không làm “hardcore” bằng cách che mọi thông tin và giết player vô lý.

## 2.7 Safety valve đáng cân nhắc

PC Gamer mô tả companion có khả năng bảo vệ một item khi player chết.

Không copy trực tiếp.

Candidate cho Căn Hầm:

### Secure Data Case / Black Box — CHƯA KHÓA

- utility item;
- chiếm 1 slot;
- bảo vệ **1 data/blueprint-class item** khi squad failed extraction;
- không bảo vệ weapon/armor/full loot;
- có thể mất charge.

Điều này cho player một lựa chọn:

> thêm combat utility hay bảo hiểm một món quan trọng?

Chưa đưa vào core design cho tới khi Loot/Crafting được làm.

## 2.8 Điều KHÔNG nên học từ Duckov

Community feedback chỉ ra:

- grind cuối game;
- RNG khó chịu khi cần đúng một item;
- một số item description chưa rõ;
- late-game repetition.

Vì vậy Căn Hầm cần:

### Bad-luck protection

Rare progression recipe không phụ thuộc hoàn toàn RNG.

Ví dụ Boss:

- random loot;
- **guaranteed token/fragment progress**.

### Source clarity

Bestiary/Intel phải nói:

```
LIKELY SOURCE:
Military Depot
War Machine A-17
Contested Salvage Site
```

Không bắt player tra wiki để biết item nằm đâu.

### Content rotation

Một target archetype cần nhiều:

- threat packages;
- route variants;
- objectives;
- rare events.

---

# 3. Bunker Buster — competitor structural gần nhất

**Release:** 2026-07-17 Early Access  
Steam: https://store.steampowered.com/app/4876950/Bunker_Buster/

Store description hiện có:

- self-sufficient bunker;
- power;
- life support;
- weapon/defense/cyber systems;
- enemy factions;
- capturable technology;
- research;
- multiplayer;
- fortress raiding;
- PvP quickmatch.

Đây là game cần monitor thường xuyên vì feature list chạm rất gần phần:

```
BUNKER
+
POWER / LIFE SUPPORT
+
TECH
+
RAID
+
PVP
```

## 3.1 Điểm Căn Hầm phải khác rõ

Không cạnh tranh bằng “bunker có nhiều phòng hơn”.

Signature khác biệt của ta phải là:

### A. Expedition squad là trung tâm

Bunker Buster tập trung fortress/weapon systems.

Căn Hầm tập trung **những con người cụ thể** đi vào unknown location.

### B. Named survivor attachment

Player phải nhớ:

> “Minh là Engineer tôi đã nuôi 30 giờ.”

Death có cảm xúc.

### C. Imperfect Intel

Trước raid không có full information.

### D. Room-by-room dungeon expedition

House/Hospital/Lab/Metro/Silo có route và retreat.

### E. Silo expansion is exploration

Đào được sector không đồng nghĩa sở hữu sector.

### F. PvP Silo = hidden-layout dungeon

Không phải chỉ fire missiles / compare fortress stats.

### G. Resource-site conflict

PvP có nguyên nhân kinh tế trên World Map.

Đây phải là differentiation moat.

---

# 4. Last Fortress: Underground

App Store:
https://apps.apple.com/us/app/last-fortress-underground/id1540557475

Google Play:
https://play.google.com/store/apps/details?id=com.more.lastfortress.gp

Có:

- underground fortress building;
- facilities;
- survivor jobs;
- heroes;
- team composition/synergy;
- wilderness resource scavenging;
- camps/resource points;
- alliance;
- competitive multiplayer/4X.

## Học

### Survivor skill ↔ Silo job

Engineer/Doctor/Scientist không chỉ là combat class.

Unit stats/traits có thể tác động:

- room production;
- research;
- Clinic;
- Scout;
- crafting.

Điều này làm unit có giá trị ngay cả khi không expedition.

### World progression

Base không tồn tại tách khỏi world.

Resource/camp/alliance kéo player ra ngoài.

## Không nên học

Căn Hầm không nên trôi thành:

- hero collection;
- generic power number;
- alliance war là gameplay chính;
- timer acceleration;
- whale snowball;
- early-game shelter chỉ là skin của 4X.

PvP của Căn Hầm phải giữ squad/room gameplay.

---

# 5. Zero City

App Store:
https://apps.apple.com/us/app/zero-city-zombie-shelter-game/id1463289293

Có:

- shelter rooms;
- dwellers;
- skills;
- weapon/equipment;
- PvP arena;
- attacks on other shelters;
- campaign.

Đây là proof rằng:

```
Fallout-Shelter-like base
+
equipped squad
+
PvP
```

đã tồn tại trên mobile.

## Differentiation bắt buộc

Nếu Căn Hầm chỉ là:

> Fallout Shelter + better gear + PvP

thì không đủ.

Ta phải giữ:

- dungeon topology;
- imperfect Intel;
- target selection;
- extraction;
- resource sites;
- boss/material progression;
- Silo clear/expansion;
- 3→5 formation;
- base-as-dungeon PvP.

---

# 6. System Arrival

Steam:
https://store.steampowered.com/app/5019800/System_Arrival/

Description hiện tại:

- top-down survival action RPG;
- solo / up to 4-player online co-op;
- ruined-world expeditions;
- bring supplies to underground bunker;
- build bunker;
- survivor management;
- equipment/base improvement.

Nó gần phần:

```
EXPEDITION
→ SUPPLIES
→ BUNKER
→ EXPEDITION
```

Nhưng combat/action và co-op direction khác ta.

## Học

Player phải luôn thấy loot ngoài world có tác động cụ thể về home base.

Mỗi run nên tạo câu:

> “Tôi mang món này về để xây/nâng cái gì?”

---

# 7. Fallout Shelter

Official:
https://fallout.bethesda.net/en/games/fallout-shelter

Vẫn là reference UX quan trọng cho:

- cutaway shelter;
- room readability;
- resident visibility;
- low-input combat;
- fast base comprehension.

Bethesda hiện vẫn phát triển Seasons/time-limited vaults, cho thấy framework shelter vẫn có thể hỗ trợ live content.

## Ta học

- readability;
- immediate room identity;
- nhân vật dễ nhìn;
- simple input.

## Ta không copy

- SPECIAL;
- Vault-Tec expression;
- art/UI;
- room design;
- quest structure cụ thể.

Mechanic inspiration phải được chuyển thành original systems.

---

# 8. AETHUS

Steam:
https://store.steampowered.com/app/2541530/

Release 2026.

Có:

- sci-fi survival;
- resource gathering;
- modular outpost;
- crafting;
- hydroponics;
- exploration;
- narrative reason to dig deeper.

Không phải competitor trực tiếp, nhưng có lesson tốt:

> progression cần cho player lý do để đi sâu hơn, không chỉ “ore tier cao hơn”.

Căn Hầm nên gắn depth/world progression với mystery/story signal.

---

# 9. Watchlist

## Defense in Depth

Pre-release bunker survival colony sim.

https://docs.axiomancer.io/silo

Theo dõi:

- scarcity;
- bunker systems;
- survivor simulation.

Chưa có public playable build tại thời điểm research.

## Minerva Rising

Một underground city-builder mới được báo chí nhắc tới trong 2026.

Theo dõi:

- multi-level underground settlement;
- citizen trust/rebellion;
- procedural scarcity.

Không coi là reference chính cho tới khi có official/public build rõ hơn.

---

# 10. Competitive Matrix

| Game | Underground base | Named units | Expedition loot | Extraction risk | PvP raid | Resource conflict | Imperfect Intel |
|---|---|---|---|---|---|---|---|
| Fallout Shelter | ++ | ++ | + | - | - | - | - |
| Last Fortress | ++ | ++ | + | - | ++ | ++ | - |
| Zero City | ++ | ++ | + | - | ++ | - | - |
| Duckov | + hideout | single char | +++ | +++ | - | - | ++ |
| Bunker Buster | +++ | ? | +/tech capture | + | +++ | + | + |
| System Arrival | ++ | ++ | +++ | + | - | - | + |
| Căn Hầm target | +++ | +++ | +++ | +++ | +++ | +++ | +++ |

Đây không phải điểm review; chỉ là feature-fit matrix.

---

# 11. Market gap / positioning

Không nên pitch:

> “Fallout Shelter nâng cấp.”

Pitch nội bộ tốt để giải thích inspiration, nhưng public positioning cần độc lập.

Đề xuất:

> **A persistent underground survival strategy game where every expedition risks the survivors you raised, and every Silo can become a dungeon for another player to infiltrate.**

Các signature pillar public-facing:

1. **Your Silo is your home — and your dungeon.**
2. **Every expedition is a gamble.**
3. **You never know everything before entering.**
4. **Weapons solve situations, not power numbers.**
5. **Survivors live long enough for death to matter.**
6. **Rare resources create real territorial conflict.**

---

# 12. Product lessons to add to backlog

## LOCK / HIGH CONFIDENCE

### Extraction greed curve

Đã có trong GDD; research củng cố mạnh.

### Multi-axis progression

Run nên reward nhiều trục, không chỉ item RNG.

### Quest as guided systems onboarding

Contracts dẫn player qua location/economy.

### Fixed map identity + variable encounter

Giữ.

### Bad-luck protection cho progression item

Nên thêm khi thiết kế Loot/Crafting.

### Clear source hints

Bestiary/Research/UI phải chỉ player biết **nhóm nơi** nên tìm.

## EXPERIMENT — NOT LOCKED

### Secure Data Case / Black Box

Một utility có thể bảo vệ 1 data/blueprint item khi failed extraction.

Cần test vì có thể làm giảm tension nếu quá mạnh.

---

# 13. Main strategic warning

Hiện đối thủ đáng lo nhất không phải Fallout Shelter.

**Bunker Buster đã chạm bunker + life support + research + raiding + PvP.**

**Duckov đã chứng minh extraction + base progression + loot greed rất hấp dẫn.**

Vì vậy Căn Hầm phải giữ phần giao nhau độc đáo:

```
FALLOUT-SHELTER READABILITY
+
DUCKOV-LIKE EXTRACTION TENSION
+
SMALL NAMED SQUAD
+
IMPERFECT INTEL
+
DUNGEON-LIKE LOCATIONS
+
BASE-AS-PVP-DUNGEON
+
CONTESTED RESOURCE WORLD
```

Nếu bỏ bất kỳ 2–3 trụ cuối, game sẽ dễ rơi vào vùng đã có đối thủ mạnh.

---

# 14. Research status

Research này không thay thế market study đầy đủ.

Trước public announcement cần:

- Steam competitive tag scrape;
- App Store / Google Play monetization study;
- review mining;
- retention/live-ops analysis;
- price/IAP positioning;
- trademark/name clearance.

Combat Simulation vẫn **NOT STARTED** theo yêu cầu chủ dự án.
