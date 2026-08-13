# 测试台原理图

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · 中文 · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

原理图是从代码生成的 —— [render_schematics.py](../../../../hardware/schematics/render_schematics.py) 同时作为设计源（schemdraw）；要进行修改，编辑脚本，然后重新生成：

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| 文件 | 什么 | 阶段 |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | 驱动器：IR2110 + 2×IRF540，bootstrap，匹配变压器 | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | 接收器：4×SS14 桥 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | 引脚排列：Pi ↔ AD9833 ↔ 压电对 ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | 节点：RX → GY-LTC3588 → 超级电容器 → ESP32（+ 负载调制） | 4 |

这些是 **面包板原型** 原理图（组件值是起始点，在示波器上标记为 `*` 的地方进行调整）。一旦原型在实践中得到验证，KiCad 项目将包含 PCB 布局，如 [driver/README.md](../driver/README.md) 中所承诺的。
