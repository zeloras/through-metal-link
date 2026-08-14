# レシーバー

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · 日本語 · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

回路図: [ステージ1 — sch2](../schematics/sch2-receiver-stage1.png) · [ステージ4 — sch4](../schematics/sch4-receiver-node.png) ([../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py) で生成)

- ステージ1（測定）: ランジュバン振動子 RX（両リードはフローティング — グラウンドしないこと！）→ ショットキーブリッジ (4×SS14) → RCフィルタ (10k || 100n) → 5 V TVS → **47 kΩ 直列** → ADS1115 A0（この抵抗はADCの保護ダイオードへの電流を制限する: TVSは入力の絶対最大定格より約9 V高くでクランプする）。
- ステージ2（ワット）: RX → 同じブリッジ → 既知の抵抗負荷（および/またはLED）、ブリッジ後のDC電圧・電流を測定；電力はその負荷への V·I。プロトコル: [experiments/002](../../experiments/002-watts-3mm-steel/README.md)。
- ステージ4（ノード）: RX → GY-LTC3588 **PZ1/PZ2 に直接接続**（ブリッジはLTC3588-1に内蔵、外部は不要）→ 1 F スーパーキャパシタ → ESP32（ディープスリープ + デューティサイクル）。負荷変調 — **DC側**（モジュールのVINピン、sch4を参照）で 2N7002 + 100 Ω；AC圧電素子の両端に単一のMOSFETを並べるだけでは機能しない — ボディダイオードが半波をショートする (docs/03)。

重要: 最初の電源投入前にTVSを必ず取り付けること — 共振時のオープン状態の圧電素子は数十〜数百ボルトを出力する。ブリッジ後のDC側 — 単方向 SMBJ5.0A；ノードの圧電素子（AC）の両端 — 双方向 SMBJ15CA のみ。
