# Приёмник

> [English (primary)](../../../../hardware/receiver/README.md) · Русский · [Deutsch](../../../de/hardware/receiver/README.md) · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

Схемы: [этап 1 — sch2](../schematics/sch2-receiver-stage1.png) · [этап 4 — sch4](../schematics/sch4-receiver-node.png) (генерируются [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

- Этап 1 (измерения): ланжевен-RX (оба вывода плавающие — не землить!) → мост Гретца/Шоттки (4×SS14) → RC-фильтр (10к || 100н) → TVS 5В → **47 кОм последовательно** → ADS1115 A0 (резистор ограничивает ток в защитные диоды АЦП: кламп TVS ~9 В выше abs.max входа).
- Этап 2 (ватты): RX → тот же мост → известная резистивная нагрузка (и/или светодиод), замер постоянного V и I после моста; мощность — V·I в эту нагрузку. Протокол: [experiments/002](../../experiments/002-watts-3mm-steel/README.md).
- Этап 4 (узел): RX → GY-LTC3588 **напрямую в PZ1/PZ2** (мост встроен в LTC3588-1, внешний не нужен) → ионистор 1Ф → ESP32 (глубокий сон + цикл работы). Нагрузочная модуляция — 2N7002 + 100 Ом на **DC-стороне** (вывод VIN модуля, см. sch4); одиночный MOSFET поперёк AC-пьезо не работает — body-диод шунтирует полуволну (docs/03).

ВАЖНО: TVS до первого включения — открытый пьезо на резонансе выдаёт десятки-сотни вольт. На DC после моста — однонаправленный SMBJ5.0A; поперёк пьезо узла (AC) — только двунаправленный SMBJ15CA.
