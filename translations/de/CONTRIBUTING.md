# Wie man beiträgt

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · Deutsch · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Danke, dass Sie den offenen Durch-Stahl-Kanal voranbringen möchten. Die drei Regeln unten sind keine Bürokratie — sie sind die Patentrüstung des Projekts (siehe [LICENSES.md](LICENSES.md) für das Warum).

## 1. Beitragslizenzen (inbound = outbound)

Mit der Einreichung eines Beitrags stimmen Sie zu, dass er unter derselben Lizenz steht wie der Rest des Materials in seinem Verzeichnis:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Patenterteilung.** Zusätzlich — da CC-BY-4.0 keine Patente lizenziert — erteilen Sie dem Projekt und allen Empfängern seiner Materialien eine unbefristete, unwiderrufliche, weltweite, lizenzgebührenfreie, nicht-exklusive Patenterlaubnis zur Herstellung, Herstellung durch Dritte, Nutzung, zum Angebot, Verkauf, Import und sonstigen Übertragung Ihres Beitrags, sowohl eigenständig als auch als Teil des Projekts — soweit Ihre Patentansprüche zwangsläufig durch den Beitrag allein oder in Kombination mit dem Projekt, für das er eingereicht wurde, verletzt werden. Die Bedingungen folgen §3 von Apache-2.0, unabhängig davon, in welchem Verzeichnis der Beitrag gelandet ist. Wenn Sie eine Patentklage gegen jemanden (einschließlich einer Gegenklage) anstrengen, in der behauptet wird, dass die Materialien des Projekts Ihr Patent verletzen, dann enden alle **Patent**-Lizenzen, die Ihnen vom Projekt und seinen Mitwirkenden unter dieser Klausel und unter den Lizenzen des Projekts erteilt wurden, zum Zeitpunkt der Einreichung der Klage.

## 2. DCO: eine Signatur für die Herkunft

Jeder Commit trägt eine Sign-off-Zeile (`git commit -s`), die die Zustimmung zum [Developer Certificate of Origin 1.1](https://developercertificate.org/) bestätigt: Sie bestätigen, dass Sie das Recht haben, diesen Beitrag unter der Lizenz des Projekts einzureichen.

```
Signed-off-by: Vorname Nachname <email@example.com>
```

PRs ohne Sign-off werden nicht gemergt; die Prüfung erfolgt automatisch — der CI-Job [.github/workflows/dco.yml](../../.github/workflows/dco.yml) lässt den PR fehlschlagen, wenn auch nur ein einziger Commit ohne Sign-off ist. Der Patentschutz der Dokumentationsschicht beruht genau auf dieser Kette — keine Ausnahmen.

**Material zwischen Schichten verschieben.** Material bleibt in der Schicht, in der es gelandet ist (und unter deren Lizenz). Das Verschieben von Text/Code zwischen Schichten mit unterschiedlichen Lizenzen ist nur erlaubt, wenn es Ihr eigenes Material ist, oder mit einem expliziten Hinweis auf die ursprüngliche Lizenz des Fragments.

## 3. Patenthygiene und Experimentprotokoll

- Jede technische Entscheidung muss auf eine freie Quelle zurückführbar sein — ein abgelaufenes Patent oder eine Arbeit aus [docs/01-prior-art.md](docs/01-prior-art.md). Implementierungen von lebenden Patentansprüchen (ebenfalls dort aufgeführt) werden nicht akzeptiert, bis diese Ansprüche ablaufen.
- Experimentelle Ergebnisse — nur über die Vorlage [experiments/TEMPLATE.md](experiments/TEMPLATE.md): ein datiertes, reproduzierbares Protokoll ist genau das, was unseren Stand der Technik ausmacht.
- Architekturentscheidungen laufen über ADRs in [docs/decisions/](docs/decisions/).
- Codekommentare, Docstrings, Bezeichner und Commit-Nachrichten sind nur auf Englisch. Doku ist mehrsprachig (siehe unten); benutzersichtbare Abbildungsbeschriftungen leben in `labels.json`.

## 4. Mehrsprachige Doku: eine Sprache bearbeiten, CI synchronisiert den Rest

Englisch ist primär und besitzt die kanonischen Pfade. Jede andere Sprache ist ein Spiegelbaum unter [translations/](..) mit identischen Dateinamen — Markdown, die BOM-CSV und generierte Abbildungen inbegriffen; Abbildungstext wird durch `labels.json` gesteuert. Sie müssen die Spiegel **nicht** von Hand pflegen:

- Bearbeiten Sie, welche Sprache Ihnen bequem ist. Beim Push übersetzt der [Translation sync](../../.github/workflows/translate.yml)-Workflow die Gegenstücke mit einem Open-Weights-LLM (`glm-5.2` auf Ollama Cloud), regeneriert Abbildungen, wenn der Sync `labels.json` aktualisiert, und committet das Ergebnis mit dem Marker `[translate-sync]`. Jeder OpenAI-kompatible Endpunkt funktioniert — setzen Sie `OPENAI_BASE_URL` und `TRANSLATE_MODEL`.
- Was noch Nacharbeit braucht, wird in `translations/.sync-state.json` verfolgt, das den primären Inhalt aufzeichnet, aus dem jede Übersetzung erstellt wurde. Ein durch Kontingent oder Timeout abgebrochener Lauf verliert also nichts: die unfertigen Paare bleiben als veraltet markiert und werden beim nächsten Push oder beim nächtlichen Lauf abgeholt. Bearbeiten Sie diese Datei nicht von Hand.
- Wenn Sie **mehrere** Sprachen eines Dokuments selbst bearbeitet haben, wird jede Version, die Sie angefasst haben, so belassen, wie Sie sie geschrieben haben; der Bot füllt nur die Sprachen aus, die Sie nicht angefasst haben.
- **`labels.json` ist die Ausnahme zu „beliebige Sprache bearbeiten".** Abbildungsbeschriftungen fließen nur von primär → Spiegel. Das Bearbeiten einer übersetzten Beschriftung korrigiert diese Sprache und stoppt dort; sie wandert nicht zurück ins Englische. Um zu ändern, was ein Label *sagt*, bearbeiten Sie den primären Abschnitt. Der Grund ist die Asymmetrie: Eine Label-Bearbeitung ist fast immer jemand, der die Wortwahl der Maschine korrigiert, und das die Primärversion umschreiben zu lassen, würde die Quelle neu definieren, aus der alle vierzehn Spiegel generiert werden. Schlüssel, die der Bot noch nie erzeugt hat, wandern trotzdem zurück, sodass ein selbst verfasstes Label nicht in einer Sprache stecken bleibt.
- Maschinelle Übersetzung wird committet — überfliegen Sie den Commit des Bots und verbessern Sie die Formulierung, wenn er den Ton verfehlt; Ihre Korrektur wird nicht überschrieben (der Bot notiert Ihre Version als die aktuelle).
- Eine Antwort, die abgeschnitten zurückkam oder mit verstümmelten `labels.json`-Platzhaltern, wird verworfen statt committet, und das Paar wird erneut versucht — also ist eine seltsam aussehende Lücke in einem Spiegel ein veraltetes Paar, keine Entscheidung.
- **Externe PRs:** der Bot läuft auf `master`, daher kann ein PR nur eine Sprache ändern — die Spiegel (einschließlich Englisch) holen automatisch nach dem Merge auf. Sie müssen kein Englisch kennen, um Doku beizutragen.
- **Eine Sprache hinzufügen:** fügen Sie ihren Code und Namen zu [i18n.json](../../i18n.json) hinzu (z. B. `"fr": "Français"`) und pushen Sie — die Pipeline baut den gesamten `translations/fr/`-Spiegel auf: jedes Dokument, einen `fr`-Abschnitt in jedem `labels.json`, den Abbildungssatz und die Sprachumschalter überall.
- **Nicht-lateinische Schriften:** CI installiert die Noto-Familien (`fonts-noto-core`, `fonts-noto-cjk`) und die Renderer durchlaufen den Font-Stack in `i18n.json` → `render.fonts`, sodass Kyrillisch, Han, Kana und Hangul korrekt ausgegeben werden. Ein Renderer prüft jetzt die Glyphenabdeckung vor dem Zeichnen und **schlägt fehl, statt `.notdef`-Boxen zu malen** — diese Prüfung existiert, weil die chinesischen Abbildungen als ein Raster aus Tofu ausgeliefert wurden und nichts in CI auf Pixel schaut. Wenn sie auslöst, fügen Sie das Noto-Fontface für diese Schrift zum Stack hinzu.
- **Schriften, die kontextuelle Formung benötigen** — Arabisch und Persisch (RTL, verbundene Formen), Devanagari und Bengalisch (Konjunktionen) — können von matplotlib nicht korrekt gezeichnet werden, das keine Formungs-Engine hat: selbst mit dem richtigen Font kommen die Glyphen unverbunden und falsch geordnet heraus. Listen Sie diese Sprachen in `i18n.json` → `render.skip_figures`. Deren Prosa ist unbeeinträchtigt; ihre Doku verlinkt einfach auf die primären Abbildungen, auf die der Link-Reparaturer in [tools/translate_sync.py](../../tools/translate_sync.py) automatisch verweist. `hi` ist so eingerichtet.
- **Schrift-Wächter:** `SCRIPTS` in [tools/i18n_render.py](../../tools/i18n_render.py) notiert, welche Schrift die Labels jeder Sprache enthalten müssen. Eine Antwort, die keine davon hat — die `ja`-Abschnitte kamen einmal mit Russisch gefüllt zurück — wird abgelehnt und erneut versucht statt committet. Eine Sprache, die in dieser Tabelle fehlt, bekommt einfach keinen Wächter, sodass das Hinzufügen zu `i18n.json` nie etwas kaputt macht; fügen Sie den Eintrag hinzu, um die Prüfung zu erhalten.

## 5. Prüfungen, die Sie vor dem Push ausführen können

```bash
python tools/check_repo.py
```

Verifiziert, was der Übersetzungsbot kaputt machen kann und nichts anderes abfangen würde: jeder relative Link löst sich auf, jeder `labels.json`-Abschnitt passt zu `i18n.json` und trägt dieselben Schlüssel und dieselben `str.format`-Platzhalter wie der primäre, jedes kanonische Dokument hat einen Spiegel in jeder Sprache, und jede Markdown-Datei hat ihre Sprachleiste. CI führt es auf beiden Workflows aus; es braucht keine Abhängigkeiten.

Der Rest von CI ([ci.yml](../../.github/workflows/ci.yml)) kompiliert die Skripte und führt die gesamte Abbildungs-Pipeline aus. Um es exakt zu reproduzieren — einschließlich der committeten Abbildungen — installieren Sie die gepinnte Toolchain, nicht die lose:

```bash
python -m pip install -r tools/requirements-ci.txt
```
