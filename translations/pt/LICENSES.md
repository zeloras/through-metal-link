# Licenciamento e proteção de patentes

> [English (primary)](../../LICENSES.md) · [Русский](../ru/LICENSES.md) · [Deutsch](../de/LICENSES.md) · Português · [中文](../zh/LICENSES.md) · [日本語](../ja/LICENSES.md)

O objetivo deste esquema: o projeto é totalmente aberto, qualquer pessoa pode bifurcá-lo e construir sobre ele (inclusivamente comercialmente), enquanto o risco de litígio de patentes é reduzido ao mínimo alcançável por meios legais e procedimentais.

## O esquema (três camadas; textos completos em [LICENSES/](../../LICENSES))

| Área | Licença | Texto | Disposições de patente |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](../../LICENSES/Apache-2.0.txt) | §3: todo contribuidor concede automaticamente uma licença de patente para sua contribuição; ingressar com uma ação de patente e você perde a **licença de patente** (retaliação; a licença de direitos autorais em §2 é irrevogável e sobrevive à ação) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](../../LICENSES/CERN-OHL-W-2.0.txt) | §7.1: uma licença de patente (Fabricar / ter Fabricado / usar / vender / importar…) de cada licenciador — mas apenas para reivindicações necessariamente violadas pela Fonte Coberta dada; §7.2: uma ação de patente (incluindo uma tentativa de invalidar a patente de outra pessoa) termina **todos** os direitos sob a licença |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](../../LICENSES/CC-BY-4.0.txt) | concede **nenhum** direito de patente (§2(b)(2)) — a lacuna é fechada pela concessão explícita de patente em [CONTRIBUTING.md](CONTRIBUTING.md) |
| tudo o mais (raiz `README.md`, `QUICKSTART.md`, este arquivo, `data/`, etc.) | CC-BY-4.0 | — | fallback: nenhum arquivo no repositório é deixado "todos os direitos reservados" |

Os arquivos de código levam cabeçalhos SPDX (Apache-2.0); o mapa de cobertura legível por máquina é [REUSE.toml](../../REUSE.toml). A linha de direitos autorais vive em [NOTICE](../../NOTICE); a raiz [LICENSE](../../LICENSE) é um ponteiro para este esquema.

**Por que CERN-OHL-W, não S ou P.** W é o meio-termo: o design e suas modificações devem permanecer abertos em qualquer distribuição, mas o produto no qual o design é construído pode ser comercial e proprietário — o que mantém abertas as nichos de docs/05 (laboratórios, cervejarias, pacotes de bateria). S (copyleft forte) fecharia a porta para a incorporação; P (permissivo) permitiria bifurcações fechadas. O aperto em direção a S está incorporado à própria licença: §8.3 permite que qualquer pessoa trate material licenciado W como licenciado S (desde que a condição de Componentes Disponíveis seja atendida) — nenhuma permissão é necessária. O afrouxamento (em direção a P ou outra licença), por contraste, é possível apenas enquanto todo o material pertence a um único autor; após a primeira contribuição externa — apenas com o consentimento de todos os contribuidores.

**Nome do projeto.** "through-metal-link" não é uma marca registrada; as licenças em si não concedem direitos ao nome (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Referir-se ao projeto factualmente ("baseado em through-metal-link") é livre para qualquer pessoa; bifurcações com alterações incompatíveis são solicitadas a serem enviadas sob seu próprio nome.

## O que isso protege contra — e o que não protege (honestamente)

**Isso protege contra:**
1. **Ações de contribuidores.** Qualquer pessoa que tenha contribuído concedeu automaticamente suas patentes para essa contribuição (Apache §3, CERN-OHL §7.1, e CONTRIBUTING para docs). Uma ação custa caro ao autor: sob Apache-2.0 eles perdem as licenças de patente para o código; sob CERN-OHL-W eles perdem todos os direitos à camada de hardware (§7.2 — acionado mesmo por uma tentativa de desafiar a patente de outra pessoa).
2. **Privatização de bifurcações de hardware.** CERN-OHL-W obriga qualquer pessoa que distribua (Concessão de um produto ou de fontes) a publicar suas modificações de design — melhorias fluem de volta para a camada aberta e se tornam prior art. (Uma bifurcação de gaveta, nunca concedida a terceiros, não tem obrigação de publicação — mesmo sob qualquer copyleft.)
3. **Patentes futuras de outras pessoas.** Tudo publicado com uma data destrói a novidade para solicitações posteriores: para uma solução descrita aqui antes da data de depósito, uma patente válida não pode mais ser concedida. Contra solicitações depositadas *antes* de nossa publicação isso não funciona — para essas, o único escudo é a camada de patentes expiradas (veja abaixo).

**Isso não protege contra:**
- **Patentes de terceiros que já existem.** Nenhuma licença pode fazer isso. O que funciona contra elas é a disciplina de engenharia de docs/01-prior-art.md: construir apenas a partir da camada expirada (domínio público), não implementar reivindicações vivas (RPI OFDM/full-duplex, Drexel — até ~2032, apenas EUA), e rastrear cada decisão de design até uma fonte livre. Isso não é uma garantia, mas é exatamente a prática que torna uma ação judicial fútil.
- Uma bifurcação destinada à produção comercial faz sua própria análise de FTO (liberdade para operar) para sua própria jurisdição e design — o repositório não faz representações de patente (disclaimers em todas as três licenças).

## Protocolo de publicação defensiva (executar quando o repositório for público)

Todo resultado publicado é uma prior art datada que bloqueia todas as solicitações de terceiros posteriores para a mesma solução:

1. Abra o repositório com todo o histórico do git (commits = carimbos de data/hora).
2. Snapshot para **Zenodo** → DOI: um arquivo independente com uma data legalmente significativa, citável em artigos.
3. Prenda-o em **Software Heritage** (archive.softwareheritage.org — um espelho perpétuo).
4. Cada experimento concluído `experiments/NNN` — com uma data, números e gráficos: isso é a publicação de uma solução técnica específica.
5. Marcos importantes (primeiros watts, primeiro nó) — um texto no mundo (Hackaday.io / arXiv / blog): quanto mais amplo a disseminação, mais forte o status de prior art.

## Para contribuidores

As regras vivem em [CONTRIBUTING.md](CONTRIBUTING.md): DCO sign-off, inbound=outbound, uma concessão explícita de patente em cada contribuição independentemente do diretório, rastreabilidade de decisões de design para prior art livre.

Até que ele abra, o repositório permanece privado — publicar antes dos primeiros resultados reprodutíveis enfraqueceria tanto a posição científica quanto a de patente.
