# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · Italiano · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md) · [한국어](../../../ko/software/sweep-map/README.md) · [हिन्दी](../../../hi/software/sweep-map/README.md)

Mappa della risposta in frequenza del canale. Consulta l'intestazione di sweep_map.py per l'hardware, il cablaggio e le istruzioni di esecuzione.

Ambiente (le versioni recenti di Raspberry Pi OS richiedono un venv):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — solo sul Pi
```

Sul Pi: `raspi-config` → abilita SPI e I2C.

Esecuzione di prova senza hardware, su qualsiasi computer (basta matplotlib):

```bash
python3 sweep_map.py --mock
```
