# Treiber (Stufe 2): IR2110 Halbbrücke

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · Deutsch · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Schaltplan:** [../schematics/sch1-driver-halfbridge.png](../schematics/sch1-driver-halfbridge.png) (erzeugt von [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

Die Kette: Pi (SPI) → AD9833 **im Rechteckmodus** (OPBITEN-Bit: MSB auf den Ausgang geroutet, Rail-to-Rail-Swing — kein separater Komparator nötig) → **74HC14 + RC + 1N4148** Formgeber (komplementäre HIN/LIN mit ~1 µs Totzeit) → IR2110 → 2×IRF540 (Halbbrücke) → 1 µF DC-Blockkondensator → Anpassungstrafo (Ferrit, ~1:3..1:5, auf dem Prüfstand abstimmen) → Langevin-Wandler TX.

Der Sinusausgang des AD9833 (~0,6 Vpp) ist für die IR2110-Logik ungeeignet — wenn Sie aus irgendeinem Grund ausdrücklich einen Sinus aus dem DDS brauchen, setzen Sie einen Komparator dazwischen (z. B. einen LM393, nicht in der Stückliste).

Stromversorgung der Endstufe: 12–24 V Labornetzteil mit Strombegrenzung (**bei 0,2 A starten**).

Hinweis: Der Stufe-1-Sweep treibt den Piezo direkt mit dem schwachen DDS-Sinus an (~0,6 Vpp, siehe `sweep_map.py`) — **dieser Treiber tritt erst in Stufe 2 (Watt) in die Kette ein**. Erwarten Sie keine ≥0,5 W aus der reinen Stufe-1-DDS-Verdrahtung.

Hinweise:
- Der Langevin-Wandler ist eine kapazitive Last (typisch einige nF). Eine Seriendrossel oder ein Anpassungstrafo ist zwingend erforderlich; ohne sie dissipieren die MOSFETs den Blindstrom und überhitzen.
- **Anpassungstrafo (der typische Fehlerpunkt).** Starten Sie mit einem kleinen Ferrit-Ringkern (z. B. FT50-43 / ähnlich), Primärseite einige Windungen, Sekundärseite ~3–5× so viele, plus 1 µF DC-Block-Folienkondensator in Serie auf der Primärseite. Abstimmen auf minimalen Netzteilstrom *bei der Stufe-1-Resonanz* mit dem TX **auf die Platte geklemmt** und der RX belastet. Windungsverhältnis und Streuung sind empirisch — der Schaltplan markiert sie `*` aus gutem Grund. Endgültige Windungszahl im Versuchsprotokoll notieren.
- **Totzeit**: Der IR2110 erzeugt sie nicht selbst. Die Option mit diskreten Bauteilen — RC+1N4148 an den 74HC14-Eingängen (verzögert nur steigende Flanken, ~1 µs; bei 25 µs Periode bei 40 kHz sind das <5% Verlust). Die einfache Option — ein EGS002-Modul, dort ist alles eingebaut.
- **3,3 V-Logik**: Speisen Sie VDD des IR2110 aus derselben 3,3 V wie AD9833 und 74HC14 — bei VDD=5 V liegt die VIH-Schwelle bei ≈ 3,1 V und ein 3,3 V-Rechtecksignal schafft es gerade so durch (das Datenblatt erlaubt VDD bis 3,3 V).
- **Entkopplung ist Pflicht**: 100 nF an VDD und VCC (VCC — plus 47 µF), und auf der Stromschiene 470–1000 µF + 100 nF Keramik direkt an den Halbbrücken-Beinen — ohne das nimmt eine Halbbrücke auf Steckbrett-Jumperdrähten ihre eigenen Schaltspikes auf. Stromschleifen-Kurz halten; wenn der Schaltknoten stark schwingt, vom Steckbrett auf Kupferkaschierte Dead-Bug-/Protoboard-Ground-Pour umsteigen, bevor der Strom erhöht wird.
- **Erstmaliges Inbetriebnehmen** (abgestimmt mit [docs/02-safety.md](../../docs/02-safety.md)):
  1. Noch kein Langevin auf der Sekundärseite. Netzteil = 12 V, Strombegrenzung 0,2 A. Gate-Ansteuerung (HIN/LIN) und Schaltknoten mit dem Oszilloskop prüfen — Totzeit und kein Shoot-Through bestätigen.
  2. Anpassungstrafo + TX-Langevin **auf die Stahlplatte geklemmt** einbauen (oder einen dicken Opfer-Metallblock). Weiterhin 0,2 A-Begrenzung. Nur bei der Stufe-1-Spitzenfrequenz hochfahren, gerade lange genug, um Strom und RX-Spannung zu sehen.
  3. Strombegrenzung schrittweise erhöhen, dabei MOSFET- und Trafo-Temperatur beobachten. Niemals einen ungeklemmten Langevin unter Leistung lassen — Freiluft-Vollastbetrieb ist der Weg, wie Keramik reißt und Treiber sterben.

TODO: KiCad-Projekt (PCB), sobald das Steckbrett- (oder Dead-Bug-) Prototyp funktioniert. Bis dahin sind die Schaltpläne in [`../schematics/`](../schematics/) die design-maßgebliche Quelle.
