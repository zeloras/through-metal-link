# テストリグ回路図

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · 日本語

回路図はコードから生成されます — [render_schematics.py](../../../../hardware/schematics/render_schematics.py) は設計ソース (schemdraw) としても機能します。変更を行うには、スクリプトを編集し、再生成します。

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| ファイル | 内容 | ステージ |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | ドライバ: IR2110 + 2×IRF540, ブートストラップ, マッチングトランス | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | 受信機: 4×SS14 ブリッジ → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | ピンアウト: Pi ↔ AD9833 ↔ ピエゾペア ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | ノード: RX → GY-LTC3588 → イオンストール → ESP32 (+ ロードモジュレーション) | 4 |

これらは **ブレッドボードプロトタイプ** 回路図です (コンポーネント値は開始点であり、オシロスコープで調整される場所は `*` でマークされています)。KiCad プロジェクトに基づく PCB レイアウトは、プロトタイプが実際に検証された後、[driver/README.md](../driver/README.md) で約束したように提供されます。
