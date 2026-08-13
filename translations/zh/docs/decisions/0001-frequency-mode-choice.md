# ADR-0001：阶段 1 的频率模式选择

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · 中文 · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- 状态：已接受（阶段 2 后将重新评估）
- 日期：2026-07-24

## 背景
两种模式（见 docs/00-theory.md）：A — 在朗之万换能器上使用 28–40 kHz；B — 在利用壁厚共振的圆片上使用 0.6–1 MHz。

## 决策
阶段 1–2 采用模式 A。原因：更便宜（每个 $10–30）、功率更大（瓦级对几百 mW）、调谐更宽容（宽共振），而且驱动电路可以用围绕 IR2110 的半桥搭建。模式 B 等我们先把最初的几瓦功率传过去之后再上——作为高速数据的独立分支。

## 后果
阶段 3 的数据速率会较慢（kbit/s）——对传感器节点来说足够了。ADS1115 ADC（860 SPS）在整流器之后处理 40 kHz 的包络没问题，但不能直接采样——直接采样推迟到模式 B（需要不同的 ADC）。

阶段 1（扫频）仅使用弱 DDS 驱动；阶段 2（瓦级功率）是单独的实验和调试（[experiments/002](../../experiments/002-watts-3mm-steel/README.md)）。在 002 完成测量之前，仿真器的功率频带仍只是目标值。
