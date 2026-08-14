# 試験装置の回路図

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · 日本語 · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| ファイル | 内容 | ステージ |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | ドライバ: IR2110 + 2×IRF540、ブートストラップ、整合トランス | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | レシーバ: 4×SS14 ブリッジ → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | ピン配置: Pi ↔ AD9833 ↔ 圧電素子ペア ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | ノード: RX → GY-LTC3588 → スーパーキャパシタ → ESP32 (+ 負荷変調) | 4 |

これらは**ブレッドボード・プロトタイプ**の回路図です（部品値は出発点であり、オシロスコープで調整する箇所には `*` を付けています）。プロトタイプが実機で検証された後、PCBレイアウト付きのKiCadプロジェクトを公開予定です — [driver/README.md](../driver/README.md) で約束した通りです。
