# 実験 001: チャネル スイープ マップ、3 mm スチール (計画中)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · 日本語

- **ステージ:** 1 (周波数マップのみ — ここではワット目標なし; 電力は [002](../../../../experiments/002-watts-3mm-steel/README.md) です)。
- **目標:** 3 mm プレートを介したランジュバン トランスデューサー ペアの共振を検出する; チャネルの最初の周波数応答を取得する。
- **仮説:** 38–42 kHz (ランジュバン トランスデューサー共振) 周辺のピーク、グリース + クランプ接触下で数 kHz のピーク幅。
- **ドライブ:** ステージ 1 接続 — AD9833 サイン波 (~0.6 Vpp) を TX に入力、**半橋はなし** ([sch3](../../../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png))。
- **手順:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (ハードウェアを使用せずにパイプラインを実行するには `--mock` を使用)。
- **成功基準:** 再現可能なピーク (2 つのスイープを連続して実行し、中心偏差 <200 Hz)。実際の場合、`data/` 下に CSV/PNG を保存し、このファイルからリンクする。
- **ボーナス測定:** グリース クーラント + クランプとドライ プレス オンの同じスイープ — 相対アンプリチュードのみ; 絶対ボルトはドライブ レベルとシミュレーターのプレイスホルダー スケールに依存し、較正されるまで比較できない。
- **範囲外:** ≥0.5 W、LED からハーベスト、半橋のセットアップ → 実験 002。
