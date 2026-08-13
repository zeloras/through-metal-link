# 실험 002: 3 mm 강판을 통한 첫 와트 (계획됨)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · 한국어 · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **단계:** 2 ([001](../001-sweep-map-3mm-steel/README.md)에서 찾은 공진점에서 알려진 부하로 전력 전달).
- **목표:** 하프 브리지 드라이버와 정합 트랜스포머를 사용하여 3 mm 강판을 통해 전달되는 실제 DC 전력 측정.
- **가설:** 동일 배치 Langevin 쌍, 그리스+클램프(또는 에폭시) 접촉, 튜닝된 정합 트랜스포머를 사용하면 1단계 피크에서 저항성 부하에 ≥0.5 W 달성이 가능하다. (문헌의 다중 와트/kW 수치는 서로 다른 트랜스듀서와 본딩을 사용한 것으로 — 이를 상한선으로 간주하고, 합격 기준으로 삼지 말 것.)
- **사전 요구사항:**
  - 실험 001 완료 (재현 가능한 피크, 주파수 기록됨).
  - 드라이버 전원 인가 전 RX 체인에 TVS 부착 ([docs/02-safety.md](../../docs/02-safety.md)).
  - 드라이버 인가 시퀀스 준수 ([hardware/driver/README.md](../../../../hardware/driver/README.md)).
- **설정 (최소):**
  - TX: Pi → AD9833 방형파 → 데드타임 셰이퍼 → IR2110 하프 브리지 → 정합 트랜스포머 → 강판에 클램프된 Langevin ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png)).
  - 벽: 3 mm 강판, 접촉 방법 기록 (그리스+클램프 / 에폭시 / 기타).
  - RX: Langevin → 쇼트키 브리지 → 알려진 R_load (파워 저항) 및/또는 LED; 브리지 이후 V_dc 및 I_dc 측정 ([sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) 토폴로지, ADC 전용 대신 부하 사용).
- **절차 (개요):**
  1. 음향 전력을 주장하지 않고 0.2 A PSU 제한에서 전력적 인가.
  2. TX/RX 클램프, 구동 주파수를 실험 001 피크로 설정.
  3. 전류 제한 서서히 상승; PSU V/I, MOSFET/트랜스포머 온도, 부하의 V_dc 및 I_dc 기록.
  4. P_load = V_dc · I_dc. 선택: P_load 확인 후 짧은 LED 데모 사진 촬영.
  5. 냉각 후 한 번 반복; 피크 주파수는 온도에 따라 드리프트할 수 있음 — 전력이 떨어지면 미니 스윕으로 재확인.
- **성공 기준:**
  1. 문서화된 주파수와 접촉 방법에서 3 mm 강판을 통해 P_load ≥ 0.5 W.
  2. 동일한 클램프/커플런트 조건에서 두 번의 실행이 P_load 기준 ~20% 이내로 일치 (자릿수 단위 안정성, 아직 계측 등급은 아님).
  3. LED(또는 기타 부하) 사진 + CSV/로그를 이 파일에서 `data/` 아래에 링크.
- **실패도 데이터:** P_load가 ≪ 0.5 W로 유지되면, 페어 Δf(001에서), 접촉 방법, 트랜스포머 권수, 파형을 기록 — 이는 시뮬레이터를 은밀히 수정할 이유가 아니라 다음 ADR의 입력이다.
