# Experimento 002: Primeiros Watts Através de Aço de 3 mm (PLANEJADO)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · Português

- **Etapa:** 2 (potência em uma carga conhecida na ressonância encontrada em [001](../../../../experiments/001-sweep-map-3mm-steel/README.md)).
- **Objetivo:** medir a potência DC real entregue através de aço de 3 mm com o driver de ponte semicircular e transformador de acoplamento.
- **Hipótese:** com um par Langevin da mesma partida, contato de graxa+clamp (ou epóxi) e um transformador de acoplamento sintonizado, ≥0,5 W em uma carga resistiva no pico da etapa 1 é alcançável. (Figuras de multi-watt/kW da literatura usaram transdutores e ligação diferentes — trate-as como teto, não como barra de passagem.)
- **Pré-requisitos:**
  - Experimento 001 fechado (pico reprodutível, frequência registrada).
  - TVS instalado na cadeia RX antes de qualquer potência do driver ([docs/02-safety.md](../../docs/02-safety.md)).
  - Sequência de inicialização do driver seguida ([hardware/driver/README.md](../../../hardware/driver/README.md)).
- **Configuração (mínima):**
  - TX: Pi → AD9833 quadrado → formador de tempo morto → IR2110 ponte semicircular → transformador de acoplamento → Langevin preso à placa ([sch1](../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Parede: aço de 3 mm, método de contato registrado (graxa+clamp / epóxi / outro).
  - RX: Langevin → ponte Schottky → R_load conhecida (resistor de potência) e/ou LED; medir V_dc e I_dc após a ponte ([sch2](../../hardware/schematics/sch2-receiver-stage1.png) topologia, carga em vez de ADC-only).
- **Procedimento (esboço):**
  1. Inicialização elétrica com limite de 0,2 A do PSU sem reivindicar potência acústica.
  2. Prender TX/RX, definir frequência de drive para o pico do experimento 001.
  3. Aumentar o limite de corrente lentamente; registrar V/I do PSU, temperatura do MOSFET/transformador, V_dc e I_dc na carga.
  4. P_load = V_dc · I_dc. Opcional: foto de demonstração de LED curta uma vez que P_load é conhecida.
  5. Repetir uma vez após um resfriamento; a frequência do pico pode derivar com a temperatura — re-verificar com uma mini-varredura se a potência cair.
- **Critérios de sucesso:**
  1. P_load ≥ 0,5 W através de aço de 3 mm em uma frequência e método de contato documentados.
  2. Duas execuções concordam com P_load dentro de ~20% sob o mesmo clamp/couplant (estabilidade de ordem de magnitude, não de grau de metrologia).
  3. Foto de LED (ou outra carga) + CSV/log vinculado a este arquivo em `data/`.
- **Falha é dados:** se P_load permanecer ≪ 0,5 W, registrar par Δf (de 001), método de contato, voltas do transformador e formas de onda — isso é a entrada para o próximo ADR, não um motivo para editar silenciosamente o simulador.
