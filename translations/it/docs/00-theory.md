# Teoria del canale (il minimo indispensabile per lavorare)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · [Português](../../pt/docs/00-theory.md) · [Español](../../es/docs/00-theory.md) · [Français](../../fr/docs/00-theory.md) · Italiano · [Polski](../../pl/docs/00-theory.md) · [Türkçe](../../tr/docs/00-theory.md) · [Українська](../../uk/docs/00-theory.md) · [Tiếng Việt](../../vi/docs/00-theory.md) · [中文](../../zh/docs/00-theory.md) · [日本語](../../ja/docs/00-theory.md) · [한국어](../../ko/docs/00-theory.md) · [हिन्दी](../../hi/docs/00-theory.md)

## Principio
Un elemento piezo TX premuto/incollato contro la parete eccita in essa un'onda longitudinale; un piezo RX sull'altro lato la riconverte in elettricità. La parete è un risonatore: alle risonanze di spessore (multipli di mezza lunghezza d'onda) la trasmissione è massima.

## Numeri chiave
Velocità del suono longitudinale nell'acciaio: ~5900 m/s.

| Spessore acciaio | Risonanza di mezza onda |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Lunghezza d'onda nell'acciaio: 148 mm @ 40 kHz; 5,9 mm @ 1 MHz.

## Due modalità
- **A (40 kHz, trasduttori Langevin).** Una piastra di 3–5 mm ≪ λ — si comporta come una membrana; la risonanza è impostata dalla coppia di trasduttori, non dalla parete. Più semplice e potente della modalità B — quella da cui iniziare. Prova di fattibilità in laboratorio (non un obiettivo da garage): NASA JPL ~24,5 kHz, centinaia di W fino a 1 kW attraverso 5 mm di Ti con hardware purpose-built.
- **B (0,6–1 MHz, dischi).** Risonanza di spessore della parete stessa, e netta (uno shift di frequenza ~6% ⇒ la trasmissione crolla ~10× nel modello Fabry–Perot). La classe di risultati RPI/Moss: centinaia di mW più dati a centinaia di kbit/s con accoppiamento e adattamento da laboratorio. Richiede tracking automatico di frequenza.

## Perdite principali
Disallineamento di risonanza nella coppia di trasduttori (i trasduttori Langevin economici variano di ±1 kHz), qualità del contatto acustico (epoxy > accoppiante a grasso spesso + morsetto > pressione a secco), disallineamento meccanico, deriva di risonanza con la temperatura. La risposta a tutto questo è la stessa: eseguire una mappa di sweep prima di ogni modifica alla configurazione.

## Effetto sulla parete e sul mezzo dietro di essa

Versione breve: ai livelli di potenza della piattaforma la parete e qualsiasi gas dietro di essa restano intatti. Un liquido dietro la parete influisce soprattutto *sul canale*; il canale inizia a influire *sul liquido* solo in prossimità della soglia di cavitazione. I numeri orientativi seguenti sono per la modalità A: 40 kHz, ~1 W/cm² in acciaio da 3 mm.

**Parete — nessuna deformazione, nessuna fatica, mai.** Velocità di particella v = √(2I/ρc) ≈ 21 mm/s ⇒ spostamento ≈ 80 nm, deformazione a onda piana ε = v/c ≈ 3,5·10⁻⁶. Due stime equivalenti di sollecitazione: elastica E·ε ≈ 0,7 MPa (E ≈ 200 GPa) e acustica p = Z·v ≈ 1,0 MPa (Z_acciaio ≈ 4,6·10⁷ Pa·s/m). L'acciaio cede a 250+ MPa e il suo limite di fatica è ~200 MPa — margine ancora >200× in entrambi i casi, e sotto il limite di fatica l'acciaio sopporta cicli illimitati. Le parti meccanicamente fragili sono altrove: la ceramica piezo (fragile, si depolarizza se surriscaldata) e la linea di incollaggio (l'epoxy si riscalda e si affatica per primo) — vedi [02-safety](../../../docs/02-safety.md).

**Gas dietro la parete — effetto zero.** Il disadattamento di impedenza acciaio→aria (~4,6·10⁷ vs ~400 Pa·s/m) trasmette una frazione dell'ordine di 10⁻⁵ della potenza. Nessun riscaldamento o agitazione misurabile; l'elettronica dentro un contenitore sigillato non nota il moto della parete su scala nm.

**Liquido dietro la parete — due direzioni:**

- *Liquido → canale (sempre).* L'acqua carica la faccia opposta con ~1,5 MRayl invece dell'aria: parte della potenza si irradia nel liquido, Q cala, il picco dello sweep si sposta e si allarga. La modalità B è la più colpita — il pettine di risonanza di spessore è calcolato per fronti acciaio–aria e si sposta con il carico liquido. La regola consolidata copre questo caso: **rieseguire lo sweep contro il contenitore reale e completo**, non fidarsi mai di uno sweep preso a vuoto. Beneficio collaterale: lo smorzamento del liquido accorcia il ringing del risonatore (τ), quindi l'occhio OOK si apre a bitrate più alti. Le bolle nel percorso (liquido in fermentazione!) disperdono fortemente — vedi la soluzione in [04-hybrid-channels](../../../docs/04-hybrid-channels.md).
- *Canale → liquido (solo ad alta potenza).* Pressione di picco irradiata in acqua: p ≈ ρc·v ≈ 1,5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0,3 atm. La soglia di cavitazione inerziale a 40 kHz in acqua ordinaria (gassosa) è ~1–2 atm, quindi a 1 W/cm² il margine è 3–10×. Ma p cresce come √potenza, e le onde stazionarie in un contenitore chiuso creano hot spot locali — decine di W/cm² continui in un serbatoio pieno di liquido possono raggiungere la soglia. Superarla significa degassaggio di CO₂, sonochimica (off-flavor nei prodotti alimentari) ed erosione per cavitazione a lungo termine della superficie interna (esattamente come puliscono gli ultrasuoni per pulizia). Limite pratico per potenza continua in pareti bagnate dal lato liquido: **≲1 W/cm²**. La modalità B è esclusa: a MHz la soglia è un ordine di grandezza più alto e le potenze sono centinaia di mW.

## Bilancio di potenza del ricevitore (orientativo)
LED 20 mW; ESP32 in duty-cycle 1–5 mW medi; radio BLE ~150 mW mentre la radio è accesa. Riserva: un supercondensatore da 1 F @ 3,3 V immagazzina E = ½CV² = 5,4 J. Quante trasmissioni questo consenta dipende dal tempo on-air: un breve evento di advertising BLE (~2–5 ms a ~150 mW) è solo ~0,3–0,8 mJ → dell'ordine di **10⁴ pacchetti** da un condensatore pieno; una connessione / burst lunga (~100 ms di radio accesa) è ~15 mJ → dell'ordine di **10² burst**. Il consumo medio deve comunque restare entro i watt raccolti (obiettivo di stadio-2 ≥0,5 W nel carico è il gate; finché non è misurato, trattare le bande multi-watt della modalità A sui grafici del simulatore come obiettivi, non come dati).
