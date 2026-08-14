# Driver (giai đoạn 2): half-bridge IR2110

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · Tiếng Việt · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Sơ đồ mạch:** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) (tạo bởi [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

Chuỗi tín hiệu: Pi (SPI) → AD9833 **ở chế độ sóng vuông** (bit OPBITEN: MSB được đưa ra ngõ ra, biên độ rail-to-rail — không cần comparator riêng) → bộ tạo dạng xung **74HC14 + RC + 1N4148** (HIN/LIN bổ sung với dead time ~1 µs) → IR2110 → 2×IRF540 (half-bridge) → tụ cách ly DC 1 µF → biến áp ghép (ferrite, tỉ số ~1:3..1:5, chỉnh trên bàn) → transducer Langevin TX.

Ngõ ra sine của AD9833 (~0.6 Vpp) không phù hợp với logic IR2110 — nếu vì lý do nào đó bạn đặc biệt cần sóng sine từ DDS, hãy đặt một comparator ở giữa (ví dụ LM393, không có trong BOM).

Nguồn cấp cho khuếnh đại công suất: nguồn bench 12–24 V có giới hạn dòng (**bắt đầu ở 0.2 A**).

Lưu ý: quét ở giai đoạn 1 điều khiển piezo trực tiếp bằng sóng sine yếu từ DDS (~0.6 Vpp, xem `sweep_map.py`) — **driver này chỉ tham gia chuỗi ở giai đoạn 2 (công suất watt)**. Đừng kỳ vọng ≥0.5 W từ mạch chỉ dùng DDS ở giai đoạn 1.

Ghi chú:
- Transducer Langevin là tải dung tính (thường vài nF). Cuộn cảm nối tiếp hoặc biến áp ghép là bắt buộc; nếu không có, MOSFET sẽ tiêu tán dòng phản kháng và nóng cháy.
- **Biến áp ghép (điểm hỏng hóc phổ biến).** Bắt đầu với lõi ferrite nhỏ (ví dụ FT50-43 / tương đương), sơ cấp vài vòng, thứ cấp ~3–5 lần, tụ cách ly DC nối tiếp 1 µF film ở sơ cấp. Chỉnh để dòng nguồn tối thiểu *tại tần số cộng hưởng giai đoạn 1* khi TX **kẹp chặt vào tấm thép** và RX có tải. Tỉ số vòng và rò là thực nghiệm — sơ đồ đánh dấu `*` là có lý do. Ghi lại số vòng cuối cùng vào nhật ký thí nghiệm.
- **Dead time**: IR2110 không tự tạo. Phương án linh kiện rời — RC+1N4148 ở ngõ vào 74HC14 (chỉ trễ cạnh lên, ~1 µs; với chu kỳ 25 µs ở 40 kHz thì tổn thất <5%). Phương án dễ — module EGS002, mọi thứ đã tích hợp sẵn.
- **Logic 3.3 V**: cấp VDD của IR2110 từ cùng nguồn 3.3 V với AD9833 và 74HC14 — ở VDD=5 V thì ngưỡng VIH ≈ 3.1 V và sóng vuông 3.3 V chỉ vừa lọt qua (datasheet cho phép VDD xuống tới 3.3 V).
- **Bypass là bắt buộc**: 100 nF ở VDD và VCC (VCC — thêm 47 µF), và trên đường nguồn 470–1000 µF + 100 nF ceramic ngay tại nhánh half-bridge — nếu không, half-bridge trên dây cắm breadboard sẽ tự nhiễu xung switching. Giữ dây vòng công suất ngắn; nếu nút switching rung mạnh, chuyển khỏi breadboard sang tấm đồng dead-bug / protoboard với ground pour trước khi tăng dòng.
- **Trình tự cấp nguồn lần đầu** (bám theo [docs/02-safety.md](../../docs/02-safety.md)):
  1. Chưa gắn Langevin vào thứ cấp. Nguồn = 12 V, giới hạn dòng 0.2 A. Dùng oscilloscope kiểm tra xung điều khiển gate (HIN/LIN) và nút switching — xác nhận dead time và không shoot-through.
  2. Lắp biến áp ghép + TX Langevin **kẹp chặt vào tấm thép** (hoặc khối kim loại dày dùng để hi sinh). Vẫn giới hạn 0.2 A. Kích ở tần số đỉnh giai đoạn 1 chỉ đủ lâu để thấy dòng và điện áp RX.
  3. Tăng dần giới hạn dòng trong khi theo dõi nhiệt độ MOSFET và biến áp. Không bao giờ để Langevin chưa kẹp ở mức công suất — chạy công suất đầy trong không khí tự do là cách gốm nứt và driver chết.

TODO: dự án KiCad (PCB) khi prototype breadboard (hoặc dead-bug) đã kiểm tra xong. Cho đến lúc đó, các sơ đồ trong [`../schematics/`](../../../../hardware/schematics) là nguồn thiết kế chính thức.
