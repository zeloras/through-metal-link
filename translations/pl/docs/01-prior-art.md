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

## Czego nie kopiujemy, dopóki żyje (tylko USA, do ~2032; etapy 1–4 tego nie potrzebują)
OFDM z podnośnymi rozmieszczonymi tak, aby omijać harmoniczne kanału zasilania (RPI US9054826); pełny dupleks „downlink AM + uplink z modulacją obciążenia + śledzenie częstotliwości" jako jeden schemat (RPI US9455791); transducery konformalne na zakrzywione powierzchnie według podejścia Drexel (US10594409).
