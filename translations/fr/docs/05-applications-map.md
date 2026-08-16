# Cartographie des applications : qui a besoin de cette pile technologique, et pourquoi

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · [Português](../../pt/docs/05-applications-map.md) · [Español](../../es/docs/05-applications-map.md) · Français · [Italiano](../../it/docs/05-applications-map.md) · [Polski](../../pl/docs/05-applications-map.md) · [Türkçe](../../tr/docs/05-applications-map.md) · [Українська](../../uk/docs/05-applications-map.md) · [Tiếng Việt](../../vi/docs/05-applications-map.md) · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

La pile plateforme : un canal actif d'alimentation et de données à travers des parois aveugles — piézo-acoustique / EMAT / magnétique BF. Ci-dessous : où c'est nécessaire dans le monde réel, qui est déjà présent, et ce qu'il nous reste à faire.

## 1. Packs batterie scellés (VE, stockage d'énergie domestique/industriel)
- Douleur : détection précoce de l'emballement thermique — des gaz (CO₂, H₂, vapeurs d'électrolyte) apparaissent à l'intérieur du pack des minutes à des heures avant un incendie ; une pénétration de capteur dans l'enceinte = perte d'étanchéité et de certification.
- Notre pile : un nœud gaz/température à l'intérieur du pack, alimentation et télémétrie via une paire piézo à travers 2–3 mm d'aluminium. Zéro trou.
- Qui est déjà là : Liminal Insights — *diagnostics acoustiques par l'extérieur* (brevets sur les méthodes d'analyse, pas sur le canal). Personne ne vend de nœuds *à l'intérieur* du pack.
- Maturité du créneau : le marché croît de façon explosive, l'étagère est vide. Pour la plateforme — application vitrine n°1.

## 2. Équipement de laboratoire : chambres à vide, cryostats, boîtes à gants
- Douleur : chaque passage électrique dans une chambre à vide est une bride qui vaut des centaines de dollars et une source de fuites ; dans un cryostat, un câble = fuite thermique.
- Notre pile : un capteur à l'intérieur de la chambre, alimentation/données par le son à travers la paroi en acier ; pour les sandwichs sous vide des dewars — magnétique BF (un bit/s suffit largement pour un enregistreur de température).
- Qui est déjà là : personne en sans-fil à travers la paroi ; les labos vivent sur des brides de passage.
- Maturité : le créneau de départ idéal pour l'open source — les labos sont exactement le public pour le matériel ouvert (la voie TinyLev) : ils achètent sans certifications et vous citent dans des articles.

## 3. Production agroalimentaire : cuves de fermentation, autoclaves (bière, vin, produits laitiers)
- Douleur : les normes sanitaires détestent les pénétrations (lavage CIP, zones mortes) ; on veut connaître la densité/T/pression à l'intérieur de la cuve en permanence.
- Notre pile : un nœud sur la paroi intérieure d'une cuve en inox, interrogé depuis l'extérieur avec un scanner portatif ou une paire fixe.
- Qui est déjà là : capteurs classiques sur piquage ; pas de solution sans-fil à travers la paroi.
- Maturité : littéralement à portée d'un test de garage (n'importe quelle microbrasserie est un terrain d'essai à distance de marche).
- Caveat physique : une cuve pleine charge la paroi — refaire le balayage contre le récipient plein, et garder une puissance continue ≲1 W/cm² ; au-delà, cavitation dans le produit (dégazage CO₂, flés défauts, érosion à long terme de la paroi) — [théorie](00-theory.md#effet-sur-la-paroi-et-le-milieu-derrière-elle).

## 4. Pipelines, vessels sous pression, CND industriel
- Douleur : surveiller la corrosion/paramètres à l'intérieur sans arrêt ni pénétration ; les surfaces sont chaudes, peintes, sales.
- Notre pile : un « pistolet scanner » EMAT — on l'appuie contre un tuyau sans aucune préparation de surface, on lit une balise résonante passive depuis l'intérieur.
- Qui est déjà là : débitmètres ultrasonores à collier et jauges d'épaisseur (un marché mature), mais pas de balises interactives à l'intérieur.
- Maturité : mi-range ; nécessite la branche EMAT (étape ~6).

## 5. Pétrole & gaz / downhole, et nucléaire
- Qui est déjà là : Metrol, Acoustic Data, Baker Hughes (downhole, 30 ans, modèle de service) ; R&D DOE/UNT/Westinghouse (conteneurs nucléaires).
- Verdict honnête : occupé et fortement régulé — on n'y va pas, mais leur seule existence = preuve que cette physique se vend pour de l'argent sérieux. À utiliser comme référence dans le README.

## 6. Logistique maritime et structures sous-marines
- Douleur : « la cargaison est-elle vivante » dans un conteneur scellé ; données depuis la face intérieure de la coque d'un navire.
- Qui est déjà là : CSignum (EM BF à travers l'eau/les cloisons) — le seul voisin direct en philosophie hybride.
- Maturité : long terme ; pour nous, pour l'instant, seulement une direction de réflexion.

## 7. Installations à poussière combustible (étudié, pas d'entrée)
- Le pitch : un nœud de mesure de charge scellé à l'intérieur d'une ligne de transport ou d'un silo — pas de presse-étoupe, pas de chemin d'allumage — lisant l'électricité statique que le transport pneumatique génère (la charge spécifique la plus élevée de toutes les opérations sur poudres, 10⁻¹–10³ µC/kg).
- Qui est déjà là : sondes tribo certifiées en conduit sur ports standard (Sintrol S201 Ex, ENVEA DM210, Dwyer PMT2 ≈ 3 k$) et, pour les tuyaux, un tronçon de ligne isolé avec un électromètre à la terre — qui lit la charge sans rien à l'intérieur du tuyau.
- Verdict honnête : pas notre créneau. Le statique représente ~8,5 % des ignitions d'explosion de poussière (statistiques BIA), et IEC TS 60079-32-1 / NFPA 77 / NFPA 660 le contrôlent par des mesures de conception — mise à la terre, humidité, vitesse de transport, inertage — sans niveau de charge à surveiller, donc une mesure n'est pas une couche de protection que quiconque doit acheter. L'intérieur est zone 20, où ce projet ne certifiera rien ([sécurité](02-safety.md)) ; et un anneau derrière une paroi en acier ne voit rien, donc le capteur a besoin de son propre port dans le flux — la seule chose que le pitch promettait d'éviter.

## Priorités (quoi faire, dans quel ordre)
1. **Maintenant :** étapes 1–4 de la plateforme sur le scénario vitrine « chambre de labo / boîte soudée fermée » (créneau n°2 — le plus ouvert à l'open source).
2. **Ensuite :** une démo sur un objet réel du créneau n°3 (une cuve de brasserie) — bon marché, photogénique, un vrai utilisateur.
3. **Mi-range :** le scénario batterie (créneau n°1) comme cas phare pour publication ; la branche EMAT pour le créneau n°4.

*La vision passive (radiographie à muons) a été scindée dans un projet séparé — voir muon-lab dans la base de connaissances.*
