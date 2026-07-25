# Empfänger-Entdeckungs- und Autoabstimmungsprotokoll (Skizze; Implementierung in den Stufen 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · Deutsch

Das Ziel: Das Gerät stellt selbstständig fest, ob sich ein Empfänger hinter der Wand befindet, wählt die Frequenz und Leistung selbst aus und verbraucht nicht unnötig Energie, wenn jemand "vergessen hat, den Empfänger einzuschweißen".

Das Vorbild sind Qi-Ladegeräte: Sie lösen genau dieses Problem (ist ein Telefon auf der Spule?) mit genau dieser Sequenz. Unser akustisches Analogon:

## Phase 0 — analoger Ping (der Empfänger kann vollständig entladen sein)
Der TX führt einen Niedrigleistungs-Sweep über das Band aus und misst **seinen eigenen Strom und die Phase** (Shunt + Peak-Detektor → ADS1115). Ein resonanter Empfänger hinter der Wand ist eine Last, die über die Wand mit dem TX verbunden ist: Seine Anwesenheit zeigt sich als charakteristische Dip-/Buckel-Kurve auf der TX-Impedanzkurve, auch wenn alles innerhalb unbetrieben ist. Gleicher Grundsatz wie ein Metall-Detektor und Qi's analoger Ping.
- Signatur vorhanden → Phase 1. Keine Signatur → "kein Empfänger gefunden", bleibe im Standby-Ping (alle N Sekunden), erhöhe die Leistung nicht.
- Bonus: Die Impedanzkurve der "leeren" Wand wird bei der Installation als Referenz aufgezeichnet — damit können wir "keinen Empfänger" von "Empfänger ist lose geworden / wurde fehljustiert" unterscheiden.

## Phase 1 — digitales Handschlag-Protokoll
Der TX parkt auf der Kandidatenfrequenz (dem Phase-0-Peak) und liefert Leistung. Der RX-Harvester lädt den Supercapacitor, der MCU wake-up und antwortet mit **Lastmodulation**: Ein MOSFET kurzschließt periodisch sein Piezo nach einem Code (ID + Protokollversion). Der TX sieht dies als Modulation seines eigenen Stroms. Kein Transmitter ist innerhalb erforderlich — dies ist ein RFID-Schema, das gleiche wie in der aufgegebenen DOE/RPI-Anwendung US20100027379 (freie Vorart).

## Phase 2 — Frequenz-Servo-Abstimmung (Stören und Beobachten)
Der RX kann seine Bus-Spannung melden (Telemetrie über Lastmodulation). Der TX schaltet ±Δf und hält die maximale empfangene Leistung — eine klassische MPPT-Schleife. Dies schließt die Resonanz-Drift mit der Temperatur (die Hauptschwierigkeit des Nischenprodukts: eine ~6%-Verschiebung = ~10× Effizienzabfall).

## Phase 3 — Leistungsverhandlung und Wachhund
Der RX fordert ein Level an (lebendig / ladend / gib mir mehr), der TX begrenzt die Leistung auf das, was angefordert wurde. Fehlende Antworten für M-Zyklen → der TX fällt zurück in Phase 0 bei niedriger Leistung.

## Hardware, die dafür erforderlich ist (BOM-Position 12, Schaltplan — hardware/schematics/sch4)
- TX: 0,1 Ω Shunt + Gleichrichter/Peakschwellen-Detektor auf dem zweiten ADS1115-Kanal (Strom), optional ein Phasenvergleicher.
- RX: 2N7002 + ~100 Ω auf der **DC-Seite** des Gleichrichters (der VIN-Pin des LTC3588-Moduls) + GPIO — die Last wird nach der Brücke geschaltet, und der TX sieht sie als Modulation seines eigenen Stroms. Ein einzelner MOSFET über dem AC-Piezo funktioniert nicht (der Body-Diode kurzschließt eine Halbwelle, das Gate hat keinen Bezugspunkt auf einem schwimmenden Knoten); die über-dem-Piezo-Variante funktioniert nur mit einem Paar von in Reihe geschalteten MOSFETs.

## Grenzen
Der analoge Ping schwächt sich ab, wenn die Wanddicke und die Kontaktverluste zunehmen (die Signatur ertrinkt im Rauschen) — der Erkennungsschwellenwert muss in einem speziellen Experiment gemessen werden (experiments/). Für dicke Wände ist der Fallback: Der RX, sobald er Ladung gespeichert hat, "klopft" periodisch mit einem eigenen Beacon.
