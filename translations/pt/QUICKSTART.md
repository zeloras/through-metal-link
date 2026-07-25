# INÍCIO RÁPIDO: do zero absoluto ao estágio 1–2 do teste do conjunto

> [English (primary)](../../QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · Português

Cenário: você tem nada além de uma mesa e algum dinheiro. Tudo abaixo o leva a um conjunto de trabalho — "mapa de varredura + primeiros watts através do aço". Os preços são aproximados, em USD.

## Cesta 1 — ferramentas (uma base para anos, ~$120)

| Item | Por que | Preço | Onde |
|---|---|---|---|
| Estação de solda (clon de T12) | tudo | 35–50 | Ali |
| Multímetro (classe AN8008/UT61) | tensões, continuidade, capacitância | 15–25 | Ali |
| Fonte de alimentação de bancada 30V/5A com limite de corrente | alimenta o driver; o limite de corrente é seu seguro contra MOSFETs queimados | 45–60 | Ali/local |
| Ajudantes, solda, fluxo, pincel de desoldagem, alicate de corte, alicate de ponta | as coisas pequenas que você não pode fazer sem | 15 | Ali/local |
| Fios Dupont + placa de prototipagem + tubo de calor | prototipagem | 8 | Ali |

## Cesta 2 — eletrônica do conjunto (~$70)

| Item | Qtde | Preço | Nota |
|---|---|---|---|
| Raspberry Pi (Zero 2 W é suficiente; 4/5 é mais confortável) + SD | 1 | 20–60 | o cérebro: varredura, logs, gráficos |
| Transdutor Langevin 40 kHz 50–60 W | **4** | 40 | compre 4 de UMA partida; vamos escolher o melhor par por varredura |
| Módulo AD9833 DDS | 2 | 8 | o segundo é um reserva |
| IR2110 + IRF540 ×4 (ou um módulo EGS002) | 1 conjunto | 10 | meio-ponte do driver |
| ADC ADS1115 | 2 | 4 | o Pi não tem ADC próprio |
| Toróide de ferrite + fio de arame magnético 0,5 mm | 2 | 4 | transformador de acoplamento |
| Ponte Schottky (SS14 ×8), supercapacitor 1F 5,5V ×2 | 1 | 4 | cadeia do receptor |
| TVS SMBJ5.0A ×3 + SMBJ15CA ×2 | 1 | 2 | proteção. NÃO DEVE SER ECONOMIZADO |
| Módulo GY-LTC3588 | 1 | 7 | colheitor (estágio 4, mas deixe que ele seja enviado agora) |
| Conjunto de resistores/capacitores, LEDs | 1 | 8 | se você não tem nada |
| Componentes passivos de suporte: UF4007, 74HC14, 1N4148, 2N7002 | 1 | 2 | centavos; lista completa — itens BOM 11–12 |

## Cesta 3 — mecânica (~$20, localmente)

Placa de aço 3 mm ~150×150 — 2 peças (metal yard / corte a laser); clampas F-style ×2; coulant de graxa espessa e consistente (graxa de lítio); epóxi; papel de lixa (para limpar a área de contato).

## Opcional, mas fortemente recomendado (~$90)

| Item | Por que | Preço |
|---|---|---|
| Osciloscópio USB/portátil (FNIRSI/Hantek, 2 canais; você não precisa de ≥40 MHz de largura de banda — 10 é suficiente) | veja a forma de onda no gate e no piezo; economiza dias de depuração do driver | 60–80 |
| ESP32 DevKit ×2 | estágio 4 (o nó atrás da parede) | 8 |

**Total: mínimo básico ~$210, confortável ~$300.** (Se você já tem um Pi, uma estação de solda e uma fonte de alimentação de bancada em seu estoque — subtraia ~$120.)

## Ordem de compra (o caminho crítico é o envio)

1. Hoje: cesta 2 da Ali (3–4 semanas de envio — é o caminho crítico) + o osciloscópio.
2. Esta semana: cestas 1 e 3 localmente.
3. Enquanto é enviado: `raspi-config` → SPI+I2C, execute `software/sweep-map/sweep_map.py --mock` sem hardware (canal sintético — toda a pipeline CSV+plot funciona em qualquer computador), leia docs/00–03, veja os gráficos de expectativa em docs/img e os esquemas em hardware/schematics (a construção do estágio 1 segue sch3 e sch2).

## O que você verá (simulador: software/simulator/channel_sim.py → docs/img)

- `sim0-rig-sketch.png` — o conjunto inteiro em um esboço.
- `sim1-sweep-contacts.png` — resposta de frequência de varredura: um pico estreito perto de ~40 kHz; graxa + clampa dá ~4× mais do que um encaixe seco e ~50× mais do que uma lacuna de ar. Sem pico — o problema é o contato ou o par, veja sim2.
- `sim2-pair-mismatch.png` — por que 4 transdutores Langevin e não 2: uma diferença de ressonância de 1,5 kHz dentro de um par diminui a potência 10×; a varredura escolhe o melhor par de 4.
- `sim3-thickness-comb.png` — para mais tarde (modo B, MHz): a placa é transparente como um comb de ressonâncias de espessura, então a frequência precisa ser rastreada.
- `sim4-power-budget.png` — watts de destino versus as cargas: modo A alimenta tudo até os picos Wi-Fi, modo B alimenta um ESP32 com um buffer de supercapacitor.
- `sim5-ook-datarate.png` — estágio 3: por que OOK em transdutores Langevin atinge ~1–2 kbit/s (tempo de queda do anel do ressonador τ≈0,3 ms), e por que isso é suficiente para um nó de sensor.

## Critérios para "o conjunto funciona"

1. Varredura 25–45 kHz em duas execuções consecutivas: o pico se reproduz dentro de <200 Hz.
2. Em ressonância, ≥0,5 W em uma carga resistiva através de 3 mm de aço.
3. O LED atrás da placa está aceso. Foto em experiments/001 — e o estágio é fechado.

Segurança antes da primeira ligação: docs/02-safety.md (TVS no receptor, limite de corrente da fonte de alimentação em 0,2 A, nunca drive um transdutor Langevin sem pressão de clampagem).
