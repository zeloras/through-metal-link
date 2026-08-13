# ADR-0001: Выбор частотного режима для Этапа 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · Русский · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Статус: ПРИНЯТ (будет пересмотрен после Этапа 2)
- Дата: 2026-07-24

## Контекст
Два режима (см. docs/00-theory.md): A — 28–40 кГц на ланжевенах, B — 0.6–1 МГц на дисках, работающих на толщинном резонансе стенки.

## Решение
Этапы 1–2 идут в режиме A. Причины: дешевле ($10–30 за штуку), мощнее (ватты против сотен мВт), проще в настройке (широкий резонанс), а драйвер можно собрать на полумосте вокруг IR2110. Режим B подключим после того, как получим первые ватты насквозь — как отдельную ветку для высокоскоростных данных.

## Последствия
Данные на Этапе 3 будут медленными (кбит/с) — достаточно для сенсорного узла. АЦП ADS1115 (860 SPS) годится для огибающей на 40 кГц после выпрямителя, но не для прямой дискретизации — прямая дискретизация отложена до режима B (нужен другой АЦП).

Этап 1 (свип) использует только слабый DDS-драйвер; этап 2 (ватты) — отдельный эксперимент и отладка ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)). Полосы мощности из симулятора остаются целевыми, пока не будут измерены в 002.
