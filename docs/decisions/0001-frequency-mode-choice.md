# ADR-0001: Frequency Mode Selection for Stage 1

> English (primary) · [Русский](../../translations/ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../translations/de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../translations/pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../translations/es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../translations/fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../translations/it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../translations/pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../translations/tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../translations/uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../translations/vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../translations/zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../translations/ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../translations/ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../translations/hi/docs/decisions/0001-frequency-mode-choice.md)

- Status: ACCEPTED (to be revisited after Stage 2)
- Date: 2026-07-24

## Context
Two modes (see docs/00-theory.md): A — 28–40 kHz on Langevin transducers, B — 0.6–1 MHz on discs riding the wall's thickness resonance.

## Decision
Stages 1–2 run mode A. Reasons: cheaper ($10–30 apiece), more powerful (watts versus hundreds of mW), more forgiving to tune (broad resonance), and the driver can be built from a half-bridge around an IR2110. Mode B comes after we get the first watts through — as a separate branch for high-speed data.

## Consequences
Data at Stage 3 will be slow (kbit/s) — enough for a sensor node. The ADS1115 ADC (860 SPS) is fine for the envelope at 40 kHz after the rectifier, but not for direct sampling — direct sampling is deferred to mode B (needs a different ADC).

Stage 1 (sweep) uses the weak DDS drive only; stage 2 (watts) is a separate experiment and bring-up ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)). Simulator power bands remain targets until 002 is measured.
