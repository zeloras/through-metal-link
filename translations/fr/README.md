# liaison-travers-metal

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · Français · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Une plateforme ouverte pour le transfert ultrasonore d'énergie et de données à travers des parois métalliques pleines — « à travers l'acier sans un seul trou », construite avec des moyens de garage.

**Essayez-le maintenant (sans matériel requis) :** `python3 software/sweep-map/sweep_map.py --mock`

**Statut :** étape 0 — préparation · 💰 **[prime de 250 $ pour la première construction indépendante](https://github.com/zeloras/through-metal-link/issues)** · liste d'achat : [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Les docs sont multilingues : l'anglais est la langue primaire et se trouve aux chemins canoniques ; toutes les autres langues reflètent l'arborescence sous [translations/](..). Modifiez n'importe quelle langue — le CI traduit et valide les autres (voir [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Montage étape 1 : Pi → DDS → demi-pont → transformateur → piézo TX | acier | piézo RX → pont → ADC → Pi" width="900"></p>

## L'idée en un paragraphe

Les ondes radio ne traversent pas le métal (cage de Faraday), et un passage de câble signifie un trou, un joint, et un point de défaillance. Les ultrasons, en revanche, traversent le métal sans problème : un élément piézo de chaque côté de la paroi en fait un canal pour l'alimentation et les données. La littérature de laboratoire a déjà prouvé la physique à des niveaux sérieux (RPI : 50 W + 12 Mbit/s à travers 63,5 mm d'acier ; NASA JPL : jusqu'à ~kW à travers 5 mm de titane) — ce sont des preuves d'existence avec du matériel spécialisé, pas la nomenclature garage de ce dépôt. Les brevets fondamentaux ont expiré, et aucune plateforme ouverte et reproductible n'existe encore — ce dépôt en construit une, en commençant par **une puissance de l'ordre du watt et des données en kbit/s à travers 3–5 mm d'acier** une fois l'étape 2 mesurée.

## Feuille de route

| Étape | Livrable | Critère de réussite | Attente |
|---|---|---|---|
| 1. Carte de balayage | réponse en fréquence du canal « Langevin–3 mm acier–Langevin » | paire de résonances trouvée, tracé dans [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. Watts | puissance dans la charge à la résonance | ≥0,5 W à travers 3 mm d'acier, protocole dans [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. Données | FSK/OOK sur la même paire | ≥1 kbit/s sans erreur | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. Nœud | ESP32 + capteur dans une boîte soudée fermée, alimenté et télémétré par le son seul | ≥1 h de fonctionnement autonome | [sim4](docs/img/sim4-power-budget.png) |
| 5. Publication | le dépôt devient public, article/how-to | reproduction par un tiers | — |

## Carte du dépôt

python3 software/sweep-map/sweep_map.py --mock
```

**Terminé quand (par étape) :** étape 1 — le pic de balayage se reproduit sur deux exécutions à moins de <200 Hz près ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)) ; étape 2 — ≥0,5 W dans une charge connue à travers 3 mm d'acier et une LED allumée du côté RX ([experiments/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 La théorie en une minute</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

Le TX piézo est pressé contre la paroi et y envoie une onde longitudinale ; le RX piézo de l'autre côté la reconvertit en électricité. Vitesse du son dans l'acier : ~5900 m/s.

Deux modes de fonctionnement :

| Mode | Fréquence | Résonance définie par | Rendements | Statut |
|---|---|---|---|---|
| **A** — transducteurs Langevin | 40 kHz | la paire de transducteurs (paroi ≪ λ — une « membrane ») | watts, kbit/s | mode de départ (étapes 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — disques | 0,6–1 MHz | résonance d'épaisseur de la paroi ([peigne](docs/img/sim3-thickness-comb.png)) | centaines de mW, centaines de kbit/s | branche après les premiers watts ; nécessite un suivi automatique de la fréquence |

Les principales pertes : désaccord de résonance au sein de la paire (±1 kHz pour les transducteurs Langevin bon marché), qualité du contact acoustique (époxy > couplant graisse + serre > pression à sec), désalignement, dérive de résonance avec la température. La réponse à toutes est la même : **une carte de balayage avant chaque modification de la configuration**.

</details>

<details>
<summary><b>📈 Ce que le banc devrait montrer : tracés d'attente du simulateur</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Un modèle de canal semi-empirique (pas FEM, **pas de données de labo** — intuition pour « à quoi devrait ressembler le balayage et quoi viser »). Les hypothèses sont explicites dans `channel_sim.py` (Q chargé ≈40, facteurs k de contact, η de chaîne ≤40 %). Régénérez avec : `python3 channel_sim.py --out ../../docs/img`.

**Étape 1 — balayage.** Un pic étroit près de ~40 kHz ; les multiplicateurs de contact génériques du modèle sont graisse:sec:vide = 1 : 0,25 : 0,02 (c.-à-d. graisse ≈4× sec et ≈50× vide d'air). Pas de pic signifie un problème avec le contact ou la paire :

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Pourquoi 4 transducteurs Langevin, et non 2.** Avec un Q≈40, un désaccord de résonance de 1,5 kHz au sein de la paire fait chuter la puissance du modèle d'environ 10× :

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**Étape 3 — données.** L'OOK se heurte à la résonance du résonateur (modèle Q~40 → τ≈0,3 ms) : 1 kbit/s est propre, à 5 kbit/s l'œil est fermé. Aller plus vite nécessite le mode B :

<img src="docs/img/sim5-ook-datarate.png" width="720">

**Budget de puissance du récepteur.** Les bandes ombrées sont des **cibles** (mode A 0,5–5 W si l'étape 2 aboutit ; mode B plus bas). Les premières charges réalistes sont des ESP32 / BLE / LED à cycle de service ; le Wi-Fi est indiqué comme un marqueur de pic de consommation, pas une promesse continue :

<img src="docs/img/sim4-power-budget.png" width="720">

**Pour plus tard (mode B).** La plaque devient transparente à un peigne de résonances d'épaisseur — la fréquence doit être suivie :

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Sécurité — à lire avant la première mise sous tension</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Des dizaines à des centaines de volts sur le piézo** une fois le pilote de l'étape 2 en ligne — le TVS côté réception est mis en place AVANT la première exécution sous tension ; gardez vos mains éloignées des fils.
2. **Secteur** — uniquement via une alimentation de laboratoire / isolation ; les cartes de pilote de nettoyeur ultrasonique sont liées galvaniquement au secteur.
3. **Oreilles** — à une puissance non négligeable, utilisez les transducteurs pressés contre du métal ; ne faites jamais fonctionner des ultrasons aériens de haute puissance sans une enceinte.
4. **Chaleur** — un transducteur Langevin non serré surchauffe en quelques minutes à pleine puissance ; serrez-le avant d'augmenter le courant (mise en route électrique brève à faible courant uniquement — voir le README du pilote).
5. **Éclats** — la piézocéramique est fragile : un boulon trop serré ou un choc signifie des éclats ; portez des lunettes de sécurité pour tout travail mécanique.

</details>

docs/            théorie, art antérieur, sécurité, applications, journal de décisions (ADR)
docs/img/        tracés d'attente (générés par software/simulator/channel_sim.py)
hardware/        nomenclature, pilote (demi-pont), récepteur (redresseur/récolteur)
firmware/        firmware du nœud (ESP32 — stub jusqu'à l'étape 4)
software/        scripts de mesure (carte de balayage de réponse en fréquence) et simulateur de canal
experiments/     protocoles d'expérience — à partir du modèle, un répertoire = une expérience
data/            journaux bruts (les gros fichiers restent hors de git)
```

</details>

## Principes

1. **Reproductibilité depuis zéro.** Quiconque dispose d'un fer à souder et d'environ 210 $ peut reproduire le résultat à partir de ce dépôt seul.
2. **Chaque expérience est un protocole.** Pas de « ça marche à peu près » : [experiments/TEMPLATE.md](experiments/TEMPLATE.md) est obligatoire.
3. **Hygiène des brevets.** Nous construisons sur la couche expirée ([docs/01-prior-art.md](docs/01-prior-art.md)) ; les décisions sont consignées dans [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md).
4. **Mesure d'abord, opinion ensuite.** Une carte de balayage avant toute conclusion sur le canal.

## Licences et brevets

Code — Apache-2.0, matériel — CERN-OHL-W v2, documentation — CC-BY-4.0 ; textes complets dans [LICENSES/](../../LICENSES). Quiconque peut forker et bâtir sur ce projet, y compris à des fins commerciales ; la protection par brevet repose sur les clauses de concession et de représailles des licences, ainsi que sur une stratégie d'art antérieur. Le schéma complet et le protocole de publication défensive : [LICENSES.md](LICENSES.md) ; règles de contribution : [CONTRIBUTING.md](CONTRIBUTING.md).
