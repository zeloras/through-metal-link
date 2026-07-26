# Teoria do canal (o mínimo necessário para trabalhar)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · Português

## Princípio
Um elemento piezoelétrico TX pressionado/colado contra a parede excita uma onda longitudinal nela; um piezoelétrico RX do outro lado a transforma de volta em eletricidade. A parede é um ressonador: nas ressonâncias de espessura (múltiplos de um meio-comprimento de onda) a transmissão está no seu máximo.

## Números-chave
Velocidade longitudinal do som no aço: ~5900 m/s.

| Espessura do aço | Ressonância de meio-onda |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Comprimento de onda no aço: 148 mm @ 40 kHz; 5,9 mm @ 1 MHz.

## Dois modos
- **A (40 kHz, transdutores Langevin).** Uma placa de 3–5 mm ≪ λ — ela se comporta como uma membrana; a ressonância é definida pelo par de transdutores, não pela parede. Mais simples e poderoso do que o modo B — o modo para começar. Prova de existência em laboratório (não um alvo de garagem): NASA JPL ~24,5 kHz, centenas de W até um kW através de 5 mm de Ti com hardware personalizado.
- **B (0,6–1 MHz, discos).** Ressonância de espessura da própria parede, e uma ressonância afiada (um deslocamento de frequência de ~6% ⇒ a transmissão cai ~10× no modelo de Fabry-Perot). A classe de resultados RPI/Moss: centenas de mW mais dados a centenas de kbit/s sob ligação e acoplamento de laboratório. Requer rastreamento de frequência automático.

## Principais perdas
Desequilíbrio de ressonância dentro do par de transdutores (transdutores Langevin baratos se espalham ±1 kHz), qualidade do contato acústico (epóxi > couplante de graxa espessa + clamp > pressão seca), desalinhamento, deriva de ressonância com a temperatura. A resposta para tudo isso é a mesma: execute um mapa de varredura antes de cada alteração no setup.

## Efeito na parede e nos meios por trás dela

Versão curta: em níveis de potência da plataforma, a parede e qualquer gás por trás dela são intocados. Um líquido por trás da parede afeta principalmente *o canal*; o canal só começa a afetar *o líquido* perto do limiar de cavitação. Números aproximados abaixo são para o modo A: 40 kHz, ~1 W/cm² em 3 mm de aço.

**Parede — sem deformação, sem fadiga, nunca.** Velocidade de partícula v = √(2I/ρc) ≈ 21 mm/s ⇒ deslocamento ≈ 80 nm, tensão de onda plana ε = v/c ≈ 3,5·10⁻⁶. Dois cálculos de estresse equivalentes: elástico E·ε ≈ 0,7 MPa (E ≈ 200 GPa) e acústico p = Z·v ≈ 1,0 MPa (Z_aço ≈ 4,6·10⁷ Pa·s/m). O aço cede a 250+ MPa e seu limite de resistência à fadiga é ~200 MPa — ainda uma margem >200× de qualquer forma, e abaixo do limite de resistência à fadiga o aço suporta ciclos ilimitados. As partes mecanicamente frágeis estão em outro lugar: o cerâmico piezoelétrico (quebradiço, despolariza quando superaquecido) e a linha de cola (epóxi aquece e fadiga primeiro) — veja [02-safety](02-safety.md).

**Gás por trás da parede — efeito zero.** A impedância de aço→ar (~4,6·10⁷ vs ~400 Pa·s/m) transmite uma fração da ordem de 10⁻⁵ da potência. Sem aquecimento ou agitação mensuráveis; eletrônicos dentro de uma caixa selada não notam o movimento da parede na ordem de nm.

**Líquido por trás da parede — duas direções:**

- *Líquido → canal (sempre).* A água carrega a face distante com ~1,5 MRayl em vez de ar: parte da potência irradia para o líquido, Q cai, o pico de varredura se desloca e se alarga. O modo B é atingido com mais força — o comb de ressonância de espessura é calculado para fronteiras aço-ar e se move com a carga do líquido. A regra de varredura cobre isso: **re-varrer contra o recipiente real e completo**, nunca confie em uma varredura feita contra um recipiente vazio. Benefício lateral: amortecimento do líquido encurta o anelamento do ressonador (τ), então o olho OOK se abre em taxas de bits mais altas. Bolhas no caminho (líquido fermentado!) espalham fortemente — veja a solução em [04-hybrid-channels](04-hybrid-channels.md).
- *Canal → líquido (somente em alta potência).* Pressão de pico irradiada na água: p ≈ ρc·v ≈ 1,5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0,3 atm. O limiar de cavitação inercial em 40 kHz na água comum (gaseificada) é ~1–2 atm, então a 1 W/cm² a margem é 3–10×. Mas p cresce como √potência, e ondas estacionárias em um recipiente fechado criam pontos quentes locais — dezenas de W/cm² contínuos em um tanque cheio de líquido podem atingir o limiar. Cruzar isso significa degaseificação de CO₂, sonoquímica (sabores fora do comum em produtos alimentícios) e erosão de cavitação de longo prazo da superfície interna (exatamente como os limpadores ultrassônicos limpam). Teto prático para potência contínua em paredes com apoio líquido: **≲1 W/cm²**. O modo B é isento: em MHz, o limiar é uma ordem de magnitude mais alto e as potências são de centenas de mW.

## Orçamento de potência do receptor (aproximado)
LED 20 mW; ESP32 com ciclo de trabalho de 1–5 mW em média; rádio BLE ~150 mW enquanto o rádio está ligado. Buffer: um supercapacitor de 1 F @ 3,3 V armazena E = ½CV² = 5,4 J. Quantas transmissões isso compra depende do tempo no ar: um evento de publicidade BLE curto (~2–5 ms @ ~150 mW) é apenas ~0,3–0,8 mJ → na ordem de **10⁴ pacotes** de um capacitor cheio; uma conexão longa / explosão (~100 ms de rádio ligado) é ~15 mJ → na ordem de **10² explosões**. A retirada média ainda precisa ficar dentro dos watts colhidos (o alvo de estágio 2 ≥0,5 W na carga é o portão; até que isso seja medido, trate as bandas de modo A de multi-watt nos gráficos do simulador como alvos, não dados).
