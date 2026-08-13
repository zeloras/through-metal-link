# Canais híbridos: barreira → física → números

> [English (primary)](../../../docs/04-hybrid-channels.md) · [Русский](../../ru/docs/04-hybrid-channels.md) · [Deutsch](../../de/docs/04-hybrid-channels.md) · Português · [Español](../../es/docs/04-hybrid-channels.md) · [Français](../../fr/docs/04-hybrid-channels.md) · [Italiano](../../it/docs/04-hybrid-channels.md) · [Polski](../../pl/docs/04-hybrid-channels.md) · [Türkçe](../../tr/docs/04-hybrid-channels.md) · [Українська](../../uk/docs/04-hybrid-channels.md) · [Tiếng Việt](../../vi/docs/04-hybrid-channels.md) · [中文](../../zh/docs/04-hybrid-channels.md) · [日本語](../../ja/docs/04-hybrid-channels.md) · [한국어](../../ko/docs/04-hybrid-channels.md) · [हिन्दी](../../hi/docs/04-hybrid-channels.md)

O princípio (um corolário do "paradoxo da penetração"): uma onda atravessa uma barreira exatamente na medida em que interage fracamente com ela — eis por que não existe um canal universal. A plataforma não persegue um único canal; para cada barreira ela escolhe a física à qual a barreira é transparente e para a qual o receptor é ressonantemente "ganancioso".

## Tabela de seleção de canais

| Barreira | Canal de trabalho | Esperado (ordens de grandeza) | Observações |
|---|---|---|---|
| Aço/alumínio 1–60 mm, contato possível | Piezoacústica (nosso principal) | watts; kbit/s (até Mbit/s em modo MHz) | exige contato acústico (acoplante de graxa/epóxi) |
| Metal: sujo, pintado, quente, contato indesejável | EMAT (magnéticos → som na parede) | mW; kbit/s; gap até ~3 mm | apenas paredes condutivas; dados, não potência |
| Parede ferromagnética sem piezo algum | Magnetostricção (uma bobina aciona o próprio aço) | migalhas; bit/s–kbit/s | ramo experimental, barato de testar |
| Parede dupla com vácuo (termo, criostato, dewar) | Magnéticos de baixa frequência (dezenas–centenas de Hz) | µW–mW; bit/s | efeito pelicular: no aço δ≈0,6 mm @1 kHz — empurre a frequência para baixo |
| Não-metal: vidro, plástico, cerâmica | Piezoacústica (mais fácil que metal) | watts; kbit/s | + RF simples muitas vezes passa também — verifique isso primeiro |
| Parede com camada de borracha/espuma, compósito | Sinceramente: quase um beco sem saída | — | o absorvedor devora tudo; a alternativa é um ponto sem revestimento |
| Líquido atrás da parede (tanque cheio) | Piezoacústica, degradada | potência − alguns dB; ressonância mais curta | o carregamento líquido desloca/amortece a ressonância — varredura de novo contra o vaso cheio; mantenha intensidade contínua ≲1 W/cm² para ficar abaixo da cavitação ([teoria](00-theory.md#effect-on-the-wall-and-the-media-behind-it)) |
| Líquido borbulhante no caminho acústico | Solução arquitetural | — | monte o receptor na parede, mantenha o líquido fora do caminho |

## Arquitetura do nó híbrido

- Camada de potência: par piezo em ressonância (estágios 1–4).
- Camada de dados sem contato: cabeça EMAT como uma "pistola scanner" destacável (estágio ~6).
- Camada de contingência: bobinas de baixa frequência para sanduíches de vácuo (quando a tarefa exige).
- O protocolo de descoberta (docs/03) se estende de "varredura sobre frequência" para "varredura sobre física": ping piezo → ping EMAT → ping LF; o nó escolhe o canal que passa por conta própria e relata qual barreira vê.

## Aplicações de exemplo por canal

1. **Pacotes de baterias seladas (EV/armazenamento):** sensor T/gás dentro de um encapsulado potting; potência+dados via par piezo através de 2–3 mm de alumínio. O mercado está em franca expansão, e uma penetração em um encapsulado de bateria = inferno de certificação.
2. **Criostato/dewar:** um logger de temperatura dentro, enviando um pacote de bits uma vez por minuto via magnéticos de baixa frequência através da jaqueta de vácuo. Fundamentalmente fora do alcance da acústica — é aqui que o híbrido é insubstituível.
3. **Duto/autoclave sob pressão:** um scanner EMAT pressionado contra um tubo quente pintado sem nenhuma preparação de superfície — lê um beacon ressonante passivo de dentro.
4. **Tanques de fermentação (cerveja/vinho, aço inoxidável):** sensor de densidade/T dentro do tanque sem uma única penetração — os códigos sanitários adoram a ausência de furos.
5. **Contêiner marítimo/cofre:** "a carga está viva" — um par piezo através de aço corrugado, consultado com um scanner portátil.

## Limitações que nenhuma camada resolve
Potência — apenas piezo de contato (EMAT e magnéticos de baixa frequência são ordens de grandeza mais fracos). Paredes compósitas/revestidas de borracha estão fora da plataforma. A velocidade do canal LF é bits por segundo — isso é telemetria, não streaming.
