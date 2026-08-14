# Mappa delle applicazioni: chi ha bisogno di questa piattaforma tecnologica, e perché

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · [Português](../../pt/docs/05-applications-map.md) · [Español](../../es/docs/05-applications-map.md) · [Français](../../fr/docs/05-applications-map.md) · Italiano · [Polski](../../pl/docs/05-applications-map.md) · [Türkçe](../../tr/docs/05-applications-map.md) · [Українська](../../uk/docs/05-applications-map.md) · [Tiếng Việt](../../vi/docs/05-applications-map.md) · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

La piattaforma: un canale attivo di potenza e dati attraverso pareti cieche — piezo-acustica / EMAT / magnetica LF. Di seguito: dove serve nel mondo reale, chi è già sul posto e cosa resta per noi.

## 1. Pacchi batteria sigillati (EV, accumulo energetico domestico/industriale)
- Problema: rilevamento precoce del thermal runaway — gas (CO₂, H₂, vapori di elettrolita) compaiono dentro il pacco da minuti a ore prima di un incendio; una penetrazione del sensore nell'involucro = perdita di tenuta ermetica e di certificazione.
- La nostra piattaforma: un nodo gas/temperatura dentro il pacco, alimentazione e telemetria tramite una coppia piezo attraverso 2–3 mm di alluminio. Zero fori.
- Chi è già sul posto: Liminal Insights — *diagnostica acustica dall'esterno* (brevetti sui metodi di analisi, non sul canale). Nessuno vende nodi *dentro* il pacco.
- Maturità del nicho: il mercato cresce in modo esplosivo, lo scaffale è vuoto. Per la piattaforma — applicazione showcase #1.

## 2. Strumentazione da laboratorio: camere a vuoto, criostati, glove box
- Problema: ogni passante elettrico in una camera a vuoto è una flangia da centinaia di dollari e una fonte di perdite; in un criostato, un cavo = dispersione termica.
- La nostra piattaforma: un sensore dentro la camera, alimentazione/dati tramite suono attraverso la parete d'acciaio; per i sandwich a vuoto dei dewar — magnetica LF (qualche bit/s è sufficiente per un data-logger di temperatura).
- Chi è già sul posto: nessuno con through-wall wireless; i laboratori vivono di flange passanti.
- Maturità: il nicho ideale per partire con l'open source — i laboratori sono esattamente il pubblico tipico dell'hardware open (la via di TinyLev): comprano senza certificazioni e ti citano nei paper.

## 3. Produzione alimentare: tini di fermentazione, autoclavi (birra, vino, latticini)
- Problema: le normative igieniche detestano le penetrazioni (lavaggio CIP, zone morte); si vuole conoscere densità/T/pressione dentro il tino in ogni momento.
- La nostra piattaforma: un nodo sulla parete interna di un tino in acciaio inox, interrogato dall'esterno con uno scanner portatile o una coppia fissa.
- Chi è già sul posto: sensori avvitati tradizionali; nessuna soluzione through-wall wireless.
- Maturità: letteralmente alla portata di un test in garage (qualsai birrificio artigianale è un banco di prova a distanza di una passeggiata).
- Avvertenza fisica: un tino pieno carica la parete — rifare lo sweep contro il recipiente pieno e mantenere potenza continua ≲1 W/cm²; oltre, cavitazione nel prodotto (degassaggio CO₂, off-flavor, erosione a lungo termine della parete) — [teoria](00-theory.md#effetto-sulla-parete-e-sul-mezzo-dietro-di-essa).

## 4. Tubazioni, recipienti in pressione, NDT industriale
- Problema: monitorare corrosione/parametri internamente senza fermo o penetrazione; le superfici sono calde, verniciate, sporche.
- La nostra piattaforma: una "pistola scanner" EMAT — appoggiarla su un tubo senza alcuna preparazione superficiale, leggere un beacon risonante passivo dall'interno.
- Chi è già sul posto: misuratori di portata ultrasonici a pinza e spessimetri (mercato maturo), ma nessun beacon interattivo interno.
- Maturità: fascia media; richiede il ramo EMAT (stadio ~6).

## 5. Oil & gas / downhole, e nucleare
- Chi è già sul posto: Metrol, Acoustic Data, Baker Hughes (downhole, 30 anni, modello a servizio); R&D DOE/UNT/Westinghouse (contenitori nucleari).
- Verdetto onesto: occupato e fortemente regolamentato — non ci andiamo, ma la loro stessa esistenza = prova che questa fisica si vende per soldi seri. Usarli come riferimento nel README.

## 6. Logistica marittima e strutture subacquee
- Problema: "il carico è vivo?" in un container sigillato; dati dal lato interno dello scafo di una nave.
- Chi è già sul posto: CSignum (EM LF attraverso acqua/bulkhead) — l'unico vicino diretto per filosofia ibrida.
- Maturità: lungo raggio; per noi, per ora, solo una direzione di pensiero.

## Priorità (cosa fare, in che ordine)
1. **Ora:** stadi di piattaforma 1–4 sullo scenario showcase "camera da lab / scatola saldata" (nichio #2 — il più aperto all'open source).
2. **Poi:** una demo su un oggetto reale del nichio #3 (un tino da birrificio) — economica, fotogenica, un utente vero.
3. **Fascia media:** lo scenario batteria (nichio #1) come caso di punta per la pubblicazione; il ramo EMAT per il nichio #4.

*La visione passiva (muon radiography) è stata scorporata in un progetto separato — vedi muon-lab nella knowledge base.*
