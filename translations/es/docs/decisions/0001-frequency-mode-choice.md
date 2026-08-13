# ADR-0001: Selección de Modo de Frecuencia para la Etapa 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · Español · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Estado: ACEPTADO (se revisará después de la Etapa 2)
- Fecha: 2026-07-24

## Contexto
Dos modos (ver docs/00-theory.md): A — 28–40 kHz en transductores Langevin, B — 0.6–1 MHz en discos que aprovechan la resonancia de espesor de la pared.

## Decisión
Las etapas 1–2 funcionan en modo A. Razones: más baratos ($10–30 por unidad), más potentes (vatios frente a cientos de mW), más tolerantes al ajuste (resonancia amplia), y el driver puede construirse con un medio puente alrededor de un IR2110. El modo B llega después de que consigamos los primeros vatios a través — como una rama separada para datos de alta velocidad.

## Consecuencias
Los datos en la Etapa 3 serán lentos (kbit/s) — suficientes para un nodo sensor. El ADC ADS1115 (860 SPS) es adecuado para la envolvente a 40 kHz después del rectificador, pero no para muestreo directo — el muestreo directo se pospone al modo B (requiere un ADC distinto).

La Etapa 1 (barrido) usa únicamente la señal DDS débil; la etapa 2 (vatios) es un experimento y puesta a punto separado ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). Las bandas de potencia del simulador siguen siendo objetivos hasta que se midan los del 002.
