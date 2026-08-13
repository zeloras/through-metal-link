# 実験 001: チャネルスイープマップ, 3 mm 鋼板 (計画中)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · 日本語 · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **段階:** 1 (周波数マップのみ — ここではワット目標はなし; 電力は [002](../002-watts-3mm-steel/README.md))。
- **目標:** 3 mm 鋼板を通したランジュバン型振動子ペアの共振を見つける; チャネルの初回周波数応答を取得する。
- **仮説:** 38–42 kHz 付近にピーク (ランジュバン型振動子の共振), グリース+クランプ接触下で数 kHz のピーク幅。
- **駆動:** 段階1 配線 — AD9833 サイン波 (~0.6 Vpp) を TX に入力, ハーフブリッジは **なし** ([sch3](../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../hardware/schematics/sch2-receiver-stage1.png))。
- **手順:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (ハードウェアなしでパイプラインをドライランするには `--mock` を使用)。
- **成功基準:** 再現性のあるピーク (連続2回のスイープ, 中心偏差 <200 Hz)。実機で取得した CSV/PNG を `data/` に保存し、このファイルからリンクすること。
- **ボーナス測定:** 同じスイープを「グリースカップラント + クランプ」と「ドライ押し当て」で比較 — 相対振幅のみ; 絶対電圧は駆動レベルに依存し、校正するまでシミュレータのプレースホルダースケールとは比較できない。
- **対象外:** ≥0.5 W, 収穫からの LED 点灯, ハーフブリッジ立ち上げ → 実験 002。
