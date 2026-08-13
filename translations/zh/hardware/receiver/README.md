# 接收器

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · 中文 · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

电路图：[第 1 阶段 — sch2](../schematics/sch2-receiver-stage1.png) · [第 4 阶段 — sch4](../schematics/sch4-receiver-node.png) (由 [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py) 生成)

- 第 1 阶段（测量）：朗兹文超声换能器 RX（两根线都浮空 — 不要接地！）→ 肖特基桥（4×SS14）→ RC 滤波器（10k || 100n）→ 5 V TVS → **47 kΩ 串联** → ADS1115 A0（该电阻限制了进入 ADC 保护二极管的电流：TVA 抑制 ~9 V 高于输入的绝对最大值）。
- 第 2 阶段（瓦特）：RX → 同一桥 → 已知的电阻负载（和/或 LED），测量桥后 DC 电压和电流；负载中的功率是 V·I。协议：[实验/002](../../experiments/002-watts-3mm-steel/README.md)。
- 第 4 阶段（节点）：RX → GY-LTC3588 **直接连接到 PZ1/PZ2**（LTC3588-1 内置桥，不需要外部桥）→ 1 F 超级电容 → ESP32（深度睡眠 + 工作周期）。负载调制 — 2N7002 + 100 Ω 在 **DC 侧**（模块的 VIN 引脚，见 sch4）；单个 MOSFET 跨越 AC 压电器不起作用 — 体二极管短路了一半波（docs/03）。

重要：在第一次上电之前安装 TVS — 开放式压电器在谐振时输出数十到数百伏。桥后 DC 侧 — 单向 SMBJ5.0A；节点的压电器（AC）两端 — 只有双向 SMBJ15CA。
