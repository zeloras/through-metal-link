# 테스트 리그 도면

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · 한국어 · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| 파일 | 내용 | 단계 |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | 드라이버: IR2110 + 2×IRF540, 부트스트랩, 정합 트랜스포머 | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | 수신부: 4×SS14 브리지 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | 핀배치: Pi ↔ AD9833 ↔ 압전 소자 쌍 ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | 노드: RX → GY-LTC3588 → 슈퍼커패시터 → ESP32 (+ 부하 변조) | 4 |

이것들은 **브레드보드 프로토타입** 회로도입니다(부품 값은 출발점이며, 오실로스코프에서 조정해야 하는 곳은 `*`로 표시됩니다). 프로토타입이 실제로 검증되면 KiCad 프로젝트와 PCB 레이아웃이 제공될 예정입니다 — [driver/README.md](../driver/README.md)에서 약속한 대로입니다.
