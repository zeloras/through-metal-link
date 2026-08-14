# Empfänger

> [English (primary)](../../../../hardware/receiver/README.md) · [Русский](../../../ru/hardware/receiver/README.md) · Deutsch · [Português](../../../pt/hardware/receiver/README.md) · [Español](../../../es/hardware/receiver/README.md) · [Français](../../../fr/hardware/receiver/README.md) · [Italiano](../../../it/hardware/receiver/README.md) · [Polski](../../../pl/hardware/receiver/README.md) · [Türkçe](../../../tr/hardware/receiver/README.md) · [Українська](../../../uk/hardware/receiver/README.md) · [Tiếng Việt](../../../vi/hardware/receiver/README.md) · [中文](../../../zh/hardware/receiver/README.md) · [日本語](../../../ja/hardware/receiver/README.md) · [한국어](../../../ko/hardware/receiver/README.md) · [हिन्दी](../../../hi/hardware/receiver/README.md)

Schaltpläne: [Stufe 1 — sch2](../schematics/sch2-receiver-stage1.png) · [Stufe 4 — sch4](../schematics/sch4-receiver-node.png) (erzeugt von [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

- Stufe 1 (Messungen): Langevin-Wandler RX (beide Anschlüsse floating — nicht erden!) → Schottky-Brücke (4×SS14) → RC-Filter (10k || 100n) → 5 V TVS → **47 kΩ in Reihe** → ADS1115 A0 (der Widerstand begrenzt den Strom in die Schutzdioden des ADC: die TVS klemmt bei ~9 V über dem abs. Max. des Eingangs).
- Stufe 2 (Watt): RX → dieselbe Brücke → bekannte ohmsche Last (und/oder LED), DC-Spannung und -Strom nach der Brücke messen; Leistung ist V·I in diese Last. Protokoll: [experiments/002](../../experiments/002-watts-3mm-steel/README.md).
- Stufe 4 (Knoten): RX → GY-LTC3588 **direkt auf PZ1/PZ2** (die Brücke ist im LTC3588-1 integriert, keine externe erforderlich) → 1 F Superkondensator → ESP32 (Deep Sleep + Duty Cycle). Lastmodulation — 2N7002 + 100 Ω auf der **DC-Seite** (der VIN-Pin des Moduls, siehe sch4); ein einzelner MOSFET über das AC-Piezo funktioniert nicht — die Body-Diode leitet eine Halbwelle kurz (docs/03).

WICHTIG: Die TVS vor dem allerersten Einschalten einbauen — ein offener Piezo erzeugt bei Resonanz Dutzende bis Hunderte Volt. Auf der DC-Seite nach der Brücke — eine unidirektionale SMBJ5.0A; über dem Piezo des Knotens (AC) — nur eine bidirektionale SMBJ15CA.
