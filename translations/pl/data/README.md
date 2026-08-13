# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [Español](../../es/data/README.md) · [Français](../../fr/data/README.md) · [Italiano](../../it/data/README.md) · Polski · [Türkçe](../../tr/data/README.md) · [Українська](../../uk/data/README.md) · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md) · [한국어](../../ko/data/README.md) · [हिन्दी](../../hi/data/README.md)

Surowe logi pomiarowe: pliki CSV i PNG generowane przez `software/sweep-map/sweep_map.py`.

- Nazwy plików zawierają znacznik czasu UTC: `sweep_25000-45000_20260801T120000Z.csv`.
- Pliki CSV/PNG nie trafiają do gita (patrz `.gitignore`) — są duże i odtwarzalne; do gita trafiają tylko wyselekcjonowane wykresy, kopiowane do katalogu odpowiedniego eksperymentu `experiments/NNN-*/`.

Przebiegi w trybie mock (`sweep_map.py --mock`) również zapisują tutaj — te pliki można w każdej chwili bezpiecznie usunąć.
