# ADR-0001: Вибір частотного режиму для Етапу 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · Українська · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Статус: ПРИЙНЯТО (буде переглянуто після Етапу 2)
- Дата: 2026-07-24

## Контекст
Два режими (див. docs/00-theory.md): A — 28–40 кГц на перетворювачах Ланжевена, B — 0.6–1 МГц на дисках, що працюють на резонансі товщини стінки.

## Рішення
Етапи 1–2 працюють у режимі A. Причини: дешевші ($10–30 за штуку), потужніші (вати проти сотень мВт), простіші в налаштуванні (широкий резонанс), а драйвер можна зібрати на півмосту навколо IR2110. Режим B з'явиться після того, як ми отримаємо перші вати наскрізь — як окрема гілка для високошвидкісної передачі даних.

## Наслідки
Дані на Етапі 3 будуть повільними (кбіт/с) — достатньо для вузла-датчика. АЦП ADS1115 (860 SPS) підходить для огибаючої на 40 кГц після випрямляча, але не для прямого дискретизування — пряме дискретизування відкладено до режиму B (потребує іншого АЦП).

Етап 1 (розвідка) використовує лише слабкий DDS-сигнал; етап 2 (вати) — окремий експеримент і налаштування ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). Енергетичні смуги симулятора залишаються цільовими, поки не буде виміряно 002.
