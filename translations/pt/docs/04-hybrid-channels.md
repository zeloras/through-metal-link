# Canais híbridos: barreira → física → números

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · Português · [Español](../../es/docs/04-hybrid-channels.md) · [Français](../../fr/docs/04-hybrid-channels.md) · [Italiano](../../it/docs/04-hybrid-channels.md) · [Polski](../../pl/docs/04-hybrid-channels.md) · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

O princípio (um corolário do "paradoxo de penetração"): uma onda passa por uma barreira exatamente na medida em que interage fracamente com ela — é por isso que não existe um canal universal. A plataforma não procura um canal único; para cada barreira, ela escolhe a física que a barreira é transparente e o receptor é ressonantemente "ganancioso" por.

## Tabela de seleção de canal

| Barreira | Canal de trabalho | Esperado (ordens de magnitude) | Notas |
|---|---|---|---|
| Aço/alumínio 1–60 mm, contato possível | Piezo-acústica (nossa primária) | watts; kbit/s (até Mbit/s no modo MHz) | precisa de contato acústico (couplante de graxa/epóxi) |
| Metal: sujo, pintado, quente, contato indesejável | EMAT (magnéticos → som na parede) | mW; kbit/s; lacuna de até ~3 mm | paredes condutoras apenas; dados, não potência |
| Parede ferromagnética sem piezo | Magnetostricção (uma bobina aciona o próprio aço) | migalhas; bit/s–kbit/s | ramo experimental, barato para testar |
| Parede dupla com vácuo (termos, criostato, dewar) | Magnéticos de baixa frequência (dezenas–centenas de Hz) | µW–mW; bit/s | efeito de pele: no aço δ≈0.6 mm @1 kHz — reduza a frequência |
| Não-metal: vidro, plástico, cerâmica | Piezo-acústica (mais fácil do que metal) | watts; kbit/s | + RF simples frequentemente passa também — verifique isso primeiro |
| Parede com uma camada de borracha/espuma, compósito | Honestamente: quase um beco sem saída | — | o absorvedor consome tudo; a solução é um local sem revestimento |
| Líquido atrás da parede (tanque cheio) | Piezo-acústica, degradada | potência − alguns dB; anelamento mais curto | carga líquida desloca/amortece a ressonância — faça uma varredura novamente contra o vaso cheio; mantenha a intensidade contínua ≲1 W/cm² para ficar abaixo da cavitação ([teoria](00-theory.md#efeito-na-parede-e-nos-meios-atrás-dela)) |
| Líquido borbulhante no caminho acústico | Solução arquitetônica | — | monte o receptor na parede, mantenha o líquido fora do caminho |

## Arquitetura de nó híbrido

- Camada de potência: par de piezo em ressonância (etapas 1–4).
- Camada de dados sem contato: cabeça EMAT como uma "pistola de scanner" destacável (etapa ~6).
- Camada de fallback: bobinas de baixa frequência para sanduíches de vácuo (quando a tarefa exigir).
- O protocolo de descoberta (docs/03) estende de "varredura sobre frequência" para "varredura sobre física": ping piezo → ping EMAT → ping LF; o nó escolhe o canal que passa sozinho e relata qual barreira ele vê.

## Aplicações de exemplo por canal

1. **Pacotes de bateria selados (EV/armazenamento):** Sensor T/gás dentro de um invólucro encapsulado; potência+dados via par de piezo através de 2–3 mm de alumínio. O mercado está em alta, e uma penetração em um invólucro de bateria = inferno de certificação.
2. **Criostato/dewar:** registrador de temperatura dentro, enviando um pacote de bits uma vez por minuto via magnéticos de baixa frequência através do jacket de vácuo. Fundamentalmente fora do alcance da acústica — é aqui que o híbrido é insubstituível.
3. **Tubo/autoclave sob pressão:** scanner EMAT pressionado contra um tubo quente pintado com zero preparação de superfície — lê um beacon ressonante passivo de dentro.
4. **Tanques de fermentação (cerveja/vinho, aço inoxidável):** sensor de densidade/T dentro do tanque sem uma única penetração — códigos sanitários amam a ausência de furos.
5. **Contêiner do mar/seguro:** "o cargo está vivo" — par de piezo através de aço corrugado, sondado com um scanner portátil.

## Limitações que nenhuma camada pode resolver
Potência — contato piezo apenas (EMAT e magnéticos de baixa frequência são ordens de magnitude mais fracos). Paredes compostas/revestidas com borracha estão fora da plataforma. Velocidade do canal de baixa frequência é bits por segundo — isso é telemetria, não transmissão.
