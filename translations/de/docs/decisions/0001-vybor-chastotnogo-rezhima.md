# ADR-0001: Frequenzmodus-Auswahl für Phase 1

> [English (primary)](../../../../docs/decisions/0001-vybor-chastotnogo-rezhima.md) · [Русский](../../../ru/docs/decisions/0001-vybor-chastotnogo-rezhima.md) · Deutsch · [Português](../../../pt/docs/decisions/0001-vybor-chastotnogo-rezhima.md)

- Status: AKZEPTIERT (wird nach Phase 2 überarbeitet)
- Datum: 2026-07-24

## Kontext
Zwei Modi (siehe docs/00-theory.md): A — 28–40 kHz auf Langevin-Transducern, B — 0,6–1 MHz auf Scheiben, die die Dicke-Resonanz der Wand nutzen.

## Entscheidung
Phasen 1–2 verwenden Modus A. Gründe: günstiger ($10–30 pro Stück), leistungsstärker (Watt versus einige hundred mW), einfacher zu stimmen (breite Resonanz) und der Treiber kann aus einer Halbbrücke um einen IR2110 aufgebaut werden. Modus B wird nach dem ersten Durchbruch von einigen Watt — als separates Zweig für Hochgeschwindigkeits-Daten — umgesetzt.

## Konsequenzen
Daten in Phase 3 werden langsam sein (kbit/s) — ausreichend für ein Sensorknoten. Der ADS1115-ADC (860 SPS) ist für die Hüllkurve bei 40 kHz nach dem Gleichrichter geeignet, aber nicht für direktes Abtasten — direktes Abtasten wird auf Modus B verschoben (benötigt einen anderen ADC).
