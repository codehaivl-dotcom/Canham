# BURROW ZERO — Survivor Recovery Contract v0.1

**Status:** Implementation baseline, tuning chưa validated. Owner of death, body, injury, rest và comeback rules. Canonical Rules đứng trên file này.

## 1. Lethal damage state machine

| From | Trigger | To | Consequence |
|---|---|---|---|
| ACTIVE | HP ≤ 0, chưa field-revive trong mission | DOWN | HP0, bất động, không bị target/DOT; bleedout60 simulation seconds |
| DOWN | Injector action hoàn thành trước bleedout | ACTIVE_TRAUMA | HP30%, Medic40%; field_revives_used=1 |
| DOWN | Bleedout hết hoặc successful extraction trước revive (convert body before escort validation) | DEAD_RECOVERABLE | Body tồn tại tới settlement; không tự hồi HP |
| ACTIVE_TRAUMA | HP ≤ 0 lần nữa | DEAD_RECOVERABLE | Không field revive lần hai |
| DEAD_RECOVERABLE | Body được chọn và successful extract | RECOVERED_BODY | Base recovery trong Clinic; chưa thể deploy/work |
| DEAD_RECOVERABLE/DOWN | Abandon body, extraction thất bại hoặc squad wipe | PERMANENT_DEATH | Roster memorial; equipped gear mất cùng body |
| ACTIVE | Capture objective đã telegraph, HP0 lần đầu | CAPTURED | Chỉ mission gắn capture tag; thay cho DOWN; tạo rescue node |
| CAPTURED | Rescue thành công trước expiry | RECOVERING | HP30%, Trauma, fatigue80 |
| CAPTURED | Rescue expiry12 active simulation hours | PERMANENT_DEATH | Xác nhận trên mission card; timer dừng khi world offline cap hết |

All normal mission cards use recoverable bodies; only explicit capture tag overrides first down. Failed/abandoned mission resolves permanent loss after any successful-extract check; no body can recover itself at MissionEnd. Prototype normal content không có corpse destruction, instant disintegration hoặc random capture. Capture chỉ áp dụng trên tagged Metro/NPC Silo mission, không tutorial. Damage không tiếp tục trừ body. Survivors được rescue là passenger, không tăng combat cap; cargo charge mô tả dưới.

Injector là action3 simulation seconds, cần actor ACTIVE trong cùng room; một action/actor; nhận damage không hủy, actor down thì hủy và item không consume. Reserve item lúc bắt đầu, consume atomically khi hoàn thành. Actor không tự revive; khi người cuối cùng down, squad wipe ngay sau khi toàn bộ cùng-tick events đã resolve, không chờ passive item. Hết combat không xóa bleedout; player có thể pause PvE để quyết định, thời gian thực không tự giết unit khi app đóng.

Ordering một tick: resolve damage/shield → mark HP0 → cancel invalid actions → complete remaining valid actions → evaluate phase/add triggers → evaluate wipe → settle objective/extraction. Một kill đồng thời với last survivor down vẫn là wipe; không grant first-clear reward nếu extract thất bại. Tutorial exception được xét trước wipe.

## 2. Bodies, passengers và gear

- Mỗi living squad member có thể escort1 DOWN/body/rescue passenger. Không thể escort nếu chính họ bị hạ; reassignment qua manifest trước extract, không teleport body từ room chưa tới.
- Body/DOWN dùng2 Cargo Units, rescued passenger dùng1. Body equipment được gắn trong2CU đó; không cộng thêm item load, không thể tháo gear của body trong mission. Bỏ field loot để nhường cargo được phép với preview rõ.
- Cargo cap không giảm vì casualty trong mission; giữ giá trị lúc deploy. Squad3 cap12 có2living thì tối đa escort2 body/passenger, vẫn phải đủCU.
- Normal exit cần ít nhất1ACTIVE; DOWN ở exit chuyển DEAD_RECOVERABLE và được tính body trước settlement. Player thấy rõ cảnh báo và lựa chọn revive trước khi extract.
- Successful extract giữ equipped gear của living và escorted bodies. Failed extract mất mọi field loot; living chỉ tồn tại nếu một exit đã successful, nên wipe/abandon không bảo toàn squad gear. Unused consumables theo owner; consume rồi không refund khi thua.
- Survivor/gear ownership chỉ chuyển trong settlement transaction của [Mission Session](MISSION_SESSION_REWARDS_V0.1.md).
- Offline defenders/site workers dùng PROTECTED_INJURED thay cho death; không tạo body, không mất gear, recovery base15min, miễn Chemicals. Người dùng không nhận lợi ích survival/cargo bằng cách gắn một attacker thành defender trong raid đang diễn ra.

## 3. Base recovery và injury service

ClinicL1 cần1MED worker,1powered bed/case; listed beds là parallel treatment slots. QueueFIFO, manual reorder không hoàn lại khoản đã consume. Price charged/reserved khi service bắt đầu; cancel trước bắt đầu refund100%, sau bắt đầu không refund nhưng giữ elapsed work cho lần resume. Không consume lại khi reload. Khi unpowered hoặc worker rời, pause, không reset. Recovery multipliers áp lên tốc độ, không duration; profession/traits áp một lần.

| Case | Base work minutes ở speed1 | Chemicals | Result |
|---|---:|---:|---|
| Routine HP recovery | 10 cho HP0→100%; tuyến tính | 0 | Restore HP, không xóa injury |
| Tutorial bruising | 3 | 0 | Xóa tutorial injury, full HP |
| Fracture | 15 | 2 | Xóa−10% effectiveAGI |
| Concussion | 12 | 2 | Xóa−10 percentage-point accuracy |
| Burn | 10 | 2 | Restore maxHP, clamp currentHP |
| Infection | 20 | 4 | Xóa Bio penalty |
| Trauma | 20 | 3 | Xóa−15%dmg/−10%attack speed |
| RECOVERED_BODY | 30 | 6 | ACTIVE HP30%, Trauma; không field-revive allowance cho mission cũ |

Medkit active action2simulation seconds, per-user cooldown5s starts at completed use, reserve/consume/cancel rules match Injector; healing cannot target DOWN/body. RECOVERED_BODY service cần ClinicL1, không cần Injector/research để tránh recovery gate vòng tròn. Rare Injector là lợi thế cứu ngay ngoài hiện trường và không cần mang body về; không hồi sinh người đã PERMANENT_DEATH. Một body được hồi tối đa1lần cho mỗi missionID và sau đó phải hoàn tất Trauma treatment mới redeploy được. Không có age expiry khi body đã về kho Clinic. Nhiều injuries xử lý theo queue trên cùng bed, cộng cost/work; routine HP recovery chạy cùng service và full sau khi mọi service hoàn thành. Normal injury roll: tại lần down đầu tiên, chọn1 Fracture/Concussion/Burn với equal weights; lưu outcome một lần. Infection chỉ từ encounter đã ghi Bio exposure, không random trên mọi hit. Ngoài down không roll heavy-damage injury trong prototype.

Nếu Clinic chưa mở hoặc thiếu Chemicals, Command emergency cot1slot xử lý body90min và Trauma60min miễn phí, chỉ tới khi có ít nhất3fit survivors (HP≥70%, fatigue≤80, không recovery-only state). Worker y tế mặc định automated; không cần survivor khỏe để phá deadlock. Result/limits giống Clinic, không nhanh hơn Clinic. Không thể thu tiền/salvage service; thao tác sống lại không cấp XP/reward.

## 4. Rest, morale, staffing

Fatigue scale0–100. Gain lúc settlement: Easy/Tiny–Small10, Medium20, Hard30, Extreme40; dùng difficulty trước size, không cộng chồng. Travel thuộc mission, không thêm gain riêng.

| Assignment | Fatigue recovery per real minute trong simulated window |
|---|---:|
| REST ở bed | 2 |
| Clinic active treatment | 1 |
| Silo job/Training/Research/site duty | 0 |
| Mission/travel | 0 |

Rest không cần power; thiếu bed vẫn REST ở cot với rate1, overcrowding morale vẫn áp dụng. Fatigue≤60 không penalty;60<fatigue≤80:−5%attack speed/work;>80:−10%attack speed và−10%weapon damage, không cộng penalty band trước, normal redeploy blocked. **Emergency** chỉ cho tagged rescue mission:80<fatigue<95, một lần/survivor/rolling24h, ghi warning, không bypass HP/injury/cargo/supply; fatigue≥95 không được deploy. Home emergency actions luôn available, không dùng Emergency flag này.

Morale natural return về60 ở rate1point/10min khi Food/Water>0; tăng không vượt60, giảm chỉ về60. Death penalty là temporary overlay riêng: Silo−3/squad additional−8/bond additional−10, tồn tại60 simulated minutes, tổng overlay floor−25; duplicate death eventID không áp lại. Positive event là+3 rescue/+3 successful extract, cap100, once/event. Không hidden morale drain khi offline window hết.

Room staffing: productionGenerator/Water/Hydro/Recycler tối đa1worker/room prototype. No worker output50%; worker output listed×efficiency. Life support miễn negative work modifiers do hunger/dehydration/morale/fatigue, floor1.00 worker multiplier khi staffed, vẫn giữ room integrity và power requirement; positive trait/stat bonuses cap1.35. Generator +20PU là infrastructure output, không giảm khi worker rời; worker bonus không tăngPU trong prototype. Living/Storage/Command/Battery/Gate automated, không yêu cầu worker. Workshop/Radio/Research/Clinic/Training cần1worker khi active;0worker pause action. Một survivor chỉ có1assignment; deploy removes họ khỏi job, trở về không tự đuổi replacement worker. RelevantStat=(primary+secondary)/2, không cộng hai stat; chỉ1primary thì dùng primary. Tutorial uses3staff+3deployed; roster table trong content pack.

## 5. Tutorial protection và roster comeback

Protected first mission/sector + mọi tutorial mission bắt đầu trong60 simulated play minutes đầu. HP0 → SAFE_DOWN, không bleedout/permadeath, không cargo/body cost. Sau encounter sống lại HP30%, tutorial bruising; nếu toàn squad SAFE_DOWN: emergency return, mất field loot chưa commit, Supply không refund, objective giữ retry. Protection đánh giá lúc mission bắt đầu, không biến mất giữa run. Outside protected content dùng normal rules, deploy card ghi rõ.

Nếu fit roster<3 hoặc tổng living<6: Command có applicant fallback queue10min, candidate fixed stats5all, civilian equipment Pistol/Jacket, free, tự assign starting role thiếu nếu cần. Mỗi lần chỉ1pending; cap cấp tới total living6 và đủ3fit (injured residents được nghỉ, không cho spam thêm nếu total≥6: dùng emergency cot). Không dismiss/sell/salvage fallback survivor hoặc transfer gear trong24h đầu, gear bound không salvage/trade. Mỗi slot refill có stable eventID, không RNG/reroll. Không hồi lại identity người đã chết; memorial giữ consequence.

## 6. Verification fixtures

- Squad3 có1death +2living,2CU body: extract thành công giữ gear/body; bỏ body xác nhận permanent loss.
- Revive một lần rồi down lần hai: field Injector disabled, body vẫn recoverable; không thể dùng reload reset counter.
- Fatigue81, REST bed30sec →80, đủ điều kiện normal redeploy nếu các điều kiện khác đạt.
- ClinicL1 Trauma20min; L2 speed1.2:16m40s trước worker modifiers. Worker rời tại10min rồi trở lại giữ10min work.
- Full wipe sau tutorial tạo permanent losses, nhưng Command fallback/cot vẫn có đường trở lại3fit; không cấp loot/XP vì wipe.

Các fixture là expected results. Runtime execution: NOT RUN.
