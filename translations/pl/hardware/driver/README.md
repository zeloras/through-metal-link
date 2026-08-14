# Sterownik (etap 2): półmostek IR2110

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · Polski · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Schemat:** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) (generowany przez [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

Łańcuch: Pi (SPI) → AD9833 **w trybie fali prostokątnej** (bit OPBITEN: MSB kierowany na wyjście, swing rail-to-rail — bez osobnego komparatora) → **74HC14 + RC + 1N4148** układ kształtujący (komplementarne HIN/LIN z martwym czasem ~1 µs) → IR2110 → 2×IRF540 (półmostek) → kondensator blokujący DC 1 µF → transformator dopasowujący (ferryt, ~1:3..1:5, dostroić na stole) → przetwornik Langevina TX.

Wyjście sinusoidalne AD9833 (~0.6 Vpp) nie nadaje się do logiki IR2110 — jeśli z jakiegoś powodu potrzebujesz konkretnie sinusa z DDS, wstaw między nimi komparator (np. LM393, nie ma w BOM).

Zasilanie stopnia mocy: zasilacz laboratoryjny 12–24 V z ograniczeniem prądu (**zacznij od 0.2 A**).

Uwaga: skanowanie z etapu 1 steruje piezo bezpośrednio słabym sinusem DDS (~0.6 Vpp, patrz `sweep_map.py`) — **ten sterownik wchodzi do łańcucha dopiero na etapie 2 (waty)**. Nie oczekuj ≥0.5 W od układu z etapu 1 z samym DDS.

Uwagi:
- Przetwornik Langevina jest obciążeniem pojemnościowym (typowo kilka nF). Cewka szeregową lub transformator dopasowujący są obowiązkowe; bez nich tranzystory MOSFET rozpraszają prąd bierny i się przegrzewają.
- **Transformator dopasowujący (typowy punkt awarii).** Zacznij od małego rdzenia ferrytowego (np. FT50-43 / podobny), uzwojenie pierwotne kilka zwojów, wtórne ~3–5× tyle samo, szeregowy kondensator blokujący DC 1 µF foliowy na pierwotnym. Dostroić pod kątem minimalnego prądu zasilacza *przy rezonansie z etapu 1* z TX **dociśniętym do płyty** i RX obciążonym. Przełożenie zwojów i rozproszenie są empiryczne — schemat oznacza je `*` nie bez powodu. Zapisz ostateczną liczbę zwojów w dzienniku eksperymentu.
- **Czas martwy**: IR2110 nie generuje go samodzielnie. Opcja na dyskretnych elementach — RC+1N4148 na wejściach 74HC14 (opóźnia tylko zbocza narastające, ~1 µs; przy okresie 25 µs przy 40 kHz to strata <5%). Łatwa opcja — moduł EGS002, wszystko jest tam wbudowane.
- **Logika 3.3 V**: zasilaj VDD IR2110 z tego samego 3.3 V co AD9833 i 74HC14 — przy VDD=5 V próg VIH wynosi ≈ 3.1 V i fala prostokątna 3.3 V ledwo się przebija (noty katalogowe dopuszczają VDD aż do 3.3 V).
- **Dekupling jest obowiązkowy**: 100 nF przy VDD i VCC (VCC — plus 47 µF), oraz na szynie zasilania 470–1000 µF + 100 nF ceramiczny tuż przy nogach półmostka — bez tego półmostek na zworkach płytki stykowej zbiera własne szpilki przełączania. Utrzymuj krótkie przewody pętli zasilania; jeśli węzeł przełączania silnie dzwoni, zejdź z płytki stykowej na miedziowaną płytkę w stylu dead-bug / protoboard z polem masy, zanim podniesiesz prąd.
- **Sekwencja pierwszego włączenia** (zgodna z [docs/02-safety.md](../../docs/02-safety.md)):
  1. Jeszcze bez Langevina na wtórnym. Zasilacz = 12 V, limit prądu 0.2 A. Obserwuj na oscyloskopie sterowanie bramką (HIN/LIN) i węzeł przełączania — potwierdź czas martwy i brak shoot-through.
  2. Zamontuj transformator dopasowujący + TX Langevin **dociśnięty do stalowej płyty** (lub grubego bloku metalowego ofiarnego). Nadal limit 0.2 A. Podnieś napięcie przy częstotliwości szczytowej z etapu 1 tylko na tyle, by zobaczyć prąd i napięcie RX.
  3. Stopniowo podnoś limit prądu, obserwując temperaturę MOSFET i transformatora. Nigdy nie zostawiaj niedociśniętego Langevina pod zasilaniem — praca na pełnej mocy w swobodnym powietrzu to sposób na pękanie ceramiki i uszkodzenie sterowników.

TODO: projekt KiCad (PCB) gdy prototyp na płytce stykowej (lub dead-bug) przejdzie sprawdzenie. Do tego czasu schematy w [`../schematics/`](../../../../hardware/schematics) są źródłowym źródłem prawdy projektu.
