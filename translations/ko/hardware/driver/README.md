# 드라이버 (스테이지 2): IR2110 하프브리지

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · 한국어 · [हिन्दी](../../../hi/hardware/driver/README.md)

**회로도:** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) ([../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py)로 생성)

신호 체인: Pi (SPI) → AD9833 **구형파 모드** (OPBITEN 비트: MSB가 출력으로 라우팅, 레일-투-레일 스윙 — 별도의 비교기 불필요) → **74HC14 + RC + 1N4148** 셰이퍼 (~1 µs 데드타임을 가진 상보 HIN/LIN) → IR2110 → 2×IRF540 (하프브리지) → 1 µF DC 차단 커패시터 → 정합 트랜스포머 (페라이트, ~1:3..1:5, 벤치에서 튜닝) → 란제빈 트랜스듀서 TX.

AD9833의 사인 출력(~0.6 Vpp)은 IR2110 로직에 부적합합니다 — 어떤 이유로 DDS에서 사인파가 꼭 필요하다면, 그 사이에 비교기(예: LM393, BOM에는 없음)를 넣으세요.

전력 스테이지 전원: 전류 제한 기능이 있는 12–24 V 벤치 PSU (**0.2 A에서 시작**).

참고: 스테이지-1 스윕은 약한 DDS 사인파로 압전소자를 직접 구동합니다(~0.6 Vpp, `sweep_map.py` 참조) — **이 드라이버는 스테이지 2(와트 단위)에서만 체인에 투입됩니다**. 스테이지-1 DDS 단독 연결에서 0.5 W 이상을 기대하지 마세요.

참고 사항:
- 란제빈 트랜스듀서는 정전성 부하(일반적으로 수 nF)입니다. 직렬 인덕터 또는 정합 트랜스포머가 필수입니다; 이것이 없으면 MOSFET이 무효 전류를 소모하며 과열됩니다.
- **정합 트랜스포머 (가장 흔한 고장 지점).** 작은 페라이트 토로이드(예: FT50-43 / 유사품)로 시작, 1차 측은 몇 회전, 2차 측은 그 약 3–5배, 1차 측에 직렬 DC 차단 1 µF 필름 커패시터. TX를 **플레이트에 고정(clamp)**하고 RX에 부하가 걸린 상태에서 *스테이지-1 공진 주파수*에서 PSU 전류가 최소가 되도록 튜닝하세요. 권선비와 누설은 경험적입니다 — 회로도에 `*` 표시가 있는 데는 이유가 있습니다. 최종 권선 수는 실험 로그에 기록하세요.
- **데드 타임**: IR2110은 자체적으로 데드 타임을 생성하지 않습니다. 디스크리트 부품 방식 — 74HC14 입력에 RC+1N4148 (상승 에지만 지연, ~1 µs; 40 kHz에서 25 µs 주기이므로 손실 <5%). 쉬운 방식 — EGS002 모듈, 모든 것이 내장되어 있습니다.
- **3.3 V 로직**: IR2110의 VDD를 AD9833 및 74HC14와 동일한 3.3 V에서 전원 공급 — VDD=5 V에서 VIH 임계값은 ≈ 3.1 V이며 3.3 V 구형파는 겨우 통과합니다 (데이터시트는 VDD를 3.3 V까지 허용).
- **디커플링은 필수**: VDD와 VCC에 100 nF (VCC — 47 µF 추가), 전원 레일에는 하프브리지 레그 바로 앞에 470–1000 µF + 100 nF 세라믹 — 이것이 없으면 브레드보드 점퍼 위의 하프브리지가 자신의 스위칭 스파이크를 잡아냅니다. 전원 루프 배선을 짧게 유지; 스위치 노드가 심하게 링잉되면 전류를 올리기 전에 브레드보드에서 벗어나 구리 도금 데드버그 / 프로토보드 그라운드 풀로 옮기세요.
- **최초 전원 인입 순서** ([docs/02-safety.md](../../docs/02-safety.md)와 정렬):
  1. 아직 2차 측에 란제빈 없음. PSU = 12 V, 전류 제한 0.2 A. 게이트 구동(HIN/LIN)과 스위치 노드를 오실로스코프로 확인 — 데드 타임과 관통 단락(shoot-through) 없음을 확인.
  2. 정합 트랜스포머 + TX 란제빈을 **강철 플레이트에 고정**(또는 두꺼운 희생 금속 블록). 여전히 0.2 A 제한. 스테이지-1 피크 주파수에서 전류와 RX 전압이 보일 때까지만 짧게 인입.
  3. MOSFET과 트랜스포머 온도를 지켜보며 전류 제한을 점진적으로 올리세요. 고정되지 않은 란제빈을 전원이 들어온 상태로 방치하지 마세요 — 자유 공간에서 풀 파워 구동은 세라믹이 깨지고 드라이버가 죽는 원인입니다.

TODO: 브레드보드(또는 데드버그) 프로토타입이 검증되면 KiCad 프로젝트(PCB) 작성. 그 전까지 [`../schematics/`](../../../../hardware/schematics)의 회로도가 설계의 진실 소스입니다.
