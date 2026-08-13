# Estado del arte: sobre lo que construimos

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · Español · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## La regla
Cada decisión técnica en este repositorio debe ser rastreable hasta una fuente de la lista "libre" (patentes caducadas, artículos). Las patentes vigentes son de solo lectura — úsalas para extraer ideas sobre los problemas, nunca copies sus reivindicaciones (esto importa para la comercialización en EE. UU.; consulta el mapa de patentes del proyecto).

## Los cimientos libres (patentes caducadas/abandonadas = dominio público)
- **US5982297** (Aerospace Corp, 1997) — la receta básica: un par piezoeléctrico a través de la pared, energía + datos bidireccionales. El manual de cocina principal.
- US5594705 (Dynamotive, 1994) — un "transformador acústico" a través del casco.
- US6037704, US6127942 (Aerospace Corp) — alimentación de sensores, lectura de datos de vuelta.
- **US7902943** (Caltech/JPL, caducada por impago de tasas de mantenimiento en 2019) — el feed-through de Sherrit: reflector, transformador acústico.
- US9748870 (Caltech/JPL) — trabajo mecánico a través de la pared.
- **US9361877** (Univ. Oklahoma, caducada por impago de tasas de mantenimiento) — un sistema transceptor moderno y completo.
- US20100027379 / WO2008105947 (DOE+RPI, abandonada) — una portadora desde el exterior + modulación de carga desde el interior.

## Artículos clave
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, 63.5 mm de acero.
- Sherrit et al., NASA NTRS 20080048150 — una lámpara de 100 W alimentada a través de una pared.
- Yang et al., Sensors 2015 (10.3390/s151229870) — revisión, el mejor resumen de las cifras.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — metamaterial, del 2 % al 66 % a través de 1 mm de acero inoxidable (sin patente encontrada a fecha de 07.2026).

Estos artículos son la **base física y de higiene de patentes**. Sus cifras de potencia y bitrate se obtuvieron con transductores de laboratorio, encolado y adaptación — no con el BOM de Langevin + grasa de AliExpress de [QUICKSTART.md](../QUICKSTART.md). Cítalos como pruebas de existencia; las barras de aprobación propias del proyecto están en [experiments/](../../../experiments).

## Lo que no copiamos mientras esté vigente (solo EE. UU., hasta ~2032; las etapas 1–4 no lo necesitan de todos modos)
OFDM con subportadoras colocadas para esquivar los armónicos del canal de energía (RPI US9054826); dúplex completo "enlace descendente AM + modulación de carga en enlace ascendente + seguimiento de frecuencia" como un único esquema (RPI US9455791); transductores conformales para superficies curvas según el enfoque de Drexel (US10594409).
