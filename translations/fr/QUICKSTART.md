# QUICKSTART : du zéro absolu au banc de test étapes 1–2

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Português](../pt/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · Français · [Italiano](../it/QUICKSTART.md) · [Polski](../pl/QUICKSTART.md) · [Türkçe](../tr/QUICKSTART.md) · [Українська](../uk/QUICKSTART.md) · [Tiếng Việt](../vi/QUICKSTART.md) · [中文](../zh/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md)

Scénario : vous n'avez qu'un bureau et un peu de budget. Tout ce qui suit vous mène à un banc fonctionnel — « cartographie par balayage + premiers watts à travers l'acier ». Les prix sont indicatifs, en USD.

## Panier 1 — outillage (une base pour des années, ~120 $)

| Article | Pourquoi | Prix | Où |
|---|---|---|---|
| Station de soudage (clone T12) | tout | 35–50 | Ali |
| Multimètre (classe AN8008/UT61) | tensions, continuité, capacité | 15–25 | Ali |
| Alim. de labo 30 V/5 A avec limitation de courant | alimente le driver ; la limite de courant est votre assurance contre les MOSFETs grillés | 45–60 | Ali/local |
| Bras d'aide, soudure, flux, tresse à dessouder, coupe-fils, pinces | le petit matériel indispensable | 15 | Ali/local |
| Fils Dupont + breadboard + gaine thermorétractable | prototypage | 8 | Ali |

## Panier 2 — électronique du banc (~70 $)

| Article | Qté | Prix | Note |
|---|---|---|---|
| Raspberry Pi (Zero 2 W suffit ; 4/5 plus confortable) + SD | 1 | 20–60 | le cerveau : balayage, logs, tracés |
| Transducteur Langevin 40 kHz 50–60 W | **4** | 40 | achetez 4 d'UN MÊME lot ; on choisira la meilleure paire par balayage |
| Module DDS AD9833 | 2 | 8 | le deuxième est de rechange |
| IR2110 + IRF540 ×4 (ou module EGS002) | 1 jeu | 10 | demi-pont driver |
| ADC ADS1115 | 2 | 4 | le Pi n'a pas d'ADC intégré |
| Tore ferrite + fil de cuivre émaillé 0,5 mm | 2 | 4 | transformateur d'adaptation |
| Pont Schottky (SS14 ×8), supercondensateur 1F 5,5V ×2 | 1 | 4 | chaîne réceptrice |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | protection. NE PAS ROULER SUR LE BUDGET |
| Module GY-LTC3588 | 1 | 7 | récupérateur d'énergie (étape 4, mais commandons-le maintenant) |
| Assortiment résistances/condensateurs, LEDs | 1 | 8 | si vous n'avez rien du tout |
| Passifs de support : UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | broutille ; liste complète — BOM articles 11–12 |

## Panier 3 — mécanique (~20 $, en local)

Tôle d'acier 3 mm ~150×150 — 2 pièces (négociant en métaux / découpe laser) ; serre-joints type F ×2 ; couplant gras épais et homogène (graisse au lithium) ; époxy ; papier abrasif (pour nettoyer la zone de contact).

## Optionnel, mais fortement recommandé (~90 $)

| Article | Pourquoi | Prix |
|---|---|---|
| Oscilloscope USB/portatif (FNIRSI/Hantek, 2 voies ; pas besoin de ≥40 MHz de bande passante — 10 suffisent largement) | voir la forme du signal sur la grille et sur le piézo ; fait gagner des jours de débogage du driver | 60–80 |
| ESP32 DevKit ×2 | étape 4 (le nœud derrière la paroi) | 8 |

**Total : minimum vital ~210 $, confortable ~300 $.** (Si vous avez déjà un Pi, une station de soudage et une alim. de labo dans votre stock — déduisez ~120 $.)

## Bon de commande (le chemin critique, c'est la livraison)

1. Aujourd'hui : panier 2 chez Ali (livraison 3–4 semaines — c'est le chemin critique) + l'oscilloscope.
2. Cette semaine : paniers 1 et 3 en local.
3. Pendant la livraison : `raspi-config` → SPI+I2C, lancez `software/sweep-map/sweep_map.py --mock` sans matériel (canal synthétique — tout le pipeline CSV+tracés fonctionne sur n'importe quel ordinateur), lisez docs/00–03, regardez les tracés attendus dans docs/img et les schémas dans hardware/schematics (la construction de l'étape 1 suit sch3 et sch2).

## Ce que vous verrez (simulateur : software/simulator/channel_sim.py → docs/img)

Ces PNG sont des **attentes du modèle**, pas des mesures de laboratoire. Les ratios de contact, le Q chargé ≈40, et le rendement de chaîne ≤40 % sont des hypothèses explicites dans `channel_sim.py` — remplacez-les par les données de balayage/puissance une fois le banc assemblé.

- `sim0-rig-sketch.png` — tout le banc en un croquis (chaîne étape 2 ; l'étape 1 omet le demi-pont et pilote le TX depuis le signal sinusoïdal faible du DDS).
- `sim1-sweep-contacts.png` — forme de balayage attendue : un pic étroit vers ~40 kHz ; le modèle utilise graisse:sec:vide ≈ 1 : 0,25 : 0,02 comme valeurs provisoires. Pas de pic — déboguez d'abord le contact ou l'appariement (sim2).
- `sim2-pair-mismatch.png` — pourquoi 4 transducteurs Langevin et pas 2 : avec Q≈40, un écart de résonance de 1,5 kHz au sein d'une paire fait chuter la puissance du modèle d'un facteur ~10 ; le balayage sélectionne la meilleure paire parmi 4.
- `sim3-thickness-comb.png` — pour plus tard (mode B, MHz) : la tôle est transparente comme un peigne de résonances d'épaisseur, donc la fréquence doit être suivie.
- `sim4-power-budget.png` — consommation de la charge vs bandes de puissance reçue **cible**. La bande du mode A (0,5–5 W) est l'ambition de l'étape 2 si l'adaptation et le contact coopèrent ; le mode B est la bande inférieure. Le Wi-Fi continu est un marqueur de charge de pointe, pas une promesse — les premiers consommateurs réalistes sont l'ESP32/BLE/LED en mode cyclique.
- `sim5-ook-datarate.png` — étape 3 : pourquoi OOK sur transducteurs Langevin plafonne à ~1–2 kbit/s sous Q≈40 (temps de ring-down τ≈0,3 ms), et pourquoi c'est suffisant pour un nœud capteur.

## Critères pour « le banc fonctionne »

Séparés par étape — ne déclarez pas l'étape 1 terminée avec les chiffres de l'étape 2.

**Étape 1 — cartographie par balayage** ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)) :
1. Balayage 25–45 kHz en deux passes consécutives : le centre du pic se reproduit à moins de 200 Hz près.
2. Bonus optionnel : graisse+serre-joint vs pression à sec sur la même paire (amplitudes relatives, pas watts absolus).

**Étape 2 — premiers watts** ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)) :
1. Demi-pont + transformateur d'adaptation en service ; mise sous tension avec limitation de courant selon [docs/02-safety.md](../../docs/02-safety.md) et [hardware/driver/](../../hardware/driver/README.md).
2. À la résonance de l'étape 1, ≥0,5 W dans une charge résistive connue à travers 3 mm d'acier (mesurer V et I côté DC après le pont RX).
3. Une LED derrière la plaque s'allume grâce à l'énergie récupérée ; photo + CSV dans experiments/002.

Sécurité avant la première mise sous tension : [docs/02-safety.md](../../docs/02-safety.md) (TVS sur le récepteur, limite de courant de l'alim. à 0,2 A pour la mise en route, pas de fonctionnement Langevin en plein air à haute puissance).
