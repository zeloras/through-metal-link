# 수신부

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · [日本語](../../../ja/hardware/receiver/README.md) · 한국어 · [हिन्दी](../../../hi/hardware/receiver/README.md)

회로도: [단계 1 — sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) · [단계 4 — sch4](../../../../hardware/schematics/sch4-receiver-node.png) ([../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py)로 생성)

- 단계 1 (측정): Langevin 트랜스듀서 RX (두 리드 모두 플로팅 — 접지 금지!) → 쇼트키 브리지 (4×SS14) → RC 필터 (10k || 100n) → 5 V TVS → **47 kΩ 직렬** → ADS1115 A0 (이 저항은 ADC 보호 다이오드로 흐르는 전류를 제한합니다: TVS는 입력의 절대 최대치보다 약 ~9 V 높게 클램핑합니다).
- 단계 2 (전력): RX → 동일한 브리지 → 알려진 저성 부하 (및/또는 LED), 브리지 이후의 DC V 및 I 측정; 전력은 해당 부하로 들어가는 V·I입니다. 프로토콜: [experiments/002](../../experiments/002-watts-3mm-steel/README.md).
- 단계 4 (노드): RX → GY-LTC3588 **PZ1/PZ2에 직접 연결** (브리지는 LTC3588-1에 내장되어 있어 외부 브리지 불필요) → 1 F 슈퍼커패시터 → ESP32 (딥 슬립 + 듀티 사이클). 부하 변조 — **DC 측**에서 2N7002 + 100 Ω (모듈의 VIN 핀, sch4 참조); AC 압전소자 양단에 단일 MOSFET을 병렬로 연결하는 것은 작동하지 않습니다 — 바디 다이오드가 한쪽 반파를 션트합니다 (docs/03).

중요: 첫 전원 인가 전에 반드시 TVS를 장착하세요 — 공진 상태의 개방형 압전소자는 수십~수백 볼트를 출력합니다. 브리지 이후의 DC 측 — 단방향 SMBJ5.0A; 노드의 압전소자(AC) 양단 — 양방향 SMBJ15CA만 사용.
