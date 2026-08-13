# Эксперимент 001: Свип-карта канала, сталь 3 мм (ЗАПЛАНИРОВАН)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · Русский · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **Этап:** 1 (только карта частот — нет целевого значения мощности здесь; мощность в [002](../002-watts-3mm-steel/README.md)).
- **Цель:** найти резонанс пары ланжевенов через пластину 3 мм; получить первую АЧХ канала.
- **Гипотеза:** пик в районе 38–42 кГц (резонанс ланжевенов), ширина пика единицы кГц под контактом смазка+струбцина.
- **Привод:** подключение этапа 1 — сигнал AD9833 (~0,6 Впп) на TX, **без** полумоста ([sch3](../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../hardware/schematics/sch2-receiver-stage1.png)).
- **Процедура:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (используйте `--mock`, чтобы протестировать pipeline без аппаратуры).
- **Критерий успеха:** воспроизводимый пик (два свипа подряд, отклонение центра <200 Гц). Сохранить CSV/PNG в `data/` и связать их с этим файлом, когда они будут реальными.
- **Бонус-замер:** тот же свип с контактом «смазка+струбцина» vs «сухой прижим» — относительные амплитуды только; абсолютные значения вольт зависят от уровня привода и не сравнимы с масштабом симулятора до калибровки.
- **Вне задачи:** ≥0,5 Вт, светодиод от сбора, подъем полумоста → эксперимент 002.
