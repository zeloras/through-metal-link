# Hybridkanäle: Barriere → Physik → Zahlen

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · Deutsch · [Português](../../pt/docs/04-hybrid-channels.md) · [Español](../../es/docs/04-hybrid-channels.md) · [Français](../../fr/docs/04-hybrid-channels.md) · [Italiano](../../it/docs/04-hybrid-channels.md) · [Polski](../../pl/docs/04-hybrid-channels.md) · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

Das Prinzip (eine Folgerung aus dem „Penetrationsparadoxon"): Eine Welle dringt durch eine Barriere genau in dem Maße, in dem sie schwach mit ihr wechselwirkt — deshalb gibt es keinen universellen Kanal. Die Plattform jagt nicht einem einzigen Kanal hinterher; für jede Barriere wählt sie die Physik, für die die Barriere transparent ist und der Empfänger resonant „gierig" ist.

## Kanalauswahl-Tabelle

| Barriere | Arbeitskanal | Erwartet (Größenordnungen) | Hinweise |
|---|---|---|---|
| Stahl/Aluminium 1–60 mm, Kontakt möglich | Piezo-Akustik (unser Primärkanal) | Watt; kbit/s (bis Mbit/s im MHz-Modus) | akustischer Kontakt nötig (Kopplungsgel/Epoxy) |
| Metall: schmutzig, lackiert, heiß, Kontakt unerwünscht | EMAT (Magnetik → Schall in der Wand) | mW; kbit/s; Spalt bis ~3 mm | nur leitfähige Wände; Daten, keine Leistung |
| Ferromagnetische Wand ganz ohne Piezo | Magnetostriktion (eine Spule treibt den Stahl selbst an) | Krümel; bit/s–kbit/s | experimenteller Zweig, günstig zu testen |
| Doppelwand mit Vakuum (Thermos, Kryostat, Dewar) | LF-Magnetik (Zehner–Hunderter Hz) | µW–mW; bit/s | Skin-Effekt: in Stahl δ≈0,6 mm @1 kHz — Frequenz runterdrücken |
| Nichtmetall: Glas, Kunststoff, Keramik | Piezo-Akustik (einfacher als Metall) | Watt; kbit/s | + einfaches RF kommt oft auch durch — zuerst das prüfen; pro Material Zahlen und Bewertungen: [06-Materialien](../../../docs/06-materials.md) |
| Wand mit Gummi-/Schaumstoffschicht, Verbund | Ehrlich: fast eine Sackgasse | — | der Absorber schluckt alles; Workaround ist eine Stelle ohne Beschichtung |
| Flüssigkeit hinter der Wand (voller Tank) | Piezo-Akustik, degradiert | Leistung − wenige dB; kürzeres Nachschwingen | Flüssigkeitsbelastung verschiebt/dämpft die Resonanz — neu sweepen gegen das volle Gefäß; kontinuierliche Intensität ≲1 W/cm² einhalten, um unter der Kavitationsschwelle zu bleiben ([Theorie](00-theory.md#einfluss-auf-die-wand-und-die-medien-dahinter)) |
| Blasenbildung in der Flüssigkeit im akustischen Pfad | Architektonischer Workaround | — | Empfänger an der Wand montieren, Flüssigkeit aus dem Pfad heraushalten |

## Hybridknoten-Architektur

- Leistungsebene: Piezopaar bei Resonanz (Stufen 1–4).
- Kontaktfreie Datenebene: ein EMAT-Kopf als abnehmbare „Scanner-Pistole" (Stufe ~6).
- Fallback-Ebene: LF-Spulen für Vakuum-Sandwiches (wenn die Aufgabe es verlangt).
- Das Discovery-Protokoll (docs/03) wird von „Sweep über Frequenz" zu „Sweep über Physik" erweitert: Piezo pingen → EMAT pingen → LF pingen; der Knoten wählt selbst den Kanal, der durchkommt, und meldet, welche Barriere er sieht.

## Beispielanwendungen nach Kanal

1. **Versiegelte Batteriepacks (EV/Speicher):** T/Gas-Sensor in einem vergossenen Gehäuse; Leistung+Daten über ein Piezopaar durch 2–3 mm Aluminium. Der Markt boomt, und eine Penetration in ein Batteriegehäuse = Zertifizierungshölle.
2. **Kryostat/Dewar:** ein Temperatur-Logger innen, der einmal pro Minute ein Bit-Paket über LF-Magnetik durch die Vakuum-Mantelung schickt. Für Akustik grundsätzlich unerreichbar — hier ist das Hybrid-System unersetzlich.
3. **Pipeline/Autoklav unter Druck:** ein EMAT-Scanner, gegen ein heißes lackiertes Rohr gedrückt ohne jegliche Oberflächenvorbereitung — liest ein passives Resonanz-Beacon von innen.
4. **Gärtanks (Bier/Wein, Edelstahl):** ein Dichte/T-Sensor im Tankinneren ohne eine einzige Penetration — Hygienevorschriften lieben das Fehlen von Löchern.
5. **Seecontainer/Tresor:** „Ist die Ladung am Leben" — ein Piezopaar durch Wellblech-Stahl, abgefragt mit einem Handscanner.

## Grenzen, die keine Ebene lösen kann
Leistung — nur Kontakt-Piezo (EMAT und LF-Magnetik sind um Größenordnungen schwächer). Verbund-/Gummiausgekleidete Wände liegen außerhalb der Plattform. Die LF-Kanalgeschwindigkeit beträgt Bits pro Sekunde — das ist Telemetrie, kein Streaming.
