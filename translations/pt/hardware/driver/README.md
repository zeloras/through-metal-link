# Driver (stage 2): IR2110 half-bridge

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · Português

**Esquemático:** [../schematics/sch1-driver-halfbridge.png](../../../../hardware/schematics/sch1-driver-halfbridge.png) (gerado por [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py))

A cadeia: Pi (SPI) → AD9833 **no modo de onda quadrada** (bit OPBITEN: MSB encaminhado para a saída, swing de trilho a trilho — nenhum comparador separado necessário) → **74HC14 + RC + 1N4148** formador (complementar HIN/LIN com ~1 µs de tempo morto) → IR2110 → 2×IRF540 (ponte de meia-onda) → 1 µF capacitor de bloqueio CC → transformador de acoplamento (ferrite, ~1:3..1:5, ajuste para se encaixar) → transdutor Langevin TX.

A saída senoidal do AD9833 (~0,6 Vpp) não é boa para a lógica do IR2110 — se por algum motivo você precisar especificamente de uma saída senoidal do DDS, coloque um comparador entre eles (por exemplo, um LM393, não no BOM).

Alimentação da etapa de potência: fonte de alimentação de bancada de 12–24 V com limitação de corrente (inicie com 0,2 A!).

Nota: a varredura de etapa 1 aciona o piezo diretamente com a saída senoidal fraca do DDS (~0,6 Vpp, veja sweep_map.py) — o driver entra na cadeia na etapa 2 (watts).

Notas:
- O transdutor Langevin é uma carga capacitiva (nF); um indutor/servidor em série é obrigatório, caso contrário os MOSFETs cozinharam na corrente reativa.
- **Tempo morto**: o IR2110 não gera por conta própria. A opção de partes discretas — RC+1N4148 nas entradas do 74HC14 (atrasa apenas as bordas de subida, ~1 µs; com um período de 25 µs a 40 kHz isso é <5% de perda). A opção fácil — um módulo EGS002, tudo está construído lá.
- **Lógica 3,3 V**: alimente o VDD do IR2110 com os mesmos 3,3 V que o AD9833 e o 74HC14 — em VDD=5 V o limiar VIH é ≈ 3,1 V e uma onda quadrada de 3,3 V mal passa (o datasheet permite VDD até 3,3 V).
- **Desacoplamento é obrigatório**: 100 nF em VDD e VCC (VCC — mais 47 µF), e na trilha de alimentação 470–1000 µF + 100 nF cerâmico bem na perna da ponte de meia-onda — sem isso, uma ponte de meia-onda em jumpers de protoboard pega seus próprios spikes de comutação.
- Primeira alimentação: sem placa, transdutor Langevin no ar, potência mínima, verifique a forma de onda em um osciloscópio/ADC.

TODO: projeto KiCad (PCB) assim que o protótipo de protoboard for verificado.
