# ADR-0001: Selezione della modalità di frequenza per la Fase 1

> [English (primary)](../../../../docs/decisions/0001-frequency-mode-choice.md) · [Русский](../../../ru/docs/decisions/0001-frequency-mode-choice.md) · [Deutsch](../../../de/docs/decisions/0001-frequency-mode-choice.md) · [Português](../../../pt/docs/decisions/0001-frequency-mode-choice.md) · [Español](../../../es/docs/decisions/0001-frequency-mode-choice.md) · [Français](../../../fr/docs/decisions/0001-frequency-mode-choice.md) · Italiano · [Polski](../../../pl/docs/decisions/0001-frequency-mode-choice.md) · [Türkçe](../../../tr/docs/decisions/0001-frequency-mode-choice.md) · [Українська](../../../uk/docs/decisions/0001-frequency-mode-choice.md) · [Tiếng Việt](../../../vi/docs/decisions/0001-frequency-mode-choice.md) · [中文](../../../zh/docs/decisions/0001-frequency-mode-choice.md) · [日本語](../../../ja/docs/decisions/0001-frequency-mode-choice.md) · [한국어](../../../ko/docs/decisions/0001-frequency-mode-choice.md) · [हिन्दी](../../../hi/docs/decisions/0001-frequency-mode-choice.md)

- Stato: ACCETTATO (da rivedere dopo la Fase 2)
- Data: 2026-07-24

## Contesto
Due modalità (vedi docs/00-theory.md): A — 28–40 kHz su trasduttori Langevin, B — 0.6–1 MHz su dischi che sfruttano la risonanza di spessore della parete.

## Decisione
Le Fasi 1–2 usano la modalità A. Motivi: più economici ($10–30 al pezzo), più potenti (watt contro centinaia di mW), più tolleranti nella messa a punto (risonanza ampia), e il driver può essere costruito con un half-bridge attorno a un IR2110. La modalità B arriva dopo aver ottenuto i primi watt attraverso — come ramo separato per dati ad alta velocità.

## Conseguenze
I dati nella Fase 3 saranno lenti (kbit/s) — sufficienti per un nodo sensore. L'ADC ADS1115 (860 SPS) va bene per l'involuppo a 40 kHz dopo il raddrizzatore, ma non per il campionamento diretto — il campionamento diretto è rinviato alla modalità B (richiede un ADC diverso).

La Fase 1 (sweep) usa solo la debole pilotaggio DDS; la Fase 2 (watt) è un esperimento e un bring-up separati ([experiments/002](../../../../experiments/002-watts-3mm-steel/README.md)). Le bande di potenza del simulatore rimangono obiettivi finché 002 non viene misurato.
