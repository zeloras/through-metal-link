# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [Español](../../es/data/README.md) · [Français](../../fr/data/README.md) · Italiano · [Polski](../../pl/data/README.md) · [Türkçe](../../tr/data/README.md) · [Українська](../../uk/data/README.md) · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md) · [한국어](../../ko/data/README.md) · [हिन्दी](../../hi/data/README.md)

Log di misurazione grezzi: output CSV e PNG da `software/sweep-map/sweep_map.py`.

- I nomi dei file riportano un timestamp UTC: `sweep_25000-45000_20260801T120000Z.csv`.
- I file CSV/PNG restano fuori da git (vedi `.gitignore`) — sono grandi e riproducibili; solo i grafici curati entrano in git, copiati nella directory del corrispondente esperimento `experiments/NNN-*/`.

Le esecuzioni in modalità mock (`sweep_map.py --mock`) scrivono qui — quei file si possono eliminare in qualsiasi momento senza problemi.
