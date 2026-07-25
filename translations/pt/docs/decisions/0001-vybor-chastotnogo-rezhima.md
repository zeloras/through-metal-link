# ADR-0001: Seleção do Modo de Frequência para a Etapa 1

> [English (primary)](../../../../docs/decisions/0001-vybor-chastotnogo-rezhima.md) · [Русский](../../../ru/docs/decisions/0001-vybor-chastotnogo-rezhima.md) · [Deutsch](../../../de/docs/decisions/0001-vybor-chastotnogo-rezhima.md) · Português

- Status: ACEITO (a ser revisado após a Etapa 2)
- Date: 2026-07-24

## Contexto
Dois modos (veja docs/00-theory.md): A — 28–40 kHz em transdutores Langevin, B — 0,6–1 MHz em discos que acompanham a ressonância de espessura da parede.

## Decisão
As Etapas 1–2 executam o modo A. Razões: mais barato ($10–30 cada), mais poderoso (watts versus centenas de mW), mais permissivo para ajuste (ressonância ampla), e o driver pode ser construído a partir de uma ponte semicircular em torno de um IR2110. O modo B vem após obtermos os primeiros watts — como um ramo separado para dados de alta velocidade.

## Consequências
Os dados na Etapa 3 serão lentos (kbit/s) — suficientes para um nó de sensor. O ADC ADS1115 (860 SPS) é adequado para o envelope a 40 kHz após o retificador, mas não para amostragem direta — a amostragem direta é adiada para o modo B (necessita de um ADC diferente).
