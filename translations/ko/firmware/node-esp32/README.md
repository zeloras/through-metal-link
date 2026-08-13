# ESP32 노드 (4단계) — 스텁

> [English (primary)](../../../../firmware/node-esp32/README.md) · [Русский](../../../ru/firmware/node-esp32/README.md) · [Deutsch](../../../de/firmware/node-esp32/README.md) · [Português](../../../pt/firmware/node-esp32/README.md) · [Español](../../../es/firmware/node-esp32/README.md) · [Français](../../../fr/firmware/node-esp32/README.md) · [Italiano](../../../it/firmware/node-esp32/README.md) · [Polski](../../../pl/firmware/node-esp32/README.md) · [Türkçe](../../../tr/firmware/node-esp32/README.md) · [Українська](../../../uk/firmware/node-esp32/README.md) · [Tiếng Việt](../../../vi/firmware/node-esp32/README.md) · [中文](../../../zh/firmware/node-esp32/README.md) · [日本語](../../../ja/firmware/node-esp32/README.md) · 한국어 · [हिन्दी](../../../hi/firmware/node-esp32/README.md)

계획: 딥 슬립, 타이머로 웨이크, 센서 측정 수행 (가스/온도/백그라운드), 데이터를 담은 BLE 광고 패킷 전송, 다시 슬립. 전력 예산: 평균 ~1–5 mW, 피크는 슈퍼커패시터가 버퍼링.
2단계 이후에 진행.
