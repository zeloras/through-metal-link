# QUICKSTART: da zero assoluto al banco di prova stage 1–2

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Português](../pt/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · [Français](../fr/QUICKSTART.md) · Italiano · [Polski](../pl/QUICKSTART.md) · [Türkçe](../tr/QUICKSTART.md) · [Українська](../uk/QUICKSTART.md) · [Tiếng Việt](../vi/QUICKSTART.md) · [中文](../zh/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md)

Scenario: hai solo una scrivania e un po' di soldi. Tutto qui sotto ti porta a un banco funzionante — "mappa di sweep + primi watt attraverso l'acciaio". I prezzi sono indicativi, in USD.

## Cesto 1 — strumenti (una base per anni, ~$120)

| Articolo | Perché | Prezzo | Dove |
|---|---|---|---|
| Stazione di saldatura (clone T12) | di tutto | 35–50 | Ali |
| Multimetro (classe AN8008/UT61) | tensioni, continuità, capacità | 15–25 | Ali |
| Alimentatore da banco 30V/5A con limitazione di corrente | alimenta il driver; il limite di corrente è la tua assicurazione contro i MOSFET bruciati | 45–60 | Ali/locale |
| Braccia con mollette, saldatura, flussante, treccia dissaldante, tronchesi, pinzette | le piccole cose senza le quali non si può fare | 15 | Ali/locale |
| Fili Dupont + breadboard + termorestringente | prototipazione | 8 | Ali |

## Cesto 2 — elettronica del banco (~$70)

| Articolo | Qtà | Prezzo | Nota |
|---|---|---|---|
| Raspberry Pi (Zero 2 W basta; 4/5 è più comodo) + SD | 1 | 20–60 | il cervello: sweep, log, grafici |
| Trasduttore Langevin 40 kHz 50–60 W | **4** | 40 | comprane 4 da UN lotto; sceglieremo la coppia migliore via sweep |
| Modulo DDS AD9833 | 2 | 8 | il secondo è di riserva |
| IR2110 + IRF540 ×4 (oppure un modulo EGS002) | 1 set | 10 | driver half-bridge |
| ADC ADS1115 | 2 | 4 | il Pi non ha un ADC proprio |
| Toroide in ferrite + filo smaltato 0,5 mm | 2 | 4 | trasformatore di adattamento |
| Ponte Schottky (SS14 ×8), supercondensatore 1F 5,5V ×2 | 1 | 4 | catena ricevitore |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | protezione. NON CI SIAMO SUL PREZZO |
| Modulo GY-LTC3588 | 1 | 7 | harvester (stage 4, ma facciamolo spedire ora) |
| assortimento resistori/condensatori, LED | 1 | 8 | se non hai proprio nulla |
| Passivi di supporto: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | spiccioli; lista completa — BOM item 11–12 |

## Cesto 3 — meccanica (~$20, in locale)

Piastra in acciaio 3 mm ~150×150 — 2 pz (deposito metalli / taglio laser); morse a F ×2; grasso accoppiante denso e consistente (grasso al litio); resina epossidica; carta vetrata (per pulire la zona di contatto).

## Opzionale, ma fortemente consigliato (~$90)

| Articolo | Perché | Prezzo |
|---|---|---|
| Oscilloscopio USB/portatile (FNIRSI/Hantek, 2 canali; non serve ≥40 MHz di banda — 10 sono più che sufficienti) | vedi la waveform sul gate e sul piezo; risparmia giorni di debug del driver | 60–80 |
| ESP32 DevKit ×2 | stage 4 (il nodo dietro la parete) | 8 |

**Totale: minimo indispensabile ~$210, confortevole ~$300.** (Se hai già un Pi, una stazione di saldatura e un alimentatore da banco — sottrai ~$120.)

## Ordine di acquisto (il percorso critico è la spedizione)

1. Oggi: cesto 2 da Ali (3–4 settimane di spedizione — è il percorso critico) + l'oscilloscopio.
2. Questa settimana: cesti 1 e 3 in locale.
3. Mentre arriva: `raspi-config` → SPI+I2C, esegui `software/sweep-map/sweep_map.py --mock` senza hardware (canale sintetico — l'intera pipeline CSV+grafici funziona su qualsiasi computer), leggi docs/00–03, guarda i grafici attesi in docs/img e gli schemi in hardware/schematics (la build dello stage 1 segue sch3 e sch2).

## Cosa vedrai (simulatore: software/simulator/channel_sim.py → docs/img)

Questi PNG sono **previsioni del modello**, non misure di laboratorio. Rapporti di contatto, Q caricato ≈40 ed efficienza di catena ≤40% sono assunzioni esplicite in `channel_sim.py` — sostituiscili con dati di sweep/potenza appena il banco esiste.

- `sim0-rig-sketch.png` — l'intero banco in uno schizzo (catena stage 2; lo stage 1 omette l'half-bridge e pilota il TX con la debole sinusoide del DDS).
- `sim1-sweep-contacts.png` — forma attesa dello sweep: un picco stretto vicino a ~40 kHz; il modello usa grasso:secco:gap ≈ 1 : 0,25 : 0,02 come segnaposto. Nessun picco — prima debugga il contatto o il mismatch della coppia (sim2).
- `sim2-pair-mismatch.png` — perché 4 trasduttori Langevin e non 2: con Q≈40, uno scarto di risonanza di 1,5 kHz dentro una coppia fa crollare la potenza del modello di ~10×; lo sweep sceglie la coppia migliore tra 4.
- `sim3-thickness-comb.png` — per dopo (modo B, MHz): la piastra è trasparente come un pettine di risonanze di spessore, quindi la frequenza va tracciata.
- `sim4-power-budget.png` — assorbimento del carico rispetto alle bande **target** di potenza ricevuta. La banda del modo A (0,5–5 W) è l'ambizione dello stage 2 se adattamento e contatto collaborano; il modo B è la banda più bassa. Il Wi-Fi continuo è un marcatore di picco di carico, non una promessa — ESP32/BLE/LED duty-cycled sono i primi consumatori realistici.
- `sim5-ook-datarate.png` — stage 3: perché OOK su trasduttori Langevin si ferma a ~1–2 kbit/s con Q≈40 (ring-down τ≈0,3 ms), e perché va benissimo per un nodo sensore.

## Criteri per "il banco funziona"

Suddivisi per stage — non segnare lo stage 1 come completato con i numeri dello stage 2.

**Stage 1 — mappa di sweep** ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)):
1. Sweep 25–45 kHz in due passaggi consecutivi: il centro del picco si riproduce entro <200 Hz.
2. Bonus opzionale: grasso+morsa vs pressione a secco sulla stessa coppia (ampiezze relative, non watt assoluti).

**Stage 2 — primi watt** ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)):
1. Half-bridge + trasformatore di adattamento attivi; messa in servizio con limitazione di corrente del PSU secondo [docs/02-safety.md](../../docs/02-safety.md) e [hardware/driver/](../../hardware/driver/README.md).
2. Alla risonanza dello stage 1, ≥0,5 W in un carico resistivo noto attraverso 3 mm di acciaio (misura V e I sul lato DC dopo il ponte RX).
3. LED dietro la piastra si accende con la potenza raccolta; foto + CSV in experiments/002.

Sicurezza prima della prima accensione: [docs/02-safety.md](../../docs/02-safety.md) (TVS sul ricevitore, limite di corrente del PSU a 0,2 A per la messa in servizio, niente run Langevin ad alta potenza in aria libera).
