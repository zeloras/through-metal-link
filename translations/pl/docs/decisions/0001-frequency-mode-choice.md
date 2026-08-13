# ADR-0001: Wybór trybu częstotliwości dla Etapu 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · [Italiano](../../../it/docs/decisions/0001-frequency-mode-choice.md) · Polski · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Status: ZAAKCEPTOWANY (do ponownego rozpatrzenia po Etapie 2)
- Date: 2026-07-24

## Kontekst
Dwa tryby (patrz docs/00-theory.md): A — 28–40 kHz na przetwornikach Langevina, B — 0,6–1 MHz na dyskach wykorzystujących rezonans grubości ściany.

## Decyzja
Etap 1–2 działa w trybie A. Powody: tańsze (10–30 $ za sztukę), mocniejsze (waty zamiast setek mW), bardziej tolerancyjne w strojeniu (szeroki rezonans), a sterownik można zbudować z półmostka wokół układu IR2110. Tryb B wchodzi do gry, gdy przepuścimy pierwsze waty — jako osobna gałąź do szybkiej transmisji danych.

## Konsekwencje
Dane na Etapie 3 będą wolne (kbit/s) — wystarczająco dla węzła czujnikowego. Przetwornik ADS1115 (860 SPS) jest wystarczający dla obwiedni przy 40 kHz za prostownikiem, ale nie do bezpośredniego próbkowania — bezpośrednie próbkowanie jest odroczone do trybu B (wymaga innego przetwornika ADC).

Etap 1 (sweep) używa tylko słabego sterowania DDS; etap 2 (waty) to osobny eksperyment i uruchomienie ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). Pasma mocy z symulatora pozostają celami, dopóki nie zostaną zmierzone wyniki 002.
