# Applications map: who needs this technology stack, and why

> English (primary) · [Русский](../translations/ru/docs/05-applications-map.md) · [Deutsch](../translations/de/docs/05-applications-map.md) · [Português](../translations/pt/docs/05-applications-map.md) · [Español](../translations/es/docs/05-applications-map.md) · [Français](../translations/fr/docs/05-applications-map.md) · [Italiano](../translations/it/docs/05-applications-map.md) · [Polski](../translations/pl/docs/05-applications-map.md) · [Türkçe](../translations/tr/docs/05-applications-map.md) · [Українська](../translations/uk/docs/05-applications-map.md) · [Tiếng Việt](../translations/vi/docs/05-applications-map.md) · [中文](../translations/zh/docs/05-applications-map.md) · [日本語](../translations/ja/docs/05-applications-map.md) · [한국어](../translations/ko/docs/05-applications-map.md) · [हिन्दी](../translations/hi/docs/05-applications-map.md)

The platform stack: an active power-and-data channel through blind walls — piezo-acoustics / EMAT / LF magnetics. Below: where this is needed in the real world, who is already there, and what's left for us.

## 1. Sealed battery packs (EV, home/industrial energy storage)
- Pain: early detection of thermal runaway — gases (CO₂, H₂, electrolyte vapors) appear inside the pack minutes to hours before a fire; a sensor penetration in the enclosure = loss of hermetic sealing and certification.
- Our stack: a gas/temperature node inside the pack, power and telemetry via a piezo pair through 2–3 mm aluminum. Zero holes.
- Who's already there: Liminal Insights — acoustic *diagnostics from the outside* (patents on analysis methods, not on the channel). Nobody sells nodes *inside* the pack.
- Niche maturity: the market is growing explosively, the shelf is empty. For the platform — showcase application #1.

## 2. Lab equipment: vacuum chambers, cryostats, glove boxes
- Pain: every electrical feedthrough into a vacuum chamber is a flange worth hundreds of dollars and a source of leaks; in a cryostat, a cable = heat leak.
- Our stack: a sensor inside the chamber, power/data by sound through the steel wall; for the vacuum sandwiches of dewars — LF magnetics (bit/s is plenty for a T-logger).
- Who's already there: nobody with wireless through-wall; labs live on feedthrough flanges.
- Maturity: the ideal starting niche for open source — labs are exactly the audience for open hardware (the TinyLev path): they buy without certifications and cite you in papers.

## 3. Food production: fermentation tanks, autoclaves (beer, wine, dairy)
- Pain: sanitary codes hate penetrations (CIP washing, dead zones); you want to know density/T/pressure inside the tank at all times.
- Our stack: a node on the inner wall of a stainless tank, polled from outside with a handheld scanner or a fixed pair.
- Who's already there: ordinary tapped-in sensors; no wireless through-wall solutions.
- Maturity: literally within reach of a garage test (any craft brewery is a proving ground within walking distance).
- Physics caveat: a full tank loads the wall — re-sweep against the full vessel, and keep continuous power ≲1 W/cm²; above that, cavitation in the product (CO₂ degassing, off-flavors, long-term wall erosion) — [theory](00-theory.md#effect-on-the-wall-and-the-media-behind-it).

## 4. Pipelines, pressure vessels, industrial NDT
- Pain: monitoring corrosion/parameters inside without a shutdown or a penetration; surfaces are hot, painted, dirty.
- Our stack: an EMAT "scanner gun" — press it against a pipe with zero surface prep, read a passive resonant beacon from the inside.
- Who's already there: clamp-on ultrasonic flow meters and thickness gauges (a mature market), but no interactive beacons inside.
- Maturity: mid-range; requires the EMAT branch (stage ~6).

## 5. Oil & gas / downhole, and nuclear
- Who's already there: Metrol, Acoustic Data, Baker Hughes (downhole, 30 years, service model); DOE/UNT/Westinghouse R&D (nuclear canisters).
- Honest verdict: occupied and heavily regulated — we don't go there, but their very existence = proof that this physics sells for serious money. Use as a reference in the README.

## 6. Marine logistics and underwater structures
- Pain: "is the cargo alive" in a sealed container; data from the inner side of a ship's hull.
- Who's already there: CSignum (LF EM through water/bulkheads) — the only direct neighbor in hybrid philosophy.
- Maturity: long-range; for us, for now, only a direction of thought.

## Priorities (what to do, in what order)
1. **Now:** platform stages 1–4 on the showcase scenario "lab chamber / welded-shut box" (niche #2 — the most open to open source).
2. **Next:** a demo on a live object from niche #3 (a brewery tank) — cheap, photogenic, a real user.
3. **Mid-range:** the battery scenario (niche #1) as the flagship case for publication; the EMAT branch for niche #4.

*Passive vision (muon radiography) has been spun off into a separate project — see muon-lab in the knowledge base.*
