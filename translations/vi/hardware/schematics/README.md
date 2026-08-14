# Sơ đồ thiết bị thử nghiệm

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · Tiếng Việt · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Tệp | Nội dung | Giai đoạn |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | driver: IR2110 + 2×IRF540, bootstrap, biến trở khớp | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | receiver: cầu 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | sơ đồ chân: Pi ↔ AD9833 ↔ cặp piezo ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | node: RX → GY-LTC3588 → siêu tụ → ESP32 (+ điều chế tải) | 4 |

Đây là các sơ đồ nguyên lý **prototype trên breadboard** (giá trị linh kiện là điểm khởi đầu, đánh dấu `*` nơi cần tinh chỉnh trên oscilloscope). Một dự án KiCad với layout PCB sẽ ra mắt sau khi prototype được kiểm chứng thực tế — đúng như đã hứa trong [driver/README.md](../driver/README.md).
