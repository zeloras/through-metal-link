# Kanały hybrydowe: bariera → fizyka → liczby

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · [Português](../../pt/docs/04-hybrid-channels.md) · [Español](../../es/docs/04-hybrid-channels.md) · [Français](../../fr/docs/04-hybrid-channels.md) · [Italiano](../../it/docs/04-hybrid-channels.md) · Polski · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

Zasada (wniosek z „paradoksu penetracji”): fala przechodzi przez barierę dokładnie w takim stopniu, w jakim słabo z nią oddziałuje — dlatego nie istnieje żaden uniwersalny kanał. Platforma nie goni za jednym kanałem; dla każdej bariery wybiera fizykę, na którą bariera jest przezroczysta, a odbiornik jest rezonansowo „chciwy”.

## Tabela wyboru kanału

| Bariera | Kanał roboczy | Spodziewane (rzędy wielkości) | Uwagi |
|---|---|---|---|
| Stal/aluminium 1–60 mm, kontakt możliwy | Piezoakustyka (nasza główna) | waty; kbit/s (do Mbit/s w trybie MHz) | wymaga kontaktu akustycznego (smar sprzęgający/epoksyd) |
| Metal: brudny, malowany, gorący, kontakt niepożądany | EMAT (magnetyka → dźwięk w ściance) | mW; kbit/s; szczelina do ~3 mm | tylko ścianki przewodzące; dane, nie moc |
| Ferromagnetyczna ścianka bez piezo w ogóle | Magnetostrykcja (cewka wprawia stal w drgania) | okruchy; bit/s–kbit/s | gałąź eksperymentalna, tania w testach |
| Podwójna ścianka z próżnią (termos, kriostat, dewar) | Magnetyka LF (dziesiątki–setki Hz) | µW–mW; bit/s | naskórkowość: w stali δ≈0,6 mm @1 kHz — zbijaj częstotliwość w dół |
| Niemetal: szkło, plastik, ceramika | Piezoakustyka (łatwiej niż w metalu) | waty; kbit/s | + zwykłe RF często też przechodzi — sprawdź to najpierw |
| Ścianka z warstwą gumy/pianki, kompozyt | Szczerze: prawie ślepy zaułek | — | absorber zjada wszystko; obejściem jest miejsce bez powłoki |
| Ciecz za ścianką (pełny zbiornik) | Piezoakustyka, zdegradowana | moc − kilka dB; krótszy pogłos | obciążenie cieczą przesuwa/tłumi rezonans — wykonaj ponowne przeszukiwanie na pełnym naczyniu; utrzymuj ciągłą intensywność ≲1 W/cm², aby pozostać poniżej kawitacji ([teoria](00-theory.md#effect-on-the-wall-and-the-media-behind-it)) |
| Bąbelkująca ciecz w ścieżce akustycznej | Obejście architektoniczne | — | zamontuj odbiornik na ściance, trzymaj ciecz poza ścieżką |

## Architektura węzła hybrydowego

- Warstwa zasilania: para piezo w rezonansie (etapy 1–4).
- Bezkontaktowa warstwa danych: głowica EMAT jako odłączany „skaner-pistolet” (etap ~6).
- Warstwa zapasowa: cewki LF dla kanapek próżniowych (gdy zadanie tego wymaga).
- Protokół odkrywania (docs/03) rozszerza się z „przeszukiwania po częstotliwości” na „przeszukiwanie po fizyce”: ping piezo → ping EMAT → ping LF; węzeł sam wybiera kanał, który przechodzi, i zgłasza, jaką barierę widzi.

## Przykładowe zastosowania według kanału

1. **Hermetyczne pakiety baterii (EV/magazynowanie):** czujnik T/gazu wewnątrz zalanego obudowy; zasilanie+dane przez parę piezo przez 2–3 mm aluminium. Rynek kwitnie, a penetracja obudowy baterii = piekło certyfikacji.
2. **Kriostat/dewar:** rejestrator temperatury wewnątrz, wysyłający pakiet bitów raz na minutę przez magnetykę LF przez płaszcz próżniowy. Fundamentalnie poza zasięgiem akustyki — tu hybryda jest niezastąpiona.
3. **Rurociąg/autoklaw pod ciśnieniem:** skaner EMAT przyciśnięty do gorącej malowanej rury bez żadnego przygotowania powierzchni — odczytuje pasywny rezonansowy sygnał z wnętrza.
4. **Zbiorniki fermentacyjne (piwo/wino, stal nierdzewna):** czujnik gęstości/T wewnątrz zbiornika bez ani jednej penetracji — kody sanitarne uwielbiają brak otworów.
5. **Kontener morski/sejf:** „czy ładunek żyje” — para piezo przez pofalowaną stal, odpytywana ręcznym skanerem.

## Ograniczenia, których żadna warstwa nie rozwiąże
Moc — tylko piezo kontaktowe (EMAT i magnetyka LF są o rzędy wielkości słabsze). Ścianki kompozytowe/gumowane są poza platformą. Prędkość kanału LF to bity na sekundę — to telemetria, nie streaming.
