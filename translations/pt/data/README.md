# dados/

> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · [Deutsch](../../de/data/README.md) · Português

Registros de medição brutos: saída CSV e PNG do `software/sweep-map/sweep_map.py`.

- Os nomes dos arquivos carregam um carimbo de data e hora UTC: `sweep_25000-45000_20260801T120000Z.csv`.
- Arquivos CSV/PNG ficam fora do git (veja `.gitignore`) — eles são grandes e reproduzíveis; apenas os gráficos curados entram no git, copiados para o diretório do experimento correspondente `experiments/NNN-*/`.

Execuções no modo mock (`sweep_map.py --mock`) também escrevem aqui — esses arquivos podem ser excluídos a qualquer momento.
