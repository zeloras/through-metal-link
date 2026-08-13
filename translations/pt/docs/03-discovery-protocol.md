# Protocolo de descoberta e afinação automática do receptor (rascunho; implementação nas fases 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · Português · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

O objetivo: o dispositivo descobre sozinho se há um receptor atrás da parede, escolhe por conta própria a frequência e a potência, e não torra a parede à toa se alguém "esqueceu de soldar o receptor".

O modelo de referência são os carregadores Qi: eles resolvem exatamente esse problema (há um celular na bobina?) com exatamente essa sequência. Nosso análogo acústico:

## Fase 0 — ping analógico (o receptor pode estar totalmente descarregado)
O TX faz uma varredura de baixa potência pela banda e mede **sua própria corrente e fase** (shunt + detector de pico → ADS1115). Um receptor ressonante atrás da parede é uma carga acoplada ao TX através da parede: sua presença aparece como uma depressão/elevação característica na curva de impedância do TX, mesmo que tudo lá dentro esteja sem alimentação. Mesmo princípio de um detector de metais e do ping analógico do Qi.
- Assinatura presente → fase 1. Sem assinatura → "nenhum receptor encontrado", permanecer em ping de espera (uma vez a cada N segundos), não elevar a potência.
- Bônus: a curva de impedância da parede "vazia" é registrada na instalação como referência — assim conseguimos distinguir "sem receptor" de "receptor se soltou / desalinhou".

## Fase 1 — handshake digital
O TX estaciona na frequência candidata (o pico da fase 0) e entrega potência. O coletor do RX carrega o supercapacitor, o MCU acorda e responde com **modulação de carga**: um MOSFET curto-circuita periodicamente seu piezo seguindo um código (ID + versão do protocolo). O TX vê isso como modulação da sua própria corrente. Não é necessário nenhum transmissor lá dentro — trata-se de um esquema RFID, o mesmo da aplicação abandonada DOE/RPI US20100027379 (técnica anterior livre).

## Fase 2 — afinação por servo de frequência (perturba e observa)
O RX pode informar sua tensão de barramento (telemetria via modulação de carga). O TX varia ±Δf e mantém o máximo de potência recebida — um loop MPPT clássico. Isso compensa a deriva de ressonância com a temperatura (a principal pegadinha do nicho: ~6% de desvio = ~10× de queda de eficiência).

## Fase 3 — negociação de potência e watchdog
O RX solicita um nível (vivo / carregando / me dê mais), o TX limita a potência ao que foi solicitado. Respostas ausentes por M ciclos → o TX retorna à fase 0 em baixa potência.

## Hardware necessário para isso (item 12 da BOM, esquema — hardware/schematics/sch4)
- TX: shunt de 0,1 Ω + retificador/detector de pico no segundo canal do ADS1115 (corrente), opcionalmente um comparador de fase.
- RX: 2N7002 + ~100 Ω no **lado DC** do retificador (o pino VIN do módulo LTC3588) + GPIO — a carga é comutada depois da ponte, e o TX vê isso como modulação da sua própria corrente. Um único MOSFET através do piezo AC não funciona (o diodo de corpo desvia meio ciclo, o gate não tem referência num nó flutuante); a variante através do piezo só funciona com um par de MOSFETs em série frente a frente.

## Limites
O ping analógico enfraquece à medida que a espessura da parede e as perdas de contato aumentam (a assinatura se afoga no ruído) — o limiar de detecção deve ser medido num experimento dedicado (experiments/). Para paredes grossas, a alternativa: o RX, assim que acumula carga, "bate" periodicamente com um sinal próprio.
