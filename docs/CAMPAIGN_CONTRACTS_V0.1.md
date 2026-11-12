# BURROW ZERO — Campaign & Guaranteed Contract Catalog v0.1

**Status:** Prototype authoring baseline. VI/EN display strings và objective data; không phải final voiced scripts hoặc completed levels. Không main-story PvP/Alliance gate. Source không được yêu cầu item do chính reward của nó mới mở.

## 1. Chapter progression

Chapter mở khi previous chapter complete và đạt minimum CCL. CCL prerequisites không phụ thuộc một chapter unlock chưa reachable. Discovery làm sớm có thể credit completion flag khi chapter mở; reward chỉ trả một lần. Main-story nodes persistent/private, không expire hoặc chuyển thành PvP.

**CH02 có hai transaction stages riêng:** sau Warehouse manifest và Hospital P3 medical manifest + P4 data bundle (hoặc Warehouse side-office alternative), successful extraction lập tức bank `SLICE-ARCHIVE-01`: **200 Scrap, 80 Components, 10 Research Data**. Không đợi CCL5, không đợi CH02 completion. Sau đó dùng tài nguyên để nâng CCL5; reaching CCL5 mới complete CH02 và reveal Depot signal, **không trả archive reward lần hai**. Nếu đã claim sớm qua content pack, chapter chỉ đọc shared receipt. Inbox overflow theo Mission Session.

| ID / minimum CCL | VI / EN title | Completion predicate | Reward / next signal |
|---|---|---|---|
| CH00 Wake /1 | Đánh thức căn hầm / Wake the Silo | Generator, Water, Living restored; first sector clear; Hydro built | Mở tutorial CCL2/3 actions; không thêm tài nguyên ngoài content ledger |
| CH01 FirstSignal /3 | Ánh đèn trong bếp / A Light in the Kitchen | Rescue Tùng và successful House extraction | Cùng HSE cache/roster receipt, không second pool; mở Warehouse contract |
| CH02 SurfaceRemembers /4 | Những ký ức trên mặt đất / The Surface Remembers | Archive-stage receipt đã bank và đạt CCL5 | Archive reward trả **trước CCL5** như mô tả trên; completion chỉ reveal Depot Relay |
| CH03 Silo09 /7 | Tín hiệu thứ chín / The Ninth Signal | NPC09 Armory terminal + extraction; Command optional cho chapter | Credits150, Combat Data5, Military Data3 một lần; Command objective vẫn cần cho CCL8 |
| CH04 LinesInDust /7 | Những đường ranh / Lines in the Dust | Một available faction intro + claim private PvE site | Credits100, Research Data10 một lần; reputation intro, không currency mới |
| CH05 Visitor /9 | Vị khách lạ / The Visitor | Curated Mimic investigation + Fallen Visitor kill/extract | Neural Core1 và Alien Material2 là **cùng boss-node receipt**, không thêm bản sao; first sample dạy Exposure |
| CH06 OpenNetwork /10 | Mạng lưới mở / Open Network | Repair network terminal trong NPC09 follow-up; có thể chọn Remain PvE | Combat Data10, Credits200; không cần attack hoặc PvP opt-in |
| CH07 BelowZero /10 | Dưới mức không / Below Zero | DEEP-ARCHIVE-01 clear + đọc Architect log | Architect Archive1 từ **cùng node receipt**, mở CCL11 route |
| CH08 FarBeyond /11 | Vươn xa / Far Beyond | Chọn Network/Hybrid/Isolation/Coalition flavor rồi complete private relay | Credits300, Research Data30, cosmetic title Far Beyond; Archive thứ hai từ repeat DEEP-ARCHIVE-01 cho CCL12 |

CH05 ở CCL9, trước Xenobiology CCL10: Visitor loot và curated investigation dùng Clinic, manual clues và quarantine, không yêu cầu Xeno Lab hoặc Bio Scanner. CH06 giới thiệu fiction PvP sau mechanical unlock CCL8; PvP screen có thể mở sớm hơn chapter nhưng không ép chapter progression. Resource Sites mở CCL6; CH04 chỉ dạy feature đã có. NPC09 deployment cần CCL7 + Radio L3 range25km; passive 18.4km hook đầu session chỉ read-only.

## 2. Repeatable progression encounters

Named contract nodes đều private, xuất hiện ngay khi đạt gate. Refresh6simulated hours sau completed objective + extraction. Failure giữ node/objective available; token đã nhặt ngoài field nhưng mất do failure có thể lấy lại đúng một lần ở retry. Không cộng dồn hai token trong cùng attempt. Token ownership, first-clear và rewards commit ở extraction; không lấy qua cache RNG. First-clear bonus không được liệt kê nghĩa là không có bonus ẩn.

| Node / gate / distance / difficulty | Authored graph và enemies | Guaranteed reward sau objective + extraction |
|---|---|---|
| DEP-RELAY-01 /CCL5 /6km /Medium /squad4 | Entry → 2 Riflemen → Security Bot + manual switch → Terminal → Exit; một optional Supply room; cleared return path luôn mở | Military Authorization1, Military Data2, Research Data4, Scrap30, Components15 |
| HSP-LOWERNEST-01 /CCL6 /6km /Medium /squad4 | Entry → 3 Crawlers → Spitter + Mutated Brute → safe exit branch → Hive Mother | Hive Chitin Core1, Bio Sample1, Research Data5, Standard fragment1 |
| NPC09 /CCL7 /18.4km /Medium /squad4 | Entry → Security **hoặc** Maintenance → Power → Armory → optional Command; room details ở §2.1 | Armory terminal credit CH03; Command + extract credit CCL8; Scrap40, Components20 mỗi completed primary objective; chapter reward riêng một lần |
| FACTORY-A17 /CCL8 /10km /Hard /squad5 | Entry → Sentry Drone + Security Bot → Repair Drone + 2 Riflemen → cleared safe exit → War Machine A-17 | **Military AI Core1, Prototype Core1 và Prototype fragment1 guaranteed**, Components25; Prototype Core không phải rare roll |
| DEEP-VISITOR-01 /CCL9 /12km /Hard /squad5 | Entry → Crystal Beast → 2 Stalkers → readable vent switch → Fallen Visitor; manual exit không khóa | Neural Core1, Alien Material2, Alien Sample1, Advanced fragment1 |
| DEEP-ARCHIVE-01 /CCL10 /internal depth-11 /Hard /squad5 | Security Bot + Sentry Drone /2 Security Bots /Warden Mech; sau đó manual archive terminal; có Seal trước entry | Architect Archive1, Research Data12, Alien Material1 |
| SURFACE-RELAY-01 /CCL11 /15km /Hard /squad5 | Entry → Raider Hard package TC19 → 2 Stalkers + Void Caster → restore relay → exit | CH08 reward; không cần Coalition membership, Artifact gear hoặc exclusive faction tech |

Internal archive Supply =2 + squad5 + Hard2 =9, không distance surcharge. First story-door access curated, không thêm excavation gate. Boss stats dùng Enemy baseline và difficulty multiplier đúng một lần, **chưa balance verified**. Retry không refund Supply/consumables hoặc reset lethal outcome đã commit. Scout không refresh world-node version.

Mọi key trên đều có source trước CCL gate: Authorization ở5 cho6; Hive Core ở6 cho7; NPC09 Command ở7 cho8; Military AI Core ở8 cho9; Neural Core ở9 cho10; Archive ở10 cho11/12. Prototype Core ở8 có trước `ENG-05` CCL9. First Alien Sample/Material ở9 có trước `XEN-01` CCL10. Artifact fragment cho `XEN-05` nằm ở private CCL10 Archive follow-up: đọc secondary historical panel sau terminal, guaranteed1 fragment khi successful extract, shared one-time ID `ART-DISCOVERY-01`; không cần Artifact research để đọc panel. Fragment này không thay Architect Archive key.

## 2.1 NPC09 — Alarm, doors và exit

Đây là authored compact tutorial exception cho generic NPC Silo10–20rooms; các sectors không được nêu không tự sinh thêm encounters/rewards.

- **Entry:** safe return exit, luôn manual/unpowered, không có lock.
- **Security branch:** 2 Riflemen và một Sensor Node. Có thể fight/breach; không cần Engineer. Sensor là installed-device baseline trong Security§17.
- **Maintenance branch:** không combat; manual camera switch10seconds tắt Sensor trước khi kích hoạt. Engineer làm6seconds chia Tech Effect. Branch này dẫn tới cùng Power room; không cần item.
- **Power:** một Security Bot; sau clear có manual disconnect10seconds. Cắt main power tắt Sensor và electronic defenses; Alarm giảm10 một lần. Không tạo loot mới. Đường về Entry không phụ thuộc power.
- **Armory:** 2 Riflemen +1 Marksman; terminal là CH03 objective. Mở emergency shaft bằng manual lever5seconds, không cần Beacon/Engineer/key. Shaft là one-way safe exit tới return flow.
- **Command:** Tech Raider + Breacher; optional trước khi player chọn Command objective. Đọc terminal hoàn thành CCL8 prerequisite sau extract. Command nối về Armory; không auto-lock đường về.

Alarm bắt đầu0, clamp0–100, lưu cùng mission. Các increments dưới đây là event một lần, không charge per projectile:

| Event | Alarm change |
|---|---:|
| Bắt đầu một combat encounter sau detection | +10 một lần/room |
| Sensor phát hiện entry | Theo Security§17: +10 một lần/room; Relay nếu được authored thêm+5, không nhân theo số hit |
| Rocket/Frag hoặc explosive breach | +5/action; action ID ngăn replay grant |
| Door bị phá bởi damage | +10 một lần/door |
| Hack bị interrupt bởi damage/stagger | +5/interrupted attempt; manual switch không có random failure |
| Thời gian sau detection | +2 mỗi10active simulation seconds; pause/app close không tick mission |
| Tắt main power | -10 một lần |
| Tắt Alarm terminal | -15 một lần và dừng time gain30seconds; manual20seconds hoặc Engineer6seconds/Tech Effect |

Alarm terminal reachable tại Maintenance hoặc Armory; không nằm sau locked research. Delay reduction không reset reinforcement flags. At25 guards biết target; không tạo thêm enemy. At50 optional Armory side-store door khóa nhưng manual release10seconds hoặc breach HP100/Armor20 luôn có; không khóa primary terminal/exit. Door MkI defaults fail-open khi mất power. Authored Command fail-closed door vẫn breachable/hackable theo Security; không có invulnerable powered lock.

At75 spawn đúng một response wave gồm2 Riflemen +1 Breacher, khi còn đủ active-entity cap; nếu không đủ thì đợi các enemy hiện tại bị hạ, không mint nhiều waves khi Alarm lên/xuống. At100 activate một Warden Mech đúng một lần nếu còn capacity; bắt đầu pressure120active simulation seconds. Trước khi push, UI báo response/pressure và marker đường thoát. Hết pressure đóng **optional Command access**, không đóng Entry/shaft, không tự giết squad hoặc confiscate loot. Objective đã đọc vẫn credit nếu extract thành công. Alarm không biến partial extraction thành failure.

Validator kiểm tra entry→objective→exit ở power-on, power-off, Alarm50/75/100 và pressure expired. Thiếu Engineer hoặc Beacon không làm graph invalid. Pause tuân Mission Session; reinforcement/door flags persist khi reconnect. Combat entity stats dùng Enemy; installed devices dùng Security§17; research chỉ thay field được catalog cho phép.

## 3. Faction intro contracts and reputation

CH04 chọn một trong bốn base-faction intros; Ascendants chỉ available từCCL9. Không permanent faction lock. Reputation start0, clamp-100..100. Intro+20 matching faction; normal contract+10; explicit rival conflict-10 chỉ khi preview. Intro reward một lần100Credits/5RD; repeat40Credits/2RD/+5reputation mỗi6simulated hours. Không đồng thời cộng normal+10 và repeat+5 cho cùng completion.

Intro nodes dùng5km, Medium, squad4 và ba existing rooms; mỗi room tối đa2Riflemen+1Breacher. Recovery contract có peaceful manual-terminal option. Rewards là system grants, không phải dùng Credits mua strategic material.

| Faction / ID | VI / EN title | Objective | Source unlocked |
|---|---|---|---|
| Continuity /FAC-DOOR-01 | Kiểm tra cửa chắn / Door Audit | Inspect3security doors, reset manual terminal, extract | Trusted20 → Security Protocol |
| Free Settlements /FAC-RELIEF-01 | Chuyến hàng chung / Shared Supplies | Recover trade ledger; không donate Food/Water giữa crisis | Trusted20 → NPC applicant100Credits, fixed preview candidate,1/24hours; emergency fallback vẫn miễn phí |
| Earthborn /FAC-SURVEY-01 | Lối đi an toàn / Safe Passage | Scan2route beacons; hazard-free alternative exit | Trusted20 → Surface Conditioning |
| Archivists /FAC-ARCHIVE-01 | Những trang còn lại / Remaining Pages | Recover Data Center record + extract | Trusted20 → Archive Compression |
| Ascendants /FAC-ALIEN-01 | Ngôn ngữ lạ / A Strange Language | CCL9+, manual translation terminal; không cần Interface | Trusted20 vàCCL10 → Hybrid Interface research |

Không faction tokens trong prototype. Stable store: Medkit12Credits, Frag18, cosmetic banner200; basic-item stock dùng chung account limits của Implementation Baseline, không farm bằng đổi shop. Hostility recovery qua neutral mediator luôn available: private House objective, cost0Credits,6h cooldown,+20reputation. Không irreversible hostility trap.

## 4. Curated Mimic and Alien Exposure

`MIM-TUT-01` là private one-time CH05 event, không random thay favorite survivor. Một visitor mới tự vào quarantine và chưa thuộc owned roster. Ba guaranteed clues: inconsistent medical scan (Clinic hoặc free manual cot), radio echo (manual terminal), memory mismatch (interview). Mỗi action30seconds, tutorial cost0. Hai clues mở Expose. Encounter là3Crawler-equivalent Mimics, dùng Crawler stats/resistance và alien visual; exit/quarantine controls luôn available.

Innocent branch là explicit alternate debug fixture, không reroll sau khi clues đã lưu. Quarantine innocent gây-3Morale trong30simulated minutes, không injury/death. Completion5Research Data một lần. Không exclusive survivor power.

Exposure là existing account state0–100, start0, không currency. Gear có explicit research-item value dùng đúng value đó: Adaptive Hazmat/Neural Interface+5 mỗi deployment; Hybrid Interface+8 **thay**5; analysis+1 mỗi action. Không cộng generic Alien+5 lần hai cho cùng item. Gear Alien chưa có explicit override dùng+5/item/deployment. Không tăng chỉ vì equipped offline.

Bands:0–24none;25–49clue warning;50–74next eligible procedural Mimic chance5%;75–100chance10%. Tối đa1procedural event/rolling24hours, chỉ sau curated intro. Roll lúc mission return, không reconnect. High Exposure có thể reveal optional discovery nhưng không mandatory CCL gate. Command Detox20minutes/2Chemicals giảm10Exposure, queue1, repeatable. Khi toàn bộ Alien gear unequipped và survivors REST, passive giảm1/10simulated minutes. Không offline permadeath hoặc silent replacement; từ chối visitor không stall story hay xóa roster.

## 5. Presentation and readiness

Dùng stable localization keys như `chapter.ch01.title` và `contract.dep_relay_01.objective`. VI/EN strings là source copy, không baked art. Một radio line dùng lại:

- VI: “Chúng tôi vẫn ở đây. Đừng mở cánh cửa dưới cùng.”
- EN: “We are still here. Do not open the lowest door.”

Short text + radio treatment, không cần bilingual voice acting. Đây là authoring fixtures và source guarantees, chưa phải completed levels/assets. Faction/late campaign sau core slice; Season/Coalition full content và commercial decisions là milestones riêng.

**Runtime QA, simulation và playtest: NOT RUN.**

