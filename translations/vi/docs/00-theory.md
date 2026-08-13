# Lý thuyết kênh truyền (những điều tối thiểu cần biết để làm việc)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · [Português](../../pt/docs/00-theory.md) · [Español](../../es/docs/00-theory.md) · [Français](../../fr/docs/00-theory.md) · [Italiano](../../it/docs/00-theory.md) · [Polski](../../pl/docs/00-theory.md) · [Türkçe](../../tr/docs/00-theory.md) · [Українська](../../uk/docs/00-theory.md) · Tiếng Việt · [中文](../../zh/docs/00-theory.md) · [日本語](../../ja/docs/00-theory.md) · [한국어](../../ko/docs/00-theory.md) · [हिन्दी](../../hi/docs/00-theory.md)

## Nguyên lý
Một phần tử piezo TX được ép/dán vào tường kích thích sóng dọc trong tường; một piezo RX ở phía bên kia biến nó trở lại thành điện. Tường đóng vai trò như một bộ cộng hưởng: tại các tần số cộng hưởng theo độ dày (bội số của nửa bước sóng), truyền đạt đạt cực đại.

## Các con số chính
Tốc độ âm dọc trong thép: ~5900 m/s.

| Độ dày thép | Cộng hưởng nửa bước sóng |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Bước sóng trong thép: 148 mm @ 40 kHz; 5.9 mm @ 1 MHz.

## Hai chế độ
- **A (40 kHz, đầu đổi Langevin).** Một tấm 3–5 mm ≪ λ — nó hoạt động như một màng; cộng hưởng được thiết lập bởi cặp đầu đổi, không phải bởi tường. Đơn giản và mạnh hơn chế độ B — chế độ để bắt đầu với. Bằng chứng tồn tại trong phòng thí nghiệm (không phải mục tiêu gara): NASA JPL ~24.5 kHz, hàng trăm W lên đến kW qua 5 mm Ti với phần cứng chuyên dụng.
- **B (0.6–1 MHz, đĩa).** Cộng hưởng theo độ dày của chính tường, và rất sắc (dịch tần số ~6% ⇒ truyền đạt giảm ~10× trong mô hình Fabry–Perot). Lớp kết quả RPI/Moss: hàng trăm mW cộng dữ liệu ở hàng trăm kbit/s dưới điều kiện dán và ghép khớp trong phòng thí nghiệm. Yêu cầu theo dõi tần số tự động.

## Các tổn thất chính
Lệch cộng hưởng trong cặp đầu đổi (đầu đổi Langevin rẻ có độ tản ±1 kHz), chất lượng tiếp xúc âm (epoxy > mỡ bôi trơn đặc + kẹp > áp lực khô), lệch trục, trôi cộng hưởng theo nhiệt độ. Câu trả lời cho tất cả đều giống nhau: chạy quét bản đồ trước mỗi lần thay đổi thiết lập.

## Tác động lên tường và môi trường phía sau

Tóm tắt: ở mức công suất nền tảng, tường và bất kỳ khí nào phía sau đều không bị ảnh hưởng. Chất lỏng phía sau tường chủ yếu ảnh hưởng *kênh truyền*; kênh chỉ bắt đầu ảnh hưởng *chất lỏng* khi gần ngưỡng xâm thực. Các con số ước lượng dưới đây dành cho chế độ A: 40 kHz, ~1 W/cm² vào thép 3 mm.

**Tường — không biến dạng, không mỏi, bao giờ.** Vận tốc hạt v = √(2I/ρc) ≈ 21 mm/s ⇒ dịch chuyển ≈ 80 nm, biến dạng sóng phẳng ε = v/c ≈ 3.5·10⁻⁶. Hai ước lượng ứng suất tương đương: đàn hồi E·ε ≈ 0.7 MPa (E ≈ 200 GPa) và âm học p = Z·v ≈ 1.0 MPa (Z_thép ≈ 4.6·10⁷ Pa·s/m). Thép dẻo ở 250+ MPa và giới hạn bền mỏi ~200 MPa — vẫn chênh lệch >200× theo cả hai cách, và dưới giới hạn bền mỏi thép chịu số chu kỳ không giới hạn. Các bộ phận cơ học dễ hỏng nằm ở nơi khác: gốm piezo (giòn, mất phân cực khi quá nhiệt) và đường dán (epoxy nóng lên và mỏi trước) — xem [02-safety](../../../docs/02-safety.md).

**Khí phía sau tường — không tác động.** Lệch trở kháng thép→không khí (~4.6·10⁷ vs ~400 Pa·s/m) truyền một phần có bậc 10⁻⁵ công suất. Không có gia nhiệt hay khuấy đo được; điện tử bên trong hộp kín không nhận thấy chuyển động tường cỡ nm.

**Chất lỏng phía sau tường — hai hướng:**

- *Chất lỏng → kênh (luôn luôn).* Nước tải mặt xa với ~1.5 MRayl thay vì không khí: một phần công suất bức xạ vào chất lỏng, Q giảm, đỉnh quét dịch và mở rộng. Chế độ B bị ảnh hưởng nặng nhất — lược cộng hưởng theo độ dày được tính cho biên thép–không khí và dịch khi tải chất lỏng. Quy tắc đứng bao trùm điều này: **quét lại với bình đầy thật**, không bao giờ tin quét lấy với bình rỗng. Lợi ích phụ: tắt dần của chất lỏng rút ngắn rung cộng hưởng (τ), nên mắt OOK mở ở tốc độ bit cao hơn. Bong bóng trong đường truyền (chất lỏng đang lên men!) tán xạ mạnh — xem giải pháp trong [04-hybrid-channels](../../../docs/04-hybrid-channels.md).
- *Kênh → chất lỏng (chỉ ở công suất cao).* Áp suất đỉnh bức xạ vào nước: p ≈ ρc·v ≈ 1.5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0.3 atm. Ngưỡng xâm thực quán tính ở 40 kHz trong nước thường (có khí) là ~1–2 atm, nên ở 1 W/cm² chênh lệch là 3–10×. Nhưng p tăng theo √công suất, và sóng đứng trong bình kín tạo điểm nóng cục bộ — hàng chục W/cm² liên tục vào bồn đầy chất lỏng có thể đạt ngưỡng. Vượt qua nó nghĩa là khử khí CO₂, hóa học siêu âm (vị lạ trong sản phẩm thực phẩm), và xói mòn xâm thực dài hạn bề mặt trong (chính cách máy làm sạch siêu âm hoạt động). Trần công suất liên tục vào tường có chất lỏng phía sau: **≲1 W/cm²**. Chế độ B được miễn: ở MHz ngưỡng cao hơn một bậc và công suất chỉ hàng trăm mW.

## Ngân sách công suất thu (ước lượng)
LED 20 mW; ESP32 chu kỳ nhiệm vụ 1–5 mW trung bình; radio BLE ~150 mW khi radio bật. Bộ đệm: siêu tụ 1 F @ 3.3 V lưu trữ E = ½CV² = 5.4 J. Số lần truyền mua được phụ thuộc vào thời gian phát: một sự kiện quảng cáo BLE ngắn (~2–5 ms ở ~150 mW) chỉ ~0.3–0.8 mJ → cỡ **10⁴ gói** từ tụ đầy; một kết nối / burst dài (~100 ms radio bật) là ~15 mJ → cỡ **10² burst**. Tiêu thụ trung bình vẫn phải nằm trong số watt thu được (mục tiêu stage-2 ≥0.5 W vào tải là cổng; cho đến khi đo được, coi các băng mode-A đa-watt trên đồ thị mô phỏng là mục tiêu, không phải dữ liệu).
