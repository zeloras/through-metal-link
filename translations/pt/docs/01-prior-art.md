# Arte anterior: o que construímos

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · Português · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md)

## A regra
Toda decisão técnica neste repositório deve ser rastreável a uma fonte da lista "livre" (patentes expiradas, artigos). Patentes vivas são de leitura apenas — extraia insights dos problemas, nunca copie as reivindicações (isso importa para comercialização nos EUA; veja o mapa de patentes no projeto).

## A fundação livre (patentes expiradas/abandonadas = domínio público)
- **US5982297** (Aerospace Corp, 1997) — a receita básica: um par piezoelétrico através da parede, potência + dados bidirecionais. O livro de receitas principal.
- US5594705 (Dynamotive, 1994) — um "transformador acústico" através do casco.
- US6037704, US6127942 (Aerospace Corp) — alimentando sensores, lendo dados de volta.
- **US7902943** (Caltech/JPL, expirado devido a taxas de manutenção não pagas em 2019) — a alimentação de Sherrit: refletor, transformador acústico.
- US9748870 (Caltech/JPL) — trabalho mecânico através da parede.
- **US9361877** (Univ. Oklahoma, expirado devido a taxas de manutenção não pagas) — um sistema transceptor completo moderno.
- US20100027379 / WO2008105947 (DOE+RPI, abandonado) — um portador de fora + modulação de carga de dentro.

## Artigos-chave
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12,4 Mbit/s, 63,5 mm de aço.
- Sherrit et al., NASA NTRS 20080048150 — uma lâmpada de 100 W alimentada através de uma parede.
- Yang et al., Sensors 2015 (10.3390/s151229870) — revisão, o melhor resumo dos números.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — metamaterial, 2%→66% através de 1 mm de inox (nenhuma patente encontrada até 07.2026).

Esses artigos são a **base de física e higiene de patentes**. Os números de potência/taxa de bits utilizados transdutores de laboratório, ligação e acoplamento — não o Langevin do AliExpress + BOM de graxa em [QUICKSTART.md](../QUICKSTART.md). Cite-os como provas de existência; as próprias barras de passagem do projeto estão em [experiments/](../experiments/).

## O que não copiamos enquanto está vivo (apenas EUA, até ~2032; etapas 1–4 não precisam disso de qualquer forma)
OFDM com subportadoras posicionadas para evitar as harmônicas do canal de potência (RPI US9054826); full-duplex "AM downlink + load-modulation uplink + frequency tracking" como um único esquema (RPI US9455791); transdutores conformes para superfícies curvas de acordo com a abordagem Drexel (US10594409).
