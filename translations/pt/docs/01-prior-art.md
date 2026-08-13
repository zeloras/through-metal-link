# Estado da arte: no que nos baseamos

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · Português · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## A regra
Cada decisão técnica neste repositório deve ser rastreável a uma fonte da lista "livre" (patentes expiradas, artigos). Patentes vigentes são somente leitura — extraia delas insights sobre os problemas, nunca copie suas reivindicações (isso importa para a comercialização nos EUA; veja o mapa de patentes no projeto).

## A base livre (patentes expiradas/abandonadas = domínio público)
- **US5982297** (Aerospace Corp, 1997) — a receita básica: um par piezo através da parede, energia + dados bidirecionais. O livro de receitas principal.
- US5594705 (Dynamotive, 1994) — um "transformador acústico" através do casco.
- US6037704, US6127942 (Aerospace Corp) — alimentando sensores, lendo dados de volta.
- **US7902943** (Caltech/JPL, caducou por falta de pagamento de taxas de manutenção em 2019) — o feed-through de Sherrit: refletor, transformador acústico.
- US9748870 (Caltech/JPL) — trabalho mecânico através da parede.
- **US9361877** (Univ. Oklahoma, caducou por falta de pagamento de taxas de manutenção) — um sistema transceptor moderno e completo.
- US20100027379 / WO2008105947 (DOE+RPI, abandonada) — uma portadora do lado de fora + modulação de carga do lado de dentro.

## Artigos-chave
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, aço de 63.5 mm.
- Sherrit et al., NASA NTRS 20080048150 — uma lâmpada de 100 W alimentada através de uma parede.
- Yang et al., Sensors 2015 (10.3390/s151229870) — revisão, o melhor resumo dos números.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — metamaterial, 2%→66% através de 1 mm de aço inoxidável (nenhuma patente encontrada até 07.2026).

Esses artigos são a **base de física e higiene de patentes**. Seus números de potência/taxa de bits usaram transdutores de laboratório, colagem e casamento de impedância — não a BOM de Langevin + graxa do AliExpress em [QUICKSTART.md](../QUICKSTART.md). Cite-os como provas de existência; as próprias barras de aprovação do projeto vivem em [experiments/](../experiments/).

## O que não copiamos enquanto está vivo (apenas EUA, até ~2032; os estágios 1–4 não precisam disso de qualquer forma)
OFDM com subportadoras posicionadas para desviar das harmônicas do canal de potência (RPI US9054826); "downlink AM + uplink de modulação de carga + rastreamento de frequência" em full-duplex como um único esquema (RPI US9455791); transdutores conformais para superfícies curvas conforme a abordagem da Drexel (US10594409).
