# Protokół wykrywania odbiornika i autostrojenia (zarys; implementacja w etapach 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · Polski · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

Cel: urządzenie samo rozpoznaje, czy za ścianą znajduje się odbiornik, samo dobiera częstotliwość i moc, a jeśli ktoś „zapomniał przyspawać odbiornik", nie przegrzewa ściany bez sensu.

Wzorem są ładowarki Qi: rozwiązują dokładnie ten sam problem (czy na cewce leży telefon?) w dokładnie takiej samej sekwencji. Nasz odpowiednik akustyczny:

## Faza 0 — analogowy ping (odbiornik może być całkowicie rozładowany)
Nadajnik (TX) wykonuje przeciąganie po paśmie na niskiej mocy i mierzy **swój własny prąd i fazę** (szunt + detektor szczytowy → ADS1115). Rezonansowy odbiornik za ścianą jest obciążeniem sprzężonym z TX przez ścianę: jego obecność objawia się jako charakterystyczne wgłębienie/wypuklenie na krzywej impedancji TX, nawet jeśli wszystko wewnątrz jest bez zasilania. Ta sama zasada co w wykrywaczu metalu i w analogowym pingu Qi.
- Sygnatura obecna → faza 1. Brak sygnatury → „nie znaleziono odbiornika", pozostanie w trybie ping-u czuwania (co N sekund), bez podnoszenia mocy.
- Bonus: krzywa impedancji „pustej" ściany jest rejestrowana w czasie instalacji jako odniesienie — dzięki temu odróżniamy „brak odbiornika" od „odbiornik się poluzował / przesunął".

## Faza 1 — cyfrowe uzgadnianie
TX parkuje na częstotliwości kandydującej (pik z fazy 0) i dostarcza moc. Harvester RX ładuje superkondensator, MCU się budzi i odpowiada **modulacją obciążenia**: MOSFET okresowo zwiera swój piezo według kodu (ID + wersja protokołu). TX widzi to jako modulację własnego prądu. Żaden nadajnik wewnątrz nie jest w ogóle potrzebny — to schemat RFID, ten sam co w porzuconym zgłoszeniu DOE/RPI US20100027379 (wolna sztuka poprzednia).

## Faza 2 — serwostrojenie częstotliwości (perturb & observe)
RX może raportować swoje napięcie szyny (telemetria przez modulację obciążenia). TX wykonuje kroki ±Δf i utrzymuje maksimum odebranej mocy — klasyczna pętla MPPT. To kompensuje dryf rezonansu z temperaturą (główna pułapka tej niszy: przesunięcie ~6% = spadek wydajności ~10×).

## Faza 3 — negocjacja mocy i watchdog
RX żąda poziomu (aktywny / ładuje się / daj więcej), TX ogranicza moc do żądanego poziomu. Brak odpowiedzi przez M cykli → TX cofa się do fazy 0 na niskiej mocy.

## Wymagany sprzęt (pozycja BOM 12, schemat — hardware/schematics/sch4)
- TX: szunt 0,1 Ω + prostownik/detektor szczytowy na drugim kanale ADS1115 (prąd), opcjonalnie komparator fazy.
- RX: 2N7002 + ~100 Ω po **stronie DC** prostownika (pin VIN modułu LTC3588) + GPIO — obciążenie jest przełączane za mostkiem, a TX widzi to jako modulację własnego prądu. Pojedynczy MOSFET w poprzek piezo AC nie działa (dioda body zwiera jedno półokresy, bramka nie ma odniesienia na pływającym węźle); wariant w poprzek piezo działa tylko z parą MOSFET-ów włączonych szeregowo tył do tyłu.

## Ograniczenia
Analogowy ping słabnie wraz ze wzrostem grubości ściany i strat kontaktowych (sygnatura tonie w szumie) — próg detekcji musi być zmierzony w dedykowanym eksperymencie (experiments/). Dla grubych ścian rozwiązanie awaryjne: RX, gdy naładuje się, okresowo „puka" własnym sygnałem nawigacyjnym.
