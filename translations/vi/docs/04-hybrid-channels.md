# Kênh lai: rào cản → vật lý → con số

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · [Português](../../pt/docs/04-hybrid-channels.md) · [Español](../../es/docs/04-hybrid-channels.md) · [Français](../../fr/docs/04-hybrid-channels.md) · [Italiano](../../it/docs/04-hybrid-channels.md) · [Polski](../../pl/docs/04-hybrid-channels.md) · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · Tiếng Việt · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

Nguyên lý (một hệ quả của "nghịch lý xuyên thấu"): một sóng đi qua rào cản đúng ở mức độ mà nó tương tác yếu với rào cản đó — đó là lý do không tồn tại kênh vạn năng. Nền tảng không chạy theo một kênh duy nhất; với mỗi rào cản, nó chọn vật lý mà rào cản trong suốt với và mà bộ thu "thèm khát" cộng hưởng.

## Bảng chọn kênh

| Rào cản | Kênh hoạt động | Dự kiến (bậc độ lớn) | Ghi chú |
|---|---|---|---|
| Thép/nhôm 1–60 mm, có thể tiếp xúc | Piezo-âm học (kênh chính của chúng tôi) | watt; kbit/s (lên đến Mbit/s ở chế độ MHz) | cần tiếp xúc âm (mỡ ghép/epoxy) |
| Kim loại: bẩn, sơn, nóng, không mong muốn tiếp xúc | EMAT (từ trường → âm trong thành) | mW; kbit/s; khe hở lên đến ~3 mm | chỉ thành dẫn điện; dữ liệu, không phải công suất |
| Thành sắt từ không có piezo nào | Từ trễ (một cuộn dây dẫn động chính thép) | mảnh vụn; bit/s–kbit/s | nhánh thử nghiệm, rẻ để thử |
| Thành kép với chân không (thermos, cryostat, dewar) | Từ trường tần thấp (chục–trăm Hz) | µW–mW; bit/s | hiệu ứng bề mặt: trong thép δ≈0.6 mm @1 kHz — hạ tần số xuống |
| Phi kim: kính, nhựa, gốm | Piezo-âm học (dễ hơn kim loại) | watt; kbit/s | + RF thường xuyên cũng đi qua — kiểm tra cái đó trước |
| Thành có lớp cao su/bọt, composite | Thật lòng: gần như ngõ cụt | — | lớp hấp thụ nuốt hết mọi thứ; cách khắc phục là một điểm không có lớp phủ |
| Chất lỏng phía sau thành (bồn đầy) | Piezo-âm học, suy giảm | công suất − vài dB; rung ngắn hơn | tải lỏng dịch chuyển/tắt giảm cộng hưởng — quét lại với bồn đầy; giữ cường độ liên tục ≲1 W/cm² để nằm dưới ngưỡng xâm thực ([lý thuyết](00-theory.md#effect-on-the-wall-and-the-media-behind-it)) |
| Chất lỏng sủi bọt trong đường âm | Giải pháp kiến trúc | — | gắn bộ thu trên thành, giữ chất lỏng ra khỏi đường truyền |

## Kiến trúc nút lai

- Lớp công suất: cặp piezo cộng hưởng (giai đoạn 1–4).
- Lớp dữ liệu không tiếp xúc: đầu EMAT như "súng quét" tháo rời (giai đoạn ~6).
- Lớp dự phòng: cuộn LF cho cấu trúc chân không (khi nhiệm vụ yêu cầu).
- Giao thức khám phá (docs/03) mở rộng từ "quét qua tần số" sang "quét qua vật lý": ping piezo → ping EMAT → ping LF; nút tự chọn kênh đi qua được và báo cáo rào cản mà nó thấy.

## Ứng dụng mẫu theo kênh

1. **Khối pin kín (EV/lưu trữ):** cảm biến T/khí bên trong vỏ bọc potting; công suất+dữ liệu qua cặp piezo xuyên 2–3 mm nhôm. Thị trường đang bùng nổ, và việc xuyên vào vỏ pin = địa ngục chứng nhận.
2. **Cryostat/dewar:** logger nhiệt độ bên trong, gửi gói bit mỗi phút một lần qua từ trường LF xuyên lớp vỏ chân không. Về cơ bản ngoài tầm với của âm học — đây là nơi kênh lai không thể thay thế.
3. **Đường ống/autoclave dưới áp suất:** máy quét EMAT ép vào ống sơn nóng mà không cần chuẩn bị bề mặt — đọc beacon cộng hưởng thụ động từ bên trong.
4. **Bồn lên men (bia/rượu, thép không gỉ):** cảm biến mật độ/T bên trong bồn mà không một lỗ xuyên nào — quy định vệ sinh rất thích việc không có lỗ.
5. **Container biển/két sắt:** "hàng còn sống không" — cặp piezo xuyên thép gợn sóng, thăm dò bằng máy quét cầm tay.

## Giới hạn không lớp nào giải quyết được
Công suất — chỉ piezo tiếp xúc (EMAT và từ trường LF yếu hơn nhiều bậc độ lớn). Thành composite/lót cao su nằm ngoài nền tảng. Tốc độ kênh LF là bit mỗi giây — đó là telemetry, không phải streaming.
