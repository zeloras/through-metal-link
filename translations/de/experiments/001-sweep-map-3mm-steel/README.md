# Experiment 001: Kanal-Sweep-Karte, 3 mm Stahl (GEPLANT)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · Deutsch

- Ziel: Resonanz eines Langevin-Wandler-Paares durch eine 3 mm Platte finden; erste Frequenzantwort des Kanals erhalten.
- Hypothese: ein Peak um 38-42 kHz (Langevin-Wandler-Resonanz), Peakbreite von einigen kHz.
- Vorgehensweise: software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50
- Erfolgskriterium: ein reproduzierbarer Peak (zwei Sweep nacheinander, Mittelabwich <200 Hz).
- Bonus-Messung: derselbe Sweep mit "Schmiermittel-Kupplung + Klemme" Kontakt vs "trockener Press-on" — das erste Datensatz-Paar, das nirgendwo in der offenen Literatur existiert.
