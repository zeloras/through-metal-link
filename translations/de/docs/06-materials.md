# Wandmaterialien jenseits von Stahl: Welche Wände Strom und Daten übertragen

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · Deutsch · [Português](../../pt/docs/06-materials.md) · [Español](../../es/docs/06-materials.md) · [Français](../../fr/docs/06-materials.md) · [Italiano](../../it/docs/06-materials.md) · [Polski](../../pl/docs/06-materials.md) · [Türkçe](../../tr/docs/06-materials.md) · [Українська](../../uk/docs/06-materials.md) · [Tiếng Việt](../../vi/docs/06-materials.md) · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

Der Rest dieses Repos geht von Stahl aus. Diese Seite stellt die einfachere, größere Frage: **für welche Wandmaterialien funktioniert der Zwei-Wandler-Kanal überhaupt**, und in welchem Modus? Es handelt sich um eine Simulationsstudie (`--mock`-artig, keine Labordaten — Intuition dafür, was ein Hardware-Experiment verdient), aufgebaut aus demselben semi-empirischen Modell wie [channel_sim](../../../software/simulator/channel_sim.py) und erweitert um Volumenabsorption.

Erzeugen mit: `python3 software/simulator/material_map.py` (benötigt numpy + matplotlib). Modell und Annahmen: [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## Das Modell in einer Minute

Drei Größen entscheiden, ob eine Wand überhaupt nutzbar ist und für wie viel Leistung:

1. **Impedanzkontrast und Phase** — das verlustfreie Fabry–Perot-Schichtmodell, identisch mit [channel_sim](../../../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_wall / Z_couplant, Kopplungsmedium Z = 1,5 MRayl (Fett).
   Bei einer Halbwellen-Resonanz (f = c/2d) ist eine verlustfreie symmetrische Schicht *unabhängig von r* vollständig transparent; der Kontrast r bestimmt, wie **breit** die Kammzinken sind (Toleranz gegenüber Frequenzfehlern), die Schallgeschwindigkeit c bestimmt, wie weit sie auseinander liegen (Δf = c/2d).
2. **Volumenabsorption**, unsichtbar für das verlustfreie Modell und der Entscheider für Kunststoffe, Beton und Gummi:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, einfach, longitudinal],
   wobei α₁ₘₕᶻ der Wert bei 1 MHz ist.
   γ ≈ 1 = viskoser/Relaxationsverlust; γ > 2 = Streuung an Inhomogenitäten (Betonzuschlag).
3. **Die Dosis, die die Wand zurückgibt** — siehe Abschnitt [unten](#die-dosis-was-die-welle-der-wand-antut-frequenz-für-frequenz): Spannung σ = √(2·I·Z), die *nicht* von der Frequenz abhängt, und Selbsterwärmung ΔT ∝ α(f)·I, die davon abhängt.

**Annahmen, dort genannt, wo der Code sie nennt:** typische Handbuchwerte (Longitudinalwelle, ~20 °C); reale Chargen variieren — Korn, Füllstoffe, Zuschläge, Aushärtung. Alles unten ist eine Rangliste, kein Datenblatt.

| Wand | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | Kamm Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | Anmerkung |
|---|---|---|---|---|---|---|---|---|
| Stahl | 7850 | 5900 | 46,3 | 0,02 | 590 | 148 | 0,21 | feinkörniger Baustahl |
| Aluminium | 2700 | 6320 | 17,1 | 0,02 | 632 | 158 | 0,69 | 6061-Klasse |
| Titan | 4430 | 6100 | 27,0 | 0,03 | 610 | 152 | 0,45 | Ti-6Al-4V |
| Kupfer | 8960 | 4760 | 42,6 | 0,05 | 476 | 119 | 0,17 | dicht, sehr hohes Z |
| Borosilikatglas | 2230 | 5640 | 12,6 | 0,01 | 564 | 141 | 0,77 | sehr geringer Verlust |
| Aluminiumoxid-Keramik | 3890 | 9900 | 38,5 | 0,08 | 990 | 248 | 0,51 | schneller Schall, geringer Verlust |
| PMMA (Acryl) | 1180 | 2690 | 3,2 | 2,5 | 269 | 67 | 0,95 | transparent, absorptionsbegrenzt bei MHz |
| PVC (hart) | 1400 | 2380 | 3,3 | 6 | 238 | 60 | 0,92 | verlustreicher als PMMA |
| HDPE | 950 | 2340 | 2,2 | 12 | 234 | 58 | 0,98 | weich, verlustreich |
| Beton | 2300 | 3500 | 8,1 | 5 | 350 | 88 | 0,77 | Zuschlagstreuung dominiert; variiert um Größenordnungen |
| Gummi (gefüllt) | 1100 | 1500 | 1,6 | 60 | 150 | 38 | 0,85 | das ehrliche Sackgasse |

## Die Plots

**Modus B (MHz) — der Dickenkamm pro Material.** Links: Konstruktionsmetalle; rechts: Nichtmetalle. Alle Wände 5 mm, Fettkopplung. Verlustfreie Modellpeaks erreichen T = 1 an exakten Resonanzen; reale Peaks sind niedriger durch Kontaktverluste, und Absorption begrenzt die verlustreichen Materialien direkt:

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**Die Materialkarte** — die beiden Achsen, die alles entscheiden: Impedanz (Kopplungs-/Kontaktschwierigkeit) vs. 1-MHz-Absorption (MHz-Tauglichkeit). Hoher Z-Wert + niedriges α ist die Power-Grade-Ecke; niedriger Z-Wert + hohes α bedeutet „40 kHz noch offen, MHz tot"; die Gummi-Ecke ist eine Sackgasse bei jeder Frequenz, die wir anvisieren:

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Modus A (40 kHz) Kopplungsproxy** — dasselbe Übertragungsmodell, ausgewertet bei 40 kHz durch eine 3-mm-Wand, normiert auf Stahl. *Eine Rangliste, keine Watt:* das resonante Langevin-Paar multipliziert jeden Balken grob gleich und das Modell hat keine Wandlerbelastung im Inneren; dieser Multiplikator ist Stage-2-Territorium ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## Was der Sweep sagt

- **Bei 40 kHz koppeln niedrig-Z-Wände (Kunststoffe, Gummiauskleidung) *leichter* als Stahl** — durch Fett sind sie fast impedanzangepasst, daher ist der Kamm breit und die Übertragung pro Durchgang hoch. Was Kunststoffe bei höheren Frequenzen tötet, ist **Volumenabsorption**, nicht Kontakt oder Impedanz. Die Materialleiter bei 40 kHz ist daher gegenüber der Intuition invertiert: HDPE/PMMA/PVC > Glas/Beton > Aluminium > Aluminiumoxid > Titan > Stahl > Kupfer — mit dem starken Vorbehalt, dass die 40-kHz-Zahl der Gummisorten α linear von 1 MHz nach unten extrapoliert, was die Viskoelastizität nicht garantiert.
- **Modus B teilt Materialien sauber.** Metalle, Glas und Aluminiumoxid nehmen MHz mit vernachlässigbarer Absorption (α ≤ 0,1 dB/cm); der Kamm ist *scharf* für hoch-Z-Wände (Stahl, Aluminiumoxid — braucht Frequenz-Tracking, die ~6 % ⇒ ~10×-Lektion von [00-theory](00-theory.md)) und *breit* für Glas/PMMA (tolerant, aber PMMA zahlt ~1,3 dB einfach bei 1 MHz durch 5 mm — nur mW-Klasse).
- **Beton ist ein 40-kHz-Material, kein MHz-Material.** Zuschlagstreuung (λ bei 1 MHz ≈ 3,5 mm ≈ Zuschlagsgröße) treibt γ auf ~2,5 und tötet MHz; die Ultraschall-Puls-velocity-Praxis (40–80 kHz durch ≥1 m Pfade) ist exakt Modus A.
- **Die Batteriepack-Nische ([05](05-applications-map.md)) ist akustisch günstig:** eine 2–3 mm Aluminiumwand hat einen Kopplungsproxy von ~3× dem von Stahl und vernachlässigbare Absorption — der Vorzeigefall ist auch der einfache Fall.
- **Die Frequenzleiter, für die man im Modus B planen sollte** (5 mm Wand, erster Kamm): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, Kupfer ≈ 480, Stahl ≈ 590, Titan ≈ 610, Aluminium ≈ 630, Glas ≈ 560, Aluminiumoxid ≈ 990. Dünnere Wand ⇒ proportional höher.

## Die Dosis: was die Welle der Wand antut, Frequenz für Frequenz

Übertragung beantwortet „wie viel kommt durch"; dieser Abschnitt beantwortet die umgekehrte Frage — **wie viel der Welle in der Wand bleibt, und schadet das?** Schaden durch Welle-in-Wand hat genau zwei Gesichter:

- **Spannung** σ = √(2·I·Z) — ebene Wellenimpuls; *frequenzunabhängig*. Vergleiche gegen die Dauerfestigkeitsgrenze (Metalle), Biege-/Zugfestigkeit (Keramik, Glas, Beton, Gummi).
- **Selbsterwärmung** ΔT = α(f)·I·d²/(8k), stationär, beide Seiten gekühlt — *frequenzabhängig* über α(f), und genau hier greift die Frequenz: jedes isolierende Material hat einen Knick, oberhalb dessen jede zusätzliche Oktave der Frequenz die abgelagerte Wärme multipliziert.

Bei 1 W/cm² (bereits jenseits dessen, was dieses Projekt anvisiert: das Stage-2-Ziel von 0,5–5 W verteilt über eine ~19 cm² Wandlerfläche ist 0,03–0,26 W/cm²):

| Wand | σ @1 W/cm², MPa | Grenze σ_e, MPa | Spannungsreserve | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | Decke @40 kHz, W/cm² | Decke @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| Stahl | 0,96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| Aluminium | 0,58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| Titan | 0,74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| Kupfer | 0,92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| Borosilikatglas | 0,50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| Aluminiumoxid-Keramik | 0,88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (Acryl) | 0,25 | 15 | 60× | 0,2 | 9,5 | 65 | ~100 | 2,1 |
| PVC (hart) | 0,26 | 15 | 58× | 0,6 | 28,8 | 199 | ~33 | 0,7 |
| HDPE | 0,21 | 8 | 38× | 0,15 | 19,2 | 215 | ~58 | 1,0 |
| Beton | 0,40 | 2,5 | 6× | ~0 | 2,1 | 118 | 1,6 | 1,6 |
| Gummi (gefüllt) | 0,18 | 1,5 | 8× | 11,5 | 288 | 1440 | 1,7 | 0,07 |

„Decke" = kontinuierliche Intensität, bei der die Wand innerhalb von 20 % ihrer Dauerfestigkeits-/Festigkeitsgrenze und unter +20 K Selbsterwärmung bleibt (stationär, beide Seiten auf Umgebungstemperatur gehalten). Getaktete Betriebe erhitzen weniger; eine Wand, die nur an einer Seite verankert ist — der Normalfall, Luft auf einer Seite — erhitzen sich an der freien Seite bis zu 4× mehr. Diese Zahlen sind ein erster Schnitt, keine Konstruktionsgarantie. Eine Konventions-Anmerkung: die α-Werte sind Intensitäts-dB (10·log₁₀, die Dosimetrie-Konvention — ein 3-dB-Abfall halbiert I); Pulse-Echo-NDT-Literatur, die Amplituden-dB (20·log₁₀) zitiert, beschreibt dasselbe α mit doppelt so großen Zahlen — prüfen Sie, welche Konvention eine Quelle verwendet, bevor Sie ihre Zahlen in diese Tabelle übernehmen.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

Was der Dosis-Sweep sagt:

- **Das Stahl-Urteil von [00-theory](00-theory.md) gilt und verallgemeinert sich**: jedes Konstruktionsmetall trägt 1 W/cm² mit Reserven von 65–680× in der Spannung und Mikro-Kelvin an Selbsterwärmung. Metalle sind im Schadenssinn frequenzunempfindlich — ihr Verlust ist zu gering, um bei jeder Leistung, die wir koppeln können, zu erhitzen.
- **Frequenzschaden an Polymeren ist thermisch, nicht mechanisch.** PMMA's Spannungsreserve ist ein komfortables 60× selbst bei 1 W/cm², aber der Erwärmungsknick liegt genau um 1 MHz: gutartig (~0,2 K) bei 40 kHz, +9,5 K bei 1 MHz, +65 K bei 5 MHz — Erweichungsgebiet bei wenigen W/cm². PVC überschreitet die +10-K-Linie bereits bei ~0,35 W/cm² @ 1 MHz; Gummi absorbiert ~288 K pro W·cm⁻² bei 1 MHz (und ~12 K selbst bei 40 kHz) — hysteretische Erwärmung ist *der* Grund, warum elastomergefütterte Wände sterben, nicht der Kamm. HDPE teilt den Unterschied und erinnert sich an seinen Schmelzpunkt: +215 K pro W·cm⁻² bei 5 MHz.
- **Beton's enge Reserve ist Zug-, nicht thermisch**: 0,40 MPa Wellenspannung gegen eine ~2,5 MPa statische Zugfestigkeit (Dauerfestigkeit noch niedriger) lässt nur eine ~6×-Reserve bei 1 W/cm². Das 40–80-kHz-Regime bleibt bei der Leistungsdichte des Projekts in Ordnung; konzentrierte Multi-W/cm²-Strahlen in Beton sollten vermieden werden, MHz doppelt (Streuung erhitzen die Zuschlagsgrenzflächen).
- **Fazit für die Roadmap:** bei Modus-A-Leistungsdichten (≤0,3 W/cm²) ist kein Feststoff in der Tabelle gefährdet — Spannungsreserven ≥11× (die engste ist Beton's Zugdauerfestigkeit bei 11×; alles andere ≥15×) und Erwärmung ≤0,2 K für jeden technischen Feststoff (Gummi, die Ausnahme, die niemand anvisiert, ~3,5 K). Die Schadenskarte rechtfertigt den Plan des Projekts, die Leistung zu steigern: die ersten echten Materialgrenzen erscheinen *oberhalb* der Stage-2-Ziele, zuerst in Flüssigkeiten (Kavitation, die ≤1-W/cm²-Regel von [00-theory](00-theory.md)), dann in Beton's Zugdauerfestigkeit, dann in Polymeren bei MHz. Die Teile, die bei hoher Leistung tatsächlich beobachtet werden müssen, bleiben die Piezokeramik und die Klebenaht — [02-safety](02-safety.md) — nicht die Wand.

## Urteil pro Material

| Wand | Modus A — 40-kHz-Leistung | Modus B — MHz-Leistung/Daten | Urteil |
|---|---|---|---|
| Stahl | ✓✓ Referenz | ✓ scharfer Kamm — Frequenz tracken | die Basislinie |
| Aluminium | ✓✓ (Proxy ~3× Stahl) | ✓ scharf-ish Kamm | beste Konstruktionswand (Batterien!) |
| Titan | ✓✓ | ✓ scharf-ish, geringer Verlust | korrosive/heiße Nischen, Drohnen, Rümpfe |
| Kupfer | ✓ (schwerste Kopplung der Metalle) | ✓ | Nische: versiegelte Stromschienen/elektrochemische Zellen |
| Borosilikatglas | ✓✓ | ✓ breitester Kamm — am nachsichtigsten | Labortfenster, Sichtfenster |
| Aluminiumoxid-Keramik | ✓✓ | ✓ schnellste Kämme (990 kHz @ 5 mm), geringer Verlust | heiße/isolierende Prozesswände |
| PMMA | ✓ breitbandig | ⚠ mW-Klasse ≤ ~0,5 MHz nur | Tanks, Gehäuse; keine Leistungswand bei MHz |
| PVC / HDPE | ✓ dünne Wände | ✗ Absorption | minderwertige Gehäuse, datenarme Knoten |
| Beton | ✓ 40–80 kHz (UPV-Praxis) | ✗ Streuung | Fundamente, Rohre — nur Modus A |
| Gummi (gefüllt) | ⚠ Modellextrapolation unvalidiert | ✗ | empirisch die Sackgasse — [04](04-hybrid-channels.md) |

Eine niedrig-Z-Kunststoffwand hat mehr Spielraum für *ausrichtungsfehler-tolerante* Modus-A-Verbindungen, liefert aber weniger absolute Leistungsreserve gegen Absorption, sobald man über ~200 kHz geht; messen, bevor man etwas verspricht.

## Beton mit Bewehrung — der Mehrschichtfall

Echter Beton ist nie rein: Bewehrungsmatten sitzen in einer Betondeckung, und das 1D-Einschicht-Modell oben kann sie nicht sehen. `chart_rebar` / `rebar_table` erweitern das Modell auf allgemeine Stacks ([`stack_transmission`](../../../software/simulator/material_map.py), exakte Mehrschichtrekursion mit Schichtabsorption, im Self-Check abgesichert). Modellgeometrie: eine 150-mm-Konstruktionswand, eine Stahlmatte mit planarer Ersatzdicke Ø16 mm bei 40 mm Deckung; das *planare* Modell ist der Worst Case — ein echter Stab schattiert nur den Teil des Strahls, den er schneidet, also betrachten Sie diese als Hüllkurven-Dips, nicht als Vorhersagen:

| Stack (150 mm Beton) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| rein 150 mm | 0,135 | 0,133 | 8.9e-09 |
| Bewehrung Ø16 @ 40 mm | 0,013 | 0,069 | 6.6e-09 |
| zwei Matten Ø16 @ 40 mm | 0,003 | 0,001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

Was das Stack-Modell sagt:

- **Eine planare Matte unter dem Strahl kostet ×10 bei exakt 40 kHz** (Stopband-Interferenz von der Stahlschicht), aber der Dip ist schmal: bei 100 kHz verliert derselbe Stack nur ×2. Die praktische Lesart für die Pipeline-/Autoklav-Nische: *ein Frequenz-Scan um 40–120 kHz, keine feste Frequenz*, bringt eine Modus-A-Verbindung an der Bewehrung vorbei — und die Dips verschieben sich mit der Betondeckung, sodass ein Scan auch die Geometrie fingerprintet (die Grundlage einer Bewehrungstiefen-Schätzung).
- **Eine zweite Matte (ein Netz) ist in diesem Worst Case nahezu ein Wand-Killer** (×45 runter und breitbandig-flach nahe 40–100 kHz): dichte Bewehrung im Pfad ist der ehrliche „wähle eine andere Stelle an der Wand"-Indikator, kein Signalverarbeitungsproblem.
- **Modus B durch Konstruktionsbeton ist tot mit oder ohne Bewehrung** (1e-8-Niveau bei 1 MHz: 5 dB/cm × 15 cm). Bewehrung kommt bei MHz gar nicht erst ins Spiel.
- Vorbehalte, in der Reihenfolge der Wichtigkeit: Planarschichtannahme (Worst Case — ein Ø16-Stab blockiert deutlich weniger als die Hälfte eines 40–50-mm-Strahlquerschnitts), Welle-parallel-zu-Bewehrungsachse angenommen, und 1D-Ausbreitung (keine Beugung um den Stab). Das richtige Hardware-Experiment ist ein Scan-Rig auf einer echten Platte: kartiere T(x, y) bei 40/80/120 kHz über ein Bewehrungsraster und fitte die Dip-Positionen des planaren Modells an die Rasterteilung.

## Was ein Hardware-Follow-up messen sollte

Bevor man einer spezifischen Platte vertraut: Zwei-Dicken-Methode pro Material (zwei Platten mit d und 2d bei gleichem Kontakt), um reales α(f) und c zu extrahieren — dieser eine Datensatz ersetzt jede Zeile der Tabelle oben. Natürliche Bonus-Durchläufe innerhalb der bestehenden Protokolle: Wiederhole den Experiment-[001](../experiments/001-sweep-map-3mm-steel/README.md)-Sweep auf einer 5-mm-PMMA-Platte, einer Borosilikat- oder 99%-Aluminiumoxid-Platte und einem Betonblock bekannten Grads; erwarte einen *niedrigeren, aber breiteren* Peak bei den Kunststoffen, einen scharfen Kamm bei den Keramiken und einen temperaturabhängigen Kontakt überall. Während des Experiment-[002](../experiments/002-watts-3mm-steel/README.md)-Leistungslaufs ein IR-Thermometer (oder ein feines Thermoelement) an die Fernseite jedes Wandtyps schnallen — der gemessene ΔT bei bekannter Eingangsleistung ist die eine Zahl, die die Erwärmungsspalte der Dosis-Tabelle validiert oder tötet. Nichts auf dieser Seite ist gemessen — es ist die Karte dessen, was man zuerst messen sollte.
