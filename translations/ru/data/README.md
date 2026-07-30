# data/

> [English (primary)](../../../data/README.md) · Русский · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md)

Сырые логи измерений: CSV и PNG от `software/sweep-map/sweep_map.py`.

- Имена файлов — со штампом времени UTC: `sweep_25000-45000_20260801T120000Z.csv`.
- CSV/PNG в git не попадают (см. `.gitignore`) — крупные и воспроизводимые; в git идут только отобранные графики, скопированные в каталог соответствующего опыта `experiments/NNN-*/`.
- Запуски в режиме имитации (`sweep_map.py --mock`) также записываются сюда — эти файлы можно удалять в любое время.
