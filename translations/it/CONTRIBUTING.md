# Come contribuire

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · Italiano · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Grazie per voler far avanzare il canale open through-steel. Le tre regole qui sotto non sono burocrazia — sono l'armatura brevettuale del progetto (vedi [LICENSES.md](LICENSES.md) per il motivo).

## 1. Licenze dei contributi (inbound = outbound)

Inviando un contributo, accetti che venga licenziato allo stesso modo del resto del materiale nella sua directory:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Concessione di brevetto.** In aggiunta — dato che CC-BY-4.0 non licenzia brevetti — concedi al progetto e a tutti i destinatari dei suoi materiali una licenza brevettuale perpetua, irrevocabile, mondiale, esente da royalty, non esclusiva per fabbricare, far fabbricare, usare, offrire in vendita, vendere, importare e altrimenti trasferire il tuo contributo, sia autonomamente sia come parte del progetto — nella misura in cui le tue rivendicazioni di brevetto sono necessariamente violate dal contributo di per sé o dalla sua combinazione con il progetto a cui è stato inviato. I termini seguono §3 di Apache-2.0, indipendentemente dalla directory in cui il contributo è atterrato. Se intenti un'azione legale per brevetto contro chiunque (inclusa una riconvenzione) sostenendo che i materiali del progetto violano il tuo brevetto, allora tutte le licenze **brevettuali** a te concesse dal progetto e dai suoi contributori secondo questa clausola e secondo le licenze del progetto terminano a partire dalla data di deposito dell'azione legale.

## 2. DCO: una firma sulla provenienza

Ogni commit porta una sign-off (`git commit -s`), a significare l'accordo con il [Developer Certificate of Origin 1.1](https://developercertificate.org/): confermi di avere il diritto di inviare questo contributo sotto la licenza del progetto.

```
Signed-off-by: Nome Cognome <email@example.com>
```

Le PR senza sign-off non vengono mergeate; il controllo è automatico — il job CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) fa fallire la PR anche se un solo commit manca di sign-off. La protezione brevettuale del livello docs poggia esattamente su questa catena — nessuna eccezione.

**Spostare materiale tra livelli.** Il materiale vive nel livello in cui è atterrato (e sotto la licenza di quel livello). Spostare testo/codice tra livelli con licenze diverse è consentito solo se si tratta di materiale proprio, o con una nota esplicita della licenza originale del frammento.

## 3. Igiene brevettuale e protocollo sperimentale

- Ogni decisione tecnica deve ricondursi a una fonte libera — un brevetto scaduto o un paper tratto da [docs/01-prior-art.md](docs/01-prior-art.md). Implementazioni di rivendicazioni attive (elencate anch'esse lì) non sono accettate finché tali rivendicazioni non scadono.
- Risultati sperimentali — solo tramite il template [experiments/TEMPLATE.md](experiments/TEMPLATE.md): un protocollo datato e riproducibile è esattamente ciò che costituisce il nostro prior art.
- Le decisioni architetturali passano attraverso ADR in [docs/decisions/](docs/decisions/).
- Commenti al codice, docstring, identificatori e messaggi di commit sono solo in inglese. I docs sono multilingua (vedi sotto); le etichette visibili all'utente nelle figure vivono in `labels.json`.

## 4. Docs multilingua: modifica una lingua, la CI sincronizza le altre

L'inglese è primario e possiede i percorsi canonici. Ogni altra lingua è un albero mirror sotto [translations/](..) con nomi di file identici — markdown, il CSV della BOM e le figure generate incluse; il testo delle figure è guidato da `labels.json`. **Non** devi mantenere i mirror a mano:

- Modifica la lingua che ti è comoda. Al push, il workflow [Translation sync](../../.github/workflows/translate.yml) traduce le controparti con un LLM open-weights (`glm-5.2` su Ollama Cloud), rigenera le figure quando la sincronizzazione aggiorna `labels.json`, e committa il risultato con il marcatore `[translate-sync]`. Qualsiasi endpoint compatibile con OpenAI funziona — imposta `OPENAI_BASE_URL` e `TRANSLATE_MODEL`.
- Ciò che ancora richiede lavoro è tracciato in `translations/.sync-state.json`, che registra il contenuto primario da cui ogni traduzione è stata realizzata. Un'esecuzione interrotta da un limite di quota o da un timeout non perde quindi nulla: le coppie incomplete restano marcate come stale e vengono riprese al prossimo push o dall'esecuzione notturna. Non modificare a mano quel file.
- Se hai modificato **più** lingue di un doc tu stesso, ogni versione che hai toccato viene mantenuta come l'hai scritta; il bot riempie solo le lingue che non hai toccato.
- **`labels.json` è l'eccezione a "modifica qualsiasi lingua".** Le etichette delle figure fluiscono solo da primario → mirror. Modificare un'etichetta tradotta corregge quella lingua e si ferma lì; non torna indietro nell'inglese. Per cambiare ciò che un'etichetta *dice*, modifica la sezione primaria. Il motivo è l'asimmetria: una modifica a un'etichetta è quasi sempre qualcuno che corregge la formulazione della macchina, e permettere che questo riscriva il primario ridefinirebbe la fonte da cui tutti e quattordici i mirror vengono generati. Le chiavi che il bot non ha mai prodotto si propagano comunque all'indietro, quindi un'etichetta scritta a mano non rimane bloccata in una sola lingua.
- La traduzione automatica viene committata — dai un'occhiata al commit del bot e correggi la formulazione se manca il tono; la tua correzione non verrà sovrascritta (il bot registra la tua versione come quella corrente).
- Una risposta che è tornata troncata o con i placeholder di `labels.json` rovinati viene scartata invece di essere committata, e la coppia viene ritentata — quindi un vuoto dall'aspetto strano in un mirror è una coppia stale, non una decisione.
- **PR esterne:** il bot gira su `master`, quindi una PR può modificare una sola lingua — i mirror (incluso l'inglese) si aggiornano automaticamente subito dopo il merge. Non serve conoscere l'inglese per contribuire ai docs.
- **Aggiungere una lingua:** aggiungi il suo codice e nome a [i18n.json](../../i18n.json) (es. `"fr": "Français"`) e fai push — la pipeline costruisce l'intero mirror `translations/fr/`: ogni doc, una sezione `fr` in ogni `labels.json`, il set di figure e i selettori di lingua ovunque.
- **Script non latini:** la CI installa le famiglie Noto (`fonts-noto-core`, `fonts-noto-cjk`) e i renderer percorrono lo stack di font in `i18n.json` → `render.fonts`, quindi cirillico, Han, kana e Hangul vengono renderizzati correttamente. Un renderer ora verifica la copertura dei glifi prima di disegnare e **fallisce invece di disegnare riquadri `.notdef`** — quel controllo esiste perché le figure cinesi sono state pubblicate come una griglia di tofu e niente nella CI guarda i pixel. Se si attiva, aggiungi il font Noto per quello script allo stack.
- **Script che richiedono shaping contestuale** — arabo e persiano (RTL, forme unite), devanagari e bengalese (congiunzioni) — non possono essere disegnati correttamente da matplotlib, che non ha un motore di shaping: anche con il font giusto i glifi escono non uniti e in ordine sbagliato. Elenca quelle lingue in `i18n.json` → `render.skip_figures`. Il loro testo in prosa non è affected; i loro docs si limitano a linkare le figure primarie, che la riparazione dei link in [tools/translate_sync.py](../../tools/translate_sync.py) punta automaticamente. `hi` è configurato in questo modo.
- **Guardia script:** `SCRIPTS` in [tools/i18n_render.py](../../tools/i18n_render.py) registra quale script le etichette di ogni lingua devono contenere. Una risposta che non ne ha nessuno — le sezioni `ja` una volta sono state pubblicate piene di russo — viene rifiutata e ritentata invece di essere committata. Una lingua mancante in quella tabella semplicemente non riceve guardia, quindi aggiungerne una a `i18n.json` non rompe mai; aggiungi la voce per ottenere il controllo.

## 5. Controlli che puoi eseguire prima del push

```bash
python tools/check_repo.py
```

Verifica ciò che il bot di traduzione è in grado di rompere e che nient'altro intercetterebbe: ogni link relativo si risolve, ogni sezione di `labels.json` corrisponde a `i18n.json` e porta le stesse chiavi e gli stessi placeholder `str.format` di quella primaria, ogni doc canonico ha un mirror in ogni lingua, e ogni file markdown ha la sua barra lingua. La CI lo esegue su entrambi i workflow; non richiede dipendenze.

Il resto della CI ([ci.yml](../../.github/workflows/ci.yml)) compila gli script ed esegue l'intera pipeline delle figure. Per riprodurla esattamente — incluse le figure committate — installa il toolchain fissato, non quello generico:

```bash
python -m pip install -r tools/requirements-ci.txt
```
