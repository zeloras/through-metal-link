# Experiment 001: Channel Sweep Map, 3 mm Steel (PLANNED)

> English (primary) · [Русский](../../translations/ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../translations/de/experiments/001-sweep-map-3mm-steel/README.md)

- Goal: find the resonance of a Langevin transducer pair through a 3 mm plate; get the first frequency response of the channel.
- Hypothesis: a peak around 38-42 kHz (Langevin transducer resonance), peak width of a few kHz.
- Procedure: software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50
- Success criterion: a reproducible peak (two sweeps back to back, center deviation <200 Hz).
- Bonus measurement: the same sweep with "grease couplant + clamp" contact vs "dry press-on" — the first pair of data points that exist nowhere in the open literature.
