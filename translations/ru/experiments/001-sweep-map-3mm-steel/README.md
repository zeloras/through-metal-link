# Эксперимент 001: Свип-карта канала, 3 мм сталь (ЗАПЛАНИРОВАН)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · Русский · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **Этап:** 1 (только карта частот — цель по мощности здесь не ставится; мощность — это [002](../002-watts-3mm-steel/README.md)).
- **Цель:** найти резонанс пары ланжевенов через пластину 3 мм; получить первую АЧХ канала.
- **Гипотеза:** пик в районе 38–42 кГц (резонанс ланжевена), ширина пика несколько кГц при контакте «смазка + струбцина».
- **Возбуждение:** коммутация этапа 1 — синус с AD9833 (~0.6 Vpp) на TX, **без** полумоста ([sch3](../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../hardware/schematics/sch2-receiver-stage1.png)).
- **Процедура:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (используйте `--mock` для холостого прогона пайплайна без железа).
- **Критерий успеха:** воспроизводимый пик (две свип-карты подряд, отклонение центра <200 Гц). Сохранить CSV/PNG в `data/` и сослаться на них из этого файла, когда они станут реальными.
- **Бонусное измерение:** тот же свип в режимах «смазка + струбцина» и «сухой прижим» — только относительные амплитуды; абсолютные вольты зависят от уровня возбуждения и не сопоставимы с placeholder-шкалой симулятора, пока не проведена калибровка.
- **Вне рамок:** ≥0.5 Вт, свечение LED от собранной мощности, запуск полумоста → эксперимент 002.
