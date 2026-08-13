# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [Español](../../es/data/README.md) · [Français](../../fr/data/README.md) · [Italiano](../../it/data/README.md) · [Polski](../../pl/data/README.md) · [Türkçe](../../tr/data/README.md) · [Українська](../../uk/data/README.md) · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · 日本語 · [한국어](../../ko/data/README.md) · [हिन्दी](../../hi/data/README.md)

生の測定ログ：`software/sweep-map/sweep_map.py` からの CSV と PNG 出力。

- ファイル名には UTC タイムスタンプが含まれる：`sweep_25000-45000_20260801T120000Z.csv`。
- CSV/PNG ファイルは git の管理対象外 (`.gitignore` 参照) — 大容量で再現可能であるため；カーソルされたプロットのみが git にコミットされ、対応する実験ディレクトリ `experiments/NNN-*/` にコピーされる。

モックモード実行 (`sweep_map.py --mock`) もここに書き込まれる — これらのファイルは、いつでも安全に削除できる。
