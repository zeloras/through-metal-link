# Licencjonowanie i ochrona patentowa

> [English (primary)](../../LICENSES.md) · [Русский](../ru/LICENSES.md) · [Deutsch](../de/LICENSES.md) · [Português](../pt/LICENSES.md) · [Español](../es/LICENSES.md) · [Français](../fr/LICENSES.md) · [Italiano](../it/LICENSES.md) · Polski · [Türkçe](../tr/LICENSES.md) · [Українська](../uk/LICENSES.md) · [Tiếng Việt](../vi/LICENSES.md) · [中文](../zh/LICENSES.md) · [日本語](../ja/LICENSES.md) · [한국어](../ko/LICENSES.md) · [हिन्दी](../hi/LICENSES.md)

Cel tego schematu: projekt jest w pełni otwarty, każdy może go forknąć i na nim budować (również komercyjnie), a ryzyko sporu patentowego jest zredukowane do absolutnego minimum osiągalnego środkami prawnymi i proceduralnymi.

## Schemat (trzy warstwy; pełne teksty w [LICENSES/](../../LICENSES))

| Obszar | Licencja | Tekst | Postanowienia patentowe |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](../../LICENSES/Apache-2.0.txt) | §3: każdy współtwórca automatycznie udziela licencji patentowej na swój wkład; złóż pozew patentowy i tracisz licencję **patentową** (odwet; licencja autorska z §2 jest nieodwołalna i przetrwa pozew) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](../../LICENSES/CERN-OHL-W-2.0.txt) | §7.1: licencja patentowa (Make / have Made / use / sell / import…) od każdego licencjodawcy — ale tylko dla roszczeń koniecznie naruszanych przez dany Covered Source; §7.2: pozew patentowy (w tym próba unieważnienia cudzego patentu) kończy **wszystkie** prawa z licencji |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](../../LICENSES/CC-BY-4.0.txt) | nie udziela **żadnych** praw patentowych (§2(b)(2)) — luka jest zamykana przez wyraźne nadanie patentowe w [CONTRIBUTING.md](../../CONTRIBUTING.md) |
| cała reszta (główny `README.md`, `QUICKSTART.md`, ten plik, `data/` itd.) | CC-BY-4.0 | — | fallback: żaden plik w repozytorium nie zostaje „all rights reserved" |

Pliki kodu noszą nagłówki SPDX (Apache-2.0); czytelna maszynowo mapa pokrycia to [REUSE.toml](../../REUSE.toml). Linia copyright znajduje się w [NOTICE](../../NOTICE); główny [LICENSE](../../LICENSE) jest wskaźnikiem do tego schematu.

**Dlaczego CERN-OHL-W, a nie S ani P.** W to środek drogi: projekt i jego modyfikacje muszą pozostać otwarte przy każdej dystrybucji, ale produkt, w który projekt jest wbudowany, może być komercyjny i własnościowy — to zostawia otwarte nisze z docs/05 (laboratoria, browary, pakiety baterii). S (silny copyleft) zamknąłby drzwi do osadzania; P (permisywny) pozwoliłby na zamknięte forki. Zaostrzenie w stronę S jest wbudowane w samą licencję: §8.3 pozwala każdemu traktować materiał na licencji W jak na licencji S (jeśli spełniony jest warunek Available Components) — bez pozwolenia. Złagodzenie (w stronę P lub innej licencji) jest natomiast możliwe tylko wtedy, gdy cały materiał należy do jednego autora; po pierwszym zewnętrznym wkładzie — wyłącznie za zgodą każdego współtwórcy.

**Nazwa projektu.** „through-metal-link" nie jest zarejestrowanym znakiem towarowym; same licencje nie przyznają żadnych praw do nazwy (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Faktyczne odwołanie się do projektu („based on through-metal-link") jest darmowe dla każdego; forki z niekompatybilnymi zmianami proszone są o wydanie pod własną nazwą.

## Przed czym to chroni — a przed czym nie (szczzerze)

**Chroni przed:**
1. **Pozwami od współtwórców.** Każdy, kto coś wniósł, automatycznie udzielił licencji na swoje prawa patentowe z tego wkładu (Apache §3, CERN-OHL §7.1 oraz CONTRIBUTING dla docs). Pozew kosztuje powoda drogo: w Apache-2.0 traci licencje patentowe do kodu; w CERN-OHL-W traci wszystkie prawa do warstwy sprzętowej w całości (§7.2 — uruchamiany nawet próbą podważenia cudzego patentu).
2. ** Prywatyzacją forków sprzętowych.** CERN-OHL-W zobowiązuje każdego, kto dystrybuuje (Conveyance produktu lub źródeł), do publikacji swoich modyfikacji projektu — ulepszenia wracają do otwartej warstwy i same stają się stanem techniki. (Fork szufladowy, nigdy nie przekazany stronom trzecim, nie ma obowiązku publikacji — tak jak w każdym copylefcie.)
3. **Cudzymi *przyszłymi* patentami.** Wszystko opublikowane z datą niszczy nowość dla późniejszych zgłoszeń: dla rozwiązania opisanego tu przed ich datą zgłoszenia nie można już uzyskać ważnego patentu. Przeciw zgłoszonym *przed* naszą publikacją to nie działa — dla nich jedyną tarczą jest warstwa wygasłych patentów (patrz niżej).

**Nie chroni przed:**
- **Istniejącymi patentami stron trzecich.** Żadna licencja tego nie potrafi. Działa przeciwko nim dyscyplina inżynierska z docs/01-prior-art.md: buduj tylko z warstwy wygasłej (public domain), nie implementuj żywych roszczeń wymienionych tam (RPI, Drexel oraz rodziny Navy/ABB/Ultrapower dodane w 2026-08 — zwróć uwagę, że nie wszystkie są tylko z USA i nie wszystkie wygasają około 2032) i wywodź każdą decyzję projektową z wolnego źródła. To nie gwarancja, ale to właśnie praktyka, która czyni pozew bezcelowym.
- Fork zmierzający do produkcji komercyjnej robi własną analizę FTO (freedom to operate) dla swojej jurysdykcji i swojego projektu — repozytorium nie składa żadnych oświadczeń patentowych (zastrzeżenia we wszystkich trzech licencjach).

## Protokół publikacji defensywnej (wykonać, gdy repo wejdzie publicznie)

Każdy opublikowany wynik to opatentowany stan techniki z datą, który blokuje wszystkie późniejsze zgłoszenia stron trzecich na to samo rozwiązanie:

1. Otworzyć repozytorium z pełną historią git (commity = znaczki czasowe).
2. Snapshot do **Zenodo** → DOI: niezależne archiwum z prawnie istotną datą, cytowalne w publikacjach.
3. Zapinować w **Software Heritage** (archive.softwareheritage.org — wieczne lustro).
4. Każdy ukończony eksperyment `experiments/NNN` — z datą, liczbami i wykresami: to jest publikacja konkretnego rozwiązania technicznego.
5. Główne kamienie milowe (pierwsze waty, pierwszy węzeł) — opis wypuszczony w świat (Hackaday.io / arXiv / blog): im szerszy rozgłos, tym silniejszy status prior art.

## Dla współtwórców

Reguły znajdują się w [CONTRIBUTING.md](../../CONTRIBUTING.md): DCO sign-off, inbound=outbound, wyraźne nadanie patentowe na każdy wkład niezależnie od katalogu, możliwość wywiedzenia decyzji projektowych z wolnego stanu techniki.

Do czasu otwarcia repozytorium pozostaje prywatne — publikacja przed pierwszymi odtwarzalnymi wynikami osłabiłaby zarówno pozycję naukową, jak i patentową.
