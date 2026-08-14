# 测试台原理图

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · 中文 · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| 文件 | 内容 | 阶段 |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | 驱动：IR2110 + 2×IRF540，自举，匹配变压器 | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | 接收：4×SS14 桥 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | 接线：Pi ↔ AD9833 ↔ 压电片对 ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | 节点：RX → GY-LTC3588 → 超级电容 → ESP32（+ 负载调制） | 4 |

这些是**面包板原型**原理图（元件值为起始参考值，在示波器上调试确定的参数标有 `*`）。原型经过实物验证后，将推出包含 PCB 布局的 KiCad 工程 —— 正如 [driver/README.md](../driver/README.md) 中所承诺的那样。
