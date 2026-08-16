# Prior art: what we build on

> English (primary) · [Русский](../translations/ru/docs/01-prior-art.md) · [Deutsch](../translations/de/docs/01-prior-art.md) · [Português](../translations/pt/docs/01-prior-art.md) · [Español](../translations/es/docs/01-prior-art.md) · [Français](../translations/fr/docs/01-prior-art.md) · [Italiano](../translations/it/docs/01-prior-art.md) · [Polski](../translations/pl/docs/01-prior-art.md) · [Türkçe](../translations/tr/docs/01-prior-art.md) · [Українська](../translations/uk/docs/01-prior-art.md) · [Tiếng Việt](../translations/vi/docs/01-prior-art.md) · [中文](../translations/zh/docs/01-prior-art.md) · [日本語](../translations/ja/docs/01-prior-art.md) · [한국어](../translations/ko/docs/01-prior-art.md) · [हिन्दी](../translations/hi/docs/01-prior-art.md)

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

## What we don't copy while it's alive
The old core of this list is US-only and runs out around 2032–2033, and stages 1–4 need none of it: OFDM with subcarriers placed to dodge the power channel's harmonics (RPI US9054826); full-duplex "AM downlink + load-modulation uplink + frequency tracking" as a single scheme (RPI US9455791); conformal transducers for curved surfaces per the Drexel approach (US10594409). The families below are neither: one reads on the bare power channel of stage 2, and one runs in Europe to 2039.

**Added by the 2026-08 search (statuses are Google Patents flags — re-check in USPTO Patent Center / the EP Register before any commercial use):**
- **US8594572B1** (US Navy, priority 2011-06, 12-year fee paid 2025, runs to 2032-01, US-only) — claim 1 is "wall + power source + transducer converting current to ultrasound through the wall + transducer converting back + powered electronic device", with no frequency, material or thickness limitation: it reads literally on the bare power channel in the US. Welle's US5982297 (1997) discloses the same arrangement, so the expired layer is also the invalidity defence; still, a US commercial fork should get FTO advice.
- **EP3723304B1** (ABB, priority 2019-04, granted 2023-08, maintained in **DE and GB only** — CH lapsed 2024-04, no other validation found in the register data read; to 2039-04; no US member) — an "acoustic wave conductor" (the vessel wall in the description) carrying power *and* data return to a sensor platform, **where the power-carrying spectrum is lower than the data spectrum**. That limitation was imported from a dependent claim during prosecution to get the grant, which is our design-around: the planned uplink is load modulation on the *same* 40 kHz carrier ([docs/03](03-discovery-protocol.md)) — sidebands around the power carrier, not a higher band (a claim reading, not an FTO opinion). Do not add a separate higher-frequency data carrier (ABB's own example: 200–300 kHz data over low-frequency power) to a mode-A power link in a product for DE/GB.
- **Ultrapower family** (priority 2014-03, to 2035-03): US10295500B2 — sensor inside a metallic *pipe*, transceiver outside, **convex/concave** transducer arrays; US10684260B2 / US10948457B2 — a metal rod *through* the wall. We use flat spot-faced pads and no rod.
- **US9602221B2** (Zackat Inc.; security-interest/assignment events name Anelto Inc. / Instant Care Inc.; priority 2014-03, reinstated 2021, fee paid 2024, to 2035-10, US) — claim 1: an ultrasonic transmitter on a "Class 1 device" inside an explosive-risk zone, receiver outside, alert to a remote operator; **independent claim 14 drops the Class-1-device limitation** (any sensor inside an explosive-risk zone + ultrasonic link + alert). Relevant only if a node ever raises alerts out of a hazardous area — a reason to keep any such application at bench scale in the US.
- Tangential, noted: GE US9146266B2 (telemetry through power-generation structures, to 2033), UNT US11415555 (passive SAW/BAW through-wall), CEA EP4080791B1 (impedance-scan frequency optimisation), RPI US9331879B2 (MIMO), US9505031B2 (spring-loaded housing). RPI US9455791B2 claim 1 does contain MOSFET load modulation of the inner transducer — but only bundled with a differential-AM downlink, Barker-sequence-synchronised sampling and the frequency step/track algorithm; [docs/03](03-discovery-protocol.md) deliberately has none of the AM/Barker downlink, and that whole combination must not be implemented while the patent lives.
- Free, additionally confirmed: Progeny/General Dynamics US20120127833A1 (separate power/data frequencies — **abandoned**), RPI/DOE US20100027379A1 (load-modulation uplink — abandoned).
