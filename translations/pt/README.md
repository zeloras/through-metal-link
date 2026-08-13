# through-metal-link

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · Português · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [Tiếng Việt](../vi/README.md) · [中文](../zh/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [हिन्दी](../hi/README.md)

Uma plataforma aberta para transferência de energia e dados ultrassônicos através de paredes de metal sólidas — "através do aço sem um único buraco", construída com meios de garagem.

**Experimente agora (sem hardware):** `python3 software/sweep-map/sweep_map.py --mock`

**Status:** estágio 0 — preparação · 💰 **[recompensa de $250 para a primeira construção independente](https://github.com/zeloras/through-metal-link/issues)** · lista de compras: [QUICKSTART.md](../../QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml) [![DCO](https://img.shields.io/badge/DCO-signed--off--by-blue)](../../CONTRIBUTING.md) [![License](https://img.shields.io/badge/license-Apache--2.0%20%7C%20CERN--OHL--W%20v2%20%7C%20CC--BY--4.0-blue)](../../LICENSES.md)

Docs são multilíngues: Inglês é o primário e vive nos caminhos canônicos; cada outro idioma espelha a árvore em [translations/](../). Edite qualquer idioma — CI traduz e commit os demais (veja [CONTRIBUTING.md](../../CONTRIBUTING.md)).

<p align="center"><img src="../../docs/img/sim0-rig-sketch.png" alt="Estágio 1 rig: Pi → DDS → half-bridge → transformer → piezo TX | aço | piezo RX → bridge → ADC → Pi" width="900"></p>

## A ideia em um parágrafo

Ondas de rádio não passam pelo metal (gaiola de Faraday), e uma penetração de cabo significa um buraco, um selo e um ponto de falha. Ultrasom, por outro lado, viaja pelo metal sem problemas: um elemento piezo de cada lado da parede o transforma em um canal para energia e dados. A literatura de laboratório já provou a física em níveis sérios (RPI: 50 W + 12 Mbit/s através de 63,5 mm de aço; NASA JPL: até ~kW através de 5 mm de titânio) — essas são provas de existência com hardware especializado, não o BOM deste repositório. As patentes fundamentais expiraram, e não existe uma plataforma aberta e reproduzível ainda — este repositório está construindo uma, começando em **watts de energia e kbit/s de dados através de 3–5 mm de aço** uma vez que o estágio 2 seja medido.

## Roadmap

| Estágio | Entregável | Critério de sucesso | Expectativa |
|---|---|---|---|
| 1. Sweep map | resposta de frequência do canal "Langevin–3 mm de aço–Langevin" | ressonância do par encontrado, plot em [experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md) | [sim1](../../docs/img/sim1-sweep-contacts.png), [sim2](../../docs/img/sim2-pair-mismatch.png) |
| 2. Watts | energia no carregador em ressonância | ≥0,5 W através de 3 mm de aço, protocolo em [experiments/002](../../experiments/002-watts-3mm-steel/README.md) | [sim4](../../docs/img/sim4-power-budget.png) |
| 3. Dados | FSK/OOK sobre o mesmo par | ≥1 kbit/s sem erros | [sim5](../../docs/img/sim5-ook-datarate.png) |
| 4. Nó | ESP32 + sensor em uma caixa soldada, alimentada e telemetrada por som apenas | ≥1 h de operação autônoma | [sim4](../../docs/img/sim4-power-budget.png) |
| 5. Publicação | repositório vai público, artigo/como-fazer | reprodução por um terceiro | — |

## Mapa do repositório

Cada bloco abaixo expande: dentro está um resumo suficiente para trabalhar a partir dele, mais um link para o documento completo.

<details>
<summary><b>🛒 De zero a um rig funcionando: o que comprar e em que ordem</b> — <a href="../../QUICKSTART.md">QUICKSTART.md</a></summary>

**Orçamento:** ~$210 mínimo, ~$300 confortável (descontar ~$120 se você já possui um Pi, um ferro de soldar e uma fonte de alimentação de bancada). Três cestas: ferramentas (~$120), eletrônica do rig (~$70, [lista de materiais completa](../../hardware/bom/bom-stage1.csv)), mecânica (~$20). Opcional, mas fortemente recomendado: um osciloscópio USB (~$60–80).

**Caminho crítico — envio da AliExpress (3–4 semanas):** ordene a eletrônica no primeiro dia. Decisão-chave: comprar **4 transdutores Langevin do mesmo lote** — a varredura irá escolher o melhor par ([por quê](../../docs/img/sim2-pair-mismatch.png)).

**Enquanto envia:** faça um teste seco do pipeline sem hardware —

```bash
python3 software/sweep-map/sweep_map.py --mock
```

**Concluído quando (por estágio):** estágio 1 — pico de varredura se reproduz em duas execuções dentro de <200 Hz ([experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)); estágio 2 — ≥0,5 W em um carregador conhecido através de 3 mm de aço e um LED aceso do lado RX ([experiments/002](../../experiments/002-watts-3mm-steel/README.md)).

</details>

<details>
<summary><b>📚 Teoria em um minuto</b> — <a href="../../docs/00-theory.md">docs/00-theory.md</a></summary>

O transdutor piezo TX é pressionado contra a parede e aciona uma onda longitudinal nela; o transdutor piezo RX do outro lado a transforma de volta em eletricidade. Velocidade do som no aço: ~5900 m/s.

Dois modos de operação:

| Modo | Frequência | Ressonância definida por | Rende | Status |
|---|---|---|---|---|
| **A** — transdutores Langevin | 40 kHz | o par de transdutores (parede ≪ λ — uma "membrana") | watts, kbit/s | modo de início (estágios 1–4, [ADR-0001](../../docs/decisions/0001-frequency-mode-choice.md)) |
| **B** — discos | 0,6–1 MHz | ressonância de espessura da parede ([comb](../../docs/img/sim3-thickness-comb.png)) | centenas de mW, centenas de kbit/s | ramo após os primeiros watts; precisa de rastreamento de frequência automático |

As principais perdas: desajuste de ressonância dentro do par (±1 kHz para transdutores Langevin baratos), qualidade de contato acústico (epóxi > couplante de graxa + clamp > pressão seca), desalinhamento, deriva de ressonância com a temperatura. A resposta para todos eles é a mesma: **uma varredura antes de qualquer mudança no setup**.

</details>

<details>
<summary><b>📈 O que o rig deve mostrar: gráficos de expectativa do simulador</b> — <a href="../../software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

Um modelo de canal semi-empírico (não FEM, **não dados de laboratório** — intuição para "como a varredura deve parecer e o que mirar"). Suposições são explícitas em `channel_sim.py` (carga carregada Q≈40, fatores de contato, cadeia η≤40%). Regenerar com: `python3 channel_sim.py --out ../../docs/img`.

**Estágio 1 — varredura.** Um pico estreito perto de ~40 kHz; o modelo tem multiplicadores de contato placeholder grease:dry:gap = 1 : 0,25 : 0,02 (ou seja, graxa ≈4× seca e ≈50× fenda de ar). Sem pico significa um problema com o contato ou o par:

<img src="../../docs/img/sim1-sweep-contacts.png" width="720">

**Por que 4 transdutores Langevin, não 2.** Sob Q≈40, um desajuste de ressonância de 1,5 kHz dentro do par cai a potência do modelo ~10×:

<img src="../../docs/img/sim2-pair-mismatch.png" width="720">

**Estágio 3 — dados.** OOK atinge o anelamento do ressonador (modelo Q~40 → τ≈0,3 ms): 1 kbit/s é limpo, em 5 kbit/s o olho está fechado. Ir mais rápido leva ao modo B:

<img src="../../docs/img/sim5-ook-datarate.png" width="720">

**Orçamento de energia do receptor.** Bandas sombreadas são **metas** (modo A 0,5–5 W se o estágio 2 aterrissa; modo B menor). Cargas reais de primeira linha são ESP32 / BLE / LED com ciclo de trabalho; Wi-Fi é mostrado como um marcador de pico de tração, não uma promessa contínua:

<img src="../../docs/img/sim4-power-budget.png" width="720">

**Para mais tarde (modo B).** A placa se torna transparente em uma combinação de ressonâncias de espessura — a frequência precisa ser rastreada:

<img src="../../docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ Segurança — leia antes do primeiro power-up</b> — <a href="../../docs/02-safety.md">docs/02-safety.md</a></summary>

1. **Dezenas a centenas de volts no piezo** uma vez que o driver do estágio 2 esteja online — o TVS no lado de recebimento vai antes da primeira execução com energia; mantenha as mãos longe dos cabos.
2. **Mains** — apenas através de uma fonte de alimentação de bancada / isolamento; placas de driver de limpeza ultrassônica estão galvanicamente ligadas à rede.
3. **Ouvidos** — em potência não trivial, operar transdutores pressionados contra metal; nunca execute ultrassom de alta potência sem uma estrutura.
4. **Calor** — um transdutor Langevin sem clamp superaquece em minutos a potência; clamp antes de aumentar a corrente (apenas breve aumento de corrente elétrica — veja o README do driver).
5. **Estilhaços** — piezocerâmico é quebradiço: um parafuso apertado demais ou um impacto significa estilhaços; use óculos de segurança para qualquer trabalho mecânico.

Primeiro power-up do driver: limite de corrente da fonte de alimentação de bancada 0,2 A; sequência completa em [hardware/driver/](../../hardware/driver/README.md) e [docs/02-safety.md](../../docs/02-safety.md).

</details>

<details>
<summary><b>🧭 Arte anterior e higiene de patente</b> — <a href="../../docs/01-prior-art.md">docs/01-prior-art.md</a></summary>

Toda decisão técnica deve remontar a uma fonte "livre" (patentes expiradas, artigos). A fundação: **US5982297** (Aerospace Corp — a receita básica para um par de piezo de parede), **US7902943** (Caltech/JPL — feed-through de Sherrit), **US9361877** (Univ. Oklahoma — um sistema de transceptor completo); todos mortos. Artigos-chave: Lawry 2013 (50 W + 12,4 Mbit/s através de 63,5 mm de aço), Sherrit/NASA (uma lâmpada de 100 W), Yang 2015 (pesquisa).

Não copiar enquanto ainda vivo (US-only, até ~2032; estágios 1–4 não precisam): alocação de OFDM da RPI, esquema de duplex completo da RPI, transdutores conformais da Drexel.

Decisões de arquitetura são registradas em [docs/decisions/](../../docs/decisions/0001-frequency-mode-choice.md) (ADR).

</details>

<details>
<summary><b>🔌 Hardware e firmware</b> — hardware/, firmware/</summary>

- [hardware/bom/bom-stage1.csv](../../hardware/bom/bom-stage1.csv) — lista de compras do estágio 1.
- [hardware/schematics/](../../hardware/schematics/README.md) — **esquemas de circuito** (gerados a partir do código): driver, receptor, pinout do Pi, nó do harvestor.
- [hardware/driver/](../../hardware/driver/README.md) — driver TX: IR2110 half-bridge + 2×IRF540, transformador de acoplamento (um transdutor Langevin é uma carga capacitiva!). Placa KiCad vem após o protótipo de breadboard verificar.
- [hardware/receiver/](../../hardware/receiver/README.md) — receptor, estágio a estágio: ponte Schottky → ADC (estágio 1) → carregador (estágio 2) → LTC3588 + supercapacitor + ESP32 (estágio 4).
- [firmware/node-esp32/](../../firmware/node-esp32/README.md) — nó do estágio 4 (stub): sono profundo, leitura do sensor, publicidade BLE, orçamento de 1–5 mW médio.

</details>

<details>
<summary><b>💻 Software: medições e o simulador</b> — software/</summary>

- [software/sweep-map/sweep_map.py](../../software/sweep-map/sweep_map.py) — o cavalo de batalha do estágio 1: varredura DDS → leituras ADC → CSV + plot de resposta de frequência. Tem `--mock` para uma execução sem hardware. No Pi: `raspi-config` → habilitar SPI e I2C; `pip install spidev smbus2 matplotlib`.
- [software/simulator/channel_sim.py](../../software/simulator/channel_sim.py) — gerador de gráficos de expectativa (`pip install numpy matplotlib`).
- [data/](../../data/README.md) — logs brutos; CSV/PNG ficam fora do git, apenas plots curados vão para o git dentro do diretório do experimento.

</details>

<details>
<summary><b>🗺️ Onde aplicar isso: barreiras, canais, nichos</b> — [docs/04-hybrid-channels.md](../../docs/04-hybrid-channels.md), <a href="../../docs/05-applications-map.md">docs/05</a></summary>

Não há um canal universal — a plataforma combina a física com a barreira: piezo-acústica (primária: aço/alumínio com contato — watts e kbit/s), EMAT (metal sujo/quente, sem contato — dados), magnetismo de baixa frequência (paredes de dewars com areia de vácuo — bits/s). Fim honesto: paredes revestidas de borracha/compostas, líquido borbulhante no caminho.

Prioridade de nicho: **(1)** câmaras de vácuo e criostatos de laboratório — o público de hardware de código aberto, sem certificações; **(2)** tanques de fermentação — um campo de provas dentro do alcance da caminhada; **(3)** pacotes de bateria selados — o caso de bandeira (detecção de corrida térmica sem uma penetração no pacote). O protocolo de descoberta e auto-ajuste do receptor (um analógico Qi): [docs/03-discovery-protocol.md](../../docs/03-discovery-protocol.md).

</details>

<details>
<summary><b>📁 Layout do diretório</b></summary>

```
docs/            teoria, arte anterior, segurança, aplicações, log de decisões (ADR)
docs/img/        gráficos de expectativa (gerados por software/simulator/channel_sim.py)
hardware/        lista de materiais, driver (half-bridge), receptor (retificador/harvestor)
firmware/        firmware do nó (ESP32 — stub até o estágio 4)
software/        scripts de medição (varredura de mapa de resposta de frequência) e simulador de canal
experiments/     protocolos de experimento — do modelo, um diretório = um experimento
data/            logs brutos (arquivos grandes ficam fora do git)
```

</details>

## Princípios

1. **Reproduzibilidade a partir do zero.** Qualquer pessoa com um ferro de soldar e ~$210 pode reproduzir o resultado a partir deste repositório sozinho.
2. **Todo experimento é um protocolo.** Nenhum "funcionou mais ou menos": [experiments/TEMPLATE.md](../../experiments/TEMPLATE.md) é obrigatório.
3. **Higiene de patente.** Construímos sobre a camada expirada ([docs/01-prior-art.md](../../docs/01-prior-art.md)); decisões são registradas em [docs/decisions/](../../docs/decisions/0001-frequency-mode-choice.md).
4. **Medição primeiro, opinião segundo.** Uma varredura antes de qualquer conclusão sobre o canal.

## Licenças e patentes

Código — Apache-2.0, hardware — CERN-OHL-W v2, documentação — CC-BY-4.0; textos completos em [LICENSES/](../../LICENSES/). Qualquer pessoa pode bifurcar e construir sobre isso, comercialmente incluído; proteção de patente vem dos grants e cláusulas de retaliação nas licenças mais um esquema de publicação anterior. O esquema completo e o protocolo de publicação defensiva: [LICENSES.md](../../LICENSES.md); regras de contribuição: [CONTRIBUTING.md](../../CONTRIBUTING.md).
