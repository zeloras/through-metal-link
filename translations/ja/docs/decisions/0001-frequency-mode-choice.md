# ADR-0001: ステージ1の周波数モード選択

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [中文](0001-frequency-mode-choice.md) · 日本語

- ステータス: ACCEPTED (ステージ2後再検討)
- 日付: 2026-07-24

## コンテキスト
2つのモード (docs/00-theory.md参照): A — ランジュバン・トランスデューサーを使用した28–40 kHz, B — ディスクを使用した壁の厚さの共振周波数0.6–1 MHz.

## 決定
ステージ1–2ではモードAを使用する。理由: 費用が安い ($10–30 個別), 出力が高い (ワット対数百 mW), チューニングに寛容性が高い (広い共振), ドライバーがIR2110を中心としたハーフブリッジから構築できる。モードBは、最初のワットを通過させた後に別のブランチとして実装される — 高速データ用.

## 結果
ステージ3でのデータ速度は遅い (kbit/s) — センサー ノードに十分。ADS1115 ADC (860 SPS) は、40 kHz後の整流器後のエンベロープに適しているが、直接サンプリングには適していない — 直接サンプリングはモードB (別のADCが必要) まで延期される.

ステージ1 (スイープ) では、弱いDDSドライブのみを使用する。ステージ2 (ワット) は、別の実験およびブリングアップ ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)) である。シミュレータのパワーバンドは、002が測定されるまでターゲットとして残る。
