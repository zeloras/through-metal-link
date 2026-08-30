# enlace-a-través-del-metal

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · Español · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Una plataforma abierta para la transferencia ultrasónica de energía y datos a través de paredes de metal sólido — "a través del acero sin un solo agujero", construida con medios de nivel de garaje.

**Pruébalo ahora (sin hardware):** `python3 software/sweep-map/sweep_map.py --mock`

**Estado:** etapa 0 — preparación · 💰 **[recompensa de $250 para la primera construcción independiente](https://github.com/zeloras/through-metal-link/issues)** · lista de compras: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

La documentación es multilingüe: el inglés es el idioma principal y reside en las rutas canónicas; todos los demás idiomas reflejan el árbol bajo [translations/](..). Edita en cualquier idioma — la CI traduce y confirma el resto (ver [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Rig etapa 1: Pi → DDS → medio puente → transformador → piezo TX | acero | piezo RX → puente → ADC → Pi" width="900"></p>

## La idea en un párrafo

Las ondas de radio no atraviesan el metal (jaula de Faraday), y una penetración por cable significa un agujero, un sello y un punto de fallo. El ultrasonido, por su parte, viaja a través del metal sin problema: un elemento piezo a cada lado de la pared lo convierte en un canal para energía y datos. La literatura de laboratorio ya demostró la física en niveles serios (RPI: 50 W + 12 Mbit/s a través de 63,5 mm de acero; NASA JPL: hasta ~kW a través de 5 mm de titanio) — esas son pruebas de existencia con hardware especializado, no la lista de materiales de garaje de este repo. Las patentes fundamentales ya expiraron, y aún no existe una plataforma abierta y reproducible — este repositorio está construyendo una, empezando con **energía de orden de vatios y datos en kbit/s a través de 3–5 mm de acero** una vez que se mida la etapa 2.

## Hoja de ruta

| Etapa | Entregable | Criterio de éxito | Expectativa |
|---|---|---|---|
| 1. Mapa de barrido | respuesta en frecuencia del canal "Langevin–3 mm acero–Langevin" | par de resonancia encontrado, gráfico en [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. Vatios | potencia entregada a la carga en resonancia | ≥0,5 W a través de 3 mm de acero, protocolo en [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. Datos | FSK/OOK sobre el mismo par | ≥1 kbit/s sin errores | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. Nodo | ESP32 + sensor en una caja sellada por soldadura, alimentado y telemetrado únicamente por sonido | ≥1 h de operación autónoma | [sim4](docs/img/sim4-power-budget.png) |
| 5. Publicación | el repo se hace público, artículo/cómo | reproducción por un tercero | — |

## Mapa del repositorio

python3 software/sweep-map/sweep_map.py --mock
```

**Listo cuando (por etapa):** etapa 1 — el pico del barrido se reproduce entre dos ejecuciones con menos de 200 Hz de diferencia ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)); etapa 2 — ≥0.5 W en una carga conocida a través de 3 mm de acero y un LED encendido desde el lado RX ([experiments/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Teoría en un minuto</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

El piezo TX se prensa contra la pared e inyecta una onda longitudinal en ella; el piezo RX al otro lado la convierte de nuevo en electricidad. Velocidad del sonido en acero: ~5900 m/s.

Dos modos de operación:

| Modo | Frecuencia | Resonancia fijada por | Entrega | Estado |
|---|---|---|---|---|
| **A** — transductores Langevin | 40 kHz | el par de transductores (pared ≪ λ — una "membrana") | vatios, kbit/s | modo de inicio (etapas 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — discos | 0.6–1 MHz | resonancia de espesor de la pared ([comb](docs/img/sim3-thickness-comb.png)) | cientos de mW, cientos de kbit/s | rama tras los primeros vatios; necesita seguimiento automático de frecuencia |

Las pérdidas principales: desajuste de resonancia dentro del par (±1 kHz para transductores Langevin baratos), calidad del contacto acústico (epoxi > acoplante de grasa + abrazadera > presión en seco), desalineación, deriva de resonancia con la temperatura. La respuesta a todas es la misma: **un mapa de barrido antes de cada cambio en la configuración**.

</details>

<details>
<summary><b>📈 Lo que el rig debería mostrar: gráficas esperadas del simulador</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Un modelo de canal semiempírico (no FEM, **no datos de laboratorio** — intuición sobre "cómo debería verse el barrido y a qué apuntar"). Los supuestos están explícitos en `channel_sim.py` (Q cargado ≈40, factores de contacto, η de la cadena ≤40%). Regenera con: `python3 channel_sim.py --out ../../docs/img`.

**Etapa 1 — barrido.** Un pico estrecho cerca de ~40 kHz; los multiplicadores de contacto de marcador de posición del modelo son grasa:seco:aire = 1 : 0.25 : 0.02 (es decir, grasa ≈4× seco y ≈50× hueco de aire). Sin pico significa un problema con el contacto o el par:

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Por qué 4 transductores Langevin, no 2.** Con Q≈40, un desajuste de resonancia de 1.5 kHz dentro del par reduce la potencia del modelo ~10×:

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**Etapa 3 — datos.** OOK choca con el ringing del resonador (modelo Q~40 → τ≈0.3 ms): 1 kbit/s es limpio, a 5 kbit/s el ojo está cerrado. Ir más rápido requiere el modo B:

<img src="docs/img/sim5-ook-datarate.png" width="720">

**Presupuesto de potencia del receptor.** Las bandas sombreadas son **objetivos** (modo A 0.5–5 W si la etapa 2 cuaja; modo B menor). Las primeras cargas realistas son ESP32 / BLE / LED con duty-cycle; el Wi-Fi se muestra como marcador de pico de consumo, no como promesa continua:

<img src="docs/img/sim4-power-budget.png" width="720">

**Para más adelante (modo B).** La placa se vuelve transparente en un peine de resonancias de espesor — la frecuencia hay que rastrearla:

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Seguridad — leer antes del primer encendido</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Decenas a cientos de voltios en el piezo** una vez que el driver de la etapa 2 está activo — el TVS del lado de recepción va ANTES de la primera ejecución con potencia; mantén las manos lejos de los terminales.
2. **Red eléctrica** — solo a través de fuente de laboratorio / aislamiento; las placas driver de limpiadores ultrasónicos están galvánicamente conectadas a la red.
3. **Oídos** — a potencia no trivial, opera los transductores prensados contra metal; nunca ejecutes ultrasonido de alta potencia en aire sin una caja de protección.
4. **Calor** — un transductor Langevin sin abrazadera se sobrecalienta en minutos a potencia; abrazadera antes de subir la corriente (solo puesta a punto eléctrica breve de baja corriente — ver el README del driver).
5. **Esquirlas** — la piezocerámica es frágil: un tornillo demasiado apretado o un golpe significa esquirlas; usa gafas de seguridad para cualquier trabajo mecánico.

</details>

docs/            teoría, prior art, seguridad, aplicaciones, registro de decisiones (ADR)
docs/img/        gráficas esperadas (generadas por software/simulator/channel_sim.py)
hardware/        BOM, driver (half-bridge), receptor (rectificador/recolector)
firmware/        firmware del nodo (ESP32 — stub hasta la etapa 4)
software/        scripts de medición (mapa de barrido de respuesta en frecuencia) y simulador de canal
experiments/     protocolos de experimentos — desde la plantilla, un directorio = un experimento
data/            registros sin procesar (archivos grandes se mantienen fuera de git)
```

</details>

## Principios

1. **Reproducibilidad desde cero.** Cualquiera con un soldador y ~$210 puede reproducir el resultado usando únicamente este repositorio.
2. **Cada experimento es un protocolo.** Nada de "funcionó más o menos": [experiments/TEMPLATE.md](experiments/TEMPLATE.md) es obligatorio.
3. **Higiene de patentes.** Construimos sobre la capa expirada ([docs/01-prior-art.md](docs/01-prior-art.md)); las decisiones se registran en [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md).
4. **Primero la medición, luego la opinión.** Un mapa de barrido antes de cualquier conclusión sobre el canal.

## Licencias y patentes

Código — Apache-2.0, hardware — CERN-OHL-W v2, documentación — CC-BY-4.0; textos completos en [LICENSES/](../../LICENSES). Cualquiera puede hacer un fork y construir sobre esto, incluido el uso comercial; la protección de patentes proviene de las cláusulas de concesión y represalia de las licencias, además de una estrategia de técnica anterior. El esquema completo y el protocolo de publicación defensiva: [LICENSES.md](LICENSES.md); reglas de contribución: [CONTRIBUTING.md](CONTRIBUTING.md).
