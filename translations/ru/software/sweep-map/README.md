# свип-карта

> [English (primary)](../../../../software/sweep-map/README.md) · Русский · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md) · [한국어](../../../ko/software/sweep-map/README.md) · [हिन्दी](../../../hi/software/sweep-map/README.md)

python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — только на Pi
```

На Pi: `raspi-config` → включить SPI и I2C.

Пробный запуск без оборудования, на любом компьютере (достаточно matplotlib):

```bash
python3 sweep_map.py --mock
