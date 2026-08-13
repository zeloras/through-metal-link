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

## Was wir nicht kopieren, solange es lebt (nur US, bis ~2032; Stufen 1–4 brauchen es ohnehin nicht)
OFDM mit Subträgern, die so platziert sind, dass sie den Harmonischen des Leistungskanals ausweichen (RPI US9054826); Vollduplex „AM-Downlink + Lastmodulations-Uplink + Frequenz-Tracking" als ein einziges Schema (RPI US9455791); konforme Transducer für gekrümmte Oberflächen nach dem Drexel-Ansatz (US10594409).
