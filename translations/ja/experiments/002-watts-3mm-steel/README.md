# 実験002：3 mm 鋼板を通した初めてのワット級電力（計画中）

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · 日本語 · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **段階:** 2（[001](../001-sweep-map-3mm-steel/README.md) で見つけた共振点における既知負荷への電力）。
- **目標:** ハーフブリッジドライバと整合トランスを用いて、3 mm 鋼板を通して実際の DC 電力を測定する。
- **仮説:** 同一ロットのランジュバン振動子ペア、グリス＋クランプ（またはエポキシ）接触、および同調済み整合トランスを用いれば、抵抗負荷に対して段階1のピークで ≥0.5 W が達成可能である。（文献のマルチワット/kW 級の数値は異なるトランスデューサと接合方法によるものであり、上限として扱い、合格基準とはしない。）
- **前提条件:**
  - 実験001が完了している（再現性のあるピーク、周波数が記録済み）。
  - ドライバ電力印可前にRXチェーンにTVSを実装済み（[docs/02-safety.md](../../docs/02-safety.md)）。
  - ドライバ立ち上げ手順に従っている（[hardware/driver/README.md](../../hardware/driver/README.md)）。
- **セットアップ（最小構成）:**
  - TX: Pi → AD9833 方形波 → デッドタイムシェーパ → IR2110 ハーフブリッジ → 整合トランス → 鋼板にクランプされたランジュバン（[sch1](../../hardware/schematics/sch1-driver-halfbridge.png)）。
  - 壁: 3 mm 鋼板、接触方法を記録（グリス＋クランプ / エポキシ / その他）。
  - RX: ランジュバン → ショットキーブリッジ → 既知の R_load（パワーレジスタ）および/または LED；ブリッジ後の V_dc と I_dc を測定（[sch2](../../hardware/schematics/sch2-receiver-stage1.png) のトポロジ、ADCのみではなく負荷を接続）。
- **手順（概要）:**
  1. 音響電力を確認せずに、PSU 電流制限 0.2 A で電気的立ち上げを行う。
  2. TX/RX をクランプし、駆動周波数を実験001のピークに設定する。
  3. 電流制限をゆっくり上げる；PSU の V/I、MOSFET/トランスの温度、負荷の V_dc と I_dc を記録する。
  4. P_load = V_dc · I_dc。任意：P_load が判明した後、LED のデモ写真を1枚撮影する。
  5. 冷却後にもう1回繰り返す；ピーク周波数は温度でドリフトする可能性がある — 電力が低下した場合はミニスイープで再確認する。
- **成功基準:**
  1. 記録された周波数と接触方法で、3 mm 鋼板を通して P_load ≥ 0.5 W。
  2. 同じクランプ/カップラント条件下で、2回の試行が P_load で ~20% 以内に一致する（桁レベルの安定性であり、まだ計量グレードではない）。
  3. LED（またはその他の負荷）の写真 + CSV/ログを `data/` 配下にこのファイルからリンクする。
- **失敗もデータ:** P_load が ≪ 0.5 W のままであれば、ペアの Δf（001より）、接触方法、トランス巻数比、波形を記録する — それは次の ADR への入力であり、シミュレータを黙って書き換える理由ではない。
