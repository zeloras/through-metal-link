# Materiais de parede além do aço: quais paredes transmitem potência e dados

> [English (primary)](../../../docs/06-materials.md) · [Русский](../../ru/docs/06-materials.md) · [Deutsch](../../de/docs/06-materials.md) · Português · [Español](../../es/docs/06-materials.md) · [Français](../../fr/docs/06-materials.md) · [Italiano](../../it/docs/06-materials.md) · [Polski](../../pl/docs/06-materials.md) · [Türkçe](../../tr/docs/06-materials.md) · [Українська](../../uk/docs/06-materials.md) · [Tiếng Việt](../../vi/docs/06-materials.md) · [中文](../../zh/docs/06-materials.md) · [日本語](../../ja/docs/06-materials.md) · [한국어](../../ko/docs/06-materials.md) · [हिन्दी](../../hi/docs/06-materials.md)

O restante deste repositório assume aço. Esta página faz a pergunta mais simples e maior: **para quais materiais de parede o canal de dois transdutores funciona de fato**, e em qual modo? É um estudo de simulação (estilo `--mock`, sem dados de laboratório — intuição sobre o que merece um experimento de hardware), construído a partir do mesmo modelo semi-empírico do [channel_sim](../../../software/simulator/channel_sim.py) e estendido com absorção em volume.

Gerar: `python3 software/simulator/material_map.py` (requer numpy + matplotlib). Modelo e premissas: [../software/simulator/material_map.py](../../../software/simulator/material_map.py).

## O modelo em um minuto

Três grandezas decidem se uma parede é utilizável, e para quanta potência:

1. **Contraste de impedância e fase** — o modelo de placa Fabry–Perot sem perdas, idêntico ao [channel_sim](../../../software/simulator/channel_sim.py):
   T(f) = 1 / (1 + ((r − 1/r)/2)² · sin(2πfd/c)²), r = Z_parede / Z_acoplante, acoplante Z = 1.5 MRayl (graxa).
   Na ressonância de meia-onda (f = c/2d) uma placa simétrica sem perdas é totalmente transparente *independentemente de r*; o contraste r define quão **largos** são os dentes do pente (tolerância a erro de frequência), e a velocidade do som c define o espaçamento entre eles (Δf = c/2d).
2. **Absorção em volume**, invisível ao modelo sem perdas e fator decisivo para plásticos, concreto e borracha:
   A(f) = 10^(−α(f)·d/10), α(f) = α₁ₘₕᶻ · (f/1 MHz)^γ [dB/cm, unidirecional, longitudinal],
   onde α₁ₘₕᶻ é o valor a 1 MHz.
   γ ≈ 1 = perda viscosa/relaxação; γ > 2 = espalhamento por inhomogeneidades (agregado de concreto).
3. **A dose que a parede absorve de volta** — veja a seção [abaixo](#the-dose-what-the-wave-does-to-the-wall-frequency-by-frequency): tensão σ = √(2·I·Z), que *não* depende da frequência, e aquecimento próprio ΔT ∝ α(f)·I, que depende.

**Premissas, declaradas onde o código as declara:** propriedades típicas de manual (onda longitudinal, ~20 °C); lotes reais variam — grão, cargas, agregados, cura. Tudo abaixo é um ranking, não uma ficha técnica.

| Parede | ρ, kg/m³ | c_L, m/s | Z, MRayl | α @1 MHz, dB/cm | pente Δf @5 mm, kHz | λ @40 kHz, mm | T(40 kHz, 3 mm) | nota |
|---|---|---|---|---|---|---|---|---|
| aço | 7850 | 5900 | 46.3 | 0.02 | 590 | 148 | 0.21 | estrutural de grão fino |
| alumínio | 2700 | 6320 | 17.1 | 0.02 | 632 | 158 | 0.69 | classe 6061 |
| titânio | 4430 | 6100 | 27.0 | 0.03 | 610 | 152 | 0.45 | Ti-6Al-4V |
| cobre | 8960 | 4760 | 42.6 | 0.05 | 476 | 119 | 0.17 | denso, Z muito alto |
| vidro borossilicato | 2230 | 5640 | 12.6 | 0.01 | 564 | 141 | 0.77 | perda muito baixa |
| cerâmica de alumina | 3890 | 9900 | 38.5 | 0.08 | 990 | 248 | 0.51 | som rápido, baixa perda |
| PMMA (acrílico) | 1180 | 2690 | 3.2 | 2.5 | 269 | 67 | 0.95 | transparente, limitado por absorção em MHz |
| PVC (rígido) | 1400 | 2380 | 3.3 | 6 | 238 | 60 | 0.92 | mais perdedor que PMMA |
| HDPE | 950 | 2340 | 2.2 | 12 | 234 | 58 | 0.98 | macio, perdedor |
| concreto | 2300 | 3500 | 8.1 | 5 | 350 | 88 | 0.77 | espalhamento de agregado domina; varia por ordens de magnitude |
| borracha (com carga) | 1100 | 1500 | 1.6 | 60 | 150 | 38 | 0.85 | o beco sem saída honesto |

## Os gráficos

**Modo B (MHz) — o pente de espessura por material.** Esquerda: metais estruturais; direita: não-metais. Todas as paredes 5 mm, acoplamento com graxa. Picos do modelo sem perdas atingem T = 1 nas ressonâncias exatas; picos reais são menores por perdas de contato, e a absorção limita os materiais perdedores de imediato:

<img src="../../../docs/img/mat1-thickness-comb-materials.png" width="880">

**O mapa de materiais** — os dois eixos que decidem tudo: impedância (dificuldade de acoplamento/contato) vs absorção a 1 MHz (viabilidade em MHz). Alto-Z + baixo-α é o canto de classe potência; baixo-Z + alto-α é "40 kHz ainda aberto, MHz morto"; o canto da borracha é um beco sem saída em todas as frequências que visamos:

<img src="../../../docs/img/mat2-material-map.png" width="720">

**Proxy de acoplamento Modo A (40 kHz)** — o mesmo modelo de transmissão avaliado a 40 kHz através de uma parede de 3 mm, normalizado pelo aço. *Um ranking, não watts:* o par Langevin ressonante multiplica cada barra de forma aproximadamente igual e o modelo não tem carregamento de transdutor interno; esse multiplicador é território do estágio 2 ([experiments/002](../experiments/002-watts-3mm-steel/README.md)):

<img src="../../../docs/img/mat3-modea-coupling-materials.png" width="720">

## O que a varredura diz

- **A 40 kHz, paredes de baixo-Z (plásticos, revestimento de borracha) acoplam *mais facilmente* que o aço** — através da graxa elas estão quase casadas em impedância, então o pente é largo e a transmissão por passagem é alta. O que mata os plásticos em frequências mais altas é **absorção em volume**, não contato ou impedância. A escada de materiais a 40 kHz é portanto invertida em relação à intuição: HDPE/PMMA/PVC > vidro/concreto > alumínio > alumina > titânio > aço > cobre — com a ressalva forte de que o número de 40 kHz das borrachas extrapola α linearmente a partir de 1 MHz, o que a viscoelasticidade não garante.
- **O modo B divide os materiais de forma limpa.** Metais, vidro e alumina suportam MHz com absorção desprezível (α ≤ 0.1 dB/cm); o pente é *estreito* para paredes de alto-Z (aço, alumina — requer rastreamento de frequência, a lição de ~6% ⇒ ~10× de [00-theory](00-theory.md)) e *largo* para vidro/PMMA (tolerante, mas PMMA paga ~1.3 dB unidirecional a 1 MHz através de 5 mm — classe mW apenas).
- **Concreto é um material de 40 kHz, não de MHz.** Espalhamento de agregado (λ a 1 MHz ≈ 3.5 mm ≈ tamanho do agregado) eleva γ para ~2.5 e mata MHz; a prática de velocidade de pulso ultrassônico (40–80 kHz através de caminhos ≥1 m) é exatamente o modo A.
- **O nicho de baterias ([05](05-applications-map.md)) é acusticamente favorável:** uma parede de alumínio de 2–3 mm tem um proxy de acoplamento ~3× o do aço e absorção desprezível — o caso principal também é o caso fácil.
- **A escada de frequências para planejar no modo B** (parede de 5 mm, primeiro pente): PVC/HDPE ≈ 235 kHz, PMMA ≈ 270, cobre ≈ 480, aço ≈ 590, titânio ≈ 610, alumínio ≈ 630, vidro ≈ 560, alumina ≈ 990. Parede mais fina ⇒ proporcionalmente mais alta.

## A dose: o que a onda faz à parede, frequência por frequência

Transmissão responde "quanto passa"; esta seção responde à pergunta inversa — **quanto da onda fica na parede, e isso a prejudica?** O dano da onda-na-parede tem exatamente duas faces:

- **Tensão** σ = √(2·I·Z) — momento de onda plana; *independente da frequência*. Compare contra o limite de fadiga de alto ciclo (metais), resistência à flexão/tração (cerâmicas, vidro, concreto, borracha).
- **Aquecimento próprio** ΔT = α(f)·I·d²/(8k), regime estacionário, ambas as faces resfriadas — *depende da frequência* através de α(f), e é aí que a frequência morde: todo material isolante tem um joelho acima do qual cada oitava extra de frequência multiplica o calor depositado.

A 1 W/cm² (já além do que este projeto visa: a meta do estágio 2 de 0.5–5 W distribuídos sobre uma face de transdutor de ~19 cm² é 0.03–0.26 W/cm²):

| Parede | σ @1 W/cm², MPa | limite σ_e, MPa | margem de tensão | ΔT @40 kHz, K | ΔT @1 MHz, K | ΔT @5 MHz, K | teto @40 kHz, W/cm² | teto @1 MHz, W/cm² |
|---|---|---|---|---|---|---|---|---|
| aço | 0.96 | 200 | 208× | ~0 | ~0 | ~0 | ~1700 | ~1700 |
| alumínio | 0.58 | 60 | 103× | ~0 | ~0 | ~0 | ~420 | ~420 |
| titânio | 0.74 | 500 | 680× | ~0 | ~0 | ~0 | ~18000 | ~6500 |
| cobre | 0.92 | 60 | 65× | ~0 | ~0 | ~0 | ~170 | ~170 |
| vidro borossilicato | 0.50 | 30 | 60× | ~0 | ~0 | ~0 | ~140 | ~140 |
| cerâmica de alumina | 0.88 | 300 | 342× | ~0 | ~0 | ~0 | ~4700 | ~4700 |
| PMMA (acrílico) | 0.25 | 15 | 60× | 0.2 | 9.5 | 65 | ~100 | 2.1 |
| PVC (rígido) | 0.26 | 15 | 58× | 0.6 | 28.8 | 199 | ~33 | 0.7 |
| HDPE | 0.21 | 8 | 38× | 0.15 | 19.2 | 215 | ~58 | 1.0 |
| concreto | 0.40 | 2.5 | 6× | ~0 | 2.1 | 118 | 1.6 | 1.6 |
| borracha (com carga) | 0.18 | 1.5 | 8× | 11.5 | 288 | 1440 | 1.7 | 0.07 |

"Teto" = intensidade contínua na qual a parede permanece dentro de 20% do seu limite de fadiga/resistência e abaixo de +20 K de aquecimento próprio (regime estacionário, ambas as faces mantidas em ambiente). Operações com ciclos de trabalho aquecem menos; uma parede ancorada em apenas uma face — o caso usual, ar de um lado — aquece até 4× mais na face livre. Esses números são uma primeira estimativa, não uma garantia de projeto. Uma observação de convenção: os valores de α são dB de intensidade (10·log₁₀, a convenção de dosimetria — uma queda de 3 dB reduz I à metade); literatura de NDT pulse-echo que cita dB de amplitude (20·log₁₀) descreve o MESMO α com números duas vezes maiores — verifique qual convenção uma fonte usa antes de copiar seus números para esta tabela.

<img src="../../../docs/img/mat4-harm-materials.png" width="920">

O que a varredura de dose diz:

- **O veredito do aço de [00-theory](00-theory.md) se mantém e generaliza**: todo metal estrutural carrega 1 W/cm² com margens de 65–680× em tensão e micro-kelvins de aquecimento próprio. Metais são insensíveis à frequência em termos de dano — sua perda é pequena demais para aquecer a qualquer potência que possamos acoplar.
- **Dano por frequência em polímeros é térmico, não mecânico.** A margem de tensão do PMMA é um confortável 60× mesmo a 1 W/cm², mas o joelho de aquecimento fica logo acima de 1 MHz: benigno (~0.2 K) a 40 kHz, +9.5 K a 1 MHz, +65 K a 5 MHz — território de amolecimento a poucos W/cm². PVC cruza a linha de +10 K já a ~0.35 W/cm² @ 1 MHz; borracha absorbe ~288 K por W·cm⁻² a 1 MHz (e ~12 K mesmo a 40 kHz) — aquecimento histérico é *a* razão pela qual paredes revestidas de elastômero morrem, não o pente. HDPE fica no meio do caminho e lembra seu ponto de fusão: +215 K por W·cm⁻² a 5 MHz.
- **A margem apertada do concreto é de tração, não térmica**: 0.40 MPa de tensão de onda contra uma resistência à tração estática de ~2.5 MPa (fadiga ainda menor) deixa apenas ~6× de margem a 1 W/cm². O regime de 40–80 kHz permanece bem na densidade de potência do projeto; feixes concentrados de multi-W/cm² em concreto devem ser evitados, MHz duplamente (espalhamento aquece as interfaces dos agregados).
- **Conclusão para o roadmap:** nas densidades de potência do modo A (≤0.3 W/cm²) nenhum sólido na tabela está ameaçado — margens de tensão ≥11× (a mais apertada é a fadiga de tração do concreto a 11×; todo o resto ≥15×) e aquecimento ≤0.2 K para todo sólido de engenharia (borracha, a exceção que ninguém visa, ~3.5 K). O mapa de dano justifica o plano do projeto de escalar potência: os primeiros limites reais de material aparecem *acima* das metas do estágio 2, primeiro em líquidos (cavitação, a regra de ≤1 W/cm² de [00-theory](00-theory.md)), depois na fadiga de tração do concreto, depois em polímeros a MHz. As partes que realmente precisam de monitoramento em alta potência continuam sendo a cerâmica piezo e a linha de colagem — [02-safety](02-safety.md) — não a parede.

## Veredito por material

| Parede | Modo A — potência 40 kHz | Modo B — potência/dados MHz | Veredito |
|---|---|---|---|
| aço | ✓✓ referência | ✓ pente estreito — rastrear frequência | o baseline |
| alumínio | ✓✓ (proxy ~3× aço) | ✓ pente meio estreito | melhor parede estrutural (baterias!) |
| titânio | ✓✓ | ✓ meio estreito, baixa perda | nichos corrosivos/quentes, drones, cascos |
| cobre | ✓ (acoplamento mais difícil dos metais) | ✓ | nicho: barramentos selados/células eletroquímicas |
| vidro borossilicato | ✓✓ | ✓ pente mais largo — mais tolerante | janelas de lab, visores |
| cerâmica de alumina | ✓✓ | ✓ pentes mais rápidos (990 kHz @ 5 mm), baixa perda | paredes de processo quentes/isolantes |
| PMMA | ✓ banda larga | ⚠ classe mW ≤ ~0.5 MHz apenas | tanques, invólucros; não é parede de potência em MHz |
| PVC / HDPE | ✓ paredes finas | ✗ absorção | invólucros de baixo grau, nós de dados leves |
| concreto | ✓ 40–80 kHz (prática UPV) | ✗ espalhamento | fundações, tubos — modo A apenas |
| borracha (com carga) | ⚠ extrapolação de modelo não validada | ✗ | empiricamente o beco sem saída — [04](04-hybrid-channels.md) |

Uma parede de plástico de baixo-Z tem mais margem para links do modo A *tolerantes a desalinhamento*, mas oferece menos margem absoluta de potência contra absorção quando se ultrapassa ~200 kHz; meça antes de prometer qualquer coisa.

## Concreto com armadura — o caso multicamada

Concreto real nunca é simples: malhas de armadura ficam a uma profundidade de cobrimento, e o modelo 1D de placa única acima não as enxerga. `chart_rebar` / `rebar_table` estendem o modelo para pilhas gerais ([`stack_transmission`](../../../software/simulator/material_map.py), recursão multicamada exata com absorção por camada, protegida no autoteste). Geometria modelada: uma parede estrutural de 150 mm, uma malha de aço de espessura planar-equivalente Ø16 mm a 40 mm de cobrimento; o modelo *planar* é o pior caso — uma barra real sombreia apenas a parte do feixe que intersecta, então pense nessas como mergulhos de envelope, não previsões:

| Pilha (150 mm concreto) | T(40 kHz) | T(100 kHz) | T(1 MHz) |
|---|---|---|---|
| 150 mm simples | 0.135 | 0.133 | 8.9e-09 |
| armadura Ø16 @ 40 mm | 0.013 | 0.069 | 6.6e-09 |
| duas malhas Ø16 @ 40 mm | 0.003 | 0.001 | 5.1e-09 |

<img src="../../../docs/img/mat5-rebar.png" width="880">

O que o modelo de pilha diz:

- **Uma malha planar sob o feixe custa ×10 exatamente a 40 kHz** (interferência de banda de parada da camada de aço), mas o mergulho é estreito: a 100 kHz a mesma pilha perde apenas ×2. A leitura prática para o nicho de pipeline/autoclave: *uma varredura de frequência em torno de 40–120 kHz, não uma frequência fixa*, é o que faz um link do modo A passar pela armadura — e os mergulhos se movem com a profundidade de cobrimento, então uma varredura também identifica a geometria (a base de uma estimativa de profundidade de armadura).
- **Uma segunda malha (uma grade) é quase um mata-parede neste pior caso** (×45 para baixo e plana em banda larga perto de 40–100 kHz): armadura densa no caminho é o honesto indicador de "escolha outro ponto na parede", não um problema de processamento de sinal.
- **Modo B através de concreto estrutural está morto com ou sem armadura** (nível de 1e-8 a 1 MHz: 5 dB/cm × 15 cm). Armadura nem entra na história em MHz.
- Ressalvas, em ordem de importância: premissa de camada planar (pior caso — uma barra Ø16 bloqueia bem menos da metade da seção transversal de um feixe de 40–50 mm), onda paralela ao eixo da armadura assumida, e propagação 1D (sem difração ao redor da barra). O experimento de hardware certo é um aparato de varredura em uma laje real: mapear T(x, y) a 40/80/120 kHz sobre uma grade de armadura e ajustar as posições de mergulho do modelo planar ao passo da grade.

## O que um acompanhamento de hardware deveria medir

Antes de confiar em qualquer placa específica: método de duas espessuras por material (duas placas de d e 2d no mesmo contato) para extrair α(f) e c reais — esse único conjunto de dados substitui cada linha da tabela acima. Passagens bônus naturais dentro dos protocolos existentes: repetir a varredura do experimento [001](../experiments/001-sweep-map-3mm-steel/README.md) em uma placa de PMMA de 5 mm, uma placa de borossilicato ou alumina 99%, e um bloco de concreto de grau conhecido; esperar um pico *mais baixo mas mais largo* para os plásticos, um pente estreito para as cerâmicas, e um contato sensível à temperatura em todo lugar. Durante o ensaio de potência do experimento [002](../experiments/002-watts-3mm-steel/README.md), prender um termômetro IR (ou um termopar fino) na face oposta de cada tipo de parede — o ΔT medido a uma entrada conhecida é o único número que valida ou mata a coluna de aquecimento da tabela de dose. Nada nesta página é medido — é o mapa do que medir primeiro.
