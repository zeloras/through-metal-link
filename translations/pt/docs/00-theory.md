# Teoria do canal (o mínimo necessário para trabalhar)

> [English (primary)](../../../docs/00-theory.md) · [Русский](../../ru/docs/00-theory.md) · [Deutsch](../../de/docs/00-theory.md) · Português

## Princípio
Um elemento piezo TX pressionado/colado contra a parede excita uma onda longitudinal nela; um piezo RX do outro lado a transforma de volta em eletricidade. A parede é um ressonador: nas ressonâncias de espessura (múltiplos de um meio-comprimento de onda) a transmissão está no seu máximo.

## Números-chave
Velocidade longitudinal do som no aço: ~5900 m/s.

| Espessura do aço | Ressonância de meio-comprimento |
|---|---|
| 3 mm | ~983 kHz |
| 4 mm | ~738 kHz |
| 5 mm | ~590 kHz |

Comprimento de onda no aço: 148 mm @ 40 kHz; 5,9 mm @ 1 MHz.

## Dois modos
- **A (40 kHz, transdutores Langevin).** Uma placa de 3–5 mm ≪ λ — ela se comporta como uma membrana; a ressonância é definida pelo par de transdutores, não pela parede. O regime NASA JPL (~24,5 kHz, centenas de W até um kW através de 5 mm de Ti). Mais simples, mais poderoso, o que começar.
- **B (0,6–1 MHz, discos).** Ressonância de espessura da própria parede, e uma ressonância aguda (uma mudança de frequência de ~6% ⇒ eficiência cai ~10×). O regime RPI/Moss: centenas de mW mais dados a centenas de kbit/s. Requer acompanhamento automático de frequência.

## Principais perdas
Diferença de ressonância dentro do par de transdutores (transdutores Langevin baratos se espalham ±1 kHz), qualidade do contato acústico (epóxi > couplante de graxa espessa + clamp > pressão seca), desalinhamento, deriva de ressonância com a temperatura. A resposta para tudo isso é a mesma: execute um mapa de varredura antes de cada alteração no setup.

## Efeito na parede e nos meios por trás dela

Versão curta: nos níveis de potência da plataforma, a parede e qualquer gás por trás dela não são afetados. Um líquido por trás da parede afeta principalmente *o canal*; o canal só começa a afetar *o líquido* perto do limiar de cavitação. Os números abaixo são para o modo A: 40 kHz, ~1 W/cm² em 3 mm de aço.

**Parede — sem deformação, sem fadiga, nunca.** Velocidade de partícula v = √(2I/ρc) ≈ 21 mm/s ⇒ deslocamento ≈ 80 nm, deformação ≈ 3,5·10⁻⁶, tensão ≈ 0,7 MPa. O aço cede a 250+ MPa e seu limite de resistência à fadiga é ~200 MPa — uma margem >300×, e abaixo do limite de resistência à fadiga o aço suporta ciclos ilimitados. As partes mecânicamente frágeis estão em outro lugar: o cerâmico piezo (quebradiço, despolariza quando superaquecido) e a linha de ligação (epóxi aquece e fadiga primeiro) — veja [02-safety](02-safety.md).

**Gás por trás da parede — efeito zero.** A impedância de aço→ar (~4,6·10⁷ vs ~400 Pa·s/m) transmite uma fração da ordem de 10⁻⁵ da potência. Sem aquecimento ou agitação mensuráveis; eletrônicos dentro de uma caixa selada não notam o movimento de nm da parede.

**Líquido por trás da parede — duas direções:**

- *Líquido → canal (sempre).* A água carrega a face distante com ~1,5 MRayl em vez de ar: parte da potência irradia para o líquido, Q cai, o pico de varredura se desloca e se alarga. O modo B é atingido com mais força — o comb de ressonância de espessura é calculado para fronteiras aço–ar e se move com a carga do líquido. A regra de pé cobre isso: **re-varrer contra o recipiente real e completo**, nunca confie em uma varredura feita contra um recipiente vazio. Benefício lateral: a amortecimento do líquido encurta o anelamento do ressonador (τ), então o olho OOK se abre em taxas de bits mais altas. Bolhas no caminho (líquido fermentado!) espalham fortemente — veja a solução em [04-hybrid-channels](04-hybrid-channels.md).
- *Canal → líquido (somente em alta potência).* Pressão de pico irradiada para a água: p ≈ ρc·v ≈ 1,5 MRayl × 21 mm/s ≈ 30 kPa ≈ 0,3 atm. O limiar de cavitação inercial em 40 kHz em água comum (gaseificada) é ~1–2 atm, então a 1 W/cm² a margem é 3–10×. Mas p cresce como √potência, e ondas estacionárias em um recipiente fechado criam pontos quentes locais — dezenas de W/cm² contínuos em um tanque cheio de líquido podem atingir o limiar. Cruzar significa degaseificação de CO₂, sonoquímica (sabores fora em produtos alimentícios), e erosão de longo prazo da superfície interna devido à cavitação (exatamente como os limpadores ultrassônicos limpam). Teto prático para potência contínua em paredes com líquido: **≲1 W/cm²**. O modo B é isento: em MHz, o limiar é uma ordem de magnitude mais alto e as potências são de centenas de mW.

## Orçamento de energia do receptor (aproximado)
LED 20 mW; ESP32 com ciclo de trabalho de 1–5 mW em média; pacote BLE ~150 mW pico — buffer: um supercapacitor de 1 F @ 3,3 V = 5,4 J ≈ 360 transmissões.
