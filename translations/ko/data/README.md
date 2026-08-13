# data/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · [Português](../../pt/data/README.md) · [Español](../../es/data/README.md) · [Français](../../fr/data/README.md) · [Italiano](../../it/data/README.md) · [Polski](../../pl/data/README.md) · [Türkçe](../../tr/data/README.md) · [Українська](../../uk/data/README.md) · [Tiếng Việt](../../vi/data/README.md) · [中文](../../zh/data/README.md) · [日本語](../../ja/data/README.md) · 한국어 · [हिन्दी](../../hi/data/README.md)

원시 측정 로그: `software/sweep-map/sweep_map.py`의 CSV 및 PNG 출력.

- 파일명에 UTC 타임스탬프가 포함되어 있습니다: `sweep_25000-45000_20260801T120000Z.csv`.
- CSV/PNG 파일은 git에서 제외됩니다 (`.gitignore` 참조) — 용량이 크고 재생성 가능하기 때문입니다; 선별된 플롯만 git에 들어가며, 해당 실험 디렉토리 `experiments/NNN-*/`에 복사됩니다.

목업 모드 실행(`sweep_map.py --mock`)도 이곳에 파일을 작성합니다 — 언제든 삭제해도 안전합니다.
