# Experiment 001: Kanal-Sweep-Karte, 3 mm Stahl (GEPLANT)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · Deutsch · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md)

- **Stufe:** 1 (nur Frequenzkarte — kein Watt-Ziel hier; Leistung ist [002](../002-watts-3mm-steel/README.md)).
- **Ziel:** Resonanz eines Langevin-Wandler-Paares durch eine 3 mm Platte finden; erste Frequenzantwort des Kanals erhalten.
- **Hypothese:** ein Peak um 38–42 kHz (Langevin-Wandler-Resonanz), Peakbreite von einigen kHz unter Schmiermittel-Kupplung+Klemme-Kontakt.
- **Antrieb:** Stufe-1-Verbindung — AD9833-Sinus (~0,6 Vpp) in TX, **kein** Halbbrückenschaltkreis ([sch3](../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../hardware/schematics/sch2-receiver-stage1.png)).
- **Vorgehensweise:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (verwenden Sie `--mock`, um die Pipeline ohne Hardware zu testen).
- **Erfolgskriterium:** ein reproduzierbarer Peak (zwei Sweep nacheinander, Mittelabwich <200 Hz). Speichern Sie CSV/PNG unter `data/` und verlinken Sie sie von dieser Datei, wenn sie real sind.
- **Bonus-Messung:** derselbe Sweep mit "Schmiermittel-Kupplung + Klemme" vs "trockener Press-on" — relative Amplituden nur; absolute Volt hängen von der Antriebsebene ab und sind nicht mit der Platzhalter-Skala des Simulators vergleichbar, bis sie kalibriert sind.
- **Nicht im Rahmen:** ≥0,5 W, LED-von-Harvest, Halbbrückenschaltkreis-Inbetriebnahme → Experiment 002.
