# 数据/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · 中文 · [日本語](../../ja/data/README.md)

原始测量日志：CSV 和 PNG 输出来自 `software/sweep-map/sweep_map.py`。

- 文件名携带 UTC 时间戳：`sweep_25000-45000_20260801T120000Z.csv`。
- CSV/PNG 文件不在 git 中（见 `.gitignore`）——它们体积大且可重现；只有经过整理的图表进入 git，并复制到相应实验的目录 `experiments/NNN-*/` 中。

模拟模式运行（`sweep_map.py --mock`）也写入此目录 —— 这些文件可以在任何时候安全删除。
