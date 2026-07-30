# Receiver discovery and auto-tuning protocol (sketch; implementation in stages 2–4)

> English (primary) · [Русский](../translations/ru/docs/03-discovery-protocol.md) · [Deutsch](../translations/de/docs/03-discovery-protocol.md) · [Português](../translations/pt/docs/03-discovery-protocol.md) · [中文](../translations/zh/docs/03-discovery-protocol.md) · [日本語](../translations/ja/docs/03-discovery-protocol.md)

The goal: the device figures out on its own whether there is a receiver behind the wall, picks the frequency and power on its own, and doesn't roast the wall for nothing if someone "forgot to weld the receiver in".

The role model is Qi chargers: they solve exactly this problem (is there a phone on the coil?) with exactly this sequence. Our acoustic analog:

## Phase 0 — analog ping (the receiver may be fully discharged)
The TX runs a low-power sweep across the band and measures **its own current and phase** (shunt + peak detector → ADS1115). A resonant receiver behind the wall is a load coupled to the TX through the wall: its presence shows up as a characteristic dip/bump on the TX impedance curve, even if everything inside is unpowered. Same principle as a metal detector and Qi's analog ping.
- Signature present → phase 1. No signature → "no receiver found", stay in standby ping (once every N seconds), don't raise the power.
- Bonus: the impedance curve of the "empty" wall is recorded at installation time as a reference — so we can tell "no receiver" apart from "receiver came loose / got misaligned".

## Phase 1 — digital handshake
The TX parks on the candidate frequency (the phase-0 peak) and delivers power. The RX harvester charges the supercapacitor, the MCU wakes up and replies with **load modulation**: a MOSFET periodically shorts its piezo following a code (ID + protocol version). The TX sees this as modulation of its own current. No transmitter is needed inside at all — this is an RFID scheme, the same one as in the abandoned DOE/RPI application US20100027379 (free prior art).

## Phase 2 — frequency servo tuning (perturb & observe)
The RX can report its bus voltage (telemetry over load modulation). The TX steps ±Δf and holds the maximum of received power — a classic MPPT loop. This closes the resonance drift with temperature (the niche's main gotcha: a ~6% shift = ~10× efficiency drop).

## Phase 3 — power negotiation and watchdog
The RX requests a level (alive / charging / give me more), the TX caps the power at what was requested. Replies missing for M cycles → the TX falls back to phase 0 at low power.

## Hardware this requires (BOM item 12, schematic — hardware/schematics/sch4)
- TX: 0.1 Ω shunt + rectifier/peak detector on the second ADS1115 channel (current), optionally a phase comparator.
- RX: 2N7002 + ~100 Ω on the **DC side** of the rectifier (the VIN pin of the LTC3588 module) + GPIO — the load is switched after the bridge, and the TX sees it as modulation of its own current. A single MOSFET across the AC piezo does not work (the body diode shunts one half-wave, the gate has no reference on a floating node); the across-the-piezo variant only works with a pair of back-to-back series MOSFETs.

## Limits
The analog ping weakens as wall thickness and contact losses grow (the signature drowns in the noise) — the detection threshold must be measured in a dedicated experiment (experiments/). For thick walls, the fallback: the RX, once it has stored up charge, periodically "knocks" with a beacon of its own.
