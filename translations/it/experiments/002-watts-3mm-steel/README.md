# Esperimento 002: Primi Watt Attraverso 3 mm di Acciaio (PIANIFICATO)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · Italiano · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · [中文](../../../zh/experiments/002-watts-3mm-steel/README.md) · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **Fase:** 2 (potenza in un carico noto alla risonanza trovata in [001](../001-sweep-map-3mm-steel/README.md)).
- **Obiettivo:** misurare la reale potenza DC erogata attraverso 3 mm di acciaio con il driver half-bridge e il trasformatore di adattamento.
- **Ipotesi:** con una coppia di Langevin dello stesso lotto, contatto grasso+morsetto (o epoxy) e un trasformatore di adattamento accordato, ≥0,5 W su un carico resistivo al picco della fase 1 è raggiungibile. (I valori multi-watt/kW della letteratura usavano trasduttori e collegamenti diversi — considerarli come tetto, non come soglia di superamento.)
- **Prerequisiti:**
  - Esperimento 001 chiuso (picco riproducibile, frequenza registrata).
  - TVS installato sulla catena RX prima di qualsiasi alimentazione del driver ([docs/02-safety.md](../../docs/02-safety.md)).
  - Sequenza di bring-up del driver seguita ([hardware/driver/README.md](../../../../hardware/driver/README.md)).
- **Setup (minimo):**
  - TX: Pi → AD9833 onda quadra → shaper di dead-time → half-bridge IR2110 → trasformatore di adattamento → Langevin morsettato alla piastra ([sch1](../../../../hardware/schematics/sch1-driver-halfbridge.png)).
  - Parete: acciaio 3 mm, metodo di contatto registrato (grasso+morsetto / epoxy / altro).
  - RX: Langevin → ponte Schottky → R_load nota (resistenza di potenza) e/o LED; misurare V_dc e I_dc dopo il ponte ([sch2](../../../../hardware/schematics/sch2-receiver-stage1.png) topologia, carico invece di solo-ADC).
- **Procedura (schema):**
  1. Bring-up elettrico con limite PSU a 0,2 A senza rivendicare potenza acustica.
  2. Morsettare TX/RX, impostare la frequenza di pilotaggio sul picco dell'esperimento 001.
  3. Aumentare lentamente il limite di corrente; registrare V/I della PSU, temperatura MOSFET/trasformatore, V_dc e I_dc sul carico.
  4. P_load = V_dc · I_dc. Opzionale: foto breve demo del LED una volta noto P_load.
  5. Ripetere una volta dopo un raffreddamento; la frequenza di picco può derivare con la temperatura — ricontrollare con un mini-sweep se la potenza cala.
- **Criteri di successo:**
  1. P_load ≥ 0,5 W attraverso 3 mm di acciaio a una frequenza e metodo di contatto documentati.
  2. Due esecuzioni concordano su P_load entro ~20% sotto lo stesso morsetto/couplant (stabilità di ordine di grandezza, non ancora grado metrologico).
  3. Foto del LED (o altro carico) + CSV/log collegati da questo file sotto `data/`.
- **Il fallimento è dato:** se P_load rimane ≪ 0,5 W, registrare Δf della coppia (da 001), metodo di contatto, spire del trasformatore e forme d'onda — questo è l'input per il prossimo ADR, non un motivo per modificare silenziosamente il simulatore.
