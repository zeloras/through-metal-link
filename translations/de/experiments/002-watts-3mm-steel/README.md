# Experiment 002: Erste Watts durch 3 mm Stahl (GEPLANT)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · Deutsch · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md)

- **Stufe:** 2 (Leistung in eine bekannte Last bei der Resonanz, die in [001](../../../../experiments/001-sweep-map-3mm-steel/README.md) gefunden wurde).
- **Ziel:** Messen der realen Gleichstromleistung, die durch 3 mm Stahl mit dem Halbbrückentreiber und dem abgestimmten Transformator geleitet wird.
- **Hypothese:** Mit einem Langevin-Paar aus dem gleichen Los, Schmiermittel+Klemme (oder Epoxid) Kontakt und einem abgestimmten Transformator ist eine Leistung von ≥0,5 W in eine resistive Last bei der Spitze der Stufe 1 erreichbar. (Literaturwerte mit mehreren Watt/kW verwendeten unterschiedliche Wandlersysteme und Bonding – behandeln Sie sie als Obergrenze, nicht als Erfolgskriterium.)
- **Voraussetzungen:**
  - Experiment 001 abgeschlossen (reproduzierbare Spitze, Frequenz aufgezeichnet).
  - TVS auf der RX-Kette vor jeder Treiberleistung installiert ([docs/02-safety.md](../../docs/02-safety.md)).
  - Treiber-Bring-up-Sequenz befolgt ([hardware/driver/README.md](../../hardware/driver/README.md)).
- **Aufbau (mindestens):**
  - TX: Pi → AD9833 Quadrat → Totzeit-Formung → IR2110 Halbbrücke → abgestimmter Transformator → Langevin auf einer Platte geklemmt ([sch1](../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Wand: 3 mm Stahl, Kontaktmethode aufgezeichnet (Schmiermittel+Klemme / Epoxid / andere).
  - RX: Langevin → Schottky-Brücke → bekannter R_Load (Leistungs-Widerstand) und/oder LED; Messen von V_dc und I_dc nach der Brücke ([sch2](../../hardware/schematics/sch2-receiver-stage1.png) Topologie, Last anstelle von ADC-only).
- **Verfahren (Übersicht):**
  1. Elektrische Inbetriebnahme bei 0,2 A Netzteil-Limit ohne Anspruch auf akustische Leistung.
  2. Klemmen von TX/RX, Festlegen der Antriebsfrequenz auf die Spitze des Experiments 001.
  3. Langsames Erhöhen des Stromlimits; Aufzeichnen von Netzteil V/I, MOSFET/Transformator-Temperatur, V_dc und I_dc auf der Last.
  4. P_Load = V_dc · I_dc. Optional: Kurze LED-Demo-Foto, sobald P_Load bekannt ist.
  5. Wiederholen nach einer Abkühlung; die Spitzenfrequenz kann sich mit der Temperatur verschieben – Überprüfen mit einem Mini-Sweep, wenn die Leistung abfällt.
- **Erfolgskriterien:**
  1. P_Load ≥ 0,5 W durch 3 mm Stahl bei einer dokumentierten Frequenz und Kontaktmethode.
  2. Zwei Durchgänge stimmen bei P_Load innerhalb von ~20% unter der gleichen Klemme/Koppelmedium (Größenordnung-Stabilität, nicht metrologische Genauigkeit) überein.
  3. Foto von LED (oder anderer Last) + CSV/Log, verknüpft mit dieser Datei unter `data/`.
- **Fehlschlag ist Daten:** Wenn P_Load ≪ 0,5 W bleibt, aufzeichnen des Paars Δf (aus 001), Kontaktmethode, Transformator-Wicklungen und Wellenformen – das ist der Eingang für die nächste ADR, kein Grund, den Simulator stillschweigend zu bearbeiten.
