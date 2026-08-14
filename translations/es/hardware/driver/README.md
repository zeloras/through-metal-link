# Driver (etapa 2): IR2110 medio puente

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · Español · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Esquemático:** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) (generado por [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

La cadena: Pi (SPI) → AD9833 **en modo onda cuadrada** (bit OPBITEN: MSB enrutado a la salida, oscilación rail a rail — no se necesita un comparador separado) → conformador **74HC14 + RC + 1N4148** (HIN/LIN complementarios con ~1 µs de tiempo muerto) → IR2110 → 2×IRF540 (medio puente) → condensador de bloqueo DC de 1 µF → transformador de adaptación (ferrita, ~1:3..1:5, ajustar en el banco) → transductor Langevin TX.

La salida senoidal del AD9833 (~0.6 Vpp) no sirve para la lógica del IR2110 — si por alguna razón necesitas específicamente una senoidal del DDS, pon un comparador entre ellos (p. ej. un LM393, no está en la BOM).

Alimentación de la etapa de potencia: fuente de banco de 12–24 V con limitación de corriente (**comenzar en 0.2 A**).

Nota: el barrido de la etapa 1 excita el piezoeléctrico directamente con la senoidal débil del DDS (~0.6 Vpp, ver `sweep_map.py`) — **este driver entra en la cadena solo en la etapa 2 (vatios)**. No esperes ≥0.5 W de la conexión de la etapa 1 con solo el DDS.

Notas:
- El transductor Langevin es una carga capacitiva (típicamente unos pocos nF). Un inductor en serie o un transformador de adaptación es obligatorio; sin él los MOSFET disipan la corriente reactiva y se queman.
- **Transformador de adaptación (el punto de fallo habitual).** Comienza con un toroide de ferrita pequeño (p. ej. FT50-43 / similar), primario unas pocas espiras, secundario ~3–5× eso, condensador de bloqueo DC en serie de 1 µF de película en el primario. Ajusta para mínima corriente de la fuente *en la resonancia de la etapa 1* con el TX **fijado a la placa** y el RX cargado. La relación de espiras y la fuga son empíricas — el esquemático las marca con `*` por una razón. Registra las espiras finales en el registro del experimento.
- **Tiempo muerto**: el IR2110 no lo genera por sí solo. La opción con componentes discretos — RC+1N4148 en las entradas del 74HC14 (retrasa solo los flancos de subida, ~1 µs; con un periodo de 25 µs a 40 kHz eso es <5% de pérdida). La opción fácil — un módulo EGS002, todo está integrado ahí.
- **Lógica de 3.3 V**: alimenta el VDD del IR2110 con los mismos 3.3 V que el AD9833 y el 74HC14 — con VDD=5 V el umbral VIH es ≈ 3.1 V y una onda cuadrada de 3.3 V apenas pasa (el datasheet permite VDD hasta 3.3 V).
- **Desacoplo obligatorio**: 100 nF en VDD y VCC (VCC — más 47 µF), y en el riel de potencia 470–1000 µF + 100 nF cerámico justo en las ramas del medio puente — sin esto, un medio puente sobre jumpers de protoboard capta sus propios picos de conmutación. Mantén los cables del lazo de potencia cortos; si el nodo de conmutación oscila fuertemente, sal de la protoboard a una placa de cobre con montaje "dead-bug" / protoboard con plano de tierra antes de subir la corriente.
- **Secuencia de primer encendido** (alineada con [docs/02-safety.md](../../docs/02-safety.md)):
  1. Sin Langevin en el secundario todavía. Fuente = 12 V, límite de corriente 0.2 A. Observa la señal de compuerta (HIN/LIN) y el nodo de conmutación con el osciloscopio — confirma el tiempo muerto y que no haya cortocircuito de rama.
  2. Coloca el transformador de adaptación + TX Langevin **fijado a la placa de acero** (o un bloque de metal grueso de sacrificio). Todavía límite de 0.2 A. Sube solo en la frecuencia pico de la etapa 1 el tiempo suficiente para ver la corriente y el voltaje del RX.
  3. Sube el límite de corriente gradualmente mientras vigilas la temperatura del MOSFET y del transformador. Nunca dejes un Langevin sin fijar con potencia — las pruebas a potencia máxima al aire libre son cómo se agrietan las cerámicas y mueren los drivers.

TODO: proyecto KiCad (PCB) una vez que el prototipo en protoboard (o "dead-bug") funcione. Hasta entonces, los esquemáticos en [`../schematics/`](../../../../hardware/schematics) son la fuente de la verdad del diseño.
