# Hybrid channels: barrier → physics → numbers

> English (primary) · [Русский](../translations/ru/docs/04-hybrid-channels.md) · [Deutsch](../translations/de/docs/04-hybrid-channels.md) · [Português](../translations/pt/docs/04-hybrid-channels.md)

The principle (a corollary of the "penetration paradox"): a wave gets through a barrier exactly to the extent that it interacts weakly with it — which is why no universal channel exists. The platform doesn't chase a single channel; for each barrier it picks the physics that the barrier is transparent to and the receiver is resonantly "greedy" for.

## Channel selection table

| Barrier | Working channel | Expected (orders of magnitude) | Notes |
|---|---|---|---|
| Steel/aluminum 1–60 mm, contact possible | Piezo-acoustics (our primary) | watts; kbit/s (up to Mbit/s in MHz mode) | needs acoustic contact (grease couplant/epoxy) |
| Metal: dirty, painted, hot, contact undesirable | EMAT (magnetics → sound in the wall) | mW; kbit/s; gap up to ~3 mm | conductive walls only; data, not power |
| Ferromagnetic wall with no piezo at all | Magnetostriction (a coil drives the steel itself) | crumbs; bit/s–kbit/s | experimental branch, cheap to test |
| Double wall with vacuum (thermos, cryostat, dewar) | LF magnetics (tens–hundreds of Hz) | µW–mW; bit/s | skin effect: in steel δ≈0.6 mm @1 kHz — push the frequency down |
| Non-metal: glass, plastic, ceramics | Piezo-acoustics (easier than metal) | watts; kbit/s | + plain RF often gets through too — check that first |
| Wall with a rubber/foam layer, composite | Honestly: nearly a dead end | — | the absorber eats everything; the workaround is a spot with no coating |
| Liquid behind the wall (full tank) | Piezo-acoustics, degraded | power −a few dB; shorter ringing | liquid loading shifts/damps the resonance — re-sweep against the full vessel; keep continuous intensity ≲1 W/cm² to stay under cavitation ([theory](00-theory.md#effect-on-the-wall-and-the-media-behind-it)) |
| Bubbling liquid in the acoustic path | Architectural workaround | — | mount the receiver on the wall, keep the liquid out of the path |

## Hybrid node architecture

- Power layer: piezo pair at resonance (stages 1–4).
- Contactless data layer: an EMAT head as a detachable "scanner gun" (stage ~6).
- Fallback layer: LF coils for vacuum sandwiches (when the task calls for it).
- The discovery protocol (docs/03) extends from "sweep over frequency" to "sweep over physics": ping piezo → ping EMAT → ping LF; the node picks the channel that gets through on its own and reports which barrier it sees.

## Example applications by channel

1. **Sealed battery packs (EV/storage):** T/gas sensor inside a potted enclosure; power+data via a piezo pair through 2–3 mm aluminum. The market is booming, and a penetration into a battery enclosure = certification hell.
2. **Cryostat/dewar:** a temperature logger inside, sending a bit-packet once a minute via LF magnetics through the vacuum jacket. Fundamentally out of reach for acoustics — this is where the hybrid is irreplaceable.
3. **Pipeline/autoclave under pressure:** an EMAT scanner pressed against a hot painted pipe with zero surface prep — reads a passive resonant beacon from the inside.
4. **Fermentation tanks (beer/wine, stainless steel):** a density/T sensor inside the tank without a single penetration — sanitary codes love the absence of holes.
5. **Sea container/safe:** "is the cargo alive" — a piezo pair through corrugated steel, polled with a handheld scanner.

## Limitations no layer can solve
Power — contact piezo only (EMAT and LF magnetics are orders of magnitude weaker). Composite/rubber-lined walls are outside the platform. LF channel speed is bits per second — that's telemetry, not streaming.
