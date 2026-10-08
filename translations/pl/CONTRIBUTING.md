# Jak współtworzyć projekt

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · Polski · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Dziękujemy, że chcesz rozwijać otwarty kanał przez stal. Poniższe trzy zasady to nie biurokracja — to patentowy pancerz projektu (zobacz [LICENSES.md](LICENSES.md), by dowiedzieć się dlaczego).

## 1. Licencje wkładów (przychodzące = wychodzące)

Przesyłając wkład, zgadzasz się, że jest on licencjonowany tak samo jak pozostałe materiały w jego katalogu:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Przyznanie licencji patentowej.** Dodatkowo — ponieważ CC-BY-4.0 nie licencjonuje patentów — przyznajesz projektowi oraz wszystkim odbiorcom jego materiałów wieczystą, nieodwołalną, obejmującą cały świat, wolną od opłat, niewyłączną licencję patentową na wytwarzanie, zlecanie wytwarzania, używanie, oferowanie do sprzedaży, sprzedawanie, importowanie i w inny sposób przekazywanie Twojego wkładu, zarówno samodzielnie, jak i w ramach projektu — w zakresie tych roszczeń patentowych, które są niezbędnie naruszane przez sam wkład lub przez jego połączenie z projektem, do którego został przesłany. Warunki te są zgodne z §3 licencji Apache-2.0, niezależnie od tego, w którym katalogu wylądował wkład. Jeśli wytoczysz proces patentowy przeciwko komukolwiek (w tym jako powód wzajemny) twierdząc, że materiały projektu naruszają Twój patent, to wszystkie **patentowe** licencje przyznane Tobie przez projekt i jego współtwórców na mocy tego punktu oraz na mocy licencji projektu wygasają z dniem wytoczenia takiego procesu.

## 2. DCO: podpis pochodzenia

Każdy commit nosi sign-off (`git commit -s`), co oznacza zgodę z [Developer Certificate of Origin 1.1](https://developercertificate.org/): potwierdzasz, że masz prawo przesłać ten wkład na licencji projektu.

```
Signed-off-by: Imię Nazwisko <email@example.com>
```

PR-y bez sign-off nie są scalane; sprawdzanie jest automatyczne — zadanie CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) odrzuca PR, jeśli choć jeden commit nie ma sign-off. Ochrona patentowa warstwy docs opiera się dokładnie na tym łańcuchu — bez wyjątków.

**Przenoszenie materiałów między warstwami.** Materiał żyje w warstwie, w której wylądował (i pod licencją tej warstwy). Przenoszenie tekstu/kodu między warstwami o różnych licencjach jest dozwolone tylko wtedy, gdy jest to Twój własny materiał, lub z wyraźną adnotacją o pierwotnej licencji fragmentu.

## 3. Higiena patentowa i protokół eksperymentów

- Każda decyzja techniczna musi dawać się wywieść z wolnego źródła — wygasłego patentu lub publikacji z [docs/01-prior-art.md](docs/01-prior-art.md). Implementacje aktywnych roszczeń (wymienionych tamże) nie są przyjmowane, dopóki te roszczenia nie wygasną.
- Wyniki eksperymentalne — wyłącznie przez szablon [experiments/TEMPLATE.md](experiments/TEMPLATE.md): opatrzony datą, odtwarzalny protokół to dokładnie to, co stanowi nasz stan techniki.
- Decyzje architektoniczne przechodzą przez ADR-y w [docs/decisions/](docs/decisions/).
- Komentarze w kodzie, docstringi, identyfikatory i komunikaty commitów są wyłącznie po angielsku. Dokumentacja jest wielojęzyczna (patrz niżej); etykiety widoczne dla użytkownika na rysunkach żyją w `labels.json`.

## 4. Dokumentacja wielojęzyczna: edytujesz jeden język, CI synchronizuje resztę

Angielski jest językiem głównym i posiada ścieżki kanoniczne. Każdy inny język to drzewo lustrzane pod [translations/](..) o identycznych nazwach plików — markdown, CSV BOM-u i generowane rysunki włącznie; tekst na rysunkach jest sterowany przez `labels.json`. Nie musisz utrzymywać kopii lustrzanych ręcznie:

- Edytuj w języku, który jest dla Ciebie wygodny. Przy pushu, workflow [Translation sync](../../.github/workflows/translate.yml) tłumaczy odpowiedniki za pomocą modelu LLM o otwartych wagach (`glm-5.2` na Ollama Cloud), regeneruje rysunki, gdy synchronizacja aktualizuje `labels.json`, i commituje wynik z markerem `[translate-sync]`. Działa każdy endpoint zgodny z OpenAI — ustaw `OPENAI_BASE_URL` i `TRANSLATE_MODEL`.
- To, co wciąż wymaga pracy, jest śledzone w `translations/.sync-state.json`, który zapisuje treść główną, z której wykonano każde tłumaczenie. Przebieg ucięty przez limit lub timeout nie traci więc niczego: niedokończone pary pozostają oznaczone jako nieaktualne i są podjęte przez następny push lub przez nocny przebieg. Nie edytuj tego pliku ręcznie.
- Jeśli edytowałeś **kilka** języków dokumentu samodzielnie, każda wersja, której dotknąłeś, zostaje zachowana tak, jak ją napisałeś; bot wypełnia tylko języki, których nie dotknąłeś.
- **`labels.json` jest wyjątkiem od zasady „edytuj dowolny język".** Etykiety na rysunkach płyną tylko w kierunku główny → kopie lustrzane. Edycja przetłumaczonej etykiety poprawia ten język i na tym się kończy; nie wraca do angielskiego. Aby zmienić, co etykieta *mówi*, edytuj sekcję główną. Powodem jest asymetria: edycja etykiety to niemal zawsze korekta maszynowego sformułowania, a pozwolenie, by to przepisało treść główną, przedefiniowałoby źródło, z którego generowane jest czternaście kopii lustrzanych. Klucze, których bot nigdy nie wyprodukował, nadal propagują się wstecz, więc ręcznie dodana etykieta nie utyka w jednym języku.
- Tłumaczenie maszynowe jest commitowane — przejrzyj commit bota i popraw sformułowanie, jeśli uchybi tonowi; Twoja poprawka nie zostanie nadpisana (bot zapisuje Twoją wersję jako bieżącą).
- Odpowiedź, która wróciła ucięta lub ze zepsutymi placeholderami `labels.json`, jest odrzucana zamiast commitowana, a para jest ponawiana — więc dziwna luka w kopii lustrzanej to nieaktualna para, a nie decyzja.
- **Zewnętrzne PR-y:** bot działa na `master`, więc PR może zmienić tylko jeden język — kopie lustrzane (w tym angielska) nadgonią automatycznie zaraz po scaleniu. Nie musisz znać angielskiego, aby współtworzyć dokumentację.
- **Dodawanie języka:** dodaj jego kod i nazwę do [i18n.json](../../i18n.json) (np. `"fr": "Français"`) i zrób push — pipeline buduje całe drzewo `translations/fr/`: każdy dokument, sekcję `fr` w każdym `labels.json`, zestaw rysunków i przełączniki języków wszędzie.
- **Skrypty niełacińskie:** CI instaluje rodziny Noto (`fonts-noto-core`, `fonts-noto-cjk`), a renderery przechodzą przez stos fontów w `i18n.json` → `render.fonts`, więc cyrylica, Han, kana i Hangul wychodzą poprawnie. Renderer sprawdza teraz pokrycie glifów przed rysowaniem i **kończy się błędem zamiast malować pola `.notdef`** — ten test istnieje, ponieważ chińskie rysunki wyszły kiedyś jako kratka z tofu, a nic w CI nie patrzy na piksele. Jeśli się uruchomi, dodaj krój Noto dla tego skryptu do stosu.
- **Skrypty wymagające kształtowania kontekstowego** — arabski i perski (RTL, formy łączone), dewanagari i bengalski (zbitki) — nie mogą być narysowane poprawnie przez matplotlib, który nie ma silnika kształtowania: nawet z właściwym fontem glify wychodzą niepołączone i w złym porządku. Wymień te języki w `i18n.json` → `render.skip_figures`. Ich proza jest nienaruszona; ich dokumentacja po prostu linkuje do rysunków głównych, na co naprawa linków w [tools/translate_sync.py](../../tools/translate_sync.py) wskazuje automatycznie. `hi` jest skonfigurowane w ten sposób.
- **Strażnik skryptu:** `SCRIPTS` w [tools/i18n_render.py](../../tools/i18n_render.py) zapisuje, jakiego skryptu etykiety każdego języku muszą zawierać. Odpowiedź, która nie ma żadnego z niego — sekcje `ja` wyszły kiedyś wypełnione rosyjskim — jest odrzucana i ponawiana zamiast commitowana. Język nieobecny w tej tabeli po prostu nie dostaje straży, więc dodanie go do `i18n.json` niczego nie psuje; dodaj wpis, aby uzyskać sprawdzanie.

## 5. Sprawdzenia, które możesz uruchomić przed pushem

```bash
python tools/check_repo.py
```

Weryfikuje to, co bot tłumaczący jest w stanie zepsuć, a nic innego by nie złapało: każdy link względny rozwiązuje się, każda sekcja `labels.json` pasuje do `i18n.json` i niesie te same klucze oraz te same placeholdery `str.format` co sekcja główna, każdy dokument kanoniczny ma kopię lustrzaną w każdym języku, a każdy plik markdown ma swój pasek języków. CI uruchamia to na obu workflow; nie wymaga zależności.

Reszta CI ([ci.yml](../../.github/workflows/ci.yml)) kompiluje skrypty i uruchamia cały pipeline rysunków. Aby odtworzyć go dokładnie — włącznie z commitowanymi rysunkami — zainstaluj przypięty łańcuch narzędzi, a nie luźny:

```bash
python -m pip install -r tools/requirements-ci.txt
```
