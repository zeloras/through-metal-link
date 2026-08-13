# ADR-0001: Seleção de Modo de Frequência para o Estágio 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · Português · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Status: ACEITO (a ser revisitado após o Estágio 2)
- Date: 2026-07-24

## Contexto
Dois modos (ver docs/00-theory.md): A — 28–40 kHz em transdutores Langevin, B — 0.6–1 MHz em discos que operam na ressonância de espessura da parede.

## Decisão
Os Estágios 1–2 usam o modo A. Motivos: mais barato ($10–30 cada), mais potente (watts versus centenas de mW), mais tolerante no ajuste (ressonância ampla), e o driver pode ser construído com um meia-ponte em torno de um IR2110. O modo B vem depois de obtermos os primeiros watts através da parede — como um ramo separado para dados de alta velocidade.

## Consequências
Os dados no Estágio 3 serão lentos (kbit/s) — suficientes para um nó sensor. O ADC ADS1115 (860 SPS) serve para o envelope a 40 kHz após o retificador, mas não para amostragem direta — a amostragem direta fica adiada para o modo B (precisa de um ADC diferente).

O Estágio 1 (varredura) usa apenas o acionamento DDS de baixa potência; o estágio 2 (watts) é um experimento separado e bring-up ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)). As faixas de potência do simulador permanecem como metas até que 002 seja medido.
