# スイープマップ

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · [中文](../../../zh/software/sweep-map/README.md) · 日本語 · [한국어](../../../ko/software/sweep-map/README.md) · [हिन्दी](../../../hi/software/sweep-map/README.md)

チャンネルの周波数特性のスイープマップ。ハードウェア、配線、実行方法については、sweep_map.py のヘッダーを参照してください。

環境 (最近の Raspberry Pi OS リリースでは venv が必要):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — only on the Pi
```

Raspberry Pi で: `raspi-config` → SPI と I2C を有効化。

ハードウェアなしで、任意のコンピュータでドライラン (matplotlib があれば十分):

```bash
python3 sweep_map.py --mock
