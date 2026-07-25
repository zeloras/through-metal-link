# ADR-0001: Frequency Mode Selection for Stage 1

> English (primary) · [Русский](../../translations/ru/docs/decisions/0001-vybor-chastotnogo-rezhima.md) · [Deutsch](../../translations/de/docs/decisions/0001-vybor-chastotnogo-rezhima.md) · [Português](../../translations/pt/docs/decisions/0001-vybor-chastotnogo-rezhima.md)

- Status: ACCEPTED (to be revisited after Stage 2)
- Date: 2026-07-24

## Context
Two modes (see docs/00-theory.md): A — 28–40 kHz on Langevin transducers, B — 0.6–1 MHz on discs riding the wall's thickness resonance.

## Decision
Stages 1–2 run mode A. Reasons: cheaper ($10–30 apiece), more powerful (watts versus hundreds of mW), more forgiving to tune (broad resonance), and the driver can be built from a half-bridge around an IR2110. Mode B comes after we get the first watts through — as a separate branch for high-speed data.

## Consequences
Data at Stage 3 will be slow (kbit/s) — enough for a sensor node. The ADS1115 ADC (860 SPS) is fine for the envelope at 40 kHz after the rectifier, but not for direct sampling — direct sampling is deferred to mode B (needs a different ADC).
