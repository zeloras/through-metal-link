# Bộ thu

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · Tiếng Việt · [中文](../../../zh/hardware/receiver/README.md) · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

Sơ đồ mạch: [giai đoạn 1 — sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) · [giai đoạn 4 — sch4](../../../../hardware/schematics/sch4-receiver-node.png) (được tạo bởi [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

- Giai đoạn 1 (đo lường): biến áp Langevin RX (cả hai đầu nổi — không nối mass!) → cầu Schottky (4×SS14) → bộ lọc RC (10k || 100n) → TVS 5 V → **47 kΩ nối tiếp** → ADS1115 A0 (điện trở này giới hạn dòng điện vào các diode bảo vệ của ADC: TVS kẹp ở khoảng ~9 V vượt quá giá trị tuyệt đối tối đa của đầu vào).
- Giai đoạn 2 (công suất): RX → cùng cầu đó → tải trở thuần đã biết (và/hoặc LED), đo V và I một chiều sau cầu; công suất bằng V·I trên tải đó. Giao thức: [experiments/002](../../experiments/002-watts-3mm-steel/README.md).
- Giai đoạn 4 (node): RX → GY-LTC3588 **nối thẳng vào PZ1/PZ2** (cầu đã được tích hợp sẵn trong LTC3588-1, không cần cầu ngoài) → siêu tụ 1 F → ESP32 (ngủ sâu + chu kỳ nhiệm vụ). Điều biến tải — 2N7002 + 100 Ω ở **phía một chiều** (chân VIN của module, xem sch4); một MOSFET đơn đặt song song với piezo AC không hoạt động — diode thân sẽ tắt một nửa sóng (docs/03).

LƯU Ý: phải lắp TVS trước khi cấp nguồn lần đầu tiên — một piezo hở ở tần số cộng hưởng sẽ tạo ra hàng chục đến hàng trăm volt. Ở phía một chiều sau cầu — một SMBJ5.0A một chiều; song song với piezo của node (AC) — chỉ dùng SMBJ15CA hai chiều.
