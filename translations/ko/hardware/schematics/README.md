# 테스트 리그 회로도

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · 한국어 · [हिन्दी](../../../hi/hardware/schematics/README.md)

회로도는 코드로부터 생성됩니다 — [render_schematics.py](../../../../hardware/schematics/render_schematics.py)가 설계 소스(schemdraw)를 겸합니다. 변경하려면 스크립트를 수정한 뒤 다시 생성하세요:

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| 파일 | 내용 | 단계 |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | 드라이버: IR2110 + 2×IRF540, 부트스트랩, 정합 트랜스포머 | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | 수신부: 4×SS14 브리지 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | 핀아웃: Pi ↔ AD9833 ↔ 압전 페어 ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | 노드: RX → GY-LTC3588 → 슈퍼커패시터 → ESP32 (+ 부하 변조) | 4 |

이 회로도들은 **브레드보드 프로토타입** 회로도입니다(부품 값은 출발점이며, 오실로스코프에서 조정해야 하는 값은 `*`로 표시). PCB 레이아웃이 포함된 KiCad 프로젝트는 프로토타입이 실물로 검증된 뒤 제공될 예정입니다 — [driver/README.md](../driver/README.md)에서 약속한 대로입니다.
