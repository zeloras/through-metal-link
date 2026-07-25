# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · Русский · [Deutsch](../../../de/software/sweep-map/README.md)

Свип-карта АЧХ канала. См. шапку sweep_map.py: железо, подключение, запуск.

Окружение (свежие Raspberry Pi OS требуют venv):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — только на Pi
```

На Pi: `raspi-config` → включить SPI и I2C.

Прогон без железа на любом компьютере (достаточно matplotlib):

```bash
python3 sweep_map.py --mock
```
