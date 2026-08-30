# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · 日本語 · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

金属壁を通じた超音波給電・データ通信のオープンプラットフォーム — 「鋼板に穴を開けずに貫通」、ガレージレベルの手段で構築。

**今すぐ試す（ハードウェア不要）：** `python3 software/sweep-map/sweep_map.py --mock`

**ステータス:** ステージ 0 — 準備中 · 💰 **[最初の独立ビルドに$250の報奨金](https://github.com/zeloras/through-metal-link/issues)** · 購入リスト: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

ドキュメントは多言語対応です：英語が主言語であり、正規パスに配置されています。その他の言語は [translations/](..) 配下のツリーとしてミラーされています。どの言語でも編集可能 — CIが翻訳して残りの言語をコミットします（[CONTRIBUTING.md](CONTRIBUTING.md) を参照）。

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Stage 1 rig: Pi → DDS → half-bridge → transformer → piezo TX | steel | piezo RX → bridge → ADC → Pi" width="900"></p>

## ひと段落でのアイデア

電波は金属を透過しません（ファラデーケージ）。また、ケーブルを貫通させることは、穴、シール、そして故障点を意味します。一方、超音波は金属を問題なく通過します。壁の両側に圧電素子を配置すれば、壁が電力とデータのチャネルになります。実験室の文献では、かなりのレベルでその物理がすでに証明されています（RPI: 63.5 mmの鋼板を通して50 W + 12 Mbit/s、NASA JPL: 5 mmのチタンを通して最大〜kW）— これらは特殊なハードウェアによる存在証明であり、このリポジトリのガレージBOMではありません。基礎特許はすでに期限切れとなっていますが、オープンで再現可能なプラットフォームはまだ存在しません — このリポジトリはそのようなプラットフォームを構築しており、ステージ2が測定され次第、**3〜5 mmの鋼板を通したワット級の電力と kbit/s のデータ**から始めます。

## ロードマップ

| ステージ | 成果物 | 成功基準 | 期待値 |
|---|---|---|---|
| 1. スイープマップ | 「ランジュバン–3 mm鋼板–ランジュバン」チャネルの周波数応答 | 共振ペアを発見、プロットは [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) に掲載 | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. ワット | 共振時の負荷への電力 | 3 mm鋼板を通じて ≥0.5 W、プロトコルは [experiments/002](experiments/002-watts-3mm-steel/README.md) に記載 | [sim4](docs/img/sim4-power-budget.png) |
| 3. データ | 同一ペアでの FSK/OOK | ≥1 kbit/s のエラーフリー通信 | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. ノード | 溶接密閉箱内の ESP32 + センサ、音波のみで給電・テレメトリ | ≥1 時間の自律動作 | [sim4](docs/img/sim4-power-budget.png) |
| 5. 公開 | リポジトリを公開、記事/ハウツー | 第三者による再現 | — |

## リポジトリマップ

python3 software/sweep-map/sweep_map.py --mock
```

**完了の定義（ステージごと）：** ステージ1 — 2回の実行でスイープのピークが200Hz以内で再現される（[実験/001](experiments/001-sweep-map-3mm-steel/README.md)）；ステージ2 — 3mmの鋼板を通して既知の負荷に0.5W以上が供給され、RX側からLEDが点灯する（[実験/002](experiments/002-watts-3mm-steel/README.md)）。

</details>

<details>
<summary><b>📚 1分でわかる理論</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

圧電素子のTXは壁に押し当てられ、縦波を壁の中に駆動します；反対側の圧電素子のRXはそれを再び電気に変換します。鋼中の音速：約5900 m/s。

2つの動作モード：

| モード | 周波数 | 共振の決定要因 | 出力 | ステータス |
|---|---|---|---|---|
| **A** — ランジュバン型振動子 | 40 kHz | 振動子ペア（壁 ≪ λ — 「膜」として動作） | ワット、kbit/s | 開始モード（ステージ1〜4、[ADR-0001](docs/decisions/0001-frequency-mode-choice.md)） |
| **B** — ディスク | 0.6–1 MHz | 壁の厚み共振（[櫛形](docs/img/sim3-thickness-comb.png)） | 数百mW、数百kbit/s | 最初のワット到達後の分岐；自動周波数追従が必要 |

主な損失：ペア内の共振ミスマッチ（安価なランジュバン型振動子で±1 kHz）、音響接触の品質（エポキシ > グリスカップラント + クランプ > ドライ圧着）、位置ずれ、温度による共振ドリフト。これらすべてに対する答えは同じです：**セットアップを変更するたびにスイープマップを作成する**。

</details>

<details>
<summary><b>📈 リグが示すべきこと：シミュレータからの期待値プロット</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

半経験的なチャネルモデル（FEMではなく、**実験室データでもない** — 「スイープがどのように見えるべきか、何を目指すべきか」の直感）。仮定は `channel_sim.py` に明記されています（ロードされたQ≈40、接触kファクター、チェーンη≤40%）。`python3 channel_sim.py --out ../../docs/img` で再生成します。

**ステージ1 — スイープ。** 約40kHz付近の狭いピーク；モデルのプレースホルダー接触乗数は グリス:ドライ:ギャップ = 1 : 0.25 : 0.02（つまり、グリスはドライの約4倍、エアギャップの約50倍）。ピークがない場合は、接触またはペアに問題があります：

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**なぜランジュバン型振動子が2つではなく4つなのか。** Q≈40では、ペア内の1.5kHzの共振ミスマッチによりモデル上の電力が約10分の1に低下します：

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**ステージ3 — データ。** OOKは共振器のリンギングに直面します（モデルQ~40 → τ≈0.3 ms）：1 kbit/sはクリーンですが、5 kbit/sではアイが閉じます。さらに高速にするにはモードBが必要です：

<img src="docs/img/sim5-ook-datarate.png" width="720">

**受信側の電力バジェット。** 影のついた帯は**ターゲット**です（モードAはステージ2が成功すれば0.5〜5W；モードBはそれ以下）。現実的な最初の負荷はデューティサイクル駆動のESP32 / BLE / LED；Wi-Fiは連続的な約束ではなく、ピーク消費のマーカーとして示されています：

<img src="docs/img/sim4-power-budget.png" width="720">

**後日のため（モードB）。** 鋼板は厚み共振の櫛形で透過になります — 周波数を追従する必要があります：

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ 安全 — 初回電源投入前に必ず読むこと</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. ステージ2のドライバがオンになると、**圧電素子に数十から数百ボルトの電圧がかかります** — 最初の通電実行の前に受信側のTVSを組み込んでください；リード線には手を触れないでください。
2. **商用電源** — 直流安定化電源 / 絶縁トランスを通してのみ接続してください；超音波洗浄機のドライバ基板は商用電源にガルバニック接続されています。
3. **耳** — かなりの電力で動作させる場合は、金属に押し当てた状態で振動子を動作させてください；筐体なしで高出力の空中超音波を動作させないでください。
4. **熱** — クランプされていないランジュバン型振動子は、電力をかけると数分で過熱します；電流を上げる前にクランプしてください（短時間の低電流での電気的なブリングアップのみ — ドライバのREADMEを参照）。
5. **破片** — 圧電セラミックは脆いです：ボルトの締めすぎや衝撃は破片を飛ばします；機械的な作業には安全メガネを着用してください。

</details>

docs/            理論、先行技術、安全性、アプリケーション、決定ログ (ADR)
docs/img/        期待値プロット (software/simulator/channel_sim.py で生成)
hardware/        BOM、ドライバ (ハーフブリッジ)、レシーバ (整流器/ハーベスタ)
firmware/        ノードファームウェア (ESP32 — ステージ4まではスタブ)
software/        測定スクリプト (周波数応答スイープマップ) およびチャネルシミュレータ
experiments/     実験プロトコル — テンプレートから作成、1ディレクトリ = 1実験
data/            生ログ (大きなファイルはgitに含めない)
```

</details>

## 原則

1. **ゼロからの再現性。** はんだごてと約$210があれば、このリポジトリだけで結果を再現できる。
2. **すべての実験はプロトコル。** 「なんとなく動いた」は不可: [experiments/TEMPLATE.md](experiments/TEMPLATE.md) は必須である。
3. **特許の健全性。** 期限切れの層 ([docs/01-prior-art.md](docs/01-prior-art.md)) の上に構築し、決定は [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md) に記録する。
4. **測定優先、意見はその次。** チャネルに関する結論を出す前に、スイープマップを作成する。

## ライセンスと特許

コード — Apache-2.0、ハードウェア — CERN-OHL-W v2、ドキュメント — CC-BY-4.0。全文は [LICENSES/](../../LICENSES) にあります。商用利用を含め、誰でもこれをフォークして開発を進めることができます。特許保護は、ライセンスの許諾条項および報復条項に加え、先行技術戦略によって提供されます。完全なスキームおよび防御的公開プロトコルについては [LICENSES.md](LICENSES.md) を、貢献ルールについては [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。
