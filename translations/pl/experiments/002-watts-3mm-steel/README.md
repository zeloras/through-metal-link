# Eksperyment 002: Pierwsze waty przez 3 mm stali (PLANOWANY)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · Polski · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Etap:** 2 (moc w znaną rezystancję przy rezonansie znalezionym w [001](../001-sweep-map-3mm-steel/README.md)).
- **Cel:** zmierzyć rzeczywistą moc DC dostarczoną przez 3 mm stali z układem half-bridge i transformatorem dopasowującym.
- **Hipoteza:** przy parze Langevina z tej samej partii, kontakcie smar+śruba (lub epoksyd) i dostrojonym transformatorze dopasowującym, osiągnięcie ≥0,5 W w rezystancji obciążenia przy piku z etapu 1 jest wykonalne. (Literaturowe wartości wielowatowe/kW dotyczyły innych przetworników i sposobów łączenia — traktować je jako górny limit, nie próg zdawczy.)
- **Wymagania wstępne:**
  - Eksperyment 001 zamknięty (powtarzalny pik, częstotliwość zarejestrowana).
  - TVS zamontowany w torze RX przed podaniem jakiegokolwiek zasilania sterownika ([docs/02-safety.md](../../docs/02-safety.md)).
  - Sekwencja uruchomienia sterownika wykonana ([hardware/driver/README.md](../../../../hardware/driver/README.md)).
- **Stanowisko (minimum):**
  - TX: Pi → AD9833 square → dead-time shaper → IR2110 half-bridge → transformator dopasowujący → Langevin dociśnięty do płyty ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Przegroda: 3 mm stali, metoda kontaktu zarejestrowana (smar+śruba / epoksyd / inna).
  - RX: Langevin → mostek Schottky'ego → znane R_load (rezystor mocy) i/lub LED; pomiar V_dc i I_dc za mostkiem (topologia [sch2](../../../../hardware/schematics/sch2-receiver-stage1.png), obciążenie zamiast samego ADC).
- **Procedura (zarys):**
  1. Uruchomienie elektryczne przy limicie zasilacza 0,2 A bez deklarowania mocy akustycznej.
  2. Dociśnięcie TX/RX, ustawienie częstotliwości sterowania na pik z eksperymentu 001.
  3. Powolne podnoszenie limitu prądu; logowanie V/I zasilacza, temperatury MOSFET/transformatora, V_dc i I_dc na obciążeniu.
  4. P_load = V_dc · I_dc. Opcjonalnie: jednorazowe zdjęcie demonstracyjne LED po ustaleniu P_load.
  5. Jedno powtórzenie po ostygnięciu; częstotliwość piku może dryfować z temperaturą — ponownie sprawdzić mini-sweepem, jeśli moc spada.
- **Kryteria sukcesu:**
  1. P_load ≥ 0,5 W przez 3 mm stali przy udokumentowanej częstotliwości i metodzie kontaktu.
  2. Dwa przebiegi zgodne co do P_load w zakresie ~20% przy tym samym docisku/kuplancie (stabilność rzędu wielkości, jeszcze nie jakość metrologiczna).
  3. Zdjęcie LED (lub innego obciążenia) + CSV/log podlinkowane z tego pliku w `data/`.
- **Porażka to dane:** jeśli P_load pozostaje ≪ 0,5 W, zarejestrować Δf pary (z 001), metodę kontaktu, zwoje transformatora i przebiegi — to dane wejściowe do następnego ADR, nie powód do cichej edycji symulatora.
