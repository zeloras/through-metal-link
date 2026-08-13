# Experiment 001: Kanal-Sweep-Karte, 3 mm Stahl (GEPLANT)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · Deutsch · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · [Polski](../../../pl/experiments/001-sweep-map-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **Phase:** 1 (nur Frequenzkarte — hier kein Watt-Ziel; Leistung ist [002](../002-watts-3mm-steel/README.md)).
- **Ziel:** die Resonanz eines Langevin-Transducer-Paares durch eine 3-mm-Platte finden; die erste Frequenzantwort des Kanals aufnehmen.
- **Hypothese:** ein Peak um 38–42 kHz (Langevin-Transducer-Resonanz), Peakbreite von einigen kHz bei Fett+Klemm-Kontakt.
- **Ansteuerung:** Phase-1-Verkabelung — AD9833 Sinus (~0,6 Vpp) in TX, **keine** Halbbrücke ([sch3](../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../hardware/schematics/sch2-receiver-stage1.png)).
- **Vorgehen:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (`--mock` verwenden, um die Pipeline ohne Hardware im Probelauf auszuführen).
- **Erfolgskriterium:** ein reproduzierbarer Peak (zwei Sweeps hintereinander, Mittelpunktsabweichung <200 Hz). CSV/PNG unter `data/` speichern und aus dieser Datei verlinken, sobald real.
- **Zusatzmessung:** derselbe Sweep mit „Fett-Kopplung + Klemme" vs. „trocken aufpressen" — nur relative Amplituden; absolute Volt hängen vom Ansteuerungspegel ab und sind bis zur Kalibrierung nicht mit der Platzhalterskala des Simulators vergleichbar.
- **Nicht im Rahmen:** ≥0,5 W, LED-from-Harvest, Halbbrücke-Hochlauf → Experiment 002.
