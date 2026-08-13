# Protocole de découverte et d'auto-ajustement du récepteur (brouillon ; implémentation aux étapes 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · Français · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

L'objectif : l'appareil détermine par lui-même s'il y a un récepteur derrière la paroi, choisit lui-même la fréquence et la puissance, et ne grille pas la paroi pour rien si quelqu'un a « oublié de souder le récepteur ».

Le modèle de référence, ce sont les chargeurs Qi : ils résolvent exactement ce problème (y a-t-il un téléphone sur la bobine ?) avec exactement cette séquence. Notre analogue acoustique :

## Phase 0 — ping analogique (le récepteur peut être complètement déchargé)
Le TX effectue un balayage à faible puissance sur toute la bande et mesure **son propre courant et sa propre phase** (shunt + détecteur de crête → ADS1115). Un récepteur résonant derrière la paroi est une charge couplée au TX à travers la paroi : sa présence se manifeste par une bosse/un creux caractéristique sur la courbe d'impédance du TX, même si tout ce qui est à l'intérieur est hors tension. Même principe qu'un détecteur de métaux et du ping analogique de Qi.
- Signature présente → phase 1. Pas de signature → « aucun récepteur trouvé », rester en ping de veille (une fois toutes les N secondes), ne pas augmenter la puissance.
- Bonus : la courbe d'impédance de la paroi « vide » est enregistrée à l'installation comme référence — pour distinguer « pas de récepteur » de « récepteur décollé / désaligné ».

## Phase 1 — handshake numérique
Le TX se cale sur la fréquence candidate (le pic de la phase 0) et délivre de la puissance. Le récolteur d'énergie du RX charge le supercondensateur, le MCU s'éveille et répond par **modulation de charge** : un MOSFET court-circuite périodiquement son piézo selon un code (ID + version du protocole). Le TX perçoit cela comme une modulation de son propre courant. Aucun émetteur n'est nécessaire à l'intérieur — c'est un schéma RFID, le même que dans la demande DOE/RPI abandonnée US20100027379 (art antérieur libre).

## Phase 2 — asservissement de fréquence (perturb & observe)
Le RX peut rapporter sa tension de bus (télémétrie par modulation de charge). Le TX fait des pas de ±Δf et se maintient au maximum de puissance reçue — une boucle MPPT classique. Cela compense la dérive de résonance avec la température (le piège principal de cette niche : un décalage de ~6 % = chute de rendement d'un facteur ~10×).

## Phase 3 — négociation de puissance et watchdog
Le RX demande un niveau (en vie / en charge / en veux plus), le TX plafonne la puissance à ce qui a été demandé. Réponses manquantes pendant M cycles → le TX revient à la phase 0 à faible puissance.

## Matériel requis (élément BOM 12, schéma — hardware/schematics/sch4)
- TX : shunt 0,1 Ω + redresseur/détecteur de crête sur le deuxième canal ADS1115 (courant), optionnellement un comparateur de phase.
- RX : 2N7002 + ~100 Ω sur le **côté DC** du redresseur (la broche VIN du module LTC3588) + GPIO — la charge est commutée après le pont, et le TX le perçoit comme une modulation de son propre courant. Un seul MOSFET en parallèle du piézo AC ne fonctionne pas (la diode de corps shunte une demi-alternance, la grille n'a pas de référence sur un nœud flottant) ; la variante en parallèle du piézo ne fonctionne qu'avec une paire de MOSFET en série tête-bêche.

## Limites
Le ping analogique s'affaiblit à mesure que l'épaisseur de la paroi et les pertes de contact augmentent (la signature se noie dans le bruit) — le seuil de détection doit être mesuré lors d'une expérience dédiée (experiments/). Pour les parois épaisses, solution de repli : le RX, une fois qu'il a accumulé assez de charge, « frappe » périodiquement avec sa propre balise.
