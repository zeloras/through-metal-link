# Mapa zastosowań: kto potrzebuje tego stosu technologicznego i dlaczego

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · [Português](../../pt/docs/05-applications-map.md) · [Español](../../es/docs/05-applications-map.md) · [Français](../../fr/docs/05-applications-map.md) · [Italiano](../../it/docs/05-applications-map.md) · Polski · [Türkçe](../../tr/docs/05-applications-map.md) · [Українська](../../uk/docs/05-applications-map.md) · [Tiếng Việt](../../vi/docs/05-applications-map.md) · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

Stos platformy: aktywny kanał zasilania i danych przez ślepe ściany — piezoakustyka / EMAT / magnetyka LF. Poniżej: gdzie jest to potrzebne w prawdziwym świecie, kto już tam jest i co zostaje dla nas.

## 1. Zamknięte pakiety baterii (EV, magazyny energii domowe/przemysłowe)
- Ból: wczesne wykrywanie ucieczki termicznej — gazy (CO₂, H₂, opary elektrolitu) pojawiają się wewnątrz pakietu od kilku minut do kilku godzin przed pożarem; przebicie czujnika przez obudowę = utrata szczelności i certyfikacji.
- Nasz stos: węzeł gazowy/temperaturowy wewnątrz pakietu, zasilanie i telemetria przez parę piezo przez 2–3 mm aluminium. Zero otworów.
- Kto już tam jest: Liminal Insights — akustyczna *diagnostyka z zewnątrz* (patenty na metody analizy, nie na kanał). Nikt nie sprzedaje węzłów *wewnątrz* pakietu.
- Dojrzałość niszy: rynek rośnie lawinowo, a półka jest pusta. Dla platformy — zastosowanie pokazowe nr 1.

## 2. Sprzęt laboratoryjny: komory próżniowe, krioostaty, glove boxy
- Ból: każde elektryczne przepust do komory próżniowej to kołnierz za kilkaset dolarów i źródło nieszczelności; w krioostacie kabel = wyciek ciepła.
- Nasz stos: czujnik wewnątrz komory, zasilanie/dane dźwiękiem przez stalową ścianę; dla próżniowych kanapek dewarów — magnetyka LF (bit/s wystarczy dla loggera temperatury).
- Kto już tam jest: nikt z bezprzewodowym przesyłem przez ścianę; laboratoria żyją z kołnierzy przepustowych.
- Dojrzałość: idealna nisza startowa dla open source — laboratoria to właśnie publiczność dla open hardware (ścieżka TinyLev): kupują bez certyfikatów i cytują cię w publikacjach.

## 3. Produkcja żywności: tanki fermentacyjne, autoklawy (piwo, wino, nabiał)
- Ból: przepisy sanitarne nienawidzą penetracji (mycie CIP, strefy martwe); chcesz znać gęstość/T/ciśnienie wewnątrz tanku przez cały czas.
- Nasz stos: węzeł na wewnętrznej ścianie tanku ze stali nierdzewnej, odpytywany z zewnątrz skanerem ręcznym lub stałą parą.
- Kto już tam jest: zwykłe czujniki wkręcone w ścianę; brak bezprzewodowych rozwiązań przez ścianę.
- Dojrzałość: dosłownie w zasięgu testu garażowego (każda rzemieślnicza browarnia to poligon w zasięgu spaceru).
- Zastrzeżenie fizyczne: pełny tank obciąża ścianę — wykonaj ponowne skanowanie na pełnym naczyniu i utrzymuj ciągłą moc ≲1 W/cm²; powyżej tego kawitacja w produkcie (odgazowanie CO₂, obce posmaki, długotrwała erozja ściany) — [teoria](00-theory.md#effect-on-the-wall-and-the-media-behind-it).

## 4. Rurociągi, naczynia ciśnieniowe, przemysłowy NDT
- Ból: monitorowanie korozji/parametrów wewnątrz bez wyłączenia z pracy lub penetracji; powierzchnie są gorące, malowane, brudne.
- Nasz stos: „pistolet skaner” EMAT — przyłóż do rury bez przygotowania powierzchni, odczytaj pasywny rezonansowy beacon z wnętrza.
- Kto już tam jest: nakładane przepływomierze ultradźwiękowe i grubościomierze (dojrzały rynek), ale brak interaktywnych beaconów wewnątrz.
- Dojrzałość: średni zasięg; wymaga gałęzi EMAT (etap ~6).

## 5. Nafta i gaz / odwierty wgłębne oraz nuklearna
- Kto już tam jest: Metrol, Acoustic Data, Baker Hughes (odwierty wgłębne, 30 lat, model serwisowy); R&D DOE/UNT/Westinghouse (kontenery nuklearne).
- Uczciwy werdykt: zajęte i silnie regulowane — tam nie wchodzimy, ale sama ich obecność = dowód, że ta fizyka sprzedaje się za poważne pieniądze. Wykorzystać jako odniesienie w README.

## 6. Logistyka morska i konstrukcje podwodne
- Ból: „czy ładunek żyje” w zamkniętym kontenerze; dane od wewnętrznej strony kadłuba statku.
- Kto już tam jest: CSignum (LF EM przez wodę/przegrody) — jedyny bezpośredni sąsiad w hybrydowej filozofii.
- Dojrzałość: daleki zasięg; dla nas na razie tylko kierunek rozmyślań.

## Priorytety (co robić, w jakiej kolejności)
1. **Teraz:** etapy platformy 1–4 na scenariuszu pokazowym „komora laboratoryjna / zespawana skrzynka" (nisza nr 2 — najbardziej otwarta na open source).
2. **Następnie:** demo na żywym obiekcie z niszy nr 3 (tank browarniany) — tanie, fotogeniczne, prawdziwy użytkownik.
3. **Średni zasięg:** scenariusz baterii (nisza nr 1) jako przypadek flagowy do publikacji; gałąź EMAT dla niszy nr 4.

*Pasywna wizja (radiografia mionowa) została wydzielona do osobnego projektu — patrz muon-lab w bazie wiedzy.*
