# ADR-0001: Auswahl des Frequenzmodus für Stufe 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · Deutsch · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Status: AKZEPTIERT (wird nach Stufe 2 erneut geprüft)
- Datum: 2026-07-24

## Kontext
Zwei Modi (siehe docs/00-theory.md): A — 28–40 kHz an Langevin-Wandlern, B — 0,6–1 MHz an Scheiben, die die Dickenresonanz der Wand ausnutzen.

## Entscheidung
Stufen 1–2 verwenden Modus A. Gründe: günstiger (10–30 $ pro Stück), leistungsstärker (Watt statt Hunderte mW), unkomplizierter abzustimmen (breite Resonanz) und der Treiber lässt sich aus einer Halbbrücke um einen IR2110 aufbauen. Modus B kommt nach den ersten durchgeleiteten Watt — als separater Zweig für Hochgeschwindigkeitsdaten.

## Konsequenzen
Daten in Stufe 3 werden langsam sein (kbit/s) — ausreichend für einen Sensorknoten. Der ADS1115 ADC (860 SPS) ist für die Hüllkurve bei 40 kHz nach dem Gleichrichter geeignet, aber nicht für direkte Abtastung — direkte Abtastung wird auf Modus B verschoben (benötigt einen anderen ADC).

Stufe 1 (Sweep) verwendet nur den schwachen DDS-Antrieb; Stufe 2 (Watt) ist ein separates Experiment und Inbetriebnahme ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)). Simulator-Leistungsbänder bleiben Zielvorgaben, bis 002 vermessen ist.
