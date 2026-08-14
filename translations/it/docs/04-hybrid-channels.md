# Canali ibridi: barriera → fisica → numeri

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · [Português](../../pt/docs/04-hybrid-channels.md) · [Español](../../es/docs/04-hybrid-channels.md) · [Français](../../fr/docs/04-hybrid-channels.md) · Italiano · [Polski](../../pl/docs/04-hybrid-channels.md) · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

Il principio (corollario del "paradosso della penetrazione"): un'onda attraversa una barriera esattamente nella misura in cui vi interagisce debolmente — ed è per questo che non esiste un canale universale. La piattaforma non insegue un singolo canale; per ogni barriera sceglie la fisica a cui la barriera è trasparente e per cui il ricevitore è "affamato" in risonanza.

## Tabella di selezione dei canali

| Barriera | Canale funzionante | Atteso (ordini di grandezza) | Note |
|---|---|---|---|
| Acciaio/alluminio 1–60 mm, contatto possibile | Piezo-acustica (il nostro primario) | watt; kbit/s (fino a Mbit/s in modalità MHz) | richiede contatto acustico (accoppiamento con grasso/epossidico) |
| Metallo: sporco, verniciato, caldo, contatto indesiderabile | EMAT (magnetismo → suono nella parete) | mW; kbit/s; gap fino a ~3 mm | solo pareti conduttive; dati, non potenza |
| Parete ferromagnetica senza piezo | Magnetostrizione (una bobina guida l'acciaio stesso) | briciole; bit/s–kbit/s | ramo sperimentale, economico da testare |
| Doppia parete con vuoto (termos, criostato, dewar) | Magnetica LF (decine–centinaia di Hz) | µW–mW; bit/s | effetto pelle: in acciaio δ≈0,6 mm @1 kHz — abbassare la frequenza |
| Non-metallo: vetro, plastica, ceramica | Piezo-acustica (più facile del metallo) | watt; kbit/s | + spesso la RF semplice passa — controllare prima quello |
| Parete con strato di gomma/schiuma, composito | Onestamente: quasi un vicolo cieco | — | l'assorbitore mangia tutto; la via d'uscita è un punto senza rivestimento |
| Liquido dietro la parete (serbatoio pieno) | Piezo-acustica, degradata | potenza − qualche dB; risonanza più breve | il carico liquido sposta/smorza la risonanza — rifare lo sweep contro il recipiente pieno; mantenere intensità continua ≲1 W/cm² per restare sotto la cavitazione ([teoria](00-theory.md#effetto-sulla-parete-e-sul-mezzo-dietro-di-essa)) |
| Liquido in ebollizione nel percorso acustico | Soluzione architetturale | — | montare il ricevitore sulla parete, tenere il liquido fuori dal percorso |

## Architettura del nodo ibrido

- Livello di potenza: coppia piezo in risonanza (fasi 1–4).
- Livello dati senza contatto: una testa EMAT come "pistola scanner" staccabile (fase ~6).
- Livello di fallback: bobine LF per sandwich sotto vuoto (quando il compito lo richiede).
- Il protocollo di scoperta (docs/03) si estende da "sweep sulla frequenza" a "sweep sulla fisica": ping piezo → ping EMAT → ping LF; il nodo sceglie il canale che passa da solo e segnala quale barriera vede.

## Applicazioni di esempio per canale

1. **Pacchi batteria sigillati (EV/stoccaggio):** sensore T/gas dentro un involucro incapsulato; potenza+dati tramite una coppia piezo attraverso 2–3 mm di alluminio. Il mercato è in boom, e una penetrazione in un involucro batteria = inferno di certificazione.
2. **Criostato/dewar:** un logger di temperatura all'interno, che invia un pacchetto di bit una volta al minuto via magnetica LF attraverso la guaina sotto vuoto. Fondamentalmente fuori portata per l'acustica — qui l'ibrido è insostituibile.
3. **Tubazione/autoclave sotto pressione:** uno scanner EMAT premuto contro un tubo caldo verniciato senza alcuna preparazione superficiale — legge un beacon risonante passivo dall'interno.
4. **Tini di fermentazione (birra/vino, acciaio inossidabile):** un sensore di densità/T dentro il tino senza una sola penetrazione — i codici sanitari amano l'assenza di fori.
5. **Container marittimo/cassaforte:** "il carico è vivo" — una coppia piezo attraverso acciaio ondulato, interrogata con uno scanner portatile.

## Limiti che nessun livello può risolvere
Potenza — solo piezo a contatto (EMAT e magnetica LF sono ordini di grandezza più deboli). Pareti composito/rivestite di gomma sono fuori dalla piattaforma. La velocità del canale LF è bit al secondo — questo è telemetria, non streaming.
