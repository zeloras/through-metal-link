# ADR-0001: 1단계 주파수 모드 선택

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · 한국어 · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- 상태: 승인됨 (2단계 이후 재검토 예정)
- 날짜: 2026-07-24

## 배경
두 가지 모드가 있다 (docs/00-theory.md 참조): A — Langevin 트랜스듀서에서 28–40 kHz, B — 벽의 두께 공진을 타는 디스크에서 0.6–1 MHz.

## 결정
1–2단계는 모드 A로 진행한다. 이유: 더 저렴하고 ($10–30 개당), 더 강력하고 (수백 mW 대비 와트 단위), 튜닝이 더 관대하며 (넓은 공진 대역), IR2110 기반 하프브리지로 드라이버를 구성할 수 있다. 모드 B는 첫 와트를 통과시킨 이후에 고속 데이터용 별도 브랜치로 도입한다.

## 결과
3단계의 데이터 속도는 느릴 것이다 (kbit/s) — 센서 노드에는 충분하다. ADS1115 ADC (860 SPS)는 정류기 이후 40 kHz의 엔벨로프에는 적합하지만, 직접 샘플링에는 부적합하다 — 직접 샘플링은 모드 B로 연기된다 (별도의 ADC 필요).

1단계 (스윕)는 약한 DDS 드라이브만 사용한다; 2단계 (와트)는 별도의 실험 및 브링업이다 ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). 시뮬레이터 전력 대역은 002가 측정될 때까지 목표치로 남는다.
