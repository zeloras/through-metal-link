# Stato dell'arte: su cosa costruiamo

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · Italiano · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · [中文](../../zh/docs/01-prior-art.md) · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## La regola
Ogni decisione tecnica in questo repo deve essere riconducibile a una fonte della lista "libera" (brevetti scaduti, paper). I brevetti in vigore sono in sola lettura — sfruttateli per capire i problemi, non copiate mai le loro rivendicazioni (questo conta per la commercializzazione negli USA; vedi la mappa dei brevetti nel progetto).

## Le fondamenta libere (brevetti scaduti/abbandonati = dominio pubblico)
- **US5982297** (Aerospace Corp, 1997) — la ricetta di base: una coppia piezo attraverso la parete, potenza + dati bidirezionali. Il manuale di riferimento principale.
- US5594705 (Dynamotive, 1994) — un "trasformatore acustico" attraverso lo scafo.
- US6037704, US6127942 (Aerospace Corp) — alimentazione di sensori, lettura dei dati di ritorno.
- **US7902943** (Caltech/JPL, decaduto per mancati pagamenti delle tasse di mantenimento nel 2019) — il feed-through di Sherrit: riflettore, trasformatore acustico.
- US9748870 (Caltech/JPL) — lavoro meccanico attraverso la parete.
- **US9361877** (Univ. Oklahoma, decaduto per mancati pagamenti delle tasse di mantenimento) — un sistema ricetrasmettitore completo moderno.
- US20100027379 / WO2008105947 (DOE+RPI, abbandonato) — un carrier dall'esterno + modulazione di carico dall'interno.

## Paper chiave
- Lawry et al., IEEE TUFFC 2013 (10.1109/TUFFC.2013.2550) — 50 W + 12,4 Mbit/s, 63,5 mm di acciaio.
- Sherrit et al., NASA NTRS 20080048150 — una lampada da 100 W alimentata attraverso una parete.
- Yang et al., Sensors 2015 (10.3390/s151229870) — review, il miglior riassunto dei numeri.
- Ji et al., Phys. Rev. Applied 21, 014059 (2024) — metamateriale, 2%→66% attraverso 1 mm di acciaio inossidabile (nessun brevetto trovato al 07.2026).

Questi paper sono la **baseline di fisica e igiene brevettuale**. I loro numeri di potenza/bitrate usavano trasduttori da laboratorio, bonding e adattamento — non il BOM AliExpress Langevin + grasso in [QUICKSTART.md](../QUICKSTART.md). Citateli come prove di esistenza; le soglie di superamento del progetto sono in [experiments/](../../../experiments).

## Cosa non copiamo finché è vivo (solo USA, fino al ~2032; le fasi 1–4 comunque non ne hanno bisogno)
OFDM con sottoportanti posizionate per evitare le armoniche del canale di potenza (RPI US9054826); full-duplex "downlink AM + uplink a modulazione di carico + tracciamento di frequenza" come schema unico (RPI US9455791); trasduttori conformali per superfici curve secondo l'approccio Drexel (US10594409).
