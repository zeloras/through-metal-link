# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · 日本語 · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

固体金属壁を通じた超音波電力・データ転送のためのオープンプラットフォーム — 「鋼板を一枚の穴も開けずに貫通」、ガレージレベルの手段で構築。

**今すぐ試す（ハードウェア不要）:** `python3 software/sweep-map/sweep_map.py --mock`

**ステータス:** ステージ 0 — 準備段階 · 💰 **[最初の独立ビルドに$250の報奨金](https://github.com/zeloras/through-metal-link/issues)** · 購入リスト: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

ドキュメントは多言語対応です: 英語が一次言語であり正規パスに配置されています。その他の言語はすべて [translations/](..) 配下にツリー構造をミラーリングします。どの言語でも編集可能 — CIが翻訳して残りの言語をコミットします（[CONTRIBUTING.md](CONTRIBUTING.md) を参照）。

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Stage 1 rig: Pi → DDS → half-bridge → transformer → piezo TX | steel | piezo RX → bridge → ADC → Pi" width="900"></p>

## ひとことで言うと

電波は金属を透過しません（ファラデーケージ）。また、ケーブルの貫通は、穴、シール、そして故障点を意味します。一方、超音波は金属を問題なく通り抜けます。壁の両側に圧電素子を配置すれば、それが電力とデータのチャネルになります。実験室の文献では、すでに本格的なレベルで物理が証明されています（RPI：63.5 mmの鋼鉄を通して50 W + 12 Mbit/s、NASA JPL：5 mmのチタンを通して最大〜kW）。これらは特殊なハードウェアによる存在証明であり、このリポジトリのガレージレベルのBOMではありません。基礎特許はすでに失効しており、オープンで再現可能なプラットフォームはまだ存在しません。このリポジトリは、ステージ2の測定が完了次第、**3〜5 mmの鋼鉄を通したワット級の電力と kbit/s のデータ**から始まるプラットフォームを構築しています。

## ロードマップ

| 段階 | 成果物 | 成功基準 | 期待値 |
|---|---|---|---|
| 1. スイープマップ | 「ランジュバン–3 mm鋼板–ランジュバン」チャネルの周波数応答 | ペア共振を発見、プロットは [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) に掲載 | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. 電力 | 共振時の負荷への電力 | 3 mm鋼板を通じて ≥0.5 W、プロトコルは [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. データ | 同一ペアでの FSK/OOK | ≥1 kbit/s のエラーフリー通信 | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. ノード | ESP32 + センサを密閉溶接ボックスに収め、音波のみで給電・テレメトリ | ≥1 h の自律動作 | [sim4](docs/img/sim4-power-budget.png) |
| 5. 公開 | リポジトリを公開、記事/ハウツー | 第三者による再現 | — |

## リポジトリマップ

python3 software/sweep-map/sweep_map.py --mock
```

**完了の定義（ステージごと）：** ステージ1 — スイープのピークが2回の実行で<200 Hz以内に再現される（[experiments/001](experiments/001-sweep-map-3mm-steel/README.md)）；ステージ2 — 3 mmの鋼板を通して既知の負荷に≥0.5 Wが供給され、RX側からLEDが点灯する（[experiments/002](experiments/002-watts-3mm-steel/README.md)）。

</details>

<details>
<summary><b>📚 1分でわかる理論</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

圧電素子TXは壁に押し当てられ、縦波を壁に送り込みます；反対側の圧電素子RXがそれを再び電気に変換します。鋼の音速：〜5900 m/s。

2つの動作モード：

| モード | 周波数 | 共振の決定要因 | 出力 | ステータス |
|---|---|---|---|---|
| **A** — Langevinトランスデューサ | 40 kHz | トランスデューサのペア（壁 ≪ λ — 「膜」） | ワット、kbit/s | 開始モード（ステージ1〜4、[ADR-0001](docs/decisions/0001-frequency-mode-choice.md)） |
| **B** — ディスク | 0.6–1 MHz | 壁の厚み共振（[コム](docs/img/sim3-thickness-comb.png)） | 数百mW、数百kbit/s | 最初のワット以降の分岐；自動周波数追尾が必要 |

主な損失：ペア内の共振の不一致（安価なLangevinトランスデューサで±1 kHz）、音響接触の品質（エポキシ > グリースカップラント＋クランプ > ドライ圧接）、位置ずれ、温度による共振ドリフト。これらすべてに対する答えは同じです：**セットアップを変更するたびにスイープマップを作成する**。

</details>

<details>
<summary><b>📈 リグが示すべきこと：シミュレータからの期待値プロット</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

半経験的なチャネルモデル（FEMではなく、**ラボデータでもない** — 「スイープがどのように見えるべきか、何を目指すべきか」の直感）。仮定は `channel_sim.py` に明記されています（ロードされたQ≈40、接触kファクター、チェーンη≤40%）。次のコマンドで再生成します：`python3 channel_sim.py --out ../../docs/img`。

**ステージ1 — スイープ。** 〜40 kHz付近の狭いピーク；モデルのプレースホルダ接触乗数は グリース:ドライ:ギャップ = 1 : 0.25 : 0.02 です（つまり、グリースはドライの約4倍、エアギャップの約50倍）。ピークがない場合は、接触またはペアに問題があります：

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**なぜ2つではなく4つのLangevinトランスデューサなのか。** Q≈40では、ペア内の1.5 kHzの共振不一致によりモデルの電力が約10倍低下します：

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**ステージ3 — データ。** OOKは共振器のリンギングに直面します（モデルQ~40 → τ≈0.3 ms）：1 kbit/sはクリーンですが、5 kbit/sではアイが閉じます。より速くするにはモードBが必要です：

<img src="docs/img/sim5-ook-datarate.png" width="720">

**受信側の電力予算。** 影付きの帯は**ターゲット**です（ステージ2が成功した場合のモードAは0.5〜5 W；モードBはそれ以下）。現実的な最初の負荷はデューティサイクル動作のESP32 / BLE / LEDです；Wi-Fiは連続的な約束ではなく、ピーク消費のマーカーとして示されています：

<img src="docs/img/sim4-power-budget.png" width="720">

**後日用（モードB）。** プレートは厚み共振のコムで透過になります — 周波数を追尾する必要があります：

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ 安全 — 最初の電源投入前に読むこと</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **ステージ2のドライバがオンラインになると圧電素子に数十〜数百ボルトの電圧**がかかります — 最初の通電実行の前に受信側にTVSを取り付けてください；リード線には手を触れないでください。
2. **商用電源** — 直流安定化電源 / 絶縁トランスを通してのみ接続してください；超音波洗浄機のドライバボードは商用電源にガルバニック接続されています。
3. **耳** — かなりの電力の場合、金属に押し当てた状態でトランスデューサを動作させてください；筐体なしで高出力の空中超音波を絶対に動作させないでください。
4. **熱** — クランプされていないLangevinトランスデューサは、電力をかけると数分で過熱します；電流を上げる前にクランプしてください（短時間の低電流の電気的な立ち上げのみ — ドライバのREADMEを参照）。
5. **破片** — 圧電セラミックは脆いです：ボルトの締めすぎや衝撃は破片を意味します；機械的な作業には安全メガネを着用してください。

</details>

docs/            理論、先行技術、安全性、アプリケーション、決定ログ (ADR)
docs/img/        期待値プロット (software/simulator/channel_sim.py で生成)
hardware/        BOM、ドライバ (ハーフブリッジ)、レシーバ (整流器/ハーベスタ)
firmware/        ノードファームウェア (ESP32 — ステージ4までスタブ)
software/        測定スクリプト (周波数応答スイープマップ) およびチャネルシミュレータ
experiments/     実験プロトコル — テンプレートから作成、1ディレクトリ = 1実験
data/            生ログ (大きなファイルはgitに含めない)
```

</details>

## 原則

1. **ゼロからの再現性。** はんだごてと約210ドルがあれば、誰でもこのリポジトリ単独で結果を再現できる。
2. **すべての実験はプロトコル。** 「なんとなく動いた」は不可: [experiments/TEMPLATE.md](experiments/TEMPLATE.md) が必須。
3. **特許の健全性。** 期限切れの先行技術層 ([docs/01-prior-art.md](docs/01-prior-art.md)) の上に構築し、決定は [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md) に記録する。
4. **測定優先、意見は次。** チャネルに関する結論を出す前に、スイープマップを先に。

## ライセンスと特許

コード — Apache-2.0、ハードウェア — CERN-OHL-W v2、ドキュメント — CC-BY-4.0。全文は [LICENSES/](../../LICENSES) にあります。誰でもこれをフォークして発展させることができます（商用利用も含む）。特許保護は、ライセンスの許諾条項および報復条項に加え、先行技術戦略によって確保されます。完全なスキームおよび防御的公開プロトコルについては [LICENSES.md](LICENSES.md) を、貢献ルールについては [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。
