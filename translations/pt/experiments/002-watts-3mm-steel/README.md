# Experimento 002: Primeiros Watts Através de 3 mm de Aço (PLANEJADO)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · Português · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Etapa:** 2 (potência numa carga conhecida na ressonância encontrada no [001](../001-sweep-map-3mm-steel/README.md)).
- **Objetivo:** medir a potência DC real entregue através de 3 mm de aço com o driver meia-ponte e o transformador de casamento.
- **Hipótese:** com um par de Langevin do mesmo lote, contato com graxa+morsa (ou epóxi) e um transformador de casamento sintonizado, ≥0,5 W numa carga resistiva no pico da etapa 1 é alcançável. (Figuras da literatura de múltiplos watts/kW usaram transdutores e colagem diferentes — trate-os como teto, não como critério de aprovação.)
- **Pré-requisitos:**
  - Experimento 001 encerrado (pico reprodutível, frequência registrada).
  - TVS instalado na cadeia de RX antes de qualquer alimentação do driver ([docs/02-safety.md](../../docs/02-safety.md)).
  - Sequência de inicialização do driver seguida ([hardware/driver/README.md](../../hardware/driver/README.md)).
- **Montagem (mínima):**
  - TX: Pi → AD9833 onda quadrada → shaper de dead-time → meia-ponte IR2110 → transformador de casamento → Langevin fixado à placa ([sch1](../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Parede: aço de 3 mm, método de contato registrado (graxa+morsa / epóxi / outro).
  - RX: Langevin → ponte Schottky → R_load conhecido (resistor de potência) e/ou LED; medir V_dc e I_dc após a ponte (topologia [sch2](../../hardware/schematics/sch2-receiver-stage1.png), carga em vez de apenas ADC).
- **Procedimento (esboço):**
  1. Inicialização elétrica com limite de 0,2 A na fonte sem reivindicar potência acústica.
  2. Fixar TX/RX, ajustar a frequência de acionamento para o pico do experimento 001.
  3. Aumentar o limite de corrente lentamente; registrar V/I da fonte, temperatura do MOSFET/transformador, V_dc e I_dc na carga.
  4. P_load = V_dc · I_dc. Opcional: foto curta de demonstração com LED uma vez que P_load seja conhecido.
  5. Repetir uma vez após esfriamento; a frequência de pico pode variar com a temperatura — verificar novamente com um mini-sweep se a potência cair.
- **Critérios de sucesso:**
  1. P_load ≥ 0,5 W através de 3 mm de aço numa frequência e método de contato documentados.
  2. Duas execuções concordam em P_load dentro de ~20% sob a mesma morsa/acoplante (estabilidade de ordem de grandeza, ainda não nível metrológico).
  3. Foto do LED (ou outra carga) + CSV/log vinculado a partir deste arquivo em `data/`.
- **Falha é dado:** se P_load permanecer ≪ 0,5 W, registrar Δf do par (do 001), método de contato, espiras do transformador e formas de onda — isso é a entrada para o próximo ADR, não um motivo para editar silenciosamente o simulador.
