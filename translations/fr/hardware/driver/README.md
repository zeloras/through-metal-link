# Driver (étage 2) : demi-pont IR2110

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · Français · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Schéma :** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) (généré par [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

La chaîne : Pi (SPI) → AD9833 **en mode onde carrée** (bit OPBITEN : MSB routé vers la sortie, swing rail-to-rail — pas besoin de comparateur séparé) → **74HC14 + RC + 1N4148** mise en forme (HIN/LIN complémentaires avec ~1 µs de temps mort) → IR2110 → 2×IRF540 (demi-pont) → condensateur de blocage DC 1 µF → transformateur d'adaptation (ferrite, ~1:3..1:5, à régler sur le banc) → transducteur Langevin TX.

La sortie sinusoïdale de l'AD9833 (~0,6 Vpp) ne convient pas à la logique de l'IR2110 — si pour une raison quelconque vous avez absolument besoin d'une sortie sinusoïdale du DDS, insérez un comparateur entre les deux (par ex. un LM393, pas dans la BOM).

Alimentation de l'étage de puissance : alimentation de laboratoire 12–24 V avec limitation de courant (**démarrez à 0,2 A**).

Note : le balayage de l'étage 1 pilote le piézo directement avec la sinusoïdale faible du DDS (~0,6 Vpp, voir `sweep_map.py`) — **ce driver n'entre dans la chaîne qu'à l'étage 2 (watts)**. N'attendez pas ≥0,5 W du montage étage 1 avec DDS seul.

Remarques :
- Le transducteur Langevin est une charge capacitive (généralement quelques nF). Une inductance en série ou un transformateur d'adaptation est obligatoire ; sans cela, les MOSFET dissipent le courant réactif et cuisent.
- **Transformateur d'adaptation (le point de défaillance habituel).** Commencez avec un petit tore en ferrite (par ex. FT50-43 / similaire), primaire quelques spires, secondaire ~3–5× plus, condensateur film de blocage DC 1 µF en série sur le primaire. Réglez pour un courant d'alimentation minimal *à la résonance de l'étage 1* avec le TX **fixé sur la plaque** et le RX en charge. Le rapport des spires et la fuite sont empiriques — le schéma les marque `*` pour une bonne raison. Notez le nombre de spires final dans le journal d'expérience.
- **Temps mort** : l'IR2110 ne le génère pas lui-même. L'option à composants discrets — RC+1N4148 sur les entrées du 74HC14 (retarde uniquement les fronts montants, ~1 µs ; avec une période de 25 µs à 40 kHz, cela fait <5 % de perte). L'option facile — un module EGS002, tout est intégré.
- **Logique 3,3 V** : alimentez le VDD de l'IR2110 avec le même 3,3 V que l'AD9833 et le 74HC14 — à VDD=5 V, le seuil VIH est ≈ 3,1 V et une onde carrée 3,3 V passe tout juste (la datasheet autorise VDD jusqu'à 3,3 V).
- **Découplage obligatoire** : 100 nF sur VDD et VCC (VCC — plus 47 µF), et sur le rail d'alimentation 470–1000 µF + 100 nF céramique juste au niveau des pattes du demi-pont — sans cela, un demi-pont sur fils de breadboard capte ses propres pics de commutation. Gardez les fils de boucle de puissance courts ; si le nœud de commutation oscille trop, passez de la breadboard à un montage dead-bug sur cuivre / protoboard avec plan de masse avant d'augmenter le courant.
- **Séquence de première mise sous tension** (alignée avec [docs/02-safety.md](../../docs/02-safety.md)) :
  1. Pas encore de Langevin au secondaire. Alim = 12 V, limite de courant 0,2 A. Oscilloscopez la commande de grille (HIN/LIN) et le nœud de commutation — confirmez le temps mort et l'absence de shoot-through.
  2. Montez le transformateur d'adaptation + le Langevin TX **fixé sur la plaque en acier** (ou un bloc métallique sacrificiel épais). Toujours limite 0,2 A. Montez à la fréquence de pic de l'étage 1 juste assez longtemps pour voir le courant et la tension RX.
  3. Augmentez progressivement la limite de courant tout en surveillant la température des MOSFET et du transformateur. Ne laissez jamais un Langevin non fixé sous tension — les fonctionnements en plein air à pleine puissance sont ainsi que les céramiques se fissurent et les drivers meurent.

À FAIRE : projet KiCad (PCB) une fois le prototype sur breadboard (ou dead-bug) validé. D'ici là, les schémas dans [`../schematics/`](../../../../hardware/schematics) sont la source de vérité du design.
