# Protocollo di scoperta e auto-sintonizzazione del ricevitore (bozza; implementazione nelle fasi 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · Italiano · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

L'obiettivo: il dispositivo capisce da solo se c'è un ricevitore dietro la parete, sceglie da solo la frequenza e la potenza, e non arrostisce la parete per niente se qualcuno "si è scordato di saldare il ricevitore".

Il modello di riferimento sono i caricabatterie Qi: risolvono esattamente questo problema (c'è un telefono sulla bobina?) con esattamente questa sequenza. Il nostro analogo acustico:

## Fase 0 — ping analogico (il ricevitore può essere completamente scarico)
Il TX esegue una scansione a bassa potenza su tutta la banda e misura **la propria corrente e fase** (shunt + rilevatore di picco → ADS1115). Un ricevitore risonante dietro la parete è un carico accoppiato al TX attraverso la parete: la sua presenza si manifesta come un tipico avvallamento/protuberanza sulla curva di impedenza del TX, anche se tutto ciò che sta all'interno è senza alimentazione. Stesso principio di un metal detector e del ping analogico del Qi.
- Firma presente → fase 1. Nessuna firma → "nessun ricevitore trovato", resta in ping di standby (una volta ogni N secondi), non aumentare la potenza.
- Bonus: la curva di impedenza della parete "vuota" viene registrata al momento dell'installazione come riferimento — così possiamo distinguere "nessun ricevitore" da "ricevitore si è staccato / disallineato".

## Fase 1 — handshake digitale
Il TX si fissa sulla frequenza candidata (il picco della fase 0) ed eroga potenza. Il raccoglitore di energia dell'RX carica il supercondensatore, l'MCU si risveglia e risponde con **modulazione di carico**: un MOSFET cortocircuita periodicamente il proprio piezo seguendo un codice (ID + versione del protocollo). Il TX vede questo come modulazione della propria corrente. Non serve alcun trasmettitore all'interno — è uno schema RFID, lo stesso della domanda abbandonata DOE/RPI US20100027379 (prior art gratuita).

## Fase 2 — sintonizzazione servo della frequenza (perturb & observe)
L'RX può comunicare la propria tensione di bus (telemetria via modulazione di carico). Il TX fa passi di ±Δf e mantiene il massimo della potenza ricevuta — un classico loop MPPT. Questo compensa la deriva della risonanza con la temperatura (il principale trabocchetto di questa nicchia: uno slittamento di ~6% = ~10× calo di efficienza).

## Fase 3 — negoziazione della potenza e watchdog
L'RX richiede un livello (vivo / in carica / dammi di più), il TX limita la potenza a quanto richiesto. Risposte mancanti per M cicli → il TX torna alla fase 0 a bassa potenza.

## Hardware richiesto (voce BOM 12, schema — hardware/schematics/sch4)
- TX: shunt 0.1 Ω + raddrizzatore/rilevatore di picco sul secondo canale ADS1115 (corrente), opzionalmente un comparatore di fase.
- RX: 2N7002 + ~100 Ω sul **lato DC** del raddrizzatore (il pin VIN del modulo LTC3588) + GPIO — il carico viene commutato dopo il ponte, e il TX lo vede come modulazione della propria corrente. Un singolo MOSFET attraverso il piezo in AC non funziona (il diodo di body cortocircuita una semionda, il gate non ha riferimento su un nodo fluttuante); la variante attraverso il piezo funziona solo con una coppia di MOSFET in serie back-to-back.

## Limiti
Il ping analogico si indebolisce all'aumentare dello spessore della parete e delle perdite di contatto (la firma affoga nel rumore) — la soglia di rilevamento va misurata in un esperimento dedicato (experiments/). Per pareti spesse, il fallback: l'RX, una volta accumulata carica, "bussa" periodicamente con un beacon proprio.
