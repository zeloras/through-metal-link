# Théorie du canal (le minimum à connaître pour travailler)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · [Português](../../pt/docs/00-theory.md) · [Español](../../es/docs/00-theory.md) · Français · [Italiano](../../it/docs/00-theory.md) · [Polski](../../pl/docs/00-theory.md) · [Türkçe](../../tr/docs/00-theory.md) · [Українська](../../uk/docs/00-theory.md) · [Tiếng Việt](../../vi/docs/00-theory.md) · [中文](../../zh/docs/00-theory.md) · [日本語](../../ja/docs/00-theory.md) · [한국어](../../ko/docs/00-theory.md) · [हिन्दी](../../hi/docs/00-theory.md)

## Principe
Un élément piézo TX pressé/collé contre la paroi y excite une onde longitudinale ; un piézo RX de l'autre côté la reconvertit en électricité. La paroi est un résonateur : aux résonances d'épaisseur (multiples d'une demi-longueur d'onde) la transmission est maximale.

## Chiffres clés
Vitesse du son longitudinale dans l'acier : ~5900 m/s.

| Épaisseur d'acier | Résonance demi-onde |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Longueur d'onde dans l'acier : 148 mm @ 40 kHz ; 5,9 mm @ 1 MHz.

## Deux modes
- **A (40 kHz, transducteurs Langevin).** Une plaque de 3–5 mm ≪ λ — elle se comporte comme une membrane ; la résonance est fixée par la paire de transducteurs, pas par la paroi. Plus simple et plus puissant que le mode B — celui par lequel commencer. Preuve d'existence en labo (pas un objectif garage) : NASA JPL ~24,5 kHz, des centaines de W jusqu'à 1 kW à travers 5 mm de Ti avec du matériel conçu sur mesure.
- **B (0,6–1 MHz, disques).** Résonance d'épaisseur de la paroi elle-même, et une résonance pointue (un décalage de fréquence de ~6 % ⇒ la transmission chute ~10× dans le modèle Fabry–Pérot). La classe de résultats RPI/Moss : des centaines de mW plus des données à des centaines de kbit/s avec un collage et une adaptation de labo. Nécessite un suivi automatique de fréquence.

## Pertes principales
Désaccord de résonance au sein de la paire de transducteurs (les transducteurs Langevin bon marché se dispersent de ±1 kHz), qualité du contact acoustique (époxy > couplant graisse épaisse + serre > pression à sec), désalignement, dérive de résonance avec la température. La réponse à tout cela est la même : faire une cartographie par balayage avant chaque modification du montage.

## Effet sur la paroi et le milieu derrière elle

Version courte : aux niveaux de puissance de la plateforme, la paroi et tout gaz derrière elle sont intacts. Un liquide derrière la paroi affecte surtout *le canal* ; le canal ne commence à affecter *le liquide* qu'aux abords du seuil de cavitation. Les chiffres approximatifs ci-dessous concernent le mode A : 40 kHz, ~1 W/cm² dans de l'acier de 3 mm.

**Paroi — aucune déformation, aucune fatigue, jamais.** Vitesse particulaire v = √(2I/ρc) ≈ 21 mm/s ⇒ déplacement ≈ 80 nm, déformation en onde plane ε = v/c ≈ 3,5·10⁻⁶. Deux estimations équivalentes de contrainte : élastique E·ε ≈ 0,7 MPa (E ≈ 200 GPa) et acoustique p = Z·v ≈ 1,0 MPa (Z_acier ≈ 4,6·10⁷ Pa·s/m). L'acier cède à 250+ MPa et sa limite d'endurance en fatigue est ~200 MPa — encore une marge >200× dans les deux cas, et sous la limite d'endurance l'acier supporte un nombre illimité de cycles. Les parties mécaniquement fragiles sont ailleurs : la céramique piézo (fragile, se dépolarise en cas de surchauffe) et la ligne de colle (l'époxy chauffe et se fatigue en premier) — voir [02-safety](../../../docs/02-safety.md).

**Gaz derrière la paroi — effet nul.** Le désadaptation d'impédance acier→air (~4,6·10⁷ vs ~400 Pa·s/m) transmet une fraction de l'ordre de 10⁻⁵ de la puissance. Pas d'échauffement ni d'agitation mesurable ; l'électronique dans une boîte scellée ne remarque pas le mouvement de paroi à l'échelle nm.

**Liquide derrière la paroi — deux directions :**

- *Liquide → canal (toujours).* L'eau charge la face arrière avec ~1,5 MRayl au lieu de l'air : une partie de la puissance rayonne dans le liquide, le Q chute, le pic de balayage se déplace et s'élargit. Le mode B est le plus touché — le peigne de résonance d'épaisseur est calculé pour des interfaces acier–air et se déplace avec la charge liquide. La règle permanente couvre cela : **re-balayer contre le vrai récipient complet**, ne jamais faire confiance à un balayage pris contre un récipient vide. Avantage secondaire : l'amortissement par le liquide raccourcit le ringing du résonateur (τ), donc l'œil OOK s'ouvre à des débits plus élevés. Les bulles dans le trajet (liquide en fermentation !) diffusent fortement — voir la solution de contournement dans [04-hybrid-channels](../../../docs/04-hybrid-channels.md).
- *Canal → liquide (uniquement à haute puissance).* Pression de crête rayonnée dans l'eau : p ≈ ρc·v ≈ 1,5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0,3 atm. Le seuil de cavitation inertielle à 40 kHz dans l'eau ordinaire (gazeuse) est ~1–2 atm, donc à 1 W/cm² la marge est de 3–10×. Mais p croît comme √puissance, et les ondes stationnaires dans un récipient fermé créent des points chauds locaux — des dizaines de W/cm² en continu dans une cuve remplie de liquide peuvent atteindre le seuil. Le franchir signifie dégazage de CO₂, sonochimie (mauvais goûts dans les produits alimentaires) et érosion de cavitation à long terme de la surface intérieure (exactement comme le nettoyage des nettoyeurs ultrasoniques). Plafond pratique pour la puissance continue dans des parois mouillées par un liquide : **≲1 W/cm²**. Le mode B est exempt : à MHz le seuil est un ordre de grandeur plus élevé et les puissances sont de centaines de mW.

## Bilan de puissance du récepteur (estimation)
LED 20 mW ; ESP32 duty-cyclé 1–5 mW en moyenne ; radio BLE ~150 mW pendant que la radio est active. Tampon : un supercondensateur de 1 F @ 3,3 V stocke E = ½CV² = 5,4 J. Le nombre de transmissions que cela permet dépend du temps d'émission : un court événement d'advertising BLE (~2–5 ms à ~150 mW) ne consomme que ~0,3–0,8 mJ → de l'ordre de **10⁴ paquets** avec un condensateur plein ; une longue connexion / rafale (~100 ms radio active) c'est ~15 mJ → de l'ordre de **10² rafales**. La consommation moyenne doit tout de même rester dans les watts récoltés (la cible d'étape 2 ≥0,5 W dans la charge est le critère ; tant que ce n'est pas mesuré, considérer les bandes mode-A multi-watts sur les graphes du simulateur comme des objectifs, pas des données).
