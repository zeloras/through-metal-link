# Canales híbridos: barrera → física → números

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · [Português](../../pt/docs/04-hybrid-channels.md) · Español · [Français](../../fr/docs/04-hybrid-channels.md) · [Italiano](../../it/docs/04-hybrid-channels.md) · [Polski](../../pl/docs/04-hybrid-channels.md) · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

El principio (corolario de la "paradoja de penetración"): una onda atraviesa una barrera exactamente en la medida en que interactúa débilmente con ella — por eso no existe un canal universal. La plataforma no persigue un único canal; para cada barrera elige la física a la que la barrera es transparente y el receptor es resonantemente "codicioso".

## Tabla de selección de canales

| Barrera | Canal de trabajo | Esperado (órdenes de magnitud) | Notas |
|---|---|---|---|
| Acero/aluminio 1–60 mm, contacto posible | Piezoacústica (nuestro canal principal) | vatios; kbit/s (hasta Mbit/s en modo MHz) | necesita contacto acústico (acoplante de grasa/epoxi) |
| Metal: sucio, pintado, caliente, contacto indeseable | EMAT (magnetismo → sonido en la pared) | mW; kbit/s; hueco hasta ~3 mm | solo paredes conductoras; datos, no potencia |
| Pared ferromagnética sin piezo en absoluto | Magnetostricción (una bobina excita el propio acero) | migajas; bit/s–kbit/s | rama experimental, barato de probar |
| Doble pared con vacío (termo, criostato, dewar) | Magnetismo de LF (decenas–centenas de Hz) | µW–mW; bit/s | efecto pelicular: en acero δ≈0.6 mm @1 kHz — baja la frecuencia |
| No metal: vidrio, plástico, cerámica | Piezoacústica (más fácil que el metal) | vatios; kbit/s | + a menudo RF simple también pasa — comprueba eso primero; números y veredictos por material: [06-materiales](../../../docs/06-materials.md) |
| Pared con capa de goma/espuma, compuesto | Sinceramente: casi un callejón sin salida | — | el absorbedor se traga todo; la solución es un punto sin recubrimiento |
| Líquido detrás de la pared (tanque lleno) | Piezoacústica, degradada | potencia − unos dB; resonancia más corta | la carga líquida desplaza/amortigua la resonancia — re-barrer contra el recipiente lleno; mantener intensidad continua ≲1 W/cm² para quedarse bajo la cavitación ([teoría](00-theory.md#efecto-en-la-pared-y-en-el-medio-detrás-de-ella)) |
| Líquido con burbujas en la ruta acústica | Solución arquitectónica | — | monta el receptor en la pared, mantén el líquido fuera de la ruta |

## Arquitectura de nodo híbrido

- Capa de potencia: par piezo en resonancia (etapas 1–4).
- Capa de datos sin contacto: una cabeza EMAT como "pistola escáner" desmontable (etapa ~6).
- Capa de respaldo: bobinas de LF para sándwiches de vacío (cuando la tarea lo requiere).
- El protocolo de descubrimiento (docs/03) se extiende de "barrer sobre frecuencia" a "barrer sobre física": ping piezo → ping EMAT → ping LF; el nodo elige el canal que pasa por sí solo e informa qué barrera ve.

## Aplicaciones de ejemplo por canal

1. **Baterías selladas (EV/almacenamiento):** sensor T/gas dentro de un encapsulado potting; potencia+datos vía un par piezo a través de 2–3 mm de aluminio. El mercado está en auge, y penetrar un encapsulado de batería = infierno de certificación.
2. **Criostato/dewar:** un registrador de temperatura dentro, enviando un paquete de bits una vez por minuto vía magnetismo de LF a través de la camisa de vacío. Fundamentalmente fuera del alcance de la acústica — aquí el híbrido es irreemplazable.
3. **Tubería/autoclave bajo presión:** un escáner EMAT presionado contra una tubería caliente pintada sin preparación superficial alguna — lee un baliza resonante pasiva desde el interior.
4. **Tanos de fermentación (cerveza/vino, acero inoxidable):** un sensor de densidad/T dentro del tanque sin una sola penetración — los códigos sanitarios adoran la ausencia de agujeros.
5. **Contenedor marino/caja fuerte:** "¿la carga está viva?" — un par piezo a través de acero corrugado, consultado con un escáner manual.

## Limitaciones que ninguna capa puede resolver
Potencia — solo piezo por contacto (EMAT y magnetismo de LF son órdenes de magnitud más débiles). Paredes compuestas/forradas de goma están fuera de la plataforma. La velocidad del canal de LF es bits por segundo — eso es telemetría, no streaming.
