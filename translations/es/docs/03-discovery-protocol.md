# Protocolo de descubrimiento y auto-sintonía del receptor (borrador; implementación en las etapas 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · Español · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

El objetivo: el dispositivo descubre por sí mismo si hay un receptor detrás de la pared, elige por su cuenta la frecuencia y la potencia, y no tuesta la pared en vano si alguien "se olvidó de soldar el receptor".

El modelo a seguir son los cargadores Qi: resuelven exactamente este problema (¿hay un teléfono sobre la bobina?) con exactamente esta secuencia. Nuestro análogo acústico:

## Fase 0 — ping analógico (el receptor puede estar totalmente descargado)
El TX realiza un barrido de baja potencia a lo largo de la banda y mide **su propia corriente y fase** (shunt + detector de pico → ADS1115). Un receptor resonante detrás de la pared es una carga acoplada al TX a través de la pared: su presencia se manifiesta como una depresión/elevación característica en la curva de impedancia del TX, incluso si todo lo de dentro está sin alimentación. El mismo principio que un detector de metales y el ping analógico de Qi.
- Firma presente → fase 1. Sin firma → "no se encontró receptor", permanecer en ping de espera (una vez cada N segundos), sin subir la potencia.
- Bonus: la curva de impedancia de la pared "vacía" se registra al momento de la instalación como referencia — así podemos distinguir "no hay receptor" de "el receptor se soltó / se desalineó".

## Fase 1 — handshake digital
El TX se estaciona en la frecuencia candidata (el pico de la fase 0) y entrega potencia. El cosechador del RX carga el supercapacitor, el MCU despierta y responde con **modulación de carga**: un MOSFET cortocircuita periódicamente su piezo siguiendo un código (ID + versión del protocolo). El TX lo ve como modulación de su propia corriente. No se necesita ningún transmisor dentro — este es un esquema RFID, el mismo de la abandonada solicitud DOE/RPI US20100027379 (prior art gratuito).

## Fase 2 — sintonía servo de frecuencia (perturbar y observar)
El RX puede reportar su voltaje de bus (telemetría por modulación de carga). El TX avanza ±Δf y mantiene el máximo de potencia recibida — un lazo MPPT clásico. Esto compensa la deriva de resonancia con la temperatura (el principal problema del nicho: un desplazamiento de ~6% = caída de eficiencia de ~10×).

## Fase 3 — negociación de potencia y watchdog
El RX solicita un nivel (vivo / cargando / dame más), el TX limita la potencia a lo solicitado. Si faltan respuestas durante M ciclos → el TX retrocede a la fase 0 a baja potencia.

## Hardware que esto requiere (ítem 12 del BOM, esquemático — hardware/schematics/sch4)
- TX: shunt de 0.1 Ω + rectificador/detector de pico en el segundo canal del ADS1115 (corriente), opcionalmente un comparador de fase.
- RX: 2N7002 + ~100 Ω en el **lado DC** del rectificador (el pin VIN del módulo LTC3588) + GPIO — la carga se conmuta después del puente, y el TX lo ve como modulación de su propia corriente. Un solo MOSFET a través del piezo AC no funciona (el diodo de cuerpo deriva media onda, la compuerta no tiene referencia en un nodo flotante); la variante a través del piezo solo funciona con un par de MOSFETs en serie espalda con espalda.

## Límites
El ping analógico se debilita a medida que crecen el grosor de la pared y las pérdidas de contacto (la firma se ahoga en el ruido) — el umbral de detección debe medirse en un experimento dedicado (experiments/). Para paredes gruesas, la alternativa: el RX, una vez que ha acumulado carga, "golpea" periódicamente con una baliza propia.
