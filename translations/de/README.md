# durch-metall-verbindung

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · Deutsch · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Eine offene Plattform für ultraschallbasierte Energie- und Datenübertragung durch massive Metallwände — „durch Stahl ohne ein einziges Loch", gebaut mit Garage-Mitteln.

**Jetzt ausprobieren (keine Hardware nötig):** `python3 software/sweep-map/sweep_map.py --mock`

**Einstiege:**
- **A — Trockenübung:** Mock-Sweep + [Simulator](../../software/simulator/channel_sim.py) (ohne Laboraufbau)
- **B — Build-Phase 1:** [QUICKSTART.md](QUICKSTART.md) → [experiments/001](experiments/001-sweep-map-3mm-steel/README.md)
- **C — ohne Hardware beitragen:** Stand der Technik / Doku / Übersetzungen / ADR-Kommentare ([CONTRIBUTING.md](CONTRIBUTING.md))

**Status:** Phase 0 — Vorbereitung · **noch keine Hardware-Validierung** (nur Simulator; Bounty für den ersten Build) · 💰 **[$250 Bounty](https://github.com/zeloras/through-metal-link/issues/5)** · Einkaufsliste: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Die Dokumentation ist mehrsprachig: Englisch ist primär und liegt unter den kanonischen Pfaden; jede andere Sprache spiegelt den Baum unter [translations/](..). Beliebige Sprache bearbeiten — CI übersetzt und committet den Rest (siehe [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Phase-1-Aufbau: Pi → DDS → Halbbrücke → Transformator → Piezo TX | Stahl | Piezo RX → Brücke → ADC → Pi" width="900"></p>

## Die Idee in einem Absatz

Radiowellen dringen nicht durch Metall (Faraday-Käfig), und eine Kabeldurchführung bedeutet ein Loch, eine Dichtung und eine Schwachstelle. Ultraschall hingegen wandert problemlos durch Metall: Ein Piezo-Element auf jeder Seite der Wand verwandelt sie in einen Kanal für Strom und Daten. Die Labliteratur hat die Physik bereits auf ernsthafte Niveaus bewiesen (RPI: 50 W + 12 Mbit/s durch 63,5 mm Stahl; NASA JPL: bis zu ~kW durch 5 mm Titan) — das sind Existenznachweise mit Spezialhardware, nicht die Garage-BOM dieses Repos. Die grundlegenden Patente sind abgelaufen, und es existiert bislang keine offene, reproduzierbare Plattform — dieses Repository baut eine, beginnend bei **Watt-Klasse Leistung und kbit/s Daten durch 3–5 mm Stahl**, sobald Stage 2 vermessen ist.

## Roadmap

| Phase | Lieferobjekt | Erfolgskriterium | Erwartung |
|---|---|---|---|
| 1. Sweep-Map | Frequenzgang des „Langevin–3 mm Stahl–Langevin"-Kanals | Paar-Resonanz gefunden, Plot in [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. Watt | Leistung in die Last bei Resonanz | ≥0.5 W durch 3 mm Stahl, Protokoll in [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. Daten | FSK/OOK über dasselbe Paar | ≥1 kbit/s fehlerfrei | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. Knoten | ESP32 + Sensor in einer verschweißten Box, allein per Schall mit Strom versorgt und telemetriert | ≥1 h autonomer Betrieb | [sim4](docs/img/sim4-power-budget.png) |
| 5. Publikation | erste unabhängige Replikation + Artikel/How-to + Zenodo-Snapshot | Reproduktion durch Dritte dokumentiert | — |

## Repository-Übersicht

python3 software/sweep-map/sweep_map.py --mock
```

**Fertig, wenn (nach Stufe):** Stufe 1 — die Sweep-Spitze reproduziert sich über zwei Durchläufe auf unter <200 Hz ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)); Stufe 2 — ≥0,5 W in eine bekannte Last durch 3 mm Stahl und eine LED leuchtet auf der RX-Seite ([experiments/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Theorie in einer Minute</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

Der piezo TX wird gegen die Wand gepresst und treibt eine Longitudinalwelle in sie; der piezo RX auf der anderen Seite wandelt sie zurück in Strom. Schallgeschwindigkeit in Stahl: ~5900 m/s.

Zwei Betriebsmodi:

| Modus | Frequenz | Resonanz bestimmt durch | Liefert | Status |
|---|---|---|---|---|
| **A** — Langevin-Wandler | 40 kHz | das Wandlerpaar (Wand ≪ λ — eine „Membran") | Watt, kbit/s | Startmodus (Stufen 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — Scheiben | 0,6–1 MHz | Dickenresonanz der Wand ([Kamm](docs/img/sim3-thickness-comb.png)) | Hunderte mW, Hunderte kbit/s | Verzweigung nach den ersten Watt; erfordert automatische Frequenznachführung |

Die Hauptverluste: Resonanzfehlanpassung innerhalb des Paars (±1 kHz bei günstigen Langevin-Wandlern), Qualität des akustischen Kontakts (Epoxid > Kopplungsfett + Klemme > trockener Druck), Fehlausrichtung, Resonanzdrift mit der Temperatur. Die Antwort auf all diese ist dieselbe: **eine Sweep-Map vor jeder Änderung am Aufbau**.

</details>

<details>
<summary><b>📈 Was der Aufbau zeigen sollte: Erwartungsplots aus dem Simulator</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Ein semi-empirisches Kanalmodell (kein FEM, **keine Labordaten** — Intuition für „wie der Sweep aussehen sollte und worauf man zielen muss"). Annahmen sind in `channel_sim.py` explizit angegeben (geladenes Q≈40, Kontakt-k-Faktoren, Kettenwirkungsgrad η≤40%). Regenerieren mit: `python3 channel_sim.py --out ../../docs/img`.

**Stufe 1 — Sweep.** Eine schmale Spitze nahe ~40 kHz; die Platzhalter-Kontaktmultiplikatoren des Modells sind Fett:trocken:Spalt = 1 : 0,25 : 0,02 (d. h. Fett ≈4× trocken und ≈50× Luftspalt). Keine Spitze bedeutet ein Problem mit dem Kontakt oder dem Paar:

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Warum 4 Langevin-Wandler, nicht 2.** Bei Q≈40 senkt eine Resonanzfehlanpassung von 1,5 kHz innerhalb des Paars die modellierte Leistung um ~10×:

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**Stufe 3 — Daten.** OOK stößt an das Nachschwingen des Resonators (Modell-Q ~40 → τ≈0,3 ms): 1 kbit/s ist sauber, bei 5 kbit/s ist das Auge geschlossen. Schneller zu werden erfordert Modus B:

<img src="docs/img/sim5-ook-datarate.png" width="720">

**Empfänger-Leistungsbudget.** Schattierte Bänder sind **Ziele** (Modus A 0,5–5 W, wenn Stufe 2 erreicht wird; Modus B niedriger). Realistische erste Lasten sind getaktete ESP32 / BLE / LED; WLAN ist als Marker für Spitzenstromaufnahme gezeigt, nicht als kontinuierliche Zusage:

<img src="docs/img/sim4-power-budget.png" width="720">

**Für später (Modus B).** Die Platte wird bei einem Kamm von Dickenresonanzen transparent — die Frequenz muss nachgeführt werden:

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Sicherheit — vor dem ersten Einschalten lesen</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Zehn bis Hunderte Volt am Piezo**, sobald der Treiber der Stufe 2 aktiv ist — die TVS auf der Empfangsseite wird VOR dem ersten bestromten Durchlauf eingebaut; Hände von den Anschlüssen fernhalten.
2. **Netzspannung** — nur über ein Labornetzteil / Trenntrafo; Treiberplatinen von Ultraschallreinigern sind galvanisch mit dem Netz verbunden.
3. **Ohren** — bei nicht-trivialer Leistung Wandler gegen Metall gepresst betreiben; niemals Hochleistungs-Luftultraschall ohne Gehäuse betreiben.
4. **Hitze** — ein ungeklemmter Langevin-Wandler überhitzt bei Leistung in Minuten; klemmen, bevor der Strom erhöht wird (nur kurze elektrische Inbetriebnahme mit niedrigem Strom — siehe Treiber-README).
5. **Splitter** — Piezokeramik ist spröde: eine überzogene Schraube oder ein Schlag bedeutet Splitter; bei jeder mechanischen Arbeit Schutzbrille tragen.

</details>

docs/            Theorie, Stand der Technik, Sicherheit, Anwendungen, Entscheidungslog (ADR)
docs/img/        Erwartungs-Plots (generiert von software/simulator/channel_sim.py)
hardware/        BOM, Treiber (Halbbrücke), Empfänger (Gleichrichter/Harvester)
firmware/        Knoten-Firmware (ESP32 — Stub bis Stufe 4)
software/        Mess-Skripte (Frequenzgang-Sweep-Map) und Kanal-Simulator
experiments/     Experiment-Protokolle — aus der Vorlage, ein Verzeichnis = ein Experiment
data/            Roh-Logs (große Dateien bleiben aus git heraus)
```

</details>

## Prinzipien

1. **Reproduzierbarkeit von null an.** Jeder mit einem Lötkolben und ~210 $ kann das Ergebnis allein aus diesem Repo nachbauen.
2. **Jedes Experiment ist ein Protokoll.** Kein "hat irgendwie funktioniert": [experiments/TEMPLATE.md](experiments/TEMPLATE.md) ist Pflicht.
3. **Patent-Hygiene.** Wir bauen auf der abgelaufenen Schicht auf ([docs/01-prior-art.md](docs/01-prior-art.md)); Entscheidungen werden in [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md) festgehalten.
4. **Messung zuerst, Meinung danach.** Eine Sweep-Mappe, bevor irgendwelche Schlussfolgerungen über den Kanal gezogen werden.

## Lizenzen und Patente

Code — Apache-2.0, Hardware — CERN-OHL-W v2, Dokumentation — CC-BY-4.0; vollständige Texte unter [LICENSES/](../../LICENSES). Jeder darf forken und darauf aufbauen, auch kommerziell; Patentschutz ergibt sich aus den Gewährungs- und Vergeltungsklauseln in den Lizenzen plus einer Stand-der-Technik-Strategie. Das vollständige Konzept und das Protokoll für defensive Veröffentlichungen: [LICENSES.md](LICENSES.md); Beitragsregeln: [CONTRIBUTING.md](CONTRIBUTING.md).
