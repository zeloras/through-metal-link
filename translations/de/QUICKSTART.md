# QUICKSTART: von absolutem Nullpunkt zum Testrigg der Stufe 1–2

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · Deutsch

Szenario: Sie haben nichts als einen Schreibtisch und etwas Geld. Alles unten bringt Sie zu einem funktionierenden Rigg — "Sweep-Map + erste Watt durch Stahl". Preise sind Schätzungen, USD.

## Korb 1 — Werkzeuge (eine Basis für Jahre, ~120 $)

| Artikel | Warum | Preis | Wo |
|---|---|---|---|
| Lötestation (T12-Klon) | alles | 35–50 | Ali |
| Multimeter (AN8008/UT61-Klasse) | Spannungen, Kontinuität, Kapazität | 15–25 | Ali |
| Labor-Netzgerät 30V/5A mit Strombegrenzung | versorgt den Treiber; die Strombegrenzung ist Ihre Versicherung gegen verbrannte MOSFETs | 45–60 | Ali/lokale |
| Helferhände, Lötzinn, Flux, Entlöten, Seitenschneider, Pinzette | die kleinen Dinge, die Sie nicht entbehren können | 15 | Ali/lokale |
| Dupont-Drähte + Breadboard + Schrumpfschlauch | Prototyping | 8 | Ali |

## Korb 2 — Rigg-Elektronik (~70 $)

| Artikel | Menge | Preis | Hinweis |
|---|---|---|---|
| Raspberry Pi (Zero 2 W ist ausreichend; 4/5 ist komfortabler) + SD | 1 | 20–60 | das Gehirn: Sweep, Logs, Plots |
| Langevin-Wandler 40 kHz 50–60 W | **4** | 40 | kaufen Sie 4 aus EINER Charge; wir wählen das beste Paar durch Sweep |
| AD9833-DDS-Modul | 2 | 8 | das zweite ist ein Ersatz |
| IR2110 + IRF540 ×4 (oder ein EGS002-Modul) | 1 Satz | 10 | Treiber-Halbbrücke |
| ADS1115-ADC | 2 | 4 | der Pi hat keinen eigenen ADC |
| Ferrit-Toroid + 0,5 mm Magnetdraht | 2 | 4 | Matching-Transformator |
| Schottky-Brücke (SS14 ×8), Supercap 1F 5,5V ×2 | 1 | 4 | Empfänger-Kette |
| TVS SMBJ5,0A ×3 + SMBJ15CA ×2 | 1 | 2 | Schutz. SPAREN SIE NICHT |
| GY-LTC3588-Modul | 1 | 7 | Harvester (Stufe 4, aber lassen Sie es jetzt versenden) |
| Widerstands/Kondensator-Sortiment, LEDs | 1 | 8 | wenn Sie überhaupt nichts haben |
| Unterstützende Passivbauelemente: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | Pfennige; vollständige Liste — BOM-Positionen 11–12 |

## Korb 3 — Mechanik (~20 $, lokal)

Stahlplatte 3 mm ~150×150 — 2 Stück (Metallhof / Laser-Schneiden); F-Style-Spanner ×2; dicke, konsistente Schmiermittel-Kupplung (Lithium-Schmiermittel); Epoxid; Schleifpapier (um die Kontaktfläche zu reinigen).

## Optional, aber stark empfohlen (~90 $)

| Artikel | Warum | Preis |
|---|---|---|
| USB/Handheld-Oszilloskop (FNIRSI/Hantek, 2 Kanäle; Sie benötigen keine ≥40 MHz Bandbreite — 10 ist ausreichend) | sehen Sie die Wellenform auf dem Gate und auf dem Piezo; spart Tage der Treiber-Debugging | 60–80 |
| ESP32 DevKit ×2 | Stufe 4 (der Knoten hinter der Wand) | 8 |

**Gesamt: Minimalausstattung ~210 $, komfortabel ~300 $.** (Wenn Sie bereits einen Pi, eine Lötestation und ein Labor-Netzgerät in Ihrem Vorrat haben — subtrahieren Sie ~120 $.)

## Bestellvorgang (der kritische Pfad ist der Versand)

1. Heute: Korb 2 von Ali (3–4 Wochen Versand — das ist der kritische Pfad) + das Oszilloskop.
2. Diese Woche: Körbe 1 und 3 lokal.
3. Während des Versands: `raspi-config` → SPI+I2C, führen Sie `software/sweep-map/sweep_map.py --mock` ohne Hardware aus (synthetischer Kanal — die gesamte CSV+Plot-Pipeline funktioniert auf jedem Computer), lesen Sie docs/00–03, sehen Sie sich die Erwartungsplots in docs/img und die Schaltpläne in hardware/schematics an (der Aufbau der Stufe 1 folgt sch3 und sch2).

## Was Sie sehen werden (Simulator: software/simulator/channel_sim.py → docs/img)

- `sim0-rig-sketch.png` — das gesamte Rigg in einer Skizze.
- `sim1-sweep-contacts.png` — Sweep-Frequenzgang: ein schmaler Peak bei ~40 kHz; Schmiermittel + Spanner gibt ~4× mehr als ein trockener Pressfit und ~50× mehr als eine Luftlücke. Kein Peak — das Problem ist der Kontakt oder das Paar, siehe sim2.
- `sim2-pair-mismatch.png` — warum 4 Langevin-Wandler und nicht 2: eine Resonanzmismatch von 1,5 kHz innerhalb eines Paares reduziert die Leistung um 10×; der Sweep wählt das beste Paar aus 4 aus.
- `sim3-thickness-comb.png` — für später (Modus B, MHz): die Platte ist transparent als Kamm von Dickenresonanzen, so dass die Frequenz verfolgt werden muss.
- `sim4-power-budget.png` — Zielwatt versus Lasten: Modus A speist alles bis zu Wi-Fi-Spitzen, Modus B speist einen ESP32 mit einem Supercap-Puffer.
- `sim5-ook-datarate.png` — Stufe 3: warum OOK auf Langevin-Wandlern bei ~1–2 kbit/s tops out (Resonator-Ringdown τ≈0,3 ms), und warum das für einen Sensor-Knoten in Ordnung ist.

## Kriterien für "das Rigg funktioniert"

1. Sweep 25–45 kHz in zwei aufeinanderfolgenden Läufen: der Peak reproduziert sich innerhalb von <200 Hz.
2. Bei Resonanz ≥0,5 W in eine resistive Last durch 3 mm Stahl.
3. Die LED hinter der Platte leuchtet. Foto in experiments/001 — und die Stufe ist abgeschlossen.

Sicherheit vor dem ersten Einschalten: docs/02-safety.md (TVS auf dem Empfänger, Netzgerät-Strombegrenzung bei 0,2 A, nie einen Langevin-Wandler ohne Klemmdruck antreiben).
