# BURROW ZERO — Audit độc lập tài liệu game

> Historical audit snapshot, not current readiness/sign-off. The 2026-11-12 remediation is tracked in [GAP_CLOSURE_2026-11-12.md](GAP_CLOSURE_2026-11-12.md); runtime tests remain NOT RUN.


- Ngày: 2026-11-12.
- Repository: https://github.com/codehaivl-dotcom/Canham
- Commit được audit: `2aa6a080f8a463bf931023af5a67e08f7f6cd4d7`.
- Phạm vi: tài liệu thiết kế và các tương tác giữa hệ thống; không phải audit code hay runtime QA.
- Phương pháp: review-all-gdds, đối chiếu canonical precedence, rà soát consistency và design holism, cộng một agent QA độc lập. Ba agent thực hiện các lượt rà soát riêng; kết quả được tổng hợp và kiểm tra lại.
- Không chạy combat simulation, không xác nhận balance, không chỉnh gameplay spec.

## Kết luận

**CONCERNS — đủ direction để làm prototype nhỏ; chưa đủ contract để triển khai và nghiệm thu vertical slice mà không phải tự suy diễn một số luật quan trọng.**

Không dùng ước lượng 94–96% trong audit cũ làm production gate: chưa có checklist và mẫu số đo được. Coverage hệ thống rộng không đồng nghĩa các tình huống giao nhau đã được định nghĩa đủ.

P1 bên dưới cần xử lý trước vertical slice tích hợp. P2 cần giải quyết trước milestone liên quan; không tự động chặn prototype core loop. Đây là mức ưu tiên sửa tài liệu, không phải severity của bug runtime đã tái hiện.

## Findings

### GAP-01 — P1: Death và body recovery chưa có state contract quyết định

**Bằng chứng:** [GDD §34](GAME_DESIGN_V0.1.md#34-injury--death), dòng 1397, chuyển HP0 thành DOWN/DEAD tùy encounter và sát thương; [Units §22](UNITS_ITEMS_V0.1.md#22-revival-injector), dòng 722–738, yêu cầu body recoverable và sau lần chết thứ hai phải extract body hoặc mất unit; [Loot §2](LOOT_CRAFTING_V0.1.md#2-loot-ownership), dòng 49, dẫn tới recovery rule của mission.

Chưa có predicate xác định Down/Dead/PermanentDeath, điều kiện body recoverable, ai mang body, chi phí cargo, tác dụng khi đưa body về và kết quả squad wipe. Đây là luật sở hữu survivor/gear, không chỉ numerical tuning.

**Đề xuất:** state table Alive → Down → DeadRecoverable → Recovered/Lost/PermanentDeath; điều kiện chuyển trạng thái, body/gear ownership và tutorial exception.

**Acceptance:** xác định duy nhất kết quả cho lethal hit, revive lần một, chết lần hai, extract body, bỏ body, squad wipe và tutorial protection.

### GAP-02 — P1: Recovery loop thiếu baseline vận hành

**Bằng chứng:** [Population §10](POPULATION_TRAITS_V0.1.md#10-fatigue), dòng 230–257, có fatigue gain 10/20/30–40 và redeploy restriction trên 80, nhưng chỉ nêu nơi Rest; [Buildings §12](SILO_BUILDINGS_V0.1.md#12-clinic), dòng 245–267, có relative heal speed nhưng thiếu base duration/cost cho injury/Trauma.

Chưa tính được nhịp rotate roster, thời điểm đội A chơi lại hoặc ảnh hưởng staffing sau expedition. Emergency redeploy cũng chưa có contract đủ rõ.

**Đề xuất:** prototype rest rate, treatment duration/cost, offline recovery, Clinic queue và hành vi khi full/unpowered; định nghĩa Emergency.

**Acceptance:** từ Fatigue81 có thể xác định thời điểm redeploy; kiểm tra hai short run rồi một failed run vẫn có next action khả thi, không cần premium aid.

### GAP-03 — P1: Tutorial gọi Scout trước bước sửa Radio

**Bằng chứng:** [Tutorial](TUTORIAL_FIRST_2H_V0.1.md), dòng 28 mở CCL3 trước expedition; dòng 88 và 131 dùng Quick Scout ở 15–25/35–50 phút; dòng 146–148 mới Repair Radio/Scout Center ở 50–65 phút. [Buildings §15](SILO_BUILDINGS_V0.1.md#15-radio--scout-center), dòng 336–340, đặt Scout trong chức năng Radio.

Unlock không tự xác nhận building đã repaired/operational. Audit v0.4 đã bổ sung unlock sequencing nhưng chưa diễn giải operational exception này.

**Đề xuất:** sửa basic Radio trước Scout đầu, hoặc ghi rõ portable/tutorial scouting; đổi mốc sau thành mở rộng range/search.

**Acceptance:** tài khoản mới đi đúng từng bước không cần debug unlock hay facility ngầm.

### GAP-04 — P1: Tiêu chí first-2h slice không đồng nhất

**Bằng chứng:** [Design Plan §6](DESIGN_PLAN.md#6-vertical-slice-target), dòng 187 và 196, yêu cầu squad3→4 và crafting/research; [Tutorial §1.1 và §14](TUTORIAL_FIRST_2H_V0.1.md), dòng 26–29 và 265–270, mô tả tới CCL4 và squad3 tại hai giờ. Canonical mở squad4/Research Lab ở CCL5.

Production và QA có thể tuân thủ hai checklist khác nhau và bất đồng về completion.

**Đề xuất:** tách tutorial hai giờ khỏi slice dài hơn, hoặc thêm milestone CCL5 rồi cập nhật cả hai checklist.

**Acceptance:** một manifest slice duy nhất ghi CCL cuối, squad cap, room/system phải playable và các mục được defer.

### GAP-05 — P1: Thiếu gameplay contract khi đóng game giữa mission/reward

**Bằng chứng:** [Loot §2](LOOT_CRAFTING_V0.1.md#2-loot-ownership), dòng 35–49, xác lập ownership sau successful extraction; [UI §11](UI_UX_NAVIGATION_V0.1.md#11-post-run), dòng 201–210, và [Reward §4](REWARD_REVEAL_CACHE_V0.1.md#4-reward-reveal-flow) mô tả happy path, chưa có suspend/resume/abandon và thời điểm roll/commit/claim.

Implementation có thể tự chọn hành vi gây reroll, duplicate hoặc mất reward khi quit/crash. Đây là thiếu hành vi người chơi thấy; không đòi chọn backend/database ngay.

**Đề xuất:** chốt pause/suspend hay abandon, hậu quả force-close, roll-once/claim-once và thời điểm reward thành permanent inventory.

**Acceptance:** force-close tại deploy, lethal hit, room clear, extraction, return, raw loot và từng cache card; mở lại không nhân reward, reroll hay mất reward đã commit.

### GAP-06 — P2: Emergency Core chưa đáp ứng đầy đủ fallback guarantee

**Bằng chứng:** [Buildings §4](SILO_BUILDINGS_V0.1.md#4-emergency-core), dòng 79–85, Core8PU được mô tả đủ tutorial life support và tránh soft-lock khi Generator offline. WaterL1 dùng4PU (dòng138), HydroL1 dùng5PU (dòng156), Command2PU (dòng618): Water+Food đã9PU; gồm Command là11PU.

**Scenario:** Generator offline, battery0, stockpile thấp. Không thể chạy đồng thời toàn bộ life support theo các load hiện tại. Stockpile hoặc luân phiên tải có thể cứu được, nên chưa chứng minh hard soft-lock.

**Đề xuất:** định nghĩa emergency subset/rotation, reduced loads/output hoặc đường phục hồi chắc chắn; sửa wording guarantee nếu chủ ý chỉ duy trì một phần.

**Acceptance:** scenario trên có đường phục hồi không cần premium hoặc squad combat-ready.

### GAP-07 — P2: Penalty thiếu nước có nguy cơ duy trì thiếu nước

**Bằng chứng:** [Economy §5](ECONOMY_RESOURCES_V0.1.md#5-population-consumption), dòng223–237: population10 cần12Water/h; WaterL1 tạo12/h. [§6](ECONOMY_RESOURCES_V0.1.md#6-hunger--dehydration), dòng262–278: Water0 sau1h gây production−25%. Nếu áp vào Water Treatment, output chỉ9/h so với demand12/h. Supply recipe cũng cần Food/Water.

Đây là failure scenario có điều kiện, không phải kết luận mọi account sẽ soft-lock. Upgrade, surplus và loot có thể phòng tránh; thiếu phần guarantee comeback khi các lựa chọn đó không khả dụng.

**Đề xuất:** chốt life-support exemption, rationing/manual emergency recovery hoặc comeback mission có thể thực hiện khi hết Supply.

**Acceptance:** depleted Water/Supply, roster injured và stockpile thấp vẫn có next action phục hồi khả thi; xác minh cách stack hunger/morale/fatigue penalties.

### GAP-08 — P2: Claim Beacon bắt buộc nhưng chưa có nguồn lấy

**Bằng chứng:** [Resource Sites §5 và §13](RESOURCE_SITES_V0.1.md), dòng74,81,275. Tìm toàn bộ repo chỉ thấy ba chỗ yêu cầu Claim Beacon, chưa có source/recipe/unlock.

**Đề xuất:** acquisition path, unlock, consumption timing và refund khi claim bị ngắt.

**Acceptance:** tài khoản CCL6 không PvP lấy được Beacon, clear và claim site đầu từ documented sources.

### GAP-09 — P2: Site contest chưa nối với PvP consent/protection

**Bằng chứng:** canonical site capture CCL6/PvP CCL8; [Resource Sites §12](RESOURCE_SITES_V0.1.md#12-contest-window), dòng248–251, chỉ nói eligible matchmaking region/band; [PvP Protection §5](PVP_MATCHMAKING_PROTECTION_V0.1.md#5-protection-states), dòng74–75, giữ new-player protection tới unlock + first voluntary action.

Chưa có expected result cho CCL6–7 site owner bị player raid, CCL8 chưa opt-in, hoặc neutral site sau khi claim.

**Đề xuất:** eligibility matrix cho Silo raid/site raid/PvE instance, CCL, consent, shield và revenge.

**Acceptance:** kiểm tra CCL6 owner, CCL8 chưa opt-in, first voluntary site attack và reclaim/revenge; không vô tình bắt PvE-only player vào PvP.

### GAP-10 — P2: Defender loss cap chưa có định nghĩa tính được

**Bằng chứng:** [Player Raid §10](PLAYER_PVP_RAID_V0.1.md#10-exposed-resources), dòng165–166, exposed pool10% common resources; [PvP Protection §11](PVP_MATCHMAKING_PROTECTION_V0.1.md#11-resource-exposure-rolling-loss-cap--settlement), dòng195, daily cap15% protected daily production equivalent.

Chưa định nghĩa production equivalent cho loot-based materials, per-resource hay aggregate, snapshot/reset rolling24h hay calendar, và reservation khi nhiều raid đồng thời.

**Đề xuất:** exposed/remaining cap theo resource, nguồn và thời điểm đo; reserve→commit→release cùng shield race policy.

**Acceptance:** hai attacker đồng thời không vượt aggregate cap; failed extraction và ngày rollover không tạo loot hoặc trừ tài nguyên sai.

### GAP-11 — P2: Defense squad progression mơ hồ

**Bằng chứng:** [Player Raid §8](PLAYER_PVP_RAID_V0.1.md#8-defense-squad), dòng124–126, ghi3 early/4 mid/5 late; [Security §5](SILO_DEFENSE_SECURITY_V0.1.md#5-defense-squad), dòng181–185, nói theo current standard squad cap. PvP unlock CCL8 đồng thời standard cap5.

Canonical không cấm defense cap nhỏ hơn5, nên đây là missing defense milestones giữa dedicated specs, không phải đã chứng minh standard cap sai.

**Đề xuất/acceptance:** một bảng defense cap theo CCL hoặc ghi rõ cap5 từ PvP unlock; first PvP có một expected cap duy nhất.

### GAP-12 — P2: Resistance floor và enemy data không khớp

**Bằng chứng:** [Units §8](UNITS_ITEMS_V0.1.md#8-damage-formula), dòng325, và Enemy contract ghi vulnerability floor−25%; [Enemy table](ENEMIES_RESISTANCES_V0.1.md), dòng529/559/890, có Electric−30%/−35%/−30%.

Implementation clamp floor cho Repair Drone nhận1.25× damage, giữ table nhận1.35×. Đây là baseline inconsistency độc lập với simulation chưa chạy.

**Đề xuất/acceptance:** ghi exception hoặc sửa data; một damage example và validation rule xác định cách xử lý.

### GAP-13 — P2/advisory: UI Research thiếu Engineering

**Bằng chứng:** [Research §4](RESEARCH_TECH_TREE_V0.1.md#4-branches), dòng61–69, có7 nhánh; [UI §13](UI_UX_NAVIGATION_V0.1.md#13-research), dòng237–244, chỉ liệt kê6, thiếu Engineering.

System spec thắng theo precedence, nên đây là stale UI contract. Bổ sung branch hoặc mô tả rõ merged display group để Power Management/Drone/Workshop research có destination.

### GAP-14 — Advisory: TierI site có nguy cơ khuyến khích check-in quá thường xuyên

**Bằng chứng:** [Resource Sites §8](RESOURCE_SITES_V0.1.md#8-storage-collection--overflow), dòng152–157, TierI buffer4h và collect thủ công tới later logistics; economy offline window8h.

Nếu full buffer dừng production, người chơi quay lại mỗi8h chỉ giữ được nửa output window. Đây là pacing hypothesis, không phải balance defect đã chứng minh; overflow rule cũng cần rõ.

**Đề xuất/acceptance:** định nghĩa overflow/collection cost và playtest1–2 session/ngày; cân nhắc buffer8h hoặc basic early collection nếu pacing không đạt.

## Các walkthrough liên hệ nhiều hệ thống

| Scenario | Chain được rà soát | GAP liên quan |
|---|---|---|
| First expedition | CCL unlock → Radio/Scout → deploy → return → Clinic | 02,03,04 |
| Lethal hit và retreat | HP0 → revive/body → cargo → extract → roster/gear | 01,05 |
| Blackout và thiếu nước | Generator offline → battery0 → shedding → starvation → Supply/counterplay | 06,07 |
| First site ownership | CCL6 → clear → Beacon → claim → PvP discovery/consent | 08,09 |
| Concurrent raid và return | exposed pool → reserve loss cap → combat/extract → reward commit/shield | 05,10,11 |

Các walkthrough là phân tích spec, không phải test runtime đã chạy. Không gắn PASS cho scenario chưa có expected behavior đủ rõ.

## Những gì không được tính thành lỗi

- Combat simulation chưa chạy: đã được cố ý defer. Không claim TTK/balance đã xác nhận.
- Final CCL costs, drop probabilities, monetization/pricing, platform order và backend topology: open decisions được ghi rõ.
- Không khẳng định tutorial chắc chắn thiếu Scrap: repair/restore cost và curated reward chưa đủ dữ liệu để tính như full build cost.
- Scout role +15% contribution so với +5% trong scout formula cần ví dụ stacking; chưa đủ bằng chứng để khẳng định trực tiếp contradiction.
- Không đòi hoàn thiện Coalition/seasons/live-world trước prototype core loop.

## Thứ tự xử lý đề xuất

1. Thống nhất tutorial và slice acceptance manifest; sửa Scout operational sequence.
2. Khóa death/body/gear recovery, fatigue/treatment và quit/resume/reward behavior.
3. Xác minh emergency power và comeback economy bằng scenario baseline.
4. Prototype Silo → prepare → expedition → combat → loot → extract → return → upgrade.
5. Trước Resource Site/PvP milestone: bổ sung Beacon, consent/protection matrix, defense cap và loss-cap transaction rules.
6. Sửa resistance contract, Engineering navigation; kiểm chứng site collection cadence qua playtest.

## Trạng thái bàn giao

Audit tài liệu hoàn tất; chưa QA sign-off runtime. Báo cáo được lưu sau khi người dùng đồng ý. Không tự sửa system specs, không đổi trạng thái systems index, không commit/push hay tạo issue ngoài repo local.
