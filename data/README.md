# data/

> English (primary) · [Русский](../translations/ru/data/README.md) · [Deutsch](../translations/de/data/README.md) · [Português](../translations/pt/data/README.md) · [中文](../translations/zh/data/README.md) · [日本語](../translations/ja/data/README.md)

Raw measurement logs: CSV and PNG output from `software/sweep-map/sweep_map.py`.

- File names carry a UTC timestamp: `sweep_25000-45000_20260801T120000Z.csv`.
- CSV/PNG files stay out of git (see `.gitignore`) — they are large and reproducible; only the curated plots go into git, copied into the corresponding experiment's directory `experiments/NNN-*/`.

Mock-mode runs (`sweep_map.py --mock`) write here too — those files are safe to delete at any time.
