# Como Contribuir

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · Português · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md)

Obrigado por querer avançar o canal aberto através do aço. As três regras abaixo não são burocracia — elas são a armadura de patente do projeto (veja [LICENSES.md](../../LICENSES.md) para saber por quê).

## 1. Licenças de contribuição (inbound = outbound)

Ao submeter uma contribuição, você concorda que ela é licenciada da mesma forma que o restante do material em seu diretório:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Concessão de patente.** Além disso — desde que CC-BY-4.0 não licencia patentes — você concede ao projeto e a todos os destinatários de seus materiais uma licença de patente perpétua, irrevogável, mundial, gratuita, não exclusiva para fabricar, ter fabricado, usar, oferecer para venda, vender, importar e transferir de outra forma sua contribuição, tanto por si só quanto como parte do projeto — na medida em que suas reivindicações de patente sejam necessariamente infringidas pela contribuição por si só ou por sua combinação com o projeto ao qual foi submetida. Os termos seguem §3 do Apache-2.0, independentemente do diretório em que a contribuição foi inserida. Se você instituir litígio de patente contra alguém (incluindo uma contrarreclamação) alegando que os materiais do projeto infringem sua patente, então todas as **licenças de patente** concedidas a você pelo projeto e seus contribuintes sob esta cláusula e sob as licenças do projeto são rescindidas a partir da data em que tal litígio é arquivado.

## 2. DCO: uma assinatura na provenança

Cada confirmação leva uma assinatura (`git commit -s`), significando concordância com o [Certificado de Origem do Desenvolvedor 1.1](https://developercertificate.org/): você confirma que tem o direito de submeter essa contribuição sob a licença do projeto.

```
Signed-off-by: Firstname Lastname <email@example.com>
```

PRs sem assinatura não são mesclados; a verificação é automática — o trabalho de CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) falha o PR se mesmo um único commit falta assinatura. A proteção de patente da camada de docs repousa exatamente nessa cadeia — sem exceções.

**Movendo material entre camadas.** O material vive na camada em que foi inserido (e sob a licença dessa camada). Mover texto/código entre camadas com licenças diferentes é permitido apenas se for seu próprio material, ou com uma nota explícita da licença original do fragmento.

## 3. Higiene de patente e protocolo de experimento

- Toda decisão técnica deve remontar a uma fonte gratuita — uma patente expirada ou um artigo de [docs/01-prior-art.md](../../docs/01-prior-art.md). Implementações de reivindicações ativas (listadas também) não são aceitas até que essas reivindicações expirem.
- Resultados experimentais — apenas por meio do modelo [experiments/TEMPLATE.md](../../experiments/TEMPLATE.md): um protocolo datado e reprodutível é exatamente o que constitui nossa prioridade.
- Decisões de arquitetura passam por ADRs em [docs/decisions/](../../docs/decisions).
- Comentários de código, docstrings, identificadores e mensagens de confirmação são apenas em inglês. Docs são multilíngues (veja abaixo); rótulos de figura visíveis ao usuário vivem em `labels.json`.

## 4. Docs multilíngues: edite uma língua, o CI sincroniza o resto

Inglês é primário e possui os caminhos canônicos. Cada outra língua é uma árvore de espelho sob [translations/](..) com nomes de arquivo idênticos — markdown, CSV de BOM e figuras geradas incluídas; o texto da figura é impulsionado por `labels.json`. Você **não** precisa manter os espelhos manualmente:

- Edite qualquer língua que seja confortável. Ao enviar, o fluxo de trabalho [Sincronização de tradução](../../.github/workflows/translate.yml) traduz os contrapartes com Modelos do GitHub (`meta/llama-3.3-70b-instruct`, sem chaves de API necessárias), regenera figuras quando a sincronização atualiza `labels.json` e comita o resultado de volta com o marcador `[translate-sync]`.
- O que ainda deve ser trabalhado é rastreado em `translations/.sync-state.json`, que registra o conteúdo primário de cada tradução feita. Uma execução interrompida por uma cota ou um tempo limite, portanto, não perde nada: os pares incompletos permanecem marcados como estale e são retomados pela próxima envio ou pela execução noturna. Não edite manualmente esse arquivo.
- Se você editou **várias** línguas de um doc por conta própria, cada versão que você tocou é mantida como você a escreveu; o bot apenas preenche as línguas que você não tocou.
- A tradução automática é commitada — verifique o commit do bot e toque no wording se ele perder o tom; sua correção não será sobrescrita (o bot registra sua versão como a atual).
- Uma resposta que retornou truncada ou com espaços reservados `labels.json` misturados é descartada em vez de commitada, e o par é retried — então uma lacuna estranha em um espelho é um par estale, não uma decisão.
- **PRs externos:** o bot é executado em `master`, então um PR pode alterar apenas uma língua — os espelhos (incluindo inglês) são atualizados automaticamente logo após a mesclagem. Você não precisa saber inglês para contribuir com docs.
- **Adicionar uma língua:** adicione seu código e nome a [i18n.json](../../i18n.json) (por exemplo, `"fr": "Français"`) e envie — o pipeline constrói o espelho completo `translations/fr/`: cada doc, uma seção `fr` em cada `labels.json`, o conjunto de figuras e os comutadores de idioma em todos os lugares.
- **Scripts não latinos (CJK etc.):** a renderização de figuras atualmente envia apenas fontes latinas + cirílicas; antes de adicionar, por exemplo, japonês a i18n.json, uma fonte CJK precisa ser conectada aos scripts de renderização — abra uma issue primeiro.

## 5. Verificações que você pode executar antes de enviar

```bash
python tools/check_repo.py
```

Verifica o que o bot de tradução é capaz de quebrar e nada mais seria capturado: cada link relativo resolve, cada seção `labels.json` corresponde a `i18n.json` e carrega as mesmas chaves e os mesmos espaços reservados `str.format` que o primário, cada doc canônico tem um espelho em cada língua, e cada arquivo markdown tem sua barra de idioma. O CI executa isso em ambos os fluxos de trabalho; ele não precisa de dependências.

O restante do CI ([ci.yml](../../.github/workflows/ci.yml)) compila os scripts e executa toda a pipeline de figuras. Para reproduzir exatamente — incluindo as figuras commitadas — instale a cadeia de ferramentas fixada, não a solta:

```bash
python -m pip install -r tools/requirements-ci.txt
