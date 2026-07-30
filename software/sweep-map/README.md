# sweep-map

> English (primary) · [Русский](../../translations/ru/software/sweep-map/README.md) · [Deutsch](../../translations/de/software/sweep-map/README.md) · [Português](../../translations/pt/software/sweep-map/README.md) · [中文](../../translations/zh/software/sweep-map/README.md) · [日本語](../../translations/ja/software/sweep-map/README.md)

Sweep map of the channel frequency response. See the header of sweep_map.py for the hardware, wiring, and how to run it.

Environment (recent Raspberry Pi OS releases require a venv):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — only on the Pi
```

On the Pi: `raspi-config` → enable SPI and I2C.

Dry run without hardware, on any computer (matplotlib is enough):

```bash
python3 sweep_map.py --mock
```
