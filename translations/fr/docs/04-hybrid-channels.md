# Canaux hybrides : barrière → physique → chiffres

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · [Português](../../pt/docs/04-hybrid-channels.md) · [Español](../../es/docs/04-hybrid-channels.md) · Français · [Italiano](../../it/docs/04-hybrid-channels.md) · [Polski](../../pl/docs/04-hybrid-channels.md) · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

Le principe (un corollaire du « paradoxe de pénétration ») : une onde traverse une barrière exactement dans la mesure où elle interagit faiblement avec elle — c'est pourquoi aucun canal universel n'existe. La plateforme ne court pas après un canal unique ; pour chaque barrière, elle choisit la physique à laquelle la barrière est transparente et pour laquelle le récepteur est « gourmand » par résonance.

## Tableau de sélection des canaux

| Barrière | Canal de fonctionnement | Attendu (ordres de grandeur) | Notes |
|---|---|---|---|
| Acier/aluminium 1–60 mm, contact possible | Piézo-acoustique (notre canal principal) | watts ; kbit/s (jusqu'à Mbit/s en mode MHz) | nécessite un contact acoustique (couplant gras/époxy) |
| Métal : sale, peint, chaud, contact indésirable | EMAT (magnétisme → son dans la paroi) | mW ; kbit/s ; gap jusqu'à ~3 mm | parois conductrices uniquement ; données, pas de puissance |
| Paroi ferromagnétique sans piézo du tout | Magnétostriction (une bobine excite l'acier lui-même) | miettes ; bit/s–kbit/s | branche expérimentale, bon marché à tester |
| Double paroi avec vide (thermos, cryostat, dewar) | Magnétiques BF (dizaines–centaines de Hz) | µW–mW ; bit/s | effet de peau : dans l'acier δ≈0,6 mm @1 kHz — baisser la fréquence |
| Non-métal : verre, plastique, céramique | Piézo-acoustique (plus facile que le métal) | watts ; kbit/s | + la RF simple passe souvent aussi — vérifier ça d'abord |
| Paroi avec couche de caoutchouc/mousse, composite | Honnêtement : quasi impasse | — | l'absorbant mange tout ; la solution de contournement est un point sans revêtement |
| Liquide derrière la paroi (réservoir plein) | Piézo-acoustique, dégradé | puissance − quelques dB ; résonance plus courte | le chargement liquide déplace/amortit la résonance — refaire le balayage contre le récipient plein ; maintenir l'intensité continue ≲1 W/cm² pour rester sous le seuil de cavitation ([théorie](00-theory.md#effect-on-the-wall-and-the-media-behind-it)) |
| Liquide bullant dans le chemin acoustique | Solution de contournement architecturale | — | monter le récepteur sur la paroi, garder le liquide hors du chemin |

## Architecture du nœud hybride

- Couche puissance : paire piézo à la résonance (étapes 1–4).
- Couche données sans contact : une tête EMAT en « pistolet scanner » détachable (étape ~6).
- Couche de secours : bobines BF pour les sandwichs à vide (quand la tâche l'exige).
- Le protocole de découverte (docs/03) passe de « balayage en fréquence » à « balayage en physique » : ping piézo → ping EMAT → ping BF ; le nœud choisit le canal qui passe de lui-même et signale quelle barrière il voit.

## Exemples d'applications par canal

1. **Packs de batteries scellés (VE/stockage) :** capteur T/gaz à l'intérieur d'un boîtier moulé ; puissance+données via une paire piézo à travers 2–3 mm d'aluminium. Le marché explose, et une pénétration dans un boîtier de batterie = un enfer de certification.
2. **Cryostat/dewar :** un enregistreur de température à l'intérieur, envoyant un paquet de bits une fois par minute via les magnétiques BF à travers la chemise à vide. Fondamentalement hors de portée pour l'acoustique — c'est là que l'hybride est irremplaçable.
3. **Pipeline/autoclave sous pression :** un scanner EMAT pressé contre un tuyau chaud et peint sans aucune préparation de surface — lit une balise résonante passive depuis l'intérieur.
4. **Cuves de fermentation (bière/vin, acier inoxydable) :** un capteur de densité/T à l'intérieur de la cuve sans la moindre pénétration — les codes sanitaires adorent l'absence de trous.
5. **Conteneur maritime/coffre-fort :** « le cargo est-il vivant » — une paire piézo à travers l'acier ondulé, interrogée avec un scanner portatif.

## Limites qu'aucune couche ne peut résoudre
Puissance — piézo par contact uniquement (EMAT et magnétiques BF sont plus faibles de plusieurs ordres de grandeur). Les parois composites/garnies de caoutchouc sont hors du champ de la plateforme. La vitesse du canal BF est de quelques bits par seconde — c'est de la télémétrie, pas du streaming.
