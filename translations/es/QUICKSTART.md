# QUICKSTART: de cero absoluto al banco de pruebas de etapa 1–2

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Português](../pt/QUICKSTART.md) · Español · [Français](../fr/QUICKSTART.md) · [Italiano](../it/QUICKSTART.md) · [Polski](../pl/QUICKSTART.md) · [Türkçe](../tr/QUICKSTART.md) · [Українська](../uk/QUICKSTART.md) · [Tiếng Việt](../vi/QUICKSTART.md) · [中文](../zh/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md)

Escenario: no tienes nada más que un escritorio y algo de dinero. Todo lo siguiente te lleva a un banco funcional — "mapa de barrido + primeros vatios a través del acero". Los precios son aproximados, en USD.

## Cesta 1 — herramientas (una base para años, ~$120)

| Artículo | Por qué | Precio | Dónde |
|---|---|---|---|
| Estación de soldadura (clon T12) | todo | 35–50 | Ali |
| Multímetro (clase AN8008/UT61) | voltajes, continuidad, capacitancia | 15–25 | Ali |
| Fuente de laboratorio 30V/5A con limitación de corriente | alimenta el driver; el límite de corriente es tu seguro contra MOSFETs quemados | 45–60 | Ali/local |
| Brazos de ayuda, soldadura, flux, malla desoldadora, alicates de corte, pinzas | lo pequeño que no puedes evitar | 15 | Ali/local |
| Cables Dupont + protoboard + termorretráctil | prototipado | 8 | Ali |

## Cesta 2 — electrónica del banco (~$70)

| Artículo | Cant. | Precio | Nota |
|---|---|---|---|
| Raspberry Pi (Zero 2 W basta; 4/5 más cómoda) + SD | 1 | 20–60 | el cerebro: barrido, registros, gráficos |
| Transductor Langevin 40 kHz 50–60 W | **4** | 40 | compra 4 de UN solo lote; elegiremos el mejor par por barrido |
| Módulo DDS AD9833 | 2 | 8 | el segundo es de repuesto |
| IR2110 + IRF540 ×4 (o un módulo EGS002) | 1 set | 10 | medio puente del driver |
| ADC ADS1115 | 2 | 4 | la Pi no tiene ADC propio |
| Toroide de ferrita + hilo de cobre esmaltado 0.5 mm | 2 | 4 | transformador de adaptación |
| Puente Schottky (SS14 ×8), supercondensador 1F 5.5V ×2 | 1 | 4 | cadena del receptor |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | protección. NO ESCATIMES |
| Módulo GY-LTC3588 | 1 | 7 | cosechador (etapa 4, pero que llegue ya) |
| Surtido de resistencias/condensadores, LEDs | 1 | 8 | si no tienes nada en absoluto |
| Pasivos de soporte: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | céntimos; lista completa — BOM ítems 11–12 |

## Cesta 3 — mecánica (~$20, en local)

Placa de acero 3 mm ~150×150 — 2 pzs (depósito de metal / corte láser); abrazaderas tipo F ×2; acoplante de grasa consistente y espesa (grasa de litio); epoxi; papel de lija (para limpiar la zona de contacto).

## Opcional, pero muy recomendable (~$90)

| Artículo | Por qué | Precio |
|---|---|---|
| Osciloscopio USB/portátil (FNIRSI/Hantek, 2 canales; no necesitas ≥40 MHz de ancho de banda — 10 sobra) | ver la forma de onda en la compuerta y en el piezo; ahorra días de depuración del driver | 60–80 |
| ESP32 DevKit ×2 | etapa 4 (el nodo detrás de la pared) | 8 |

**Total: mínimo absoluto ~$210, cómodo ~$300.** (Si ya tienes una Pi, una estación de soldadura y una fuente de laboratorio en tu arsenal — resta ~$120.)

## Orden de compra (el camino crítico es el envío)

1. Hoy: cesta 2 desde Ali (3–4 semanas de envío — es el camino crítico) + el osciloscopio.
2. Esta semana: cestas 1 y 3 en local.
3. Mientras llega: `raspi-config` → SPI+I2C, ejecuta `software/sweep-map/sweep_map.py --mock` sin hardware (canal sintético — todo el pipeline de CSV+gráficos funciona en cualquier ordenador), lee docs/00–03, mira los gráficos esperados en docs/img y los esquemáticos en hardware/schematics (el montaje de etapa 1 sigue sch3 y sch2).

## Lo que verás (simulador: software/simulator/channel_sim.py → docs/img)

Estos PNG son **expectativas del modelo**, no mediciones de laboratorio. Las relaciones de contacto, el Q cargado ≈40 y la eficiencia de cadena ≤40% son supuestos explícitos en `channel_sim.py` — sustitúyelos con datos de barrido/potencia una vez que el banco exista.

- `sim0-rig-sketch.png` — todo el banco en un solo esquema (cadena etapa 2; la etapa 1 omite el medio puente y conduce el TX desde la senoidal débil del DDS).
- `sim1-sweep-contacts.png` — forma de barrido esperada: un pico estrecho cerca de ~40 kHz; el modelo usa grasa:seco:aire ≈ 1 : 0.25 : 0.02 como marcadores de posición. Sin pico — depura primero el contacto o el desemparejamiento del par (sim2).
- `sim2-pair-mismatch.png` — por qué 4 transductores Langevin y no 2: con Q≈40, una desviación de resonancia de 1.5 kHz dentro de un par reduce la potencia del modelo ~10×; el barrido elige el mejor par de entre 4.
- `sim3-thickness-comb.png` — para más adelante (modo B, MHz): la placa es transparente como un peine de resonancias de espesor, así que la frecuencia hay que rastrearla.
- `sim4-power-budget.png` — consumo de la carga frente a bandas de **potencia recibida objetivo**. La banda del modo A (0.5–5 W) es la ambición de etapa 2 si la adaptación y el contacto cooperan; el modo B es la banda inferior. Wi-Fi continuo es un marcador de pico de carga, no una promesa — ESP32/BLE/LED con ciclo de trabajo son los primeros consumidores realistas.
- `sim5-ook-datarate.png` — etapa 3: por qué OOK en transductores Langevin llega como máximo a ~1–2 kbit/s con Q≈40 (tiempo de ring-down τ≈0.3 ms), y por qué eso está bien para un nodo sensor.

## Criterios para "el banco funciona"

Dividido por etapa — no marques la etapa 1 como completada con números de la etapa 2.

**Etapa 1 — mapa de barrido** ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)):
1. Barrer 25–45 kHz en dos corridas consecutivas: el centro del pico se reproduce dentro de <200 Hz.
2. Bonus opcional: grasa+abrazadera vs presión en seco sobre el mismo par (amplitudes relativas, no vatios absolutos).

**Etapa 2 — primeros vatios** ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)):
1. Medio puente + transformador de adaptación en línea; puesta en marcha con fuente limitada en corriente según [docs/02-safety.md](../../docs/02-safety.md) y [hardware/driver/](../../hardware/driver/README.md).
2. En la resonancia de la etapa 1, ≥0.5 W en una carga resistiva conocida a través de 3 mm de acero (medir V e I en el lado DC después del puente RX).
3. Un LED detrás de la placa se enciende con la potencia cosechada; foto + CSV en experiments/002.

Seguridad antes de la primera puesta en marcha: [docs/02-safety.md](../../docs/02-safety.md) (TVS en el receptor, límite de corriente de la fuente en 0.2 A para la puesta en marcha, sin funcionamientos de Langevin de alta potencia al aire libre).
