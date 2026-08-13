# 实验 001：通道扫频图，3 mm 钢板（计划中）

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · 中文 · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **阶段：** 1（仅频率图——此处无功率目标；功率见 [002](../002-watts-3mm-steel/README.md)）。
- **目标：** 找到一对 Langevin 换能器穿过 3 mm 钢板的谐振点；获取通道的首次频率响应。
- **假设：** 在 38–42 kHz 附近出现峰值（Langevin 换能器谐振），在脂耦合+夹具接触条件下峰值宽度为数千 Hz。
- **驱动：** 阶段 1 接线——AD9833 正弦波（~0.6 Vpp）送入 TX，**不使用**半桥（[sch3](../../hardware/schematics/sch3-stage1-wiring.png)、[sch2](../../hardware/schematics/sch2-receiver-stage1.png)）。
- **步骤：** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50`（使用 `--mock` 可在无硬件情况下试运行整个流程）。
- **成功标准：** 可复现的峰值（连续两次扫频，中心偏差 <200 Hz）。将 CSV/PNG 保存到 `data/` 下，并在真实数据生成后从本文件中链接它们。
- **附加测量：** 在"脂耦合剂+夹具"与"干压接触"两种条件下进行相同扫频——仅比较相对幅值；绝对电压取决于驱动电平，在校准之前无法与仿真器的占位标度进行比较。
- **不在范围内：** ≥0.5 W、能量收集点亮 LED、半桥调试 → 实验 002。
