# Mapa de aplicações: quem precisa dessa pilha de tecnologia e por quê

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · Português

A pilha de plataforma: um canal ativo de energia e dados através de paredes cegas — piezo-acústica / EMAT / magnética de baixa frequência. Abaixo: onde isso é necessário no mundo real, quem já está lá e o que resta para nós.

## 1. Pacotes de bateria selados (EV, armazenamento de energia caseira/industrial)
- Dor: detecção precoce de fuga térmica — gases (CO₂, H₂, vapores de eletrólito) aparecem dentro do pacote minutos a horas antes de um incêndio; uma penetração do sensor na embalagem = perda de vedação hermética e certificação.
- Nossa pilha: um nó de gás/temperatura dentro do pacote, alimentação e telemetria via um par piezo-elétrico através de 2–3 mm de alumínio. Zero furos.
- Quem já está lá: Liminal Insights — diagnósticos acústicos *de fora* (patentes sobre métodos de análise, não sobre o canal). Ninguém vende nós *dentro* do pacote.
- Maturidade da nicho: o mercado está crescendo explosivamente, a prateleira está vazia. Para a plataforma — aplicação de demonstração #1.

## 2. Equipamentos de laboratório: câmaras de vácuo, criostatos, caixas de luvas
- Dor: cada alimentação elétrica para uma câmara de vácuo é uma flange que vale centenas de dólares e uma fonte de vazamentos; em um criostato, um cabo = vazamento de calor.
- Nossa pilha: um sensor dentro da câmara, alimentação/dados por som através da parede de aço; para os sanduíches de vácuo de dewars — magnética de baixa frequência (bit/s é suficiente para um registrador de temperatura).
- Quem já está lá: ninguém com sem fio através da parede; laboratórios vivem em flanges de alimentação.
- Maturidade: a nicho ideal para iniciar o open source — laboratórios são exatamente o público para hardware de código aberto (o caminho TinyLev): eles compram sem certificações e citam você em artigos.

## 3. Produção de alimentos: tanques de fermentação, autoclaves (cerveja, vinho, laticínios)
- Dor: códigos sanitários odeiam penetrações (lavagem CIP, zonas mortas); você quer saber densidade/T/pressão dentro do tanque a todo momento.
- Nossa pilha: um nó na parede interna de um tanque de aço inoxidável, sondado de fora com um scanner portátil ou um par fixo.
- Quem já está lá: sensores comuns conectados; nenhuma solução sem fio através da parede.
- Maturidade: literalmente ao alcance de um teste de garagem (qualquer cervejaria artesanal é um campo de teste dentro do alcance de uma caminhada).

## 4. Gasodutos, vasos de pressão, NDT industrial
- Dor: monitoramento de corrosão/parâmetros dentro sem uma parada ou uma penetração; superfícies são quentes, pintadas, sujas.
- Nossa pilha: uma "pistola de scanner" EMAT — pressione-a contra um tubo com zero preparação de superfície, leia um beacon resonante passivo de dentro.
- Quem já está lá: medidores de fluxo ultrassônicos de fixação e medidores de espessura (um mercado maduro), mas nenhum beacon interativo dentro.
- Maturidade: meio alcance; requer o ramo EMAT (etapa ~6).

## 5. Petróleo & gás / downhole e nuclear
- Quem já está lá: Metrol, Acoustic Data, Baker Hughes (downhole, 30 anos, modelo de serviço); DOE/UNT/Westinghouse R&D (canisters nucleares).
- Veredito honesto: ocupado e fortemente regulamentado — não vamos lá, mas sua existência = prova de que essa física vende por dinheiro sério. Use como referência no README.

## 6. Logística marítima e estruturas subaquáticas
- Dor: "o cargo está vivo" em um contêiner selado; dados do lado interno da casca de um navio.
- Quem já está lá: CSignum (EM de baixa frequência através de água/bulkheads) — o único vizinho direto na filosofia híbrida.
- Maturidade: longo alcance; para nós, por enquanto, apenas uma direção de pensamento.

## Prioridades (o que fazer, em que ordem)
1. **Agora:** etapas 1–4 da plataforma no cenário de demonstração "câmara de laboratório / caixa fechada" (nicho #2 — o mais aberto ao open source).
2. **Próximo:** uma demonstração em um objeto vivo do nicho #3 (um tanque de cervejaria) — barato, fotogênico, um usuário real.
3. **Meio alcance:** o cenário de bateria (nicho #1) como o caso de publicação de bandeira; o ramo EMAT para o nicho #4.

*Visão passiva (radiografia de muão) foi separada em um projeto separado — veja muon-lab na base de conhecimento.*
