# Giao thức khám phá bộ thu và tự động chỉnh tần (bản phác thảo; triển khai theo giai đoạn 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · Tiếng Việt · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

Mục tiêu: thiết bị tự xác định xem có bộ thu phía sau vách hay không, tự chọn tần số và công suất, và không làm hỏng vách một cách vô ích nếu ai đó "quên hàn bộ thu vào".

Mô hình tham chiếu là sạc Qi: chúng giải quyết đúng vấn đề này (có điện thoại trên cuộn dây không?) bằng đúng chuỗi thao tác này. Tương tự âm học của chúng ta:

## Giai đoạn 0 — ping tương tự (bộ thu có thể bị xả hoàn toàn)
Phát (TX) quét dải tần số ở công suất thấp và đo **dòng và pha của chính nó** (shunt + bộ tách đỉnh → ADS1115). Một bộ thu cộng hưởng phía sau vách là một tải được ghép với TX qua vách: sự hiện diện của nó thể hiện dưới dạng một vùng lồi/vùng lõm đặc trưng trên đường cong trở kháng TX, ngay cả khi mọi thứ bên trong đều không được cấp nguồn. Cùng nguyên lý với máy dò kim loại và ping tương tự của Qi.
- Có dấu hiệu → giai đoạn 1. Không có dấu hiệu → "không tìm thấy bộ thu", giữ ở chế độ ping chờ (mỗi N giây một lần), không tăng công suất.
- Thêm: đường cong trở kháng của vách "trống" được ghi lại lúc lắp đặt làm tham chiếu — để phân biệt "không có bộ thu" với "bộ thu bị tuột / bị lệch".

## Giai đoạn 1 — bắt tay số
TX dừng ở tần số ứng cử (đỉnh của giai đoạn 0) và cấp công suất. Bộ thu hoạch năng lượng (RX) nạp siêu tụ, MCU thức dậy và phản hồi bằng **điều biến tải**: một MOSFET định kỳ nối tắt piezo của nó theo một mã (ID + phiên bản giao thức). TX nhìn thấy điều này dưới dạng điều biến dòng của chính nó. Hoàn toàn không cần bộ phát bên trong — đây là sơ đồ RFID, cùng loại như trong đơn đăng ký DOE/RPI đã bị bỏ hoang US20100027379 (kỹ thuật trước đây miễn phí).

## Giai đoạn 2 — chỉnh tần servo (nhiễu loạn & quan sát)
RX có thể báo cáo điện áp bus của nó (đo lường từ xa qua điều biến tải). TX bước ±Δf và giữ ở mức công suất thu lớn nhất — một vòng lặp MPPT cổ điển. Điều này bù trôi dịch cộng hưởng theo nhiệt độ (cái bẫy chính của ngách này: dịch ~6% = giảm hiệu suất ~10×).

## Giai đoạn 3 — đàm phán công suất và watchdog
RX yêu cầu một mức (sống / đang sạc / cho thêm), TX giới hạn công suất ở mức đã yêu cầu. Không nhận phản hồi trong M chu kỳ → TX quay lại giai đoạn 0 ở công suất thấp.

## Phần cứng cần thiết (BOM mục 12, sơ đồ — hardware/schematics/sch4)
- TX: shunt 0.1 Ω + bộ chỉnh lưu/tách đỉnh trên kênh thứ hai của ADS1115 (dòng), tùy chọn bộ so sánh pha.
- RX: 2N7002 + ~100 Ω ở phía **DC** của bộ chỉnh lưu (chân VIN của mô-đun LTC3588) + GPIO — tải được chuyển mạch sau cầu, và TX nhìn thấy nó dưới dạng điều biến dòng của chính nó. Một MOSFET đơn nối tắt piezo AC không hoạt động (diode thân nối tắt một nửa sóng, cổng không có tham chiếu trên nút trôi); biến thể nối tắt piezo chỉ hoạt động với một cặp MOSFET nối tiếp lưng đối lưng.

## Giới hạn
Ping tương tự yếu dần khi độ dày vách và tổn thất tiếp xúc tăng (dấu hiệu bị chìm trong tạp âm) — ngưỡng phát hiện phải được đo trong một thí nghiệm riêng (experiments/). Đối với vách dày, phương án dự phòng: RX, sau khi đã tích lũy đủ điện tích, định kỳ "gõ" bằng một beacon riêng của nó.
