# Vorarbeiten: worauf wir aufbauen

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · Deutsch · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## Die Regel
Jede technische Entscheidung in diesem Repo muss auf eine Quelle aus der „freien" Liste (abgelaufene Patente, Paper) zurückführbar sein. Lebende Patente sind Lese-only — man fördert aus ihnen Erkenntnisse über die Probleme, kopiert aber niemals ihre Ansprüche (das ist für die Kommerzialisierung in den USA relevant; siehe die Patentkarte im Projekt).

## Das freie Fundament (abgelaufene/aufgegebene Patente = Public Domain)
- **US5982297** (Aerospace Corp, 1997) — das Grundrezept: ein Piezo-Paar durch die Wand, Leistung + bidirektionale Daten. Das wichtigste Kochbuch.
- US5594705 (Dynamotive, 1994) — ein „akustischer Transformator" durch den Rumpf.
- US6037704, US6127942 (Aerospace Corp) — Sensoren mit Strom versorgen, Daten zurücklesen.
- **US7902943** (Caltech/JPL, wegen unbezahlter Erhaltungsgebühren 2019 verfallen) — der Sherrit-Feed-through: Reflektor, akustischer Transformator.
- US9748870 (Caltech/JPL) — mechanische Arbeit durch die Wand.
- **US9361877** (Univ. Oklahoma, wegen unbezahlter Erhaltungsgebühren verfallen) — ein modernes, vollständiges Transceiver-System.
- US20100027379 / WO2008105947 (DOE+RPI, aufgegeben) — ein Träger von außen + Lastmodulation von innen.

## Wichtige Paper
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, 63.5 mm Stahl.
- Sherrit et al., NASA NTRS 20080048150 — eine 100-W-Lampe, durch eine Wand mit Strom versorgt.
- Yang et al., Sensors 2015 (10.3390/s151229870) — Übersicht, die beste Zusammenfassung der Zahlen.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — Metamaterial, 2 %→66 % durch 1 mm Edelstahl (kein Patent gefunden Stand 07.2026).

Diese Paper sind die **Physik- und Patent-Hygiene-Basislinie**. Ihre Leistungs-/Bitraten-Zahlen entstanden mit Labortransducern, Bonding und Matching — nicht mit der AliExpress-Langevin + Fett-BOM aus [QUICKSTART.md](../QUICKSTART.md). Zitiert sie als Existenznachweise; die eigenen Bestehenswerte des Projekts leben in [experiments/](../experiments/).

## Was wir nicht kopieren, solange es lebt
Der alte Kern dieser Liste ist nur US und läuft etwa 2032–2033 ab, und die Stufen 1–4 brauchen nichts davon: OFDM mit Subträgern, die so platziert sind, dass sie den Harmonischen des Leistungskanals ausweichen (RPI US9054826); Vollduplex „AM-Downlink + Lastmodulations-Uplink + Frequenz-Tracking" als ein einziges Schema (RPI US9455791); konforme Transducer für gekrümmte Oberflächen nach dem Drexel-Ansatz (US10594409). Die folgenden Familien sind davon nicht betroffen: eine liest auf den nackten Leistungskanal der Stufe 2, und eine läuft in Europa bis 2039.

**Hinzugefügt durch die 2026-08-Recherche (Statusangaben sind Google-Patents-Flags — vor jeder kommerziellen Nutzung im USPTO Patent Center / im EP-Register erneut prüfen):**
- **US8594572B1** (US Navy, Priorität 2011-06, 12-Jahres-Gebühr 2025 bezahlt, läuft bis 2032-01, nur US) — Anspruch 1 lautet „Wand + Stromquelle + Transducer, der Strom in Ultraschall durch die Wand wandelt + Transducer, der zurückwandelt + stromversorgtes elektronisches Gerät", ohne Frequenz-, Material- oder Dickenbeschränkung: er liest wörtlich auf den nackten Leistungskanal in den USA. Welles US5982297 (1997) offenbart dieselbe Anordnung, somit ist die abgelaufene Schicht auch die Nichtigkeitsverteidigung; dennoch sollte ein US-Kommerzfork FTO-Beratung einholen.
- **EP3723304B1** (ABB, Priorität 2019-04, erteilt 2023-08, nur in **DE und GB aufrechterhalten** — CH 2024-04 verfallen, keine weitere Validierung in den gelesenen Registerdaten gefunden; bis 2039-04; kein US-Mitglied) — ein „akustischer Wellenleiter" (die Gefäßwand in der Beschreibung), der Leistung *und* Datenrückkehr zu einer Sensorplattform überträgt, **wobei das leistungsübertragende Spektrum niedriger ist als das Datenspektrum**. Diese Beschränkung wurde während der Prüfung aus einem abhängigen Anspruch importiert, um die Erteilung zu erreichen, was unser Design-Around ist: der geplante Uplink ist Lastmodulation auf dem *selben* 40-kHz-Träger ([docs/03](03-discovery-protocol.md)) — Seitenbänder um den Leistungsträger, kein höheres Band (eine Anspruchslektüre, keine FTO-Stellungnahme). Kein separater höherfrequenter Datenträger (ABBs eigenes Beispiel: 200–300 kHz Daten über niederfrequenten Strom) zu einer Mode-A-Leistungsverbindung in einem Produkt für DE/GB hinzufügen.
- **Ultrapower-Familie** (Priorität 2014-03, bis 2035-03): US10295500B2 — Sensor in einem metallischen *Rohr*, Transceiver außen, **konvexe/konkave** Transducer-Arrays; US10684260B2 / US10948457B2 — eine Metallstange *durch* die Wand. Wir verwenden flache plan-gedrehte Pads und keine Stange.
- **US9602221B2** (Zackat Inc.; Sicherheiten-/Abtretungsereignisse nennen Anelto Inc. / Instant Care Inc.; Priorität 2014-03, 2021 wiedereingesetzt, Gebühr 2024 bezahlt, bis 2035-10, US) — Anspruch 1: ein Ultraschall-Sender an einem „Class-1-Gerät" in einer Explosionsgefährdeten-Zone, Empfänger außen, Alarm an einen entfernten Operator; **unabhängiger Anspruch 14 lässt die Class-1-Gerät-Beschränkung fallen** (beliebiger Sensor in einer Explosionsgefährdeten-Zone + Ultraschall-Verbindung + Alarm). Nur relevant, falls ein Knoten jemals Alarme aus einem Gefahrenbereich sendet — ein Grund, jede solche Anwendung in den USA im Labormaßstab zu halten.
- Tangential, notiert: GE US9146266B2 (Telemetrie durch Kraftwerksstrukturen, bis 2033), UNT US11415555 (passive SAW/BAW durch die Wand), CEA EP4080791B1 (Impedanz-Scan-Frequenzoptimierung), RPI US9331879B2 (MIMO), US9505031B2 (federgelagertes Gehäuse). RPI US9455791B2 Anspruch 1 enthält zwar MOSFET-Lastmodulation des inneren Transducers — aber nur gebündelt mit einem differentiellen AM-Downlink, Barker-Sequenz-synchronisierter Abtastung und dem Frequenz-Schritt/Track-Algorithmus; [docs/03](03-discovery-protocol.md) hat bewusst keinen AM/Barker-Downlink, und diese gesamte Kombination darf nicht implementiert werden, solange das Patent lebt.
- Frei, zusätzlich bestätigt: Progeny/General Dynamics US20120127833A1 (separate Strom-/Datenfrequenzen — **aufgegeben**), RPI/DOE US20100027379A1 (Lastmodulations-Uplink — aufgegeben).
