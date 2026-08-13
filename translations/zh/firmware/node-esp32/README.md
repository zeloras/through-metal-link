# ESP32 节点（第 4 阶段）— 桩

> [English (primary)](../../../../firmware/node-esp32/README.md) · [Русский](../../../ru/firmware/node-esp32/README.md) · [Deutsch](../../../de/firmware/node-esp32/README.md) · [Português](../../../pt/firmware/node-esp32/README.md) · [Español](../../../es/firmware/node-esp32/README.md) · [Français](../../../fr/firmware/node-esp32/README.md) · [Italiano](../../../it/firmware/node-esp32/README.md) · [Polski](../../../pl/firmware/node-esp32/README.md) · [Türkçe](../../../tr/firmware/node-esp32/README.md) · [Українська](../../../uk/firmware/node-esp32/README.md) · [Tiếng Việt](../../../vi/firmware/node-esp32/README.md) · 中文 · [日本語](../../../ja/firmware/node-esp32/README.md) · [한국어](../../../ko/firmware/node-esp32/README.md) · [हिन्दी](../../../hi/firmware/node-esp32/README.md)

计划：深度睡眠，定时器唤醒，采集传感器读数（气体/温度/背景），通过 BLE 广播包发送数据，然后重新进入睡眠。功耗预算：平均约 1–5 mW，峰值由超级电容缓冲。
在第 2 阶段之后进行。
