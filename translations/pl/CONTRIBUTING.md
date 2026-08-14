# Jak współtworzyć projekt

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · Polski · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Dziękujemy za chęć rozwoju otwartego kanału przez stal. Poniższe trzy zasady to nie biurokracja — to patentowa zbroja projektu (zobacz [LICENSES.md](LICENSES.md), aby dowiedzieć się dlaczego).

## 1. Licencje wkładu (przychodzący = wychodzący)

Przesyłając wkład, wyrażasz zgodę na to, że jest on licencjonowany w ten sam sposób, co pozostałe materiały w jego katalogu:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Udzielenie licencji patentowej.** Dodatkowo — ponieważ licencja CC-BY-4.0 nie obejmuje patentów — udzielasz projektowi oraz wszystkim odbiorcom jego materiałów wieczystej, nieodwołalnej, obejmującej cały świat, wolnej od opłat licencyjnych, niewyłącznej licencji patentowej na wytwarzanie, zlecanie wytwarzania, używanie, oferowanie do sprzedaży, sprzedawanie, importowanie i w inny sposób przekazywanie Twojego wkładu, zarówno samodzielnie, jak i w ramach projektu — w zakresie tych Twoich roszczeń patentowych, które są koniecznie naruszane przez wkład sam w sobie lub przez jego połączenie z projektem, do którego został przesłany. Warunki te są zgodne z §3 licencji Apache-2.0, niezależnie od tego, w którym katalogu trafił wkład. Jeśli wszczniesz postępowanie sądowe w sprawie patentowej przeciwko komukolwiek (w tym w drodze kontrpozwu) twierdząc, że materiały projektu naruszają Twój patent, to wszystkie licencje **patentowe** udzielone Ci przez projekt i jego współtwórców na mocy tego punktu oraz licencji projektu wygasają z dniem wniesienia takiego postępowania.

## 2. DCO: podpis pochodzenia

Signed-off-by: Firstname Lastname <email@example.com>
```

PR-y bez sign-off nie są scalane; sprawdzanie jest automatyczne — zadanie CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) odrzuca PR, nawet jeśli jeden commit nie ma sign-off. Ochrona patentowa warstwy dokumentacji opiera się dokładnie na tym łańcuchu — bez wyjątków.

**Przenoszenie materiałów między warstwami.** Materiał pozostaje w warstwie, w której trafił (i na licencji tej warstwy). Przenoszenie tekstu/kodu między warstwami o różnych licencjach jest dozwolone tylko wtedy, gdy jest to twój własny materiał lub z wyraźną adnotacją o oryginalnej licencji fragmentu.

## 3. Higiena patentowa i protokół eksperymentu

- Każda decyzja techniczna musi znajdować uzasadnienie w wolnym źródle — wygasłym patencie lub publikacji z [docs/01-prior-art.md](docs/01-prior-art.md). Implementacje aktywnych roszczeń patentowych (wymienionych tam również) nie są akceptowane, dopóki te roszczenia nie wygasną.
- Wyniki eksperymentalne — wyłącznie przez szablon [experiments/TEMPLATE.md](experiments/TEMPLATE.md): datowany, odtwarzalny protokół to dokładnie to, co stanowi nasz stan techniki.
- Decyzje architektoniczne przechodzą przez ADR-y w [docs/decisions/](docs/decisions/).
- Komentarze w kodzie, docstringi, identyfikatory i komunikaty commitów są wyłącznie w języku angielskim. Dokumentacja jest wielojęzyczna (patrz niżej); etykiety widoczne dla użytkownika na rysunkach znajdują się w `labels.json`.

## 4. Dokumentacja wielojęzyczna: edytuj jeden język, CI synchronizuje resztę

Język angielski jest podstawowy i posiada ścieżki kanoniczne. Każdy inny język to drzewo lustrzane w [translations/](..) o identycznych nazwach plików — w tym markdown, plik CSV BOM i wygenerowane rysunki; tekst na rysunkach jest sterowany przez `labels.json`. Nie musisz utrzymywać kopii lustrzanych **ręcznie**:

- Edytuj w języku, który jest dla Ciebie wygodny. Przy wypchnięciu (push) przepływ pracy [Translation sync](../../.github/workflows/translate.yml) tłumaczy odpowiedniki za pomocą modelu LLM o otwartych wagach (`glm-5.2` na Ollama Cloud), regeneruje rysunki, gdy synchronizacja aktualizuje `labels.json`, i zatwierdza wynik z powrotem ze znacznikiem `[translate-sync]`. Działa każdy punkt końcowy zgodny z OpenAI — ustaw `OPENAI_BASE_URL` i `TRANSLATE_MODEL`.
- To, co nadal wymaga pracy, jest śledzone w `translations/.sync-state.json`, który rejestruje podstawową treść, z której każde tłumaczenie powstało. Przebieg przerwany przez limit (quota) lub limit czasu nie traci więc niczego: niedokończone pary pozostają oznaczone jako nieaktualne i są podchwytywane przez następne wypchnięcie lub nocny przebieg. Nie edytuj tego pliku ręcznie.
- Jeśli sam edytowałeś **kilka** języków dokumentu, każda wersja, której dotknąłeś, jest zachowana tak, jak ją napisałeś; bot tylko wypełnia języki, których nie dotknąłeś.
- **`labels.json` jest wyjątkiem od zasady "edytuj w dowolnym języku".** Etykiety rysunków przepływają tylko z podstawowego → do kopii lustrzanych. Edycja przetłumaczonej etykiety naprawia ten język i na tym się kończy; nie wraca do języka angielskiego. Aby zmienić to, co etykieta *mówi*, edytuj sekcję podstawową. Powodem jest asymetria: edycja etykiety to prawie zawsze korekta maszynowego sformułowania przez kogoś, a pozwolenie, by to przepisało wersję podstawową, przedefiniowałoby źródło, z którego generowane jest wszystkich czternaście kopii lustrzanych. Klucze, których bot nigdy nie wyprodukował, nadal propagują się wstecz, więc ręcznie napisana etykieta nie utyka w jednym języku.
- Tłumaczenie maszynowe jest zatwierdzane (commit) — przejrzyj zatwierdzenie bota i popraw sformułowanie, jeśli nie trafia w ton; Twoja poprawka nie zostanie nadpisana (bot rejestruje Twoją wersję jako bieżącą).
- Odpowiedź, która wróciła obcięta lub ze zepsutymi symbolami zastępczymi `labels.json`, jest odrzucana, a nie zatwierdzana, i para jest ponawiana — więc dziwnie wyglądająca luka w kopii lustrzanej to nieaktualna para, a nie decyzja.
- **Zewnętrzne PR:** bot działa na `master`, więc PR może zmienić tylko jeden język — kopie lustrzane (w tym angielski) nadganiają automatycznie zaraz po scaleniu. Nie musisz znać angielskiego, aby współtworzyć dokumentację.
- **Dodawanie języka:** dodaj jego kod i nazwę do [i18n.json](../../i18n.json) (np. `"fr": "Français"`) i wypchnij (push) — potok buduje całą kopię lustrzaną `translations/fr/`: każdy dokument, sekcję `fr` w każdym `labels.json`, zestaw rysunków i przełączniki języków wszędzie.
- **Skrypty niełacińskie:** CI instaluje rodziny Noto (`fonts-noto-core`, `fonts-noto-cjk`), a renderery przechodzą przez stos czcionek w `i18n.json` → `render.fonts`, więc cyrylica, Han, kana i hangul wychodzą poprawnie. Renderer sprawdza teraz pokrycie glifów przed rysowaniem i **kończy się błędem, zamiast malować pola `.notdef`** — to sprawdzenie istnieje, ponieważ chińskie rysunki zostały wysłane jako siatka tofu i nic w CI nie patrzy na piksele. Jeśli się uruchomi, dodaj krój Noto dla tego skryptu do stosu.
- **Skrypty wymagające kształtowania kontekstowego** — arabski i perski (RTL, formy łączone), dewanagari i bengalski (ligatury) — nie mogą być poprawnie rysowane przez matplotlib, który nie ma silnika kształtowania: nawet przy odpowiedniej czcionce glify wychodzą niepołączone i w złej kolejności. Wymień te języki w `i18n.json` → `render.skip_figures`. Ich proza nie jest dotknięta; ich dokumenty po prostu linkują do podstawowych rysunków, na które naprawa linków w [tools/translate_sync.py](../../tools/translate_sync.py) wskazuje automatycznie. `hi` jest skonfigurowane w ten sposób.
- **Strażnik skryptu:** `SCRIPTS` w [tools/i18n_render.py](../../tools/i18n_render.py) rejestruje, jaki skrypt muszą zawierać etykiety każdego języka. Odpowiedź, która nie ma go wcale — sekcje `ja` kiedyś zostały wysłane wypełnione rosyjskim — jest odrzucana i ponawiana, zamiast być zatwierdzana. Językowi brakującemu w tej tabeli po prostu nie przypisuje się straży, więc dodanie go do `i18n.json` nigdy niczego nie psuje; dodaj wpis, aby uzyskać sprawdzanie.

## 5. Sprawdzenia, które możesz wykonać przed wysłaniem

python tools/check_repo.py
```

Sprawdza to, co bot tłumaczący potrafi zepsuć, a nic innego by tego nie wyłapało: każdy link względny prawidłowo prowadzi do celu, każda sekcja `labels.json` pasuje do `i18n.json` i zawiera te same klucze oraz te same placeholdery `str.format` co wersja główna, każdy kanoniczny dokument ma swoje odbicie w każdym języku, a każdy plik markdown ma swój pasek językowy. CI uruchamia to w obu workflow; skrypt nie wymaga żadnych zależności.

Reszta CI ([ci.yml](../../.github/workflows/ci.yml)) kompiluje skrypty i uruchamia cały pipeline generujący wykresy. Aby odtworzyć go dokładnie — łącznie z zatwierdzonymi wykresami — zainstaluj przypięty toolchain, a nie ten luźny:

```bash
python -m pip install -r tools/requirements-ci.txt
