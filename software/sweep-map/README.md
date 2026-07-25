# sweep-map

> English (primary) · [Русский](README.ru.md) · [Deutsch](README.de.md)

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
