# Anwendungsübersicht: Wer braucht diesen Technologie-Stack, und warum

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · Deutsch · [Português](../../pt/docs/05-applications-map.md) · [Español](../../es/docs/05-applications-map.md) · [Français](../../fr/docs/05-applications-map.md) · [Italiano](../../it/docs/05-applications-map.md) · [Polski](../../pl/docs/05-applications-map.md) · [Türkçe](../../tr/docs/05-applications-map.md) · [Українська](../../uk/docs/05-applications-map.md) · [Tiếng Việt](../../vi/docs/05-applications-map.md) · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

Der Plattform-Stack: ein aktiver Energie- und Datenkanal durch blinde Wände — Piezoakustik / EMAT / LF-Magnetik. Im Folgenden: wo das in der realen Welt gebraucht wird, wer schon dort ist, und was für uns übrig bleibt.

## 1. Versiegelte Batteriepacks (EV, Heim-/Industrie-Energiespeicher)
- Schmerzpunkt: Früherkennung von Thermal Runaway — Gase (CO₂, H₂, Elektrolytdämpfe) entstehen im Pack Minuten bis Stunden vor einem Brand; ein Sensordurchbruch im Gehäuse = Verlust der hermetischen Dichtigkeit und Zertifizierung.
- Unser Stack: ein Gas-/Temperatur-Knoten im Pack, Energie und Telemetrie über ein Piezopaar durch 2–3 mm Aluminium. Null Bohrungen.
- Wer schon dort ist: Liminal Insights — akustische *Diagnostik von außen* (Patente auf Analysemethoden, nicht auf den Kanal). Niemand verkauft Knoten *innerhalb* des Packs.
- Nischenreife: der Markt wächst explosionsartig, das Regal ist leer. Für die Plattform — Showcase-Anwendung Nr. 1.

## 2. Laborausstattung: Vakuumkammern, Kryostaten, Glove-Boxen
- Schmerzpunkt: jede elektrische Durchführung in eine Vakuumkammer ist ein Flansch, der Hunderte Dollar kostet, und eine Leckquelle; in einem Kryostaten bedeutet ein Kabel = Wärmeleck.
- Unser Stack: ein Sensor innerhalb der Kammer, Energie/Daten per Schall durch die Stahlwand; für die Vakuum-Sandwiches von Dewars — LF-Magnetik (bit/s reicht locker für einen T-Logger).
- Wer schon dort ist: niemand mit drahtlosem Durchwand-Transfer; Labore leben von Durchführungsflanschen.
- Reife: die ideale Startnische für Open Source — Labore sind genau das Publikum für Open Hardware (der TinyLev-Pfad): sie kaufen ohne Zertifizierungen und zitieren Sie in Publikationen.

## 3. Lebensmittelproduktion: Fermenter, Autoklaven (Bier, Wein, Milch)
- Schmerzpunkt: Hygienevorschriften hassen Durchbrüche (CIP-Reinigung, Totzonen); man möchte Dichte/T/Druck im Tank jederzeit kennen.
- Unser Stack: ein Knoten an der Innenwand eines Edelstahltanks, abgefragt von außen mit einem Handscanner oder einem festen Paar.
- Wer schon dort ist: gewöhnliche eingeschraubte Sensoren; keine drahtlosen Durchwand-Lösungen.
- Reife: buchstäblich in Reichweite eines Garagentests (jede Craft-Brauerei ist ein Testgelände in Gehweite).
- Physikalischer Hinweis: ein voller Tank belastet die Wand — neu abgleichen gegen das volle Gefäß, und die kontinuierliche Leistung ≲1 W/cm² halten; darüber hinaus Kavitation im Produkt (CO₂-Entgasung, Fehlaromen, langfristige Wandlerosion) — [Theorie](00-theory.md#effect-on-the-wall-and-the-media-behind-it).

## 4. Pipelines, Druckbehälter, industrielle NDT
- Schmerzpunkt: Überwachung von Korrosion/Parametern im Inneren ohne Stillstand oder Durchbruch; Oberflächen sind heiß, lackiert, schmutzig.
- Unser Stack: eine EMAT-„Scanner-Pistole" — gegen ein Rohr pressen ohne jegliche Oberflächenvorbereitung, einen passiven Resonanz-Beacon von innen auslesen.
- Wer schon dort ist: Aufschraub-Ultraschall-Durchflussmesser und Dickenmessgeräte (ein reifer Markt), aber keine interaktiven Beacons im Inneren.
- Reife: mittelfristig; erfordert den EMAT-Zweig (Stufe ~6).

## 5. Öl & Gas / Downhole, und Nuklear
- Wer schon dort ist: Metrol, Acoustic Data, Baker Hughes (Downhole, 30 Jahre, Service-Modell); DOE/UNT/Westinghouse R&D (Nuklear-Behälter).
- Ehrliches Urteil: besetzt und streng reguliert — da gehen wir nicht hin, aber ihre bloße Existenz = Beweis, dass diese Physik für ernstes Geld verkauft wird. Als Referenz im README verwenden.

## 6. Maritime Logistik und Unterwasserstrukturen
- Schmerzpunkt: „ist die Ladung lebendig" in einem versiegelten Container; Daten von der Innenseite eines Schiffsrumpfs.
- Wer schon dort ist: CSignum (LF-EM durch Wasser/Schotten) — der einzige direkte Nachbar in hybrider Philosophie.
- Reife: langfristig; für uns, vorerst, nur eine Denkrichtung.

## Prioritäten (was tun, in welcher Reihenfolge)
1. **Jetzt:** Plattform-Stufen 1–4 im Showcase-Szenario „Laborkammer / verschweißte Box" (Nische #2 — die offenste für Open Source).
2. **Als Nächstes:** eine Demo an einem Live-Objekt aus Nische #3 (ein Brauerei-Tank) — günstig, fotogen, ein echter Nutzer.
3. **Mittelfristig:** das Batterie-Szenario (Nische #1) als Flaggschiff-Fall für Publikation; der EMAT-Zweig für Nische #4.

*Passive Vision (Myon-Radiografie) wurde in ein separates Projekt ausgegliedert — siehe muon-lab in der Wissensbasis.*
