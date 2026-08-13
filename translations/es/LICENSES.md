# Licencias y protección de patentes

> [English (primary)](../../LICENSES.md) · [Русский](../ru/LICENSES.md) · [Deutsch](../de/LICENSES.md) · [Português](../pt/LICENSES.md) · Español · [Français](../fr/LICENSES.md) · [Italiano](../it/LICENSES.md) · [Polski](../pl/LICENSES.md) · [Türkçe](../tr/LICENSES.md) · [Українська](../uk/LICENSES.md) · [Tiếng Việt](../vi/LICENSES.md) · [中文](../zh/LICENSES.md) · [日本語](../ja/LICENSES.md) · [한국어](../ko/LICENSES.md) · [हिन्दी](../hi/LICENSES.md)

El objetivo de este esquema: que el proyecto sea totalmente abierto, cualquiera puede hacer un fork y construir sobre él (incluido comercialmente), mientras que el riesgo de litigio por patentes se reduce al mínimo absoluto alcanzable por medios legales y procedimentales.

## El esquema (tres capas; textos completos en [LICENSES/](../../LICENSES))

| Área | Licencia | Texto | Disposiciones sobre patentes |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](../../LICENSES/Apache-2.0.txt) | §3: todo contribuyente concede automáticamente una licencia de patente sobre su contribución; presenta una demanda por patentes y pierdes la licencia de **patente** (represalia; la licencia de copyright en §2 es irrevocable y sobrevive a la demanda) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](../../LICENSES/CERN-OHL-W-2.0.txt) | §7.1: una licencia de patente (Fabricar / mandar fabricar / usar / vender / importar…) de cada licenciante — pero solo para reivindicaciones necesariamente infringidas por el Covered Source dado; §7.2: una demanda por patentes (incluido el intento de invalidar la patente de un tercero) termina **todos** los derechos bajo la licencia |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](../../LICENSES/CC-BY-4.0.txt) | no concede **ningún** derecho de patente (§2(b)(2)) — el vacío se cierra con la concesión explícita de patente en [CONTRIBUTING.md](../../CONTRIBUTING.md) |
| todo lo demás (`README.md` raíz, `QUICKSTART.md`, este archivo, `data/`, etc.) | CC-BY-4.0 | — | respaldo: ningún archivo del repositorio queda como "todos los derechos reservados" |

Los archivos de código llevan cabeceras SPDX (Apache-2.0); el mapa de cobertura legible por máquina está en [REUSE.toml](../../REUSE.toml). La línea de copyright vive en [NOTICE](../../NOTICE); el [LICENSE](../../LICENSE) raíz es un puntero a este esquema.

**Por qué CERN-OHL-W, no S ni P.** W es el punto intermedio: el diseño y sus modificaciones deben mantenerse abiertas en cualquier distribución, pero el producto en el que se integra el diseño puede ser comercial y propietario — lo que deja abiertos los nichos de docs/05 (laboratorios, cervecerías, paquetes de baterías). S (copyleft fuerte) cerraría la puerta a la integración; P (permisiva) permitiría forks cerrados. El endurecimiento hacia S está incorporado en la propia licencia: §8.3 permite a cualquiera tratar el material con licencia W como si tuviera licencia S (siempre que se cumpla la condición de Available Components) — sin necesidad de permiso. El aflojamiento (hacia P u otra licencia), en cambio, solo es posible mientras todo el material pertenezca a un único autor; después de la primera contribución externa — solo con el consentimiento de todos los contribuyentes.

**Nombre del proyecto.** "through-metal-link" no es una marca registrada; las propias licencias no conceden derechos sobre el nombre (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Referirse al proyecto de forma factual ("basado en through-metal-link") es libre para cualquiera; los forks con cambios incompatibles deben publicarse bajo su propio nombre.

## De qué protege esto — y de qué no (honestamente)

**Protege contra:**
1. **Demandas de contribuyentes.** Cualquiera que haya contribuido ha licenciado automáticamente sus derechos de patente sobre esa contribución (Apache §3, CERN-OHL §7.1, y CONTRIBUTING para docs). Una demanda le cuesta caro al demandante: bajo Apache-2.0 pierde las licencias de patente sobre el código; bajo CERN-OHL-W pierde todos los derechos sobre la capa de hardware sin más (§7.2 — se activa incluso por un intento de impugnar la patente de otro).
2. **Privatización de forks de hardware.** CERN-OHL-W obliga a cualquiera que distribuya (Conveyance de un producto o de fuentes) a publicar sus modificaciones de diseño — las mejoras fluyen de vuelta a la capa abierta y ellas mismas se convierten en estado de la técnica. (Un fork de cajón, nunca transmitido a terceros, no tiene obligación de publicación — igual que bajo cualquier copyleft.)
3. **Patentes *futuras* de terceros.** Todo lo publicado con fecha destruye la novedad para solicitudes posteriores: para una solución descrita aquí antes de su fecha de presentación, ya no puede concederse una patente válida. Contra solicitudes presentadas *antes* de nuestra publicación esto no funciona — para esas, el único escudo es la capa de patentes expiradas (ver más abajo).

**No protege contra:**
- **Patentes de terceros que ya existen.** Ninguna licencia puede hacer eso. Lo que funciona contra ellas es la disciplina de ingeniería de docs/01-prior-art.md: construir solo a partir de la capa expirada (dominio público), no implementar reivindicaciones vigentes (RPI OFDM/full-duplex, Drexel — hasta ~2032, solo EE. UU.), y rastrear cada decisión de diseño hasta una fuente libre. Eso no es una garantía, pero es exactamente la práctica que hace que una demanda sea inútil.
- Un fork que se encamine a producción comercial hace su propio análisis de FTO (freedom to operate) para su propia jurisdicción y diseño — el repositorio no hace declaraciones sobre patentes (descargos de responsabilidad en las tres licencias).

## Protocolo de publicación defensiva (ejecutar cuando el repo se haga público)

Cada resultado publicado es estado de la técnica con fecha que bloquea todas las solicitudes posteriores de terceros para la misma solución:

1. Abrir el repositorio con su historial git completo (commits = marcas de tiempo).
2. Snapshot a **Zenodo** → DOI: un archivo independiente con una fecha legalmente significativa, citable en artículos.
3. Fijarlo en **Software Heritage** (archive.softwareheritage.org — un espejo perpetuo).
4. Cada experimento completado `experiments/NNN` — con fecha, números y gráficas: esa es la publicación de una solución técnica específica.
5. Hitos importantes (primeros vatios, primer nodo) — un writeup publicado al mundo (Hackaday.io / arXiv / blog): cuanto mayor la difusión, más fuerte el estado de estado de la técnica.

## Para contribuyentes

Las reglas están en [CONTRIBUTING.md](../../CONTRIBUTING.md): DCO sign-off, inbound=outbound, una concesión explícita de patente en cada contribución independientemente del directorio, trazabilidad de las decisiones de diseño a estado de la técnica libre.

Hasta que se abra, el repositorio permanece privado — publicar antes de los primeros resultados reproducibles debilitaría tanto la posición científica como la de patentes.
