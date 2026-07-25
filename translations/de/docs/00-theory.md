# Kanaltheorie (das Minimum, das Sie wissen müssen)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · Deutsch

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
- **A (40 kHz, Langevin-Transduktoren).** Eine 3-5 mm dicke Platte ≪ λ — sie verhält sich wie eine Membran; die Resonanz wird durch das Transduktoren-Paar und nicht durch die Wand bestimmt. Der NASA-JPL-Betrieb (~24,5 kHz, Hunderte von Watt bis zu einem kW durch 5 mm Ti). Einfacher, leistungsstärker, der zuerst zu verwenden ist.
- **B (0,6-1 MHz, Scheiben).** Dickenresonanz der Wand selbst und eine scharfe Resonanz (eine ~6%ige Frequenzverschiebung ⇒ Effizienzabfall ~10×). Der RPI/Moss-Betrieb: Hunderte von mW plus Daten bei Hunderten von kbit/s. Benötigt automatische Frequenzverfolgung.

## Hauptverluste
Resonanzmismatch innerhalb des Transduktoren-Paares (billige Langevin-Transduktoren haben eine Streuung von ±1 kHz), Qualität des akustischen Kontakts (Epoxy > dicke Schmiermittel-Koppel + Klemme > trockener Druck), Fehlausrichtung, Resonanzdrift mit der Temperatur. Die Antwort auf all dies ist dieselbe: vor jeder Änderung der Einrichtung eine Sweep-Karte ausführen.

## Empfänger-Leistungsbudget (grobe Schätzung)
LED 20 mW; ESP32 mit Zykluszeit 1-5 mW Durchschnitt; BLE-Paket ~150 mW Spitze — Puffer: ein 1 F-Ionistoren @ 3,3 V = 5,4 J ≈ 360 Übertragungen.
