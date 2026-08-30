# Materiały ściany poza stalą: które ściany przenoszą moc i dane

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · [Deutsch](../../de/docs/06-materials.md) · [Português](../../pt/docs/06-materials.md) · [Español](../../es/docs/06-materials.md) · [Français](../../fr/docs/06-materials.md) · [Italiano](../../it/docs/06-materials.md) · Polski · [Türkçe](../../tr/docs/06-materials.md) · [Українська](../../uk/docs/06-materials.md) · [Tiếng Việt](../../vi/docs/06-materials.md) · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

Resztę tego repozytorium zakłada stal. Ta strona zadaje prostsze, większe pytanie: **dla jakich materiałów ściany kanał dwutransduktorowy w ogóle działa**, i w którym trybie? Jest to badanie symulacyjne (w stylu `--mock`, bez danych laboratoryjnych — intuicja co zasługuje na eksperyment sprzętowy), zbudowane na tym samym modelu półempirycznym co [channel_sim](../../../software/simulator/channel_sim.py) i rozszerzone o absorpcję objętościową.

Generowanie: `python3 software/simulator/material_map.py` (wymaga numpy + matplotlib). Model i założenia: [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## Model w jednej minucie

Trzy wielkości decydują, czy ściana w ogóle jest użyteczna, i dla jakiej mocy:

1. **Kontrast impedancji i faza** — bezstratny model płyty Fabry'ego–Pérota, identyczny jak w [channel_sim](../../../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_wall / Z_couplant, couplant Z = 1.5 MRayl (smar).
   Przy rezonansie półfalowym (f = c/2d) bezstratna symetryczna płyta jest w pełni przezroczysta *niezależnie od r*; kontrast r określa, jak **szerokie** są zęby grzebienia (tolerancja na błąd częstotliwości), prędkość dźwięku c określa, jak są oddalone (Δf = c/2d).
2. **Absorpcja objętościowa**, niewidoczna dla modelu bezstratnego i decydująca dla plastików, betonu i gumy:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, jednokierunkowo, podłużna],
   gdzie α₁ₘₕᶻ jest wartością przy 1 MHz.
   γ ≈ 1 = straty lepkosprężyste/relaksacyjne; γ > 2 = rozpraszanie na niejednorodnościach (kruszywo betonowe).
3. **Dawka, jaką ściana przyjmuje z powrotem** — patrz sekcja [niżej](#dawka-co-fala-robi-ścianie-częstotliwość-po-częstotliwości): naprężenie σ = √(2·I·Z), które *nie zależy* od częstotliwości, oraz nagrzewanie własne ΔT ∝ α(f)·I, które zależy.

**Założenia, sformułowane tam, gdzie kod je podaje:** typowe wartości z podręczników (fala podłużna, ~20 °C); rzeczywiste materiały różnią się — ziarno, wypełniacze, kruszywa, utwardzenie. Wszystko poniżej to ranking, nie karta katalogowa.

| Ściana | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | comb Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | uwaga |
|---|---|---|---|---|---|---|---|---|
| stal | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | drobnoziarnista konstrukcyjna |
| aluminium | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | klasa 6061 |
| tytan | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| miedź | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | gęsta, bardzo wysokie Z |
| szkło borokrzemowe | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | bardzo niskie straty |
| ceramika tlenkowa (alumina) | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | szybki dźwięk, niskie straty |
| PMMA (akryl) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | przezroczysty, limit absorpcyjny przy MHz |
| PVC (sztywny) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | bardziej stratny niż PMMA |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | miękki, stratny |
| beton | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | dominuje rozpraszanie na kruszywie; różnice rzędów wielkości |
| guma (wypełniona) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | uczciwy ślepy zaułek |

## Wykresy

**Tryb B (MHz) — grzebień grubości dla każdego materiału.** Po lewej: metale konstrukcyjne; po prawej: niemetale. Wszystkie ściany 5 mm, sprzężenie przez smar. Piki modelu bezstratnego osiągają T = 1 przy dokładnych rezonansach; rzeczywiste piki są niższe z powodu strat kontaktowych, a absorpcja wręcz ogranicza materiały stratne:

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**Mapa materiałów** — dwie osie, które decydują o wszystkim: impedancja (trudność sprzężenia/kontaktu) vs absorpcja przy 1 MHz (wydajność przy MHz). Wysokie Z + niskie α to róg klasy mocy; niskie Z + wysokie α to „40 kHz nadal otwarte, MHz martwe"; róg gumy to ślepy zaułek przy każdej częstotliwości, którą celujemy:

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Proxy sprzężenia trybu A (40 kHz)** — ten sam model transmisji oceniony przy 40 kHz przez ścianę 3 mm, znormalizowany do stali. *Ranking, nie waty:* rezonansowa para Langevina mnoży każdy słupek w przybliżeniu równo, a model nie uwzględnia obciążenia transduktorów wewnątrz; ten mnożnik to terytorium etapu 2 ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## Co mówi przegląd

- **Przy 40 kHz ściany o niskim Z (plastiki, wykładzina gumowa) sprzęgają się *łatwiej* niż stal** — przez smar są prawie dopasowane impedancyjnie, więc grzebień jest szeroki, a transmisja na przejście wysoka. To, co zabija plastiki przy wyższych częstotliwościach, to **absorpcja objętościowa**, nie kontakt ani impedancja. Drabina materiałów przy 40 kHz jest więc odwrócona względem intuicji: HDPE/PMMA/PVC > szkło/beton > aluminium > alumina > tytan > stal > miedź — z mocnym zastrzeżeniem, że liczba 40 kHz dla gum ekstrapoluje α liniowo w dół z 1 MHz, czego lepkosprężystość nie gwarantuje.
- **Tryb B dzieli materiały czysto.** Metale, szkło i alumina przyjmują MHz z pomijalną absorpcją (α ≤ 0.1 dB/cm); grzebień jest *ostry* dla ścian o wysokim Z (stal, alumina — wymaga śledzenia częstotliwości, lekcja ~6% ⇒ ~10× z [00-theory](00-theory.md)) i *szeroki* dla szkła/PMMA (tolerancyjny, ale PMMA płaci ~1.3 dB jednokierunkowo przy 1 MHz przez 5 mm — tylko klasa mW).
- **Beton to materiał 40 kHz, nie MHz.** Rozpraszanie na kruszywie (λ przy 1 MHz ≈ 3.5 mm ≈ rozmiar kruszywa) podbija γ do ~2.5 i zabija MHz; praktyka prędkości impulsu ultradźwiękowego (40–80 kHz przez ścieżki ≥1 m) to dokładnie tryb A.
- **Nisza obwodów bateryjnych ([05](05-applications-map.md)) jest akustycznie korzystna:** ściana aluminiowa 2–3 mm ma proxy sprzężenia ~3× stali i pomijalną absorpcję — przypadek flagowy jest też przypadkiem łatwym.
- **Drabina częstotliwości do zaplanowania w trybie B** (ściana 5 mm, pierwszy grzebień): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, miedź ≈ 480, stal ≈ 590, tytan ≈ 610, aluminium ≈ 630, szkło ≈ 560, alumina ≈ 990. Cieńsza ściana ⇒ proporcjonalnie wyżej.

## Dawka: co fala robi ścianie, częstotliwość po częstotliwości

Transmisja odpowiada na „ile przechodzi"; ta sekcja odpowiada na odwrotne pytanie — **ile fali zostaje w ścianie, i czy to ją boli?** Szkodzenie fali w ścianie ma dokładnie dwa oblicza:

- **Naprężenie** σ = √(2·I·Z) — pęd fali płaskiej; *niezależne od częstotliwości*. Porównaj z limitem zmęczenia wysokocyklowego (metale), wytrzymałością na zginanie/rozciąganie (ceramika, szkło, beton, guma).
- **Nagrzewanie własne** ΔT = α(f)·I·d²/(8k), stan ustalony, obie powierzchnie chłodzone — *zależne od częstotliwości* przez α(f), i tam częstotliwość gryzie: każdy materiał izolacyjny ma załom, powyżej którego każda dodatkowa oktawa częstotliwości mnoży odkładane ciepło.

Przy 1 W/cm² (już powyżej tego, co celuje ten projekt: cel etapu 2 to 0.5–5 W rozłożone na ~19 cm² powierzchni transduktora, czyli 0.03–0.26 W/cm²):

| Ściana | σ @1 W/cm², MPa | limit σ_e, MPa | margines naprężenia | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | sufit @40 kHz, W/cm² | sufit @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| stal | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| aluminium | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| tytan | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| miedź | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| szkło borokrzemowe | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| ceramika tlenkowa (alumina) | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (akryl) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (sztywny) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| beton | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| guma (wypełniona) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

„Sufit" = ciągłe natężenie, przy którym ściana pozostaje w granicach 20% swojego limitu zmęczenia/wytrzymałości i poniżej +20 K nagrzewania własnego (stan ustalony, obie powierzchnie utrzymywane w temperaturze otoczenia). Praca cykliczna nagrzewa mniej; ściana zakotwiczona tylko z jednej strony — zwykły przypadek, powietrze z jednej strony — nagrzewa się do 4× bardziej na swobodnej powierzchni. Te liczby są pierwszym podejściem, nie gwarancją projektową. Jedna uwaga konwencyjna: wartości α to dB intensywności (10·log₁₀, konwencja dozymetryczna — spadek 3 dB halwuje I); literatura NDT pulse-echo podająca dB amplitudy (20·log₁₀) opisuje TO SAMO α liczbami dwukrotnie większymi — sprawdź, której konwencji używa źródło, zanim skopiujesz jego liczby do tej tabeli.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

Co mówi przegląd dawek:

- **Werdykt dla stali z [00-theory](00-theory.md) obowiązuje i uogólnia się**: każdy metal konstrukcyjny przenosi 1 W/cm² z marginesami 65–680× w naprężeniu i mikrokelwinami nagrzewania własnego. Metale są niewrażliwe na częstotliwość w sensie szkód — ich straty są zbyt małe, by nagrzać przy każdej mocy, którą możemy sprzężyć.
- **Szkody częstotliwościowe na polimerach są termiczne, nie mechaniczne.** Margines naprężenia PMMA to wygodne 60× nawet przy 1 W/cm², ale załom grzania leży tuż przy 1 MHz: łagodne (~0.2 K) przy 40 kHz, +9.5 K przy 1 MHz, +65 K przy 5 MHz — terytorium zmiękczania przy kilku W/cm². PVC przekracza linię +10 K już przy ~0.35 W/cm² @ 1 MHz; guma absorbuje ~288 K na W·cm⁻² przy 1 MHz (i ~12 K nawet przy 40 kHz) — grzanie histerezowe jest *głównym* powodem, dla którego ściany wyłożone elastomerem umierają, nie grzebień. HDPE dzieli różnicę i pamięta swój punkt topnienia: +215 K na W·cm⁻² przy 5 MHz.
- **Ciasny margines betonu jest rozciągający, nie termiczny**: 0.40 MPa naprężenia fali wobec ~2.5 MPa statycznej wytrzymałości na rozciąganie (zmęczenie jeszcze niższe) zostawia tylko ~6× margines przy 1 W/cm². Reżim 40–80 kHz pozostaje w porządku przy gęstości mocy projektu; skupione wiązki multi-W/cm² w beton należy unikać, MHz tym bardziej (rozpraszanie nagrzewa granice kruszywa).
- **Konkluzja dla mapy drogowej:** przy gęstościach mocy trybu A (≤0.3 W/cm²) żaden materiał w tabeli nie jest zagrożony — marginesy naprężenia ≥11× (najciaśniejsze to zmęczenie rozciągające betonu przy 11×; wszystko inne ≥15×) i nagrzewanie ≤0.2 K dla każdego materiału inżynieryjnego (guma, wyjątek, którego nikt nie celuje, ~3.5 K). Mapa szkód uzasadnia plan projektu eskalacji mocy: pierwsze rzeczywiste limity materiałowe pojawiają się *powyżej* celów etapu 2, najpierw w cieczach (kawitacja, reguła ≤1 W/cm² z [00-theory](00-theory.md)), potem w zmęczeniu rozciągającym betonu, potem w polimerach przy MHz. Części, które faktycznie wymagają obserwacji przy wysokiej mocy, to ceramika piezoelektryczna i linia spoiny — [02-safety](02-safety.md) — nie ściana.

## Werdykt dla każdego materiału

| Ściana | Tryb A — moc 40 kHz | Tryb B — moc/dane MHz | Werdykt |
|---|---|---|---|
| stal | ✓✓ odniesienie | ✓ ostry grzebień — śledź częstotliwość | linia bazowa |
| aluminium | ✓✓ (proxy ~3× stal) | ✓ dość ostry grzebień | najlepsza ściana konstrukcyjna (baterie!) |
| tytan | ✓✓ | ✓ dość ostry, niskie straty | nisze korozyjne/gorące, drony, kadłuby |
| miedź | ✓ (najtrudniejsze sprzężenie z metali) | ✓ | nisza: szczelne szyny zbiorcze/ogniska elektrochemiczne |
| szkło borokrzemowe | ✓✓ | ✓ najszerszy grzebień — najbardziej wyrozumiały | okna laboratoryjne, wizjery |
| ceramika tlenkowa (alumina) | ✓✓ | ✓ najszybsze grzebienie (990 kHz @ 5 mm), niskie straty | gorące/izolujące ściany procesowe |
| PMMA | ✓ szerokopasmowo | ⚠ klasa mW ≤ ~0.5 MHz tylko | zbiorniki, obudowy; nie ściana mocy przy MHz |
| PVC / HDPE | ✓ cienkie ściany | ✗ absorpcja | obudowy niskiej klasy, węzły z małymi danymi |
| beton | ✓ 40–80 kHz (praktyka UPV) | ✗ rozpraszanie | fundamenty, rury — tylko tryb A |
| guma (wypełniona) | ⚠ ekstrapolacja modelu niezweryfikowana | ✗ | empirycznie ślepy zaułek — [04](04-hybrid-channels.md) |

Ściana z plastiku o niskim Z ma więcej zapasu na łącza trybu A *tolerancyjne na niedokładność ustawienia*, ale daje mniej bezwzględnego zapasu mocy wobec absorpcji, gdy przekroczysz ~200 kHz; zmierz, zanim cokolwiek obiecujesz.

## Beton z zbrojeniem — przypadek wielowarstwowy

Prawdziwy beton nigdy nie jest czysty: maty zbrojeniowe leżą na głębokości otulenia, a powyższy model 1D pojedynczej płyty ich nie widzi. `chart_rebar` / `rebar_table` rozszerzają model na ogólne stosy ([`stack_transmission`](../../../software/simulator/material_map.py), dokładna rekurencja wielowarstwowa z absorpcją warstwy, zabezpieczona w self-check). Modelowana geometria: ściana konstrukcyjna 150 mm, jedna mata stalowa o grubości równoważnej płaskiej Ø16 mm na otuleniu 40 mm; model *płaski* jest przypadkiem najgorszym — prawdziwy pręt zacienia tylko część wiązki, którą przecina, więc traktuj to jako spadki obwiedni, nie przewidywania:

| Stos (150 mm betonu) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| czysty 150 mm | 0.135 | 0.133 | 8.9e-09 |
| zbrojenie Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| dwie maty Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

Co mówi model stosu:

- **Jedna mata płaska pod wiązką kosztuje ×10 przy dokładnie 40 kHz** (interferencja pasma zatrzymującego od warstwy stalowej), ale spadek jest wąski: przy 100 kHz ten sam stos traci tylko ×2. Praktyczny odczyt dla niszy rurociągów/autoklawów: *skan częstotliwości wokół 40–120 kHz, nie stała częstotliwość*, to co przeprowadza łącze trybu A przez zbrojenie — a spadki przesuwają się z głębokością otulenia, więc skan także identyfikuje geometrię (podstawa estymacji głębokości zbrojenia).
- **Druga mata (siatka) jest blisko zabójcy ściany w tym przypadku najgorszym** (×45 w dół i płasko-broadbandowo w pobliżu 40–100 kHz): gęste zbrojenie na ścieżce to uczciwy wskaźnik „wybierz inne miejsce na ścianie", nie problem przetwarzania sygnału.
- **Tryb B przez beton konstrukcyjny jest martwy z zbrojeniem lub bez** (poziom 1e-8 przy 1 MHz: 5 dB/cm × 15 cm). Zbrojenie w ogóle nie wchodzi do historii przy MHz.
- Zastrzeżenia, w kolejności ważności: założenie warstwy płaskiej (przypadek najgorszy — pręt Ø16 blokuje znacznie mniej niż połowę przekroju wiązki 40–50 mm), założenie fali równoległej do osi zbrojenia, oraz propagacja 1D (brak dyfrakcji wokół pręta). Właściwy eksperyment sprzętowy to skaner na prawdziwej płycie: mapuj T(x, y) przy 40/80/120 kHz nad siatką zbrojenia i dopasuj pozycje spadków modelu płaskiego do skoku siatki.

## Co powinien zmierzyć eksperyment sprzętowy

Przed zaufaniem jakiejkolwiek konkretnej płycie: metoda dwóch grubości dla każdego materiału (dwie płyty o grubości d i 2d przy tym samym kontakcie), aby wydobyć rzeczywiste α(f) i c — ten jeden zbiór danych zastępuje każdy wiersz powyższej tabeli. Naturalne dodatkowe przebiegi w ramach istniejących protokołów: powtórz eksperyment [001](../experiments/001-sweep-map-3mm-steel/README.md) skan na płycie PMMA 5 mm, płycie borokrzemowej lub 99% aluminy, oraz bloku betonu znanej klasy; spodziewaj się *niższego ale szerszego* piku dla plastików, ostrego grzebienia dla ceramiki, oraz wrażliwego na temperaturę kontaktu wszędzie. Podczas eksperymentu [002](../experiments/002-watts-3mm-steel/README.md) przebiegu mocy, przypnij termometr IR (lub cienki termoparę) do dalszej powierzchni każdego typu ściany — zmierzone ΔT przy znanym wejściu to jedna liczba, która waliduje lub zabija kolumnę grzania tabeli dawek. Nic na tej stronie nie jest zmierzone — to mapa tego, co zmierzyć najpierw.
