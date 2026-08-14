# 如何贡献

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · 中文 · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

感谢您愿意推动开放式穿钢通道的发展。以下三条规则并非繁文缛节——它们是本项目的专利护甲（原因详见 [LICENSES.md](LICENSES.md)）。

## 1. 贡献许可证（入站 = 出站）

提交贡献即表示您同意该贡献按照其所在目录中其余材料的相同许可方式进行授权：

- `software/`、`firmware/` → Apache-2.0；
- `hardware/` → CERN-OHL-W v2；
- `docs/`、`experiments/` → CC-BY-4.0。

**专利授权。** 此外——鉴于 CC-BY-4.0 不授予专利许可——您向本项目及其材料的所有接收方授予一项永久的、不可撤销的、全球范围的、免版税的、非独占的专利许可，允许其制造、委托制造、使用、许诺销售、销售、进口以及以其他方式转让您的贡献，无论是单独使用还是作为本项目的一部分使用——该许可的范围以您的专利权利要求中因该贡献本身或其与所提交项目的组合而必然被侵权的部分为限。无论贡献落入哪个目录，相关条款均遵循 Apache-2.0 第 3 条的规定。如果您对任何人提起专利诉讼（包括反诉），指控本项目的材料侵犯了您的专利，则本项目及其贡献者根据本条款及本项目许可协议授予您的所有**专利**许可，自该诉讼提起之日起终止。

## 2. DCO：关于来源的签名

Signed-off-by: Firstname Lastname <email@example.com>
```

没有 sign-off 的 PR 不会被合并；检查是全自动的——CI 任务 [.github/workflows/dco.yml](../../.github/workflows/dco.yml) 只要发现哪怕一个提交缺少 sign-off，就会让 PR 直接挂掉。文档层的专利保护正是依赖于这条链——没有例外。

**在层之间搬运材料。** 材料停留在它落地时所在的层（并受该层许可证约束）。在不同许可证的层之间移动文本/代码，仅当材料为你本人所有，或附带该片段原始许可证的明确说明时才被允许。

## 3. 专利规范与实验协议

- 每一项技术决策都必须可追溯到一个免费来源——一份已过期的专利或一篇来自 [docs/01-prior-art.md](docs/01-prior-art.md) 的论文。在相关专利权利到期之前，不接受对仍有效的权利要求（同样在该文件中列出）的实现。
- 实验结果——仅通过 [experiments/TEMPLATE.md](experiments/TEMPLATE.md) 模板提交：一份注明日期、可复现的实验方案正是构成我们现有技术（prior art）的关键所在。
- 架构决策须通过 [docs/decisions/](docs/decisions/) 中的 ADR（架构决策记录）进行。
- 代码注释、文档字符串、标识符和提交信息仅限英文。文档为多语言（见下文）；用户可见的图表标签存放在 `labels.json` 中。

## 4. 多语言文档：编辑一种语言，CI 同步其余语言

英语是主要语言并拥有规范路径。其他所有语言都是 [translations/](..) 下的镜像树，文件名完全相同——包括 markdown、BOM CSV 和生成的图表；图表文本由 `labels.json` 驱动。你**不**需要手动维护镜像：

- 用你觉得舒服的语言进行编辑。推送时，[Translation sync](../../.github/workflows/translate.yml) 工作流会使用开源权重 LLM（Ollama Cloud 上的 `glm-5.2`）翻译对应文件，当同步更新 `labels.json` 时重新生成图表，并使用 `[translate-sync]` 标记将结果提交回去。任何兼容 OpenAI 的端点都可以——设置 `OPENAI_BASE_URL` 和 `TRANSLATE_MODEL` 即可。
- 仍有待处理的工作记录在 `translations/.sync-state.json` 中，该文件记录了每次翻译所基于的主要语言内容。因此，因配额或超时而中断的运行不会丢失任何内容：未完成的配对仍被标记为过期，并在下一次推送或夜间运行时被拾取处理。请勿手动编辑该文件。
- 如果你亲自编辑了文档的**多种**语言，你修改过的每个版本都会按你的原样保留；机器人只会填充你未触及的语言。
- **`labels.json` 是“编辑任何语言”的例外。** 图表标签仅从主要语言流向镜像。编辑翻译后的标签只会修正该语言并到此为止；它不会回流到英语中。要更改标签的*内容*，请编辑主要语言部分。原因在于不对称性：标签编辑几乎总是某人在纠正机器的措辞，如果让它重写主要语言，就会重新定义所有十四个镜像的生成源。机器人从未生成过的键仍然会传播回去，因此手动编写的标签不会被困在一种语言中。
- 机器翻译会被提交——浏览机器人的提交并在语气不对时润色措辞；你的修改不会被覆盖（机器人会将你的版本记录为当前版本）。
- 如果返回的回复被截断或 `labels.json` 占位符被破坏，它将被丢弃而不是提交，并且该配对会被重试——因此，镜像中看起来奇怪的空缺是过期的配对，而不是有意为之的决定。
- **外部 PR：** 机器人在 `master` 上运行，因此 PR 可能只更改一种语言——镜像（包括英语）会在合并后立即自动同步。你不需要懂英语也可以为文档做贡献。
- **添加语言：** 将其代码和名称添加到 [i18n.json](../../i18n.json)（例如 `"fr": "Français"`）并推送——流水线会构建整个 `translations/fr/` 镜像：每个文档、每个 `labels.json` 中的 `fr` 部分、图表集以及各处的语言切换器。
- **非拉丁文字：** CI 安装了 Noto 字体系列（`fonts-noto-core`、`fonts-noto-cjk`），并且渲染器会遍历 `i18n.json` → `render.fonts` 中的字体栈，因此西里尔文、汉字、假名和韩文都能正确显示。渲染器现在在绘制前会检查字形覆盖范围，并且**宁可失败也不会绘制 `.notdef` 方块**——这个检查的存在是因为中文图表曾经以豆腐块网格的形式发布，而 CI 中没有任何东西会检查像素。如果它触发了，请将该文字的 Noto 字体添加到字体栈中。
- **需要上下文成形的文字**——阿拉伯文和波斯文（RTL，连写形式）、天城文和孟加拉文（连字）——无法被 matplotlib 正确绘制，因为它没有成形引擎：即使使用正确的字体，字形也会出现未连写和顺序错误的情况。在 `i18n.json` → `render.skip_figures` 中列出这些语言。它们的正文不受影响；它们的文档只需链接到主要语言的图表，[tools/translate_sync.py](../../tools/translate_sync.py) 中的链接修复会自动指向这些图表。`hi` 就是这样设置的。
- **文字防护：** [tools/i18n_render.py](../../tools/i18n_render.py) 中的 `SCRIPTS` 记录了每种语言的标签必须包含的文字。如果回复中不包含该文字——`ja` 部分曾经发布时充满了俄文——它将被拒绝并重试，而不是被提交。该表中缺失的语言只是没有防护，因此向 `i18n.json` 添加语言永远不会破坏现有功能；添加条目即可获得检查。

## 5. 推送前可运行的检查

python tools/check_repo.py
```

验证那些翻译机器人可能弄坏、而其他工具都抓不到的问题：每个相对链接都能解析，每个 `labels.json` 章节都与 `i18n.json` 匹配并携带与主文件相同的键和相同的 `str.format` 占位符，每个规范文档在每种语言中都有对应的镜像，每个 markdown 文件都带有语言栏。CI 在两个工作流中都会运行它；它不需要任何依赖。

CI 的其余部分（[ci.yml](../../.github/workflows/ci.yml)）会编译脚本并运行整个图表生成流程。要完全复现它——包括已提交的图表——请安装锁定的工具链，而非宽松的工具链：

```bash
python -m pip install -r tools/requirements-ci.txt
