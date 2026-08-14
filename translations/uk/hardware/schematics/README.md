# Схеми випробувального стенду

> [English (primary)](../../../../hardware/schematics/README.md) · [Русский](../../../ru/hardware/schematics/README.md) · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · Українська · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Файл | Що | Етап |
|---|---|---|
| [sch1-driver-halfbridge](../../../../hardware/schematics/sch1-driver-halfbridge.png) | драйвер: IR2110 + 2×IRF540, бутстреп, узгоджувальний трансформатор | 2 |
| [sch2-receiver-stage1](../../../../hardware/schematics/sch2-receiver-stage1.png) | приймач: міст 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](../../../../hardware/schematics/sch3-stage1-wiring.png) | розпіновка: Pi ↔ AD9833 ↔ пара п'єзо ↔ ADS1115 | 1 |
| [sch4-receiver-node](../../../../hardware/schematics/sch4-receiver-node.png) | вузол: RX → GY-LTC3588 → суперконденсатор → ESP32 (+ модуляція навантаження) | 4 |

Це схеми **для макетної плати** (значення компонентів є початковими, позначені `*` там, де їх підбирають за осцилографом). Проєкт KiCad із розводкою PCB з'явиться, як тільки прототип буде перевірено на живу — як обіцяно в [driver/README.md](../driver/README.md).
