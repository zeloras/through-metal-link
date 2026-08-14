# Driver (stadio 2): half-bridge IR2110

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · Italiano · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Schema:** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) (generato da [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

La catena: Pi (SPI) → AD9833 **in modalità onda quadra** (bit OPBITEN: MSB instradato all'uscita, oscillazione rail-to-rail — nessun comparatore separato necessario) → **74HC14 + RC + 1N4148** shaper (HIN/LIN complementari con ~1 µs di dead time) → IR2110 → 2×IRF540 (half-bridge) → condensatore di blocco DC da 1 µF → trasformatore di adattamento (ferrite, ~1:3..1:5, regolare sul banco) → trasduttore Langevin TX.

L'uscita sinusoidale dell'AD9833 (~0,6 Vpp) non va bene per la logica dell'IR2110 — se per qualche motivo serve specificamente un'uscita sinusoidale dal DDS, mettere un comparatore tra i due (es. un LM393, non in BOM).

Alimentazione stadio di potenza: alimentatore da banco 12–24 V con limitazione di corrente (**partire da 0,2 A**).

Nota: lo sweep di stadio 1 pilota il piezo direttamente con il segnale sinusoidale debole del DDS (~0,6 Vpp, vedi `sweep_map.py`) — **questo driver entra nella catena solo allo stadio 2 (watt)**. Non aspettarsi ≥0,5 W dal collegamento solo-DDS di stadio 1.

Note:
- Il trasduttore Langevin è un carico capacitivo (tipicamente pochi nF). Un induttore in serie o un trasformatore di adattamento è obbligatorio; senza di esso i MOSFET dissipano la corrente reattiva e si bruciano.
- **Trasformatore di adattamento (il solito punto di guasto).** Partire con un piccolo toroide in ferrite (es. FT50-43 / simile), primario poche spire, secondario ~3–5× tanto, condensatore film di blocco DC in serie da 1 µF sul primario. Regolare per la corrente minima dell'alimentatore *alla risonanza di stadio 1* con il TX **fissato alla piastra** e l'RX caricato. Il rapporto spire e la dispersione sono empirici — lo schema li marca con `*` per un motivo. Registrare le spire finali nel log di esperimento.
- **Dead time**: l'IR2110 non lo genera da solo. L'opzione con componenti discreti — RC+1N4148 sugli ingressi del 74HC14 (ritarda solo i fronti di salita, ~1 µs; con un periodo di 25 µs a 40 kHz è una perdita <5%). L'opzione facile — un modulo EGS002, ha tutto integrato.
- **Logica 3,3 V**: alimentare il VDD dell'IR2110 dalla stessa linea 3,3 V di AD9833 e 74HC14 — a VDD=5 V la soglia VIH è ≈ 3,1 V e un'onda quadra a 3,3 V passa a malapena (il datasheet permette VDD fino a 3,3 V).
- **Disaccoppiamento obbligatorio**: 100 nF su VDD e VCC (VCC — più 47 µF), e sulla linea di alimentazione 470–1000 µF + 100 nF ceramico proprio ai rami dell'half-bridge — senza questo, un half-bridge su jumper di breadboard captano i propri spike di commutazione. Tenere corti i cavi del loop di potenza; se il nodo di commutazione oscilla violentemente, spostarsi dalla breadboard a una ground pour su protoboard in stile dead-bug con rame massiccio prima di aumentare la corrente.
- **Sequenza di prima accensione** (allineata con [docs/02-safety.md](../../docs/02-safety.md)):
  1. Nessun Langevin sul secondario per ora. Alimentatore = 12 V, limite di corrente 0,2 A. Osservare con l'oscilloscopio il pilotaggio dei gate (HIN/LIN) e il nodo di commutazione — confermare il dead time e l'assenza di shoot-through.
  2. Inserire il trasformatore di adattamento + TX Langevin **fissato alla piastra in acciaio** (o un blocco metallico di sacrificio spesso). Ancora limite 0,2 A. Alzare alla frequenza di picco di stadio 1 solo il tempo necessario per vedere corrente e tensione RX.
  3. Aumentare gradualmente il limite di corrente mentre si controlla la temperatura dei MOSFET e del trasformatore. Non lasciare mai un Langevin non fissato in potenza — le esecuzioni a piena potenza in aria libera sono il modo in cui le ceramiche si crepano e i driver muoiono.

TODO: progetto KiCad (PCB) quando il prototipo su breadboard (o dead-bug) sarà validato. Fino ad allora gli schemi in [`../schematics/`](../../../../hardware/schematics) sono la fonte di verità del progetto.
