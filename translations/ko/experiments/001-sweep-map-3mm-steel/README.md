# 실험 001: 채널 스윕 맵, 3 mm 강판 (계획됨)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · 한국어 · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **단계:** 1 (주파수 맵만 — 여기서는 와트 목표 없음; 전력은 [002](../../../../experiments/002-watts-3mm-steel/README.md)).
- **목표:** 3 mm 강판을 통과하는 란주반(Langevin) 트랜스듀서 쌍의 공진을 찾고, 채널의 첫 번째 주파수 응답을 얻는다.
- **가설:** 38–42 kHz 부근에서 피크(란주반 트랜스듀서 공진), 그리스+클램프 접촉 조건에서 수 kHz 폭의 피크.
- **구동:** 단계-1 연결 — AD9833 사인파(~0.6 Vpp)를 TX에 인가, 하프브리지 **없음** ([sch3](../../../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png)).
- **절차:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (하드웨어 없이 파이프라인을 드라이런하려면 `--mock` 사용).
- **성공 기준:** 재현 가능한 피크(연속 두 번 스윕, 중심 편차 <200 Hz). 실제 데이터의 경우 CSV/PNG를 `data/` 아래에 저장하고 이 파일에서 링크한다.
- **보너스 측정:** "그리스 결합제 + 클램프" 대 "드라이 가압" 조건으로 동일한 스윕 수행 — 상대 진폭만 측정; 절대 전압은 구동 레벨에 따라 달라지며, 교정 전까지는 시뮬레이터의 플레이스홀더 스케일과 비교할 수 없다.
- **범위 외:** ≥0.5 W, 하베스트 기반 LED, 하프브리지 구동 → 실험 002.
