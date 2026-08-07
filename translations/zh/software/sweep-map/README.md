# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · 中文 · [日本語](../../../ja/software/sweep-map/README.md)

通道频率响应的扫描图。请参阅 sweep_map.py 头部的硬件、接线和运行方法。

环境（较新的 Raspberry Pi OS 版本需要虚拟环境）：

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — 只在 Pi 上
```

在 Pi 上：`raspi-config` → 启用 SPI 和 I2C。

不需要硬件，在任何计算机上进行干跑（只需 matplotlib）：

```bash
python3 sweep_map.py --mock
