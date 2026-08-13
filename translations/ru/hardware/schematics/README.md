# Схемы стенда

> [English (primary)](../../../../hardware/schematics/README.md) · Русский · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [Español](../../../es/hardware/schematics/README.md) · [Français](../../../fr/hardware/schematics/README.md) · [Italiano](../../../it/hardware/schematics/README.md) · [Polski](../../../pl/hardware/schematics/README.md) · [Türkçe](../../../tr/hardware/schematics/README.md) · [Українська](../../../uk/hardware/schematics/README.md) · [Tiếng Việt](../../../vi/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md) · [한국어](../../../ko/hardware/schematics/README.md) · [हिन्दी](../../../hi/hardware/schematics/README.md)

Схемы генерируются из кода — [render_schematics.py](../../../../hardware/schematics/render_schematics.py) одновременно служит источником дизайна (schemdraw); для внесения изменений редактируйте скрипт, затем перегенерируйте:

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Файл | Что | Стадия |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | драйвер: IR2110 + 2×IRF540, bootstrap, согласующий трансформатор | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | приёмник: 4×SS14 мост → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | пиновка: Pi ↔ AD9833 ↔ пьезо-пара ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | узел: RX → GY-LTC3588 → суперконденсатор → ESP32 (+ нагрузочная модуляция) | 4 |

Это схемы **макета на хлебной доске** (номиналы компонентов являются стартовыми, отмечены `*` там, где они подбираются по осциллографу). Проект KiCad с разводкой печатной платы будет добавлен после проверки макета — как обещано в [driver/README.md](../driver/README.md).
