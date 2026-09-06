# 金属貫通リンク

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · 日本語 · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

固体金属壁を通じた超音波電力・データ転送のためのオープンプラットフォーム — 「鋼板を貫く、一つの穴も開けずに」、ガレージレベルの手段で構築。

**今すぐ試す（ハードウェア不要）:** `python3 software/sweep-map/sweep_map.py --mock`

**以下のパスで参加:**
- **A — ドライラン:** モックスイープ + [シミュレータ](../../software/simulator/channel_sim.py)（ベンチ不要）
- **B — ビルドステージ1:** [QUICKSTART.md](QUICKSTART.md) → [experiments/001](experiments/001-sweep-map-3mm-steel/README.md)
- **C — ハードウェアなしで貢献:** 先行技術 / ドキュメント / 翻訳 / ADRコメント（[CONTRIBUTING.md](CONTRIBUTING.md)）

**ステータス:** ステージ0 — 準備中 · **ハードウェア検証はまだなし**（シミュレータのみ; 最初のビルドに報奨金） · 💰 **[$250 報奨金](https://github.com/zeloras/through-metal-link/issues/5)** · 買い物リスト: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

ドキュメントは多言語対応: 英語が一次言語であり正規パスに配置; その他の言語はすべて[translations/](..)配下にツリーをミラー。どの言語でも編集可能 — CIが翻訳して残りをコミットします（[CONTRIBUTING.md](CONTRIBUTING.md)を参照）。

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Stage 1 rig: Pi → DDS → half-bridge → transformer → piezo TX | steel | piezo RX → bridge → ADC → Pi" width="900"></p>

## 1段落でのアイデア

電波は金属を透過しません（ファラデーケージ）し、ケーブルの貫通は穴、シール、そして故障点を意味します。一方、超音波は金属を問題なく通過します。壁の両側に圧電素子を配置すれば、それが電力とデータのチャネルになります。実験室の文献では、すでに本格的なレベルで物理現象が証明されています（RPI：63.5 mmの鋼鉄を通して50 W + 12 Mbit/s、NASA JPL：5 mmのチタンを通して最大約1 kW）。これらは専用ハードウェアによる存在証明であり、このリポジトリのガレージレベルのBOMではありません。基礎特許はすでに失効しており、オープンで再現可能なプラットフォームはまだ存在しません。このリポジトリは、ステージ2の測定が完了次第、**3〜5 mmの鋼鉄を通したワット級の電力とkbit/sのデータ**から始まるプラットフォームを構築しています。

## ロードマップ

| ステージ | 成果物 | 成功基準 | 期待値 |
|---|---|---|---|
| 1. スイープマップ | 「ランジュバン–3 mm鋼板–ランジュバン」チャネルの周波数応答 | ペア共振を発見、プロットは[experiments/001](experiments/001-sweep-map-3mm-steel/README.md)に掲載 | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. ワット | 共振時の負荷への電力 | 3 mmの鋼板を通じて≥0.5 W、プロトコルは[experiments/002](experiments/002-watts-3mm-steel/README.md)に掲載 | [sim4](docs/img/sim4-power-budget.png) |
| 3. データ | 同一ペアでのFSK/OOK | エラーフリーで≥1 kbit/s | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. ノード | 溶接密閉箱内のESP32 + センサ、音響単独で給電・テレメトリ | ≥1 hの自律動作 | [sim4](docs/img/sim4-power-budget.png) |
| 5. 出版 | 初の独立再現 + 記事/ハウツー + Zenodoスナップショット | 第三者による再現が文書化されている | — |

## リポジトリマップ

python3 software/sweep-map/sweep_map.py --mock
```

**完了の目安（ステージ別）：** ステージ1 — スイープのピークが2回の実行で200 Hz以内で再現される（[experiments/001](experiments/001-sweep-map-3mm-steel/README.md)）；ステージ2 — 3 mmの鋼板と既知の負荷を通して≥0.5 W、RX側でLEDが点灯する（[experiments/002](experiments/002-watts-3mm-steel/README.md)）。

</details>

<details>
<summary><b>📚 1分でわかる理論</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

圧電TXを壁に押し当てて縦波を壁に送り込み、反対側の圧電RXがそれを電気に戻します。鋼中の音速：約5900 m/s。

2つの動作モード：

| モード | 周波数 | 共振の決定要因 | 得られるもの | 状態 |
|---|---|---|---|---|
| **A** — Langevinトランスデューサ | 40 kHz | トランスデューサのペア（壁 ≪ λ — 「膜」） | ワット、kbit/s | 開始モード（ステージ1–4、[ADR-0001](docs/decisions/0001-frequency-mode-choice.md)） |
| **B** — ディスク | 0.6–1 MHz | 壁の厚み共振（[コム](docs/img/sim3-thickness-comb.png)） | 数百mW、数百kbit/s | 最初のワット達成後の分岐；自動周波数追尾が必要 |

主な損失：ペア内の共振ミスマッチ（安価なLangevinトランスデューサで±1 kHz）、音響接触の品質（エポキシ > グリースカプラント＋クランプ > ドライ圧接）、ミスアライメント、温度による共振ドリフト。これらすべてに対する答えは同じです：**セットアップを変更するたびにスイープマップを作成する**。

</details>

<details>
<summary><b>📈 装置が示すべきもの：シミュレータからの期待プロット</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

半経験的チャネルモデル（FEMではなく、**実験室データでもない** — 「スイープがどのように見えるべきか、何を狙うべきか」の直感用）。前提は `channel_sim.py` に明示されています（ロードされたQ≈40、接触kファクタ、チェーンη≤40%）。再生成コマンド：`python3 channel_sim.py --out ../../docs/img`。

**ステージ1 — スイープ。** 約40 kHz付近の狭いピーク；モデルのプレースホルダ接触乗数はグリース：ドライ：ギャップ = 1 : 0.25 : 0.02（つまりグリースはドライの約4倍、エアギャップの約50倍）。ピークがない場合は接触またはペアに問題があります：

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Langevinトランスデューサを2個ではなく4個にする理由。** Q≈40では、ペア内の1.5 kHzの共振ミスマッチがモデル上の電力を約10分の1に低下させます：

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**ステージ3 — データ。** OOKは共振器のリンギングに直面します（モデルQ≈40 → τ≈0.3 ms）：1 kbit/sはクリーン、5 kbit/sではアイが閉じます。より高速にするにはモードBが必要です：

<img src="docs/img/sim5-ook-datarate.png" width="720">

**受信側の電力予算。** 網掛け帯は**ターゲット**です（モードAは0.5–5 W、ステージ2が達成されれば；モードBはより低い）。現実的な初期負荷はデューティサイクル駆動のESP32 / BLE / LED；Wi-Fiは連続的な約束ではなくピーク消費マーカーとして表示されています：

<img src="docs/img/sim4-power-budget.png" width="720">

**後日用（モードB）。** 厚み共振のコムでプレートが透過になります — 周波数を追尾する必要があります：

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ 安全 — 初回通電前に必ず読む</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **圧電素子に数十〜数百ボルト** — ステージ2のドライバが稼働するとすぐに発生 — 受信側のTVSは最初の通電実行の前に挿入すること；リード線には手を触れないこと。
2. **商用電源** — 卓上電源 / 絶縁を通してのみ使用；超音波洗浄機のドライバボードは商用電源にガルバニック接続されています。
3. **耳** — 非自明な電力では、トランスデューサを金属に押し当てて運用すること；密閉筐体なしで高出力の空中超音波を稼働させないこと。
4. **熱** — クランプされていないLangevinトランスデューサは通電すると数分で過熱します；電流を上げる前にクランプすること（短時間の低電流電気的な立ち上げのみ — ドライバのREADMEを参照）。
5. **破片** — 圧電セラミックは脆い：ボルトの締めすぎや衝撃は破片につながります；機械的な作業には安全メガネを着用すること。

</details>

docs/            理論、先行技術、安全性、アプリケーション、決定ログ (ADR)
docs/img/        期待値プロット (software/simulator/channel_sim.py により生成)
hardware/        BOM、ドライバ (ハーフブリッジ)、レシーバ (整流器/ハーベスタ)
firmware/        ノードファームウェア (ESP32 — ステージ4までスタブ)
software/        測定スクリプト (周波数応答スイープマップ) およびチャネルシミュレータ
experiments/     実験プロトコル — テンプレートから作成、1ディレクトリ = 1実験
data/            生ログ (大きなファイルはgitから除外)
```

</details>

## 原則

1. **ゼロからの再現性。** はんだごてと約210ドルがあれば、誰でもこのリポジトリ単独で結果を再現できる。
2. **すべての実験はプロトコルである。** 「なんとなく動いた」はなし：[experiments/TEMPLATE.md](experiments/TEMPLATE.md) は必須である。
3. **特許の健全性。** 期限切れの層 ([docs/01-prior-art.md](docs/01-prior-art.md)) を基盤として構築し、決定事項は [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md) に記録する。
4. **測定が先、意見は後。** チャネルに関する結論を出す前にスイープマップを。

## ライセンスと特許

コード — Apache-2.0、ハードウェア — CERN-OHL-W v2、ドキュメント — CC-BY-4.0。全文は [LICENSES/](../../LICENSES) にあります。誰でもこれをフォークして構築できます（商用利用を含む）。特許保護は、ライセンス内の許諾条項および報復条項に加え、先行技術戦略によって提供されます。完全なスキームおよび防御的公開プロトコルについては [LICENSES.md](LICENSES.md) を、貢献ルールについては [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。
