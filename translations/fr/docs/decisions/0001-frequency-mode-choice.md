# ADR-0001 : Choix du mode de fréquence pour l'étape 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · Français · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Statut : ACCEPTÉ (à revoir après l'étape 2)
- Date : 2026-07-24

## Contexte
Deux modes (voir docs/00-theory.md) : A — 28–40 kHz sur des transducteurs Langevin, B — 0,6–1 MHz sur des disques exploitant la résonance d'épaisseur de la paroi.

## Décision
Les étapes 1–2 utilisent le mode A. Raisons : moins cher (10–30 $ pièce), plus puissant (des watts contre des centaines de mW), plus tolérant au réglage (résonance large), et le driver peut être construit autour d'un demi-pont utilisant un IR2110. Le mode B arrive après avoir fait passer les premiers watts — comme une branche séparée pour les données à haute vitesse.

## Conséquences
Les données à l'étape 3 seront lentes (kbit/s) — suffisant pour un nœud capteur. Le CAN ADS1115 (860 SPS) convient pour l'enveloppe à 40 kHz après le redresseur, mais pas pour l'échantillonnage direct — l'échantillonnage direct est reporté au mode B (nécessite un CAN différent).

L'étape 1 (balayage) utilise uniquement le pilotage DDS faible ; l'étape 2 (watts) est une expérience et une mise en route séparées ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). Les bandes de puissance du simulateur restent des objectifs tant que 002 n'est pas mesuré.
