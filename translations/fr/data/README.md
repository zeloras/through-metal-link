# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [Español](../../es/data/README.md) · Français · [Italiano](../../it/data/README.md) · [Polski](../../pl/data/README.md) · [Türkçe](../../tr/data/README.md) · [Українська](../../uk/data/README.md) · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md) · [한국어](../../ko/data/README.md) · [हिन्दी](../../hi/data/README.md)

Journaux de mesures bruts : sortie CSV et PNG depuis `software/sweep-map/sweep_map.py`.

- Les noms de fichiers comportent un horodatage UTC : `sweep_25000-45000_20260801T120000Z.csv`.
- Les fichiers CSV/PNG restent hors de git (voir `.gitignore`) — ils sont volumineux et reproductibles ; seules les figures sélectionnées entrent dans git, copiées dans le répertoire de l'expérience correspondante `experiments/NNN-*/`.

Les exécutions en mode simulé (`sweep_map.py --mock`) écrivent également ici — ces fichiers peuvent être supprimés à tout moment.
