# BURROW ZERO — Game Vision / GDD v0.3

**Trạng thái:** Concept / Pre-production  
**Tên game:** BURROW ZERO  
**Slogan:** *Deep Below. Far Beyond.*  
**Ngôn ngữ đầu tiên:** Tiếng Việt + English  
**Art direction:** Panda survivors, simple AI-first low-poly 3D  
**Mục tiêu tài liệu:** khóa hướng game trước khi prototype để tránh biến dự án thành bản sao đơn giản của Fallout Shelter hoặc Clash of Clans.

---

# 0. Brand lock

- **Game:** BURROW ZERO
- **Slogan:** Deep Below. Far Beyond.
- **Initial languages:** Vietnamese + English.
- **Primary survivor visual:** panda mascot.
- **Production art:** simple low-poly 3D, primitive-friendly, one shared survivor rig.
- **Localization:** no production UI text baked into textures or concept art.

Canonical brand/localization spec: [BRAND_LOCALIZATION_V0.1.md](./BRAND_LOCALIZATION_V0.1.md)

---

# 1. High concept

Trong tương lai, nhân loại phải đối mặt với nhiều mối đe dọa ngoài Trái Đất: sinh vật lạ, bào tử biến đổi sinh học, công nghệ không rõ nguồn gốc, nhiễu điện từ và những cấu trúc xuất hiện trên bề mặt.

Thảm họa không diễn ra trong một ngày. Trong nhiều năm, các quốc gia, tập đoàn và tổ chức quân sự xây dựng hàng nghìn dự án trú ẩn sâu dưới lòng đất.

Mỗi người chơi là người điều hành **một Silo sinh tồn độc lập**.

Ban đầu người chơi chỉ biết cách sống sót trong hầm. Sau đó họ bắt đầu mở lại liên lạc, đi thám hiểm, tìm thấy các Silo khác, các faction, dấu tích chính phủ cũ và cuối cùng là những người chơi thật.

Game bắt đầu như một survival management game và dần mở thành một persistent world có PvE, Boss, PvP, Alliance và tranh giành công nghệ.

---

# 2. North Star

> Xây một Silo mà người chơi thực sự có cảm giác sở hữu; nuôi một đội survivor mà họ sợ mất; rồi buộc họ phải bước ra khỏi nơi an toàn để tranh giành những thứ không thể tự sản xuất.

Game phải tạo được ba cảm xúc chính:

1. **Sở hữu:** “Đây là căn hầm của tôi.”
2. **Gắn bó:** “Đây là squad của tôi, tôi không muốn họ chết.”
3. **Tham vọng:** “Muốn mạnh hơn tôi phải mạo hiểm ra ngoài.”

---

# 3. Design pillars

## 3.1 Silo là home base thật sự

Silo không chỉ là một cây công nghệ.

Người chơi xây phòng, bố trí dân cư, điện, nước, thực phẩm, workshop, phòng nghiên cứu, bệnh xá, kho, defense, command center và các tầng đặc biệt.

Layout của Silo về sau cũng chính là layout defense khi bị raid.

## 3.2 Unit có giá trị cá nhân

Mỗi survivor là một unit có:

- tên;
- level;
- profession;
- stats;
- traits;
- weapon;
- armor;
- accessory;
- consumables;
- injury;
- morale;
- relation;
- combat history.

Người chơi phải nhớ được unit của mình chứ không nhìn họ như một con số.

## 3.3 Exploration phải là gameplay, không phải timer

Không dùng mô hình chính là:

> gửi unit đi → chờ 4 giờ → nhận đồ.

Người chơi phải có khả năng điều khiển hoặc ra quyết định trong expedition.

Các khu vực được chia thành room / building / sector. Người chơi chọn đường đi, xử lý encounter, loot, khóa cửa, trap, survivor, terminal, boss và quyết định khi nào rút lui.

## 3.4 Power phải đến từ risk

Các tài nguyên cơ bản có thể được sản xuất trong Silo.

Nhưng công nghệ mạnh, blueprint hiếm và vật liệu đặc biệt **không thể chỉ ngồi trong căn cứ farm mãi**.

Người chơi phải:

- expedition vùng nguy hiểm;
- đánh elite/boss;
- raid Silo khác;
- tranh contested site;
- tham gia world event.

## 3.5 PvP phải có lý do kinh tế

PvP không được tồn tại chỉ vì “game online cần PvP”.

Người chơi tấn công vì có thứ họ muốn:

- rare material;
- encrypted research data;
- prototype component;
- blueprint fragment;
- prestige;
- territory;
- seasonal reward.

## 3.6 Skill nằm ở preparation + decision

Khó hơn không đồng nghĩa enemy chỉ có nhiều HP hơn.

Khả năng sống sót phải phụ thuộc vào:

- mix team;
- role;
- súng;
- giáp;
- resistance;
- utility;
- consumable;
- route;
- retreat timing.

---

# 4. Core game loop

```
BUILD SILO
   ↓
RECRUIT / TRAIN UNITS
   ↓
CRAFT & EQUIP
   ↓
SCOUT
   ↓
CHOOSE TARGET + DIFFICULTY
   ↓
EXPEDITION / BOSS / PVP
   ↓
LOOT / EXTRACT
   ↓
HEAL / REPAIR / RESEARCH
   ↓
UPGRADE SILO
   ↓
UNLOCK NEW TECH / REGION / THREATS
   ↺
```

Điểm quan trọng:

**Silo tạo khả năng để đi ra ngoài.  
Thế giới bên ngoài tạo vật liệu để nâng Silo.**

Hai phần phải phụ thuộc lẫn nhau.

---

# 5. Silo progression

Silo có cấp trung tâm tương tự Town Hall trong Clash of Clans, tạm gọi:

**Command Core Level — CCL**

Ví dụ prototype:

| CCL | Giai đoạn | Mở khóa chính |
|---|---|---|
| 1 | Survival | Power, Water, Living, Storage |
| 2 | Stability | Workshop, Clinic |
| 3 | Contact | Radio, Scout |
| 4 | Expedition | Squad deployment |
| 5 | Research | Research Lab |
| 6 | Defense | Security, turret, reinforced door |
| 7 | Network | phát hiện Silo khác |
| 8 | Conflict | PvP raid |
| 9 | Advanced Tech | prototype weapon |
| 10 | Alien Tech | artifact research |
| 11 | Coalition | alliance projects |
| 12 | Surface Return | endgame systems |

Con số chưa khóa; mục tiêu là có một trục progression rất dễ hiểu.

## Quy tắc quan trọng

Nâng CCL không chỉ cần tài nguyên xây dựng.

Từ mid-game, một số mốc phải cần:

- boss component;
- encrypted core;
- military authorization chip;
- PvP research token;
- alien material.

Nhờ vậy người chơi không thể chỉ idle farm để lên endgame.

---

# 6. Các phòng trong Silo

Nhóm production:

- Power Generator
- Water Treatment
- Hydroponics
- Recycling
- Synthetic Food Lab

Nhóm population:

- Living Quarters
- Recreation
- School / Training
- Mess Hall

Nhóm combat:

- Armory
- Training Room
- Clinic
- Security Room
- Drone Bay

Nhóm technology:

- Workshop
- Research Lab
- Electronics Lab
- Xenobiology Lab
- Prototype Forge

Nhóm command:

- Command Center
- Radio
- Scout Center
- Intelligence Room

Nhóm storage / protection:

- General Storage
- Weapon Vault
- Secure Vault
- Quarantine
- Blast Door

---

# 7. Hidden Silo exploration

Một khác biệt lớn với Fallout Shelter:

**không phải toàn bộ không gian dưới Silo đều do người chơi tự xây.**

Trong lúc đào mở rộng có thể tìm thấy:

- sealed military corridor;
- bunker cũ;
- laboratory;
- reactor;
- hang tự nhiên;
- infected nest;
- unknown chamber;
- alien structure.

Ví dụ:

```
NEW SECTOR DISCOVERED

Depth: -312 m
Signal: Unknown
Atmosphere: Unsafe
Door: Pre-war military

[Send squad]
[Seal sector]
```

Như vậy ngay cả việc mở rộng căn cứ cũng tạo exploration.

## Quy tắc chiếm phòng / sector

**Phát hiện một phòng không đồng nghĩa sở hữu phòng đó.**

Một sector mới đào trúng luôn bắt đầu ở trạng thái chưa kiểm soát, ví dụ:

- UNKNOWN;
- SEALED;
- HOSTILE;
- CONTAMINATED;
- UNSTABLE;
- CONTROLLED.

Để biến sector thành đất xây dựng, người chơi có thể phải:

- phá cửa;
- cấp điện tạm;
- scan môi trường;
- tiêu diệt sinh vật;
- vô hiệu hóa turret / robot;
- xử lý khí độc / bức xạ;
- dọn ổ ký sinh;
- sửa kết cấu;
- đánh mini-boss;
- giữ sector trong một khoảng thời gian.

Ví dụ:

```
SECTOR B-17

Status: HOSTILE
Threat: UNKNOWN BIOLOGICAL
Power: OFFLINE
Atmosphere: PARTIAL TOXIC

Objective:
[ ] Restore emergency power
[ ] Clear hostile presence
[ ] Seal ventilation breach
[ ] Establish control

Reward:
+1 buildable room
Unknown cache
```

Chỉ sau khi hoàn thành điều kiện kiểm soát, phòng mới trở thành một phần chính thức của Silo và cho phép xây / cải tạo.

Một số phòng có thể có giá trị đặc biệt đến mức người chơi chọn **giữ nguyên công năng cũ** thay vì phá đi xây lại, ví dụ reactor cổ, kho quân sự hay laboratory.

---

# 8. Unit system

Mỗi unit có 5 nhóm thông tin.

## 8.1 Base stats

Ví dụ:

- Combat
- Endurance
- Agility
- Perception
- Intelligence
- Tech
- Medical
- Resolve

Không nhất thiết dùng SPECIAL của Fallout để tránh sao chép trực tiếp.

## 8.2 Role

Ví dụ:

### Vanguard
chịu sát thương, shield, heavy armor.

### Assault
DPS chính.

### Scout
recon, trap detection, critical.

### Engineer
hack, repair, robot/drone.

### Medic
heal, revive, antidote.

### Specialist
explosive, alien tech, sniper, biological defense...

## 8.3 Trait

Trait làm unit khác nhau.

Ví dụ:

**Claustrophobic**
- giảm morale khi ở Silo lâu;
- tăng morale khi expedition.

**Veteran**
- weapon handling tốt hơn.

**Field Medic**
- hiệu quả medkit +25%.

**Paranoid**
- phát hiện Mimic tốt;
- dễ gây conflict trong Silo.

**Alien Touched**
- dùng alien gear hiệu quả;
- tăng Exposure.

## 8.4 Gear

Mỗi unit:

- Primary weapon
- Armor
- Utility
- Trinket / Module
- Consumable slots

## 8.5 Condition

- HP
- fatigue
- radiation / toxin
- infection
- morale
- trauma
- injury

Một unit sống sót nhiều mission có giá trị hơn unit mới không chỉ vì level mà còn vì trait/history.

---

# 9. Team composition

Đây là một phần phải sâu hơn Fallout Shelter.

Không có một đội hình “4 khẩu súng mạnh nhất” luôn thắng.

## Squad size progression — khóa 3 → 4 → 5

Squad mở dần theo progression:

| Giai đoạn | Squad cap | Mục đích |
|---|---:|---|
| Early game | 3 | học combat, weapon, heal, revive, retreat |
| Mid game | 4 | bắt đầu role specialization rõ ràng |
| Late game | 5 | mở full tactical composition |
| Endgame | 5 max | mạnh lên bằng build/gear/trait, không tăng quân số |

**5 là giới hạn cứng của squad tiêu chuẩn.**

Lý do:

- đủ nhỏ để người chơi nhớ từng survivor;
- đủ lớn để tạo Tank / DPS / Medic / Engineer / Specialist;
- combat vẫn đọc được rõ ràng theo phong cách Fallout Shelter;
- tránh biến trận đánh thành đám đông khó theo dõi;
- mỗi slot mới mở phải tạo cảm giác progression đáng kể.

Ví dụ ở squad 3, người chơi thường phải đánh đổi:

```
Vanguard
Assault
Medic
```

Khi mở slot 4:

```
Vanguard
Assault
Medic
Engineer
```

Khi mở slot 5:

```
Vanguard
Assault
Heavy / Specialist
Engineer
Medic
```

Unlock slot thứ 4 và thứ 5 nên gắn với milestone CCL / facility progression thay vì chỉ level nhân vật.

### Không phải lúc nào cũng nên mang đủ 5

Cuối game vẫn phải có lý do để squad 3–4 người tồn tại.

Mission có thể tác động bởi:

- supply consumption;
- travel speed;
- Noise / detection;
- deployment cost;
- giới hạn không gian.

Ví dụ:

```
STEALTH RECON
Recommended: 3 units or fewer

COLLAPSED TUNNEL
Maximum deployment: 3

HEAVY ASSAULT
Maximum deployment: 5
```

Squad 5 mạnh hơn trong combat nhưng không mặc định tối ưu cho mọi nhiệm vụ.

Ví dụ squad 4 người:

```
Vanguard
Assault
Medic
Engineer
```

hoặc:

```
Scout
Scout
Sniper
Medic
```

Tùy target.

## Ví dụ encounter

### Infested Hospital

Threat:

- biological infection;
- close-range enemies;
- locked medicine storage.

Đội phù hợp:

- Medic;
- Vanguard;
- Engineer;
- Assault.

### Military Research Base

Threat:

- turret;
- robot;
- electronic lock;
- armored enemies.

Đội phù hợp:

- Engineer;
- EMP consumable;
- armor piercing weapon.

### Alien Nest

Threat:

- acid;
- swarm;
- psychic effect.

Đội phù hợp:

- resistance armor;
- flamethrower;
- Resolve cao;
- antidote.

Nhờ vậy việc chuẩn bị team trở thành gameplay.

---

# 10. Consumables

Consumable phải quan trọng.

Ví dụ:

- Medkit
- Stim
- Antidote
- EMP
- Grenade
- Breaching Charge
- Portable Shield
- Drone
- Scanner
- Oxygen
- Anti-radiation injection
- Emergency Beacon

Người chơi có số slot giới hạn.

Trước mission phải quyết định:

> mang thêm medkit hay breaching charge?

Đây là một lựa chọn chiến thuật có giá trị.

---

# 11. Scout system

Scout là bước trước Expedition / Raid.

Người chơi không luôn biết chính xác mục tiêu.

Ví dụ:

```
ABANDONED RESEARCH CAMP

Distance: 12 km
Estimated Threat: ???
Possible Loot:
- Electronics
- Medical
- Research Data

Signal detected: YES

[Quick Scout]
[Deep Scout]
[Deploy]
```

Deep Scout tốn:

- thời gian;
- drone battery;
- intel;
- scout unit.

Nhưng Scout **không bao giờ biến mission thành thông tin hoàn hảo**.

Scout có thể reveal hoặc ước lượng:

- nhóm enemy có khả năng xuất hiện;
- dấu hiệu boss;
- số room ước tính;
- hazard đã phát hiện;
- nhóm loot có khả năng tồn tại;
- mức độ hoạt động;
- một phần layout.

Thông tin phải có **confidence** và có thể thiếu.

Ví dụ:

```
DEEP SCAN

Biological activity: HIGH       Confidence 82%
Mechanical activity: LOW        Confidence 61%
Energy weapon signature: NONE   Confidence 47%
Rooms detected: 6–9
Possible loot:
- Medical
- Research
- Unknown

Unmapped area: YES
```

Scout tốt làm giảm rủi ro chứ không xóa rủi ro.

Một căn cứ được báo chủ yếu là biological vẫn có thể có robot trong phòng sâu. Một boss được dự đoán dùng giáp nhẹ vẫn có thể xuất hiện biến thể kháng laser.

**Information is probabilistic, not omniscient.**

---

# 12. Chọn độ khó Expedition

Một điểm khóa của game:

**người chơi tự chọn risk level của mục tiêu.**

Ví dụ cùng loại mission:

### EASY

- threat thấp;
- enemy ít;
- loot phổ thông;
- tỷ lệ injury thấp;
- extraction dễ.

### MEDIUM

- elite có thể xuất hiện;
- loot tốt;
- có rare component.

### HARD

- elite thường xuyên;
- hazard;
- limited extraction;
- rare blueprint fragment;
- nguy cơ mất unit cao.

### EXTREME / FORBIDDEN

- boss;
- alien anomaly;
- permadeath hoặc severe injury có thể xảy ra;
- prototype / artifact loot.

Difficulty không chỉ nhân HP.

Mỗi tier thêm mechanic mới.

---

# 13. Survival probability

UI có thể hiển thị một đánh giá trước khi đi:

```
MISSION RISK

Combat Match      GOOD
Hazard Resistance POOR
Medical Support   GOOD
Recon              LOW

Estimated Survival:
67%

Estimated Loot:
HIGH
```

Nhưng không nên cho con số chính xác tuyệt đối.

Game chỉ đưa estimate.

Người chơi vẫn phải tự đánh giá.

---

# 14. Expedition gameplay

Expedition được chia theo node/room.

Ví dụ:

```
Entrance
   ↓
Lobby
 ├── Security Room
 │      └── Armory
 ↓
Laboratory
 ├── Quarantine
 ↓
Underground Sector
 ↓
Boss
```

Mỗi room có thể:

- combat;
- loot;
- story event;
- trap;
- locked door;
- survivor;
- terminal;
- puzzle;
- secret;
- anomaly.

Người chơi quyết định:

- vào hay bỏ;
- dùng item hay tiết kiệm;
- chữa ngay hay tiếp tục;
- loot thêm hay extraction.

---

# 15. Extraction là quyết định quan trọng

Loot chưa thực sự thuộc về người chơi cho tới khi squad về được Silo.

Ví dụ:

```
MISSION PROGRESS 73%

Loot Value: VERY HIGH
Squad Condition: POOR

Continue to Boss?
[Continue]
[Extract]
```

Tham thêm có thể mất tất cả.

Đây là nguồn tension chính.

---

# 16. Loot tiers

Ví dụ:

- Scrap
- Civilian
- Industrial
- Military
- Advanced
- Prototype
- Alien
- Artifact

Không nên chỉ tăng damage tuyến tính.

Gear hiếm có mechanic khác.

Ví dụ:

**Arc Rifle**
- damage trung bình;
- chain lightning.

**Phase Armor**
- né đòn đầu mỗi room.

**Bio Scanner**
- reveal infected survivor.

**Alien Core**
- tăng năng lượng;
- tăng Signal.

---

# 17. Blueprint system

Không phải nhặt được khẩu súng là có thể sản xuất vô hạn.

Một số gear cần **Blueprint**.

Blueprint có thể gồm fragment.

Ví dụ:

```
M-77 GAUSS RIFLE

Blueprint:
3 / 5 fragments

Required:
Military Data      12
Titanium Alloy      8
Prototype Capacitor 2
```

## Nguồn Blueprint

### Common / Standard
- PvE;
- research;
- quest.

### Advanced
- elite expedition;
- military site;
- boss.

### Prototype
- boss;
- high difficulty PvE;
- PvP.

### Legendary / Artifact
- world boss;
- contested site;
- seasonal event;
- deep alien sector.

---

# 18. Tranh đoạt tài nguyên

Một số vật liệu **không sản xuất được trong Silo**.

Ví dụ:

### Military Encryption Key
dùng unlock military blueprint.

### Prototype Capacitor
dùng chế tạo energy weapon.

### Alien Neural Core
dùng alien research.

### Silo Combat Data
dùng nâng advanced defense / weapon system.

### Quantum Alloy
endgame crafting.

Người chơi muốn tiến sâu phải ra khỏi Silo.

Đây là động lực cạnh tranh chính.

---

# 19. Boss system

Boss không chỉ drop một khẩu súng ngẫu nhiên.

Boss là nguồn progression.

Ví dụ:

## Hive Mother

Drop:

- Chitin Core;
- Bio Sample;
- Bio-weapon blueprint fragment.

## War Machine A-17

Drop:

- Military AI Core;
- Servo;
- Heavy weapon blueprint.

## Fallen Visitor

Drop:

- Alien Crystal;
- Unknown Data;
- Artifact blueprint.

Boss có:

- normal;
- elite;
- world;
- alliance.

---

# 20. Boss-exclusive progression

Một số recipe bắt buộc phải có vật liệu boss.

Ví dụ:

```
PLASMA CUTTER MK-II

Research complete: YES

Required:
Alloy              40
Electronics         25
Alien Plasma Core    1   ← boss only
```

Điều này khiến người chơi mạnh về economy nhưng không chịu đi combat vẫn không thể sở hữu mọi công nghệ.

---

# 21. PvP unlock

PvP không mở ngay đầu game.

Đề xuất:

- CCL 1–4: hoàn toàn PvE.
- CCL 5–6: thấy NPC Silo.
- CCL 7: trade / scan player.
- CCL 8: raid PvP mở.
- CCL 9+: advanced PvP systems.

Mục đích:

trước khi PvP xuất hiện, người chơi đã có thứ họ quan tâm và muốn bảo vệ.

---

# 22. PvP matchmaking

Không match bằng level đơn giản.

Match score nên xét:

- Command Core Level;
- Defense Rating;
- Squad Power;
- tech tier;
- recent PvP performance.

Trọng số chính vẫn là **CCL**.

Nguyên tắc:

> CCL 6 không bị CCL 10 nghiền.

Có thể cho khoảng:

```
Target band:
CCL ±1
Power band ±15–20%
```

Tùy balance sau test.

---

# 23. PvP scouting

Trước khi raid, người chơi scout.

Ví dụ:

```
SILO 2841

CCL: 8
Population: 71
Defense: HIGH

Detected Resources:
Food        HIGH
Metal       MEDIUM
Research    HIGH

Security Layout:
PARTIAL

Possible Reward:
Encrypted Combat Data
```

Scout sâu có thể reveal:

- entrance;
- defense room;
- vault;
- power;
- command center.

---

# 24. Silo raid = Dungeon PvP

Đây nên là signature feature.

Không phải click “Attack” rồi xem hai đội tự tính.

Attacker phải đột nhập từng sector.

Ví dụ:

```
Surface Entrance
      ↓
Blast Door
      ↓
Security
     / \
Power  Armory
   \    /
 Living Area
      ↓
Command Core
```

Attacker quyết định:

- phá Power để disable turret;
- đánh Armory lấy weapon cache;
- đi thẳng Command Core;
- tìm Secure Vault.

Càng ở lâu:

- alarm tăng;
- defender reinforcement mạnh hơn;
- extraction khó hơn.

---

# 25. PvP objectives

Raid không nhất thiết luôn phải phá Core.

Có thể có nhiều mục tiêu:

### Resource Raid
lấy nguyên liệu.

### Intelligence Raid
lấy Research Data.

### Sabotage
phá temporary system.

### Blueprint Hunt
tìm encrypted blueprint fragment.

### Full Assault
đánh Command Core.

Nhờ vậy PvP đa dạng hơn.

---

# 26. PvP reward — không phá người thua

Không nên cho attacker cướp sạch kho.

Điều này dễ làm casual player bỏ game.

Đề xuất:

Attacker nhận:

- một phần nhỏ exposed resource;
- bonus reward do hệ thống tạo;
- Combat Data;
- PvP chest;
- ranking.

Rare blueprint nên phần lớn đến từ **reward crate / token**, không phải giật mất vật phẩm đã sở hữu của defender.

Defender mất có giới hạn.

---

# 27. Defense design

Người chơi bố trí:

- security doors;
- turret;
- guard squad;
- drone;
- sensor;
- trap;
- blast door;
- quarantine trap;
- power routing.

Nhưng defense bị giới hạn bằng:

**Defense Capacity**

Ví dụ:

```
Defense Capacity: 84 / 100

Turret       15
Blast Door   10
Drone Bay    20
Guard Post   18
Sensor        5
```

Tránh spam vô hạn.

---

# 28. Online interaction nhưng không ép online

PvP chính nên asynchronous.

Người bị tấn công không cần online.

AI dùng:

- unit defense roster;
- room layout;
- defense rules do chủ Silo đặt.

Ví dụ:

```
Defense Rule:

If Power Room attacked:
→ Deploy Engineer Squad

If Command Core breached:
→ Deploy Elite Guard
```

Sau này có thể có live PvP event riêng, nhưng không phải core.

---

# 29. Contested Sites

Một lớp gameplay giúp tăng tranh đoạt.

Trên World Map xuất hiện các vị trí hiếm:

- crashed alien ship;
- military bunker;
- satellite uplink;
- underground laboratory;
- uranium mine;
- artifact crater.

Các site chỉ tồn tại một thời gian.

Nhiều player có thể phát hiện cùng một site.

Ví dụ:

```
CRASH SITE A-91

Expires: 02:17:44

Potential:
Alien Alloy
Unknown Blueprint

Detected Silo activity:
3
```

Người chơi phải quyết định:

- đi ngay;
- scout;
- chờ người khác đánh boss trước;
- tranh quyền loot.

---

# 30. World Map

World Map bắt đầu nhỏ.

```
          ???
           |
Ruins -- SILO -- Metro
           |
        Forest
```

Sau đó mở rộng thành:

- city ruins;
- military zone;
- forest;
- crater;
- alien zone;
- NPC settlement;
- player silo;
- boss;
- contested site;
- trade route.

Fog of war được mở bằng Scout / Radio / expedition.

---

# 31. Dynamic target generation

Scout có thể tìm mục tiêu ngẫu nhiên như Fallout Shelter, nhưng sâu hơn.

Người chơi chọn:

```
SEARCH PARAMETERS

Target difficulty:
[Easy] [Medium] [Hard] [Extreme]

Preferred loot:
[Food]
[Weapon]
[Tech]
[Medical]
[Unknown]

Search radius:
20 km
```

Game sinh ra hoặc tìm target phù hợp.

Difficulty càng cao:

- target xa hơn;
- encounter nguy hiểm hơn;
- extraction khó hơn;
- loot table tốt hơn.

---

# 32. Search cost

Không nên cho reroll vô hạn.

Search tiêu tốn:

- radio energy;
- intel;
- drone battery;
- time.

Nhờ vậy “tìm được mục tiêu ngon” cũng có giá trị.

---

# 33. Risk vs Reward

Mỗi mission phải có câu hỏi:

> Tôi có đủ mạnh để đánh không?

và:

> Tôi có chấp nhận mất squad để lấy món này không?

Ví dụ:

```
PROTOTYPE LAB

Recommended:
Squad Power: 8,400

Your Squad:
7,650

Risk:
HIGH

Possible:
Gauss Blueprint
Prototype Capacitor
Military AI

[Deploy]
```

Game vẫn cho đánh.

Không hard block.

Người chơi giỏi preparation có thể thắng mục tiêu mạnh hơn.

---

# 34. Injury / death

**Death là thật ở mọi nội dung combat.**

Khi HP về 0, unit chuyển sang trạng thái **DOWN / DEAD** tùy encounter và sát thương.

Unit chết không tự hồi khi kết thúc trận.

Muốn đưa unit trở lại, người chơi phải dùng một **revival item** hiếm tương tự chức năng hồi sinh trong Fallout Shelter, tạm gọi:

- Revival Injector;
- Trauma Kit;
- Emergency Reanimator.

Tên và fiction sẽ khóa sau.

Quy tắc:

- revive item chiếm inventory / consumable capacity;
- có thể dùng trong mission nếu điều kiện an toàn;
- nếu không còn item, squad phải mang thi thể / dữ liệu sinh học về hoặc chấp nhận mất unit;
- một số trạng thái đặc biệt có thể chặn revive;
- revive không nên miễn phí và không nên vô hạn.

Difficulty tác động vào:

- damage;
- tốc độ unit bị hạ;
- số lượng encounter;
- khả năng tiếp cận extraction;
- mức tiêu hao revive / medical item;

chứ **không thay đổi nguyên tắc “Easy thì bất tử, Hard mới chết”.**

Mục tiêu là khiến người chơi quý unit nhưng vẫn có một lớp cứu hộ để death không biến thành mất mát ngẫu nhiên hoàn toàn.

Ngoài death, unit vẫn có thể bị **Lost / Captured / Separated**, mở rescue mission trong một số loại encounter.

---

# 35. Rescue system

Ví dụ:

```
UNIT LOST

Maya Chen
Last signal:
Old Metro Sector 7

Life signal:
WEAK

Rescue window:
11h 42m
```

Người chơi có thể lập squad thứ hai đi cứu.

Đây là một hệ thống rất phù hợp để tạo emergent story.

---

# 36. Alien Exposure

Dùng công nghệ Alien tạo một trục progression riêng:

```
ALIEN EXPOSURE

██████░░░░ 62%
```

Exposure cao có lợi:

- alien weapon efficiency;
- artifact research;
- mutations;
- exotic abilities.

Nhưng gây:

- event bất thường;
- mental effect;
- Mimic;
- alien detection;
- attack.

Người chơi phải chọn:

**Human Technology**

hay

**Hybrid / Alien Technology**.

---

# 37. Signal / Noise system

Silo càng phát triển càng phát ra tín hiệu.

Nguồn Noise:

- reactor;
- radio;
- alien tech;
- active radar;
- large factory.

Noise cao:

+ scout xa hơn;
+ production mạnh hơn;

nhưng:

- player khác dễ phát hiện;
- alien event tăng;
- world threat tăng.

Một Silo mạnh không thể hoàn toàn vô hình.

---

# 38. Internal Silo events

Ví dụ:

- fight giữa colonist;
- sabotage;
- disease;
- reactor problem;
- survivor xin vào;
- unit mất tích;
- scientist muốn thử artifact;
- black market;
- strange signal;
- suspected Mimic.

Quyết định có hậu quả dài hạn.

---

# 39. Mimic / infiltration

Một survivor cứu từ expedition có thể không phải con người.

Ví dụ:

```
ANOMALY

Oxygen use does not match
registered population.

Possible causes:
- sensor error
- hidden survivor
- biological anomaly
```

Người chơi có thể:

- scan dân cư;
- quarantine;
- điều tra;
- bỏ qua.

Đây là một lớp gameplay rất phù hợp với bối cảnh Silo kín.

---

# 40. Factions

NPC faction có thể gồm:

### Continuity
tàn dư chính phủ / quân đội.

### Free Settlements
cộng đồng tự trị mặt đất.

### Earthborn
chống alien technology.

### Ascendants
ủng hộ tiến hóa bằng công nghệ Alien.

### Archivists
thu thập tri thức thế giới cũ.

Faction mở:

- quest;
- gear;
- blueprint;
- trade;
- reputation perk.

---

# 41. Alliance

Nhiều Silo có thể lập Coalition.

Alliance gameplay:

- shared radar;
- boss;
- research project;
- trade;
- defense support;
- world structure.

Ví dụ công trình:

- Relay Station;
- Anti-Alien Shield;
- Research Array;
- Orbital Scanner;
- Trade Hub.

Không nên biến Alliance thành bắt buộc để chơi casual.

---

# 42. Endgame

Endgame không chỉ là Silo level max.

Progression chuyển sang:

- surface reclamation;
- regional control;
- alien megastructure;
- world boss;
- alliance project;
- artifact research.

Mục tiêu dài hạn:

> từ một căn hầm cố sống sót → trở thành một trung tâm tái thiết nhân loại.

---

# 43. Narrative reveal

Gợi ý cốt truyện dài hạn:

Ban đầu nhân loại tin rằng Alien đã xâm lược Trái Đất.

Sau này phát hiện:

**một số cấu trúc Alien đã nằm sâu dưới Trái Đất từ hàng triệu năm trước.**

Những vật thể ngoài không gian không phải đội quân đầu tiên.

Chúng có thể đang:

- đánh thức;
- thu hồi;
- tiêu diệt;
- hoặc ngăn chặn

một thứ đã tồn tại trên Trái Đất từ trước con người.

Không khóa đáp án ngay ở pre-production.

---

# 44. Seasonal narrative

Ví dụ:

## Season 1 — The Signal
mở Radio Network.

## Season 2 — First Contact
phát hiện Silo và faction khác.

## Season 3 — The Hive
world biological threat.

## Season 4 — Architects
alien structures.

## Season 5 — Surface
tranh giành khu vực mặt đất.

---

# 45. Economy layers

## Tier 1 — Basic

Silo tự sản xuất:

- food;
- water;
- power.

## Tier 2 — Industrial

Farm / expedition:

- metal;
- chemical;
- electronics.

## Tier 3 — Strategic

không sản xuất dễ dàng:

- military data;
- reactor material;
- rare alloy.

## Tier 4 — Conflict

chủ yếu Boss / PvP / contested:

- Combat Data;
- Prototype Core;
- Alien Core;
- Artifact Fragment.

Nhờ vậy economy tự nhiên buộc người chơi mở rộng gameplay.

---

# 46. Anti pay-to-win rule

Không bán trực tiếp:

- PvP-exclusive blueprint;
- boss-exclusive component;
- artifact;
- max-level gear.

Có thể monetize:

- cosmetic;
- Silo decoration;
- outfit;
- skin;
- quality-of-life;
- battle pass có reward không phá balance.

Nếu bán tài nguyên, phải tránh việc người trả tiền bypass toàn bộ expedition / boss / PvP progression.

---

# 47. Gameplay escalation

## Early game

Fallout Shelter feeling:

- xây;
- dân;
- resource;
- room;
- small PvE.

## Mid game

RPG / expedition:

- gear;
- squad composition;
- difficult target;
- blueprint;
- boss.

## Late game

Shared world:

- PvP;
- contested site;
- faction;
- alliance;
- alien threat.

Nhờ vậy game dễ học nhưng có chiều sâu tăng dần.

---

# 48. Điểm khác biệt so với Fallout Shelter

Không định vị game là “Fallout Shelter nhưng skin khác”.

Các khác biệt cốt lõi:

1. Expedition có gameplay thật.
2. Difficulty do người chơi lựa chọn.
3. Team composition ảnh hưởng lớn.
4. Consumable và preparation quan trọng.
5. Blueprint và crafting sâu.
6. Boss là nguồn progression.
7. PvP Silo raid.
8. Persistent World Map.
9. Contested resources.
10. Alien Exposure / Noise.
11. Silo tự thân cũng có exploration.
12. Unit có injury / rescue / history.

---

# 49. Điểm khác biệt so với Clash of Clans

Học Clash ở:

- base progression;
- clear central level;
- matchmaking;
- asynchronous attack;
- long-term upgrade loop.

Không học theo kiểu:

- quân dùng một lần;
- base chỉ nhìn từ trên xuống;
- phá % công trình để lấy sao;
- người chơi mạnh nghiền người yếu.

Trong Căn Hầm:

**raid là một dungeon infiltration bằng squad mà người chơi đã nuôi từ trước.**

---

# 50. MVP / Prototype đề xuất

Không làm World Map MMO ngay.

Prototype đầu nên chứng minh 3 thứ:

## Prototype A — Silo

- 6 loại room;
- production;
- 10–20 unit;
- drag / assign worker;
- upgrade.

## Prototype B — Expedition

- squad system hỗ trợ cap 5;
- prototype bắt đầu bằng squad 3 và test unlock 4 → 5;
- 1 map;
- 8–12 room;
- loot;
- consumable;
- injury;
- extraction.

## Prototype C — Silo Raid

- dùng cùng combat system;
- một Silo defense giả lập;
- room route;
- vault;
- alarm;
- extraction.

Nếu ba prototype này vui, mới xây persistent world.

---

# 51. Vertical slice mục tiêu

Một vertical slice tốt phải cho người chơi trải nghiệm:

1. bắt đầu Silo nhỏ;
2. xây Power / Water / Living;
3. recruit unit;
4. tìm weapon;
5. lập squad;
6. scout một building;
7. chọn Medium;
8. đi từng room;
9. gặp injury;
10. tìm rare component;
11. quyết định extract;
12. craft weapon mới;
13. upgrade Command Core;
14. bắt được tín hiệu Silo khác.

Khoảnh khắc kết thúc slice:

```
UNKNOWN HUMAN SIGNAL DETECTED

Distance: 18.4 km
Status: ACTIVE

[SCAN]
```

Đây là hook đưa người chơi từ single-player survival sang shared world.

---

# 52. Các quyết định thiết kế khóa ở v0.2

Các điểm sau được xem là direction chính cho tới khi prototype chứng minh ngược lại:

- Mỗi người chơi sở hữu một Silo.
- Silo có central progression level.
- 10–20 giờ đầu ưu tiên PvE, không ép PvP.
- Expedition là gameplay room-by-room / area-by-area.
- Người chơi được chọn difficulty.
- Team composition, equipment và consumable quyết định khả năng sống sót.
- Squad progression khóa theo **3 → 4 → 5**, với **5 là cap tiêu chuẩn tối đa**.
- Combat giữ nhịp trực quan kiểu Fallout Shelter nhưng thêm formation, role và tactical preparation.
- Weapon class phải khác nhau bằng damage profile/effect, không chỉ bằng con số DPS.
- Unit có thể chết thật và phải dùng revival item để cứu.
- Scout chỉ cung cấp thông tin xác suất; không có reconnaissance 100% chính xác.
- Phòng / sector mới trong Silo phải được clear và giành quyền kiểm soát trước khi sử dụng.
- Rare progression materials tồn tại ngoài Silo.
- Một số blueprint/component chỉ đến từ Boss, PvP hoặc contested content.
- PvP ưu tiên matchmaking ngang CCL/power.
- PvP là asynchronous Silo infiltration.
- Không cho high-level farm người mới.
- Defender không mất sạch tài nguyên.
- Silo layout có giá trị cả PvE management và PvP defense.
- Persistent World Map mở dần theo progression.
- Alien technology luôn đi kèm trade-off.

---

# 53. Những điểm cần prototype để quyết định sau

Chưa khóa:

- mức độ active-control trong combat (bao nhiêu skill / retarget / timing);
- side-view hay isometric;
- mốc CCL chính xác để mở slot squad thứ 4 và thứ 5;
- số Command Core Level;
- PvP target selection;
- season duration;
- alliance size;
- monetization cụ thể.

Không nên khóa những điểm này trước khi có prototype chiến đấu.

---

# 54. Core fantasy

Một session tốt phải tạo được câu chuyện kiểu:

> Tôi cần một Prototype Capacitor để nâng Gauss Rifle. Scout tìm thấy một phòng nghiên cứu Hard cách Silo 14 km. Squad của tôi thiếu Engineer nên tôi đổi một Assault lấy Minh — Engineer level thấp hơn nhưng hack tốt. Tôi mang 2 Medkit, 1 EMP và bỏ grenade. Mission đi ổn cho tới tầng 5 thì Medic bị thương. Tôi đã nhặt được Capacitor nhưng radar báo còn một boss room phía dưới. Tôi quyết định tham, mất Vanguard và phải bỏ mission. Hai giờ sau xuất hiện rescue signal của Vanguard. Tôi phải lập squad thứ hai đi cứu.

Đó chính là loại câu chuyện mà hệ thống game cần tự sinh ra.

---

# 55. Một câu tóm tắt sản phẩm

> **Căn Hầm là survival base-builder nơi mỗi người chơi xây một Silo, nuôi một đội survivor, khám phá thế giới hậu thảm họa theo từng khu vực và buộc phải mạo hiểm PvE, Boss hoặc PvP để giành công nghệ cần thiết cho bước tiến hóa tiếp theo của căn cứ.**


---

# 56. Combat direction lock — Fallout Shelter feel, sâu hơn về chiến thuật

Combat giữ tinh thần dễ đọc của Fallout Shelter:

- squad bước vào room / encounter;
- battle diễn ra liên tục;
- unit tự thực hiện đòn đánh cơ bản;
- weapon và target tạo phần lớn DPS;
- người chơi không micro từng bước chân như RTS.

Nhưng trước và trong trận có thêm chiều sâu.

## Trước trận

Người chơi quyết định:

- squad composition;
- formation;
- weapon;
- armor;
- utility;
- consumables;
- target priority preset.

Ví dụ:

```
FRONT
Vanguard      Shotgun

MID
Assault       Laser Rifle
Engineer      SMG + EMP

BACK
Medic         Pistol
```

## Trong trận

Người chơi tập trung vào các quyết định quan trọng thay vì spam thao tác:

- focus target;
- đổi target;
- kích hoạt consumable;
- heal / revive;
- dùng active ability nếu unit có;
- đổi vị trí trong giới hạn;
- quyết định đi tiếp hay rút.

Mục tiêu:

> **Easy to control, hard to prepare well.**

Chiến thuật chính nằm ở đội hình và preparation, không phải APM.

---

# 57. Imperfect Intel — không bao giờ biết chắc mình sắp gặp gì

Đây là một nguyên tắc gameplay khóa.

Người chơi **không được biết chính xác toàn bộ enemy, resistance, loot và layout trước khi vào**.

Recon chỉ thay đổi từ:

> “gần như mù”

thành:

> “có cơ sở để dự đoán”.

Không bao giờ thành:

> “biết chính xác 100%”.

Ví dụ người chơi thấy:

```
OLD ENERGY LAB

Known:
- electromagnetic activity
- at least 1 hostile lifeform
- possible weapon storage

Unknown:
- lower floors
- exact enemy subtype
- boss resistance
```

Người chơi đoán nơi này hợp với laser weapon.

Nhưng xuống sâu có thể gặp:

**Crystal Carapace Beast**
- Laser Resistance 70%
- Ballistic Resistance 10%

Assault mang Laser Rifle lúc này trở thành lựa chọn không tối ưu.

Điều này là **feature**, không phải lỗi RNG.

---

# 58. Tactical redundancy — một lựa chọn sai không được phá toàn bộ squad

Bất định chỉ vui nếu người chơi còn cách xoay xở.

Vì vậy game phải tránh hard-counter tuyệt đối ở nội dung bình thường.

Ví dụ:

- enemy kháng Laser 70%, không phải miễn nhiễm 100%;
- Engineer mang súng yếu vẫn có thể hỗ trợ EMP / utility;
- Vanguard có thể giữ quái để Ballistic unit gánh DPS;
- grenade hoặc consumable có thể bù một phần;
- người chơi có thể bỏ room đó và tìm route khác;
- cuối cùng luôn có quyền **RETREAT** nếu chưa bị mechanic đặc biệt khóa.

Một team cân bằng có khả năng chịu sai thông tin tốt hơn một team cực đoan.

Đây tạo ra trade-off:

### Specialized Squad
đánh rất nhanh nếu đoán đúng target.

### Balanced Squad
chậm hơn nhưng sống sót tốt khi thông tin sai.

Không đội hình nào luôn tối ưu.

---

# 59. Mission completion không bắt buộc 100%

Người chơi **không cần clear toàn bộ map để mission được xem là có giá trị**.

Ví dụ:

```
MAP DISCOVERED: 8 rooms

Cleared: 5
Unexplored: 3

Recovered:
+ 1 Military Rifle
+ 18 Electronics
+ Medical Data

Squad:
1 DEAD — revived
2 injured
Revival items: 0

[GO DEEPER]
[EXTRACT]
```

Rút lui sau 5/8 phòng là một quyết định hợp lệ.

Điều này rất quan trọng vì nó biến:

> “không đủ mạnh = thua”

thành:

> “không đủ mạnh = phải biết dừng đúng lúc”.

Một mission có thể kết thúc với:

- Partial Clear;
- Successful Extraction;
- Full Clear;
- Boss Clear;
- Failed Extraction.

Reward và progression phản ánh mức hoàn thành.

---

# 60. Silo Expansion Encounter

Mở rộng căn cứ dùng **cùng combat language** với expedition.

Ví dụ người chơi đào sang một phòng mới:

```
DEPTH -184 m

UNKNOWN CHAMBER
Door integrity: 63%
Internal motion: DETECTED
Signal quality: POOR
```

Người chơi chuẩn bị squad ngay trong Silo.

Sau khi phá cửa:

### Room 1
hai sinh vật.

### Room 2
turret cũ tự kích hoạt.

### Room 3
khí độc + một container quân sự.

### Core room
mini-boss / control terminal.

Sau khi clear:

```
SECTOR SECURED

Choose:
[Convert to Buildable Space]
[Restore Original Facility]
[Seal Sector]
```

Như vậy mỗi lần Silo lớn lên đều có khả năng tạo một câu chuyện nhỏ, thay vì chỉ:

> trả tài nguyên → chờ timer → có phòng mới.

---

# 61. Encounter variability

Cùng một location template không đồng nghĩa cùng encounter.

Ví dụ:

**Abandoned Warehouse — Medium**

Lần A:
- raider;
- ballistic weapon;
- food cache.

Lần B:
- infected;
- biological hazard;
- medicine.

Lần C:
- trống ở tầng đầu;
- alien organism ở basement;
- prototype component.

Game sinh encounter từ nhiều lớp:

```
LOCATION TYPE
    +
THREAT FAMILY
    +
THREAT VARIANT
    +
HAZARD
    +
ROOM MODIFIER
    +
LOOT TABLE
    +
RARE EVENT
```

Scout reveal một phần của các lớp trên.

Nhờ vậy người chơi học cách **đọc dấu hiệu và chuẩn bị**, nhưng không thể thuộc lòng toàn bộ map.

---

# 62. Revised combat fantasy

Một mission đúng tinh thần game có thể diễn ra như sau:

> Scout phát hiện một kho nghiên cứu có dấu hiệu năng lượng cao. Tôi đoán sẽ gặp robot nên mang hai Laser Rifle và một EMP. Ba phòng đầu đúng như dự đoán. Sang phòng bốn, squad gặp sinh vật có lớp vỏ hấp thụ năng lượng khiến một Assault gần như mất phần lớn hiệu quả. Tôi không thể đổi loadout giữa mission. Vanguard giữ aggro, Medic dùng Stim, Engineer chuyển sang SMG và Assault còn lại dùng ballistic sidearm để gánh. Tôi vẫn clear thêm hai phòng nhưng mất một unit và phải dùng Revival Injector cuối cùng. Radar báo phía dưới còn ba phòng chưa biết và có tín hiệu boss. Tôi đang mang loot tốt, không còn revive nên quyết định rút. Mission chỉ clear 6/9 phòng nhưng vẫn là một chuyến đi thành công.

Đây là trải nghiệm mục tiêu:

**chuẩn bị tốt giúp tăng cơ hội, nhưng không bao giờ xóa bất định; đội hình tốt giúp chịu được một phần sai lầm; người chơi giỏi biết khi nào phải rút.**


---

# 63. Weapon identity — khác nhau bằng damage profile, không chỉ DPS

Vũ khí không được thiết kế theo kiểu:

```
Rifle   20 damage
Laser   30 damage
Rocket  50 damage
```

Mỗi weapon class phải có **combat identity** riêng.

## Laser / Energy Rifle

Vai trò:

- single-target focus mạnh;
- accuracy tốt;
- sustained damage vào một mục tiêu;
- có thể hiệu quả với armor / shield tùy loại.

Điểm yếu:

- kém khi bị swarm;
- một số sinh vật / material có resistance năng lượng cao.

Ví dụ:

```
LASER RIFLE

Damage profile:
Single Target ++++
AOE            -
Fire rate      +++
Armor effect   ++

Special:
Focus Beam — càng giữ cùng target càng ổn định damage.
```

## Rocket Launcher / Bazooka

Vai trò:

- burst damage cao;
- AOE;
- rất mạnh khi nhiều enemy đứng cùng room.

Điểm yếu:

- reload chậm;
- overkill mục tiêu nhỏ;
- không nhất thiết tối ưu với một boss đơn lẻ.

```
ROCKET LAUNCHER

Damage profile:
Single Target  ++
AOE            +++++
Fire rate      -
Stagger        +++

Special:
Explosion hits nearby enemies.
```

## Shotgun

- close-range burst;
- cone / multi-target;
- mạnh với enemy áp sát;
- giảm hiệu quả ở khoảng cách xa.

## Assault Rifle

- general-purpose;
- damage ổn định;
- ít matchup tệ;
- lựa chọn an toàn khi intel kém.

## Sniper Rifle

- single-target burst cực cao;
- ưu tiên elite / boss;
- fire rate chậm;
- dễ bị swarm gây áp lực.

## Flamethrower

- AOE;
- damage-over-time;
- mạnh với swarm / biological target;
- có thể kém với robot / heat-resistant enemy.

## EMP / Disruptor

- raw damage thấp;
- mạnh với shield / robot / electronic system;
- stun / disable / vulnerability window.

Danh sách weapon class sẽ mở rộng sau, nhưng nguyên tắc phải giữ:

> **Vũ khí mạnh vì đúng tình huống, không phải vì luôn có con số damage lớn hơn.**

---

# 64. Soft counter — mang sai vũ khí vẫn phải gây damage

Do reconnaissance cố ý không hoàn hảo, game **không được hard-punish người chơi bằng immunity tràn lan**.

Nếu mang sai vũ khí:

- vẫn gây damage;
- damage bị giảm;
- effect có thể kém hiệu quả;
- kill time dài hơn;
- squad tiêu hao heal / revive / ammo nhiều hơn.

Ví dụ:

```
CRYSTAL BEAST

Laser Resistance:    70%
Ballistic Resistance:10%
Explosive Resistance:25%
```

Laser Rifle vẫn gây khoảng 30% damage cơ bản thay vì:

```
IMMUNE
0 DAMAGE
```

Hard immunity chỉ nên dành cho mechanic đặc biệt rất rõ ràng và hiếm.

Điều này bảo vệ triết lý:

> **Một char mang sai gear là weak link, không phải dead slot.**

Các thành viên khác vẫn có thể gánh team ở mức nhất định.

---

# 65. Damage effect phải thay đổi cách trận đánh diễn ra

Damage không chỉ là số HP bị trừ.

Các damage profile có thể tạo effect khác nhau:

### Energy
- focus;
- shield interaction;
- heat / overload.

### Ballistic
- reliable direct damage;
- armor penetration tùy ammunition;
- stagger nhẹ.

### Explosive
- AOE;
- stagger;
- phá cover / thiết bị;
- friendly-spacing pressure nếu sau này cần.

### Fire
- DOT;
- panic / area denial;
- mạnh với swarm.

### Electric / EMP
- disable;
- shield break;
- anti-robot.

### Chemical / Biological
- poison / corrosion;
- damage theo thời gian;
- hiệu quả theo physiology.

Không cần tất cả ngay ở MVP.

Prototype chỉ cần chứng minh rõ ít nhất:

1. **single-target weapon**;
2. **AOE weapon**;
3. **general-purpose weapon**;
4. **utility / anti-system weapon**.

Nếu bốn nhóm này đã khiến người chơi đổi đội hình theo target, hệ thống weapon đã đi đúng hướng.

---

# 66. Formation cho squad tối đa 5

Formation phải đủ để tạo chiến thuật nhưng không biến game thành tactical grid.

Gợi ý cơ bản:

```
          FRONT
          [ 1 ]

       [ 2 ] [ 3 ]

       [ 4 ] [ 5 ]
          BACK
```

Formation ảnh hưởng:

- aggro probability;
- melee exposure;
- protection;
- weapon range;
- target priority;
- một số skill / AOE.

Ví dụ:

- Vanguard ở front có khả năng giữ aggro;
- Shotgun muốn gần front;
- Assault linh hoạt mid;
- Medic / Sniper thường ở back;
- enemy flank hoặc ambush có thể làm backline bị đe dọa.

Formation không nên yêu cầu di chuyển từng ô.

Người chơi set trước trận và chỉ có một số thao tác đổi vị trí quan trọng trong combat.

---

# 67. Squad progression fantasy

Progression squad phải tạo cảm giác rõ ràng:

### Squad cap 3

> “Tôi không thể có tất cả. Tôi buộc phải hy sinh một vai trò.”

Ví dụ:

```
Vanguard + Assault + Medic
```

Không có Engineer → nhiều phòng kỹ thuật khó mở.

### Squad cap 4

> “Tôi bắt đầu xây được một team hoàn chỉnh.”

```
Vanguard + Assault + Engineer + Medic
```

### Squad cap 5

> “Tôi có slot cho specialization.”

```
Vanguard
Assault
Engineer
Medic
Heavy / Sniper / Scout / Specialist
```

Slot thứ 5 không đơn giản là +25% damage.

Nó mở ra khả năng mang một vai trò chuyên dụng mà trước đây người chơi không đủ chỗ.

Đây phải là một trong những milestone progression đáng nhớ của Silo.
