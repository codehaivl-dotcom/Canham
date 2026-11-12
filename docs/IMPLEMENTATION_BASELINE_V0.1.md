# BURROW ZERO — Combat & Content Implementation Baseline v0.1

**Status:** Quyết định cho prototype; chưa có bằng chứng runtime, simulation hoặc playtest. Canonical Rules có ưu tiên cao nhất. Tài liệu này đóng các quy tắc vận hành, không tạo combat mode thứ hai.

## 1. Ownership

- Units & Items sở hữu stats, weapon tables và consumables; Enemies & Resistances sở hữu enemy archetypes và abilities.
- Silo Defense & Security §17 sở hữu giá xây, HP, Armor, damage, Alarm và tương tác của **installed player defenses**. Enemy Auto Turret không phải player Turret.
- Prototype Research Catalog sở hữu research IDs, gates, giá, thời gian và research effects. Giá lắp defense vẫn lấy từ Security; không cộng hai bảng giá.
- Survivor Recovery sở hữu death, injury, bleedout, treatment và assignment. Mission Session sở hữu save, extraction transaction và reward ownership.

## 2. Control, formation và timing

Grid có một Front slot, hai Mid slots và hai Back slots. Chọn đúng 3/4/5 survivors theo cap, đặt vào bất kỳ legal slots nào nhưng phải có một living survivor ở Front lúc departure. Đội tutorial: Vanguard Front, Assault Mid, Medic Back. Không bắt squad 3 bỏ Back trống.

Formation cố định trong mission. Death không tự đổi vị trí giữa room. Trước room tiếp theo, nếu Front trống thì promote living survivor có HP cao nhất, hòa theo stable survivor ID. Không đổi cargo cap hoặc revive allowance.

Prototype dùng autoattacks, manual focus và manual consumables. Active abilities, manual reposition giữa combat và dodge minigame tắt. Role bonuses là passive. PvE pause dừng mission attack/action/bleedout clocks, không dừng background Silo; PvP không pause.

Simulation step cố định **0.1 second**. Attack đầu sẵn sàng sau một interval khi vào room. Attack-speed factor chia interval, mỗi modifier áp một lần, factor cuối clamp `[0.5, 2.0]`. Damage cùng tick resolve theo batch; log dùng stable entity ID. Wipe/action ordering theo Survivor Recovery. Projectile là presentation, damage ở scheduled impact tick, không roll thêm theo frame rate.

Allied AI chọn manual focus còn hợp lệ; nếu không, chọn enemy revealed/reachable có current HP thấp nhất, hòa theo stable ID. Không auto consumables. Enemy priorities theo Enemy §21; aggro weights chỉ áp giữa eligible targets, không hủy Assassin leap đã khai báo.

### Slot geometry

Ranged attacks có thể nhắm mọi opposing slot đã reveal trong room. Slice không có cover/line-of-sight bonus bằng NavMesh. Geometry dùng slot graph, không khoảng cách pixel. Front nối hai Mid; mỗi Mid nối Back cùng cột; hai slots cùng hàng là neighbors. Swarm subslots được authored trong cùng hàng, xếp theo stable index.

| Attack | Target selection | Damage profile |
|---|---|---|
| Shotgun | Primary + tối đa hai enemy cùng hàng, gần primary theo slot index | 100/45/25% |
| Rocket | Primary + tối đa ba enemy cùng group hoặc neighboring slot; sort graph distance rồi stable ID | 100/60/45/30% |
| Flame | Primary + tối đa hai enemy cùng hàng | 100/60/60% |
| Frag | Cùng eligibility graph như Rocket | Primary55 Explosive; secondary60/45/30%; COM-03 chỉ tăng secondary |

Không friendly fire hoặc hit hai lần cùng target. Sniper Back Accuracy +5 percentage points chỉ áp **một lần**, dù được nhắc ở Formation và weapon identity. Close-range pressure: -10 percentage points Accuracy khi một melee enemy đang nhắm Sniper; bỏ khi điều kiện không còn. Front penalty là field riêng, không tự thêm một penalty khác chưa khai báo.

## 3. Hit, shield và status effects

Weapon intervals không tạo ammo stockpile hoặc reload resource riêng. Assault cycle bonus sửa interval một lần.

```text
Accuracy = clamp(Weapon + PER bonus + Formation + Trait + Status, 55%, 98%)
ArmorMultiplier = 120 / (Armor + 120), Armor >= 0
Resistance = clamp(sum(applicable modifiers), -25%, 80%)
```

Hit/crit outcome lưu một lần/event. Crit ×1.5 áp direct damage, không DOT. Round final direct damage tới0.01; floor1 chỉ sau hit hợp lệ, không biến miss/untargetable thành damage. Ballistic/direct physical dùng ArmorMultiplier; Energy/Fire/Electric/Bio bỏ generic Armor, dùng resistance. Explosive dùng Armor/2 rồi resistance. Mixed damage phải khai báo tỷ lệ trước mitigation.

Repair Drone Electric resistance là -25%: raw100 Electric, không Armor, nhận125 damage; không ngoại lệ -35%. Shield nhận post-mitigation damage trước; overflow vào HP cùng tick, không áp resistance hai lần. Chỉ ability ghi rõ mới hồi shield. Shield break event một lần/depletion cycle.

| Effect | Stack/timing |
|---|---|
| Burn | 3 raw Fire/second trong4seconds; tick1second; refresh duration, strongest instance; không hidden DOT minimum |
| Corrode | -10 Armor trong6seconds; refresh, không stack, Armor không dưới0 |
| Poison/Bio | 4 raw Bio/second trong6seconds; refresh; Antidote xóa; không tick mission khi offline |
| EMP buildup | Rifle hit+1; Mechanical threshold3, shielded organic4; organic không shield không tích; reset sau Disable; không decay cùng room |
| EMP Disable | Rifle2.5seconds, grenade3seconds, Sentry Drone grenade4seconds; Tech/Engineer modifiers một lần; boss×0.40; repeat cùng CC trong8seconds duration×0.5, minimum0.1second |
| Stagger | Base0.5second, boss×0.35; postpone ready attack; repeat cùng CC trong8seconds duration×0.5 |
| Fear | Resolve success `clamp(0.5 + (RES - 5) × 0.05, 0.25, 0.90)`; fail -15% attack speed5seconds; refresh, không stack |
| Smoke | Enemy Accuracy -20 percentage points8seconds, obey floor, strongest only |

EMP/Stagger dùng `max(existingEnd, newEnd)`, không cộng durations. Shared action lock tối đa4seconds liên tục, sau đó2seconds CC immunity, kể cả boss. Shield-break vulnerability không phải Disable và không bỏ qua CC immunity. Room change xóa transient status/buildup, giữ injury/Trauma. HP, consumed items, shield charges và revive allowance không reset mỗi room. Living Armor không heal corpses.

Boss details: Hive Mother Phase2 spawn1Spitter+1Crawler mỗi18seconds, lần đầu18seconds sau chuyển phase; zone4Bio/second trong6seconds mỗi12seconds. Phase3 Slam35Ballistic vàoFront/Mid mỗi8seconds. War Machine cannon28Ballistic mỗi second, Repair Drone spawn một lần tại75%HP, hazard6Fire mỗi living unit/10seconds dưới35%HP. Fallen Visitor ở50%HP spawn2Stalkers và Shield250 một lần; mỗi20seconds đo actual direct+DOT damage của20seconds trước, hòa theo damage-type ID; secondary type dùng persisted RNG. Clamp adaptive resistance sau mỗi thay đổi.

Tối đa6active enemies ở room thường,8ở authored swarm/boss adds; mỗi boss tối đa3spawn waves. Spawn vượt cap bị bỏ, không backlog. TTK/HP-loss targets vẫn chưa simulation.

Consumable actions ngoài Medkit/Injector mất1second; mỗi actor chỉ có một action và shared2seconds cooldown sau completion. Medkit/Injector duration theo Units/Recovery, không dùng một duration thứ hai. Reserve stack lúc bắt đầu; cancel trước completion trả reservation, completion consume một lần và không refund. Unused consumables chỉ return một lần khi owner sống hoặc body được escort; theo Mission Session/Recovery receipt. Optional Durability và Secure Data Case **OFF** trong first slice; không automatic repair fee.

## 4. XP và Training

Chỉ successful extraction bank XP: mỗi cleared normal combat room20; elite40 **thay**20; boss100 **thay**20/40; completed mission objective thêm40 một lần. Room không encounter không mint combat XP. Living và recovered-body survivors trong deployed roster nhận bằng nhau; captured/permadead nhận0. Partial extract tính rooms thực sự clear. Stable room XP IDs ngăn retry trả lại XP của cùng persistent attempt.

```text
Cumulative XP for Level L = 25 × (L - 1) × L
Level2 = 50; Level3 = 150; cap50
```

Mỗi level tăng Max HP5 và Current HP5 nếu living, không revive. Settlement xử lý nhiều levels trong một loop, reward một lần/level ID. Mỗi5levels có1stat point; tại10/20/30/40 còn có1role perk. Base stats cap10. Không XP từ repair/recharge/revive/failed run/repeated claim.

Training cần một worker và một trainee khác nhau; L1 hai slots đủ cho hai người. Role assignment5minutes, miễn phí prototype; hoàn thành mới bỏ role cũ. Không queue khi deployed, defense-reserved hoặc recovering. Nam học Engineer trong extended slice không phát sinh hidden Scrap fee. Stat allocation instant bằng earned points, max10; respec1minute miễn phí, không tạo points. Không offline combat XP.

Mỗi role có ba perk examples hiện có; không chọn lại perk. Choice thứ tư level40 là **Steady Resolve**: +5 percentage points Resolve-check success, cap95%, không thêm damage. Đổi role giữ earned selections nhưng chỉ current-role perks hoạt động; respec giữ nguyên earned count.

## 5. Crafting, gear và NPC trade

Workshop recipes hiện có vẫn authoritative; research extensions dùng Research Catalog. Modifier cần matching slot trống, không có reroll recipe. Named example weapon dùng explicit item stats; không nhân Tier budget lần nữa. Generic unnamed weapon dùng base weapon table và đúng một Tier multiplier.

Salvage round từng recovered material xuống số nguyên, không trả blueprint/RD/progression token. Prototype rare-component roll5% cho1Component, outcome lưu lúc reserve; tổng recovery không vượt original recipe inputs. Artifact dùng unique research/salvage path.

| Item | NPC mua từ player | NPC bán cho player |
|---|---:|---:|
| Civilian Pistol | 10 Credits | 40 Credits |
| Rifle | 30 Credits | 120 Credits |
| Medkit | 3 Credits | 12 Credits |
| Frag | 4 Credits | 18 Credits |

NPC mua Scrap1Credit/unit, Components2, Chemicals2; không mua strategic/key/bound gear. Shared account stock mỗi rolling24hours:10Medkits,5Frags,2Pistols,1Rifle. Faction stores không nhân stock limits. Không mua strategic progression trực tiếp bằng Credits. Buy/sell/refund/salvage không được sinh input value; đây là invariant cần test, chưa phải kết quả simulation.

Blueprint requirements giữ Standard3/Advanced5/Prototype8/Alien8+research/Artifact12+key. Tutorial2fragments + Hospital thứ ba mở Standard. Bỏ Hospital thì Warehouse follow-up cung cấp fragment thứ ba qua shared one-time ID `BP-SLICE-03`; quay lại Hospital không nhận thêm cùng reward. Pistol/Combat Armor recipes không cần Blueprint, M-4 cần Standard Weapon Blueprint. Military Authorization là key riêng.

## 6. Normal loot authoring

Chỉ bật archetype có authored graph và reward table. Content chưa làm phải unavailable/milestone, không random placeholder cho mandatory source. Seeded loot dùng source+version. Roll count uniform inclusive trong Loot§6 difficulty band. Common stack amount uniform: Easy8–15, Medium12–20, Hard18–28, Extreme24–36. Mỗi resource100units/CU, combine trước kiểm tra cargo.

| Archetype | Scrap | Components | Chemicals | Food/Water | Data | Gear/Consumable | Fragment |
|---|---:|---:|---:|---:|---:|---:|---:|
| House |30|10|10|30|0|18|2|
| Warehouse |35|30|10|10|5|8|2|
| Hospital |10|10|35|10|15|18|2|
| Depot |15|25|5|0|15|30|10|
| Lab |10|20|15|0|30|15|10|
| Metro |25|15|15|20|10|12|3|
| NPC Silo |20|20|10|0|20|20|10|

Mỗi row tổng100, một category/roll. Food/Water split50/50. Gear/Consumable subpool: Medkit40%, Frag20%, Pistol20%, Rifle20%; lọc options hợp lệ rồi normalize. Data quantity theo difficulty1/2/3/4. Fragment roll cấp1fragment, không full blueprint; enemy kill không mint thêm Credits ngoài budget.

Generic Tier ceiling: CCL1–2 Civilian;3–4 Industrial;5–6 Military;7–8 Advanced;9 Prototype;10+ Alien. Source phải cho phép Tier đó; ceiling không biến House thành Alien source. Rare-flex5% tăng một Tier trong legal source pool, không vượt ceiling, không Artifact. First slice không có random Alien/Artifact table. Authored story/tutorial rewards là explicit named exceptions.

Pity: mỗi3successful named-archetype objective clears liên tiếp không bank fragment sẽ cấp1matching-family fragment tại settlement thứ ba. Counter account+family; reset khi bank fragment. Boss guaranteed fragment không thêm một pity increment thứ hai. Failure không tăng counter. Odds này là prototype baseline.

Normal five-card cache: material roll; Medkit/Frag50/50; Credits30 hoặc Data2 theo source (Data nếu source Data weight>0); gear/material50/50; fragment1. Military/NPC family Standard dướiCCL9, Prototype từCCL9; Lab Advanced từCCL5, Alien từCCL10. Material card chỉ roll material categories hợp lệ, normalize weights. Gear card dùng Pistol/Rifle50/50 sau gate filter. Persist outcomes khi tạo cache, không lúc mở animation. Tutorial caches dùng đúng explicit cards, không cộng weighted roll.

## 7. Validation, Alarm và telemetry

Validator kiểm tra `entry → primary objective → exit` với actual declared loadout. Không mandatory Engineer/Beacon/key trừ key guaranteed ở node reachable trước cửa. Graph fail dùng authored fallback cùng archetype, không charge deployment lần nữa. Validate power-off, fail-closed door, lockdown và maximum encounter state. NPC raid luôn có unpowered manual exit. Boss budget override normal TC nhưng giữ entity cap.

NPC09 Alarm increments/doors ở Campaign Contracts§2.1; installed Sensor/Relay/Trap stats ở Security§17. Research unlock hoặc sửa đúng field, không cộng hai bản sao. Nếu copied table khác owner, sửa copy trước implementation.

Minimum events: `tutorial_step_complete`, `assignment_changed`, `deploy_accepted`, `room_complete`, `unit_down`, `field_revive`, `body_extract`, `mission_settled`, `return_inbox_claim`, `research_complete`, `site_claim`, `pvp_consent`, `raid_reserved`, `raid_settled`.

Payload: opaque account/mission/event ID, content version, simulation time, mode, CCL, step/result/reason, resource delta; không raw chat/name/location. Telemetry opt-out không phá save/grant. Event IDs chống đếm hai lần. Playtest xem tutorial completion, extract/abandon, recovery wait, loadout variation và PvP cap rejections; không bịa retention percentages.

**Runtime QA, simulation và playtest: NOT RUN.** Fixtures là expected behavior, không evidence đã pass.

