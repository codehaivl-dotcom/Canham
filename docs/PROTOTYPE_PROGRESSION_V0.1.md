# BURROW ZERO — Prototype Progression & Recovery Economy v0.1

**Status:** Implementable prototype baseline; không phải live balance đã kiểm chứng. File này sở hữu CCL cost fixtures, emergency economy và bounded source loops. Research nodes và mission content có catalog riêng.

## 1. CCL requirements

CCL upgrade không cần Research Lab cùng cấp chưa mở, không yêu cầu PvP/Coalition. Existing rooms không bị demote khi tăngCCL. Upgrade cost upfront, queue1 Command; cancel trước hoàn thành refund100%, elapsed reset; no instant repeat reward. Times theo real simulated window; Command luôn hoạt động.

| Target CCL | Scrap | Components | Research Data | Time | Additional prerequisite |
|---|---:|---:|---:|---|---|
| 2 | 20 | 5 | 0 | 30s | Water restored + Living6beds; curated sector được clear bằng internal3-unit squad trước Gate |
| 3 | 30 | 10 | 0 | 30s | HydroL1 active;6living; không bắt first external mission |
| 4 | 40 | 10 | 0 | 1min | First House successful extract |
| 5 | 200 | 75 | 10 | 5min | Warehouse objective clear, GeneratorL2, LivingL2; không yêu cầu Lab trước unlock |
| 6 | 400 | 150 | 30 | 10min | Population≥10, GeneratorL3, WorkshopL2, LabL1,1Military Authorization |
| 7 | 650 | 240 | 60 | 15min | SecurityL1,1Hive Chitin Core, Population≥12 |
| 8 | 900 | 320 | 90 | 20min |1NPC Silo09 command objective successful extract, GeneratorL3 |
| 9 | 1250 | 450 | 140 | 30min |1Military AI Core, LabL3, WorkshopL3 |
| 10 | 1700 | 600 | 220 | 45min |1Neural Core, GeneratorL4, LabL4 |
| 11 | 2200 | 800 | 320 | 60min | Chapter7BelowZero discovery,1Architect Archive, Population≥18; không cần Alliance membership |
| 12 | 3000 | 1100 | 450 | 90min | Chapter8 resolution,2Architect Archives, GeneratorL5; solo path hợp lệ |

Storage capacity là affordability gate: nhiều General Storage cộng capacity riêng mỗi resource; baseline capacity250 mỗi category từ starting StorageL1, không thêm base250 nữa. StartScrap300 được grandfathered (chỉ giữ existing surplus, dừng production/incoming claims tới dưới cap); không xóa50Scrap. Upgrade/build thêm kho để trả cost lớn, không silent auto-expand. Gear locker baseline20 trước Armory, quy tắc trong Mission Session.

## 2. Mandatory PvE source routes

Mọi progression boss/key encounter là persistent named contract, repeatable và guaranteed token **sau successful extraction**. Không dùng rare loot roll để gateCCL.

| Required item | Available before gate | Guaranteed objective | Repeat policy |
|---|---|---|---|
| Military Authorization | CCL5 | Depot Relay01: open command terminal, squad4, Medium |1/token successful clear;6h refresh; first access immediate |
| Hive Chitin Core | CCL6 | Hospital LowerNest01, squad4, bossHiveMother |1/kill+extract;6h refresh |
| Military AI Core | CCL8 | FactoryWarMachine01, squad5, WarMachineA17 |1/kill+extract;6h refresh |
| Neural Core | CCL9 | DeepResearchVisitor01, squad5, FallenVisitor |1/kill+extract;6h refresh; không cần Xenobiology trước encounter |
| Architect Archive | CCL10 | DeepSectorArchive01, clear3Mechanical rooms +restore terminal, squad5 |1/objective+extract;6h refresh; không cần CCL11/Coalition |

First-clear/per-repeat loot khác token vẫn theo location budget. Token không trade/salvage/steal và không tự consume khi mở tooltip. CCL dùng item deduction trong upgrade transaction. Nếu thất bại, không permanent target lock; comeback chain vẫn hoạt động. Chapter unlock cần table ở campaign; chapter completion không cần voluntary PvP.

## 3. Emergency8PU mode và survival comeback

EmergencyCore giữ **8PU**, GeneratorL1 giữ20PU. Khi generation không đủ priority1 full loads và battery0, automatic Emergency Life Support mode:

- Command2PU + emergencyWater3PU + emergencyFood3PU =8PU. Emergency channels are Core infrastructure, available even if normal rooms damaged/unbuilt; they do not create normal-room output.
- Emergency mode **waives Food/Water consumption**, net0, without minting resources. Normal production is paused for emergency channels. No separate relief output or emergency1unit top-up; UI shows consumption suspended. Surviving roster never generates spendable output from the waiver.
- Food/Water hunger timers đứng lại và giảm về0 sau10 emergency minutes; không offline health/death event. No research/crafting/Radio/security output bằng8PU này. Các job khác pause, không cashout emergency supplies.
- Generator có **Manual Restart** action5min, Command automation, cost0, restore lên25%integrity từ disabled. Một lần/generator/rolling24h; không tạo Scrap/XP/loot, không heal vượt25%. Nếu EmergencyCore-only mà Restart cooldown chưa hết, emergency mode vẫn bảo toàn residents; sabotage không thể disable repaired Generator trong protected cooldown30min sau restart.
- At25%integrity normal Generator output giữ20PU×0.8=16PU (25%integrity band); Core8 tổng24 đủlife-support11. Normal repair nâng integrity costceil(20Scrap×missingIntegrity), timeceil(4min×missingIntegrity), min1Scrap/30s. Generator repair không cần Components/Workshop/healthy worker. Other basic rooms dùng cùng rule; advanced cost thêmceil(5Components×missingIntegrity).

Normal staffed Food/Water production miễn các negative efficiency do thiếu ăn/nước/morale/fatigue; damage/power vẫn áp. Không thể tự duy trì deficit vì starvation giảm chính survival output. Negative hunger penalty chỉ áp Workshop/Research/Training/Recycler và recovery, không áp rescue/emergency actions. At hunger/dehydration threshold chỉ health readiness penalty (−10%maxHP, clamp minimum1HP), **không random offline death hoặc injury roll**; xóa sau10min ổn định. Food và Water production penalties multiplicative cho nonessential rooms, cap tổng−40%; Clinic healing penalty max25%, không nhân thêm morale vô hạn.

### Bounded emergency salvage

Nếu available Food<5 hoặc Water<6 hoặc Supply<6, Command có **Local Relief**10min, không roster/deploy/cost: top-up tới Food10,Water12,Supply6; không vượt threshold, không stack thêm vào held stock. Output bound: chỉ normal consumption và next PvESupply; không dùng craft/trade/CCL/site/PvP; normal stock dùng trước, separate bound ledger trên UI. Eligibility tính cả bound balance và pending mission/items/inbox để reconnect không mint;1active relief, cooldown30 simulated minutes từ completion, persist eventID. Không cấp Scrap/Components/gear/XP. BoundSupply được dùng deploy comeback route, không scouting/PvP; comeback route auto reveals basic target card, noScout required.

**Shelter Perimeter**: permanent private repeatable PvE,0km, squad1–3, deploymentSupply=2+squadSize (khôngdistance/difficulty surcharge),2rooms,2Crawler split1/room, exit aftereach room, no hazards/locks, objective repair crate. Reward15Scrap5Components2Chemicals +Food5Water6;1stack/resource, total5CU; Cargo squad1=4, squad2=8, squad3=12, nên squad1 chọn4/5stacks, keyobjective0CU. Có0worker outside? applicant/cot khôi phục squad. Relief+salvage chỉ tạo recovery rate thấp, không strategic/progression token/first-clear/cache farm. Repeat immediate sausettlement; fatigueEasy10 và normal death ngoài tutorial. Player muốn tránh combat có manual collection action15min cho5Scrap2Components1Chemicals,1/30simulated min, không cần healthy roster. Emergency economy không tạo account progression mạnh hơn expeditions bình thường; verify rate qua playtest.

## 4. Offline event stepping

Account-wide simulated offline window=min(trustedNow−lastAccountObservation,8h). After processing, persist lastAccountObservation=trustedNow, including skipped time beyond8h; never retain that skipped time as catch-up debt. Reconnect at the same timestamp processes0seconds, not another8h batch. All jobs, consumption, fatigue/rest/treatment, construction/research và site production dùng cùng window. Advance đến next event (queue complete, storagefull/depleted, batteryempty, hungerthreshold, fatigueband, sitecollection), apply once rồi tiếp tục; storagefull chỉ dừng relevant production, consumption vẫn chạy và mở chỗ cho production. Non-resource mission pause theo Mission Session. Không roll lethal event trong offline survival. Sau8h toàn bộ background clocks freeze; real-time PvP reservation/shields vẫn dùng trusted real time và loss policies riêng. On login after16h, only8h background elapsed is simulated; immediately reopening yields0additional output.

## 5. Slice boundary và QA

First2h: CCL4,squad3,7–8survivors,House+Warehouse,Clinic injury treatment,craft1item,Radio online,one sectorchoice,unknown18.4km hint. **Extended slice2–4h**: CCL5,squad4,LabL1,one tierI research,Hospital branch và normal death/recovery fixture ngoài tutorial. Không claim4h chắc chắn đạt với live balance; đây là target cầnplaytest. UI phải ghi event hook ở18.4km chỉ là passive story transmission, không target deployable vượtRadio range.

Runtime/simulation acceptance NOT RUN. Numeric checks bằng arithmetic không thay thế playtest.
