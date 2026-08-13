# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · Español · [Français](../../fr/data/README.md) · [Italiano](../../it/data/README.md) · [Polski](../../pl/data/README.md) · [Türkçe](../../tr/data/README.md) · [Українська](../../uk/data/README.md) · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md) · [한국어](../../ko/data/README.md) · [हिन्दी](../../hi/data/README.md)

Registros de medición en bruto: salida CSV y PNG de `software/sweep-map/sweep_map.py`.

- Los nombres de archivo incluyen una marca de tiempo UTC: `sweep_25000-45000_20260801T120000Z.csv`.
- Los archivos CSV/PNG no entran en git (ver `.gitignore`) — son grandes y reproducibles; solo las gráficas curadas entran en git, copiadas en el directorio del experimento correspondiente `experiments/NNN-*/`.

Las ejecuciones en modo mock (`sweep_map.py --mock`) también escriben aquí — esos archivos se pueden borrar en cualquier momento.
