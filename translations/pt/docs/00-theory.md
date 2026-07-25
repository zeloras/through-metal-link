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

## Orçamento de energia do receptor (aproximado)
LED 20 mW; ESP32 com ciclo de trabalho de 1–5 mW em média; pacote BLE ~150 mW pico — buffer: um supercapacitor de 1 F @ 3,3 V = 5,4 J ≈ 360 transmissões.
