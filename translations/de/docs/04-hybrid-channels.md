# Hybridkanäle: Barrier → Physik → Zahlen

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · Deutsch

Das Prinzip (eine Folge des "Penetrationsparadoxons"): Eine Welle durchdringt eine Barriere genau in dem Maße, in dem sie schwach mit ihr interagiert — daher existiert kein universeller Kanal. Die Plattform verfolgt keinen einzelnen Kanal; für jede Barriere wählt sie die Physik, die die Barriere durchlässig ist, und der Empfänger ist resonant "gierig" danach.

## Kanal-Auswahl-Tabelle

| Barriere | Funktionskanal | Erwartet (Größenordnungen) | Notizen |
|---|---|---|---|
| Stahl/Aluminum 1–60 mm, Kontakt möglich | Piezo-Akustik (unser primärer) | Watt; kbit/s (bis Mbit/s im MHz-Modus) | benötigt akustischen Kontakt (Schmiermittel/Kupplungsepoxyd) |
| Metall: schmutzig, lackiert, heiß, Kontakt unerwünscht | EMAT (Magnetismus → Schall in der Wand) | mW; kbit/s; Spalt bis zu ~3 mm | leitende Wände nur; Daten, nicht Leistung |
| Ferromagnetische Wand ohne Piezo | Magnetostriction (eine Spule treibt den Stahl selbst an) | Krümel; bit/s–kbit/s | experimenteller Zweig, billig zu testen |
| Doppelwand mit Vakuum (Thermos, Kryostat, Dewar) | LF-Magnetismus (Zehner–Hunderter Hz) | µW–mW; bit/s | Hauteffekt: in Stahl δ≈0.6 mm @1 kHz — Frequenz nach unten drücken |
| Nicht-Metall: Glas, Kunststoff, Keramik | Piezo-Akustik (einfacher als Metall) | Watt; kbit/s | + einfacher RF kommt oft auch durch — prüfen Sie das zuerst |
| Wand mit einer Gummischicht, Composite | Ehrlich: fast ein totes Ende | — | der Absorber frisst alles; die Umgehung ist ein Punkt ohne Beschichtung |
| Blasenbildende Flüssigkeit im akustischen Pfad | Architektonische Umgehung | — | Empfänger an der Wand montieren, Flüssigkeit aus dem Pfad halten |

## Hybridknoten-Architektur

- Leistungsschicht: Piezo-Paar bei Resonanz (Stufen 1–4).
- Berührungslose Datenschicht: ein EMAT-Kopf als abnehmbare "Scanner-Pistole" (Stufe ~6).
- Fallback-Schicht: LF-Spulen für Vakuum-Sandwiches (wenn die Aufgabe es erfordert).
- Das Entdeckungsprotokoll (docs/03) erweitert sich von "Sweep über Frequenz" zu "Sweep über Physik": ping Piezo → ping EMAT → ping LF; der Knoten wählt den Kanal, der von selbst durchkommt, und meldet, welche Barriere er sieht.

## Beispielanwendungen nach Kanal

1. **Geschlossene Batteriepacks (EV/Speicher):** T/Gas-Sensor innerhalb einer verklebten Verkleidung; Leistung+Daten via Piezo-Paar durch 2–3 mm Aluminium. Der Markt boomt, und eine Penetration in eine Batterieverkleidung = Zertifizierungshölle.
2. **Kryostat/Dewar:** ein Temperaturregler innerhalb, der ein Bit-Paket einmal pro Minute via LF-Magnetismus durch die Vakuumjacke sendet. Grundlegend außer Reichweite für Akustik — hier ist das Hybrid-System unersetzlich.
3. **Rohr/Druckbehälter unter Druck:** ein EMAT-Scanner, der gegen eine heiße lackierte Rohrleitung mit null Oberflächenpräparierung gepresst wird — liest ein passives resonantes Signal von innen.
4. **Gärbehälter (Bier/Wein, Edelstahl):** ein Dichte/T-Sensor innerhalb des Behälters ohne eine einzige Penetration — sanitäre Vorschriften lieben das Fehlen von Löchern.
5. **Seehafen-Container/Safe:** "ist die Ladung am Leben" — ein Piezo-Paar durch gewellten Stahl, abgefragt mit einem Handscanner.

## Einschränkungen, die keine Schicht lösen kann
Leistung — Kontakt-Piezo nur (EMAT und LF-Magnetismus sind Größenordnungen schwächer). Composite/Gummischicht-Wände sind außerhalb der Plattform. LF-Kanalgeschwindigkeit ist Bits pro Sekunde — das ist Telemetrie, nicht Streaming.
