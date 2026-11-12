# BURROW ZERO — Mission Session, Save & Reward Contract v0.1

**Status:** Gameplay implementation baseline. Không chọn engine/backend provider; bắt buộc bảo toàn các invariants dưới đây.

## 1. Mission lifecycle và ownership

`PREPARED → TRAVEL_OUT → EXPLORING → EXTRACTING → RETURNING → SETTLED → PRESENTED`.
Alternative terminal result: `FAILED/ABANDONED → SETTLED`. Một account chỉ1active expedition/raid prototype; Silo background jobs tiếp tục. Departure atomically reserve roster/equipment, debit round-trip Supply và raid charge nếu PvP, create missionID + immutable contentVersion/seed/initial outcome stream. Chưa commit departure thì không debit; retry cùng requestID trả cùng missionID. Scout cost riêng consume khi scan bắt đầu; cancel scan không refund Supply, time retry không reroll cùng intel version.

Successful extraction là giao dịch ownership: validate exit, escort/cargo, mission result → commit survivor/body/gear + loot + XP + knowledge + contract + first-clear flags + theft ledger một lần → RETURNING. Return travel chỉ trì hoãn survivor availability, không tước loot đã secured, không lethal/random loss event trên return. Outbound travel event chỉ minor HP loss tối đa10%currentHP, không thể down; event roll một lần, resolve khi đến. Return event chỉ fiction/cache bổ sung được roll/debit riêng cùng mission settlement, không phát sinh double loot. First-clear reward gắn account+namedNodeID+bossTier, không gắn seed/refresh; chỉ commit khi successful extract với objective hoàn thành.

## 2. Pause/quit/disconnect

| Context | Pause/app close | Resume | Time limits |
|---|---|---|---|
| PvE combat/explore | Freeze mission simulation tại durable tick gần nhất; không chạy attack/bleedout khi app đóng | Resume same seed/RNG cursor, HP/items/rooms | Không real-time expiry khi inside; tối đa1mission/account tránh giữ nhiều node |
| PvE travel | Tiếp tục bằng trusted elapsed trong8h offline window | Resolve once tại arrival | Không đi quá8h simulated offline |
| PvP combat/site raid | Không tactical pause; disconnect tiếp tục locked default AI, không auto consume item | Resume latest authoritative tick |15real minutes từ departure; timeout auto-extract chỉ nếu squad hiện đang ở cleared valid exit và escort/cargo valid, khác là FAILED |
| Reward reveal | Animation/presentation dừng | Hiện cùng cards/claimed state | Không đổi outcome hoặc grant lại |

PvE suspend không khóa world shared node cho người khác: PvE instance là private snapshot. Temporary node hết hạn sau khi departure thì mission instance giữ tới settlement, node không phát sinh farm slot mới cho account tới khi mission hết. PvP đặt incoming reservation độc quyền tối đa15min; hết hạn phải release/settle deterministic, không kéo dài vì pause/disconnect. Countdown không bị pause trong Settings hoặc background.

Abandon là explicit confirmation liệt kê field loot, survivors/body và charge loss. Normal PvE abandon ngoài safe exit tương đương failed extraction; không gọi là retreat. Retreat tại cleared exit giữ secured manifest và là successful extraction. Không có nút force-safe-return ngoài tutorial/explicit emergency exit. Có thể pause PvE để chọn, không cho sửa state. Default PvP AI: focus lowest-HP reachable enemy, không reposition/consumable tự phát; defender cũng dùng snapshot AI preset, không phản ứng qua remote UI.

## 3. Durable events và recovery

Mỗi mission có monotonically increasing eventSequence; random outcome ghi trước khi show hit/loot/card, mọi input xử lý một lần theo requestID. Persistent record gồm initial snapshot, RNG cursor, event outcomes, inventory debits, field_revives_used, bodies/passengers, current room graph, action progress và terminal settlementID. Save trước acknowledgement; crash trước ACK được retry, không quay về prelethal visible result. Authoritative persistence/anti-cheat provider sẽ chọn trong architecture, không được dùng client local clock để quyết định competitive state.

Settlement dùng một transaction hoặc durable state machine recoverable tương đương: reserve → commit with settlementID → acknowledge. Không show ownership success trước commit. On retry, trả lại cùng receipt; không apply phần reward lần hai. First-clear, objective item, XP, body recovery và theft commit chung receipt; partial interrupted write phải complete hoặc rollback toàn bộ. Mission/contentVersion không thay giữa chừng khi patch game; migrate bằng explicit versioned rule hoặc giữ compatibility snapshot.

## 4. Cache, overflow và knowledge

Cache contents roll một lần khi cache instance được tạo trong mission; cacheID+contentVersion+immutable cards persisted cùng event. Trước extraction là field loot có thể mất, không được mở để đưa item vào Secure Data Case. Sau extraction cache owned; Open chỉ reveal. Crash card3/5 → cùng5cards, cùng claimed flag. RevealAll/Skip không đổi quantity, odds hay reward.

Nếu common storage/gear inventory đầy, settlement đưa loot vào **Return Inbox**: không cap số lượng trong prototype, không expiry, không production/PvP exposed, chỉ chứa reward already committed; không thể chủ động gửi kho vào inbox. Inbox cho chọn claim phần vừa capacity, salvage/sell theo recipe hoặc discard confirmation. Partial claim có remaining quantity và idempotent requestID. Mission mới bị chặn nếu có từ3 uncleared return manifests nhằm tránh dùng inbox làm kho farm vô hạn; notification nêu cách giải quyết. Cache mở khi gear full cũng dùng inbox, không auto-delete. Gear trước Armory có20slots automated Command locker; Armory bonus thay thế cap20 bằng listed cap, không cộng thêm20. Equipped gear không tính locker cap; key/story items không cap.

Failed run: không loot/XP/contract/first-clear reward, nhưng encountered Bestiary family/behavior và map discovery của room đã tới giữ như knowledge, recorded once/event; không Research Data/blueprint cho failure trừ Secure Data Case nếu experiment được bật riêng (default OFF). Không thể reroll quest reward bằng abandon/repeat.

## 5. Regression acceptance

Force-close tại departure, hit lethal, Injector completion, room loot, extract commit, return, mỗi card reveal; retry request10lần phải cho cùng receipt, resource totals và survivor state. Compare one8h offline simulation với8×1h partition, cùng state nếu không có player action; full storage xử lý theo từng next event, không dừng consumption. PvP two incoming attacks chỉ1reservation thành công. QA status NOT RUN cho tới khi có build.
