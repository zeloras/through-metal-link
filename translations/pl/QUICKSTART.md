# QUICKSTART: od absolutnego zera do stanowiska testowego etapu 1–2

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Português](../pt/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · [Français](../fr/QUICKSTART.md) · [Italiano](../it/QUICKSTART.md) · Polski · [Türkçe](../tr/QUICKSTART.md) · [Українська](../uk/QUICKSTART.md) · [Tiếng Việt](../vi/QUICKSTART.md) · [中文](../zh/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md)

Scenariusz: masz tylko biurko i trochę pieniędzy. Wszystko poniżej doprowadzi Cię do działającego stanowiska — „mapa przeszukiwania + pierwsze waty przez stal". Ceny są orientacyjne, w USD.

## Koszyk 1 — narzędzia (baza na lata, ~$120)

| Element | Dlaczego | Cena | Skąd |
|---|---|---|---|
| Stacja lutownicza (klon T12) | wszystko | 35–50 | Ali |
| Multimetr (klasa AN8008/UT61) | napięcia, ciągłość, pojemność | 15–25 | Ali |
| Zasilacz laboratoryjny 30V/5A z ograniczeniem prądu | zasilanie drivera; ograniczenie prądu to Twoja polisa ubezpieczeniowa przed spalonymi MOSFET-ami | 45–60 | Ali/lokalnie |
| Trzecia ręka, lut, topnik, plecionka do odlutowania, obcinaczki, pęsety | drobnice, bez których się nie obejdzie | 15 | Ali/lokalnie |
| Przewody Dupont + płytka stykowa + rurka termokurczliwa | prototypowanie | 8 | Ali |

## Koszyk 2 — elektronika stanowiska (~$70)

| Element | Ilość | Cena | Uwaga |
|---|---|---|---|
| Raspberry Pi (Zero 2 W wystarczy; 4/5 wygodniejsze) + SD | 1 | 20–60 | mózg: sweep, logi, wykresy |
| Przetwornik Langevina 40 kHz 50–60 W | **4** | 40 | kup 4 z JEDNEJ partii; wybierzemy najlepszą parę przez sweep |
| Moduł DDS AD9833 | 2 | 8 | drugi jako zapas |
| IR2110 + IRF540 ×4 (lub moduł EGS002) | 1 zestaw | 10 | półmostek drivera |
| ADC ADS1115 | 2 | 4 | Pi nie ma własnego ADC |
| Rdzeń ferrytowy + drut nawojowy 0,5 mm | 2 | 4 | transformator dopasowujący |
| Mostek Schottky'ego (SS14 ×8), superkondensator 1F 5,5V ×2 | 1 | 4 | tor odbiornika |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | ochrona. NIE OSZCZĘDZAJ |
| Moduł GY-LTC3588 | 1 | 7 | harvester (etap 4, ale niech już jedzie) |
| Zestaw rezystorów/kondensatorów, LED | 1 | 8 | jeśli nie masz kompletnie nic |
| Elementy bierne uzupełniające: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | grosze; pełna lista — pozycje BOM 11–12 |

## Koszyk 3 — mechanika (~$20, lokalnie)

Płytka stalowa 3 mm ~150×150 — 2 szt. (skup złomu / cięcie laserowe); zaciski typu F ×2; gęsty, spójny smar sprzęgający (smar litowy); epoksyd; papier ścierny (do oczyszczenia pola styku).

## Opcjonalne, ale bardzo zalecane (~$90)

| Element | Dlaczego | Cena |
|---|---|---|
| Oscyloskop USB/ręczny (FNIRSI/Hantek, 2 kanały; nie potrzebujesz pasma ≥40 MHz — 10 wystarczy) | zobacz przebieg na bramce i na piezo; oszczędza dni debugowania drivera | 60–80 |
| ESP32 DevKit ×2 | etap 4 (węzeł za ścianą) | 8 |

**Razem: absolutne minimum ~$210, komfortowo ~$300.** (Jeśli masz już Pi, stację lutowniczą i zasilacz laboratoryjny — odejmij ~$120.)

## Zamówienie (ścieżka krytyczna to wysyłka)

1. Dziś: koszyk 2 z Ali (3–4 tygodnie wysyłki — to ścieżka krytyczna) + oscyloskop.
2. W tym tygodniu: koszyki 1 i 3 lokalnie.
3. Czas wysyłki: `raspi-config` → SPI+I2C, uruchom `software/sweep-map/sweep_map.py --mock` bez sprzętu (kanał syntetyczny — cały potok CSV+wykresy działa na dowolnym komputerze), przeczytaj docs/00–03, obejrzyj wykresy oczekiwane w docs/img oraz schematy w hardware/schematics (budowa etapu 1 opiera się na sch3 i sch2).

## Co zobaczysz (symulator: software/simulator/channel_sim.py → docs/img)

Te pliki PNG to **oczekiwania modelowe**, nie pomiary laboratoryjne. Współczynniki kontaktu, obciążone Q≈40 oraz sprawność łańcucha ≤40% to jawne założenia w `channel_sim.py` — zastąp je danymi z sweep/mocy, gdy stanowisko będzie gotowe.

- `sim0-rig-sketch.png` — całe stanowisko na jednym szkicu (łańcuch etapu 2; etap 1 pomija półmostek i steruje TX słabą sinusoidą z DDS).
- `sim1-sweep-contacts.png` — oczekiwany kształt sweep: wąski pik w okolicach ~40 kHz; model używa smar:sucho:szpara ≈ 1 : 0,25 : 0,02 jako wartości zastępczych. Brak piku — najpierw zdebuguj kontakt lub niedopasowanie pary (sim2).
- `sim2-pair-mismatch.png` — dlaczego 4 przetworniki Langevina, a nie 2: przy Q≈40 niedopasowanie rezonansu 1,5 kHz w parze obniża moc modelowaną ~10×; sweep wybiera najlepszą parę spośród 4.
- `sim3-thickness-comb.png` — na później (tryb B, MHz): płyta jest przezroczysta jako grzebień rezonansów grubościowych, więc częstotliwość musi być śledzona.
- `sim4-power-budget.png` — pobór obciążenia vs **docelowe** pasma mocy odbieranej. Pasmo trybu A (0,5–5 W) to cel etapu 2, jeśli dopasowanie i kontakt współpracują; tryb B to dolne pasmo. Ciągłe Wi-Fi to znacznik obciążenia szczytowego, nie obietnica — duty-cycled ESP32/BLE/LED to realistyczni pierwsi konsumenci.
- `sim5-ook-datarate.png` — etap 3: dlaczego OOK na przetwornikach Langevina wyczerpuje się na ~1–2 kbit/s przy Q≈40 (ring-down τ≈0,3 ms) i dlaczego to wystarczy dla węzła sensorowego.

## Kryteria „stanowisko działa"

Podzielone według etapów — nie oznaczaj etapu 1 jako ukończony liczbami z etapu 2.

**Etap 1 — mapa sweep** ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)):
1. Sweep 25–45 kHz w dwóch kolejnych przebiegach: środek piku odtwarzalny w granicach <200 Hz.
2. Opcjonalny bonus: smar+zacisk vs suchy docisk na tej samej parze (amplitudy względne, nie waty absolutne).

**Etap 2 — pierwsze waty** ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)):
1. Półmostek + transformator dopasowujący włączone; uruchomienie z ograniczeniem prądu zasilacza zgodnie z [docs/02-safety.md](../../docs/02-safety.md) i [hardware/driver/](../../hardware/driver/README.md).
2. Przy rezonansie z etapu 1, ≥0,5 W w znaną rezystancję obciążenia przez 3 mm stali (zmierz V i I po stronie DC za mostkiem RX).
3. LED za płytą świeci z mocy zebranej; zdjęcie + CSV w experiments/002.

Bezpieczeństwo przed pierwszym włączeniem: [docs/02-safety.md](../../docs/02-safety.md) (TVS na odbiorniku, ograniczenie prądu zasilacza na 0,2 A do uruchomienia, żadnych pracy Langevina na wolnym powietrzu przy dużej mocy).
