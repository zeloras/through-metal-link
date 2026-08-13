# Mapa de aplicaciones: quién necesita esta pila tecnológica, y por qué

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · [Português](../../pt/docs/05-applications-map.md) · Español · [Français](../../fr/docs/05-applications-map.md) · [Italiano](../../it/docs/05-applications-map.md) · [Polski](../../pl/docs/05-applications-map.md) · [Türkçe](../../tr/docs/05-applications-map.md) · [Українська](../../uk/docs/05-applications-map.md) · [Tiếng Việt](../../vi/docs/05-applications-map.md) · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

La pila de la plataforma: un canal activo de potencia y datos a través de paredes ciegas — piezoacústica / EMAT / magnéticos de baja frecuencia. A continuación: dónde se necesita esto en el mundo real, quién ya está ahí, y qué nos queda a nosotros.

## 1. Baterías selladas (VE, almacenamiento de energía doméstico/industrial)
- Dolor: detección temprana de fuga térmica — los gases (CO₂, H₂, vapores de electrolito) aparecen dentro del paquete minutos u horas antes de un incendio; una penetración de sensor en el recinto = pérdida del sellado hermético y de la certificación.
- Nuestra pila: un nodo de gas/temperatura dentro del paquete, potencia y telemetría mediante un par piezo a través de 2–3 mm de aluminio. Cero agujeros.
- Quién ya está ahí: Liminal Insights — *diagnóstico acústico desde el exterior* (patentes sobre métodos de análisis, no sobre el canal). Nadie vende nodos *dentro* del paquete.
- Madurez del nicho: el mercado crece de forma explosiva, el estante está vacío. Para la plataforma — aplicación de demostración n.º 1.

## 2. Equipamiento de laboratorio: cámaras de vacío, criostatos, cajas de guantes
- Dolor: cada paso eléctrico hacia una cámara de vacío es una brida que cuesta cientos de dólares y una fuente de fugas; en un criostato, un cable = fuga de calor.
- Nuestra pila: un sensor dentro de la cámara, potencia/datos por sonido a través de la pared de acero; para los sándwiches de vacío de los dewares — magnéticos de baja frecuencia (bit/s es suficiente para un registrador de temperatura).
- Quién ya está ahí: nadie con inalámbrico a través de pared; los laboratorios viven de bridas de paso.
- Madurez: el nicho inicial ideal para código abierto — los laboratorios son exactamente el público del hardware abierto (el camino TinyLev): compran sin certificaciones y te citan en artículos.

## 3. Producción de alimentos: tanques de fermentación, autoclaves (cerveza, vino, lácteos)
- Dolor: los códigos sanitarios odian las penetraciones (lavado CIP, zonas muertas); quieres conocer densidad/T/presión dentro del tanque en todo momento.
- Nuestra pila: un nodo en la pared interior de un tanque de acero inoxidable, consultado desde fuera con un escáner portátil o un par fijo.
- Quién ya está ahí: sensores convencionales con penetración; sin soluciones inalámbricas a través de pared.
- Madurez: literalmente al alcance de una prueba de garaje (cualquier cervecería artesanal es un campo de pruebas a poca distancia a pie).
- Advertencia física: un tanque lleno carga la pared — re-barrer contra el recipiente lleno, y mantener potencia continua ≲1 W/cm²; por encima de eso, cavitación en el producto (desgasificación de CO₂, sabores indeseados, erosión de pared a largo plazo) — [teoría](00-theory.md#effect-on-the-wall-and-the-media-behind-it).

## 4. Tuberías, recipientes a presión, END industrial
- Dolor: monitorear corrosión/parámetros internos sin parada ni penetración; las superficies están calientes, pintadas, sucias.
- Nuestra pila: una "pistola escáner" EMAT — presiónala contra una tubería sin preparación de superficie, lee un baliza resonante pasiva desde el interior.
- Quién ya está ahí: medidores de flujo ultrasónicos de abrazadera y medidores de espesor (un mercado maduro), pero sin balizas interactivas en el interior.
- Madurez: rango medio; requiere la rama EMAT (etapa ~6).

## 5. Petróleo y gas / fondo de pozo, y nuclear
- Quién ya está ahí: Metrol, Acoustic Data, Baker Hughes (fondo de pozo, 30 años, modelo de servicio); I+D de DOE/UNT/Westinghouse (contenedores nucleares).
- Veredicto honesto: ocupado y fuertemente regulado — no vamos ahí, pero su mera existencia = prueba de que esta física se vende por dinero serio. Úsalo como referencia en el README.

## 6. Logística marítima y estructuras submarinas
- Dolor: "¿la carga está viva?" en un contenedor sellado; datos desde el lado interior del casco de un barco.
- Quién ya está ahí: CSignum (EM de baja frecuencia a través de agua/mamparos) — el único vecino directo en filosofía híbrida.
- Madurez: largo alcance; para nosotros, por ahora, solo una dirección de pensamiento.

## Prioridades (qué hacer, en qué orden)
1. **Ahora:** etapas 1–4 de la plataforma en el escenario de demostración "cámara de laboratorio / caja sellada por soldadura" (nicho n.º 2 — el más abierto al código abierto).
2. **Después:** una demostración en un objeto real del nicho n.º 3 (un tanque de cervecería) — barato, fotogénico, un usuario real.
3. **Rango medio:** el escenario de batería (nicho n.º 1) como caso insignia para publicación; la rama EMAT para el nicho n.º 4.

*La visión pasiva (radiografía de muones) se ha escindido en un proyecto aparte — ver muon-lab en la base de conocimiento.*
