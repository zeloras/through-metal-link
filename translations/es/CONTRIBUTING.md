# Cómo contribuir

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · Español · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Gracias por querer avanzar el canal abierto a través del acero. Las tres reglas siguientes no son burocracia — son la armadura de patentes del proyecto (ver [LICENSES.md](LICENSES.md) para saber por qué).

## 1. Licencias de contribución (entrada = salida)

Al enviar una contribución, aceptas que se licencia de la misma manera que el resto del material en su directorio:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Concesión de patentes.** Además — dado que CC-BY-4.0 no licencia patentes — concedes al proyecto y a todos los destinatarios de sus materiales una licencia de patente perpetua, irrevocable, mundial, libre de regalías y no exclusiva para fabricar, hacer fabricar, usar, ofrecer para la venta, vender, importar y, en general, transferir tu contribución, tanto por sí sola como como parte del proyecto — en la medida de aquellas de tus reivindicaciones de patente que sean necesariamente infringidas por la contribución por sí sola o por su combinación con el proyecto al que fue enviada. Los términos siguen el §3 de Apache-2.0, independientemente del directorio en el que haya aterrizado la contribución. Si inicias litigio por patentes contra cualquiera (incluida una contrademanda) alegando que los materiales del proyecto infringen tu patente, entonces todas las licencias de **patente** que el proyecto y sus colaboradores te concedieron bajo esta cláusula y bajo las licencias del proyecto terminan a partir de la fecha en que se presenta dicho litigio.

## 2. DCO: una firma sobre la procedencia

Cada commit lleva un sign-off (`git commit -s`), lo que significa aceptación del [Developer Certificate of Origin 1.1](https://developercertificate.org/): confirmas que tienes derecho a enviar esta contribución bajo la licencia del proyecto.

```
Signed-off-by: Nombre Apellido <email@example.com>
```

Los PR sin sign-off no se fusionan; la comprobación es automática — el job de CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) hace fallar el PR si aunque sea un solo commit carece de sign-off. La protección de patentes de la capa de docs descansa exactamente en esta cadena — sin excepciones.

**Mover material entre capas.** El material vive en la capa en la que aterrizó (y bajo la licencia de esa capa). Mover texto/código entre capas con licencias distintas solo se permite si es material propio, o con una nota explícita de la licencia original del fragmento.

## 3. Higiene de patentes y protocolo de experimentos

- Cada decisión técnica debe trazarse a una fuente gratuita — una patente expirada o un artículo de [docs/01-prior-art.md](docs/01-prior-art.md). No se aceptan implementaciones de reivindicaciones vigentes (listadas también allí) hasta que dichas reivindicaciones expiren.
- Resultados experimentales — solo mediante la plantilla [experiments/TEMPLATE.md](experiments/TEMPLATE.md): un protocolo fechado y reproducible es precisamente lo que constituye nuestro prior art.
- Las decisiones de arquitectura pasan por ADRs en [docs/decisions/](docs/decisions/).
- Los comentarios de código, docstrings, identificadores y mensajes de commit son solo en inglés. La documentación es multilingüe (ver más abajo); las etiquetas visibles para el usuario en figuras viven en `labels.json`.

## 4. Docs multilingües: edita un idioma, CI sincroniza el resto

El inglés es el idioma principal y posee las rutas canónicas. Todos los demás idiomas son árboles espejo bajo [translations/](..) con nombres de archivo idénticos — markdown, el CSV de la BOM y las figuras generadas incluidas; el texto de las figuras se controla con `labels.json`. **No** tienes que mantener los espejos a mano:

- Edita el idioma que te resulte cómodo. Al hacer push, el workflow [Translation sync](../../.github/workflows/translate.yml) traduce las contrapartes con un LLM de pesos abiertos (`glm-5.2` en Ollama Cloud), regenera las figuras cuando la sincronización actualiza `labels.json`, y commitea el resultado con el marcador `[translate-sync]`. Cualquier endpoint compatible con OpenAI funciona — define `OPENAI_BASE_URL` y `TRANSLATE_MODEL`.
- Lo que aún debe trabajo se rastrea en `translations/.sync-state.json`, que registra el contenido primario a partir del cual se hizo cada traducción. Una ejecución interrumpida por una cuota o un timeout no pierde nada: los pares sin terminar quedan marcados como obsoletos y se retoman en el siguiente push o en la ejecución nocturna. No edites ese archivo a mano.
- Si editaste **varios** idiomas de un doc tú mismo, cada versión que tocaste se conserva tal como la escribiste; el bot solo rellena los idiomas que no tocaste.
- **`labels.json` es la excepción a "edita cualquier idioma".** Las etiquetas de figuras fluyen solo de primario → espejos. Editar una etiqueta traducida arregla ese idioma y se detiene ahí; no viaja de vuelta al inglés. Para cambiar lo que una etiqueta *dice*, edita la sección primaria. La razón es la asimetría: una edición de etiqueta casi siempre es alguien corrigiendo la redacción de la máquina, y permitir que eso reescriba el primario redefiniría la fuente de la que se generan los catorce espejos. Las claves que el bot nunca ha producido sí se propagan hacia atrás, así que una etiqueta escrita a mano no queda atrapada en un solo idioma.
- La traducción automática se commitea — revisa el commit del bot y ajusta la redacción si no acierta con el tono; tu corrección no se sobrescribirá (el bot registra tu versión como la actual).
- Una respuesta que llegó truncada o con placeholders de `labels.json` corruptos se descarta en lugar de commitearse, y el par se reintenta — así que un hueco raro en un espejo es un par obsoleto, no una decisión.
- **PRs externos:** el bot corre en `master`, así que un PR puede cambiar un solo idioma — los espejos (incluido el inglés) se ponen al día automáticamente justo después del merge. No necesitas saber inglés para contribuir con docs.
- **Añadir un idioma:** añade su código y nombre a [i18n.json](../../i18n.json) (p. ej. `"fr": "Français"`) y haz push — el pipeline construye todo el espejo `translations/fr/`: cada doc, una sección `fr` en cada `labels.json`, el conjunto de figuras y los selectores de idioma en todas partes.
- **Scripts no latinos:** CI instala las familias Noto (`fonts-noto-core`, `fonts-noto-cjk`) y los renderizadores recorren la pila de fuentes en `i18n.json` → `render.fonts`, de modo que el cirílico, el Han, el kana y el Hangul salen correctamente. Un renderizador ahora verifica la cobertura de glifos antes de dibujar y **falla en lugar de pintar cajas `.notdef`** — esa comprobación existe porque las figuras en chino se publicaron como una cuadrícula de tofu y nada en CI mira los píxeles. Si se dispara, añade la fuente Noto para ese script a la pila.
- **Scripts que necesitan composición contextual** — árabe y persa (RTL, formas unidas), devanagari y bengalí (conjuncciones) — no pueden dibujarse correctamente con matplotlib, que no tiene motor de composición: incluso con la fuente correcta los glifos salen sin unir y mal ordenados. Lista esos idiomas en `i18n.json` → `render.skip_figures`. Su prosa no se ve afectada; sus docs simplemente enlazan a las figuras primarias, a las que la reparación de enlaces en [tools/translate_sync.py](../../tools/translate_sync.py) apunta automáticamente. `hi` está configurado así.
- **Guardia de script:** `SCRIPTS` en [tools/i18n_render.py](../../tools/i18n_render.py) registra qué script deben contener las etiquetas de cada idioma. Una respuesta que no tenga ninguno — las secciones `ja` una vez se publicaron llenas de ruso — se rechaza y se reintenta en lugar de commitearse. Un idioma ausente de esa tabla simplemente no tiene guardia, así que añadir uno a `i18n.json` nunca rompe; añade la entrada para tener la comprobación.

## 5. Comprobaciones que puedes ejecutar antes de hacer push

```bash
python tools/check_repo.py
```

Verifica lo que el bot de traducción es capaz de romper y nada más detectaría: cada enlace relativo resuelve, cada sección de `labels.json` coincide con `i18n.json` y lleva las mismas claves y los mismos placeholders de `str.format` que la primaria, cada doc canónico tiene un espejo en cada idioma, y cada archivo markdown tiene su barra de idiomas. CI lo ejecuta en ambos workflows; no necesita dependencias.

El resto de CI ([ci.yml](../../.github/workflows/ci.yml)) compila los scripts y ejecuta todo el pipeline de figuras. Para reproducirlo exactamente — incluidas las figuras commiteadas — instala el toolchain fijado, no el suelto:

```bash
python -m pip install -r tools/requirements-ci.txt
```
