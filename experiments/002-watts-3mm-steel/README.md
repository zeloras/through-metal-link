# Experiment 002: First Watts Through 3 mm Steel (PLANNED)

> English (primary) · [Русский](../../translations/ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../translations/de/experiments/002-watts-3mm-steel/README.md) · [Português](../../translations/pt/experiments/002-watts-3mm-steel/README.md) · [中文](../../translations/zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../translations/ja/experiments/002-watts-3mm-steel/README.md)

- **Stage:** 2 (power into a known load at the resonance found in [001](../001-sweep-map-3mm-steel/README.md)).
- **Goal:** measure real DC power delivered through 3 mm steel with the half-bridge driver and matching transformer.
- **Hypothesis:** with a same-batch Langevin pair, grease+clamp (or epoxy) contact, and a tuned matching transformer, ≥0.5 W into a resistive load at the stage-1 peak is achievable. (Literature multi-watt/kW figures used different transducers and bonding — treat them as ceiling, not the pass bar.)
- **Prerequisites:**
  - Experiment 001 closed (reproducible peak, frequency recorded).
  - TVS fitted on the RX chain before any driver power ([docs/02-safety.md](../../docs/02-safety.md)).
  - Driver bring-up sequence followed ([hardware/driver/README.md](../../hardware/driver/README.md)).
- **Setup (minimum):**
  - TX: Pi → AD9833 square → dead-time shaper → IR2110 half-bridge → matching transformer → Langevin clamped to plate ([sch1](../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Wall: 3 mm steel, contact method recorded (grease+clamp / epoxy / other).
  - RX: Langevin → Schottky bridge → known R_load (power resistor) and/or LED; measure V_dc and I_dc after the bridge ([sch2](../../hardware/schematics/sch2-receiver-stage1.png) topology, load instead of ADC-only).
- **Procedure (outline):**
  1. Electrical bring-up at 0.2 A PSU limit without claiming acoustic power.
  2. Clamp TX/RX, set drive frequency to the experiment-001 peak.
  3. Raise current limit slowly; log PSU V/I, MOSFET/transformer temperature, V_dc and I_dc on the load.
  4. P_load = V_dc · I_dc. Optional: short LED demo photo once P_load is known.
  5. Repeat once after a cool-down; peak frequency may drift with temperature — re-check with a mini-sweep if power falls off.
- **Success criteria:**
  1. P_load ≥ 0.5 W through 3 mm steel at a documented frequency and contact method.
  2. Two runs agree on P_load within ~20% under the same clamp/couplant (order-of-magnitude stability, not metrology-grade yet).
  3. Photo of LED (or other load) + CSV/log linked from this file under `data/`.
- **Failure is data:** if P_load stays ≪ 0.5 W, log pair Δf (from 001), contact method, transformer turns, and waveforms — that is the input to the next ADR, not a reason to silently edit the simulator.
