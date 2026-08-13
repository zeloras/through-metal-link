# ADR-0001: 第一阶段频率模式选择

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · 中文 · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- 状态：已接受（将在第二阶段后重新审视）
- 日期：2026-07-24

## 背景
两个模式（见 docs/00-theory.md）：A — 28–40 kHz 的 Langevin 传感器，B — 0.6–1 MHz 的厚度谐振壁上的圆盘。

## 决策
第一和第二阶段采用模式 A。原因：更便宜（每个 10–30 美元），更强大（瓦特与数百毫瓦），调谐更宽容（宽谐振），并且驱动器可以使用 IR2110 周围的半桥构建。模式 B 将在我们获得第一瓦特电力后实施 —— 作为高速度数据的单独分支。

## 后果
第三阶段的数据将较慢（kbit/s）——足够用于传感器节点。ADS1115 ADC（860 SPS）适用于 40 kHz 后的整流器包络，但不适用于直接采样——直接采样将推迟到模式 B（需要不同的 ADC）。

第一阶段（扫描）仅使用弱 DDS 驱动；第二阶段（瓦特）是一个单独的实验和启动（[experiments/002](../../experiments/002-watts-3mm-steel/README.md)）。模拟器功率带将保持目标，直到 002 被测量。
