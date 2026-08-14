# Como Contribuir

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · Português · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · [中文](../zh/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

Obrigado por querer avançar o canal aberto através de aço. As três regras abaixo não são burocracia — são a armadura de patentes do projeto (veja [LICENSES.md](LICENSES.md) para saber porquê).

## 1. Licenças de contribuição (entrada = saída)

Ao enviar uma contribuição, você concorda que ela é licenciada da mesma forma que o restante do material em seu diretório:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Concessão de patentes.** Adicionalmente — já que a CC-BY-4.0 não licencia patentes — você concede ao projeto e a todos os destinatários de seus materiais uma licença de patente perpétua, irrevogável, mundial, isenta de royalties, não exclusiva, para fabricar, mandar fabricar, usar, oferecer para venda, vender, importar e de outra forma transferir sua contribuição, tanto por si só quanto como parte do projeto — na medida em que suas reivindicações de patente sejam necessariamente infringidas pela contribuição por si só ou por sua combinação com o projeto ao qual foi enviada. Os termos seguem o §3 da Apache-2.0, independentemente do diretório em que a contribuição foi incluída. Se você instaurar litígio de patente contra qualquer pessoa (incluindo uma reconvenção) alegando que os materiais do projeto infringem sua patente, então todas as licenças de **patente** concedidas a você pelo projeto e seus colaboradores sob esta cláusula e sob as licenças do projeto terminam a partir da data em que tal litígio for ajuizado.

## 2. DCO: uma assinatura sobre a proveniência

Signed-off-by: Firstname Lastname <email@example.com>
```

PRs sem sign-off não são mergeados; a verificação é automática — o job de CI [.github/workflows/dco.yml](../../.github/workflows/dco.yml) reprova o PR se sequer um único commit não tiver sign-off. A proteção de patentes da camada de docs depende exatamente dessa cadeia — sem exceções.

**Movendo material entre camadas.** O material vive na camada em que pousou (e sob a licença dessa camada). Mover texto/código entre camadas com licenças diferentes só é permitido se for material seu, ou com uma nota explícita da licença original do fragmento.

## 3. Higiene de patentes e protocolo de experimentação

- Toda decisão técnica deve rastrear até uma fonte gratuita — uma patente expirada ou um artigo em [docs/01-prior-art.md](docs/01-prior-art.md). Implementações de reivindicações vigentes (listadas também lá) não são aceitas até que essas reivindicações expirem.
- Resultados experimentais — apenas via o modelo [experiments/TEMPLATE.md](experiments/TEMPLATE.md): um protocolo datado e reproduzível é precisamente o que constitui nosso estado da técnica.
- Decisões de arquitetura passam por ADRs em [docs/decisions/](docs/decisions/).
- Comentários de código, docstrings, identificadores e mensagens de commit são apenas em inglês. A documentação é multilíngue (veja abaixo); rótulos visíveis para o usuário em figuras ficam em `labels.json`.

## 4. Documentação multilíngue: edite um idioma, a CI sincroniza o restante

O inglês é o idioma principal e possui os caminhos canônicos. Todos os outros idiomas são árvores espelho sob [translations/](..) com nomes de arquivo idênticos — incluindo markdown, o CSV da BOM e as figuras geradas; o texto das figuras é controlado por `labels.json`. Você **não** precisa manter os espelhos manualmente:

- Edite o idioma com o qual se sentir confortável. No push, o workflow [Translation sync](../../.github/workflows/translate.yml) traduz as contrapartes com um LLM de pesos abertos (`glm-5.2` na Ollama Cloud), regenera as figuras quando a sincronização atualiza o `labels.json`, e faz o commit do resultado de volta com o marcador `[translate-sync]`. Qualquer endpoint compatível com OpenAI funciona — defina `OPENAI_BASE_URL` e `TRANSLATE_MODEL`.
- O que ainda deve trabalho é rastreado em `translations/.sync-state.json`, que registra o conteúdo principal a partir do qual cada tradução foi feita. Uma execução interrompida por cota ou tempo limite, portanto, não perde nada: os pares inacabados permanecem marcados como desatualizados e são retomados no próximo push ou na execução noturna. Não edite esse arquivo manualmente.
- Se você editou **vários** idiomas de um documento, todas as versões que você tocou serão mantidas como você as escreveu; o bot apenas preenche os idiomas que você não tocou.
- **`labels.json` é a exceção à regra de "edite qualquer idioma".** Os rótulos das figuras fluem apenas do principal → espelhos. Editar um rótulo traduzido corrige aquele idioma e para por aí; ele não volta para o inglês. Para mudar o que um rótulo *diz*, edite a seção principal. A razão é a assimetria: a edição de um rótulo é quase sempre alguém corrigindo a redação da máquina, e permitir que isso reescreva o principal redefiniria a fonte da qual todos os catorze espelhos são gerados. As chaves que o bot nunca produziu ainda se propagam de volta, então um rótulo escrito à mão não fica preso em um único idioma.
- A tradução automática é commitada — dê uma olhada no commit do bot e ajuste a redação se ela perder o tom; sua correção não será sobrescrita (o bot registra sua versão como a atual).
- Uma resposta que voltou truncada ou com placeholders do `labels.json` corrompidos é descartada em vez de commitada, e o par é tentado novamente — então uma lacuna estranha em um espelho é um par desatualizado, não uma decisão.
- **PRs externos:** o bot roda no `master`, então um PR pode alterar apenas um idioma — os espelhos (incluindo o inglês) se atualizam automaticamente logo após o merge. Você não precisa saber inglês para contribuir com a documentação.
- **Adicionando um idioma:** adicione seu código e nome ao [i18n.json](../../i18n.json) (ex.: `"fr": "Français"`) e faça o push — o pipeline constrói todo o espelho `translations/fr/`: todos os documentos, uma seção `fr` em cada `labels.json`, o conjunto de figuras e os seletores de idioma em todos os lugares.
- **Scripts não latinos:** o CI instala as famílias Noto (`fonts-noto-core`, `fonts-noto-cjk`) e os renderizadores percorrem a pilha de fontes em `i18n.json` → `render.fonts`, então cirílico, Han, kana e Hangul saem corretamente. Um renderizador agora verifica a cobertura de glifos antes de desenhar e **falha em vez de pintar caixas `.notdef`** — essa verificação existe porque as figuras em chinês foram entregues como uma grade de tofu e nada no CI olha para os pixels. Se disparar, adicione a fonte Noto para esse script à pilha.
- **Scripts que precisam de modelagem contextual** — Árabe e Persa (RTL, formas unidas), Devanágari e Bengali (conjuntos) — não podem ser desenhados corretamente pelo matplotlib, que não possui motor de modelagem: mesmo com a fonte certa, os glifos saem desconectados e fora de ordem. Liste esses idiomas em `i18n.json` → `render.skip_figures`. Sua prosa não é afetada; seus documentos simplesmente linkam para as figuras principais, para as quais a reparação de links em [tools/translate_sync.py](../../tools/translate_sync.py) aponta automaticamente. O `hi` está configurado assim.
- **Guarda de script:** `SCRIPTS` em [tools/i18n_render.py](../../tools/i18n_render.py) registra qual script os rótulos de cada idioma devem conter. Uma resposta que não tem nenhum — as seções `ja` uma vez foram entregues preenchidas com russo — é rejeitada e tentada novamente em vez de commitada. Um idioma ausente dessa tabela simplesmente não recebe guarda, então adicionar um ao `i18n.json` nunca quebra; adicione a entrada para obter a verificação.

## 5. Verificações que você pode executar antes de enviar

python tools/check_repo.py
```

Verifica aquilo que o bot de tradução é capaz de quebrar e que nada mais detectaria: todo link relativo resolve, toda seção de `labels.json` corresponde a `i18n.json` e carrega as mesmas chaves e os mesmos placeholders de `str.format` da versão principal, todo documento canônico tem um espelho em cada idioma, e todo arquivo markdown tem sua barra de idioma. O CI o executa em ambos os fluxos de trabalho; não precisa de dependências.

O restante do CI ([ci.yml](../../.github/workflows/ci.yml)) compila os scripts e executa todo o pipeline de figuras. Para reproduzi-lo exatamente — incluindo as figuras versionadas — instale a toolchain fixada, não a solta:

```bash
python -m pip install -r tools/requirements-ci.txt
