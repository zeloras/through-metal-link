# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · Tiếng Việt · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md) · [한국어](../../../ko/software/sweep-map/README.md) · [हिन्दी](../../../hi/software/sweep-map/README.md)

Bản đồ quét đáp ứng tần số của kênh. Xem phần tiêu đề trong `sweep_map.py` để biết chi tiết phần cứng, cách đấu dây và cách chạy.

Môi trường (các bản Raspberry Pi OS gần đây yêu cầu venv):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — chỉ trên Pi
```

Trên Pi: `raspi-config` → bật SPI và I2C.

Chạy thử không cần phần cứng, trên bất kỳ máy tính nào (chỉ cần matplotlib là đủ):

```bash
python3 sweep_map.py --mock
```
