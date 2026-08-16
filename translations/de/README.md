# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · Deutsch · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Eine offene Plattform für ultraschallbasierte Energie- und Datenübertragung durch massive Metallwände — „durch Stahl ohne ein einziges Loch", gebaut mit garagentauglichen Mitteln.

**Jetzt ausprobieren (keine Hardware nötig):** `python3 software/sweep-map/sweep_map.py --mock`

**Status:** Phase 0 — Vorbereitung · 💰 **[250 $ Kopfgeld für den ersten unabhängigen Nachbau](https://github.com/zeloras/through-metal-link/issues)** · Einkaufsliste: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Die Dokumentation ist mehrsprachig: Englisch ist die Hauptsprache und liegt unter den kanonischen Pfaden; jede andere Sprache spiegelt den Verzeichnisbaum unter [translations/](..). Jede Sprache kann bearbeitet werden — die CI übersetzt und committet den Rest (siehe [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Phase-1-Aufbau: Pi → DDS → Halbbrücke → Transformator → Piezo TX | Stahl | Piezo RX → Brücke → ADC → Pi" width="900"></p>

## Die Idee in einem Absatz

Radiowellen dringen nicht durch Metall (Faraday-Käfig), und eine Kabeldurchführung bedeutet ein Loch, eine Dichtung und eine potenzielle Fehlerquelle. Ultraschall hingegen breitet sich problemlos durch Metall aus: ein Piezo-Element auf jeder Seite der Wand verwandelt es in einen Kanal für Energie und Daten. Die Fachliteratur hat die Physik bereits auf beeindruckenden Niveaus bewiesen (RPI: 50 W + 12 Mbit/s durch 63,5 mm Stahl; NASA JPL: bis zu ~kW durch 5 mm Titan) — dies sind Existenznachweise mit spezieller Hardware, nicht die Garagen-BOM dieses Repos. Die grundlegenden Patente sind abgelaufen, und es existiert bisher keine offene, reproduzierbare Plattform — dieses Repository baut eine, beginnend mit **Leistung im Watt-Bereich und kbit/s Daten durch 3–5 mm Stahl**, sobald Stufe 2 vermessen ist.

## Roadmap

| Phase | Ergebnis | Erfolgskriterium | Erwartung |
|---|---|---|---|
| 1. Sweep-Map | Frequenzgang des „Langevin–3 mm Stahl–Langevin“-Kanals | Paarresonanz gefunden, Plot in [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. Watt | Leistung in die Last bei Resonanz | ≥0,5 W durch 3 mm Stahl, Protokoll in [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. Daten | FSK/OOK über dasselbe Paar | ≥1 kbit/s fehlerfrei | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. Knoten | ESP32 + Sensor in einer verschweißten Box, allein per Schall versorgt und telemetriert | ≥1 h autonomer Betrieb | [sim4](docs/img/sim4-power-budget.png) |
| 5. Veröffentlichung | Repo wird öffentlich, Artikel/How-to | Reproduktion durch Dritte | — |

## Repository-Übersicht

python3 software/sweep-map/sweep_map.py --mock
```

**Fertig, wenn (nach Phase):** Phase 1 — der Sweep-Peak reproduziert sich über zwei Durchläufe auf unter <200 Hz ([Experimente/001](experiments/001-sweep-map-3mm-steel/README.md)); Phase 2 — ≥0,5 W in eine bekannte Last durch 3 mm Stahl und eine LED, die von der RX-Seite aus leuchtet ([Experimente/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Theorie in einer Minute</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

Der Piezo-TX wird gegen die Wand gedrückt und treibt eine Longitudinalwelle in sie; der Piezo-RX auf der anderen Seite wandelt sie wieder in Strom um. Schallgeschwindigkeit in Stahl: ~5900 m/s.

Zwei Betriebsmodi:

| Modus | Frequenz | Resonanz bestimmt durch | Liefert | Status |
|---|---|---|---|---|
| **A** — Langevin-Wandler | 40 kHz | das Wandlerpaar (Wand ≪ λ — eine "Membran") | Watt, kbit/s | Startmodus (Phasen 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — Scheiben | 0.6–1 MHz | Dickenresonanz der Wand ([Kamm](docs/img/sim3-thickness-comb.png)) | Hunderte von mW, Hunderte von kbit/s | Verzweigung nach den ersten Watt; benötigt automatische Frequenzverfolgung |

Die Hauptverluste: Resonanzfehlanpassung innerhalb des Paares (±1 kHz bei billigen Langevin-Wandlern), Qualität des akustischen Kontakts (Epoxid > Fett-Kopplungsmittel + Klemme > trockener Druck), Fehlausrichtung, Resonanzdrift mit der Temperatur. Die Antwort auf all dies ist dieselbe: **eine Sweep-Map vor jeder Änderung am Aufbau**.

</details>

<details>
<summary><b>📈 Was der Aufbau zeigen sollte: Erwartungsdiagramme aus dem Simulator</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Ein semi-empirisches Kanalmodell (kein FEM, **keine Labordaten** — Intuition für "wie der Sweep aussehen sollte und worauf man abzielen muss"). Annahmen sind in `channel_sim.py` explizit angegeben (belasteter Q≈40, Kontakt-k-Faktoren, Kettenwirkungsgrad η≤40%). Neu generieren mit: `python3 channel_sim.py --out ../../docs/img`.

**Phase 1 — Sweep.** Ein schmaler Peak nahe ~40 kHz; die Platzhalter-Kontaktfaktoren des Modells sind Fett:trocken:Spalt = 1 : 0.25 : 0.02 (d.h. Fett ≈4× trocken und ≈50× Luftspalt). Kein Peak bedeutet ein Problem mit dem Kontakt oder dem Paar:

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Warum 4 Langevin-Wandler, nicht 2.** Bei Q≈40 senkt eine 1,5 kHz Resonanzfehlanpassung innerhalb des Paares die Modellleistung um ~10×:

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**Phase 3 — Daten.** OOK stößt auf das Nachschwingen des Resonators (Modell Q~40 → τ≈0,3 ms): 1 kbit/s ist sauber, bei 5 kbit/s ist das Auge geschlossen. Schneller geht es nur mit Modus B:

<img src="docs/img/sim5-ook-datarate.png" width="720">

**Leistungsbudget des Empfängers.** Schattierte Bänder sind **Ziele** (Modus A 0,5–5 W, wenn Phase 2 erfolgreich ist; Modus B niedriger). Realistische erste Lasten sind getaktete ESP32 / BLE / LED; WLAN wird als Marker für Spitzenstromaufnahme gezeigt, nicht als kontinuierliche Zusage:

<img src="docs/img/sim4-power-budget.png" width="720">

**Für später (Modus B).** Die Platte wird bei einem Kamm von Dickenresonanzen transparent — die Frequenz muss nachgeführt werden:

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Sicherheit — vor dem ersten Einschalten lesen</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Zehn bis Hunderte Volt am Piezo**, sobald der Treiber der Phase 2 online ist — die TVS-Diode auf der Empfangsseite wird VOR dem ersten unter Strom stehenden Lauf eingebaut; lass die Finger von den Anschlüssen.
2. **Netzstrom** — nur über ein Labornetzteil / Trenntrafo; Treiberplatinen von Ultraschallreinigern sind galvanisch mit dem Netz verbunden.
3. **Ohren** — bei nicht unerheblicher Leistung Wandler nur gegen Metall gedrückt betreiben; niemals leistungsstarken luftgetragenen Ultraschall ohne Gehäuse betreiben.
4. **Hitze** — ein ungeklemmter Langevin-Wandler überhitzt bei Leistung in Minuten; klemmen, bevor der Strom erhöht wird (nur kurze elektrische Inbetriebnahme mit niedrigem Strom — siehe Treiber-README).
5. **Splitter** — Piezokeramik ist spröde: eine überzogene Schraube oder ein Schlag bedeutet Splitter; trage bei mechanischen Arbeiten immer eine Schutzbrille.

</details>

docs/            Theorie, Stand der Technik, Sicherheit, Anwendungen, Entscheidungslog (ADR)
docs/img/        Erwartungsplots (generiert von software/simulator/channel_sim.py)
hardware/        BOM, Treiber (Halbbrücke), Empfänger (Gleichrichter/Harvester)
firmware/        Knoten-Firmware (ESP32 — Stub bis Stufe 4)
software/        Messskripte (Frequenzgang-Sweep-Map) und Kanal-Simulator
experiments/     Experiment-Protokolle — aus der Vorlage, ein Verzeichnis = ein Experiment
data/            Rohdaten (große Dateien bleiben aus git heraus)
```

</details>

## Prinzipien

1. **Reproduzierbarkeit von null an.** Jeder mit einem Lötkolben und ~$210 kann das Ergebnis allein aus diesem Repo nachbauen.
2. **Jedes Experiment ist ein Protokoll.** Kein „hat irgendwie funktioniert“: [experiments/TEMPLATE.md](experiments/TEMPLATE.md) ist verpflichtend.
3. **Patent-Hygiene.** Wir bauen auf der abgelaufenen Schicht auf ([docs/01-prior-art.md](docs/01-prior-art.md)); Entscheidungen werden in [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md) festgehalten.
4. **Messung zuerst, Meinung später.** Eine Sweep-Map, bevor irgendwelche Schlussfolgerungen über den Kanlo gezogen werden.

## Lizenzen und Patente

Code — Apache-2.0, Hardware — CERN-OHL-W v2, Dokumentation — CC-BY-4.0; vollständige Texte unter [LICENSES/](../../LICENSES). Jeder darf forken und darauf aufbauen, auch kommerziell; der Patentschutz ergibt sich aus den Grant- und Retaliation-Klauseln der Lizenzen plus einer Prior-Art-Strategie. Das vollständige Konzept und das Protokoll zur defensiven Veröffentlichung: [LICENSES.md](LICENSES.md); Beitragsregeln: [CONTRIBUTING.md](CONTRIBUTING.md).
