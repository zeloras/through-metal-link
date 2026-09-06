# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · Polski · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Otwarta platforma do ultradźwiękowego przesyłu energii i danych przez lite ściany metalowe — „przez stal bez ani jednego otworu", zbudowana środkami warsztatowymi.

**Wypróbuj teraz (bez sprzętu):** `python3 software/sweep-map/sweep_map.py --mock`

**Ścieżki wejścia:**
- **A — dry-run:** symulowany sweep + [symulator](../../software/simulator/channel_sim.py) (bez stanowiska)
- **B — budowa etapu 1:** [QUICKSTART.md](QUICKSTART.md) → [experiments/001](experiments/001-sweep-map-3mm-steel/README.md)
- **C — wkład bez sprzętu:** stan techniki / dokumenty / tłumaczenia / komentarze ADR ([CONTRIBUTING.md](CONTRIBUTING.md))

**Status:** etap 0 — przygotowania · **brak walidacji sprzętowej** (tylko symulator; nagroda za pierwszą budowę) · 💰 **[$250 nagrody](https://github.com/zeloras/through-metal-link/issues/5)** · lista zakupów: [QUICKSTART.md](QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](LICENSES.md)

Dokumentacja jest wielojęzyczna: angielski jest językiem podstawowym i znajduje się w ścieżkach kanonicznych; każdy inny język odzwierciedla drzewo pod [translations/](..). Edytuj w dowolnym języku — CI tłumaczy i zatwierdza resztę (patrz [CONTRIBUTING.md](CONTRIBUTING.md)).

<p align="center"><img src="docs/img/sim0-rig-sketch.png" alt="Stanowisko etapu 1: Pi → DDS → pół-mostek → transformator → piezo TX | stal | piezo RX → mostek → ADC → Pi" width="900"></p>

## Idea w jednym akapicie

Fale radiowe nie przenikają przez metal (klatka Faradaya), a kablowe przejście oznacza dziurę, uszczelnienie i punkt awarii. Ultradźwięki z kolei przenikają przez metal bez problemu: element piezoelektryczny po każdej stronie ściany zamienia ją w kanał dla zasilania i danych. Literatura laboratoryjna już udowodniła fizykę na poważnych poziomach (RPI: 50 W + 12 Mbit/s przez 63,5 mm stali; NASA JPL: do ~kW przez 5 mm tytanu) — to dowody istnienia z użyciem specjalistycznego sprzętu, a nie garażowy BOM z tego repozytorium. Podstawowe patenty wygasły, a żadna otwarta, odtwarzalna platforma jeszcze nie istnieje — to repozytorium buduje taką, zaczynając od **zasilania rzędu watów i danych kbit/s przez stal 3–5 mm**, gdy tylko etap 2 zostanie zmierzony.

## Plan działania

| Etap | Rezultat | Kryterium sukcesu | Oczekiwanie |
|---|---|---|---|
| 1. Mapa skanowania | odpowiedź częstotliwościowa kanału „Langevin–3 mm stali–Langevin” | znaleziona para rezonansów, wykres w [experiments/001](experiments/001-sweep-map-3mm-steel/README.md) | [sim1](docs/img/sim1-sweep-contacts.png), [sim2](docs/img/sim2-pair-mismatch.png) |
| 2. Waty | moc w obciążeniu przy rezonansie | ≥0,5 W przez 3 mm stali, protokół w [experiments/002](experiments/002-watts-3mm-steel/README.md) | [sim4](docs/img/sim4-power-budget.png) |
| 3. Dane | FSK/OOK przez tę samą parę | ≥1 kbit/s bez błędów | [sim5](docs/img/sim5-ook-datarate.png) |
| 4. Węzeł | ESP32 + czujnik w zespawanej szczelnie skrzynce, zasilany i telemetrowany samym dźwiękiem | ≥1 h autonomicznej pracy | [sim4](docs/img/sim4-power-budget.png) |
| 5. Publikacja | pierwsza niezależna replikacja + artykuł/instrukcja + zrzut Zenodo | udokumentowana reprodukcja przez stronę trzecią | — |

## Mapa repozytorium

python3 software/sweep-map/sweep_map.py --mock
```

**Gotowe, gdy (według etapu):** etap 1 — pik skanu odtwarza się między dwoma przebiegami z dokładnością <200 Hz ([experiments/001](experiments/001-sweep-map-3mm-steel/README.md)); etap 2 — ≥0,5 W w znane obciążenie przez 3 mm stali i zapalona LED po stronie RX ([experiments/002](experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Teoria w minutę</b> — <a href="docs/00-theory.md">docs/00-theory.md</a></summary>

Piezoelektryczny TX jest dociskany do ściany i wprowadza w nią falę podłużną; piezoelektryczny RX po drugiej stronie zamienia ją z powrotem na prąd. Prędkość dźwięku w stali: ~5900 m/s.

Dwa tryby pracy:

| Tryb | Częstotliwość | Rezonans ustalany przez | Daje | Status |
|---|---|---|---|---|
| **A** — przetworniki Langevina | 40 kHz | para przetworników (ściana ≪ λ — „membrana”) | waty, kbit/s | tryb startowy (etapy 1–4, [ADR-0001](docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — dyski | 0,6–1 MHz | rezonans grubościowy ściany ([grzebień](docs/img/sim3-thickness-comb.png)) | setki mW, setki kbit/s | odgałęzienie po pierwszych watach; wymaga automatycznego śledzenia częstotliwości |

Główne straty: niedopasowanie rezonansu w obrębie pary (±1 kHz dla tanich przetworników Langevina), jakość kontaktu akustycznego (epoksyd > smar sprzęgający + zacisk > suchy nacisk), niewspółosiowość, dryf rezonansu z temperaturą. Odpowiedź na wszystkie jest ta sama: **mapa skanu przed każdą zmianą konfiguracji**.

</details>

<details>
<summary><b>📈 Co stanowisko powinno pokazać: wykresy oczekiwane z symulatora</b> — <a href="software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Półempiryczny model kanału (nie FEM, **nie dane laboratoryjne** — intuicja dla „jak powinien wyglądać skan i w co celować”). Założenia są jawne w `channel_sim.py` (obciążone Q≈40, k-czynniki kontaktu, sprawność łańcucha η≤40%). Regeneruj przez: `python3 channel_sim.py --out ../../docs/img`.

**Etap 1 — skan.** Wąski pik w okolicach ~40 kHz; mnożniki kontaktu placeholder w modelu to smar:suchy:szczelina = 1 : 0,25 : 0,02 (tzn. smar ≈4× suchy i ≈50× szczelina powietrzna). Brak piku oznacza problem z kontaktem lub parą:

<img src="docs/img/sim1-sweep-contacts.png" width="720">

**Dlaczego 4 przetworniki Langevina, nie 2.** Przy Q≈40 niedopasowanie rezonansu 1,5 kHz w obrębie pary obniża moc z modelu ~10×:

<img src="docs/img/sim2-pair-mismatch.png" width="720">

**Etap 3 — dane.** OOK natrafia na dzwonienie rezonatora (model Q~40 → τ≈0,3 ms): 1 kbit/s jest czysty, przy 5 kbit/s oko jest zamknięte. Szybsza transmisja wymaga trybu B:

<img src="docs/img/sim5-ook-datarate.png" width="720">

**Budżet mocy odbiornika.** Zacieniowane pasma to **cele** (tryb A 0,5–5 W jeśli etap 2 się uda; tryb B niżej). Realistyczne pierwsze obciążenia to pracujące w cyklach ESP32 / BLE / LED; Wi-Fi pokazany jest jako znacznik szczytowego poboru, nie ciągła obietnica:

<img src="docs/img/sim4-power-budget.png" width="720">

**Na później (tryb B).** Płyta staje się przezroczysta przy grzebieniu rezonansów grubościowych — częstotliwość musi być śledzona:

<img src="docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Bezpieczeństwo — przeczytaj przed pierwszym włączeniem</b> — <a href="docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Od dziesiątek do setek woltów na piezo** gdy tylko sterownik etapu 2 zostanie uruchomiony — TVS po stronie odbioru wchodzi PRZED pierwszym zasilonym przebiegiem; nie dotykaj przewodów.
2. **Sieć** — tylko przez zasilacz laboratoryjny / izolację; płyty sterowników z myjek ultradźwiękowych są galwanicznie połączone z siecią.
3. **Uszy** — przy nieprzebranej mocy pracuj z przetwornikami dociskającymi do metalu; nigdy nie uruchamiaj ultradźwięków o dużej mocy w powietrzu bez obudowy.
4. **Ciepło** — niezaciśnięty przetwornik Langevina przegrzewa się w kilka minut przy mocy; zaciśnij przed zwiększeniem prądu (tylko krótkie uruchomienie elektryczne przy niskim prądzie — patrz README sterownika).
5. **Odłamki** — piezoceramika jest krucha: zbyt mocno dokręcona śruba lub uderzenie oznacza odłamki; noś okulary ochronne przy każdej pracy mechanicznej.

</details>

docs/            teoria, stan wiedzy, bezpieczeństwo, zastosowania, dziennik decyzji (ADR)
docs/img/        wykresy oczekiwań (generowane przez software/simulator/channel_sim.py)
hardware/        BOM, sterownik (półmostek), odbiornik (prostownik/harvester)
firmware/        firmware węzła (ESP32 — stub do etapu 4)
software/        skrypty pomiarowe (mapa odpowiedzi częstotliwościowej) i symulator kanału
experiments/     protokoły eksperymentów — z szablonu, jeden katalog = jeden eksperyment
data/            surowe logi (duże pliki pozostają poza gitem)
```

</details>

## Zasady

1. **Powtarzalność od zera.** Każdy z lutownicą i ~210 $ może odtworzyć wynik korzystając wyłącznie z tego repozytorium.
2. **Każdy eksperyment to protokół.** Bez „jakoś zadziałało”: [experiments/TEMPLATE.md](experiments/TEMPLATE.md) jest obowiązkowy.
3. **Higiena patentowa.** Budujemy na wygasłej warstwie ([docs/01-prior-art.md](docs/01-prior-art.md)); decyzje są zapisywane w [docs/decisions/](docs/decisions/0001-frequency-mode-choice.md).
4. **Najpierw pomiary, potem opinie.** Mapa skanowania przed jakimikolwiek wnioskami o kanale.

## Licencje i patenty

Kod — Apache-2.0, sprzęt — CERN-OHL-W v2, dokumentacja — CC-BY-4.0; pełne teksty w [LICENSES/](../../LICENSES). Każdy może forkać i rozwijać ten projekt, również komercyjnie; ochrona patentowa wynika z klauzul udzielenia i odwetowych w licencjach oraz ze strategii sztuki przodującej. Pełny schemat i protokół publikacji obronnej: [LICENSES.md](LICENSES.md); zasady współtworzenia: [CONTRIBUTING.md](CONTRIBUTING.md).
