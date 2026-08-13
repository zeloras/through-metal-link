# Treiber (Stufe 2): IR2110 Halbbrücke

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · Deutsch · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Schaltplan:** [../schematics/sch1-driver-halfbridge.png](../schematics/sch1-driver-halfbridge.png) (generiert von [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

Die Kette: Pi (SPI) → AD9833 **im Rechteckwellenmodus** (OPBITEN-Bit: MSB zur Ausgabe geroutet, Rail-to-Rail-Schwingung — kein separater Komparator erforderlich) → **74HC14 + RC + 1N4148** Formgeber (komplementärer HIN/LIN mit ~1 µs Totzeit) → IR2110 → 2×IRF540 (Halbbrücke) → 1 µF Gleichspannungs-Entkopplungskondensator → Anpassungstransformator (Ferrit, ~1:3..1:5, abstimmen auf dem Werkbank) → Langevin-Wandler TX.

Die Sinusausgabe des AD9833 (~0,6 Vpp) ist für die IR2110-Logik nicht geeignet — wenn Sie aus einem bestimmten Grund eine Sinusausgabe aus dem DDS benötigen, setzen Sie einen Komparator dazwischen (z. B. einen LM393, nicht im BOM).

Stromversorgung der Leistungsstufe: 12–24 V Labor-Netzgerät mit Strombegrenzung (**beginnen Sie bei 0,2 A**).

Hinweis: Die Sweep-Steuerung der Stufe 1 treibt das Piezo direkt mit dem schwachen DDS-Sinus (~0,6 Vpp, siehe `sweep_map.py`) an — **dieser Treiber tritt in die Kette nur bei der Stufe 2 (Watt) ein**. Erwarten Sie nicht ≥0,5 W von der Stufe-1-DDS-Only-Verbindung.

Hinweise:
- Der Langevin-Wandler ist eine kapazitive Last (typischerweise einige nF). Ein Reiheninduktor oder Anpassungstransformator ist obligatorisch; ohne diesen dissipieren die MOSFETs den reaktiven Strom und überhitzen.
- **Anpassungstransformator (der übliche Fehlerpunkt).** Beginnen Sie mit einem kleinen Ferrit-Toroid (z. B. FT50-43 / ähnlich), Primärwicklungen einige Windungen, Sekundärwicklungen ~3–5× so viele, Reihen-DC-Block 1 µF Folienkondensator an der Primärseite. Stimmen Sie auf den minimalen Stromversorgungs-Strom *bei der Resonanz der Stufe 1* ab, wenn der TX **an der Platte befestigt** und der RX belastet ist. Das Verhältnis der Windungen und die Streuung sind empirisch — das Schema markiert sie mit `*` aus einem Grund. Notieren Sie die endgültigen Windungen im Experimenten-Logbuch.
- **Totzeit**: Die IR2110 erzeugt diese nicht selbst. Die diskrete-Komponenten-Option — RC+1N4148 an den 74HC14-Eingängen (verzögert nur steigende Flanken, ~1 µs; mit einer Periode von 25 µs bei 40 kHz ist das <5% Verlust). Die einfache Option — ein EGS002-Modul, alles ist bereits integriert.
- **3,3 V Logik**: Versorgen Sie die IR2110-VDD mit dem gleichen 3,3 V wie die AD9833 und 74HC14 — bei VDD=5 V liegt der VIH-Schwellenwert bei ≈ 3,1 V und eine 3,3 V-Rechteckwelle kommt gerade noch durch (das Datenblatt erlaubt VDD bis hinunter zu 3,3 V).
- **Entkopplung ist obligatorisch**: 100 nF bei VDD und VCC (VCC — plus 47 µF) und an der Stromversorgungsleitung 470–1000 µF + 100 nF Keramik direkt an den Halbbrückenbeinen — ohne diese nimmt eine Halbbrücke auf einem Prototypen-Breadboard ihre eigenen Schaltspitzen auf. Halten Sie die Stromschleifen-Kabel kurz; wenn der Schaltpunkt stark oszilliert, wechseln Sie vom Breadboard zu einer kupferbeschichteten Tot-Bug-/Protoboard-Masse, bevor Sie die Strombegrenzung erhöhen.
- **Erster Einschaltvorgang** (abgestimmt mit [docs/02-safety.md](../../docs/02-safety.md)):
  1. Kein Langevin auf der Sekundärseite. Stromversorgung = 12 V, Strombegrenzung 0,2 A. Oszilloskop-Gate-Antrieb (HIN/LIN) und Schaltpunkt — bestätigen Sie die Totzeit und keinen Durchschlag.
  2. Passen Sie den Anpassungstransformator + TX-Langevin **an der Stahlplatte befestigt** (oder einem dicken Opfer-Metallblock) an. Nach wie vor 0,2 A Begrenzung. Heben Sie bei der Resonanzfrequenz der Stufe 1 nur so lange an, bis Sie den Strom und die RX-Spannung sehen.
  3. Erhöhen Sie die Strombegrenzung allmählich, während Sie die Temperatur der MOSFETs und des Transformators beobachten. Lassen Sie niemals einen ungesicherten Langevin bei Strom — Freiluft-Vollstrom-Läufe sind, wie Keramik bricht und Treiber sterben.

TODO: KiCad-Projekt (PCB) sobald der Prototyp auf einem Breadboard (oder Tot-Bug) überprüft wurde. Bis dahin sind die Schaltpläne in [`../schematics/`](../schematics/) die Quelle der Wahrheit für das Design.
