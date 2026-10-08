# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · [Español](../../../es/software/sweep-map/README.md) · [Français](../../../fr/software/sweep-map/README.md) · [Italiano](../../../it/software/sweep-map/README.md) · [Polski](../../../pl/software/sweep-map/README.md) · [Türkçe](../../../tr/software/sweep-map/README.md) · [Українська](../../../uk/software/sweep-map/README.md) · [Tiếng Việt](../../../vi/software/sweep-map/README.md) · 中文 · [日本語](../../../ja/software/sweep-map/README.md) · [한국어](../../../ko/software/sweep-map/README.md) · [हिन्दी](../../../hi/software/sweep-map/README.md)

通道频率响应的扫频图。有关硬件、接线及运行方式，请参阅 sweep_map.py 的头部说明。

运行环境（较新的 Raspberry Pi OS 版本需要 venv）：

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — 仅在 Pi 上可用
```

在 Pi 上：`raspi-config` → 启用 SPI 和 I2C。

在任意计算机上无硬件空跑（只需 matplotlib）：

```bash
python3 sweep_map.py --mock
```
