# Kanaltheorie (das Minimum, das Sie wissen müssen)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · Deutsch · [Português](../../pt/docs/00-theory.md) · [Español](../../es/docs/00-theory.md) · [Français](../../fr/docs/00-theory.md) · [Italiano](../../it/docs/00-theory.md) · [Polski](../../pl/docs/00-theory.md) · [Türkçe](../../tr/docs/00-theory.md) · [Українська](../../uk/docs/00-theory.md) · [Tiếng Việt](../../vi/docs/00-theory.md) · [中文](../../zh/docs/00-theory.md) · [日本語](../../ja/docs/00-theory.md) · [한국어](../../ko/docs/00-theory.md) · [हिन्दी](../../hi/docs/00-theory.md)

## Prinzip
Ein TX-Piezoelement, das gegen die Wand gepresst oder aufgeklebt ist, erregt eine longitudinale Welle in ihr; ein Piezo-Empfänger auf der anderen Seite wandelt sie zurück in Elektrizität. Die Wand ist ein Resonator: bei Dickenresonanzen (Vielfache einer Halbwellenlänge) ist die Übertragung am größten.

## Schlüsselzahlen
Longitudinale Schallgeschwindigkeit in Stahl: ~5900 m/s.

| Stahldicke | Halbwellenresonanz |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Wellenlänge in Stahl: 148 mm @ 40 kHz; 5,9 mm @ 1 MHz.

## Zwei Modi
- **A (40 kHz, Langevin-Transduktoren).** Eine 3-5 mm dicke Platte ≪ λ — sie verhält sich wie eine Membran; die Resonanz wird durch das Transduktoren-Paar und nicht durch die Wand bestimmt. Einfacher und leistungsstärker als Modus B — der zuerst zu verwenden ist. Labornachweis (nicht für die Garage vorgesehen): NASA JPL ~24,5 kHz, Hunderte von Watt bis zu einem kW durch 5 mm Ti mit speziell entwickelter Hardware.
- **B (0,6-1 MHz, Scheiben).** Dickenresonanz der Wand selbst und eine scharfe Resonanz (eine ~6%ige Frequenzverschiebung ⇒ Übertragung fällt ~10× im Fabry-Perot-Modell). Die RPI/Moss-Klasse von Ergebnissen: Hunderte von mW plus Daten bei Hunderten von kbit/s unter Labor-Bonding und -Abstimmung. Benötigt automatische Frequenzverfolgung.

## Hauptverluste
Resonanzmismatch innerhalb des Transduktoren-Paares (billige Langevin-Transduktoren haben eine Streuung von ±1 kHz), Qualität des akustischen Kontakts (Epoxy > dicke Schmiermittel-Koppel + Klemme > trockener Druck), Fehlausrichtung, Resonanzdrift mit der Temperatur. Die Antwort auf all dies ist dieselbe: vor jeder Änderung der Einrichtung eine Sweep-Karte ausführen.

## Einfluss auf die Wand und die Medien dahinter

Kurzversion: bei Plattformleistungen bleibt die Wand und jedes Gas dahinter unberührt. Ein Fluid dahinter beeinflusst hauptsächlich den *Kanal*; der Kanal beginnt erst, das *Fluid* zu beeinflussen, in der Nähe der Kavitationsgrenze. Die folgenden Schätzungen gelten für Modus A: 40 kHz, ~1 W/cm² in 3 mm Stahl.

**Wand — keine Deformation, keine Ermüdung, nie.** Teilchengeschwindigkeit v = √(2I/ρc) ≈ 21 mm/s ⇒ Verschiebung ≈ 80 nm, ebene Wellen-Dehnung ε = v/c ≈ 3,5·10⁻⁶. Zwei äquivalente Spannungs-Schätzungen: elastisch E·ε ≈ 0,7 MPa (E ≈ 200 GPa) und akustisch p = Z·v ≈ 1,0 MPa (Z_Stahl ≈ 4,6·10⁷ Pa·s/m). Stahl hat eine Streckgrenze von 250+ MPa und eine Ermüdungsgrenze von ~200 MPa — ein >200-facher Spielraum, und unter der Ermüdungsgrenze kann Stahl unbegrenzte Zyklen aushalten. Die mechanisch fragilen Teile sind woanders: das Piezokeramik (spröde, depolt, wenn es überhitzt wird) und die Bondlinie (Epoxy heizt sich auf und ermüdet zuerst) — siehe [02-Sicherheit](02-safety.md).

**Gas hinter der Wand — keine Auswirkung.** Die Stahl-Luft-Impedanzmismatch (~4,6·10⁷ vs ~400 Pa·s/m) überträgt einen Bruchteil der Größenordnung 10⁻⁵ der Leistung. Keine messbare Erwärmung oder Bewegung; Elektronik in einer abgedichteten Box bemerkt keine nm-Skalen-Wandbewegung.

**Fluid hinter der Wand — zwei Richtungen:**

- *Fluid → Kanal (immer).* Wasser belastet die ferne Seite mit ~1,5 MRayl anstelle von Luft: ein Teil der Leistung strahlt in das Fluid aus, Q sinkt, der Sweep-Peak verschiebt und verbreitert sich. Modus B ist am stärksten betroffen — die Dickenresonanz-Kamm ist für Stahl-Luft-Grenzen berechnet und bewegt sich mit Fluidbelastung. Die stehende Regel deckt dies ab: **erneut Sweep gegen das reale, volle Gefäß**, nie vertrauen Sie einem Sweep, der gegen ein leeres Gefäß aufgenommen wurde. Nebeneffekt: Fluiddämpfung verkürzt das Resonator-Verklingen (τ), so dass das OOK-Auge bei höheren Bitraten geöffnet wird. Blasen im Pfad (gärendes Fluid!) streuen stark — siehe die Lösung in [04-Hybridkanälen](04-hybrid-channels.md).
- *Kanal → Fluid (nur bei hoher Leistung).* Maximaler Druck, der in Wasser ausgestrahlt wird: p ≈ ρc·v ≈ 1,5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0,3 atm. Die inertielle Kavitationsgrenze bei 40 kHz in normalem (gasreichem) Wasser liegt bei ~1-2 atm, so dass bei 1 W/cm² der Spielraum 3-10× beträgt. Aber p wächst wie √Leistung, und stehende Wellen in einem geschlossenen Gefäß erzeugen lokale Hotspots — Zehner von W/cm² kontinuierlich in ein flüssigkeitsgefülltes Gefäß können die Grenze erreichen. Das Überschreiten bedeutet CO₂-Entgasung, Sonochemie (unangenehme Aromen in Lebensmittelprodukten) und langfristige Kavitationserosion der Innenoberfläche (genau so reinigen Ultraschallreiniger). Praktische Obergrenze für kontinuierliche Leistung in flüssigkeitsgefüllte Wände: **≲1 W/cm²**. Modus B ist ausgenommen: bei MHz liegt die Grenze eine Größenordnung höher und die Leistungen betragen Hunderte von mW.

## Empfänger-Leistungsbudget (grobe Schätzung)
LED 20 mW; ESP32 mit Zykluszeit 1-5 mW Durchschnitt; BLE-Radio ~150 mW, solange das Radio eingeschaltet ist. Puffer: ein 1 F-Supercapacitor @ 3,3 V speichert E = ½CV² = 5,4 J. Wie viele Übertragungen das ermöglicht, hängt von der Sendezeit ab: ein kurzes BLE-Werbeereignis (~2-5 ms bei ~150 mW) ist nur ~0,3-0,8 mJ → in der Größenordnung von **10⁴ Paketen** von einem vollen Kondensator; eine lange Verbindung / Übertragung (~100 ms Radio-Ein) ist ~15 mJ → in der Größenordnung von **10² Übertragungen**. Der Durchschnittsverbrauch muss immer noch innerhalb der gesammelten Watt bleiben (Ziel für Stufe 2 ≥0,5 W in die Last ist das Tor; bis dahin sind die multi-Watt-Modus-A-Bänder auf den Simulator-Plots Ziele, keine Daten).
