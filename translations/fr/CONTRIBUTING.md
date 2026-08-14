# Comment contribuer

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · Français · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Merci de vouloir faire avancer le canal ouvert à travers l'acier. Les trois règles ci-dessous ne sont pas de la bureaucratie — elles constituent l'armure brevet du projet (voir [LICENSES.md](LICENSES.md) pour en comprendre la raison).

## 1. Licences de contribution (entrant = sortant)

En soumettant une contribution, vous acceptez qu'elle soit licenciée de la même manière que le reste du matériel dans son répertoire :

- `software/`, `firmware/` → Apache-2.0 ;
- `hardware/` → CERN-OHL-W v2 ;
- `docs/`, `experiments/` → CC-BY-4.0.

**Octroi de brevet.** De plus — étant donné que CC-BY-4.0 ne couvre pas les brevets — vous accordez au projet et à tous les destinataires de ses matériaux une licence de brevet perpétuelle, irrévocable, mondiale, sans redevance et non exclusive pour fabriquer, faire fabriquer, utiliser, offrir à la vente, vendre, importer et transférer de toute autre manière votre contribution, à la fois en elle-même et en tant que partie du projet — dans la mesure de vos revendications de brevet qui sont nécessairement enfreintes par la contribution en elle-même ou par sa combinaison avec le projet auquel elle a été soumise. Les termes suivent le §3 d'Apache-2.0, quel que soit le répertoire dans lequel la contribution a été déposée. Si vous engagez une action en contrefaçon de brevet contre quiconque (y compris par voie de reconvention) alléguant que les matériaux du projet enfreignent votre brevet, alors toutes les licences de **brevet** qui vous ont été accordées par le projet et ses contributeurs en vertu de cette clause et des licences du projet prennent fin à la date à laquelle cette action est intentée.

## 2. DCO : une signature sur la provenance

Signed-off-by: Firstname Lastname <email@example.com>
```

Les PR sans sign-off ne sont pas fusionnées ; la vérification est automatique — le job CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) fait échouer la PR si un seul commit manque de sign-off. La protection par brevet de la couche de documentation repose exactement sur cette chaîne — aucune exception.

**Déplacement de matériel entre les couches.** Le matériel vit dans la couche où il a atterri (et sous la licence de cette couche). Déplacer du texte/code entre des couches avec des licences différentes est autorisé uniquement s'il s'agit de votre propre matériel, ou avec une note explicite de la licence d'origine du fragment.

## 3. Hygiène des brevets et protocole d'expérimentation

- Chaque décision technique doit être rattachée à une source libre — un brevet expiré ou un article issu de [docs/01-prior-art.md](docs/01-prior-art.md). Les implémentations de revendications en vigueur (également listées à cet endroit) ne sont pas acceptées jusqu'à l'expiration de ces revendications.
- Résultats expérimentaux — uniquement via le modèle [experiments/TEMPLATE.md](experiments/TEMPLATE.md) : un protocole daté et reproductible est précisément ce qui constitue notre art antérieur.
- Les décisions d'architecture passent par des ADR dans [docs/decisions/](docs/decisions/).
- Les commentaires de code, docstrings, identifiants et messages de commit sont en anglais uniquement. Les docs sont multilingues (voir ci-dessous) ; les libellés des figures visibles par l'utilisateur se trouvent dans `labels.json`.

## 4. Documentation multilingue : modifier une langue, CI synchronise le reste

L'anglais est la langue principale et possède les chemins canoniques. Chaque autre langue est un arbre miroir sous [translations/](..) avec des noms de fichiers identiques — markdown, le CSV de la BOM et les figures générées inclus ; le texte des figures est piloté par `labels.json`. Vous n'avez **pas** à maintenir les miroirs à la main :

- Modifiez la langue qui vous convient. Lors d'un push, le workflow [Translation sync](../../.github/workflows/translate.yml) traduit les équivalents avec un LLM à poids ouverts (`glm-5.2` sur Ollama Cloud), régénère les figures lorsque la synchronisation met à jour `labels.json`, et commite le résultat avec le marqueur `[translate-sync]`. Tout point de terminaison compatible OpenAI fonctionne — définissez `OPENAI_BASE_URL` et `TRANSLATE_MODEL`.
- Ce qui reste à faire est suivi dans `translations/.sync-state.json`, qui enregistre le contenu principal à partir duquel chaque traduction a été réalisée. Une exécution interrompue par un quota ou un délai d'attente ne perd donc rien : les paires inachevées restent marquées comme obsolètes et sont reprises par le prochain push ou par l'exécution nocturne. Ne modifiez pas ce fichier à la main.
- Si vous avez modifié **plusieurs** langues d'un document vous-même, chaque version que vous avez touchée est conservée telle que vous l'avez écrite ; le bot ne remplit que les langues que vous n'avez pas touchées.
- **`labels.json` fait exception à la règle "modifiez n'importe quelle langue".** Les étiquettes de figure circulent uniquement du principal vers les miroirs. Modifier une étiquette traduite corrige cette langue et s'arrête là ; elle ne revient pas en anglais. Pour changer ce qu'une étiquette *dit*, modifiez la section principale. La raison est l'asymétrie : une modification d'étiquette est presque toujours quelqu'un qui corrige la formulation de la machine, et laisser cela réécrire le principal redéfinirait la source à partir de laquelle les quatorze miroirs sont générés. Les clés que le bot n'a jamais produites se propagent toujours en retour, donc une étiquette rédigée à la main n'est pas bloquée dans une seule langue.
- La traduction automatique est commitée — parcourez le commit du bot et retouchez la formulation s'il manque le ton ; votre correction ne sera pas écrasée (le bot enregistre votre version comme étant l'actuelle).
- Une réponse revenue tronquée ou avec des espaces réservés `labels.json` mutilés est rejetée plutôt que commitée, et la paire est réessayée — donc un vide d'apparence étrange dans un miroir est une paire obsolète, pas une décision.
- **PR externes :** le bot s'exécute sur `master`, donc une PR peut ne changer qu'une seule langue — les miroirs (y compris l'anglais) se mettent à jour automatiquement juste après la fusion. Vous n'avez pas besoin de connaître l'anglais pour contribuer à la documentation.
- **Ajouter une langue :** ajoutez son code et son nom à [i18n.json](../../i18n.json) (par ex. `"fr": "Français"`) et poussez — le pipeline construit tout le miroir `translations/fr/` : chaque document, une section `fr` dans chaque `labels.json`, le jeu de figures, et les sélecteurs de langue partout.
- **Scripts non latins :** le CI installe les familles Noto (`fonts-noto-core`, `fonts-noto-cjk`) et les moteurs de rendu parcourent la pile de polices dans `i18n.json` → `render.fonts`, de sorte que le cyrillique, le Han, le kana et le Hangul sortent correctement. Un moteur de rendu vérifie désormais la couverture des glyphes avant de dessiner et **échoue plutôt que de peindre des boîtes `.notdef`** — cette vérification existe parce que les figures chinoises ont été livrées comme une grille de tofu et que rien dans le CI ne regarde les pixels. Si elle se déclenche, ajoutez la police Noto pour ce script à la pile.
- **Scripts nécessitant une mise en forme contextuelle** — l'arabe et le persan (RTL, formes jointes), le devanagari et le bengali (conjoints) — ne peuvent pas être dessinés correctement par matplotlib, qui n'a pas de moteur de mise en forme : même avec la bonne police, les glyphes sortent non joints et mal ordonnés. Listez ces langues dans `i18n.json` → `render.skip_figures`. Leur prose n'est pas affectée ; leurs documents se contentent de lier vers les figures principales, ce que la réparation de liens dans [tools/translate_sync.py](../../tools/translate_sync.py) pointe automatiquement. `hi` est configuré de cette façon.
- **Garde des scripts :** `SCRIPTS` dans [tools/i18n_render.py](../../tools/i18n_render.py) enregistre quel script les étiquettes de chaque langue doivent contenir. Une réponse qui n'en a aucun — les sections `ja` ont déjà été livrées remplies de russe — est rejetée et réessayée plutôt que commitée. Une langue absente de ce tableau n'a simplement pas de garde, donc en ajouter une à `i18n.json` ne casse jamais ; ajoutez l'entrée pour obtenir la vérification.

## 5. Vérifications que vous pouvez exécuter avant de pousser

python tools/check_repo.py
```

Vérifie ce que le robot de traduction est susceptible de casser et que rien d'autre ne détecterait : chaque lien relatif aboutit, chaque section de `labels.json` correspond à `i18n.json` et comporte les mêmes clés et les mêmes espaces réservés `str.format` que la version principale, chaque document canonique possède un équivalent dans chaque langue, et chaque fichier markdown contient sa barre de langue. CI l'exécute sur les deux workflows ; il ne nécessite aucune dépendance.

Le reste de CI ([ci.yml](../../.github/workflows/ci.yml)) compile les scripts et exécute l'ensemble du pipeline de figures. Pour le reproduire exactement — figures validées comprises — installez la chaîne d'outils épinglée, et non la version libre :

```bash
python -m pip install -r tools/requirements-ci.txt
