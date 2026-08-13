# Thí nghiệm 002: Những Watt đầu tiên qua thép 3 mm (ĐÃ LÊN KẾ HOẠCH)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · Tiếng Việt · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Giai đoạn:** 2 (công suất vào tải đã biết tại cộng hưởng tìm được trong [001](../001-sweep-map-3mm-steel/README.md)).
- **Mục tiêu:** đo công suất DC thực tế truyền qua thép 3 mm với driver half-bridge và biến áp ghép.
- **Giả thuyết:** với một cặp Langevin cùng lô, tiếp xúc bằng mỡ+kẹp (hoặc epoxy), và biến áp ghép đã chỉnh, ≥0.5 W vào tải điện trở tại đỉnh giai đoạn 1 là khả thi. (Các con số multi-watt/kW trong tài liệu dùng transducer và cách dán khác — coi chúng là trần trên, không phải ngưỡng đạt.)
- **Điều kiện tiên quyết:**
  - Thí nghiệm 001 đã hoàn tất (đỉnh có thể tái lặp, tần số đã ghi).
  - TVS đã lắp trên mạch RX trước khi cấp nguồn cho driver ([docs/02-safety.md](../../docs/02-safety.md)).
  - Đã tuân thủ trình tự khởi động driver ([hardware/driver/README.md](../../../../hardware/driver/README.md)).
- **Thiết lập (tối thiểu):**
  - TX: Pi → AD9833 sóng vuông → mạch tạo dead-time → half-bridge IR2110 → biến áp ghép → Langevin kẹp vào tấm ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Vách: thép 3 mm, phương pháp tiếp xúc đã ghi (mỡ+kẹp / epoxy / khác).
  - RX: Langevin → cầu Schottky → R_load đã biết (điện trở công suất) và/hoặc LED; đo V_dc và I_dc sau cầu ([sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) topology, tải thay vì chỉ ADC).
- **Quy trình (phác thảo):**
  1. Khởi động điện ở giới hạn PSU 0.2 A mà không khai báo công suất âm thanh.
  2. Kẹp TX/RX, đặt tần số dẫn đến đỉnh của thí nghiệm 001.
  3. Tăng giới hạn dòng từ từ; ghi PSU V/I, nhiệt độ MOSFET/biến áp, V_dc và I_dc trên tải.
  4. P_load = V_dc · I_dc. Tùy chọn: chụp ảnh demo LED một lần khi P_load đã biết.
  5. Lặp lại một lần sau khi nguội; tần số đỉnh có thể trôi theo nhiệt độ — kiểm lại bằng mini-sweep nếu công suất giảm.
- **Tiêu chí thành công:**
  1. P_load ≥ 0.5 W qua thép 3 mm tại tần số và phương pháp tiếp xúc đã ghi chép.
  2. Hai lần chạy đồng nhất về P_load trong khoảng ~20% dưới cùng kẹp/couplant (ổn định bậc độ lớn, chưa đạt cấp đo lường).
  3. Ảnh LED (hoặc tải khác) + CSV/log liên kết từ file này dưới `data/`.
- **Thất bại cũng là dữ liệu:** nếu P_load vẫn ≪ 0.5 W, ghi Δf của cặp (từ 001), phương pháp tiếp xúc, số vòng biến áp, và waveform — đó là đầu vào cho ADR tiếp theo, không phải lý do để âm thầm sửa simulator.
