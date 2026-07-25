# Treiber (Stufe 2): IR2110 Halbbrücke

> [English (primary)](README.md) · [Русский](README.ru.md) · Deutsch

**Schaltplan:** [../schematics/sch1-driver-halfbridge.de.png](../schematics/sch1-driver-halfbridge.de.png) (generiert von [../schematics/render_schematics.py](../schematics/render_schematics.py))

Die Kette: Pi (SPI) → AD9833 **im Rechteckwellenmodus** (OPBITEN-Bit: MSB zur Ausgabe geroutet, Rail-to-Rail-Schwingung — kein separater Komparator erforderlich) → **74HC14 + RC + 1N4148** Formgeber (komplementärer HIN/LIN mit ~1 µs Totzeit) → IR2110 → 2×IRF540 (Halbbrücke) → 1 µF Gleichspannungs-Entkopplungskondensator → Anpassungstransformator (Ferrit, ~1:3..1:5, abstimmen) → Langevin-Wandler TX.

Die Sinusausgabe des AD9833 (~0,6 Vpp) ist für die IR2110-Logik nicht geeignet — wenn Sie aus einem bestimmten Grund eine Sinusausgabe aus dem DDS benötigen, setzen Sie einen Komparator dazwischen (z. B. einen LM393, nicht im BOM).

Stromversorgung der Leistungsstufe: 12–24 V Labor-Netzgerät mit Strombegrenzung (beginnen Sie bei 0,2 A!).

Hinweis: Die Sweep-Steuerung der Stufe 1 treibt das Piezo direkt mit dem schwachen DDS-Sinus (~0,6 Vpp, siehe sweep_map.py) an — der Treiber tritt in die Kette bei der Stufe 2 (Watt) ein.

Hinweise:
- Der Langevin-Wandler ist eine kapazitive Last (nF); ein Reiheninduktor/Transformator ist obligatorisch, sonst verbrennen die MOSFETs aufgrund des reaktiven Stroms.
- **Totzeit**: Die IR2110 erzeugt diese nicht selbst. Die diskrete-Komponenten-Option — RC+1N4148 an den 74HC14-Eingängen (verzögert nur steigende Flanken, ~1 µs; mit einer Periode von 25 µs bei 40 kHz ist das <5% Verlust). Die einfache Option — ein EGS002-Modul, alles ist bereits integriert.
- **3,3 V Logik**: Versorgen Sie die IR2110-VDD mit dem gleichen 3,3 V wie die AD9833 und 74HC14 — bei VDD=5 V liegt der VIH-Schwellenwert bei ≈ 3,1 V und eine 3,3 V-Rechteckwelle kommt gerade noch durch (das Datenblatt erlaubt VDD bis hinunter zu 3,3 V).
- **Entkopplung ist obligatorisch**: 100 nF bei VDD und VCC (VCC — plus 47 µF) und an der Stromversorgungsleitung 470–1000 µF + 100 nF Keramik direkt an den Halbbrückenbeinen — ohne diese nimmt eine Halbbrücke auf einem Prototypen-Breadboard ihre eigenen Schaltspitzen auf.
- Erster Einschaltvorgang: Kein Platten, Langevin-Wandler in der Luft, minimale Leistung, überprüfen Sie die Wellenform auf einem Oszilloskop/ADC.

TODO: KiCad-Projekt (PCB) sobald der Prototyp auf einem Breadboard überprüft wurde.
