# Anwendungsübersicht: wer benötigt diesen Technologie-Stack und warum

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · Deutsch

Der Plattform-Stack: ein aktiver Power- und Datenkanal durch blinde Wände — Piezo-Akustik / EMAT / LF-Magnetik. Unten: wo dies in der realen Welt benötigt wird, wer bereits dort ist und was für uns noch übrig bleibt.

## 1. Versiegelte Batteriepacks (EV, Heim-/Industrie-Energiespeicher)
- Problem: Früherkennung von thermischem Durchgehen — Gase (CO₂, H₂, Elektrolyt-Dämpfe) erscheinen innerhalb des Packs Minuten bis Stunden vor einem Brand; eine Sensor-Penetration in der Verkleidung = Verlust der hermetischen Abdichtung und Zertifizierung.
- Unser Stack: ein Gas-/Temperaturknoten innerhalb des Packs, Power und Telemetrie via Piezo-Paar durch 2–3 mm Aluminium. Keine Löcher.
- Wer ist bereits dort: Liminal Insights — akustische *Diagnostics von außen* (Patente auf Analysemethode, nicht auf den Kanal). Niemand verkauft Knoten *innerhalb* des Packs.
- Nischenreife: der Markt wächst explosiv, das Regal ist leer. Für die Plattform — Showcase-Anwendung #1.

## 2. Laboreinrichtungen: Vakuumkammern, Kryostate, Handschuhkästen
- Problem: jeder elektrische Durchgang in eine Vakuumkammer ist ein Flansch im Wert von hunderten Dollar und eine Quelle für Lecks; in einem Kryostat ist ein Kabel = Wärmeleitverlust.
- Unser Stack: ein Sensor innerhalb der Kammer, Power/Daten via Schall durch die Stahlwand; für die Vakuum-Sandwiches von Dewars — LF-Magnetik (Bit/s ist ausreichend für einen T-Logger).
- Wer ist bereits dort: niemand mit drahtloser Durchgangswand; Labore leben von Durchgangsflanschen.
- Reife: die ideale Startnische für Open-Source — Labore sind genau das Publikum für Open-Hardware (der TinyLev-Pfad): sie kaufen ohne Zertifizierungen und zitieren dich in Papieren.

## 3. Lebensmittelproduktion: Fermentationsbehälter, Autoklaven (Bier, Wein, Milch)
- Problem: hygienische Vorschriften hassen Penetrationen (CIP-Wäsche, tote Zonen); du möchtest die Dichte/T/Druck innerhalb des Tanks zu jedem Zeitpunkt kennen.
- Unser Stack: ein Knoten an der Innenwand eines Edelstahl-Tanks, abgefragt von außen mit einem Handscanner oder einem festen Paar.
- Wer ist bereits dort: herkömmliche angeschlossene Sensoren; keine drahtlosen Durchgangswand-Lösungen.
- Reife: buchstäblich in Reichweite eines Garagentests (jede Craft-Brauerei ist ein Testgelände in Laufnähe).

## 4. Rohrleitungen, Druckbehälter, industrielle NDT
- Problem: Überwachung von Korrosion/Parametern innerhalb ohne Stillstand oder Penetration; Oberflächen sind heiß, lackiert, schmutzig.
- Unser Stack: ein EMAT-"Scanner-Gewehr" — drücke es gegen eine Rohrleitung mit keiner Oberflächenpräparation, lies ein passives resonantes Signal von innen.
- Wer ist bereits dort: Klemm-Ultrachall-Durchflussmesser und Dickenmesser (ein ausgereifter Markt), aber keine interaktiven Signale innerhalb.
- Reife: mittlerer Bereich; erfordert den EMAT-Zweig (Stufe ~6).

## 5. Öl & Gas / Tiefbohrung und Kernenergie
- Wer ist bereits dort: Metrol, Acoustic Data, Baker Hughes (Tiefbohrung, 30 Jahre, Service-Modell); DOE/UNT/Westinghouse R&D (Kernenergie-Behälter).
- Ehrliches Urteil: besetzt und stark reguliert — wir gehen nicht dorthin, aber ihre bloße Existenz = Beweis, dass diese Physik für ernstes Geld verkauft wird. Verwenden als Referenz im README.

## 6. Marine-Logistik und Unterwasserstrukturen
- Problem: "ist die Fracht lebendig" in einem versiegelten Container; Daten von der Innenseite des Schiffsrumpfes.
- Wer ist bereits dort: CSignum (LF-EM durch Wasser/Schott) — der einzige direkte Nachbar in hybrider Philosophie.
- Reife: langfristig; für uns, für jetzt, nur eine Richtung des Denkens.

## Prioritäten (was zu tun ist, in welcher Reihenfolge)
1. **Jetzt:** Plattform-Stufen 1–4 auf dem Showcase-Szenario "Laborkammer / verschweißte Box" (Nische #2 — am offensten für Open-Source).
2. **Als nächstes:** ein Demo auf einem Live-Objekt aus Nische #3 (einem Brauerei-Tank) — günstig, fotogen, ein echter Benutzer.
3. **Mittlerer Bereich:** das Batterie-Szenario (Nische #1) als Flaggschiff-Fall für die Veröffentlichung; der EMAT-Zweig für Nische #4.

*Passive Sicht (Myon-Radiographie) wurde in ein separates Projekt ausgelagert — siehe muon-lab im Wissensbasis.
