# Mapa de aplicações: quem precisa desta stack de tecnologia, e por quê

> [English (primary)](../../../docs/05-applications-map.md) · [Русский](../../ru/docs/05-applications-map.md) · [Deutsch](../../de/docs/05-applications-map.md) · Português · [Español](../../es/docs/05-applications-map.md) · [Français](../../fr/docs/05-applications-map.md) · [Italiano](../../it/docs/05-applications-map.md) · [Polski](../../pl/docs/05-applications-map.md) · [Türkçe](../../tr/docs/05-applications-map.md) · [Українська](../../uk/docs/05-applications-map.md) · [Tiếng Việt](../../vi/docs/05-applications-map.md) · [中文](../../zh/docs/05-applications-map.md) · [日本語](../../ja/docs/05-applications-map.md) · [한국어](../../ko/docs/05-applications-map.md) · [हिन्दी](../../hi/docs/05-applications-map.md)

A stack da plataforma: um canal ativo de potência e dados através de paredes cegas — piezoacústica / EMAT / magnéticos de baixa frequência. Abaixo: onde isso é necessário no mundo real, quem já está lá, e o que sobra para nós.

## 1. Pacotes de baterias selados (VE, armazenamento de energia residencial/industrial)
- Dor: detecção precoce de fuga térmica — gases (CO₂, H₂, vapores de eletrólito) aparecem dentro do pacote minutos a horas antes de um incêndio; uma penetração de sensor no invólucro = perda de vedação hermética e de certificação.
- Nossa stack: um nó de gás/temperatura dentro do pacote, potência e telemetria via um par piezo através de 2–3 mm de alumínio. Zero furos.
- Quem já está lá: Liminal Insights — *diagnóstico acústico pelo lado de fora* (patentes sobre métodos de análise, não sobre o canal). Ninguém vende nós *dentro* do pacote.
- Maturidade do nicho: o mercado está crescendo explosivamente, a prateleira está vazia. Para a plataforma — aplicação de destaque nº 1.

## 2. Equipamentos de laboratório: câmaras de vácuo, criostatos, caixas de luvas
- Dor: cada passagem elétrica para dentro de uma câmara de vácuo é um flange que custa centenas de dólares e uma fonte de vazamentos; em um criostato, um cabo = vazamento de calor.
- Nossa stack: um sensor dentro da câmara, potência/dados por som através da parede de aço; para os sanduíches de vácuo de garrafas térmicas — magnéticos de baixa frequência (bit/s é mais que suficiente para um registrador de temperatura).
- Quem já está lá: ninguém com through-wall sem fio; laboratórios vivem de flanges de passagem.
- Maturidade: o nicho inicial ideal para código aberto — laboratórios são exatamente o público para hardware aberto (o caminho do TinyLev): eles compram sem certificações e te citam em artigos.

## 3. Produção de alimentos: tanques de fermentação, autoclaves (cerveja, vinho, laticínios)
- Dor: códigos sanitários odeiam penetrações (lavagem CIP, zonas mortas); você quer saber densidade/T/pressão dentro do tanque o tempo todo.
- Nossa stack: um nó na parede interna de um tanque de aço inoxidável, consultado pelo lado de fora com um scanner portátil ou um par fixo.
- Quem já está lá: sensores comuns rosqueados; sem soluções through-wall sem fio.
- Maturidade: literalmente ao alcance de um teste de garagem (qualquer cervejaria artesanal é um campo de prova a uma caminhada de distância).
- Ressalva física: um tanque cheio carrega a parede — refaça o sweep contra o vaso cheio, e mantenha potência contínua ≲1 W/cm²; acima disso, cavitação no produto (degaseificação de CO₂, off-flavors, erosão da parede a longo prazo) — [teoria](00-theory.md#efeito-na-parede-e-nos-meios-por-trás-dela).

## 4. Tubulações, vasos de pressão, NDT industrial
- Dor: monitorar corrosão/parâmetros internos sem shutdown ou penetração; superfícies estão quentes, pintadas, sujas.
- Nossa stack: uma "pistola scanner" EMAT — pressione contra um tubo sem preparação de superfície, leia um beacon ressonante passivo de dentro.
- Quem já está lá: medidores de fluxo ultrassônicos clamp-on e medidores de espessura (um mercado maduro), mas sem beacons interativos internos.
- Maturidade: médio alcance; requer o ramo EMAT (estágio ~6).

## 5. Petróleo & gás / downhole, e nuclear
- Quem já está lá: Metrol, Acoustic Data, Baker Hughes (downhole, 30 anos, modelo de serviço); P&D DOE/UNT/Westinghouse (cápsulas nucleares).
- Veredito honesto: ocupado e fortemente regulado — não vamos para lá, mas a própria existência deles = prova de que essa física vende por dinheiro sério. Usar como referência no README.

## 6. Logística marítima e estruturas subaquáticas
- Dor: "a carga está viva" em um contêiner selado; dados do lado interno do casco de um navio.
- Quem já está lá: CSignum (EM de baixa frequência através de água/anteparas) — o único vizinho direto em filosofia híbrida.
- Maturidade: longo alcance; para nós, por enquanto, apenas uma direção de pensamento.

## Prioridades (o que fazer, em que ordem)
1. **Agora:** estágios 1–4 da plataforma no cenário de destaque "câmara de laboratório / caixa soldada fechada" (nicho nº 2 — o mais aberto a código aberto).
2. **A seguir:** um demo em um objeto real do nicho nº 3 (um tanque de cervejaria) — barato, fotogênico, um usuário real.
3. **Médio alcance:** o cenário de bateria (nicho nº 1) como caso bandeira para publicação; o ramo EMAT para o nicho nº 4.

*Visão passiva (muon radiography) foi separada em um projeto próprio — veja muon-lab na base de conhecimento.*
