# Експеримент 001: Карта сканування каналу, 3 мм сталь (ЗАПЛАНОВАНО)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · Українська · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **Етап:** 1 (лише карта частот — тут немає цільової потужності; потужність у [002](../../../../experiments/002-watts-3mm-steel/README.md)).
- **Мета:** знайти резонанс пари перетворювачів Ланжевена через 3 мм пластину; отримати першу частотну характеристику каналу.
- **Гіпотеза:** пік приблизно 38–42 кГц (резонанс перетворювача Ланжевена), ширина піка кілька кГц за контакту через мастило+затискач.
- **Драйвер:** підключення етапу 1 — синусоїда AD9833 (~0.6 Vpp) на TX, **без** півмоста ([sch3](../../../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png)).
- **Процедура:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (використовуйте `--mock` для сухого прогону конвеєра без обладнання).
- **Критерій успіху:** відтворюваний пік (два сканування підряд, відхилення центру <200 Гц). Збережіть CSV/PNG у `data/` і додайте посилання на них з цього файлу, коли будуть реальні дані.
- **Бонусний вимір:** те саме сканування з «мастильний контакт + затискач» проти «сухий притиск» — лише відносні амплітуди; абсолютні вольти залежать від рівня драйвера і не порівнюються з масштабом-заглушкою симулятора, поки не відкалібровані.
- **Поза межами:** ≥0.5 Вт, світлодіод від збору, налаштування півмоста → експеримент 002.
