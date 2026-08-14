# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · Polski · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Otwarta platforma do ultradźwiękowego przesyłu energii i danych przez lite ściany metalowe — „przez stal bez ani jednego otworu", zbudowana środkami warsztatowymi.

**Wypróbuj teraz (bez sprzętu):** `python3 software/sweep-map/sweep_map.py --mock`

**Status:** etap 0 — przygotowania · 💰 **[$250 nagrody za pierwszą niezależną budowę](https://github.com/zeloras/through-metal-link/issues)** · lista zakupów: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Dokumentacja jest wielojęzyczna: angielski jest językiem głównym i znajduje się w ścieżkach kanonicznych; każdy inny język odzwierciedla drzewo w [translations/](..). Edytuj w dowolnym języku — CI tłumaczy i zatwierdza resztę (zobacz [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="../../docs/img/sim0-rig-sketch.png" alt="Stage 1 rig: Pi → DDS → half-bridge → transformer → piezo TX | steel | piezo RX → bridge → ADC → Pi" width="900"></p>

## Pomysł w jednym akapicie

Fale radiowe nie przenikają przez metal (klatka Faradaya), a wprowadzenie kabla oznacza otwór, uszczelnienie i punkt awarii. Ultradźwięki z kolei przechodzą przez metal bez problemu: element piezoelektryczny po każdej stronie ściany zamienia ją w kanał transmisji energii i danych. Literatura laboratoryjna już udowodniła fizykę na poważnym poziomie (RPI: 50 W + 12 Mbit/s przez 63,5 mm stali; NASA JPL: do ~kW przez 5 mm tytanu) — to dowody istnienia z użyciem specjalistycznego sprzętu, a nie garażowa lista materiałów (BOM) z tego repozytorium. Podstawowe patenty wygasły, a otwarta, odtwarzalna platforma jeszcze nie istnieje — to repozytorium buduje taką, zaczynając od **mocy rzędu watów i danych rzędu kbit/s przez 3–5 mm stali**, gdy tylko etap 2 zostanie zmierzony.

## Plan działania

| Etap | Rezultat | Kryterium sukcesu | Oczekiwanie |
|---|---|---|---|
| 1. Mapa skanowania | odpowiedź częstotliwościowa kanału „Langevin–3 mm stal–Langevin” | znaleziona para rezonansów, wykres w [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](../../docs/img/sim1-sweep-contacts.png), [sim2](../../docs/img/sim2-pair-mismatch.png) |
| 2. Waty | moc w obciążeniu przy rezonansie | ≥0,5 W przez 3 mm stali, protokół w [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](../../docs/img/sim4-power-budget.png) |
| 3. Dane | FSK/OOK przez tę samą parę | ≥1 kbit/s bez błędów | [sim5](../../docs/img/sim5-ook-datarate.png) |
| 4. Węzeł | ESP32 + czujnik w zespawanej szczelnie skrzynce, zasilany i telemetrowany samym dźwiękiem | ≥1 h pracy autonomicznej | [sim4](../../docs/img/sim4-power-budget.png) |
| 5. Publikacja | repo publicznie dostępne, artykuł/how-to | reprodukcja przez stronę trzecią | — |

## Mapa repozytorium

python3 software/sweep-map/sweep_map.py --mock
```

**Gotowe, gdy (według etapów):** etap 1 — pik skanowania powtarza się w dwóch przebiegach z dokładnością do <200 Hz ([eksperymenty/001](experiments/001-sweep-map-3mm-steel/README.md)); etap 2 — ≥0,5 W do znanego obciążenia przez 3 mm stali i zapalona dioda LED po stronie RX ([eksperymenty/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Teoria w minutę</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

Piezoelektryczny nadajnik (TX) jest dociskany do ściany i wprowadza w nią falę podłużną; piezoelektryczny odbiornik (RX) po drugiej stronie zamienia ją z powrotem na prąd. Prędkość dźwięku w stali: ~5900 m/s.

Dwa tryby pracy:

| Tryb | Częstotliwość | Rezonans ustalany przez | Daje | Status |
|---|---|---|---|---|
| **A** — przetworniki Langevina | 40 kHz | para przetworników (ściana ≪ λ — "membrana") | waty, kbit/s | tryb startowy (etapy 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — dyski | 0,6–1 MHz | rezonans grubościowy ściany ([grzebień](../../docs/img/sim3-thickness-comb.png)) | setki mW, setki kbit/s | odgałęzienie po pierwszych watach; wymaga automatycznego śledzenia częstotliwości |

Główne straty: niedopasowanie rezonansu wewnątrz pary (±1 kHz dla tanich przetworników Langevina), jakość kontaktu akustycznego (epoksyd > smar sprzęgający + zacisk > suchy nacisk), niedopasowanie kątowe, dryf rezonansu z temperaturą. Odpowiedź na wszystkie jest ta sama: **mapa skanowania przed każdą zmianą konfiguracji**.

</details>

<details>
<summary><b>📈 Co powinno pokazać stanowisko: wykresy oczekiwane z symulatora</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Półempiryczny model kanału (nie FEM, **nie dane laboratoryjne** — intuicja dla "jak powinno wyglądać skanowanie i w co celować"). Założenia są jawne w `channel_sim.py` (obciążone Q≈40, współczynniki kontaktu k, sprawność łańcucha η≤40%). Wygeneruj ponownie za pomocą: `python3 channel_sim.py --out ../../docs/img`.

**Etap 1 — skanowanie.** Wąski pik w okolicach ~40 kHz; zastępcze mnożniki kontaktu w modelu to smar:suchy:szczelina = 1 : 0,25 : 0,02 (tzn. smar ≈4× suchy i ≈50× szczelina powietrzna). Brak piku oznacza problem z kontaktem lub parą:

<img src="../../docs/img/sim1-sweep-contacts.png" width="720">

**Dlaczego 4 przetworniki Langevina, a nie 2.** Przy Q≈40 niedopasowanie rezonansu 1,5 kHz wewnątrz pary obniża moc w modelu ~10×:

<img src="../../docs/img/sim2-pair-mismatch.png" width="720">

**Etap 3 — dane.** OOK napotyka na dzwonienie rezonatora (model Q~40 → τ≈0,3 ms): 1 kbit/s jest czysty, przy 5 kbit/s oko jest zamknięte. Aby iść szybciej, potrzebny jest tryb B:

<img src="../../docs/img/sim5-ook-datarate.png" width="720">

**Budżet mocy odbiornika.** Zacieniowane pasma to **cele** (tryb A 0,5–5 W, jeśli etap 2 wypali; tryb B niższe). Realistyczne pierwsze obciążenia to pracujące z wypełnieniem ESP32 / BLE / LED; Wi-Fi jest pokazane jako znacznik szczytowego poboru, a nie ciągła obietnica:

<img src="../../docs/img/sim4-power-budget.png" width="720">

**Na później (tryb B).** Płyta staje się przezroczysta przy grzebieniu rezonansów grubościowych — częstotliwość musi być śledzona:

<img src="../../docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Bezpieczeństwo — przeczytaj przed pierwszym włączeniem</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Od dziesiątek do setek woltów na piezo**, gdy tylko sterownik etapu 2 zostanie włączony — dioda TVS po stronie odbioru trafia tam PRZED pierwszym włączonym przebiegiem; nie dotykaj przewodów.
2. **Sieć energetyczna** — tylko przez zasilacz laboratoryjny / izolację; płytki sterujące oczyszczaczy ultradźwiękowych są galwanicznie połączone z siecią.
3. **Uszy** — przy niebanalnej mocy pracuj z przetwornikami dociskającymi do metalu; nigdy nie uruchamiaj ultradźwięków powietrznych o dużej mocy bez obudowy.
4. **Ciepło** — niezaciśnięty przetwornik Langevina przegrzewa się w kilka minut pod zasilaniem; zaciśnij przed zwiększeniem prądu (tylko krótkie uruchomienie elektryczne przy niskim prądzie — patrz README sterownika).
5. **Odłamki** — piezoceramika jest krucha: zbyt mocno dokręcona śruba lub uderzenie oznaczają odłamki; noś okulary ochronne przy każdej pracy mechanicznej.

docs/            teoria, stan wiedzy, bezpieczeństwo, zastosowania, dziennik decyzji (ADR)
docs/img/        wykresy oczekiwań (generowane przez software/simulator/channel_sim.py)
hardware/        BOM, sterownik (półmostek), odbiornik (prostownik/harwester)
firmware/        firmware węzła (ESP32 — stub do etapu 4)
software/        skrypty pomiarowe (mapa odpowiedzi częstotliwościowej) i symulator kanału
experiments/     protokoły eksperymentów — z szablonu, jeden katalog = jeden eksperyment
data/            surowe logi (duże pliki nie trafiają do gita)
```

</details>

## Zasady

1. **Powtarzalność od zera.** Każdy z lutownicą i ~210 $ może odtworzyć wynik korzystając wyłącznie z tego repozytorium.
2. **Każdy eksperiment to protokół.** Bez „jakoś działa”: [experiments/TEMPLATE.md](experiments/TEMPLATE.md) jest obowiązkowy.
3. **Higiena patentowa.** Budujemy na wygasłej warstwie ([docs/01-prior-art.md](docs/01-prior-art.md)); decyzje są zapisywane w [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md).
4. **Najpierw pomiary, potem opinie.** Mapa skanowania przed jakimikolwiek wnioskami o kanale.

## Licencje i patenty

Kod — Apache-2.0, sprzęt — CERN-OHL-W v2, dokumentacja — CC-BY-4.0; pełne teksty w [LICENSES/](../../LICENSES). Każdy może forkać i rozwijać ten projekt, również komercyjnie; ochrona patentowa wynika z klauzul udzielania i odwetowych w licencjach oraz ze strategii sztuki przodującej. Pełny schemat i protokół publikacji obronnej: [LICENSES.md](LICENSES.md); zasady współtworzenia: [CONTRIBUTING.md](CONTRIBUTING.md).
