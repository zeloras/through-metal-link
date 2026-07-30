# Принципиальные схемы стенда

> [English (primary)](../../../../hardware/schematics/README.md) · Русский · [Deutsch](../../../de/hardware/schematics/README.md) · [Português](../../../pt/hardware/schematics/README.md) · [中文](../../../zh/hardware/schematics/README.md) · [日本語](../../../ja/hardware/schematics/README.md)

Схемы генерируются кодом — [render_schematics.py](../../../../hardware/schematics/render_schematics.py) и есть исходник дизайна (schemdraw); правки — в скрипт, потом перегенерация:

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Файл | Что | Этап |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.png) | драйвер: IR2110 + 2×IRF540, бутстреп, согласующий транс | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.png) | приёмник: мост 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.png) | пиновка: Pi ↔ AD9833 ↔ пьезо-пара ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.png) | узел: RX → GY-LTC3588 → ионистор → ESP32 (+ нагрузочная модуляция) | 4 |

Это схемы **макета** (номиналы — стартовые, помечены `*` там, где подбираются по осциллографу). KiCad-проект с разводкой платы появится после проверки макета живьём — как и обещано в [driver/README.md](../driver/README.md).
