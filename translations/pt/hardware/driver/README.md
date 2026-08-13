# Driver (estágio 2): meio-ponte IR2110

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · Português · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · [中文](../../../zh/hardware/driver/README.md) · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**Esquemático:** [../schematics/sch1-driver-halfbridge.png](../schematics/sch1-driver-halfbridge.png) (gerado por [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

A cadeia: Pi (SPI) → AD9833 **em modo onda quadrada** (bit OPBITEN: MSB roteado para a saída, swing rail-to-rail — sem comparador separado necessário) → **74HC14 + RC + 1N4148** modelador de pulsos (HIN/LIN complementares com ~1 µs de tempo morto) → IR2110 → 2×IRF540 (meio-ponte) → capacitor de bloqueio DC de 1 µF → transformador de casamento (núcleo de ferrite, ~1:3..1:5, ajuste na bancada) → transdutor Langevin TX.

A saída senoidal do AD9833 (~0,6 Vpp) não serve para a lógica do IR2110 — se por algum motivo você precisar especificamente de uma senoide na saída do DDS, coloque um comparador entre eles (ex.: LM393, não está na BOM).

Alimentação do estágio de potência: fonte de bancada 12–24 V com limite de corrente (**comece em 0,2 A**).

Nota: a varredura do estágio 1 aciona o piezo diretamente com a senoide fraca do DDS (~0,6 Vpp, veja `sweep_map.py`) — **este driver entra na cadeia apenas no estágio 2 (watts)**. Não espere ≥0,5 W da ligação do estágio 1 apenas com o DDS.

Notas:
- O transdutor Langevin é uma carga capacitiva (tipicamente alguns nF). Um indutor em série ou transformador de casamento é obrigatório; sem isso os MOSFETs dissipam a corrente reativa e queimam.
- **Transformador de casamento (o ponto de falha usual).** Comece com um toroide de ferrite pequeno (ex.: FT50-43 / similar), primário com algumas espiras, secundário ~3–5× isso, capacitor filme de bloqueio DC de 1 µF em série no primário. Ajuste para corrente mínima da fonte *na ressonância do estágio 1* com o TX **fixado à placa** e o RX carregado. A relação de espiras e a dispersão são empíricas — o esquemático as marca com `*` por um motivo. Registre as espiras finais no log de experimentos.
- **Tempo morto**: o IR2110 não o gera por conta própria. A opção com componentes discretos — RC+1N4148 nas entradas do 74HC14 (atrasa apenas as bordas de subida, ~1 µs; com um período de 25 µs a 40 kHz isso é <5% de perda). A opção fácil — um módulo EGS002, tudo já embutido.
- **Lógica 3,3 V**: alimente o VDD do IR2110 com os mesmos 3,3 V do AD9833 e do 74HC14 — em VDD=5 V o limiar VIH é ≈ 3,1 V e uma onda quadrada de 3,3 V mal passa (o datasheet permite VDD até 3,3 V).
- **Desacoplamento é obrigatório**: 100 nF no VDD e VCC (VCC — mais 47 µF), e no trilho de potência 470–1000 µF + 100 nF cerâmico bem nos braços do meio-ponte — sem isso, um meio-ponte em jumpers de protoboard capta seus próprios picos de comutação. Mantenha os fios do laço de potência curtos; se o nó de comutação oscilar muito, saia da protoboard para uma placa de cobre (dead-bug / protoboard com plano de terra) antes de aumentar a corrente.
- **Sequência de primeiro energização** (alinhada com [docs/02-safety.md](../../docs/02-safety.md)):
  1. Sem o Langevin no secundário ainda. Fonte = 12 V, limite de corrente 0,2 A. Observe o acionamento do gate (HIN/LIN) e o nó de comutação no osciloscópio — confirme o tempo morto e a ausência de shoot-through.
  2. Instale o transformador de casamento + TX Langevin **fixado à placa de aço** (ou um bloco metálico espesso de sacrifício). Ainda com limite de 0,2 A. Suba na frequência de pico do estágio 1 apenas pelo tempo suficiente para ver a corrente e a tensão no RX.
  3. Aumente o limite de corrente gradualmente enquanto monitora a temperatura dos MOSFETs e do transformador. Nunca deixe um Langevin solto em potência — operações em potência total ao ar livre é como cerâmicas racham e drivers morrem.

TODO: projeto KiCad (PCB) assim que o protótipo em protoboard (ou dead-bug) for validado. Até então, os esquemáticos em [`../schematics/`](../schematics/) são a fonte de verdade do projeto.
