# Stan techniki: na czym budujemy

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · Polski · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## Zasada
Każda decyzja techniczna w tym repozytorium musi być wywodzona ze źródła z listy „wolnej" (wygasłe patenty, publikacje). Żywe patenty są tylko do odczytu — czerp z nich wiedzę o problemach, nigdy nie kopiuj ich roszczeń (to ma znaczenie dla komercjalizacji w USA; zobacz mapę patentów w projekcie).

## Wolna baza (patenty wygasłe/porzucone = domena publiczna)
- **US5982297** (Aerospace Corp, 1997) — podstawowy przepis: para piezoelementów przez ścianę, zasilanie + dwukierunkowa transmisja danych. Główna książka kucharska.
- US5594705 (Dynamotive, 1994) — „transformator akustyczny" przez kadłub.
- US6037704, US6127942 (Aerospace Corp) — zasilanie czujników, odczyt danych zwrotnych.
- **US7902943** (Caltech/JPL, wygasły z powodu niezapłaconych opłat utrzymania w 2019) — przepust Sherrita: reflektor, transformator akustyczny.
- US9748870 (Caltech/JPL) — praca mechaniczna przez ścianę.
- **US9361877** (Univ. Oklahoma, wygasły z powodu niezapłaconych opłat utrzymania) — nowoczesny kompletny system transceivera.
- US20100027379 / WO2008105947 (DOE+RPI, porzucony) — nośnik z zewnątrz + modulacja obciążenia od wewnątrz.

## Kluczowe publikacje
- Lawry i in., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12.4 Mbit/s, 63.5 mm stali.
- Sherrit i in., NASA NTRS 20080048150 — lampa 100 W zasilana przez ścianę.
- Yang i in., Sensors 2015 (10.3390/s151229870) — przegląd, najlepsze zestawienie liczb.
- Ji i in., Phys. Rev. Applied 21, 014059 (2024) — metamateriał, 2%→66% przez 1 mm stali nierdzewnej (brak patentu na dzień 07.2026).

Te publikacje to **baza fizyczna i patentowo-higieniczna**. Ich liczby dotyczące mocy/przepływności uzyskano na transducerach laboratoryjnych, z klejeniem i dopasowaniem — a nie z BOM opartym na AliExpress Langevin + smarze w [QUICKSTART.md](../QUICKSTART.md). Cytuj je jako dowód istnienia; własne progi zdawcze projektu znajdują się w [experiments/](../../../experiments).

## Czego nie kopiujemy, dopóki żyje
Stare jądro tej listy dotyczy tylko USA i wygasa około 2032–2033, a etapy 1–4 nie potrzebują żadnego z tych patentów: OFDM z podnośnymi rozmieszczonymi tak, aby omijać harmoniczne kanału zasilania (RPI US9054826); pełny dupleks „downlink AM + uplink z modulacją obciążenia + śledzenie częstotliwości" jako jeden schemat (RPI US9455791); transducery konformalne na zakrzywione powierzchnie według podejścia Drexel (US10594409). Rodziny poniżej to ani jedno, ani drugie: jedna czyta się na goły kanał zasilania etapu 2, a druga obowiązuje w Europie do 2039.

**Dodane przez wyszukiwanie z 2026-08 (statusy to flagi Google Patents — weryfikuj w USPTO Patent Center / EP Register przed jakimkolwiek użyciem komercyjnym):**
- **US8594572B1** (US Navy, priorytet 2011-06, opłata 12-letnia zapłacona 2025, obowiązuje do 2032-01, tylko USA) — roszczenie 1 to „ściana + źródło zasilania + transducer zamieniający prąd na ultradźwięki przez ścianę + transducer zamieniający z powrotem + zasilane urządzenie elektroniczne", bez ograniczeń co do częstotliwości, materiału ani grubości: czyta się dosłownie na goły kanał zasilania w USA. Patent Welle'a US5982297 (1997) opisuje to samo układ, więc wygasła warstwa jest też obroną z nieważności; mimo to amerykański fork komercyjny powinien uzyskać opinię FTO.
- **EP3723304B1** (ABB, priorytet 2019-04, przyznany 2023-08, utrzymywany **tylko w DE i GB** — CH wygasł 2024-04, brak innych walidacji w odczytanych danych rejestru; do 2039-04; brak członka US) — „przewodnik fali akustycznej" (ściana naczynia w opisie) przenoszący zasilanie *i* powrót danych do platformy czujnikowej, **gdzie widmo przenoszące zasilanie jest niższe niż widmo danych**. To ograniczenie zostało zaimportowane z roszczenia zależnego w trakcie procedury, aby uzyskać przyznanie — i stanowi nasze obejście: planowany uplink to modulacja obciążenia na *tym samym* nośniku 40 kHz ([docs/03](03-discovery-protocol.md)) — pasma boczne wokół nośnika zasilania, a nie wyższe pasmo (czytanie roszczenia, nie opinia FTO). Nie dodawaj osobnego nośnika danych o wyższej częstotliwości (własny przykład ABB: dane 200–300 kHz nad zasilaniem niskiej częstotliwości) do łącza zasilania trybu A w produkcie na DE/GB.
- **Rodzina Ultrapower** (priorytet 2014-03, do 2035-03): US10295500B2 — czujnik wewnątrz metalowej *rury*, transceiver na zewnątrz, **wypukłe/wklęsłe** matryce transducerów; US10684260B2 / US10948457B2 — metalowy pręt *przez* ścianę. My stosujemy płaskie pady fazowane i żadnego pręta.
- **US9602221B2** (Zackat Inc.; zdarzenia zabezpieczenia/przeniesienia wymieniają Anelto Inc. / Instant Care Inc.; priorytet 2014-03, przywrócony 2021, opłata zapłacona 2024, do 2035-10, USA) — roszczenie 1: nadajnik ultradźwiękowy na „urządzeniu klasy 1" wewnątrz strefy zagrożenia wybuchem, odbiornik na zewnątrz, alert do zdalnego operatora; **niezależne roszczenie 14 odrzuca ograniczenie urządzenia klasy 1** (dowolny czujnik w strefie zagrożenia wybuchem + łącze ultradźwiękowe + alert). Istotne tylko, jeśli węzeł kiedykolwiek wysyła alerty ze strefy niebezpiecznej — powód, aby utrzymać każdą taką aplikację na poziomie laboratoryjnym w USA.
- Poboczne, odnotowane: GE US9146266B2 (telemetria przez struktury wytwarzania energii, do 2033), UNT US11415555 (pasywne SAW/BAW przez ścianę), CEA EP4080791B1 (optymalizacja częstotliwości przez skan impedancji), RPI US9331879B2 (MIMO), US9505031B2 (obudowa na sprężynie). Roszczenie 1 RPI US9455791B2 zawiera modulację obciążenia MOSFET wewnętrznego transducera — ale tylko w pakiecie z downlinkiem różnicowym AM, próbkowaniem synchronizowanym sekwencją Barkera i algorytmem kroku/śledzenia częstotliwości; [docs/03](03-discovery-protocol.md) celowo nie ma żadnego downlinku AM/Barkera, i ta cała kombinacja nie może być realizowana, dopóki patent żyje.
- Wolne, dodatkowo potwierdzone: Progeny/General Dynamics US20120127833A1 (osobne częstotliwości zasilania/danych — **porzucony**), RPI/DOE US20100027379A1 (uplink z modulacją obciążenia — porzucony).
