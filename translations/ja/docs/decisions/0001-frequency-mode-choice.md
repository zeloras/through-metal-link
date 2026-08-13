# ADR-0001: Stage 1 の周波数モード選択

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · 日本語 · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- ステータス: 承認済み（Stage 2 完了後に再検討）
- 日付: 2026-07-24

## 背景
2つのモードがある（docs/00-theory.md を参照）: A — Langevin トランスデューサで 28–40 kHz、B — 壁厚の共振に乗るディスクで 0.6–1 MHz。

## 決定
Stage 1–2 はモード A で進める。理由: 安価（1個 $10–30）、高出力（数百 mW に対してワット級）、チューニングが容易（広い共振）、そしてドライバは IR2110 を中心としたハーフブリッジで構築できる。モード B は最初のワット級電力を通した後に追加する — 高速データ通信用の独立ブランチとして。

## 結果
Stage 3 のデータは低速（kbit/s）になる — センサーノードには十分。ADS1115 ADC（860 SPS）は整流後の 40 kHz エンベロープには対応できるが、直接サンプリングには不十分 — 直接サンプリングはモード B まで保留（別の ADC が必要）。

Stage 1（スイープ）は弱い DDS ドライブのみを使用する。Stage 2（ワット級）は別の実験およびブリングアップである（[experiments/002](../../experiments/002-watts-3mm-steel/README.md)）。シミュレータの電力バンドは 002 が測定されるまで目標値のままである。
