# Materiali di parete oltre l'acciaio: quali pareti trasportano potenza e dati

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · [Deutsch](../../de/docs/06-materials.md) · [Português](../../pt/docs/06-materials.md) · [Español](../../es/docs/06-materials.md) · [Français](../../fr/docs/06-materials.md) · Italiano · [Polski](../../pl/docs/06-materials.md) · [Türkçe](../../tr/docs/06-materials.md) · [Українська](../../uk/docs/06-materials.md) · [Tiếng Việt](../../vi/docs/06-materials.md) · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

Il resto di questo repo assume l'acciaio. Questa pagina pone la domanda più semplice e più grande: **per quali materiali di parete il canale a due trasduttori funziona del tutto**, e in quale modalità? È uno studio di simulazione (in stile `--mock`, senza dati di laboratorio — intuizione su cosa merita un esperimento hardware), costruito sullo stesso modello semi-empirico di [channel_sim](../../../software/simulator/channel_sim.py) ed esteso con l'assorbimento di bulk.

Genera: `python3 software/simulator/material_map.py` (richiede numpy + matplotlib). Modello e assunzioni: [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## Il modello in un minuto

Tre grandezze decidono se una parete è utilizzabile e per quanta potenza:

1. **Contrasto di impedenza e fase** — il modello a lastra Fabry–Perot senza perdite, identico a [channel_sim](../../../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_wall / Z_couplant, couplant Z = 1.5 MRayl (grasso).
   A una risonanza di mezz'onda (f = c/2d) una lastra simmetrica senza perdite è completamente trasparente *indipendentemente da r*; il contrasto r determina quanto sono **larghi** i denti del pettine (tolleranza all'errore di frequenza), la velocità del suono c determina quanto sono distanti (Δf = c/2d).
2. **Assorbimento di bulk**, invisibile al modello senza perdite e decisivo per plastiche, calcestruzzo e gomma:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, una via, longitudinale],
   dove α₁ₘₕᶻ è il valore a 1 MHz.
   γ ≈ 1 = perdita viscosa/relaxation; γ > 2 = scattering su inomogeneità (inerti del calcestruzzo).
3. **La dose che la parete restituisce** — vedi la sezione [sotto](#la-dose-cosa-londa-fa-alla-parete-frequenza-per-frequenza): tensione σ = √(2·I·Z), che *non* dipende dalla frequenza, e autoriscaldamento ΔT ∝ α(f)·I, che dipende.

**Assunzioni, dichiarate dove le dichiara il codice:** proprietà tipiche da manuale (onda longitudinale, ~20 °C); i materiali reali variano — grana, cariche, inerti, stagionatura. Tutto ciò che segue è una classificazione, non un datasheet.

| Parete | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | pettine Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | nota |
|---|---|---|---|---|---|---|---|---|
| acciaio | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | strutturale a grana fine |
| alluminio | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | classe 6061 |
| titanio | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| rame | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | denso, Z molto alta |
| vetro borosilicatico | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | perdite molto basse |
| ceramica allumina | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | suono veloce, perdite basse |
| PMMA (acrílico) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | trasparente, limitato da assorbimento a MHz |
| PVC (rigido) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | più perdente del PMMA |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | morbido, perdente |
| calcestruzzo | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | scattering degli inerti domina; varia di ordini di grandezza |
| gomma (caricata) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | l'onesto vicolo cieco |

## I grafici

**Modalità B (MHz) — il pettine di spessore per materiale.** A sinistra: metalli strutturali; a destra: non metalli. Tutte le pareti 5 mm, accoppiamento con grasso. I picchi del modello senza perdite raggiungono T = 1 alle risonanze esatte; i picchi reali sono più bassi per le perdite di contatto, e l'assorbimento blocca direttamente i materiali perdenti:

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**La mappa dei materiali** — i due assi che decidono tutto: impedenza (difficoltà di accoppiamento/contatto) vs assorbimento a 1 MHz (fattibilità a MHz). Z alta + α basso è l'angolo di potenza; Z bassa + α alto è "40 kHz ancora aperto, MHz morto"; l'angolo della gomma è un vicolo cieco a ogni frequenza che prendiamo di mira:

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Proxy di accoppiamento in modalità A (40 kHz)** — lo stesso modello di trasmissione valutato a 40 kHz attraverso una parete di 3 mm, normalizzato all'acciaio. *Una classificazione, non watt:* la coppia Langevin risonante moltiplica ogni barra all'incirca allo stesso modo e il modello non ha caricamento del trasduttore interno; quel moltiplicatore è territorio di stage-2 ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## Cosa dice lo sweep

- **A 40 kHz, le pareti a bassa Z (plastiche, rivestimenti in gomma) si accoppiano *più facilmente* dell'acciaio** — attraverso il grasso sono quasi adattate in impedenza, quindi il pettine è largo e la trasmissione per passaggio è alta. Ciò che uccide le plastiche a frequenze più alte è l'**assorbimento di bulk**, non il contatto o l'impedenza. La scala dei materiali a 40 kHz è quindi invertita rispetto all'intuizione: HDPE/PMMA/PVC > vetro/calcestruzzo > alluminio > allumina > titanio > acciaio > rame — con la forte avvertenza che il numero a 40 kHz delle gomme estrapola α linearmente verso il basso da 1 MHz, cosa che la viscoelasticità non garantisce.
- **La modalità B divide i materiali in modo netto.** Metalli, vetro e allumina reggono i MHz con assorbimento trascurabile (α ≤ 0.1 dB/cm); il pettine è *stretto* per le pareti ad alta Z (acciaio, allumina — richiede tracciamento di frequenza, la lezione ~6% ⇒ ~10× di [00-theory](00-theory.md)) e *largo* per vetro/PMMA (tollerante, ma il PMMA paga ~1.3 dB una via a 1 MHz attraverso 5 mm — solo classe mW).
- **Il calcestruzzo è un materiale da 40 kHz, non da MHz.** Lo scattering degli inerti (λ a 1 MHz ≈ 3.5 mm ≈ dimensione degli inerti) porta γ a ~2.5 e uccide i MHz; la pratica della velocità di pulso ultrasonico (40–80 kHz attraverso percorsi ≥1 m) è esattamente la modalità A.
- **La nicchia dei pacchi batteria ([05](05-applications-map.md)) è acusticamente favorevole:** una parete di alluminio di 2–3 mm ha un proxy di accoppiamento ~3× rispetto all'acciaio e assorbimento trascurabile — il caso di punta è anche il caso facile.
- **La scala di frequenze da pianificare in modalità B** (parete 5 mm, primo pettine): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, rame ≈ 480, acciaio ≈ 590, titanio ≈ 610, alluminio ≈ 630, vetro ≈ 560, allumina ≈ 990. Parete più sottile ⇒ proporzionalmente più alta.

## La dose: cosa l'onda fa alla parete, frequenza per frequenza

La trasmissione risponde a "quanto passa"; questa sezione risponde alla domanda inversa — **quanta parte dell'onda rimane nella parete, e la danneggia?** Il danno dell'onda-nella-parete ha esattamente due facce:

- **Tensione** σ = √(2·I·Z) — quantità di moto ad onda piana; *indipendente dalla frequenza*. Confrontare con il limite di fatica ad alto numero di cicli (metalli), resistenza flessionale/trazionale (ceramiche, vetro, calcestruzzo, gomma).
- **Autoriscaldamento** ΔT = α(f)·I·d²/(8k), stato stazionario, entrambe le facce raffreddate — *dipende dalla frequenza* attraverso α(f), ed è qui che la frequenza morde: ogni materiale isolante ha un ginocchio oltre il quale ogni ottava aggiuntiva di frequenza moltiplica il calore depositato.

A 1 W/cm² (già oltre ciò che questo progetto si prefigge: l'obiettivo di stage-2 di 0.5–5 W distribuito su una faccia trasduttore di ~19 cm² è 0.03–0.26 W/cm²):

| Parete | σ @1 W/cm², MPa | limite σ_e, MPa | margine di tensione | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | soffitto @40 kHz, W/cm² | soffitto @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| acciaio | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| alluminio | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| titanio | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| rame | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| vetro borosilicatico | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| ceramica allumina | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (acrílico) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (rigido) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| calcestruzzo | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| gomma (caricata) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

"Soffitto" = intensità continua alla quale la parete rimane entro il 20% del suo limite di fatica/resistenza e sotto +20 K di autoriscaldamento (stato stazionario, entrambe le facce mantenute a temperatura ambiente). Le esercitazioni a duty-cycle riscaldano meno; una parete ancorata su una sola faccia — il caso abituale, aria su un lato — si riscalda fino a 4× di più alla faccia libera. Questi numeri sono una prima stima, non una garanzia di progetto. Una nota sulle convenzioni: i valori di α sono intensity-dB (10·log₁₀, la convenzione dosimetrica — un calo di 3 dB dimezza I); la letteratura NDT pulse-echo che usa amplitude-dB (20·log₁₀) descrive lo STESSO α con numeri doppi — verificate quale convenzione usa una fonte prima di copiare i suoi numeri in questa tabella.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

Cosa dice lo sweep della dose:

- **Il verdetto sull'acciaio di [00-theory](00-theory.md) regge e si generalizza**: ogni metallo strutturale trasporta 1 W/cm² con margini di 65–680× in tensione e micro-kelvin di autoriscaldamento. I metalli sono insensibili alla frequenza in termini di danno — le loro perdite sono troppo piccole per riscaldarsi a qualsiasi potenza che possiamo accoppiare.
- **Il danno da frequenza sui polimeri è termico, non meccanico.** Il margine di tensione del PMMA è un comodo 60× anche a 1 W/cm², ma il ginocchio termico si trova proprio intorno a 1 MHz: benigno (~0.2 K) a 40 kHz, +9.5 K a 1 MHz, +65 K a 5 MHz — territorio di ammorbidimento a pochi W/cm². Il PVC supera la soglia dei +10 K già a ~0.35 W/cm² @ 1 MHz; la gomma assorbe ~288 K per W·cm⁻² a 1 MHz (e ~12 K anche a 40 kHz) — il riscaldamento isteretico è *il* motivo per cui le pareti rivestite di elastomero muoiono, non il pettine. L'HDPE si divide la differenza e ricorda il suo punto di fusione: +215 K per W·cm⁻² a 5 MHz.
- **Il margine stretto del calcestruzzo è trazionale, non termico**: 0.40 MPa di tensione d'onda contro una resistenza trazionale statica di ~2.5 MPa (fatica ancora inferiore) lascia solo un margine di ~6× a 1 W/cm². Il regime 40–80 kHz rimane fine alla densità di potenza del progetto; fasci concentrati multi-W/cm² nel calcestruzzo dovrebbero essere evitati, i MHz doppiamente (lo scattering riscalda le interfacce degli inerti).
- **Sintesi per la roadmap:** alle densità di potenza della modalità A (≤0.3 W/cm²) nessun solido nella tabella è in pericolo — margini di tensione ≥11× (il più stretto è la fatica trazionale del calcestruzzo a 11×; tutto il resto ≥15×) e riscaldamento ≤0.2 K per ogni solido ingegnerizzato (la gomma, l'eccezione che nessuno prende di mira, ~3.5 K). La mappa dei danni giustifica il piano del progetto di aumentare la potenza: i primi veri limiti materiali appaiono *sopra* gli obiettivi di stage-2, prima nei liquidi (cavitazione, la regola ≤1 W/cm² di [00-theory](00-theory.md)), poi nella fatica trazionale del calcestruzzo, poi nei polimeri a MHz. Le parti che richiedono davvero attenzione ad alta potenza rimangono la ceramica piezo e la linea di adesione — [02-safety](02-safety.md) — non la parete.

## Verdetto per materiale

| Parete | Modalità A — potenza 40 kHz | Modalità B — potenza/dati MHz | Verdetto |
|---|---|---|---|
| acciaio | ✓✓ riferimento | ✓ pettine stretto — tracciare la frequenza | la baseline |
| alluminio | ✓✓ (proxy ~3× acciaio) | ✓ pettine abbastanza stretto | migliore parete strutturale (batterie!) |
| titanio | ✓✓ | ✓ pettine abbastanza stretto, perdite basse | nicchie corrosive/calde, droni, scafi |
| rame | ✓ (accoppiamento più difficile tra i metalli) | ✓ | nicchia: sbarre sigillate/celle elettrochimiche |
| vetro borosilicatico | ✓✓ | ✓ pettine più largo — più tollerante | finestre da laboratorio, viewports |
| ceramica allumina | ✓✓ | ✓ pettini più veloci (990 kHz @ 5 mm), perdite basse | pareti di processo calde/isolanti |
| PMMA | ✓ banda larga | ⚠ classe mW ≤ ~0.5 MHz solo | serbatoi, custodie; non una parete di potenza a MHz |
| PVC / HDPE | ✓ pareti sottili | ✗ assorbimento | custodie di basso grado, nodi data-light |
| calcestruzzo | ✓ 40–80 kHz (pratica UPV) | ✗ scattering | fondamenta, tubazioni — solo modalità A |
| gomma (caricata) | ⚠ estrapolazione del modello non validata | ✗ | empiricamente il vicolo cieco — [04](04-hybrid-channels.md) |

Una parete di plastica a bassa Z ha più margine per link in modalità A *tolleranti al disallineamento* ma offre meno margine di potenza assoluta contro l'assorbimento una volta sopra ~200 kHz; misurare prima di promettere qualsiasi cosa.

## Calcestruzzo con armatura — il caso multistrato

Il calcestruzzo reale non è mai semplice: i teli di armatura si trovano a un copriferro, e il modello 1D a lastra singola sopra non può vederli. `chart_rebar` / `rebar_table` estendono il modello a stack generali ([`stack_transmission`](../../../software/simulator/material_map.py), ricorsione esatta multistrato con assorbimento per strato, verificata nel self-check). Geometria modellata: una parete strutturale di 150 mm, un telo di acciaio di spessore planare equivalente Ø16 mm a 40 mm di copriferro; il modello *planare* è il caso peggiore — una barra reale oscura solo la parte del fascio che interseca, quindi considerate questi come avvallamenti di inviluppo, non previsioni:

| Stack (calcestruzzo 150 mm) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| 150 mm semplice | 0.135 | 0.133 | 8.9e-09 |
| armatura Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| due teli Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

Cosa dice il modello a stack:

- **Un telo planare sotto il fascio costa ×10 a esattamente 40 kHz** (interferenza di stop-band dallo strato di acciaio), ma l'avvallamento è stretto: a 100 kHz lo stesso stack perde solo ×2. La lettura pratica per la nicchia pipeline/autoclave: *una scansione di frequenza intorno a 40–120 kHz, non una frequenza fissa*, è ciò che fa passare un link in modalità A oltre l'armatura — e gli avvallamenti si spostano con il copriferro, quindi una scansione anche impronta la geometria (la base di una stima della profondità dell'armatura).
- **Un secondo telo (una maglia) è quasi un muro-killer in questo caso peggiore** (×45 giù e piatto su banda larga vicino a 40–100 kHz): l'armatura densa nel percorso è l'onesto indicatore "scegli un altro punto della parete", non un problema di elaborazione del segnale.
- **La modalità B attraverso calcestruzzo strutturale è morta con o senza armatura** (livello 1e-8 a 1 MHz: 5 dB/cm × 15 cm). L'armatura non entra nemmeno nella storia a MHz.
- Avvertenze, in ordine di importanza: assunzione di strato planare (caso peggiore — una barra Ø16 blocca ben meno della metà della sezione di un fascio di 40–50 mm), onda parallela all'asse dell'armatura assunta, e propagazione 1D (nessuna diffrazione attorno alla barra). L'esperimento hardware giusto è un banco di scansione su una lastra reale: mappare T(x, y) a 40/80/120 kHz su una griglia di armatura e fittare le posizioni degli avvallamenti del modello planare al passo della griglia.

## Cosa dovrebbe misurare un follow-up hardware

Prima di fidarsi di qualsiasi piastra specifica: metodo dei due spessori per materiale (due piastre di d e 2d allo stesso contatto) per estrarre α(f) e c reali — quel singolo dataset sostituisce ogni riga della tabella sopra. Passaggi bonus naturali nei protocolli esistenti: ripetere lo sweep dell'esperimento [001](../experiments/001-sweep-map-3mm-steel/README.md) su una piastra di PMMA da 5 mm, una piastra di borosilicato o allumina al 99%, e un blocco di calcestruzzo di grado noto; aspettarsi un picco *più basso ma più largo* per le plastiche, un pettine netto per le ceramiche, e un contatto sensibile alla temperatura ovunque. Durante la prova di potenza dell'esperimento [002](../experiments/002-watts-3mm-steel/README.md), fissare un termometro IR (o una termocoppia fine) alla faccia opposta di ogni tipo di parete — il ΔT misurato a ingresso noto è l'unico numero che valida o uccide la colonna del riscaldamento della tabella della dose. Niente in questa pagina è misurato — è la mappa di cosa misurare per primo.
