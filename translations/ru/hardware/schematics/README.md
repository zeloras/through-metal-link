# Схемы стенда

> [English (primary)](../../../../hardware/schematics/README.md) · Русский · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Файл | Что | Этап |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | драйвер: IR2110 + 2×IRF540, бутстреп, согласующий трансформатор | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | приёмник: мост Шоттки 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | распиновка: Pi ↔ AD9833 ↔ пара пьезо ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | узел: RX → GY-LTC3588 → ионистор → ESP32 (+ нагрузочная модуляция) | 4 |

Это схемы **макета** (номиналы компонентов — отправные точки, помечены `*` там, где они подгоняются по осциллографу). Проект KiCad с разводкой платы появится, как только прототип будет проверен в железе — как обещано в [driver/README.md](../driver/README.md).
