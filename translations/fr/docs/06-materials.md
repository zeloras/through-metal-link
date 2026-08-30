# Matériaux de paroi au-delà de l'acier : quelles parois transportent puissance et données

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · [Deutsch](../../de/docs/06-materials.md) · [Português](../../pt/docs/06-materials.md) · [Español](../../es/docs/06-materials.md) · Français · [Italiano](../../it/docs/06-materials.md) · [Polski](../../pl/docs/06-materials.md) · [Türkçe](../../tr/docs/06-materials.md) · [Українська](../../uk/docs/06-materials.md) · [Tiếng Việt](../../vi/docs/06-materials.md) · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

Le reste de ce dépôt suppose de l'acier. Cette page pose la question plus simple et plus large : **pour quels matériaux de paroi le canal à deux transducteurs fonctionne-t-il du tout**, et dans quel mode ? Il s'agit d'une étude par simulation (style `--mock`, sans données de laboratoire — une intuition sur ce qui mérite une expérience matérielle), construite à partir du même modèle semi-empirique que [channel_sim](../../../software/simulator/channel_sim.py) et étendue avec l'absorption volumique.

Génération : `python3 software/simulator/material_map.py` (nécessite numpy + matplotlib). Modèle et hypothèses : [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## Le modèle en une minute

Trois grandeurs décident si une paroi est utilisable, et pour quelle puissance :

1. **Contraste d'impédance et phase** — le modèle de lame Fabry–Perot sans pertes, identique à [channel_sim](../../../software/simulator/channel_sim.py) :
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_wall / Z_couplant, couplant Z = 1.5 MRayl (graisse).
   À une résonance demi-onde (f = c/2d) une lame symétrique sans pertes est totalement transparente *quel que soit r* ; le contraste r fixe la **largeur** des dents du peigne (tolérance à l'erreur de fréquence), la vitesse du son c fixe leur espacement (Δf = c/2d).
2. **Absorption volumique**, invisible au modèle sans pertes et déterminante pour les plastiques, le béton et le caoutchouc :
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, unidirectionnel, longitudinal],
   où α₁ₘₕᶻ est la valeur à 1 MHz.
   γ ≈ 1 = perte visqueuse/relaxation ; γ > 2 = diffusion par les inhomogénéités (granulats de béton).
3. **La dose que la paroi reprend** — voir la section [ci-dessous](#la-dose-ce-que-londe-fait-à-la-paroi-fréquence-par-fréquence) : contrainte σ = √(2·I·Z), qui *ne dépend pas* de la fréquence, et auto-échauffement ΔT ∝ α(f)·I, qui en dépend.

**Hypothèses, énoncées là où le code les énonce :** propriétés typiques de manuel (onde longitudinale, ~20 °C) ; les stocks réels varient — grain, charges, granulats, cure. Tout ce qui suit est un classement, pas une fiche technique.

| Paroi | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | peigne Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | note |
|---|---|---|---|---|---|---|---|---|
| acier | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | structurel à grain fin |
| aluminium | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | classe 6061 |
| titane | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| cuivre | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | dense, Z très élevé |
| verre borosilicaté | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | très faible perte |
| céramique alumine | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | son rapide, faible perte |
| PMMA (acrylique) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | transparent, limité par l'absorption au MHz |
| PVC (rigide) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | plus lossy que le PMMA |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | mou, lossy |
| béton | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | diffusion par granulats domine ; varie d'ordres de grandeur |
| caoutchouc (chargé) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | la vraie impasse |

## Les tracés

**Mode B (MHz) — le peigne d'épaisseur par matériau.** À gauche : métaux structurels ; à droite : non-métaux. Toutes parois 5 mm, couplage par graisse. Les pics du modèle sans pertes atteignent T = 1 aux résonances exactes ; les pics réels sont plus bas à cause des pertes de contact, et l'absorption plafonne les matériaux lossy d'emblée :

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**La carte des matériaux** — les deux axes qui décident tout : impédance (difficulté de couplage/contact) vs absorption à 1 MHz (viabilité au MHz). Haut-Z + faible-α est le coin de classe puissance ; bas-Z + haut-α est « 40 kHz encore ouvert, MHz mort » ; le coin caoutchouc est une impasse à toutes les fréquences que nous ciblons :

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Proxy de couplage Mode A (40 kHz)** — le même modèle de transmission évalué à 40 kHz à travers une paroi de 3 mm, normalisé à l'acier. *Un classement, pas des watts :* la paire Langevin résonante multiplie chaque barre à peu près également et le modèle n'a pas de chargement de transducteur interne ; ce multiplicateur relève de l'étape 2 ([experiments/002](../experiments/002-watts-3mm-steel/README.md)) :

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## Ce que le balayage dit

- **À 40 kHz, les parois à faible Z (plastiques, revêtement caoutchouc) se couplent *plus facilement* que l'acier** — à travers la graisse elles sont presque adaptées en impédance, donc le peigne est large et la transmission par passe est élevée. Ce qui tue les plastiques aux fréquences plus élevées, c'est l'**absorption volumique**, pas le contact ou l'impédance. L'échelle des matériaux à 40 kHz est donc inversée par rapport à l'intuition : HDPE/PMMA/PVC > verre/béton > aluminium > alumine > titane > acier > cuivre — avec la réserve forte que le nombre 40 kHz des caoutchoucs extrapole α linéairement depuis 1 MHz, ce que la viscoélasticité ne garantit pas.
- **Le mode B sépare nettement les matériaux.** Métaux, verre et alumine acceptent le MHz avec une absorption négligeable (α ≤ 0.1 dB/cm) ; le peigne est *étroit* pour les parois à haut Z (acier, alumine — nécessite un suivi de fréquence, la leçon ~6 % ⇒ ~10× de [00-theory](00-theory.md)) et *large* pour verre/PMMA (tolérants, mais le PMMA paie ~1.3 dB unidirectionnel à 1 MHz sur 5 mm — classe mW seulement).
- **Le béton est un matériau à 40 kHz, pas à MHz.** La diffusion par granulats (λ à 1 MHz ≈ 3.5 mm ≈ taille de granulat) fait monter γ jusqu'à ~2.5 et tue le MHz ; la pratique de vitesse de pulsation ultrasonore (40–80 kHz à travers des trajets ≥1 m) est exactement le mode A.
- **La niche batterie ([05](05-applications-map.md)) est acoustiquement favorable :** une paroi en aluminium de 2–3 mm a un proxy de couplage ~3× celui de l'acier et une absorption négligeable — le cas amiral est aussi le cas facile.
- **L'échelle de fréquences à anticiper en mode B** (paroi 5 mm, premier peigne) : PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, cuivre ≈ 480, acier ≈ 590, titane ≈ 610, aluminium ≈ 630, verre ≈ 560, alumine ≈ 990. Paroi plus mince ⇒ proportionnellement plus haut.

## La dose : ce que l'onde fait à la paroi, fréquence par fréquence

La transmission répond à « combien passe » ; cette section répond à la question inverse — **quelle part de l'onde reste dans la paroi, et est-ce que ça la blesse ?** Le dommage de l'onde-dans-la-paroi a exactement deux visages :

- **Contrainte** σ = √(2·I·Z) — quantité de mouvement d'onde plane ; *indépendante de la fréquence*. Comparer à la limite de fatigue oligocyclique (métaux), à la résistance en flexion/traction (céramiques, verre, béton, caoutchouc).
- **Auto-échauffement** ΔT = α(f)·I·d²/(8k), régime stationnaire, les deux faces refroidies — *dépend de la fréquence* via α(f), et c'est là que la fréquence mord : tout matériau isolant a un genou au-delà duquel chaque octave supplémentaire de fréquence multiplie la chaleur déposée.

À 1 W/cm² (déjà au-delà de ce que ce projet cible : l'objectif étape 2 de 0.5–5 W répartis sur une face de transducteur de ~19 cm² est 0.03–0.26 W/cm²) :

| Paroi | σ @1 W/cm², MPa | limite σ_e, MPa | marge de contrainte | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | plafond @40 kHz, W/cm² | plafond @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| acier | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| aluminium | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| titane | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| cuivre | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| verre borosilicaté | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| céramique alumine | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (acrylique) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (rigide) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| béton | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| caoutchouc (chargé) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

« Plafond » = intensité continue à laquelle la paroi reste dans 20 % de sa limite de fatigue/résistance et sous +20 K d'auto-échauffement (régime stationnaire, les deux faces maintenues à l'ambiance). Les fonctionnement à cycle de service chauffent moins ; une paroi ancrée sur une seule face — le cas habituel, air d'un côté — chauffe jusqu'à 4× plus à la face libre. Ces chiffres sont une première estimation, pas une garantie de conception. Une convention à signaler : les valeurs α sont en dB d'intensité (10·log₁₀, la convention de dosimétrie — une chute de 3 dB divise I par deux) ; la littérature NDT en pulse-echo qui cite des dB d'amplitude (20·log₁₀) décrit le MÊME α avec des nombres deux fois plus grands — vérifiez quelle convention une source utilise avant de copier ses nombres dans ce tableau.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

Ce que le balayage de dose dit :

- **Le verdict sur l'acier de [00-theory](00-theory.md) tient et se généralise** : chaque métal structurel transporte 1 W/cm² avec des marges de 65–680× en contrainte et des micro-kelvins d'auto-échauffement. Les métaux sont insensibles à la fréquence en termes de dommage — leur perte est trop faible pour chauffer à toute puissance que nous savons coupler.
- **Le dommage fréquentiel sur les polymères est thermique, pas mécanique.** La marge de contrainte du PMMA est un confortable 60× même à 1 W/cm², mais le genou thermique se situe juste autour de 1 MHz : bénin (~0.2 K) à 40 kHz, +9.5 K à 1 MHz, +65 K à 5 MHz — territoire de ramollissement à quelques W/cm². Le PVC franchit la ligne +10 K déjà à ~0.35 W/cm² @ 1 MHz ; le caoutchouc absorbe ~288 K par W·cm⁻² à 1 MHz (et ~12 K même à 40 kHz) — l'échauffement hystérétique est *la* raison pour laquelle les parois revêtues d'élastomère meurent, pas le peigne. Le HDPE partage la différence et se souvient de son point de fusion : +215 K par W·cm⁻² à 5 MHz.
- **La marge étroite du béton est en traction, pas en thermique** : 0.40 MPa de contrainte d'onde contre une résistance statique en traction de ~2.5 MPa (fatigue encore plus basse) ne laisse qu'une marge de ~6× à 1 W/cm². Le régime 40–80 kHz reste correct à la densité de puissance du projet ; les faisceaux concentrés de plusieurs W/cm² dans le béton doivent être évités, le MHz doublement (la diffusion chauffe les interfaces de granulats).
- **Conclusion pour la feuille de route :** aux densités de puissance du mode A (≤0.3 W/cm²) aucun solide du tableau n'est menacé — marges de contrainte ≥11× (la plus serrée est la fatigue en traction du béton à 11× ; tout le reste ≥15×) et échauffement ≤0.2 K pour chaque solide d'ingénierie (le caoutchouc, l'exception que personne ne cible, ~3.5 K). La carte de dommage justifie le plan du projet d'escalader la puissance : les premières vraies limites matériaux apparaissent *au-dessus* des cibles étape 2, d'abord dans les liquides (cavitation, la règle ≤1 W/cm² de [00-theory](00-theory.md)), puis dans la fatigue en traction du béton, puis dans les polymères au MHz. Les pièces qui nécessitent vraiment une surveillance à haute puissance restent la céramique piézo et la ligne de collage — [02-safety](02-safety.md) — pas la paroi.

## Verdict par matériau

| Paroi | Mode A — puissance 40 kHz | Mode B — puissance/données MHz | Verdict |
|---|---|---|---|
| acier | ✓✓ référence | ✓ peigne étroit — suivre la fréquence | la référence |
| aluminium | ✓✓ (proxy ~3× acier) | ✓ peigne assez étroit | meilleure paroi structurelle (batteries !) |
| titane | ✓✓ | ✓ assez étroit, faible perte | niches corrosives/chaudes, drones, coques |
| cuivre | ✓ (couplage le plus difficile des métaux) | ✓ | niche : barres omnibus scellées/cellules électrochimiques |
| verre borosilicaté | ✓✓ | ✓ peigne le plus large — le plus indulgent | fenêtres de labo, hublots |
| céramique alumine | ✓✓ | ✓ peignes les plus rapides (990 kHz @ 5 mm), faible perte | parois de procédé chaud/isolant |
| PMMA | ✓ large bande | ⚠ classe mW ≤ ~0.5 MHz seulement | cuves, enceintes ; pas une paroi de puissance au MHz |
| PVC / HDPE | ✓ parois minces | ✗ absorption | enceintes de bas grade, nœuds à données légères |
| béton | ✓ 40–80 kHz (pratique UPV) | ✗ diffusion | fondations, tuyaux — mode A seulement |
| caoutchouc (chargé) | ⚠ extrapolation de modèle non validée | ✗ | empiriquement l'impasse — [04](04-hybrid-channels.md) |

Une paroi plastique à faible Z offre plus de marge pour des liens en mode A *tolérants au désalignement* mais délivre moins de marge de puissance absolue face à l'absorption une fois qu'on dépasse ~200 kHz ; mesurez avant de promettre quoi que ce soit.

## Béton avec armature — le cas multicouche

Le vrai béton n'est jamais nu : les nattes d'armature se trouvent à une profondeur d'enrobage, et le modèle 1D à une seule lame ci-dessus ne peut pas les voir. `chart_rebar` / `rebar_table` étendent le modèle aux empilements généraux ([`stack_transmission`](../../../software/simulator/material_map.py), récursion multicouche exacte avec absorption par couche, protégée dans l'auto-test). Géométrie modélisée : une paroi structurelle de 150 mm, une natte d'acier d'épaisseur planaire équivalente Ø16 mm à 40 mm d'enrobage ; le modèle *planaire* est le pire cas — une vraie barre n'ombrage que la partie du faisceau qu'elle intersecte, donc considérez ces valeurs comme des creux enveloppes, pas des prédictions :

| Empilement (béton 150 mm) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| béton nu 150 mm | 0.135 | 0.133 | 8.9e-09 |
| armature Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| deux nattes Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

Ce que le modèle d'empilement dit :

- **Une natte planaire sous le faisceau coûte ×10 à exactement 40 kHz** (interférence de bande stop due à la couche d'acier), mais le creux est étroit : à 100 kHz le même empilement ne perd que ×2. La lecture pratique pour la niche pipeline/autoclave : *un balayage de fréquence autour de 40–120 kHz, pas une fréquence fixe*, est ce qui fait passer un lien en mode A au-delà de l'armature — et les creux se déplacent avec la profondeur d'enrobage, donc un balayage identifie aussi la géométrie (la base d'une estimation de profondeur d'armature).
- **Une seconde natte (un maillage) est presque un tueur de paroi dans ce pire cas** (×45 en bas et plat en bande large près de 40–100 kHz) : une armature dense dans le trajet est l'indicateur honnête « choisissez un autre endroit sur la paroi », pas un problème de traitement de signal.
- **Le mode B à travers le béton structurel est mort avec ou sans armature** (niveau 1e-8 à 1 MHz : 5 dB/cm × 15 cm). L'armature n'entre même pas dans l'histoire au MHz.
- Réserves, par ordre d'importance : hypothèse de couche planaire (pire cas — une barre Ø16 bloque bien moins de la moitié de la section d'un faisceau de 40–50 mm), onde parallèle à l'axe de l'armature supposée, et propagation 1D (pas de diffraction autour de la barre). La bonne expérience matérielle est un banc de balayage sur une vraie dalle : cartographier T(x, y) à 40/80/120 kHz sur une grille d'armature et ajuster les positions de creux du modèle planaire au pas de la grille.

## Ce qu'un suivi matériel devrait mesurer

Avant de faire confiance à une plaque spécifique : méthode à deux épaisseurs par matériau (deux plaques de d et 2d au même contact) pour extraire le vrai α(f) et c — ce seul jeu de données remplace chaque ligne du tableau ci-dessus. Des passes bonus naturelles dans les protocoles existants : répéter le balayage de l'expérience [001](../experiments/001-sweep-map-3mm-steel/README.md) sur une plaque de PMMA de 5 mm, une plaque de borosilicate ou d'alumine 99 %, et un bloc de béton de grade connu ; s'attendre à un pic *plus bas mais plus large* pour les plastiques, un peigne étroit pour les céramiques, et un contact sensible à la température partout. Pendant l'essai de puissance de l'expérience [002](../experiments/002-watts-3mm-steel/README.md), fixer un thermomètre IR (ou un thermocouple fin) sur la face arrière de chaque type de paroi — le ΔT mesuré à entrée connue est le seul nombre qui valide ou tue la colonne d'échauffement du tableau de dose. Rien dans cette page n'est mesuré — c'est la carte de ce qu'il faut mesurer en premier.
