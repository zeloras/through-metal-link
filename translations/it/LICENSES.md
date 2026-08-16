# Licenze e protezione brevettuale

> [English (primary)](../../LICENSES.md) · [Русский](../ru/LICENSES.md) · [Deutsch](../de/LICENSES.md) · [Português](../pt/LICENSES.md) · [Español](../es/LICENSES.md) · [Français](../fr/LICENSES.md) · Italiano · [Polski](../pl/LICENSES.md) · [Türkçe](../tr/LICENSES.md) · [Українська](../uk/LICENSES.md) · [Tiếng Việt](../vi/LICENSES.md) · [中文](../zh/LICENSES.md) · [日本語](../ja/LICENSES.md) · [한국어](../ko/LICENSES.md) · [हिन्दी](../hi/LICENSES.md)

L'obiettivo di questo schema: il progetto è completamente aperto, chiunque può farne un fork e costruirci sopra (uso commerciale compreso), mentre il rischio di cause legali su brevetti è ridotto al minimo assoluto raggiungibile con mezzi legali e procedurali.

## Lo schema (tre livelli; testi completi in [LICENSES/](../../LICENSES))

| Area | Licenza | Testo | Disposizioni sui brevetti |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](../../LICENSES/Apache-2.0.txt) | §3: ogni contributore concede automaticamente una licenza brevettuale per il proprio contributo; intenta una causa brevettuale e perdi la licenza **brevettuale** (rappresaglia; la licenza sul copyright del §2 è irrevocabile e sopravvive alla causa) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](../../LICENSES/CERN-OHL-W-2.0.txt) | §7.1: una licenza brevettuale (Make / have Made / use / sell / import…) da ogni concedente — ma solo per le rivendicazioni necessariamente violate dal dato Covered Source; §7.2: una causa brevettuale (compreso il tentativo di invalidare il brevetto di terzi) termina **tutti** i diritti sotto la licenza |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](../../LICENSES/CC-BY-4.0.txt) | non concede **nessun** diritto brevettuale (§2(b)(2)) — il vuoto è colmato dalla concessione brevettuale esplicita in [CONTRIBUTING.md](../../CONTRIBUTING.md) |
| tutto il resto (`README.md` radice, `QUICKSTART.md`, questo file, `data/`, ecc.) | CC-BY-4.0 | — | fallback: nessun file nel repository resta "tutti i diritti riservati" |

I file di codice riportano intestazioni SPDX (Apache-2.0); la mappa di copertura leggibile dalle macchine è [REUSE.toml](../../REUSE.toml). La riga di copyright si trova in [NOTICE](../../NOTICE); il file [LICENSE](../../LICENSE) radice è un puntatore a questo schema.

**Perché CERN-OHL-W, non S né P.** W è il compromesso intermedio: il design e le sue modifiche devono restare aperti a ogni distribuzione, ma il prodotto in cui il design è integrato può essere commerciale e proprietario — il che mantiene aperte le nicchie di docs/05 (laboratori, birrifici, pacchi batteria). S (copyleft forte) chiuderebbe la porta all'integrazione; P (permissiva) permetterebbe fork chiusi. Il rafforzamento verso S è insito nella licenza stessa: §8.3 permette a chiunque di trattare il materiale con licenza W come se fosse con licenza S (a condizione che il requisito degli Available Components sia soddisfatto) — senza necessità di permesso. L'allentamento (verso P o un'altra licenza), al contrario, è possibile solo finché tutto il materiale appartiene a un unico autore; dopo il primo contributo esterno — solo con il consenso di ogni contributore.

**Nome del progetto.** "through-metal-link" non è un marchio registrato; le licenze stesse non concedono alcun diritto sul nome (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Fare riferimento al progetto in modo fattuale ("basato su through-metal-link") è libero per chiunque; i fork con modifiche incompatibili sono pregati di pubblicare con un proprio nome.

## Contro cosa protegge — e contro cosa no (onestamente)

**Protegge contro:**
1. **Cause dai contributori.** Chiunque abbia contribuito ha automaticamente concesso in licenza i propri diritti brevettuali su quel contributo (Apache §3, CERN-OHL §7.1, e CONTRIBUTING per i docs). Una causa costa caro all'attore: sotto Apache-2.0 perde le licenze brevettuali sul codice; sotto CERN-OHL-W perde tutti i diritti sul livello hardware senza appello (§7.2 — scattato anche solo per un tentativo di impugnare il brevetto di terzi).
2. **Privatizzazione dei fork hardware.** CERN-OHL-W obbliga chiunque distribuisca (Conveyance di un prodotto o di sorgenti) a pubblicare le proprie modifiche al design — i miglioramenti rifluiscono nel livello aperto e diventano essi stessi prior art. (Un fork da cassetto, mai trasmesso a terzi, non ha obbligo di pubblicazione — come sotto qualsiasi copyleft.)
3. **Brevetti *futuri* di terzi.** Tutto ciò che viene pubblicato con data distrugge la novità per domande successive: per una soluzione qui descritta prima della loro data di deposito, non può più essere concesso un brevetto valido. Contro domande depositate *prima* della nostra pubblicazione questo non funziona — per quelle, l'unica difesa è il livello dei brevetti scaduti (vedi sotto).

**Non protegge contro:**
- **Brevetti di terzi già esistenti.** Nessuna licenza può farlo. Quello che funziona contro di essi è la disciplina ingegneristica di docs/01-prior-art.md: costruire solo dal livello scaduto (pubblico dominio), non implementare le rivendicazioni attive lì elencate (RPI, Drexel, e le famiglie Navy/ABB/Ultrapower aggiunte in 2026-08 — nota che non sono tutte solo USA e non tutte scadono intorno al 2032), e ricondurre ogni decisione di design a una fonte libera. Non è una garanzia, ma è esattamente la pratica che rende vana una causa.
- Un fork diretto alla produzione commerciale fa la propria analisi FTO (freedom to operate) per la propria giurisdizione e il proprio design — il repository non fornisce alcuna dichiarazione brevettuale (disclaimer in tutte e tre le licenze).

## Protocollo di pubblicazione difensiva (eseguire quando il repo diventa pubblico)

Ogni risultato pubblicato è prior art datata che blocca tutte le domande successive di terzi per la stessa soluzione:

1. Aprire il repository con la sua cronologia git completa (commit = timestamp).
2. Snapshot su **Zenodo** → DOI: un archivio indipendente con una data legalmente significativa, citabile nei paper.
3. Fissarlo in **Software Heritage** (archive.softwareheritage.org — un mirror perpetuo).
4. Ogni esperimento completato `experiments/NNN` — con data, numeri e grafici: quella è la pubblicazione di una soluzione tecnica specifica.
5. Grandi traguardi (primi watt, primo nodo) — un resoconto diffuso nel mondo (Hackaday.io / arXiv / blog): più ampia la diffusione, più forte lo status di prior art.

## Per i contributori

Le regole si trovano in [CONTRIBUTING.md](../../CONTRIBUTING.md): DCO sign-off, inbound=outbound, una concessione brevettuale esplicita su ogni contributo a prescindere dalla directory, tracciabilità delle decisioni di design a prior art libera.

Finché non apre, il repository resta privato — pubblicare prima dei primi risultati riproducibili indebolirebbe sia la posizione scientifica che quella brevettuale.
