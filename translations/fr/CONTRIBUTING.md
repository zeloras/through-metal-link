# Comment contribuer

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · Français · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Merci de vouloir faire avancer le canal ouvert à travers l'acier. Les trois règles ci-dessous ne sont pas de la bureaucratie — ce sont l'armure brevet du projet (voir [LICENSES.md](LICENSES.md) pour comprendre pourquoi).

## 1. Licences de contribution (entrant = sortant)

En soumettant une contribution, vous acceptez qu'elle soit licenciée de la même manière que le reste du contenu de son répertoire :

- `software/`, `firmware/` → Apache-2.0 ;
- `hardware/` → CERN-OHL-W v2 ;
- `docs/`, `experiments/` → CC-BY-4.0.

**Octroi de brevet.** De plus — étant donné que CC-BY-4.0 ne licencie pas les brevets — vous accordez au projet et à tous les destinataires de ses contenus une licence de brevet perpétuelle, irrévocable, mondiale, libre de redevance, non exclusive, pour fabriquer, faire fabriquer, utiliser, offrir à la vente, vendre, importer et autrement transférer votre contribution, tant seule que comprise dans le projet — dans la mesure de vos revendications de brevet nécessairement contrefaites par la contribution seule ou par sa combinaison avec le projet auquel elle a été soumise. Les termes suivent le §3 d'Apache-2.0, quel que soit le répertoire dans lequel la contribution a atterri. Si vous engagez une action en contrefaçon de brevet contre quiconque (y compris en reconvention) alléguant que les contenus du projet contrefont votre brevet, alors toutes les licences de **brevet** qui vous ont été accordées par le projet et ses contributeurs au titre de cette clause et des licences du projet prennent fin à la date où cette action est engagée.

## 2. DCO : une signature sur la provenance

Chaque commit porte un sign-off (`git commit -s`), signifiant l'accord avec le [Developer Certificate of Origin 1.1](https://developercertificate.org/) : vous confirmez que vous avez le droit de soumettre cette contribution sous la licence du projet.

```
Signed-off-by: Prénom Nom <email@example.com>
```

Les PR sans sign-off ne sont pas fusionnées ; la vérification est automatique — le job CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) fait échouer la PR si un seul commit manque de sign-off. La protection par brevet de la couche docs repose exactement sur cette chaîne — pas d'exception.

**Déplacement de contenu entre couches.** Le contenu vit dans la couche où il a atterri (et sous la licence de cette couche). Déplacer du texte/code entre des couches de licences différentes est autorisé uniquement s'il s'agit de votre propre contenu, ou avec une note explicite de la licence d'origine du fragment.

## 3. Hygiène des brevets et protocole d'expérimentation

- Chaque décision technique doit remonter à une source libre — un brevet expiré ou un article de [docs/01-prior-art.md](docs/01-prior-art.md). Les implémentations de revendications en vigueur (également listées là) ne sont pas acceptées avant l'expiration de ces revendications.
- Résultats expérimentaux — uniquement via le modèle [experiments/TEMPLATE.md](experiments/TEMPLATE.md) : un protocole daté et reproductible est précisément ce qui constitue notre antériorité (prior art).
- Les décisions d'architecture passent par des ADR dans [docs/decisions/](docs/decisions/).
- Les commentaires de code, docstrings, identifiants et messages de commit sont en anglais uniquement. La documentation est multilingue (voir ci-dessous) ; les étiquettes de figures visibles par l'utilisateur vivent dans `labels.json`.

## 4. Documentation multilingue : modifiez une langue, CI synchronise les autres

L'anglais est la langue primaire et possède les chemins canoniques. Chaque autre langue est un arbre miroir sous [translations/](..) avec des noms de fichiers identiques — markdown, le CSV de BOM et les figures générées inclus ; le texte des figures est piloté par `labels.json`. Vous n'avez **pas** à maintenir les miroirs à la main :

- Modifiez la langue qui vous convient. Au push, le workflow [Translation sync](../../.github/workflows/translate.yml) traduit les contreparties avec un LLM à poids ouverts (`glm-5.2` sur Ollama Cloud), régénère les figures quand la synchro met à jour `labels.json`, et commite le résultat avec le marqueur `[translate-sync]`. Tout endpoint compatible OpenAI fonctionne — définissez `OPENAI_BASE_URL` et `TRANSLATE_MODEL`.
- Ce qui reste à faire est suivi dans `translations/.sync-state.json`, qui enregistre le contenu primaire à partir duquel chaque traduction a été réalisée. Une exécution interrompue par un quota ou un délai d'attente ne perd donc rien : les paires inachevées restent marquées comme périmées et sont reprises au prochain push ou par l'exécution nocturne. Ne modifiez pas ce fichier à la main.
- Si vous avez modifié **plusieurs** langues d'un document vous-même, chaque version que vous avez touchée est conservée telle que vous l'avez écrite ; le bot ne remplit que les langues que vous n'avez pas touchées.
- **`labels.json` fait exception à « modifiez n'importe quelle langue ».** Les étiquettes de figures circulent uniquement du primaire vers les miroirs. Modifier une étiquette traduite corrige cette langue et s'arrête là ; elle ne remonte pas vers l'anglais. Pour changer ce qu'une étiquette *dit*, modifiez la section primaire. La raison est l'asymétrie : une modification d'étiquette est presque toujours quelqu'un qui corrige le libellé de la machine, et laisser cela réécrire le primaire redéfinirait la source dont les quatorze miroirs sont générés. Les clés que le bot n'a jamais produites remontent tout de même, donc une étiquette rédigée à la main n'est pas bloquée dans une seule langue.
- La traduction automatique est commitée — parcourez le commit du bot et retouchez le libellé s'il manque le ton ; votre correction ne sera pas écrasée (le bot enregistre votre version comme la version courante).
- Une réponse qui revient tronquée ou avec des placeholders `labels.json` altérés est rejetée plutôt que commitée, et la paire est réessayée — donc un trou étrange dans un miroir est une paire périmée, pas une décision.
- **PR externes :** le bot tourne sur `master`, donc une PR peut ne modifier qu'une seule langue — les miroirs (y compris l'anglais) se mettent à niveau automatiquement juste après la fusion. Vous n'avez pas besoin de connaître l'anglais pour contribuer à la documentation.
- **Ajouter une langue :** ajoutez son code et son nom à [i18n.json](../../i18n.json) (par ex. `"fr": "Français"`) et pushez — le pipeline construit tout le miroir `translations/fr/` : chaque doc, une section `fr` dans chaque `labels.json`, le jeu de figures et les sélecteurs de langue partout.
- **Écritures non latines :** CI installe les familles Noto (`fonts-noto-core`, `fonts-noto-cjk`) et les moteurs de rendu parcourent la pile de polices dans `i18n.json` → `render.fonts`, de sorte que le cyrillique, le Han, les kana et le Hangul sortent correctement. Un moteur de rendu vérifie désormais la couverture des glyphes avant de dessiner et **échoue plutôt que d'afficher des carrés `.notdef`** — cette vérification existe parce que les figures chinoises ont été livrées comme une grille de tofu et que rien dans CI ne regarde les pixels. Si elle se déclenche, ajoutez la police Noto pour cette écriture à la pile.
- **Écritures nécessitant une mise en forme contextuelle** — arabe et persan (RTL, formes liées), devanagari et bengali (conjoints) — ne peuvent pas être dessinées correctement par matplotlib, qui n'a pas de moteur de mise en forme : même avec la bonne police, les glyphes sortent non liés et mal ordonnés. Listez ces langues dans `i18n.json` → `render.skip_figures`. Leur prose n'est pas affectée ; leur documentation se contente de lier les figures primaires, ce que la réparation de liens dans [tools/translate_sync.py](../../tools/translate_sync.py) pointe automatiquement. `hi` est configuré ainsi.
- **Garde d'écriture :** `SCRIPTS` dans [tools/i18n_render.py](../../tools/i18n_render.py) enregistre l'écriture que les étiquettes de chaque langue doivent contenir. Une réponse qui n'en a aucune — les sections `ja` ont déjà été livrées remplies de russe — est rejetée et réessayée plutôt que commitée. Une langue absente de cette table n'a simplement pas de garde, donc en ajouter une à `i18n.json` ne casse jamais ; ajoutez l'entrée pour activer la vérification.

## 5. Vérifications que vous pouvez lancer avant de pousser

```bash
python tools/check_repo.py
```

Vérifie ce que le bot de traduction est capable de casser et que rien d'autre ne détecterait : chaque lien relatif résout, chaque section `labels.json` correspond à `i18n.json` et porte les mêmes clés et les mêmes placeholders `str.format` que la section primaire, chaque doc canonique a un miroir dans chaque langue, et chaque fichier markdown a sa barre de langue. CI l'exécute sur les deux workflows ; il ne nécessite aucune dépendance.

Le reste de CI ([ci.yml](../../.github/workflows/ci.yml)) compile les scripts et exécute tout le pipeline de figures. Pour le reproduire exactement — figures commitées comprises — installez la chaîne d'outils épinglée, pas la version lâche :

```bash
python -m pip install -r tools/requirements-ci.txt
```
