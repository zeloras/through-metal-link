# Expérience 002 : Premiers watts à travers 3 mm d'acier (PLANIFIÉE)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · Français · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Étape :** 2 (puissance dans une charge connue à la résonance trouvée dans [001](../001-sweep-map-3mm-steel/README.md)).
- **Objectif :** mesurer la puissance DC réelle délivrée à travers 3 mm d'acier avec le pilote en demi-pont et le transformateur d'adaptation.
- **Hypothèse :** avec une paire de transducteurs Langevin du même lot, un contact par graisse+serre (ou époxy), et un transformateur d'adaptation accordé, ≥0,5 W dans une charge résistive au pic de l'étape 1 est atteignable. (Les chiffres multi-watts/kW de la littérature utilisaient des transducteurs et des liaisons différents — les considérer comme un plafond, pas comme le critère de réussite.)
- **Prérequis :**
  - Expérience 001 clôturée (pic reproductible, fréquence enregistrée).
  - TVS monté sur la chaîne RX avant toute mise sous tension du pilote ([docs/02-safety.md](../../docs/02-safety.md)).
  - Séquence de mise en route du pilote suivie ([hardware/driver/README.md](../../../../hardware/driver/README.md)).
- **Montage (minimum) :**
  - TX : Pi → AD9833 carré → mise en forme du temps mort → IR2110 demi-pont → transformateur d'adaptation → Langevin serré contre la plaque ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Paroi : acier de 3 mm, méthode de contact enregistrée (graisse+serre / époxy / autre).
  - RX : Langevin → pont Schottky → R_load connue (résistance de puissance) et/ou LED ; mesurer V_dc et I_dc après le pont (topologie [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png), charge au lieu d'ADC seul).
- **Procédure (aperçu) :**
  1. Mise en route électrique à limite d'alim 0,2 A sans prétendre à une puissance acoustique.
  2. Serrer TX/RX, régler la fréquence de pilotage sur le pic de l'expérience 001.
  3. Augmenter lentement la limite de courant ; enregistrer V/I de l'alim, température MOSFET/transformateur, V_dc et I_dc sur la charge.
  4. P_load = V_dc · I_dc. Optionnel : photo de démo LED une fois P_load connu.
  5. Répéter une fois après refroidissement ; la fréquence de pic peut dériver avec la température — revérifier avec un mini-sweep si la puissance chute.
- **Critères de réussite :**
  1. P_load ≥ 0,5 W à travers 3 mm d'acier à une fréquence et une méthode de contact documentées.
  2. Deux passages concordent sur P_load à ~20 % près sous la même serre/couplant (stabilité d'ordre de grandeur, pas encore de qualité métrologique).
  3. Photo de la LED (ou autre charge) + CSV/log lié depuis ce fichier sous `data/`.
- **Un échec est une donnée :** si P_load reste ≪ 0,5 W, enregistrer le Δf de la paire (issu de 001), la méthode de contact, le rapport de transformation, et les formes d'onde — c'est l'entrée du prochain ADR, pas une raison pour modifier silencieusement le simulateur.
