# Empfänger

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · Deutsch · [Português](../../../pt/hardware/receiver/README.md)

Schemazeichnungen: [Stufe 1 — sch2](../schematics/sch2-receiver-stage1.png) · [Stufe 4 — sch4](../schematics/sch4-receiver-node.png) (generiert durch [../../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

- Stufe 1 (Messungen): Langevin-Transducer RX (beide Leiter schwimmen — nicht auf Masse legen!) → Schottky-Brücke (4×SS14) → RC-Filter (10k || 100n) → 5 V TVS → **47 kΩ in Reihe** → ADS1115 A0 (der Widerstand begrenzt den Strom in die Schutzdioden des ADC: die TVS begrenzt ~9 V über dem absoluten Maximalwert des Eingangs).
- Stufe 2 (Watt): RX → dieselbe Brücke → elektronische/widerständige Last, messen von V und I.
- Stufe 4 (Knoten): RX → GY-LTC3588 **direkt in PZ1/PZ2** (die Brücke ist im LTC3588-1 integriert, keine externe Brücke erforderlich) → 1 F Supercap → ESP32 (Tiefschlaf + Duty Cycle). Lastmodulation — 2N7002 + 100 Ω auf der **Gleichstromseite** (die VIN-Buchse des Moduls, siehe sch4); ein einzelner MOSFET über dem AC-Piezo funktioniert nicht — die Body-Diode schaltet eine Halbwelle kurz (docs/03).

WICHTIG: Die TVS vor dem ersten Einschalten installieren — ein offener Piezo bei Resonanz liefert Tens bis Hunderte von Volt. Auf der Gleichstromseite nach der Brücke — ein unidirektionales SMBJ5.0A; über dem Piezo des Knotens (AC) — nur ein bidirektionales SMBJ15CA.
