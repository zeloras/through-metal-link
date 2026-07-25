# Prior art: what we build on

> English (primary) · [Русский](../translations/ru/docs/01-prior-art.md) · [Deutsch](../translations/de/docs/01-prior-art.md) · [Português](../translations/pt/docs/01-prior-art.md)

## The rule
Every technical decision in this repo must be traceable to a source from the "free" list (expired patents, papers). Live patents are read-only — mine them for insight into the problems, never copy their claims (this matters for commercialization in the US; see the patent map in the project).

## The free foundation (expired/abandoned patents = public domain)
- **US5982297** (Aerospace Corp, 1997) — the basic recipe: a piezo pair through the wall, power + bidirectional data. The main cookbook.
- US5594705 (Dynamotive, 1994) — an "acoustic transformer" through the hull.
- US6037704, US6127942 (Aerospace Corp) — powering sensors, reading data back out.
- **US7902943** (Caltech/JPL, lapsed over unpaid maintenance fees in 2019) — the Sherrit feed-through: reflector, acoustic transformer.
- US9748870 (Caltech/JPL) — mechanical work through the wall.
- **US9361877** (Univ. Oklahoma, lapsed over unpaid maintenance fees) — a modern complete transceiver system.
- US20100027379 / WO2008105947 (DOE+RPI, abandoned) — a carrier from the outside + load modulation from the inside.

## Key papers
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, 63.5 mm steel.
- Sherrit et al., NASA NTRS 20080048150 — a 100 W lamp powered through a wall.
- Yang et al., Sensors 2015 (10.3390/s151229870) — review, the best summary of the numbers.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — metamaterial, 2%→66% through 1 mm stainless (no patent found as of 07.2026).

These papers are the **physics and patent-hygiene baseline**. Their power/bitrate numbers used lab transducers, bonding, and matching — not the AliExpress Langevin + grease BOM in [QUICKSTART.md](../QUICKSTART.md). Cite them as existence proofs; the project's own pass bars live in [experiments/](../experiments/).

## What we don't copy while it's alive (US-only, until ~2032; stages 1–4 don't need it anyway)
OFDM with subcarriers placed to dodge the power channel's harmonics (RPI US9054826); full-duplex "AM downlink + load-modulation uplink + frequency tracking" as a single scheme (RPI US9455791); conformal transducers for curved surfaces per the Drexel approach (US10594409).
