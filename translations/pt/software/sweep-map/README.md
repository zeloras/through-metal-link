# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · Português · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md)

Mapa de varredura da resposta de frequência do canal. Veja o cabeçalho do sweep_map.py para o hardware, fios e como executá-lo.

Ambiente (lançamentos recentes do Raspberry Pi OS exigem um venv):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — apenas no Pi
```

No Pi: `raspi-config` → ative SPI e I2C.

Execução seca sem hardware, em qualquer computador (matplotlib é suficiente):

```bash
python3 sweep_map.py --mock
