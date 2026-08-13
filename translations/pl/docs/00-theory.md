# Teoria kanału (minimum, by zacząć pracę)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · [Português](../../pt/docs/00-theory.md) · [Español](../../es/docs/00-theory.md) · [Français](../../fr/docs/00-theory.md) · [Italiano](../../it/docs/00-theory.md) · Polski · [Türkçe](../../tr/docs/00-theory.md) · [Українська](../../uk/docs/00-theory.md) · [Tiếng Việt](../../vi/docs/00-theory.md) · [中文](../../zh/docs/00-theory.md) · [日本語](../../ja/docs/00-theory.md) · [한국어](../../ko/docs/00-theory.md) · [हिन्दी](../../hi/docs/00-theory.md)

## Zasada działania
Element piezoelektryczny TX dociskany/klejony do ściany wzbudza w niej falę podłużną; piezoelektryczny RX po drugiej stronie zamienia ją z powrotem na prąd. Ściana jest rezonatorem: przy rezonansach grubościowych (wielokrotnościach półfalowej długości fali) transmisja osiąga maksimum.

## Liczby kluczowe
Prędkość dźwięku podłużnego w stali: ~5900 m/s.

| Grubość stali | Rezonans półfalowy |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Długość fali w stali: 148 mm @ 40 kHz; 5,9 mm @ 1 MHz.

## Dwa tryby
- **A (40 kHz, przetworniki Langevina).** Płyta 3–5 mm ≪ λ — zachowuje się jak membrana; rezonans wyznacza para przetworników, a nie ściana. Prostszy i mocniejszy niż tryb B — ten, od którego warto zacząć. Dowód istnienia z laboratorium (nie cel garażowy): NASA JPL ~24,5 kHz, setki W do kW przez 5 mm Ti przy użyciu specjalnie zbudowanego sprzętu.
- **B (0,6–1 MHz, dyski).** Rezonans grubościowy samej ściany, i to ostry (przesunięcie częstotliwości ~6% ⇒ spadek transmisji ~10× w modelu Fabry'ego–Perota). Klasa wyników RPI/Moss: setki mW plus dane z prędkością setek kbit/s przy laboratoryjnym klejeniu i dopasowaniu. Wymaga automatycznego śledzenia częstotliwości.

## Główne straty
Niedopasowanie rezonansowe w obrębie pary przetworników (tanie przetworniki Langevina mają rozrzut ±1 kHz), jakość kontaktu akustycznego (epoksyd > gruby smar sprzęgający + docisk > suchy nacisk), brak współosiowości, dryf rezonansu z temperaturą. Odpowiedź na to wszystko jest ta sama: wykonaj mapę skanu przed każdą zmianą konfiguracji.

## Wpływ na ścianę i ośrodek za nią

Wersja krótka: przy mocach platformy ściana i jakikolwiek gaz za nią pozostają nietknięte. Ciecz za ścianą wpływa głównie *na kanał*; kanał zaczyna wpływać *na ciecz* dopiero w pobliżu progu kawitacji. Liczby orientacyjne poniżej dotyczą trybu A: 40 kHz, ~1 W/cm² w stal 3 mm.

**Ściana — żadna odkształcenia, żadna zmęczenia, nigdy.** Prędkość cząstek v = √(2I/ρc) ≈ 21 mm/s ⇒ przemieszczenie ≈ 80 nm, odkształcenie fali płaskiej ε = v/c ≈ 3,5·10⁻⁶. Dwa równoważne oszacowania naprężeń: sprężyste E·ε ≈ 0,7 MPa (E ≈ 200 GPa) oraz akustyczne p = Z·v ≈ 1,0 MPa (Z_stali ≈ 4,6·10⁷ Pa·s/m). Stal plastyzuje przy 250+ MPa, a jej granica zmęczeniowa to ~200 MPa — wciąż margines >200× w obu wypadkach, a poniżej granicy zmęczeniowej stal znosi nieograniczoną liczbę cykli. Mechanicznie delikatne części są gdzie indziej: ceramika piezoelektryczna (krucha, traci polaryzację przy przegrzaniu) oraz spoina (epoksyd nagrzewa się i zmęcza jako pierwszy) — patrz [02-safety](../../../docs/02-safety.md).

**Gaz za ścianą — zerowy wpływ.** Niedopasowanie impedancji stal→powietrze (~4,6·10⁷ vs ~400 Pa·s/m) transmituje ułamek rzędu 10⁻⁵ mocy. Brak mierzalnego nagrzewania lub ruchu; elektronika wewnątrz szczelnej obudowy nie zauważa ruchu ściany rzędu nm.

**Ciecz za ścianą — dwa kierunki:**

- *Ciecz → kanał (zawsze).* Woda obciąża powierzchnię zewnętrzną ~1,5 MRayl zamiast powietrza: część mocy promieniuje do cieczy, Q spada, pik skanu się przesuwa i poszerza. Tryb B jest najbardziej uderzony — grzebień rezonansu grubościowego jest liczony dla granic stal–powietrze i przesuwa się przy obciążeniu cieczą. Obecna zasada to obejmuje: **skanuj ponownie przy prawdziwym, pełnym naczyniu**, nigdy nie ufaj skanowi wykonanemu przy pustym. Dodatkowa korzyść: tłumienie przez ciecz skraca dzwonienie rezonatora (τ), więc „oko” OOK otwiera się przy wyższych przepływnościach bitowych. Bąbelki na drodze (fermentująca ciecz!) silnie rozpraszają — patrz obejście w [04-hybrid-channels](../../../docs/04-hybrid-channels.md).
- *Kanał → ciecz (tylko przy dużej mocy).* Szczytowe ciśnienie promieniowane do wody: p ≈ ρc·v ≈ 1,5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0,3 atm. Próg kawitacji bezwładnościowej przy 40 kHz w zwykłej (nasyconej gazem) wodzie to ~1–2 atm, więc przy 1 W/cm² margines wynosi 3–10×. Ale p rośnie jak √mocy, a fale stojące w zamkniętym naczyniu tworzą lokalne punkty gorące — dziesiątki W/cm² ciągłego wpływu do naczynia wypełnionego cieczą mogą osiągnąć próg. Przekroczenie go oznacza odgazowanie CO₂, sonochemię (obce posmaki w produktach spożywczych) i długotrwałą erozję kawitacyjną wewnętrznej powierzchni (dokładnie tak, jak czyszczą ultradźwiękowe myjki). Praktyczny sufit mocy ciągłej w ściany z cieczą z tyłu: **≲1 W/cm²**. Tryb B jest wyjęty: przy MHz próg jest o rząd wielkości wyższy, a moce to setki mW.

## Budżet mocy odbiornika (orientacyjnie)
LED 20 mW; ESP32 w trybie cyklicznym 1–5 mW średnio; radio BLE ~150 mW podczas pracy radia. Bufor: superkondensator 1 F @ 3,3 V magazynuje E = ½CV² = 5,4 J. Ile transmisji to daje, zależy od czasu w eterze: krótkie zdarzenie reklamowe BLE (~2–5 ms przy ~150 mW) to tylko ~0,3–0,8 mJ → rzędu **10⁴ pakietów** z pełnego kondensatora; długie połączenie / seria (~100 ms pracy radia) to ~15 mJ → rzędu **10² serii**. Średni pobór nadal musi mieścić się w zbieranych watach (cel etapu 2: ≥0,5 W w obciążeniu to bramka; dopóki to nie zostanie zmierzone, traktuj pasma trybu A o mocy kilku watów na wykresach symulatora jako cele, a nie dane).
