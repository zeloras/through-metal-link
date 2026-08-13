# Eksperyment 001: Mapa przeszukiwania kanału, stal 3 mm (PLANOWANY)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · [Português](../../../pt/experiments/001-sweep-map-3mm-steel/README.md) · [Español](../../../es/experiments/001-sweep-map-3mm-steel/README.md) · [Français](../../../fr/experiments/001-sweep-map-3mm-steel/README.md) · [Italiano](../../../it/experiments/001-sweep-map-3mm-steel/README.md) · Polski · [Türkçe](../../../tr/experiments/001-sweep-map-3mm-steel/README.md) · [Українська](../../../uk/experiments/001-sweep-map-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/001-sweep-map-3mm-steel/README.md) · [中文](../../../zh/experiments/001-sweep-map-3mm-steel/README.md) · [日本語](../../../ja/experiments/001-sweep-map-3mm-steel/README.md) · [한국어](../../../ko/experiments/001-sweep-map-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/001-sweep-map-3mm-steel/README.md)

- **Etap:** 1 (tylko mapa częstotliwości — brak celu watowego tutaj; moc to [002](../../../../experiments/002-watts-3mm-steel/README.md)).
- **Cel:** znaleźć rezonans pary przetworników Langevina przez płytę 3 mm; uzyskać pierwszą odpowiedź częstotliwościową kanału.
- **Hipoteza:** pik w okolicach 38–42 kHz (rezonans przetwornika Langevina), szerokość piku kilku kHz przy kontakcie smar+zacisk.
- **Wysterowanie:** podłączenie etapu 1 — sinus AD9833 (~0,6 Vpp) na TX, **bez** półmostka ([sch3](../../../../hardware/schematics/sch3-stage1-wiring.png), [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png)).
- **Procedura:** `python3 software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50` (użyj `--mock`, aby wykonać próbę potoku bez sprzętu).
- **Kryterium sukcesu:** odtwarzalny pik (dwa przebiegi jeden po drugim, odchyłka środka <200 Hz). Zapisz CSV/PNG w `data/` i podlinkuj je z tego pliku, gdy będą rzeczywiste.
- **Pomiar dodatkowy:** ten sam przebieg z „sprzęgło smarowe + zacisk" vs „suche dociskanie" — tylko amplitudy względne; bezwzględne wolty zależą od poziomu wysterowania i nie są porównywalne ze skalą zastępczą symulatora do czasu kalibracji.
- **Poza zakresem:** ≥0,5 W, LED z odzysku, uruchomienie półmostka → eksperyment 002.
