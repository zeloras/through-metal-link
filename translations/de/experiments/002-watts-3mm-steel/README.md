# Experiment 002: Erste Watt durch 3 mm Stahl (GEPLANT)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · Deutsch · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Stufe:** 2 (Leistung in eine bekannte Last bei der in [001](../001-sweep-map-3mm-steel/README.md) gefundenen Resonanz).
- **Ziel:** echte DC-Leistung messen, die durch 3 mm Stahl mit dem Halbbrücken-Treiber und dem Anpassungsübertrager geliefert wird.
- **Hypothese:** Mit einem Langevin-Paar aus derselben Charge, Fett+Klemme (oder Epoxid) als Kontakt und einem abgestimmten Anpassungsübertrager sind ≥0,5 W in eine ohmsche Last beim Stufe-1-Peak erreichbar. (Multi-Watt/kW-Angaben aus der Literatur verwendeten andere Transducer und Bonding — als Obergrenze betrachten, nicht als Bestehenskriterium.)
- **Voraussetzungen:**
  - Experiment 001 abgeschlossen (reproduzierbarer Peak, Frequenz dokumentiert).
  - TVS in der RX-Kette eingebaut, bevor Treiberleistung anliegt ([docs/02-safety.md](../../docs/02-safety.md)).
  - Inbetriebnahmesequenz des Treibers befolgt ([hardware/driver/README.md](../../hardware/driver/README.md)).
- **Aufbau (Minimum):**
  - TX: Pi → AD9833 Rechteck → Totzeit-Former → IR2110 Halbbrücke → Anpassungsübertrager → Langevin auf Platte geklemmt ([sch1](../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Wand: 3 mm Stahl, Kontaktmethode dokumentiert (Fett+Klemme / Epoxid / andere).
  - RX: Langevin → Schottky-Brücke → bekannte R_load (Leistungswiderstand) und/oder LED; V_dc und I_dc nach der Brücke messen ([sch2](../../hardware/schematics/sch2-receiver-stage1.png) Topologie, Last statt nur-ADC).
- **Vorgehen (Übersicht):**
  1. Elektrische Inbetriebnahme bei 0,2 A PSU-Strombegrenzung ohne Beanspruchung akustischer Leistung.
  2. TX/RX klemmen, Ansteuerfrequenz auf den Peak aus Experiment 001 einstellen.
  3. Strombegrenzung langsam erhöhen; PSU V/I, MOSFET/Übertrager-Temperatur, V_dc und I_dc an der Last protokollieren.
  4. P_load = V_dc · I_dc. Optional: kurzes LED-Demo-Foto, sobald P_load bekannt ist.
  5. Einmal nach Abkühlung wiederholen; die Peakfrequenz kann mit der Temperatur driften — bei Leistungsabfall mit einem Mini-Sweep erneut prüfen.
- **Erfolgskriterien:**
  1. P_load ≥ 0,5 W durch 3 mm Stahl bei dokumentierter Frequenz und Kontaktmethode.
  2. Zwei Durchläufe stimmen bei P_load innerhalb ~20 % unter derselben Klemmung/Kopplungsmittel überein (Größenordnungs-Stabilität, noch keine metrologische Genauigkeit).
  3. Foto der LED (oder anderen Last) + CSV/Log verlinkt aus dieser Datei unter `data/`.
- **Misserfolg ist Daten:** Wenn P_load ≪ 0,5 W bleibt, Paar-Δf (aus 001), Kontaktmethode, Übertrager-Windungszahlen und Oszillogramme protokollieren — das ist der Input für das nächste ADR, kein Grund, den Simulator stillschweigend zu ändern.
