# Cómo contribuir

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · Español · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Gracias por querer impulsar el canal abierto a través del acero. Las tres reglas siguientes no son burocracia — son la armadura de patentes del proyecto (consulta [LICENSES.md](LICENSES.md) para saber por qué).

## 1. Licencias de contribución (entrante = saliente)

Al enviar una contribución, aceptas que se licencia de la misma manera que el resto del material en su directorio:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Concesión de patentes.** Además — dado que CC-BY-4.0 no licencia patentes — concedes al proyecto y a todos los destinatarios de sus materiales una licencia de patente perpetua, irrevocable, mundial, libre de regalías y no exclusiva para fabricar, hacer que se fabrique, usar, ofrecer para la venta, vender, importar y, de otro modo, transferir tu contribución, tanto por sí sola como como parte del proyecto — en la medida de aquellas de tus reclamaciones de patente que sean necesariamente infringidas por la contribución por sí sola o por su combinación con el proyecto al que se envió. Los términos siguen el §3 de Apache-2.0, independientemente del directorio en el que haya aterrizado la contribución. Si inicias litigios de patentes contra alguien (incluyendo una contrademanda) alegando que los materiales del proyecto infringen tu patente, entonces todas las licencias de **patente** que el proyecto y sus colaboradores te han concedido bajo esta cláusula y bajo las licencias del proyecto terminan a partir de la fecha en que se presenta dicho litigio.

## 2. DCO: una firma sobre la procedencia

Signed-off-by: Firstname Lastname <email@example.com>
```

Los PRs sin un sign-off no se fusionan; la comprobación es automática — el trabajo de CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) hace fallar el PR si incluso un solo commit carece de sign-off. La protección de patentes de la capa de documentación depende exactamente de esta cadena — sin excepciones.

**Mover material entre capas.** El material vive en la capa en la que aterrizó (y bajo la licencia de esa capa). Mover texto/código entre capas con diferentes licencias solo está permitido si es material propio, o con una nota explícita de la licencia original del fragmento.

## 3. Higiene de patentes y protocolo de experimentación

- Cada decisión técnica debe rastrearse hasta una fuente gratuita — una patente expirada o un artículo de [docs/01-prior-art.md](docs/01-prior-art.md). No se aceptan implementaciones de reivindicaciones vigentes (listadas también allí) hasta que dichas reivindicaciones expiren.
- Resultados experimentales — únicamente mediante la plantilla [experiments/TEMPLATE.md](experiments/TEMPLATE.md): un protocolo fechado y reproducible es precisamente lo que constituye nuestro estado de la técnica.
- Las decisiones de arquitectura se gestionan mediante ADRs en [docs/decisions/](docs/decisions/).
- Los comentarios de código, docstrings, identificadores y mensajes de commit son exclusivamente en inglés. La documentación es multilingüe (ver más abajo); las etiquetas visibles para el usuario en las figuras viven en `labels.json`.

## 4. Documentación multilingüe: edita un idioma, CI sincroniza el resto

El inglés es el idioma principal y posee las rutas canónicas. Todos los demás idiomas son árboles espejo bajo [translations/](..) con nombres de archivo idénticos — markdown, el CSV de la BOM y las figuras generadas incluidas; el texto de las figuras se controla mediante `labels.json`. **No** tienes que mantener los espejos a mano:

- Edita el idioma que te resulte cómodo. Al hacer push, el flujo de trabajo [Sincronización de traducción](../../.github/workflows/translate.yml) traduce las contrapartes con un LLM de pesos abiertos (`glm-5.2` en Ollama Cloud), regenera las figuras cuando la sincronización actualiza `labels.json`, y confirma el resultado de vuelta con el marcador `[translate-sync]`. Cualquier endpoint compatible con OpenAI funciona — establece `OPENAI_BASE_URL` y `TRANSLATE_MODEL`.
- Lo que aún debe trabajo se rastrea en `translations/.sync-state.json`, que registra el contenido principal a partir del cual se hizo cada traducción. Una ejecución interrumpida por una cuota o un tiempo de espera, por lo tanto, no pierde nada: los pares inacabados permanecen marcados como obsoletos y son retomados por el siguiente push o por la ejecución nocturna. No edites ese archivo a mano.
- Si editaste **varios** idiomas de un documento tú mismo, cada versión que tocaste se mantiene tal como la escribiste; el bot solo rellena los idiomas que no tocaste.
- **`labels.json` es la excepción a "edita cualquier idioma".** Las etiquetas de las figuras fluyen solo del principal → a los espejos. Editar una etiqueta traducida arregla ese idioma y se detiene ahí; no viaja de vuelta al inglés. Para cambiar lo que una etiqueta *dice*, edita la sección principal. La razón es la asimetría: la edición de una etiqueta casi siempre es alguien corrigiendo la redacción de la máquina, y permitir que eso reescriba el principal redefiniría la fuente de la que se generan los catorce espejos. Las claves que el bot nunca ha producido aún se propagan hacia atrás, por lo que una etiqueta escrita a mano no queda atrapada en un solo idioma.
- La traducción automática se confirma — revisa el commit del bot y retoca la redacción si no capta el tono; tu corrección no será sobrescrita (el bot registra tu versión como la actual).
- Una respuesta que regresa truncada o con los marcadores de posición de `labels.json` destrozados se descarta en lugar de confirmarse, y el par se reintenta — por lo que un espacio de aspecto extraño en un espejo es un par obsoleto, no una decisión.
- **PRs externos:** el bot se ejecuta en `master`, por lo que un PR puede cambiar solo un idioma — los espejos (incluyendo el inglés) se ponen al día automáticamente justo después de la fusión. No necesitas saber inglés para contribuir con documentos.
- **Añadir un idioma:** añade su código y nombre a [i18n.json](../../i18n.json) (p. ej., `"fr": "Français"`) y haz push — el pipeline construye todo el espejo `translations/fr/`: cada documento, una sección `fr` en cada `labels.json`, el conjunto de figuras y los selectores de idioma en todas partes.
- **Scripts no latinos:** CI instala las familias Noto (`fonts-noto-core`, `fonts-noto-cjk`) y los renderizadores recorren la pila de fuentes en `i18n.json` → `render.fonts`, por lo que el cirílico, el Han, el kana y el Hangul salen correctamente. Un renderizador ahora verifica la cobertura de glifos antes de dibujar y **falla en lugar de pintar cajas `.notdef`** — esa verificación existe porque las figuras en chino se publicaron como una cuadrícula de tofu y nada en CI mira los píxeles. Si se activa, añade la fuente Noto para ese script a la pila.
- **Scripts que necesitan conformación contextual** — árabe y persa (RTL, formas unidas), devanagari y bengalí (conjuntos) — no pueden ser dibujados correctamente por matplotlib, que no tiene motor de conformación: incluso con la fuente correcta, los glifos salen desunidos y desordenados. Lista esos idiomas en `i18n.json` → `render.skip_figures`. Su prosa no se ve afectada; sus documentos simplemente enlazan a las figuras principales, a las que la reparación de enlaces en [tools/translate_sync.py](../../tools/translate_sync.py) apunta automáticamente. `hi` está configurado de esta manera.
- **Guardia de script:** `SCRIPTS` en [tools/i18n_render.py](../../tools/i18n_render.py) registra qué script deben contener las etiquetas de cada idioma. Una respuesta que no tenga ninguno — las secciones `ja` una vez se publicaron llenas de ruso — se rechaza y se reintenta en lugar de confirmarse. Un idioma que falte en esa tabla simplemente no obtiene guardia, por lo que añadir uno a `i18n.json` nunca rompe nada; añade la entrada para obtener la verificación.

## 5. Verificaciones que puedes ejecutar antes de hacer push

python tools/check_repo.py
```

Verifica lo que el bot de traducción es capaz de romper y nada más detectaría: que cada enlace relativo resuelva, que cada sección de `labels.json` coincida con `i18n.json` y contenga las mismas claves y los mismos marcadores de `str.format` que la principal, que cada documento canónico tenga su réplica en cada idioma, y que cada archivo markdown incluya su barra de idiomas. CI lo ejecuta en ambos flujos de trabajo; no requiere dependencias.

El resto de CI ([ci.yml](../../.github/workflows/ci.yml)) compila los scripts y ejecuta todo el pipeline de figuras. Para reproducirlo exactamente —incluyendo las figuras versionadas— instala el toolchain fijado, no el flexible:

```bash
python -m pip install -r tools/requirements-ci.txt
