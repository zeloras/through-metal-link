# QUICKSTART: von absolutem Nullpunkt zum Testrigg der Stufe 1–2

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · Deutsch · [Português](../pt/QUICKSTART.md) · [中文](../zh/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md)

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

Diese PNGs sind **Modellerwartungen**, nicht Labormessungen. Kontaktverhältnisse, beladene Q≈40 und Ketteneffizienz ≤40% sind explizite Annahmen in `channel_sim.py` — ersetzen Sie sie durch Sweep/Leistungsdaten, sobald das Rigg existiert.

* `sim0-rig-sketch.png` — das gesamte Rigg in einer Skizze (Stufe-2-Kette; Stufe 1 omittiert die Halbbrücke und treibt den TX vom schwachen DDS-Sinus aus).
* `sim1-sweep-contacts.png` — erwartete Sweep-Form: ein schmaler Peak bei ~40 kHz; das Modell verwendet Schmiermittel:trocken:Luftlücke ≈ 1 : 0,25 : 0,02 als Platzhalter. Kein Peak — debuggen Sie den Kontakt oder die Paarungsmismatch zuerst (sim2).
* `sim2-pair-mismatch.png` — warum 4 Langevin-Wandler und nicht 2: mit Q≈40 reduziert eine Resonanzmismatch von 1,5 kHz innerhalb eines Paares die Modellleistung um ~10×; der Sweep wählt das beste Paar aus 4 aus.
* `sim3-thickness-comb.png` — für später (Modus B, MHz): die Platte ist transparent als Kamm von Dickenresonanzen, so dass die Frequenz verfolgt werden muss.
* `sim4-power-budget.png` — Lastaufnahme versus **Ziel**-Empfangsleistungsbänder. Modus-A-Band (0,5–5 W) ist das Stufe-2-Ambitionsziel, wenn Matching und Kontakt zusammenarbeiten; Modus B ist das untere Band. Kontinuierliches Wi-Fi ist ein Spitzenlasten-Marker, nicht ein Versprechen — duty-cycelte ESP32/BLE/LED sind die realistischen ersten Verbraucher.
* `sim5-ook-datarate.png` — Stufe 3: warum OOK auf Langevin-Wandlern bei ~1–2 kbit/s unter Q≈40 (Resonator-Ringdown τ≈0,3 ms) tops out und warum das für einen Sensor-Knoten in Ordnung ist.

## Kriterien für "das Rigg funktioniert"

Teilen Sie es nach Stufen auf — markieren Sie Stufe 1 nicht als abgeschlossen, wenn Sie Stufe-2-Zahlen haben.

**Stufe 1 — Sweep-Map** ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)):
1. Sweep 25–45 kHz in zwei aufeinanderfolgenden Läufen: der Peak-Zentrum reproduziert sich innerhalb von <200 Hz.
2. Optionaler Bonus: Schmiermittel+Spanner vs. trockener Pressfit auf demselben Paar (relative Amplituden, nicht absolute Watt).

**Stufe 2 — erste Watt** ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)):
1. Halbbrücke + Matching-Transformator online; Netzgerät-Strombegrenzung bei der Inbetriebnahme gemäß [docs/02-safety.md](docs/02-safety.md) und [hardware/driver/](hardware/driver/README.md).
2. Bei der Stufe-1-Resonanz ≥0,5 W in eine bekannte resistive Last durch 3 mm Stahl (messen Sie V und I auf der DC-Seite nach der RX-Brücke).
3. Die LED hinter der Platte leuchtet von der geharvesteten Leistung; Foto + CSV in experiments/002.

Sicherheit vor dem ersten Einschalten: [docs/02-safety.md](docs/02-safety.md) (TVS auf dem Empfänger, Netzgerät-Strombegrenzung bei 0,2 A für die Inbetriebnahme, nie einen Langevin-Wandler ohne Klemmdruck antreiben).
