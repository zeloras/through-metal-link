# sweep-map

> [English (primary)](../../../../software/sweep-map/README.md) · [Русский](../../../ru/software/sweep-map/README.md) · [Deutsch](../../../de/software/sweep-map/README.md) · [Português](../../../pt/software/sweep-map/README.md) · 中文 · [日本語](../../../ja/software/sweep-map/README.md)

频道频率响应的扫描图。请参阅sweep_map.py头部的硬件、连接和运行方法。

环境（最近的Raspberry Pi OS版本需要虚拟环境）：

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r ../requirements.txt spidev smbus2   # spidev/smbus2 — 只在Pi上
```

在Pi上：`raspi-config` → 启用SPI和I2C。

不需要硬件，在任何计算机上进行干跑（只需要matplotlib）：

```bash
python3 sweep_map.py --mock
