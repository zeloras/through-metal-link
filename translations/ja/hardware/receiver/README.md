# 受信機

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · 日本語 · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

回路図: [ステージ 1 — sch2](../schematics/sch2-receiver-stage1.png) · [ステージ 4 — sch4](../schematics/sch4-receiver-node.png) (生成元: [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

- ステージ 1 (測定): ランジュバン トランスデューサ RX (両方のリードは浮遊 — グラウンドに接続しないでください) → ショットキー ブリッジ (4×SS14) → RC フィルタ (10k || 100n) → 5 V TVS → **47 kΩ シリーズ** → ADS1115 A0 (抵抗器は、ADC の保護ダイオードへの電流を制限します: TVS は入力の絶対最大値より約 9 V 上方でクランプします)。
- ステージ 2 (ワット): RX → 同じブリッジ → 既知の抵抗負荷 (および/または LED) → ブリッジ後の DC 電圧と電流を測定; 負荷への電力は V·I です。プロトコル: [experiments/002](../../experiments/002-watts-3mm-steel/README.md)。
- ステージ 4 (ノード): RX → GY-LTC3588 **直結 PZ1/PZ2** (LTC3588-1 にブリッジが内蔵されているため、外部ブリッジは不要) → 1 F イオンストル → ESP32 (ディープ スリープ + デューティ サイクル)。負荷変調 — 2N7002 + 100 Ω **DC 側** (モジュールの VIN ピン、sch4 参照); AC パイエゾに単一の MOSFET を使用することは機能しません — ボディ ダイオードが半波をショートします (docs/03)。

重要: 最初の電源投入前に TVS を装着してください。共振時のオープン パイエゾは数十から数百ボルトの電圧を出力します。ブリッジ後の DC 側 — 単方向の SMBJ5.0A; ノードのパイエゾ (AC) 跨ぐ — 仅 対向の SMBJ15CA。
