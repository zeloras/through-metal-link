# Empfänger-Discovery- und Auto-Tuning-Protokoll (Skizze; Implementierung in den Phasen 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · Deutsch · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

Das Ziel: Das Gerät stellt selbst fest, ob sich ein Empfänger hinter der Wand befindet, wählt Frequenz und Leistung selbst aus und röstet die Wand nicht umsonst, falls jemand „vergessen hat, den Empfänger einzuschweißen".

Das Vorbild sind Qi-Ladegeräte: Sie lösen genau dieses Problem (liegt ein Handy auf der Spule?) mit genau dieser Sequenz. Unser akustisches Analogon:

## Phase 0 — analoger Ping (der Empfänger kann vollständig entladen sein)
Der TX führt einen Low-Power-Sweep über das Band aus und misst **seinen eigenen Strom und seine Phase** (Shunt + Spitzenwertdetektor → ADS1115). Ein resonanter Empfänger hinter der Wand ist eine Last, die über die Wand an den TX gekoppelt ist: Seine Anwesenheit zeigt sich als charakteristische Einbuchtung/Beule auf der TX-Impedanzkurve, selbst wenn alles im Inneren stromlos ist. Dasselbe Prinzip wie bei einem Metalldetektor und dem analogen Ping von Qi.
- Signatur vorhanden → Phase 1. Keine Signatur → „kein Empfänger gefunden", im Standby-Ping bleiben (alle N Sekunden), die Leistung nicht erhöhen.
- Bonus: Die Impedanzkurve der „leeren" Wand wird bei der Installation als Referenz aufgezeichnet — so können wir „kein Empfänger" von „Empfänger hat sich gelöst / wurde dejustiert" unterscheiden.

## Phase 1 — digitaler Handshake
Der TX parkt auf der Kandidatfrequenz (dem Phase-0-Peak) und liefert Leistung. Der RX-Harvester lädt den Superkondensator auf, der MCU erwacht und antwortet mit **Lastmodulation**: Ein MOSFET schließt periodisch seinen Piezo nach einem Code (ID + Protokollversion). Der TX sieht dies als Modulation seines eigenen Stroms. Im Inneren wird überhaupt kein Sender benötigt — dies ist ein RFID-Schema, dasselbe wie in der aufgegebenen DOE/RPI-Anmeldung US20100027379 (freier Stand der Technik).

## Phase 2 — Frequenz-Servo-Tuning (Perturb & Observe)
Der RX kann seine Bus-Spannung melden (Telemetrie über Lastmodulation). Der TX variiert ±Δf und hält das Maximum der empfangenen Leistung — eine klassische MPPT-Regelschleife. Dies kompensiert die Resonanzdrift mit der Temperatur (der Hauptfallstrick der Nische: eine Verschiebung von ~6 % = ~10× Wirkungsgradverlust).

## Phase 3 — Leistungsverhandlung und Watchdog
Der RX fordert einen Pegel an (aktiv / lädt / gib mir mehr), der TX begrenzt die Leistung auf das angeforderte Maß. Antworten für M Zyklen ausbleiben → der TX fällt auf Phase 0 bei niedriger Leistung zurück.

## Hierfür erforderliche Hardware (BOM-Position 12, Schaltplan — hardware/schematics/sch4)
- TX: 0,1 Ω Shunt + Gleichrichter/Spitzenwertdetektor auf dem zweiten ADS1115-Kanal (Strom), optional ein Phasenkomparator.
- RX: 2N7002 + ~100 Ω auf der **DC-Seite** des Gleichrichters (der VIN-Pin des LTC3588-Moduls) + GPIO — die Last wird nach der Brücke geschaltet, und der TX sieht dies als Modulation seines eigenen Stroms. Ein einzelner MOSFET über dem AC-Piezo funktioniert nicht (die Body-Diode leitet eine Halbwelle ab, das Gate hat keinen Bezugspunkt an einem schwebenden Knoten); die Variante über dem Piezo funktioniert nur mit einem Paar rückwärts in Reihe geschalteter MOSFETs.

## Grenzen
Der analoge Ping schwächt sich mit zunehmender Wanddicke und Kontaktverlusten ab (die Signatur geht im Rauschen unter) — die Erkennungsschwelle muss in einem dedizierten Experiment gemessen werden (experiments/). Für dicke Wände gilt der Fallback: Der RX, sobald er genug Ladung angesammelt hat, „klopft" periodisch mit einem eigenen Beacon.
