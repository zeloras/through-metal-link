# Принципиальные схемы стенда

> [English (primary)](README.md)

Схемы генерируются кодом — [render_schematics.py](render_schematics.py) и есть исходник дизайна (schemdraw); правки — в скрипт, потом перегенерация:

```bash
uv run --with schemdraw --with matplotlib python render_schematics.py
```

| Файл | Что | Этап |
|---|---|---|
| [sch1-driver-halfbridge](sch1-driver-halfbridge.ru.png) | драйвер: IR2110 + 2×IRF540, бутстреп, согласующий транс | 2 |
| [sch2-receiver-stage1](sch2-receiver-stage1.ru.png) | приёмник: мост 4×SS14 → RC → TVS → ADS1115 A0 | 1 |
| [sch3-stage1-wiring](sch3-stage1-wiring.ru.png) | пиновка: Pi ↔ AD9833 ↔ пьезо-пара ↔ ADS1115 | 1 |
| [sch4-receiver-node](sch4-receiver-node.ru.png) | узел: RX → GY-LTC3588 → ионистор → ESP32 (+ нагрузочная модуляция) | 4 |

Это схемы **макета** (номиналы — стартовые, помечены `*` там, где подбираются по осциллографу). KiCad-проект с разводкой платы появится после проверки макета живьём — как и обещано в [driver/README.md](../driver/README.ru.md).
