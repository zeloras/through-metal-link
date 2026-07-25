# Experimento 001: Mapa de Varredura do Canal, Aço 3 mm (PLANEJADO)

> [English (primary)](../../../../experiments/001-sweep-map-3mm-steel/README.md) · [Русский](../../../ru/experiments/001-sweep-map-3mm-steel/README.md) · [Deutsch](../../../de/experiments/001-sweep-map-3mm-steel/README.md) · Português

- Objetivo: encontrar a ressonância de um par de transdutores Langevin através de uma placa de 3 mm; obter a primeira resposta de frequência do canal.
- Hipótese: um pico em torno de 38-42 kHz (ressonância do transdutor Langevin), largura do pico de alguns kHz.
- Procedimento: software/sweep-map/sweep_map.py --start 25000 --stop 45000 --step 50
- Critério de sucesso: um pico reprodutível (duas varreduras consecutivas, desvio do centro <200 Hz).
- Medição bônus: a mesma varredura com "contato com couplante de graxa + clamp" versus "pressão seca" — o primeiro par de pontos de dados que não existem na literatura aberta.
