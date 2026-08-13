# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [Español](../../es/data/README.md) · [Français](../../fr/data/README.md) · [Italiano](../../it/data/README.md) · [Polski](../../pl/data/README.md) · [Türkçe](../../tr/data/README.md) · Українська · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md) · [한국어](../../ko/data/README.md) · [हिन्दी](../../hi/data/README.md)

Сирі журнали вимірювань: CSV та PNG-вивід з `software/sweep-map/sweep_map.py`.

- Імена файлів містять часову мітку UTC: `sweep_25000-45000_20260801T120000Z.csv`.
- CSV/PNG-файли не потрапляють у git (див. `.gitignore`) — вони великі та відтворювані; до git потрапляють лише відібрані графіки, скопійовані до директорії відповідного експерименту `experiments/NNN-*/`.

Запуски в mock-режимі (`sweep_map.py --mock`) також пишуть сюди — ці файли можна безпечно видалити в будь-який час.
