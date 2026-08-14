# Come contribuire

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · Italiano · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Grazie per voler far avanzare il canale aperto attraverso l'acciaio. Le tre regole qui sotto non sono burocrazia — sono l'armatura brevettuale del progetto (vedi [LICENSES.md](LICENSES.md) per sapere perché).

## 1. Licenze dei contributi (in ingresso = in uscita)

Inviando un contributo, accetti che sia concesso in licenza allo stesso modo del resto del materiale nella sua directory:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Concessione di brevetto.** Inoltre — poiché CC-BY-4.0 non concede licenze sui brevetti — concedi al progetto e a tutti i destinatari dei suoi materiali una licenza brevettuale perpetua, irrevocabile, mondiale, esente da canoni, non esclusiva per fabbricare, far fabbricare, usare, offrire in vendita, vendere, importare e altrimenti trasferire il tuo contributo, sia autonomamente che come parte del progetto — nella misura in cui le tue rivendicazioni di brevetto sono necessariamente violate dal contributo di per sé o dalla sua combinazione con il progetto a cui è stato inviato. I termini seguono lo §3 di Apache-2.0, indipendentemente dalla directory in cui è stato inserito il contributo. Se intenti una causa per brevetto contro chiunque (inclusa una domanda riconvenzionale) sostenendo che i materiali del progetto violano il tuo brevetto, allora tutte le licenze **brevettuali** a te concesse dal progetto e dai suoi collaboratori ai sensi di questa clausola e delle licenze del progetto si estinguono a partire dalla data di deposito di tale causa.

## 2. DCO: una firma sulla provenienza

Signed-off-by: Firstname Lastname <email@example.com>
```

Le PR senza sign-off non vengono mergeate; il controllo è automatico — il job CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) fa fallire la PR anche se un solo commit manca della sign-off. La tutela brevettuale del layer docs si fonda esattamente su questa catena — nessuna eccezione.

**Spostare materiale tra layer.** Il materiale resta nel layer in cui è approdato (e sotto la licenza di quel layer). Spostare testo/codice tra layer con licenze diverse è consentito solo se si tratta di materiale proprio, oppure con una nota esplicita della licenza originale del frammento.

## 3. Igiene dei brevetti e protocollo sperimentale

- Ogni decisione tecnica deve ricondursi a una fonte libera — un brevetto scaduto o un paper tratto da [docs/01-prior-art.md](docs/01-prior-art.md). Le implementazioni di claim ancora in vigore (elencati anch'essi lì) non vengono accettate finché tali claim non scadono.
- Risultati sperimentali — solo tramite il template [experiments/TEMPLATE.md](experiments/TEMPLATE.md): un protocollo datato e riproducibile è esattamente ciò che costituisce il nostro prior art.
- Le decisioni di architettura passano attraverso ADR in [docs/decisions/](docs/decisions/).
- I commenti al codice, le docstring, gli identificatori e i messaggi di commit sono esclusivamente in inglese. I documenti sono multilingua (vedi sotto); le etichette delle figure visibili all'utente si trovano in `labels.json`.

## 4. Documentazione multilingue: modifica una lingua, la CI sincronizza le altre

L'inglese è la lingua principale e possiede i percorsi canonici. Ogni altra lingua è un albero mirror sotto [translations/](..) con nomi di file identici — markdown, il CSV della BOM e le figure generate incluse; il testo delle figure è guidato da `labels.json`. Non **devi** mantenere i mirror a mano:

- Modifica la lingua che ti è più comoda. Al push, il workflow [Translation sync](../../.github/workflows/translate.yml) traduce le controparti con un LLM open-weights (`glm-5.2` su Ollama Cloud), rigenera le figure quando la sincronizzazione aggiorna `labels.json`, e committa il risultato con il marker `[translate-sync]`. Qualsiasi endpoint compatibile con OpenAI funziona — imposta `OPENAI_BASE_URL` e `TRANSLATE_MODEL`.
- Ciò che richiede ancora lavoro è tracciato in `translations/.sync-state.json`, che registra il contenuto principale da cui è stata tratta ogni traduzione. Un'esecuzione interrotta da un limite di quota o da un timeout non perde quindi nulla: le coppie non finite rimangono segnate come stale e vengono riprese dal prossimo push o dall'esecuzione notturna. Non modificare a mano quel file.
- Se hai modificato **più** lingue di un documento tu stesso, ogni versione che hai toccato viene mantenuta come l'hai scritta; il bot riempie solo le lingue che non hai toccato.
- **`labels.json` è l'eccezione a "modifica qualsiasi lingua".** Le etichette delle figure fluiscono solo da principale → mirror. Modificare un'etichetta tradotta corregge quella lingua e si ferma lì; non torna indietro nell'inglese. Per cambiare ciò che un'etichetta *dice*, modifica la sezione principale. Il motivo è l'asimmetria: una modifica a un'etichetta è quasi sempre qualcuno che corregge la formulazione della macchina, e permettere che questo riscriva il principale ridefinirebbe la fonte da cui vengono generati tutti i quattordici mirror. Le chiavi che il bot non ha mai prodotto si propagano comunque all'indietro, quindi un'etichetta scritta a mano non rimane bloccata in una lingua.
- La traduzione automatica viene committata — dai un'occhiata al commit del bot e ritocca la formulazione se non coglie il tono; la tua correzione non verrà sovrascritta (il bot registra la tua versione come quella attuale).
- Una risposta che torna troncata o con segnaposto `labels.json` danneggiati viene scartata invece di essere committata, e la coppia viene ritentata — quindi un vuoto dall'aspetto strano in un mirror è una coppia stale, non una decisione.
- **PR esterni:** il bot gira su `master`, quindi una PR può cambiare solo una lingua — i mirror (incluso l'inglese) si aggiornano automaticamente subito dopo il merge. Non hai bisogno di conoscere l'inglese per contribuire ai documenti.
- **Aggiungere una lingua:** aggiungi il suo codice e nome a [i18n.json](../../i18n.json) (es. `"fr": "Français"`) e fai il push — la pipeline costruisce l'intero mirror `translations/fr/`: ogni documento, una sezione `fr` in ogni `labels.json`, il set di figure e i selettori di lingua ovunque.
- **Script non latini:** la CI installa le famiglie Noto (`fonts-noto-core`, `fonts-noto-cjk`) e i renderer percorrono lo stack di font in `i18n.json` → `render.fonts`, quindi cirillico, Han, kana e Hangul vengono renderizzati correttamente. Un renderer ora controlla la copertura dei glifi prima di disegnare e **fallisce invece di dipingere riquadri `.notdef`** — questo controllo esiste perché le figure cinesi sono state pubblicate come una griglia di tofu e niente nella CI guarda i pixel. Se si attiva, aggiungi il font Noto per quello script allo stack.
- **Script che necessitano di shaping contestuale** — Arabo e Persiano (RTL, forme unite), Devanagari e Bengalese (congiunzioni) — non possono essere disegnati correttamente da matplotlib, che non ha un motore di shaping: anche con il font giusto i glifi escono non uniti e nell'ordine sbagliato. Elenca queste lingue in `i18n.json` → `render.skip_figures`. La loro prosa non è interessata; i loro documenti si limitano a collegarsi alle figure principali, che la riparazione dei link in [tools/translate_sync.py](../../tools/translate_sync.py) punta automaticamente. `hi` è configurato in questo modo.
- **Guardia script:** `SCRIPTS` in [tools/i18n_render.py](../../tools/i18n_render.py) registra quale script le etichette di ogni lingua devono contenere. Una risposta che non ne ha nessuno — le sezioni `ja` una volta sono state pubblicate piene di russo — viene rifiutata e ritentata invece di essere committata. Una lingua mancante da quella tabella semplicemente non ottiene alcuna guardia, quindi aggiungerne una a `i18n.json` non si rompe mai; aggiungi la voce per ottenere il controllo.

## 5. Controlli eseguibili prima del push

python tools/check_repo.py
```

Verifica ciò che il bot di traduzione è in grado di rompere e che nient altro rileverebbe: ogni link relativo risolve correttamente, ogni sezione di `labels.json` corrisponde a `i18n.json` e porta le stesse chiavi e gli stessi segnaposto `str.format` di quella principale, ogni documento canonico ha un mirror in ogni lingua, e ogni file markdown ha la propria barra lingue. La CI lo esegue su entrambi i workflow; non richiede dipendenze.

Il resto della CI ([ci.yml](../../.github/workflows/ci.yml)) compila gli script ed esegue l'intera pipeline delle figure. Per riprodurla esattamente — figure commesse incluse — installare il toolchain fissato, non quello generico:

```bash
python -m pip install -r tools/requirements-ci.txt
