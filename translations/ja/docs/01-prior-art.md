# 先行技術：私たちが基盤とするもの

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · 日本語 · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## ルール
このリポジトリのすべての技術的決定は、「フリー」リスト（期限切れ特許、論文）の情報源にまで遡ることができなければならない。存続中の特許は読み取り専用である — 問題への洞察を得るために活用し、決してそのクレームをコピーしないこと（これは米国での事業化において重要である；プロジェクト内の特許マップを参照のこと）。

## フリーの基盤（期限切れ・放棄特許 = パブリックドメイン）
- **US5982297**（Aerospace Corp, 1997） — 基本レシピ：壁を通す圧電素子ペア、電力＋双方向データ。メインの料理本。
- US5594705（Dynamotive, 1994） — 船体を通す「音響トランス」。
- US6037704, US6127942（Aerospace Corp） — センサーへの給電、データの読み出し。
- **US7902943**（Caltech/JPL, 2019年に維持費未納で失効） — Sherrit フィードスルー：リフレクター、音響トランス。
- US9748870（Caltech/JPL） — 壁を通した機械的仕事。
- **US9361877**（Univ. Oklahoma, 維持費未納で失効） — 現代的な完全トランシーバシステム。
- US20100027379 / WO2008105947（DOE+RPI, 放棄） — 外側からのキャリア＋内側からの負荷変調。

## 主要論文
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s、63.5 mm 鋼板。
- Sherrit et al., NASA NTRS 20080048150 — 壁を通して給電された 100 W ランプ。
- Yang et al., Sensors 2015 (10.3390/s151229870) — レビュー論文、数値の最良のまとめ。
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — メタマテリアル、1 mm ステンレスを通して 2%→66%（2026年7月時点で特許は見つかっていない）。

これらの論文は **物理学および特許衛生のベースライン** である。論文の電力・ビットレート数値は、実験室用トランスデューサ、接合、マッチングを使用したものであり、[QUICKSTART.md](../QUICKSTART.md) の AliExpress Langevin + グリース BOM とは異なる。存在証明として引用すること；プロジェクト自身の合格基準は [experiments/](../experiments/) にある。

## 存続中はコピーしないもの（米国のみ、〜2032年まで；ステージ1〜4ではそもそも不要）
電力チャネルの高調波を回避するためのサブキャリア配置を伴う OFDM（RPI US9054826）；単一方式としての全二重「AM ダウンリンク＋負荷変調アップリンク＋周波数追跡」（RPI US9455791）；Drexel アプローチに基づく曲面用コンフォーマル・トランスデューサ（US10594409）。
