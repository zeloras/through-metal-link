# Protocolo de descoberta e auto-ajuste do receptor (esboço; implementação em estágios 2–4)

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · Português · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · [中文](../../zh/docs/03-discovery-protocol.md) · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

O objetivo: o dispositivo descobre sozinho se há um receptor atrás da parede, escolhe a frequência e a potência sozinho e não aquece a parede em vão se alguém "esqueceu de soldar o receptor".

O modelo de referência é o carregador Qi: eles resolvem exatamente esse problema (há um telefone no coil?) com exatamente essa sequência. Nosso análogo acústico:

## Fase 0 — ping analógico (o receptor pode estar completamente descarregado)
O TX executa uma varredura de baixa potência na faixa e mede **sua própria corrente e fase** (shunt + detector de pico → ADS1115). Um receptor resonante atrás da parede é uma carga acoplada ao TX através da parede: sua presença aparece como um característico dip/bump na curva de impedância do TX, mesmo se tudo dentro estiver desligado. Mesmo princípio que um detector de metal e o ping analógico do Qi.
- Assinatura presente → fase 1. Sem assinatura → "receptor não encontrado", permanece em ping de espera (uma vez a cada N segundos), não aumente a potência.
- Bônus: a curva de impedância da "parede vazia" é registrada no momento da instalação como referência — então podemos distinguir "sem receptor" de "receptor se soltou / foi mal alinhado".

## Fase 1 — aperto de mãos digital
O TX se estabelece na frequência candidata (o pico da fase 0) e entrega potência. O harvester do RX carrega o supercapacitor, o MCU acorda e responde com **modulação de carga**: um MOSFET periodicamente curta seu piezo seguindo um código (ID + versão do protocolo). O TX vê isso como modulação de sua própria corrente. Nenhum transmissor é necessário dentro — isso é um esquema RFID, o mesmo que na aplicação abandonada DOE/RPI US20100027379 (arte priori gratuita).

## Fase 2 — ajuste de servo de frequência (perturbar e observar)
O RX pode relatar sua tensão de barramento (telemetria sobre modulação de carga). O TX dá passos ±Δf e mantém o máximo de potência recebida — um loop MPPT clássico. Isso fecha o drift de ressonância com a temperatura (o principal problema da niche: um shift de ~6% = ~10× queda de eficiência).

## Fase 3 — negociação de potência e watchdog
O RX solicita um nível (vivo / carregando / me dê mais), o TX limita a potência ao que foi solicitado. Respostas ausentes por M ciclos → o TX volta à fase 0 com baixa potência.

## Hardware necessário (item 12 do BOM, esquemático — hardware/schematics/sch4)
- TX: shunt 0,1 Ω + retificador/detector de pico no segundo canal do ADS1115 (corrente), opcionalmente um comparador de fase.
- RX: 2N7002 + ~100 Ω no **lado DC** do retificador (o pino VIN do módulo LTC3588) + GPIO — a carga é comutada após a ponte, e o TX a vê como modulação de sua própria corrente. Um único MOSFET através do piezo AC não funciona (o diodo do corpo shunta uma meia-onda, o portão não tem referência em um nó flutuante); a variante através do piezo só funciona com um par de MOSFETs em série de costas.

## Limites
O ping analógico enfraquece à medida que a espessura da parede e as perdas de contato crescem (a assinatura se afoga no ruído) — o limiar de detecção deve ser medido em um experimento dedicado (experiments/). Para paredes grossas, o fallback: o RX, uma vez que tenha armazenado carga, periodicamente "bate" com um farol próprio.
