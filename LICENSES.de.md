# Lizenzen und Patentschutz

> [English (primary)](LICENSES.md) · [Русский](LICENSES.ru.md) · Deutsch

Das Ziel dieses Schemas: Das Projekt ist vollständig offen, jeder kann es forken und darauf aufbauen (einschließlich kommerzieller Nutzung), während das Risiko von Patentstreitigkeiten auf das absolute Minimum reduziert wird, das durch rechtliche und prozedurale Mittel erreichbar ist.

## Das Schema (drei Schichten; vollständige Texte in [LICENSES/](LICENSES/))

| Bereich | Lizenz | Text | Patentschutzbestimmungen |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt) | §3: Jeder Beitragende gewährt automatisch eine Patentschutzlizenz für seinen Beitrag; eine Patentklage einreichen und man verliert die **Patentschutz**-Lizenz (Vergeltung; die Urheberrechtslizenz in §2 ist unwiderruflich und überlebt die Klage) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](LICENSES/CERN-OHL-W-2.0.txt) | §7.1: Eine Patentschutzlizenz (Herstellen / herstellen lassen / verwenden / verkaufen / importieren…) von jedem Lizenzgeber — aber nur für Ansprüche, die notwendigerweise durch die gegebenen Covered Source verletzt werden; §7.2: Eine Patentklage (einschließlich eines Versuchs, jemand anderes' Patent ungültig zu machen) beendet **alle** Rechte unter der Lizenz |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](LICENSES/CC-BY-4.0.txt) | gewährt **keine** Patentschutzrechte (§2(b)(2)) — die Lücke wird durch die explizite Patentschutzlizenz in [CONTRIBUTING.md](CONTRIBUTING.md) geschlossen |
| alles andere (root `README.md`, `QUICKSTART.md`, diese Datei, `data/` usw.) | CC-BY-4.0 | — | Fallback: Keine Datei im Repository ist "alle Rechte vorbehalten" |

Code-Dateien enthalten SPDX-Header (Apache-2.0); die maschinenlesbare Abdeckungskarte ist [REUSE.toml](REUSE.toml). Die Urheberrechtszeile befindet sich in [NOTICE](NOTICE); die root [LICENSE](LICENSE) ist ein Pointer zu diesem Schema.

**Warum CERN-OHL-W, nicht S oder P.** W ist der Mittelweg: Das Design und seine Modifikationen müssen bei jeder Verteilung offen bleiben, aber das Produkt, in das das Design integriert wird, kann kommerziell und proprietär sein — was die Nischen aus docs/05 (Labore, Brauereien, Batteriepacks) offen hält. S (starker Copyleft) würde die Tür für die Einbettung schließen; P (permissiv) würde geschlossene Forks zulassen. Eine Verschärfung in Richtung S ist in die Lizenz selbst eingebaut: §8.3 ermöglicht es jedem, W-lizenziertes Material als S-lizenziert zu behandeln (vorausgesetzt, die Bedingung der verfügbaren Komponenten ist erfüllt) — keine Genehmigung erforderlich. Eine Lockerung (in Richtung P oder einer anderen Lizenz) ist dagegen nur möglich, solange alle Materialien einem einzigen Autor gehören; nach dem ersten externen Beitrag — nur mit Zustimmung aller Beitragenden.

**Projektname.** "through-metal-link" ist kein eingetragenes Markenzeichen; die Lizenzen selbst gewähren keine Rechte am Namen (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Eine tatsächliche Bezugnahme auf das Projekt ("basierend auf through-metal-link") ist für jeden kostenlos; Forks mit inkompatiblen Änderungen werden gebeten, unter ihrem eigenen Namen zu verschiffen.

## Was dies schützt — und was nicht (ehrlich)

**Es schützt gegen:**
1. **Klagen von Beitragenden.** Jeder, der beigetragen hat, hat automatisch seine Patentschutzrechte für diesen Beitrag lizenziert (Apache §3, CERN-OHL §7.1 und CONTRIBUTING für Dokumente). Eine Klage kostet den Kläger teuer: unter Apache-2.0 verlieren sie die Patentschutzlizenzen für den Code; unter CERN-OHL-W verlieren sie alle Rechte an der Hardware-Schicht direkt (§7.2 — ausgelöst sogar durch einen Versuch, jemand anderes' Patent in Frage zu stellen).
2. **Privatisierung von Hardware-Forks.** CERN-OHL-W verpflichtet jeden, der verteilt (Übertragung eines Produkts oder von Quellen), seine Designmodifikationen zu veröffentlichen — Verbesserungen fließen zurück in die offene Schicht und werden selbst zu Prior Art. (Ein Fork in der Schublade, der nie an Dritte weitergegeben wird, hat keine Veröffentlichungspflicht — gleich wie unter jedem Copyleft.)
3. **Andere Menschen *zukünftige* Patente.** Alles, was mit einem Datum veröffentlicht wird, zerstört die Neuheit für spätere Anmeldungen: für eine Lösung, die hier vor ihrem Anmeldedatum beschrieben wird, kann kein gültiges Patent mehr erteilt werden. Gegen Anmeldungen, die *vor* unserer Veröffentlichung eingereicht wurden, funktioniert dies nicht — für diese ist der einzige Schild die Schicht der abgelaufenen Patente (siehe unten).

**Es schützt nicht gegen:**
- **Drittpatente, die bereits existieren.** Keine Lizenz kann das tun. Was gegen sie funktioniert, ist die ingenieurtechnische Disziplin von docs/01-prior-art.md: Bauen Sie nur aus der abgelaufenen Schicht (Public Domain), implementieren Sie keine live-Ansprüche (RPI OFDM/full-duplex, Drexel — bis ~2032, US-only) und verfolgen Sie jede Designentscheidung zurück zu einer freien Quelle. Das ist keine Garantie, aber es ist genau die Praxis, die eine Klage sinnlos macht.
- Ein Fork, der für die kommerzielle Produktion bestimmt ist, führt seine eigene FTO-Analyse (Freiheit zur Nutzung) für seine eigene Rechtsordnung und sein Design durch — das Repository macht keine Patentschutzangaben (Haftungsausschlüsse in allen drei Lizenzen).

## Defensiver Publikationsprotokoll (ausführen, wenn das Repository öffentlich wird)

Jedes veröffentlichte Ergebnis ist eine datierte Prior Art, die alle späteren Drittanwendungen für die gleiche Lösung blockiert:

1. Öffnen Sie das Repository mit seiner vollständigen Git-Historie (Commits = Timestamps).
2. Snapshot zu **Zenodo** → DOI: Ein unabhängiges Archiv mit einem rechtlich bedeutungsvollen Datum, das in Papieren zitiert werden kann.
3. Pin es in **Software Heritage** (archive.softwareheritage.org — ein ewiger Spiegel).
4. Jedes abgeschlossene Experiment `experiments/NNN` — mit einem Datum, Zahlen und Plots: Das ist die Veröffentlichung einer spezifischen technischen Lösung.
5. Wichtige Meilensteine (erste Watt, erster Knoten) — ein Write-up in der Welt (Hackaday.io / arXiv / Blog): Je weiter die Verbreitung, desto stärker der Prior-Art-Status.

## Für Beitragende

Die Regeln leben in [CONTRIBUTING.md](CONTRIBUTING.md): DCO-Sign-off, inbound=outbound, eine explizite Patentschutzlizenz für jeden Beitrag unabhängig vom Verzeichnis, Nachvollziehbarkeit von Designentscheidungen zu freier Prior Art.

Bis es öffnet, bleibt das Repository privat — Veröffentlichen vor den ersten reproduzierbaren Ergebnissen würde sowohl die wissenschaftliche als auch die Patentschutzposition schwächen.
