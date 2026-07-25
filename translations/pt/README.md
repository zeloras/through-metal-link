# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · Português

Uma plataforma aberta para transferência de energia e dados ultrassônicos através de paredes de metal sólidas — "através do aço sem um único buraco", construída com meios de garagem.

**Status:** estágio 0 — preparação · repositório permanece privado até os primeiros resultados reproduzíveis · lista de compras: [QUICKSTART.md](../../QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml)

Os documentos são multilíngues: o inglês é o primário e vive nos caminhos canônicos; cada outra língua espelha a árvore em [translations/](../../translations/). Edite qualquer idioma — o CI traduz e commita o restante (veja [CONTRIBUTING.md](../../CONTRIBUTING.md)).

<p align="center"><img src="../../docs/img/sim0-rig-sketch.png" alt="Rig de estágio 1: Pi → DDS → ponte de meia-onda → transformador → transdutor piezo TX | aço | transdutor piezo RX → ponte → ADC → Pi" width="900"></p>

## A ideia em um parágrafo

As ondas de rádio não passam pelo metal (gaiola de Faraday) e uma penetração de cabo significa um buraco, um selo e um ponto de falha. O ultrassom, por outro lado, viaja pelo metal muito bem: um elemento piezo de cada lado da parede o transforma em um canal para energia (watts através de 3–5 mm de aço) e dados (kbit/s). A física é comprovada (RPI: 50 W + 12 Mbit/s através de 63 mm de aço; NASA JPL: ~kW através de 5 mm de titânio), as patentes fundamentais expiraram e não existe uma plataforma aberta — este repositório está construindo uma.

## Roadmap

| Estágio | Entregável | Critério de sucesso | Expectativa |
|---|---|---|---|
| 1. Mapa de varredura | resposta de frequência do canal "Langevin–3 mm de aço–Langevin" | ressonância do par encontrado, plot em [experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md) | [sim1](../../docs/img/sim1-sweep-contacts.png), [sim2](../../docs/img/sim2-pair-mismatch.png) |
| 2. Watts | energia no carregamento em ressonância | ≥0,5 W através de 3 mm de aço | [sim4](../../docs/img/sim4-power-budget.png) |
| 3. Dados | FSK/OOK sobre o mesmo par | ≥1 kbit/s sem erros | [sim5](../../docs/img/sim5-ook-datarate.png) |
| 4. Nó | ESP32 + sensor em uma caixa soldada, alimentado e telemetizado pelo som sozinho | ≥1 h de operação autônoma | [sim4](../../docs/img/sim4-power-budget.png) |
| 5. Publicação | repositório vai público, artigo/como-fazer | reprodução por um terceiro | — |

## Mapa do repositório

Cada bloco abaixo se expande: dentro está um resumo suficiente para trabalhar a partir dele, mais um link para o documento completo.

<details>
<summary><b>🛒 De zero a um rig de trabalho: o que comprar e em que ordem</b> — <a href="../../QUICKSTART.md">QUICKSTART.md</a></summary>

**Orçamento:** ~$210 mínimo, ~$300 confortável (descontar ~$120 se você já possui um Pi, um ferro de soldar e uma fonte de alimentação de bancada). Três cestas: ferramentas (~$120), eletrônica do rig (~$70, [BOM completo](../../hardware/bom/bom-stage1.csv)), mecânica (~$20). Opcional, mas fortemente recomendado: um osciloscópio USB (~$60–80).

**Caminho crítico — envio do AliExpress (3–4 semanas):** ordene a eletrônica no primeiro dia. Decisão-chave: comprar **4 transdutores Langevin do mesmo lote** — a varredura escolherá o melhor par ([por quê](../../docs/img/sim2-pair-mismatch.png)).

**Enquanto isso chega:** faça um teste seco do pipeline sem hardware —
```bash
python3 software/sweep-map/sweep_map.py --mock
```
**O rig é considerado funcionando quando:** (1) o pico da varredura se reproduz em duas execuções dentro de <200 Hz; (2) ≥0,5 W no carregamento através de 3 mm de aço; (3) o LED atrás da placa acende, foto em experiments/001.

</details>

<details>
<summary><b>📚 Teoria em um minuto</b> — <a href="../../docs/00-theory.md">docs/00-theory.md</a></summary>

O transdutor piezo TX é pressionado contra a parede e impulsiona uma onda longitudinal nela; o transdutor piezo RX do outro lado a transforma de volta em eletricidade. Velocidade do som no aço: ~5900 m/s.

Dois modos de operação:

| Modo | Frequência | Ressonância definida por | Rendimentos | Status |
|---|---|---|---|---|
| **A** — transdutores Langevin | 40 kHz | o par de transdutores (parede ≪ λ — uma "membrana") | watts, kbit/s | modo de início (estágios 1–4, [ADR-0001](../../docs/decisions/0001-vybor-chastotnogo-rezhima.md)) |
| **B** — discos | 0,6–1 MHz | ressonância de espessura da parede ([comb](../../docs/img/sim3-thickness-comb.png)) | centenas de mW, centenas de kbit/s | ramo após os primeiros watts; precisa de rastreamento de frequência automático |

As principais perdas: desajuste de ressonância dentro do par (±1 kHz para transdutores Langevin baratos), qualidade de contato acústico (epóxi > couplante de graxa + morsa > pressão seca), desalinhamento, deriva de ressonância com a temperatura. A resposta para todos eles é a mesma: **um mapa de varredura antes de qualquer alteração no setup**.

</details>

<details>
<summary><b>📈 O que o rig deve mostrar: gráficos de expectativa do simulador</b> — <a href="../../software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Um modelo de canal semi-empírico (não FEM — intuição para "o que a varredura mostrará e o que contar"). Regenerar com: `python3 channel_sim.py --out ../../docs/img`.

**Estágio 1 — varredura.** Um pico estreito perto de ~40 kHz; couplante de graxa + morsa dá ~4× pressão seca e ~50× um vazio. Sem pico significa um problema com o contato ou o par:
<img src="../../docs/img/sim1-sweep-contacts.png" width="720">

**Por que 4 transdutores Langevin, não 2.** Um desajuste de ressonância de 1,5 kHz dentro do par diminui a potência 10 vezes:
<img src="../../docs/img/sim2-pair-mismatch.png" width="720">

**Estágio 3 — dados.** OOK atinge o anelamento do ressonador (Q~40 → τ≈0,3 ms): 1 kbit/s é limpo, em 5 kbit/s o olho está fechado. Ir mais rápido leva ao modo B:
<img src="../../docs/img/sim5-ook-datarate.png" width="720">

**Orçamento de energia do receptor.** O modo A alimenta tudo até os picos Wi-Fi; o modo B alimenta um ESP32 com um buffer de supercapacitor:
<img src="../../docs/img/sim4-power-budget.png" width="720">

**Para mais tarde (modo B).** A placa se torna transparente em uma combinação de ressonâncias de espessura — a frequência precisa ser rastreada:
<img src="../../docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Segurança — leia antes do primeiro power-up</b> — <a href="../../docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Centenas de volts no piezo** em ressonância — o TVS no lado do receptor vai antes do primeiro power-up; mantenha as mãos longe dos cabos.
2. **Mains** — apenas através de uma fonte de alimentação de bancada / isolamento; placas de driver de limpeza ultrassônica são galvanicamente ligadas à rede.
3. **Ouvidos** — operar transdutores apenas quando pressionados contra o metal; nunca execute ultrassom de alta potência sem uma estrutura.
4. **Calor** — um transdutor Langevin sem morsa superaquece em minutos; verifique a morsa antes de aplicar energia.
5. **Estilhaços** — o piezocerâmico é quebradiço: um parafuso apertado demais ou um impacto significa estilhaços; use óculos de segurança para qualquer trabalho mecânico.

Primeiro power-up do driver: defina o limite de corrente da fonte de alimentação de bancada para 0,2 A.

</details>

<details>
<summary><b>🧭 Arte anterior e higiene de patente</b> — <a href="../../docs/01-prior-art.md">docs/01-prior-art.md</a></summary>

Toda decisão técnica deve remontar a uma "fonte livre" (patentes expiradas, artigos). A fundação: **US5982297** (Aerospace Corp — a receita básica para um par de piezo de parede), **US7902943** (Caltech/JPL — feed-through de Sherrit), **US9361877** (Univ. Oklahoma — um sistema de transceptor completo); todos mortos. Artigos-chave: Lawry 2013 (50 W + 12,4 Mbit/s através de 63,5 mm de aço), Sherrit/NASA (uma lâmpada de 100 W), Yang 2015 (pesquisa).

Não copie enquanto ainda estiver vivo (US-only, até ~2032; estágios 1–4 não precisam disso): alocação de OFDM da RPI, esquema de duplex completo da RPI, transdutores conformais da Drexel.

Decisões de arquitetura são registradas em [docs/decisions/](../../docs/decisions/0001-vybor-chastotnogo-rezhima.md) (ADR).

</details>

<details>
<summary><b>🔌 Hardware e firmware</b> — hardware/, firmware/</summary>

- [hardware/bom/bom-stage1.csv](../../hardware/bom/bom-stage1.csv) — lista de compras do estágio 1.
- [hardware/schematics/](../../hardware/schematics/README.md) — **esquemas de circuito** (gerados a partir do código): driver, receptor, pinout do Pi, nó do harvestor.
- [hardware/driver/](../../hardware/driver/README.md) — driver TX: ponte de meia-onda IR2110 + 2×IRF540, transformador de acoplamento (um transdutor Langevin é uma carga capacitiva!). Placa KiCad vem após o protótipo de breadboard dar certo.
- [hardware/receiver/](../../hardware/receiver/README.md) — receptor, etapa a etapa: ponte de Schottky → ADC (estágio 1) → carregamento (estágio 2) → LTC3588 + supercapacitor + ESP32 (estágio 4).
- [firmware/node-esp32/](../../firmware/node-esp32/README.md) — nó do estágio 4 (stub): sono profundo, leitura do sensor, publicidade BLE, orçamento de 1–5 mW médio.

</details>

<details>
<summary><b>💻 Software: medições e simulador</b> — software/</summary>

- [software/sweep-map/sweep_map.py](../../software/sweep-map/sweep_map.py) — o cavalo de batalha do estágio 1: varredura DDS → leituras ADC → CSV + plot de resposta de frequência. Tem `--mock` para uma execução sem hardware. No Pi: `raspi-config` → habilite SPI e I2C; `pip install spidev smbus2 matplotlib`.
- [software/simulator/channel_sim.py](../../software/simulator/channel_sim.py) — gerador de gráficos de expectativa (`pip install numpy matplotlib`).
- [data/](../../data/README.md) — logs brutos; CSV/PNG ficam fora do git, apenas plots curados vão para o git dentro do diretório do experimento.

</details>

<details>
<summary><b>🗺️ Onde aplicar isso: barreiras, canais, nichos</b> — <a href="../../docs/04-hybrid-channels.md">docs/04</a>, <a href="../../docs/05-applications-map.md">docs/05</a></summary>

Não há um canal universal — a plataforma combina a física com a barreira: piezo-acústica (primária: aço/alumínio com contato — watts e kbit/s), EMAT (metal sujo/quente, sem contato — dados), magnetismo de baixa frequência (paredes de dewars com areia de vácuo — bits/s). Fim honesto: paredes revestidas de borracha/compostas, líquido borbulhante no caminho.

Prioridade de nicho: **(1)** câmaras de vácuo e criostatos de laboratório — o público de hardware de código aberto, sem certificações; **(2)** tanques de fermentação — um terreno de prova a uma distância a pé; **(3)** pacotes de bateria selados — o caso emblemático (detecção de corrida térmica sem uma penetração no pacote). O protocolo de descoberta e ajuste automático do receptor (um analógico Qi): [docs/03-discovery-protocol.md](../../docs/03-discovery-protocol.md).

</details>

<details>
<summary><b>📁 Layout do diretório</b></summary>

```
docs/            teoria, arte anterior, segurança, aplicações, log de decisões (ADR)
docs/img/        gráficos de expectativa (gerados por software/simulator/channel_sim.py)
hardware/        BOM, driver (ponte de meia-onda), receptor (retificador/harvestor)
firmware/        firmware do nó (ESP32 — stub até o estágio 4)
software/        scripts de medição (mapa de varredura de resposta de frequência) e simulador de canal
experiments/     protocolos de experimento — do modelo, um diretório = um experimento
data/            logs brutos (arquivos grandes ficam fora do git)
```

</details>

## Princípios

1. **Reprodutibilidade a partir do zero.** Qualquer pessoa com um ferro de soldar e ~$210 pode reproduzir o resultado a partir deste repositório sozinho.
2. **Cada experimento é um protocolo.** Nenhum "funcionou mais ou menos": [experiments/TEMPLATE.md](../../experiments/TEMPLATE.md) é obrigatório.
3. **Higiene de patente.** Construímos sobre a camada expirada ([docs/01-prior-art.md](../../docs/01-prior-art.md)); decisões são registradas em [docs/decisions/](../../docs/decisions/0001-vybor-chastotnogo-rezhima.md).
4. **Medição primeiro, opinião segundo.** Um mapa de varredura antes de qualquer conclusão sobre o canal.

## Licenças e patentes

Código — Apache-2.0, hardware — CERN-OHL-W v2, documentação — CC-BY-4.0; textos completos em [LICENSES/](../../LICENSES/). Qualquer pessoa pode bifurcar e construir sobre isso, comercialmente incluído; proteção de patente vem dos grants e cláusulas de retaliação nas licenças mais um estratégia de publicação defensiva. O esquema completo e o protocolo de publicação defensiva: [LICENSES.md](../../LICENSES.md); regras de contribuição: [CONTRIBUTING.md](../../CONTRIBUTING.md).
