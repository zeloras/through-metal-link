# Licence et protection par brevets

> [English (primary)](../../LICENSES.md) · [Русский](../ru/LICENSES.md) · [Deutsch](../de/LICENSES.md) · [Português](../pt/LICENSES.md) · [Español](../es/LICENSES.md) · Français · [Italiano](../it/LICENSES.md) · [Polski](../pl/LICENSES.md) · [Türkçe](../tr/LICENSES.md) · [Українська](../uk/LICENSES.md) · [Tiếng Việt](../vi/LICENSES.md) · [中文](../zh/LICENSES.md) · [日本語](../ja/LICENSES.md) · [한국어](../ko/LICENSES.md) · [हिन्दी](../hi/LICENSES.md)

L'objectif de ce dispositif : le projet est entièrement ouvert, n'importe qui peut le forker et construire dessus (y compris commercialement), tout en réduisant le risque de litige sur les brevets au strict minimum atteignable par les moyens juridiques et procéduraux.

## Le dispositif (trois couches ; textes complets dans [LICENSES/](../../LICENSES))

| Domaine | Licence | Texte | Dispositions sur les brevets |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](../../LICENSES/Apache-2.0.txt) | §3 : chaque contributeur accorde automatiquement une licence de brevet pour sa contribution ; engagez une action en contrefaçon de brevet et vous perdez la licence de **brevet** (représailles ; la licence de droit d'auteur au §2 est irrévocable et survit à l'action) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](../../LICENSES/CERN-OHL-W-2.0.txt) | §7.1 : une licence de brevet (Fabriquer / faire Fabriquer / utiliser / vendre / importer…) de la part de chaque concédant — mais uniquement pour les revendications nécessairement contrefaites par le Code Source Couvert donné ; §7.2 : une action en brevet (y compris une tentative d'invalider le brevet d'un tiers) met fin à **tous** les droits accordés par la licence |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](../../LICENSES/CC-BY-4.0.txt) | n'accorde **aucun** droit de brevet (§2(b)(2)) — le vide est comblé par l'octroi explicite de licence de brevet dans [CONTRIBUTING.md](../../CONTRIBUTING.md) |
| tout le reste (`README.md` à la racine, `QUICKSTART.md`, ce fichier, `data/`, etc.) | CC-BY-4.0 | — | solution de repli : aucun fichier du dépôt n'est laissé « tous droits réservés » |

Les fichiers de code portent des en-têtes SPDX (Apache-2.0) ; la carte de couverture lisible par machine est [REUSE.toml](../../REUSE.toml). La ligne de copyright se trouve dans [NOTICE](../../NOTICE) ; le fichier [LICENSE](../../LICENSE) à la racine est un pointeur vers ce dispositif.

**Pourquoi CERN-OHL-W, et non S ou P.** W est le compromis : le design et ses modifications doivent rester ouverts à toute distribution, mais le produit dans lequel le design est intégré peut être commercial et propriétaire — ce qui laisse ouvertes les niches de docs/05 (laboratoires, brasseries, packs de batteries). S (copyleft fort) fermerait la porte à l'intégration ; P (permissif) permettrait des forks fermés. Le resserrement vers S est intégré à la licence elle-même : §8.3 permet à quiconque de traiter le matériel sous licence W comme s'il était sous licence S (à condition que la condition des Composants Disponibles soit remplie) — sans autorisation requise. L'assouplissement (vers P ou une autre licence), en revanche, n'est possible que tant que tout le matériel appartient à un seul auteur ; après la première contribution externe — uniquement avec le consentement de chaque contributeur.

**Nom du projet.** « through-metal-link » n'est pas une marque déposée ; les licences elles-mêmes n'accordent aucun droit sur le nom (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Faire référence au projet de manière factuelle (« based on through-metal-link ») est libre pour tout le monde ; les forks avec des modifications incompatibles sont invités à publier sous leur propre nom.

## Ce contre quoi cela protège — et ce contre quoi cela ne protège pas (honnêtement)

**Cela protège contre :**
1. **Les actions en justice de la part de contributeurs.** Quiconque a contribué a automatiquement concédé ses droits de brevet sur cette contribution (Apache §3, CERN-OHL §7.1, et CONTRIBUTING pour les docs). Une action coûte cher au demandeur : sous Apache-2.0, il perd les licences de brevet sur le code ; sous CERN-OHL-W, il perd tous les droits sur la couche matérielle, purement et simplement (§7.2 — déclenché même par une tentative de contester le brevet d'un tiers).
2. **La privatisation des forks matériels.** CERN-OHL-W oblige quiconque distribue (Transmission d'un produit ou de sources) à publier ses modifications du design — les améliorations reviennent dans la couche ouverte et deviennent elles-mêmes antériorité. (Un fork resté dans un tiroir, jamais transmis à des tiers, n'a aucune obligation de publication — comme sous tout copyleft.)
3. **Les brevets *futurs* d'autrui.** Tout ce qui est publié avec une date détruit la nouveauté pour les demandes ultérieures : pour une solution décrite ici avant leur date de dépôt, un brevet valide ne peut plus être accordé. Contre les demandes déposées *avant* notre publication, cela ne fonctionne pas — pour celles-là, le seul bouclier est la couche de brevets expirés (voir ci-dessous).

**Cela ne protège pas contre :**
- **Les brevets de tiers qui existent déjà.** Aucune licence ne peut faire cela. Ce qui fonctionne contre eux, c'est la discipline d'ingénierie de docs/01-prior-art.md : ne construire qu'à partir de la couche expirée (domaine public), ne pas implémenter les revendications en vigueur listées là (RPI, Drexel, et les familles Navy/ABB/Ultrapower ajoutées en 2026-08 — notez qu'elles ne sont pas toutes américaines et n'expirent pas toutes vers 2032), et remonter chaque décision de design à une source libre. Ce n'est pas une garantie, mais c'est exactement la pratique qui rend une action en justice vaine.
- Un fork destiné à la production commerciale fait sa propre analyse FTO (freedom to operate) pour sa propre juridiction et son propre design — le dépôt ne fait aucune déclaration sur les brevets (clauses de non-responsabilité dans les trois licences).

## Protocole de publication défensive (à continuer d'exécuter au fur et à mesure que les jalons sont publiés)

Chaque résultat publié est une antériorité datée qui bloque toutes les demandes ultérieures de tiers pour la même solution :

1. Conserver intact tout l'historique git public (commits = horodatages).
2. Snapshot vers **Zenodo** → DOI : une archive indépendante avec une date juridiquement pertinente, citable dans des articles.
3. L'épingler dans **Software Heritage** (archive.softwareheritage.org — un miroir perpétuel).
4. Chaque expérience terminée `experiments/NNN` — avec une date, des chiffres et des graphiques : c'est la publication d'une solution technique spécifique.
5. Les jalons majeurs (premiers watts, premier nœud) — un compte-rendu publié dans le monde (Hackaday.io / arXiv / blog) : plus la diffusion est large, plus le statut d'antériorité est solide.

## Pour les contributeurs

Les règles se trouvent dans [CONTRIBUTING.md](../../CONTRIBUTING.md) : DCO sign-off, inbound=outbound, un octroi explicite de licence de brevet sur chaque contribution quel que soit le répertoire, traçabilité des décisions de design vers l'antériorité libre.

Le dépôt est déjà public. Continuez le protocole ci-dessus à chaque jalon (snapshot Zenodo, épingle Software Heritage, comptes-rendus d'expériences) pour que l'antériorité datée reste solide au fur et à mesure que les résultats arrivent.
