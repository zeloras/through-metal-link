# ADR-0001: Frequenzmodus-Auswahl für Stufe 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · Deutsch · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Status: AKZEPTIERT (wird nach Stufe 2 überarbeitet)
- Datum: 2026-07-24

## Kontext
Zwei Modi (siehe docs/00-theory.md): A — 28–40 kHz auf Langevin-Transducern, B — 0,6–1 MHz auf Scheiben, die die Dicke-Resonanz der Wand nutzen.

## Entscheidung
Stufen 1–2 verwenden Modus A. Gründe: günstiger ($10–30 pro Stück), leistungsstärker (Watt versus einige hundert mW), einfacher zu stimmen (breite Resonanz) und der Treiber kann aus einer Halbbrücke um einen IR2110 aufgebaut werden. Modus B kommt nach dem ersten Durchbruch von einigen Watt — als separates Zweig für Hochgeschwindigkeits-Daten — zum Einsatz.

## Konsequenzen
Daten bei Stufe 3 werden langsam sein (kbit/s) — ausreichend für ein Sensorknoten. Der ADS1115-ADC (860 SPS) ist für die Hüllkurve bei 40 kHz nach dem Gleichrichter geeignet, aber nicht für direktes Abtasten — direktes Abtasten wird auf Modus B verschoben (benötigt einen anderen ADC).

Stufe 1 (Sweep) verwendet nur den schwachen DDS-Antrieb; Stufe 2 (Watt) ist ein separates Experiment und eine Inbetriebnahme ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)). Simulator-Leistungsbänder bleiben Ziele, bis 002 gemessen wird.
