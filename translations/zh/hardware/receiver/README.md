# 接收端

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · 中文 · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

原理图：[阶段 1 — sch2](../schematics/sch2-receiver-stage1.png) · [阶段 4 — sch4](../schematics/sch4-receiver-node.png)（由 [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py) 生成）

- 阶段 1（测量）：Langevin 换能器 RX（两根引线均悬空——切勿接地！）→ 肖特基桥（4×SS14）→ RC 滤波（10k || 100n）→ 5 V TVS → **47 kΩ 串联** → ADS1115 A0（该电阻限制流入 ADC 保护二极管的电流：TVS 将电压钳位在输入绝对最大值约 9 V 以上）。
- 阶段 2（功率）：RX → 同一桥 → 已知阻性负载（和/或 LED），测量桥后的直流电压和电流；功率为该负载上的 V·I。协议：[experiments/002](../../experiments/002-watts-3mm-steel/README.md)。
- 阶段 4（节点）：RX → GY-LTC3588 **直连 PZ1/PZ2**（LTC3588-1 内置桥，无需外部桥）→ 1 F 超级电容 → ESP32（深度睡眠 + 占空比）。负载调制——2N7002 + 100 Ω 接在 **直流侧**（模块的 VIN 引脚，见 sch4）；单个 MOSFET 并联在交流压电片上不工作——体二极管会将半个周期短路（docs/03）。

重要提示：在首次上电前务必安装 TVS——谐振时开路压电片会输出数十至数百伏。桥后直流侧——单向 SMBJ5.0A；节点压电片（交流）两端——仅用双向 SMBJ15CA。
