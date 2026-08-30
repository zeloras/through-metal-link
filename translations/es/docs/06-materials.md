# Materiales de pared más allá del acero: qué paredes transportan energía y datos

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · [Deutsch](../../de/docs/06-materials.md) · [Português](../../pt/docs/06-materials.md) · Español · [Français](../../fr/docs/06-materials.md) · [Italiano](../../it/docs/06-materials.md) · [Polski](../../pl/docs/06-materials.md) · [Türkçe](../../tr/docs/06-materials.md) · [Українська](../../uk/docs/06-materials.md) · [Tiếng Việt](../../vi/docs/06-materials.md) · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

El resto de este repositorio asume acero. Esta página plantea la pregunta más simple y más grande: **¿para qué materiales de pared funciona en absoluto el canal de dos transductores**, y en qué modo? Es un estudio por simulación (estilo `--mock`, sin datos de laboratorio — intuición sobre qué merece un experimento de hardware), construido a partir del mismo modelo semiempírico que [channel_sim](../../../software/simulator/channel_sim.py) y extendido con absorción volumétrica.

Generar con: `python3 software/simulator/material_map.py` (requiere numpy + matplotlib). Modelo y supuestos: [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## El modelo en un minuto

Tres magnitudes deciden si una pared es utilizable en absoluto, y para cuánta potencia:

1. **Contraste de impedancia y fase** — el modelo de placa Fabry–Perot sin pérdidas, idéntico a [channel_sim](../../../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_pared / Z_acoplante, acoplante Z = 1.5 MRayl (grasa).
   En una resonancia de media onda (f = c/2d) una placa simétrica sin pérdidas es totalmente transparente *independientemente de r*; el contraste r determina la **anchura** de los dientes del peine (tolerancia al error de frecuencia), la velocidad del sonido c determina la separación entre ellos (Δf = c/2d).
2. **Absorción volumétrica**, invisible al modelo sin pérdidas y decisiva para plásticos, hormigón y caucho:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, unidireccional, longitudinal],
   donde α₁ₘₕᶻ es el valor a 1 MHz.
   γ ≈ 1 = pérdida viscosa/relajación; γ > 2 = dispersión por inhomogeneidades (árido de hormigón).
3. **La dosis que la pared devuelve** — véase la sección [más abajo](#la-dosis-qué-le-hace-la-onda-a-la-pared-frecuencia-por-frecuencia): tensión σ = √(2·I·Z), que *no* depende de la frecuencia, y autocalentamiento ΔT ∝ α(f)·I, que sí depende.

**Supuestos, indicados donde el código los indica:** propiedades típicas de manual (onda longitudinal, ~20 °C); los lotes reales varían — grano, cargas, áridos, curado. Todo lo que sigue es un ranking, no una hoja de datos.

| Pared | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | peine Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | nota |
|---|---|---|---|---|---|---|---|---|
| acero | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | estructural de grano fino |
| aluminio | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | clase 6061 |
| titanio | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| cobre | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | denso, Z muy alto |
| vidrio borosilicatado | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | pérdidas muy bajas |
| cerámica de alúmina | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | sonido rápido, baja pérdida |
| PMMA (acrílico) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | transparente, limitado por absorción en MHz |
| PVC (rígido) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | más pérdidas que PMMA |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | blando, con pérdidas |
| hormigón | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | la dispersión del árido domina; varía en órdenes de magnitud |
| caucho (cargado) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | el honesto callejón sin salida |

## Los gráficos

**Modo B (MHz) — el peine de espesor por material.** Izquierda: metales estructurales; derecha: no metales. Todas las paredes de 5 mm, acoplamiento con grasa. Los picos del modelo sin pérdidas alcanzan T = 1 en resonancias exactas; los picos reales son menores por pérdidas de contacto, y la absorpción limita directamente a los materiales con pérdidas:

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**El mapa de materiales** — los dos ejes que lo deciden todo: impedancia (dificultad de acoplamiento/contacto) vs. absorción a 1 MHz (viabilidad en MHz). Alta-Z + baja-α es la esquina de grado de potencia; baja-Z + alta-α es "40 kHz todavía abierto, MHz muerto"; la esquina del caucho es un callejón sin salida en cada frecuencia que objetivo:

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Proxy de acoplamiento Modo A (40 kHz)** — el mismo modelo de transmisión evaluado a 40 kHz a través de una pared de 3 mm, normalizado al acero. *Un ranking, no vatios:* el par Langevin resonante multiplica cada barra aproximadamente por igual y el modelo no incluye carga de transductor; ese multiplicador es territorio de etapa 2 ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## Lo que dice el barrido

- **A 40 kHz, las paredes de baja-Z (plásticos, revestimiento de caucho) se acoplan *más fácilmente* que el acero** — a través de grasa están casi emparejadas en impedancia, así que el peine es ancho y la transmisión por paso es alta. Lo que mata a los plásticos a frecuencias más altas es la **absorción volumétrica**, no el contacto ni la impedancia. La escalera de materiales a 40 kHz está por tanto invertida respecto a la intuición: HDPE/PMMA/PVC > vidrio/hormigón > aluminio > alúmina > titanio > acero > cobre — con la fuerte salvedad de que el número de 40 kHz de los cauchos extrapola α linealmente desde 1 MHz, lo que la viscoelasticidad no garantiza.
- **El modo B divide a los materiales limpiamente.** Metales, vidrio y alúmina soportan MHz con absorción despreciable (α ≤ 0.1 dB/cm); el peine es *estrecho* para paredes de alta-Z (acero, alúmina — necesita seguimiento de frecuencia, la lección del ~6% ⇒ ~10× de [00-theory](00-theory.md)) y *ancho* para vidrio/PMMA (tolerante, pero PMMA paga ~1.3 dB unidireccional a 1 MHz a través de 5 mm — solo clase mW).
- **El hormigón es un material de 40 kHz, no de MHz.** La dispersión del árido (λ a 1 MHz ≈ 3.5 mm ≈ tamaño del árido) dispara γ hasta ~2.5 y mata MHz; la práctica de velocidad de pulso ultrasónico (40–80 kHz a través de trayectos ≥1 m) es exactamente el modo A.
- **El nicho de paquetes de baterías ([05](05-applications-map.md)) es acústicamente favorable:** una pared de aluminio de 2–3 mm tiene un proxy de acoplamiento ~3× el del acero y absorción despreciable — el caso estrella es también el caso fácil.
- **La escalera de frecuencias a planificar en modo B** (pared de 5 mm, primer peine): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, cobre ≈ 480, acero ≈ 590, titanio ≈ 610, aluminio ≈ 630, vidrio ≈ 560, alúmina ≈ 990. Pared más delgada ⇒ proporcionalmente más alta.

## La dosis: qué le hace la onda a la pared, frecuencia por frecuencia

La transmisión responde "cuánto pasa"; esta sección responde a la pregunta inversa — **¿cuánto de la onda se queda en la pared, y eso la daña?** El daño de la onda en la pared tiene exactamente dos caras:

- **Tensión** σ = √(2·I·Z) — momento de onda plana; *independiente de la frecuencia*. Comparar contra el límite de fatiga de alto número de ciclos (metales), resistencia flexional/traccional (cerámicas, vidrio, hormigón, caucho).
- **Autocalentamiento** ΔT = α(f)·I·d²/(8k), estado estacionario, ambas caras enfriadas — *depende de la frecuencia* a través de α(f), y ahí es donde la frecuencia muerde: todo material aislante tiene una rodilla por encima de la cual cada octava extra de frecuencia multiplica el calor depositado.

A 1 W/cm² (ya por encima de lo que este proyecto persigue: el objetivo de etapa 2 de 0.5–5 W repartidos sobre una cara de transductor de ~19 cm² es 0.03–0.26 W/cm²):

| Pared | σ @1 W/cm², MPa | límite σ_e, MPa | margen de tensión | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | techo @40 kHz, W/cm² | techo @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| acero | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| aluminio | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| titanio | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| cobre | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| vidrio borosilicatado | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| cerámica de alúmina | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (acrílico) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (rígido) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| hormigón | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| caucho (cargado) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

"Techo" = intensidad continua a la cual la pared se mantiene dentro del 20% de su límite de fatiga/resistencia y por debajo de +20 K de autocalentamiento (estado estacionario, ambas caras a temperatura ambiente). Las operaciones con ciclo de trabajo calientan menos; una pared anclada por una sola cara —el caso habitual, aire en un lado— se calienta hasta 4× más en la cara libre. Estos números son una primera aproximación, no una garantía de diseño. Una convención a destacar: los valores de α son dB de intensidad (10·log₁₀, la convención de dosimetría — una caída de 3 dB reduce I a la mitad); la literatura de END por pulso-eco que cita dB de amplitud (20·log₁₀) describe el MISMO α con números el doble de grandes — verifique qué convención usa una fuente antes de copiar sus números a esta tabla.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

Lo que dice el barrido de dosis:

- **El veredicto sobre el acero de [00-theory](00-theory.md) se mantiene y generaliza**: todo metal estructural transporta 1 W/cm² con márgenes de 65–680× en tensión y microkelvins de autocalentamiento. Los metales son insensibles a la frecuencia en términos de daño — su pérdida es demasiado pequeña para calentar a cualquier potencia que podamos acoplar.
- **El daño por frecuencia en polímeros es térmico, no mecánico.** El margen de tensión del PMMA es un cómodo 60× incluso a 1 W/cm², pero la rodilla de calentamiento está justo alrededor de 1 MHz: benigno (~0.2 K) a 40 kHz, +9.5 K a 1 MHz, +65 K a 5 MHz — territorio de ablandamiento a unos pocos W/cm². El PVC cruza la línea de +10 K ya a ~0.35 W/cm² @ 1 MHz; el caucho absorbe ~288 K por W·cm⁻² a 1 MHz (y ~12 K incluso a 40 kHz) — el calentamiento histérico es *la* razón por la que las paredes revestidas de elastómero mueren, no el peine. El HDPE parte la diferencia y recuerda su punto de fusión: +215 K por W·cm⁻² a 5 MHz.
- **El margen ajustado del hormigón es traccional, no térmico**: 0.40 MPa de tensión de onda contra una resistencia traccional estática de ~2.5 MPa (fatiga aún menor) deja solo un margen de ~6× a 1 W/cm². El régimen de 40–80 kHz se mantiene bien a la densidad de potencia del proyecto; los haces concentrados de multi-W/cm² en hormigón deben evitarse, MHz doblemente (la dispersión calienta las interfaces del árido).
- **Conclusión para la hoja de ruta:** a densidades de potencia del modo A (≤0.3 W/cm²) ningún sólido de la tabla está en peligro — márgenes de tensión ≥11× (el más ajustado es la fatiga traccional del hormigón a 11×; todo lo demás ≥15×) y calentamiento ≤0.2 K para todo sólido de ingeniería (el caucho, la excepción que nadie persigue, ~3.5 K). El mapa de daño justifica el plan del proyecto de escalar la potencia: los primeros límites reales de material aparecen *por encima* de los objetivos de etapa 2, primero en líquidos (cavitación, la regla de ≤1 W/cm² de [00-theory](00-theory.md)), luego en la fatiga traccional del hormigón, luego en polímeros a MHz. Las partes que realmente hay que vigilar a alta potencia siguen siendo la cerámica piezoeléctrica y la línea de adhesivo — [02-safety](02-safety.md) — no la pared.

## Veredicto por material

| Pared | Modo A — potencia 40 kHz | Modo B — potencia/datos MHz | Veredicto |
|---|---|---|---|
| acero | ✓✓ referencia | ✓ peine estrecho — seguir frecuencia | la línea base |
| aluminio | ✓✓ (proxy ~3× acero) | ✓ peine algo estrecho | mejor pared estructural (¡baterías!) |
| titanio | ✓✓ | ✓ peine algo estrecho, baja pérdida | nichos corrosivos/cálidos, drones, cascos |
| cobre | ✓ (acoplamiento más difícil de los metales) | ✓ | nicho: barras selladas/celdas electroquímicas |
| vidrio borosilicatado | ✓✓ | ✓ peine más ancho — el más tolerante | ventanas de laboratorio, mirillas |
| cerámica de alúmina | ✓✓ | ✓ peines más rápidos (990 kHz @ 5 mm), baja pérdida | paredes de proceso caliente/aislante |
| PMMA | ✓ banda ancha | ⚠ clase mW ≤ ~0.5 MHz solo | tanques, recintos; no es pared de potencia en MHz |
| PVC / HDPE | ✓ paredes finas | ✗ absorción | recintos de bajo grado, nodos ligeros en datos |
| hormigón | ✓ 40–80 kHz (práctica UPV) | ✗ dispersión | cimentaciones, tuberías — solo modo A |
| caucho (cargado) | ⚠ extrapolación del modelo sin validar | ✗ | empíricamente el callejón sin salida — [04](04-hybrid-channels.md) |

Una pared de plástico de baja-Z tiene más margen para enlaces de modo A *tolerantes a desalineación* pero ofrece menos margen absoluto de potencia contra la absorción una vez que se sube por encima de ~200 kHz; medir antes de prometer nada.

## Hormigón con armadura — el caso multicapa

El hormigón real nunca es liso: las mallas de refuerzo se sitúan a una profundidad de recubrimiento, y el modelo 1D de placa única anterior no puede verlas. `chart_rebar` / `rebar_table` extienden el modelo a apilamientos generales ([`stack_transmission`](../../../software/simulator/material_map.py), recursión multicapa exacta con absorción por capa, validada en el autotest). Geometría modelada: una pared estructural de 150 mm, una malla de acero de espesor equivalente planar Ø16 mm a 40 mm de recubrimiento; el modelo *planar* es el peor caso — una barra real solo proyecta sombra sobre la parte del haz que intersecta, así que considere estos como valles envolventes, no predicciones:

| Apilamiento (150 mm hormigón) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| 150 mm liso | 0.135 | 0.133 | 8.9e-09 |
| armadura Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| dos mallas Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

Lo que dice el modelo de apilamiento:

- **Una malla planar bajo el haz cuesta ×10 a exactamente 40 kHz** (interferencia de banda de parada por la capa de acero), pero el valle es estrecho: a 100 kHz el mismo apilamiento pierde solo ×2. La lectura práctica para el nicho de tuberías/autoclaves: *un barrido de frecuencia alrededor de 40–120 kHz, no una frecuencia fija*, es lo que permite que un enlace de modo A pase el refuerzo — y los valles se desplazan con la profundidad de recubrimiento, así que un barrido también identifica la geometría (la base de una estimación de profundidad de armadura).
- **Una segunda malla (una rejilla) es casi un mata-paredes en este peor caso** (×45 abajo y plano de banda ancha cerca de 40–100 kHz): el refuerzo denso en el camino es el honesto indicador de "buscar otro punto en la pared", no un problema de procesamiento de señales.
- **El modo B a través de hormigón estructural está muerto con o sin armadura** (nivel 1e-8 a 1 MHz: 5 dB/cm × 15 cm). La armadura ni siquiera entra en la historia a MHz.
- Advertencias, en orden de importancia: supuesto de capa planar (peor caso — una barra Ø16 bloquea bastante menos de la mitad de la sección transversal de un haz de 40–50 mm), onda paralela al eje de la barra asumida, y propagación 1D (sin difracción alrededor de la barra). El experimento de hardware correcto es un banco de barrido sobre una losa real: mapear T(x, y) a 40/80/120 kHz sobre una rejilla de armadura y ajustar las posiciones de los valles del modelo planar a la separación de la rejilla.

## Lo que debería medir un seguimiento de hardware

Antes de confiar en una placa específica: método de dos espesores por material (dos placas de d y 2d en el mismo contacto) para extraer α(f) y c reales — ese único conjunto de datos reemplaza cada fila de la tabla anterior. Pasos bonus naturales dentro de los protocolos existentes: repetir el barrido del experimento [001](../experiments/001-sweep-map-3mm-steel/README.md) sobre una placa de PMMA de 5 mm, una placa de borosilicato o alúmina 99%, y un bloque de hormigón de grado conocido; esperar un pico *más bajo pero más ancho* para los plásticos, un peine estrecho para las cerámicas, y un contacto sensible a la temperatura en todas partes. Durante la pasada de potencia del experimento [002](../experiments/002-watts-3mm-steel/README.md), fijar un termómetro IR (o un termopar fino) a la cara lejana de cada tipo de pared — el ΔT medido a entrada conocida es el único número que valida o mata la columna de calentamiento de la tabla de dosis. Nada en esta página está medido — es el mapa de qué medir primero.
