# Experimento 002: Primeros vatios a través de 3 mm de acero (PLANIFICADO)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · Español · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Etapa:** 2 (potencia en una carga conocida en la resonancia encontrada en [001](../001-sweep-map-3mm-steel/README.md)).
- **Objetivo:** medir la potencia DC real entregada a través de 3 mm de acero con el driver de medio puente y el transformador de adaptación.
- **Hipótesis:** con un par de Langevin del mismo lote, contacto con grasa+abrazadera (o epoxi) y un transformador de adaptación sintonizado, ≥0,5 W en una carga resistiva en el pico de la etapa 1 es alcanzable. (Las cifras de multi-vatios/kW de la literatura usaron transductores y uniones diferentes — trátalas como techo, no como criterio de aprobación.)
- **Requisitos previos:**
  - Experimento 001 cerrado (pico reproducible, frecuencia registrada).
  - TVS instalado en la cadena RX antes de aplicar potencia al driver ([docs/02-safety.md](../../docs/02-safety.md)).
  - Secuencia de puesta en marcha del driver seguida ([hardware/driver/README.md](../../../../hardware/driver/README.md)).
- **Configuración (mínima):**
  - TX: Pi → AD9833 cuadrada → shaper de dead-time → IR2110 medio puente → transformador de adaptación → Langevin fijado a la placa ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Muro: 3 mm de acero, método de contacto registrado (grasa+abrazadera / epoxi / otro).
  - RX: Langevin → puente Schottky → R_load conocida (resistencia de potencia) y/o LED; medir V_dc e I_dc después del puente (topología [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png), carga en lugar de solo ADC).
- **Procedimiento (esquema):**
  1. Puesta en marcha eléctrica con límite de 0,2 A en la PSU sin reclamar potencia acústica.
  2. Fijar TX/RX, ajustar la frecuencia de conducción al pico del experimento 001.
  3. Subir el límite de corriente lentamente; registrar V/I de la PSU, temperatura de MOSFET/transformador, V_dc e I_dc en la carga.
  4. P_load = V_dc · I_dc. Opcional: foto corta de demostración con LED una vez conocido P_load.
  5. Repetir una vez tras un enfriamiento; la frecuencia de pico puede derivar con la temperatura — volver a comprobar con un mini-sweep si la potencia cae.
- **Criterios de éxito:**
  1. P_load ≥ 0,5 W a través de 3 mm de acero a una frecuencia y método de contacto documentados.
  2. Dos ejecuciones coinciden en P_load dentro de ~20% bajo la misma abrazadera/acoplante (estabilidad de orden de magnitud, todavía no de grado metrológico).
  3. Foto del LED (u otra carga) + CSV/log enlazado desde este archivo en `data/`.
- **El fracaso es dato:** si P_load se mantiene ≪ 0,5 W, registrar Δf del par (de 001), método de contacto, espiras del transformador y formas de onda — eso es la entrada para el siguiente ADR, no razón para editar silenciosamente el simulador.
