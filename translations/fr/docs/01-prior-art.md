# État de l'art : sur quoi nous nous appuyons

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · Français · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## La règle
Chaque décision technique dans ce dépôt doit être traçable à une source de la liste « libre » (brevets expirés, articles). Les brevets en vigueur sont en lecture seule — exploitez-les pour comprendre les problèmes, ne copiez jamais leurs revendications (cela compte pour la commercialisation aux États-Unis ; voir la cartographie des brevets dans le projet).

## Le socle libre (brevets expirés/abandonnés = domaine public)
- **US5982297** (Aerospace Corp, 1997) — la recette de base : une paire de piézos à travers la paroi, énergie + données bidirectionnelles. Le manuel de référence principal.
- US5594705 (Dynamotive, 1994) — un « transformateur acoustique » à travers la coque.
- US6037704, US6127942 (Aerospace Corp) — alimenter des capteurs, lire les données en retour.
- **US7902943** (Caltech/JPL, tombé pour non-paiement des frais de maintien en 2019) — le feed-through de Sherrit : réflecteur, transformateur acoustique.
- US9748870 (Caltech/JPL) — travail mécanique à travers la paroi.
- **US9361877** (Univ. Oklahoma, tombé pour non-paiement des frais de maintien) — un système émetteur-récepteur complet et moderne.
- US20100027379 / WO2008105947 (DOE+RPI, abandonné) — une porteuse depuis l'extérieur + modulation de charge depuis l'intérieur.

## Articles clés
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12,4 Mbit/s, 63,5 mm d'acier.
- Sherrit et al., NASA NTRS 20080048150 — une lampe de 100 W alimentée à travers une paroi.
- Yang et al., Sensors 2015 (10.3390/s151229870) — revue, la meilleure synthèse des chiffres.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — métamatériau, 2 %→66 % à travers 1 mm d'inox (aucun brevet trouvé au 07.2026).

Ces articles constituent la **référence en matière de physique et d'hygiène brevet**. Leurs chiffres de puissance/débit ont été obtenus avec des transducteurs de laboratoire, un collage et un adaptateur d'impédance — pas avec le BOM Langevin AliExpress + graisse de [QUICKSTART.md](../QUICKSTART.md). Citez-les comme preuves d'existence ; les critères de réussite propres au projet se trouvent dans [experiments/](../../../experiments).

## Ce qu'on ne copie pas tant que c'est vivant (États-Unis uniquement, jusqu'à ~2032 ; les étapes 1–4 n'en ont de toute façon pas besoin)
OFDM avec sous-porteuses placées pour éviter les harmoniques du canal d'énergie (RPI US9054826) ; « liaison descendante AM + liaison montante par modulation de charge + suivi de fréquence » en duplex intégral comme schéma unique (RPI US9455791) ; transducteurs conformes pour surfaces courbes selon l'approche Drexel (US10594409).
