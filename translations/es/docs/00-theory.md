# Teoría del canal (lo mínimo que necesitas para trabajar)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · [Português](../../pt/docs/00-theory.md) · Español · [Français](../../fr/docs/00-theory.md) · [Italiano](../../it/docs/00-theory.md) · [Polski](../../pl/docs/00-theory.md) · [Türkçe](../../tr/docs/00-theory.md) · [Українська](../../uk/docs/00-theory.md) · [Tiếng Việt](../../vi/docs/00-theory.md) · [中文](../../zh/docs/00-theory.md) · [日本語](../../ja/docs/00-theory.md) · [한국어](../../ko/docs/00-theory.md) · [हिन्दी](../../hi/docs/00-theory.md)

## Principio
Un elemento piezoeléctrico TX prensado/pegado contra la pared excita en ella una onda longitudinal; un piezo RX en el otro lado la convierte de nuevo en electricidad. La pared es un resonador: en las resonancias de espesor (múltiplos de una semilongitud de onda) la transmisión alcanza su máximo.

## Números clave
Velocidad longitudinal del sonido en acero: ~5900 m/s.

| Espesor de acero | Resonancia de semionda |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Longitud de onda en acero: 148 mm @ 40 kHz; 5.9 mm @ 1 MHz.

## Dos modos
- **A (40 kHz, transductores Langevin).** Una placa de 3–5 mm ≪ λ — se comporta como una membrana; la resonancia la fija el par de transductores, no la pared. Más sencillo y potente que el modo B — el primero con el que empezar. Prueba de existencia en laboratorio (no es un objetivo de garaje): NASA JPL ~24.5 kHz, cientos de W hasta un kW a través de 5 mm de Ti con hardware diseñado a medida.
- **B (0.6–1 MHz, discos).** Resonancia de espesor de la propia pared, y afilada (un desplazamiento de frecuencia de ~6% ⇒ la transmisión cae ~10× en el modelo Fabry–Perot). La clase de resultados RPI/Moss: cientos de mW más datos a cientos de kbit/s con acoplamiento y adaptación de laboratorio. Requiere seguimiento automático de frecuencia.

## Principales pérdidas
Desajuste de resonancia dentro del par de transductores (los transductores Langevin baratos se dispersan ±1 kHz), calidad del contacto acústico (epoxi > grasa espesa como acoplante + abrazadera > presión en seco), desalineación, deriva de resonancia con la temperatura. La respuesta a todo esto es la misma: hacer un barrido de mapeo antes de cada cambio en la configuración.

## Efecto en la pared y en el medio detrás de ella

Versión corta: a los niveles de potencia de la plataforma, la pared y cualquier gas detrás de ella quedan intactos. Un líquido detrás de la pared afecta sobre todo *al canal*; el canal solo empieza a afectar *al líquido* cerca del umbral de cavitación. Las cifras aproximadas siguientes son para el modo A: 40 kHz, ~1 W/cm² en acero de 3 mm.

**Pared — sin deformación, sin fatiga, nunca.** Velocidad de partícula v = √(2I/ρc) ≈ 21 mm/s ⇒ desplazamiento ≈ 80 nm, deformación de onda plana ε = v/c ≈ 3.5·10⁻⁶. Dos estimaciones de tensión equivalentes: elástica E·ε ≈ 0.7 MPa (E ≈ 200 GPa) y acústica p = Z·v ≈ 1.0 MPa (Z_acero ≈ 4.6·10⁷ Pa·s/m). El acero cede a 250+ MPa y su límite de resistencia a la fatiga es ~200 MPa — sigue habiendo un margen >200× de cualquier forma, y por debajo del límite de resistencia el acero soporta ciclos ilimitados. Las partes mecánicamente frágiles están en otro sitio: la cerámica piezoeléctrica (frágil, se despolariza al sobrecalentarse) y la línea de unión (el epoxi se calienta y se fatiga primero) — ver [02-safety](../../../docs/02-safety.md).

**Gas detrás de la pared — efecto cero.** El desajuste de impedancia acero→aire (~4.6·10⁷ vs ~400 Pa·s/m) transmite una fracción del orden de 10⁻⁵ de la potencia. Sin calentamiento ni agitación medibles; la electrónica dentro de una caja sellada no nota el movimiento de la pared a escala nm.

**Líquido detrás de la pared — dos direcciones:**

- *Líquido → canal (siempre).* El agua carga la cara opuesta con ~1.5 MRayl en lugar de aire: parte de la potencia se radía al líquido, cae la Q, el pico del barrido se desplaza y se ensancha. El modo B es el más afectado — el peine de resonancias de espesor se calcula para fronteras acero–aire y se desplaza con la carga líquida. La regla vigente cubre esto: **re-barrer contra el recipiente real y completo**, nunca confíes en un barrido tomado contra uno vacío. Beneficio adicional: la amortiguación del líquido acorta la resonancia del resonador (τ), por lo que el ojo OOK se abre a bitrates más altos. Las burbujas en el camino (¡líquido en fermentación!) dispersan fuertemente — ver la solución en [04-hybrid-channels](../../../docs/04-hybrid-channels.md).
- *Canal → líquido (solo a alta potencia).* Presión pico radiada al agua: p ≈ ρc·v ≈ 1.5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0.3 atm. El umbral de cavitación inercial a 40 kHz en agua ordinaria (con gases) es ~1–2 atm, así que a 1 W/cm² el margen es 3–10×. Pero p crece como √potencia, y las ondas estacionarias en un recipiente cerrado crean puntos calientes locales — decenas de W/cm² continuos en un tanque lleno de líquido pueden alcanzar el umbral. Cruzarlo significa desgasificación de CO₂, sonoquímica (sabores desagradables en productos alimenticios) y erosión por cavitación a largo plazo de la superficie interior (exactamente como limpian los limpiadores ultrasónicos). Techo práctico para potencia continua en paredes respaldadas por líquido: **≲1 W/cm²**. El modo B está exento: a MHz el umbral es un orden de magnitud superior y las potencias son de cientos de mW.

## Presupuesto de potencia del receptor (estimación)
LED 20 mW; ESP32 en ciclo de trabajo 1–5 mW de media; radio BLE ~150 mW mientras el radio está encendido. Reserva: un supercondensador de 1 F @ 3.3 V almacena E = ½CV² = 5.4 J. Cuántas transmisiones permite depende del tiempo al aire: un evento corto de publicidad BLE (~2–5 ms a ~150 mW) son solo ~0.3–0.8 mJ → del orden de **10⁴ paquetes** desde un condensador lleno; una conexión / ráfaga larga (~100 ms de radio encendido) son ~15 mJ → del orden de **10² ráfagas**. El consumo medio sigue teniendo que mantenerse dentro de los vatios cosechados (el objetivo de la etapa 2 es ≥0.5 W en la carga, esa es la puerta; hasta que se mida, trata las bandas de modo A de varios vatios en las gráficas del simulador como objetivos, no como datos).
