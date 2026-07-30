# メタルウォールを貫く超音波パワーおよびデータ転送プラットフォーム

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [中文](../zh/README.md) · 日本語

ガレージグレードの手段を使用して、固体メタルウォールを貫く超音波パワーおよびデータ転送のオープンプラットフォーム — 「鋼材に単一の穴なし」。

**ステータス:** ステージ 0 — 準備中 · リポジトリは最初の再現可能な結果が出るまで非公開 · ショッピングリスト: [QUICKSTART.md](../../QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml)

ドキュメントはマルチリンガルです。英語はプライマリ言語であり、カノニカルパスにあります。他の言語は、[translations/](..) の下に同一のファイル名でミラーリングされています。任意の言語を編集すると、CI が翻訳してコミットします (詳細は [CONTRIBUTING.md](../../CONTRIBUTING.md) を参照してください)。

<p align="center"><img src="../../docs/img/sim0-rig-sketch.png" alt="ステージ 1 ラック: Pi → DDS → ハーフブリッジ → トランスフォーマー → ピエゾ TX | ステール | ピエゾ RX → ブリッジ → ADC → Pi" width="900"></p>

## 概要

ラジオ波はメタルを通過しません (ファラデーケージ)。ケーブルの貫通は穴、シール、および故障点を意味します。超音波は、メタルを通過することができます。メタルウォールの両側にピエゾ要素を配置することで、パワーおよびデータのチャネルを作成できます。研究文献は、すでに物理学的証明を提供しています (RPI: 50 W + 12 Mbit/s を 63.5 mm の鋼材を通過; NASA JPL: 5 mm のチタンを通過する約 kW) — これらは、専門のハードウェアを使用した存在証明であり、このリポジトリのガレージ BOM ではありません。基礎となる特許は、すでに期限切れになっています。オープンで再現可能なプラットフォームはまだ存在しません — このリポジトリは、ステージ 2 で測定された後、**3〜5 mm の鋼材を通過するワットクラスのパワーと kbit/s のデータ** で構築しています。

## ロードマップ

| ステージ | デリバリー | 成功基準 | 予想 |
| --- | --- | --- | --- |
| 1. スイープマップ | "ランジュバン-3 mm ステール-ランジュバン" チャネルの周波数特性 | 共鳴ピークが見つかり、[experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md) にプロットされる | [sim1](../../docs/img/sim1-sweep-contacts.png)、[sim2](../../docs/img/sim2-pair-mismatch.png) |
| 2. ワット | ロードでの共鳴でのパワー | 3 mm の鋼材を通過する ≥0.5 W、プロトコルは [experiments/002](../../experiments/002-watts-3mm-steel/README.md) に記載 | [sim4](../../docs/img/sim4-power-budget.png) |
| 3. データ | 同じペア上の FSK/OOK | ≥1 kbit/s のエラーなし | [sim5](../../docs/img/sim5-ook-datarate.png) |
| 4. ノード | ESP32 + センサーを溶接したボックス、サウンドによってのみ給電およびテレメータ | ≥1 時間の自律運転 | [sim4](../../docs/img/sim4-power-budget.png) |
| 5. 発表 | リポジトリが公開され、記事/チュートリアルが作成される | 第三者による再現 | — |

## リポジトリマップ

以下の各ブロックは、内部に十分なダイジェストと、フルドキュメントへのリンクを含みます。

<details>
<summary><b>🛒 ゼロから動くラッグまで: どんなものを買い、どのような順序で</b> — <a href="QUICKSTART.md">QUICKSTART.md</a></summary>

**予算:** ~210 ドル (最小)、~300 ドル (快適) (Pi、ソルダリングアイロン、ベンチパワーサプライをすでに所有している場合は ~120 ドルを削減します)。ツール (~120 ドル)、ラッグ電子 (~70 ドル、[フル BOM](../../hardware/bom/bom-stage1.csv))、メカニクス (~20 ドル) の 3 つのバスケット。オプションですが、強く推奨されています: USB オシロスコープ (~60-80 ドル)。

**クリティカルパス — AliExpress 出荷 (3-4 週間):** 電子機器を 1 日目に注文します。重要な決定: **同じバッチの 4 つのランジュバン トランスデューサー** を購入します — スイープは最適なペアを選択します ([why](../../docs/img/sim2-pair-mismatch.png))。

**出荷中:** ハードウェアなしでパイプラインを実行します — 

```bash
python3 software/sweep-map/sweep_map.py --mock
```

**完了時 (ステージごと):** ステージ 1 — スイープピークが 2 つの実行で <200 Hz 以内に再現します ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md))。ステージ 2 — 3 mm の鋼材と RX 側の LED を通過する ≥0.5 W のロードにパワーを供給します ([experiments/002](../../experiments/002-watts-3mm-steel/README.md))。

</details>

<details>
<summary><b>📚 1 分で理解する理論</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

TX 側のピエゾ要素はウォールに押し付けられており、ロングィチューダル波を駆動し、RX 側のピエゾ要素はそれを電気に戻します。鋼材の中での音速: ~5900 m/s。

2 つの動作モード:

| モード | 周波数 | 共鳴セット | 結果 | 状態 |
| --- | --- | --- | --- | --- |
| **A** — ランジュバン トランスデューサー | 40 kHz | トランスデューサー ペア (ウォール ≪ λ — "膜") | ワット、kbit/s | 開始モード (ステージ 1-4、[ADR-0001](../../docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — ディスク | 0.6-1 MHz | ウォールの厚さ共鳴 ([コーム](../../docs/img/sim3-thickness-comb.png)) | 数百 mW、数百 kbit/s | 最初のワットの後に分岐; 自動周波数追跡が必要 |

主な損失: ペア内での共鳴ミスマッチ (±1 kHz の安価なランジュバン トランスデューサー)、音響接触の品質 (エポキシ > グリース クーラント + クランプ > 乾いた圧力)、ミスアライメント、温度による共鳴ドリフト。すべての答えは同じです: **セットアップの変更前にスイープマップ**。

</details>

<details>
<summary><b>📈 ラッグが示すべきもの: シミュレータからの期待プロット</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

半経験的チャネルモデル (FEM ではありません、**ラボデータではありません** — "スイープの見え方と目標" のための直感)。仮定は `channel_sim.py` (ロード Q≈40、接触 k 因子、チェーン η≤40%) に明示的に記載されています。再生成するには: `python3 channel_sim.py --out ../../docs/img`。

**ステージ 1 — スイープ。** ~40 kHz 近辺の狭いピーク; モデルのプレイスホルダー接触乗数はグリース:乾いた:ギャップ = 1 : 0.25 : 0.02 (つまり、グリース ≈4× 乾いたおよび ≈50× エアギャップ)。ピークがない場合、接触またはペアに問題があります:

<img src="../../docs/img/sim1-sweep-contacts.png" width="720">

**4 つのランジュバン トランスデューサーを 2 つではなく購入する理由。** Q≈40 の下で、ペア内での 1.5 kHz の共鳴ミスマッチはモデルパワーを ~10 倍低下させます:

<img src="../../docs/img/sim2-pair-mismatch.png" width="720">

**ステージ 3 — データ。** OOK は共振器のリングに当たる (モデル Q~40 → τ≈0.3 ms): 1 kbit/s はクリーンですが、5 kbit/s のときアイは閉じられます。より速くするにはモード B が必要です:

<img src="../../docs/img/sim5-ook-datarate.png" width="720">

**レシーバパワーバジェット。** 影付きの帯は **ターゲット** (モード A 0.5-5 W if ステージ 2 が着陸する; モード B は低い) です。現実的な最初のロードはデューティサイクル ESP32 / BLE / LED; Wi-Fi は連続的な約束ではなく、ピークドローマーカーとして表示されます:

<img src="../../docs/img/sim4-power-budget.png" width="720">

**後で (モード B).** プレートは厚さ共鳴のコームで透明になります — 周波数を追跡する必要があります:

<img src="../../docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ セーフティ — 最初のパワーアップ前に読んでください</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **ピエゾに数十から数百ボルト** がステージ 2 ドライバーがオンラインになると適用されます — RX 側の TVS は最初のパワーアップ前に入力されます。リードから手を離してください。
2. **メインス** — ベンチパワーサプライ / アイソレーションのみを通過します。超音波クリーナードライバーボードはメインスにガルバニックに結合されています。
3. **耳** — 非実用的パワーで、メタルに押し付けられたトランスデューサーを操作します。高パワーの空中超音波をエンクロージャなしで実行しないでください。
4. **熱** — クランプされていないランジュバン トランスデューサーは数分で高パワーで過熱します。電流を上げる前にクランプします (電気的なブリングアップのみ — ドライバーの README を参照)。
5. **破片** — ピエゾセラミックは脆いです。過緊したボルトまたは衝撃は破片を意味します。機械的な作業のために安全メガネを着用してください。

最初のドライバーパワーアップ: ベンチサプライの電流制限 0.2 A; フルシーケンスは [hardware/driver/](../../hardware/driver/README.md) および [docs/02-safety.md](../../docs/02-safety.md) に記載されています。

</details>

<details>
<summary><b>🧭 先行技術と特許衛生</b> — <a href="docs/01-prior-art.md">docs/01-prior-art.md</a></summary>

すべての技術的決定は "無料" のソース (期限切れの特許、論文) に遡る必要があります。基礎: **US5982297** (エアロスペース コーポレーション — ウォールを貫くピエゾペアの基本レシピ)、**US7902943** (カリフォルニア工科大学 / JPL — シェリットのフィードスルー)、**US9361877** (オクラホマ大学 — 完全なトランシーバーシステム); すべて死亡しました。重要な論文: Lawry 2013 (50 W + 12.4 Mbit/s を 63.5 mm の鋼材を通過)、Sherrit/NASA (100 W のランプ)、Yang 2015 (調査)。

まだ生きている場合 (USのみ、~2032 年まで; ステージ 1-4 では必要ありません): RPI の OFDM 配置、RPI のフルデュプレックス スキーム、Drexel のコンフォーマル トランスデューサー。

アーキテクチャの決定は [docs/decisions/](../../docs/decisions/0001-frequency-mode-choice.md) (ADR) に記録されています。

</details>

<details>
<summary><b>🔌 ハードウェアとファームウェア</b> — hardware/, firmware/</summary>

- [hardware/bom/bom-stage1.csv](../../hardware/bom/bom-stage1.csv) — ステージ 1 ショッピングリスト。
- [hardware/schematics/](../../hardware/schematics/README.md) — **回路図** (コードから生成): ドライバー、レシーバー、Pi ピンアウト、ハーベスター ノード。
- [hardware/driver/](../../hardware/driver/README.md) — TX ドライバー: IR2110 ハーフブリッジ + 2×IRF540、マッチング トランスフォーマー (ランジュバン トランスデューサーは容量ロードです!)。KiCad ボードは、ブレッドボード プロトタイプがチェックアウトした後に来ます。
- [hardware/receiver/](../../hardware/receiver/README.md) — レシーバー、ステージごとに: ショットキー ブリッジ → ADC (ステージ 1) → ロード (ステージ 2) → LTC3588 + スーパーキャパシタ + ESP32 (ステージ 4)。
- [firmware/node-esp32/](../../firmware/node-esp32/README.md) — ステージ 4 ノード (スタブ): ディープスリープ、センサー読み取り、BLE 広告、1-5 mW の平均予算。

</details>

<details>
<summary><b>💻 ソフトウェア: 測定とシミュレーター</b> — software/</summary>

- [software/sweep-map/sweep_map.py](../../software/sweep-map/sweep_map.py) — ステージ 1 のワークホース: DDS スイープ → ADC 読み取り → CSV + 周波数応答プロット。ハードウェアなしで実行する `--mock` があります。Pi 上で: `raspi-config` → SPI と I2C を有効にする; `pip install spidev smbus2 matplotlib`。
- [software/simulator/channel_sim.py](../../software/simulator/channel_sim.py) — 期待プロットの生成 (`pip install numpy matplotlib`）。
- [data/](../../data/README.md) — 生ログ; CSV/PNG は Git に含まれず、カーキュレーテッド プロットのみが実験ディレクトリ内に Git に含まれます。

</details>

<details>
<summary><b>🗺️ どこに適用するか: バリア、チャネル、ニッチ</b> — <a href="docs/04-hybrid-channels.md">docs/04</a>, <a href="docs/05-applications-map.md">docs/05</a></summary>

ユニバーサルチャネルはありません。プラットフォームは物理学をバリアに合わせます: ピエゾアクースティクス (プライマリ: 鋼材/アルミニウムとの接触 — ワットと kbit/s)、EMAT (汚れた/熱した金属、接触なし — データ)、低周波磁気 (真空サンドイッチ壁のデュワール — ビット/秒)。誠実な死角: ゴムライニング/複合材の壁、パスの途中の気泡液。

ニッチの優先順位: **(1)** ラボ真空チャンバーとクライオスタット — オープンソースハードウェアのオーディエンス、認定不要; **(2)** 発酵タンク — 歩いてアクセスできる証明場; **(3)** 封じられたバッテリーパック — 旗艦ケース (熱暴走検出 without パックへの貫通)。レシーバーの発見と自動チューニングプロトコル (Qi の類似品): [docs/03-discovery-protocol.md](../../docs/03-discovery-protocol.md)。

</details>

<details>
<summary><b>📁 ディレクトリレイアウト</b></summary>

```
docs/            理論、先行技術、セーフティ、アプリケーション、決定ログ (ADR)
docs/img/        期待プロット (software/simulator/channel_sim.py によって生成)
hardware/        BOM、ドライバー (ハーフブリッジ)、レシーバー (整流器/ハーベスター)
firmware/        ノードファームウェア (ESP32 — ステージ 4 までスタブ)
software/        測定スクリプト (周波数応答スイープマップ) とチャネルシミュレーター
experiments/     実験プロトコル — テンプレートから、1 つのディレクトリ = 1 つの実験
data/            生ログ (大きなファイルは Git に含まれず)
```

</details>

## 原則

1. **ゼロからの再現性。** ソルダリングアイロンと ~210 ドルがあれば、誰でもこのリポジトリだけで結果を再現できます。
2. **すべての実験はプロトコルです。** "なんとなく動いた" ではありません: [experiments/TEMPLATE.md](../../experiments/TEMPLATE.md) は必須です。
3. **特許衛生。** 期限切れの層 ([docs/01-prior-art.md](../../docs/01-prior-art.md)) を基にしています。決定は [docs/decisions/](../../docs/decisions/0001-frequency-mode-choice.md) に記録されています。
4. **測定が先、意見が後。** セットアップの変更前にスイープマップ。

## ライセンスと特許

コード — Apache-2.0、ハードウェア — CERN-OHL-W v2、ドキュメント — CC-BY-4.0; フルテキストは [LICENSES/](../../LICENSES) にあります。誰でもフォークしてビルドできます。商業的に含めます。特許保護は、ライセンスの付与と報復条項、および先行技術戦略から来ます。スキームと防御公開プロトコル: [LICENSES.md](../../LICENSES.md); 貢献ルール: [CONTRIBUTING.md](../../CONTRIBUTING.md)。
