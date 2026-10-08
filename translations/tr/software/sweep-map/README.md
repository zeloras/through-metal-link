# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · Türkçe · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · [中文](../../../zh/software/sweep-map/README.md) · [日本語](../../../ja/software/sweep-map/README.md) · [한국어](../../../ko/software/sweep-map/README.md) · [हिन्दी](../../../hi/software/sweep-map/README.md)

Kanal frekans tepkisinin tarama haritası. Donanım, bağlantılar ve çalıştırma yöntemi için sweep_map.py dosyasının başlığına bakın.

Ortam (yeni Raspberry Pi OS sürümleri bir venv gerektirir):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — yalnızca Pi üzerinde
```

Pi üzerinde: `raspi-config` → SPI ve I2C etkinleştirin.

Donanım olmadan kuru çalıştırma, herhangi bir bilgisayarda (matplotlib yeterlidir):

```bash
python3 sweep_map.py --mock
```
