# Experiment 001: Channel Sweep Map, 3 mm Steel (PLANNED)

> English (primary) · [Русский](../../translations/ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../translations/de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../translations/pt/experiments/001-sweep-map-3mm-steel/README.md)

- **Stage:** 1 (frequency map only — no watt target here; power is [002](../002-watts-3mm-steel/README.md)).
- **Goal:** find the resonance of a Langevin transducer pair through a 3 mm plate; get the first frequency response of the channel.
- **Hypothesis:** a peak around 38–42 kHz (Langevin transducer resonance), peak width of a few kHz under grease+clamp contact.
- **Drive:** stage-1 hookup — AD9833 sine (~0.6 Vpp) into TX, **no** half-bridge ([sch3](../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../hardware/schematics/sch2-receiver-stage1.png)).
- **Procedure:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (use `--mock` to dry-run the pipeline without hardware).
- **Success criterion:** a reproducible peak (two sweeps back to back, center deviation <200 Hz). Save CSV/PNG under `data/` and link them from this file when real.
- **Bonus measurement:** the same sweep with "grease couplant + clamp" vs "dry press-on" — relative amplitudes only; absolute volts depend on drive level and are not comparable to the simulator’s placeholder scale until calibrated.
- **Out of scope:** ≥0.5 W, LED-from-harvest, half-bridge bring-up → experiment 002.
