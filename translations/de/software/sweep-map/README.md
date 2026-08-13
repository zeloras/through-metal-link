# Sweep-Karte

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · Deutsch · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md) · [한국어](../../../ko/software/sweep-map/README.md) · [हिन्दी](../../../hi/software/sweep-map/README.md)

Sweep-Karte der Kanal-Frequenzantwort. Siehe den Header von sweep_map.py für die Hardware, Verkabelung und Anleitung zur Ausführung.

Umgebung (neuere Raspberry Pi OS-Versionen erfordern ein venv):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — nur auf dem Pi
```

Auf dem Pi: `raspi-config` → SPI und I2C aktivieren.

Testlauf ohne Hardware, auf jedem Computer (matplotlib ist ausreichend):

```bash
python3 sweep_map.py --mock
