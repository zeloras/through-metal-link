# 实验 001：通道扫描图，3 mm 钢板（计划中）

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · 中文 · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **阶段：** 1（仅频率图，无功率目标；功率为 [002](../002-watts-3mm-steel/README.md)）。
- **目标：** 找到朗兹文换能器对通过 3 mm 钢板的谐振；获得通道的首个频率响应。
- **假设：** 在 38-42 kHz 附近有一个峰值（朗兹文换能器谐振），峰值宽度在几 kHz 范围内，使用润滑剂和夹持接触。
- **驱动：** 第一阶段连接 — AD9833 正弦波（~0.6 Vpp）输入 TX，**无** 半桥 ([sch3](../../hardware/schematics/sch3-stage1-wiring.png)，[sch2](../../hardware/schematics/sch2-receiver-stage1.png)）。
- **程序：** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50`（使用 `--mock` 进行模拟运行，测试管道而不使用硬件）。
- **成功标准：** 可重复的峰值（连续两次扫描，中心偏差 <200 Hz）。将 CSV/PNG 文件保存在 `data/` 下，并在文件中链接它们。
- **额外测量：** 使用“润滑剂和夹持”与“干燥按压”进行相同的扫描 — 相对幅度；绝对电压取决于驱动级别，在校准之前与模拟器的占位符刻度不相容。
- **超出范围：** ≥0.5 W，LED 从收获，半桥启动 → 实验 002。
