# Mitwirken

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · Deutsch · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Danke, dass du den offenen Durch-Stahl-Kanal voranbringen möchtest. Die drei Regeln weiter unten sind keine Bürokratie — sie sind die Patentrüstung des Projekts (siehe [LICENSES.md](LICENSES.md) für das Warum).

## 1. Beitragslizenzen (inbound = outbound)

Mit der Einreichung eines Beitrags stimmen Sie zu, dass er unter derselben Lizenz steht wie der Rest des Materials in seinem Verzeichnis:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Patenterteilung.** Zusätzlich — da CC-BY-4.0 keine Patente lizenziert — erteilen Sie dem Projekt und allen Empfängern seiner Materialien eine unbefristete, unwiderrufliche, weltweite, lizenzgebührenfreie, nicht-exklusive Patentlizenz, Ihren Beitrag herzustellen, herstellen zu lassen, zu nutzen, zum Verkauf anzubieten, zu verkaufen, zu importieren und anderweitig zu übertragen, sowohl eigenständig als auch als Teil des Projekts — in dem Umfang, in dem Ihre Patentansprüche notwendigerweise durch den Beitrag allein oder durch seine Kombination mit dem Projekt, bei dem er eingereicht wurde, verletzt werden. Die Bedingungen folgen §3 von Apache-2.0, unabhängig davon, in welchem Verzeichnis der Beitrag gelandet ist. Wenn Sie eine Patentklage gegen jemanden (einschließlich einer Gegenklage) einreichen, in der behauptet wird, dass die Materialien des Projekts Ihr Patent verletzen, dann enden alle **Patent**-Lizenzen, die Ihnen durch das Projekt und seine Mitwirkenden unter dieser Klausel und unter den Lizenzen des Projekts gewährt wurden, ab dem Datum der Einreichung einer solchen Klage.

## 2. DCO: eine Signatur für die Herkunft

Signed-off-by: Firstname Lastname <email@example.com>
```

PRs ohne Sign-off werden nicht gemergt; die Prüfung erfolgt automatisch — der CI-Job [.github/workflows/dco.yml](../../.github/workflows/dco.yml) lässt den PR fehlschlagen, wenn auch nur ein einziger Commit das Sign-off vermissen lässt. Der Patentschutz der Docs-Schicht beruht exakt auf dieser Kette — keine Ausnahmen.

**Material zwischen Schichten verschieben.** Material verbleibt in der Schicht, in der es gelandet ist (und unter der Lizenz dieser Schicht). Das Verschieben von Text/Code zwischen Schichten mit unterschiedlichen Lizenzen ist nur zulässig, wenn es sich um Dein eigenes Material handelt oder mit einem ausdrücklichen Hinweis auf die ursprüngliche Lizenz des Fragments.

## 3. Patent-Hygiene und Experimentprotokoll

- Jede technische Entscheidung muss auf eine frei zugängliche Quelle zurückzuführen sein — ein abgelaufenes Patent oder eine Publikation aus [docs/01-prior-art.md](docs/01-prior-art.md). Implementierungen noch laufender Patentansprüche (ebenfalls dort aufgeführt) werden erst akzeptiert, wenn diese Ansprüche ablaufen.
- Experimentelle Ergebnisse — ausschließlich über die Vorlage [experiments/TEMPLATE.md](experiments/TEMPLATE.md): ein datiertes, reproduzierbares Protokoll ist genau das, was unseren Stand der Technik ausmacht.
- Architekturentscheidungen laufen über ADRs in [docs/decisions/](docs/decisions/).
- Code-Kommentare, Docstrings, Bezeichner und Commit-Messages sind ausschließlich auf Englisch. Dokumentationen sind mehrsprachig (siehe unten); nutzersichtbare Beschriftungen in Abbildungen liegen in `labels.json`.

## 4. Mehrsprachige Dokumentation: eine Sprache bearbeiten, CI synchronisiert den Rest

Englisch ist die primäre Sprache und besitzt die kanonischen Pfade. Jede andere Sprache ist ein Spiegelbaum unter [translations/](..) mit identischen Dateinamen — Markdown, die BOM-CSV und generierte Abbildungen inbegriffen; der Abbildungstext wird durch `labels.json` gesteuert. Sie müssen die Spiegel **nicht** von Hand pflegen:

- Bearbeiten Sie, welche Sprache Ihnen angenehm ist. Beim Push übersetzt der [Translation sync](../../.github/workflows/translate.yml)-Workflow die Gegenstücke mit einem Open-Weights-LLM (`glm-5.2` auf Ollama Cloud), regeneriert Abbildungen, wenn der Sync `labels.json` aktualisiert, und committet das Ergebnis mit dem Marker `[translate-sync]` zurück. Jeder OpenAI-kompatible Endpunkt funktioniert — setzen Sie `OPENAI_BASE_URL` und `TRANSLATE_MODEL`.
- Was noch Arbeit erfordert, wird in `translations/.sync-state.json` verfolgt, das den primären Inhalt aufzeichnet, aus dem jede Übersetzung erstellt wurde. Ein durch ein Kontingent oder ein Timeout abgebrochener Lauf verliert daher nichts: Die unvollständigen Paare bleiben als veraltet markiert und werden beim nächsten Push oder beim nächtlichen Lauf abgeholt. Bearbeiten Sie diese Datei nicht von Hand.
- Wenn Sie **mehrere** Sprachen eines Dokuments selbst bearbeitet haben, wird jede von Ihnen berührte Version so beibehalten, wie Sie sie geschrieben haben; der Bot füllt nur die Sprachen aus, die Sie nicht berührt haben.
- **`labels.json` ist die Ausnahme von „bearbeite jede Sprache“.** Abbildungsbeschriftungen fließen nur von primär → Spiegel. Das Bearbeiten einer übersetzten Beschriftung korrigiert diese Sprache und stoppt dort; sie wandert nicht zurück ins Englische. Um zu ändern, was ein Label *sagt*, bearbeiten Sie den primären Abschnitt. Der Grund ist Asymmetrie: Eine Label-Bearbeitung ist fast immer jemand, der die Wortwahl der Maschine korrigiert, und wenn man dies das Primäre umschreiben ließe, würde das die Quelle neu definieren, aus der alle vierzehn Spiegel generiert werden. Schlüssel, die der Bot noch nie produziert hat, propagieren weiterhin zurück, sodass ein handgeschriebenes Label nicht in einer Sprache feststeckt.
- Maschinelle Übersetzung wird committet — überfliegen Sie den Commit des Bots und passen Sie die Wortwahl an, wenn er den Ton verfehlt; Ihre Korrektur wird nicht überschrieben (der Bot zeichnet Ihre Version als die aktuelle auf).
- Eine Antwort, die abgeschnitten oder mit verstümmelten `labels.json`-Platzhaltern zurückkam, wird verworfen statt committet, und das Paar wird erneut versucht — also ist eine seltsam aussehende Lücke in einem Spiegel ein veraltetes Paar, keine Entscheidung.
- **Externe PRs:** Der Bot läuft auf `master`, daher kann ein PR nur eine Sprache ändern — die Spiegel (einschließlich Englisch) holen automatisch direkt nach dem Merge auf. Sie müssen kein Englisch kennen, um Dokumente beizusteuern.
- **Hinzufügen einer Sprache:** Fügen Sie ihren Code und Namen zu [i18n.json](../../i18n.json) hinzu (z. B. `"fr": "Français"`) und pushen Sie — die Pipeline baut den gesamten `translations/fr/`-Spiegel auf: jedes Dokument, einen `fr`-Abschnitt in jedem `labels.json`, den Abbildungssatz und die Sprachumschalter überall.
- **Nicht-lateinische Schriften:** CI installiert die Noto-Familien (`fonts-noto-core`, `fonts-noto-cjk`) und die Renderer gehen den Font-Stack in `i18n.json` → `render.fonts` durch, sodass Kyrillisch, Han, Kana und Hangul richtig herauskommen. Ein Renderer prüft jetzt die Glyphenabdeckung vor dem Zeichnen und **schlägt fehl, anstatt `.notdef`-Boxen zu malen** — diese Prüfung existiert, weil die chinesischen Abbildungen als ein Raster aus Tofu ausgeliefert wurden und nichts in CI auf Pixel schaut. Wenn sie auslöst, fügen Sie den Noto-Schriftschnitt für diese Schrift zum Stack hinzu.
- **Schriften, die kontextuelle Formung benötigen** — Arabisch und Persisch (RTL, verbundene Formen), Devanagari und Bengalisch (Konjunktionen) — können von matplotlib, das keine Formungs-Engine hat, nicht richtig gezeichnet werden: selbst mit dem richtigen Font kommen die Glyphen unverbunden und falsch geordnet heraus. Listen Sie diese Sprachen in `i18n.json` → `render.skip_figures` auf. Ihre Prosa ist unbeeinträchtigt; ihre Dokumente verlinken einfach auf die primären Abbildungen, auf die die Link-Reparatur in [tools/translate_sync.py](../../tools/translate_sync.py) automatisch verweist. `hi` ist auf diese Weise eingerichtet.
- **Schrift-Wächter:** `SCRIPTS` in [tools/i18n_render.py](../../tools/i18n_render.py) zeichnet auf, welche Schrift die Labels jeder Sprache enthalten müssen. Eine Antwort, die keine davon hat — die `ja`-Abschnitte wurden einmal mit Russisch gefüllt ausgeliefert — wird abgelehnt und erneut versucht, statt committet. Eine Sprache, die in dieser Tabelle fehlt, bekommt einfach keinen Wächter, sodass das Hinzufügen einer zu `i18n.json` niemals kaputtgeht; fügen Sie den Eintrag hinzu, um die Prüfung zu erhalten.

## 5. Prüfungen, die Sie vor dem Pushen ausführen können

python tools/check_repo.py
```

Prüft, was der Übersetzungs-Bot kaputt machen kann und was sonst nichts anderes abfängt: jeder relative Link löst auf, jeder `labels.json`-Abschnitt stimmt mit `i18n.json` überein und trägt dieselben Schlüssel und dieselben `str.format`-Platzhalter wie der primäre Abschnitt, jedes kanonische Dokument hat ein Spiegelbild in jeder Sprache und jede Markdown-Datei hat ihre Sprachleiste. CI führt ihn in beiden Workflows aus; er benötigt keine Abhängigkeiten.

Der Rest von CI ([ci.yml](../../.github/workflows/ci.yml)) kompiliert die Skripte und führt die gesamte Abbildungs-Pipeline aus. Um es exakt nachzuvollziehen — einschließlich der committeten Abbildungen — installieren Sie die gepinnte Toolchain, nicht die lose:

```bash
python -m pip install -r tools/requirements-ci.txt
