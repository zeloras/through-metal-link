# Wie man beiträgt

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · Deutsch · [Português](../pt/CONTRIBUTING.md)

Vielen Dank, dass Sie den offenen Durch-Stahl-Kanal vorantreiben möchten. Die vier Regeln unten sind keine Bürokratie — sie sind die Patentrüstung des Projekts (siehe [LICENSES.md](../../LICENSES.md) für den Grund).

## 1. Beitragslizenzen (inbound = outbound)

Durch die Einreichung eines Beitrags stimmen Sie zu, dass er unter der gleichen Lizenz wie der Rest des Materials in seinem Verzeichnis steht:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Patentgewährung.** Zusätzlich — da CC-BY-4.0 keine Patente lizenziert — gewähren Sie dem Projekt und allen Empfängern seiner Materialien eine perpetuelle, unwiderrufliche, weltweite, gebührenfreie, nicht-exklusive Patentlizenz, um Ihren Beitrag herzustellen, herstellen zu lassen, zu verwenden, zum Verkauf anzubieten, zu verkaufen, einzuführen und auf andere Weise zu übertragen — in dem Umfang, in dem Ihre Patentansprüche notwendigerweise durch den Beitrag selbst oder durch dessen Kombination mit dem Projekt, dem er eingereicht wurde, verletzt werden. Die Bedingungen folgen §3 von Apache-2.0, unabhängig davon, in welchem Verzeichnis der Beitrag gelandet ist. Wenn Sie Patentstreitigkeiten gegen jemanden einleiten (einschließlich einer Gegenklage), die behaupten, dass die Materialien des Projekts Ihre Patente verletzen, dann enden alle **Patent**-Lizenzen, die Ihnen von dem Projekt und seinen Mitwirkenden unter dieser Klausel und unter den Lizenzen des Projekts gewährt wurden, mit dem Datum, an dem diese Streitigkeiten eingereicht werden.

## 2. DCO: eine Signatur auf die Herkunft

Jeder Commit trägt eine Signatur (`git commit -s`), die die Zustimmung zu dem [Developer Certificate of Origin 1.1](https://developercertificate.org/) bedeutet: Sie bestätigen, dass Sie das Recht haben, diesen Beitrag unter der Lizenz des Projekts einzureichen.

```
Signed-off-by: Vorname Nachname <email@example.com>
```

Pull-Requests ohne Signatur werden nicht zusammengeführt; die Überprüfung ist automatisch — der CI-Job [../../.github/workflows/dco.yml](../../.github/workflows/dco.yml) schlägt den Pull-Request fehl, wenn auch nur ein einzelner Commit keine Signatur hat. Der Patentschutz der Dokumentationsebene beruht genau auf dieser Kette — keine Ausnahmen.

**Umzug von Material zwischen Ebenen.** Material lebt in der Ebene, in der es gelandet ist (und unter der Lizenz dieser Ebene). Der Umzug von Text/Code zwischen Ebenen mit unterschiedlichen Lizenzen ist nur erlaubt, wenn es sich um Ihr eigenes Material handelt oder mit einer expliziten Notiz des ursprünglichen Lizenzfragments.

## 3. Patenthygiene und Experimentprotokoll

- Jede technische Entscheidung muss auf eine freie Quelle zurückverfolgt werden können — ein abgelaufenes Patent oder ein Papier aus [docs/01-prior-art.md](../../docs/01-prior-art.md). Implementierungen von lebenden Ansprüchen (die dort ebenfalls aufgeführt sind) werden nicht akzeptiert, bis diese Ansprüche ablaufen.
- Experimentelle Ergebnisse — nur über das [experiments/TEMPLATE.md](../../experiments/TEMPLATE.md)-Template: ein datiertes, reproduzierbares Protokoll ist genau das, was unsere Vorarbeiten ausmacht.
- Architekturentscheidungen werden in ADRs in [docs/decisions/](../../docs/decisions/) durchgeführt.
- Code-Kommentare, Docstrings, Bezeichner und Commit-Nachrichten sind englisch-only. Dokumentationen sind multilingual (siehe unten); benutzerseitige Figurenbeschriftungen leben in `labels.json`.

## 4. Mehrsprachige Dokumentation: bearbeiten Sie eine Sprache, CI synchronisiert die anderen

Englisch ist primär und besitzt die kanonischen Pfade. Jede andere Sprache ist ein Spiegelbaum unter [translations/](..) mit identischen Dateinamen — Markdown, die BOM-CSV und generierte Abbildungen eingeschlossen; Abbildungstext wird von `labels.json` gesteuert. Sie müssen **nicht** die Spiegel manuell pflegen:

- Bearbeiten Sie die Sprache, die Ihnen am bequemsten ist. Bei Push findet der [Übersetzungs-Sync](../../.github/workflows/translate.yml)-Workflow Dokumente, bei denen nur eine Sprache geändert wurde, übersetzt die Gegenstücke mit GitHub-Modellen (`meta/llama-3.3-70b-instruct`, keine API-Schlüssel erforderlich), regeneriert Abbildungen, wenn der Sync `labels.json` aktualisiert, und committet das Ergebnis zurück mit dem `[translate-sync]`-Marker.
- Wenn Sie **mehrere** Sprachen eines Dokuments selbst bearbeitet haben, lässt der Bot es in Ruhe.
- Maschinelle Übersetzungen werden committet — überprüfen Sie den Commit des Bots und korrigieren Sie die Formulierung, wenn er den Ton verfehlt; Ihre Korrektur wird nicht überschrieben (der Bot reagiert nur auf neue Änderungen).
- **Externe Pull-Requests:** der Bot läuft auf `master`, sodass ein Pull-Request nur eine Sprache ändern kann — die Spiegel (einschließlich Englisch) werden automatisch nach dem Merge aktualisiert. Sie müssen kein Englisch sprechen, um Dokumentation beizutragen.
- **Hinzufügen einer Sprache:** fügen Sie den Code und den Namen zu [i18n.json](../../i18n.json) hinzu (z. B. `"fr": "Französisch"`) und pushen Sie — die Pipeline baut den gesamten `translations/fr/`-Spiegel: jedes Dokument, einen `fr`-Abschnitt in jedem `labels.json`, die Abbildungssammlung und die Sprachumschalter überall.
- **Nicht-lateinische Schriften (CJK usw.):** die Abbildungswiedergabe enthält derzeit nur lateinische und kyrillische Schriften; bevor Sie z. B. Japanisch zu i18n.json hinzufügen, muss eine CJK-Schrift in die Render-Skripte eingebunden werden — eröffnen Sie zuerst ein Issue.
