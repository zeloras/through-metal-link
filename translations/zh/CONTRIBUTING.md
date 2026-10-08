# 如何贡献

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · 中文 · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

感谢你愿意推动这个开放穿透钢壁通道的发展。以下三条规则并非官僚主义——它们是本项目的专利护甲（原因详见 [LICENSES.md](LICENSES.md)）。

## 1. 贡献许可（入站 = 出站）

提交贡献即表示你同意，该贡献按照其所在目录中其余材料相同的许可方式获得授权：

- `software/`、`firmware/` → Apache-2.0；
- `hardware/` → CERN-OHL-W v2；
- `docs/`、`experiments/` → CC-BY-4.0。

**专利授权。** 此外——由于 CC-BY-4.0 不涉及专利授权——你向本项目及其所有材料接收方授予一项永久、不可撤销、全球范围、免版税、非独占的专利许可，以制造、委托制造、使用、要约销售、销售、进口及以其他方式转让你的贡献，无论单独使用还是作为项目的一部分——授权范围以你的专利权利要求中因该贡献本身或其与所提交项目的组合而必然被侵犯的部分为限。条款遵循 Apache-2.0 第 3 条，无论贡献落入哪个目录。如果你对任何人提起专利诉讼（包括反诉），指控本项目的材料侵犯你的专利，则本项目及其贡献者根据本条款及项目许可授予你的所有**专利**许可，自该诉讼提起之日起终止。

## 2. DCO：来源签名

每个提交都附带一个 sign-off（`git commit -s`），表示你同意 [Developer Certificate of Origin 1.1](https://developercertificate.org/)：你确认你有权在项目许可下提交此贡献。

```
Signed-off-by: Firstname Lastname <email@example.com>
```

没有 sign-off 的 PR 不会被合并；检查是自动的——CI 任务 [.github/workflows/dco.yml](../../.github/workflows/dco.yml) 会在哪怕只有一个提交缺少 sign-off 时就让 PR 失败。文档层的专利保护恰恰依赖这条链——没有例外。

**在层之间移动材料。** 材料停留在它落入的层中（并受该层的许可约束）。在不同许可的层之间移动文本/代码，仅当材料为你本人所有，或附带该片段原始许可的明确说明时才被允许。

## 3. 专利规范与实验协议

- 每个技术决策都必须可追溯到一个免费来源——一份已过期的专利或一篇来自 [docs/01-prior-art.md](docs/01-prior-art.md) 的论文。有效权利要求的实现（同样列在那里）在那些权利要求过期之前不予接受。
- 实验结果——只能通过 [experiments/TEMPLATE.md](experiments/TEMPLATE.md) 模板提交：一份带日期、可复现的协议正是构成我们现有技术的东西。
- 架构决策通过 [docs/decisions/](docs/decisions/) 中的 ADR 进行。
- 代码注释、文档字符串、标识符和提交消息仅限英文。文档是多语言的（见下文）；用户可见的图标签位于 `labels.json`。

## 4. 多语言文档：编辑一种语言，CI 同步其余

英文是主语言并拥有规范路径。其他每种语言都是 [translations/](..) 下的镜像树，文件名相同——包括 markdown、BOM CSV 和生成的图表；图表文本由 `labels.json` 驱动。你**不必**手动维护镜像：

- 编辑你觉得方便的任何语言。推送时，[Translation sync](../../.github/workflows/translate.yml) 工作流会用一个开放权重 LLM（Ollama Cloud 上的 `glm-5.2`）翻译对应文件，在同步更新 `labels.json` 时重新生成图表，并以 `[translate-sync]` 标记提交结果。任何 OpenAI 兼容端点都可以——设置 `OPENAI_BASE_URL` 和 `TRANSLATE_MODEL`。
- 仍需处理的工作记录在 `translations/.sync-state.json` 中，它记录了每个翻译所基于的主内容。因此，因配额或超时而被截断的运行不会丢失任何东西：未完成的配对保持过期状态，由下一次推送或夜间运行接续。不要手动编辑该文件。
- 如果你自行编辑了某个文档的**多种**语言，你触碰的每个版本都会按你写的保留；机器人只填充你没有触碰的语言。
- **`labels.json` 是"编辑任何语言"的例外。** 图标签仅从主语言流向镜像。编辑翻译后的标签只会修正该语言并止步于此；它不会回流到英文。要更改标签*说的内容*，请编辑主语言部分。原因是非对称性：标签编辑几乎总是有人在纠正机器的措辞，而让这种改写覆盖主语言会重新定义所有十四个镜像的生成源头。机器人从未生成过的键仍然会回传，因此手写的标签不会困在一种语言中。
- 机器翻译会被提交——浏览机器人的提交，如果语气不对就润色措辞；你的修改不会被覆盖（机器人会将你的版本记录为当前版本）。
- 如果回复被截断或 `labels.json` 占位符被弄乱，该回复会被丢弃而非提交，配对会被重试——因此镜像中出现的奇怪缺口是过期配对，而非有意为之。
- **外部 PR：** 机器人在 `master` 上运行，因此 PR 可以只更改一种语言——镜像（包括英文）会在合并后自动跟上。你不需要懂英文就能贡献文档。
- **添加语言：** 将其代码和名称添加到 [i18n.json](../../i18n.json)（例如 `"fr": "Français"`）并推送——流水线会构建整个 `translations/fr/` 镜像：每个文档、每个 `labels.json` 中的 `fr` 部分、图表集以及各处的语言切换器。
- **非拉丁文字：** CI 安装 Noto 字体系列（`fonts-noto-core`、`fonts-noto-cjk`），渲染器按 `i18n.json` → `render.fonts` 中的字体栈遍历，因此西里尔文、汉字、假名和谚文都能正确输出。渲染器现在在绘制前会检查字形覆盖，**宁可失败也不会画出 `.notdef` 方框**——这个检查之所以存在，是因为中文图表曾以一整片豆腐块的形式发布，而 CI 中没有任何东西检查像素。如果它触发了，请将该文字的 Noto 字体添加到栈中。
- **需要上下文成形的文字**——阿拉伯文和波斯文（RTL，连写形式）、天城文和孟加拉文（合字）——无法被 matplotlib 正确绘制，因为它没有成形引擎：即使字体正确，字形也会不连写且顺序错乱。请在 `i18n.json` → `render.skip_figures` 中列出这些语言。它们的正文不受影响；它们的文档只需链接到主语言的图表，[tools/translate_sync.py](../../tools/translate_sync.py) 中的链接修复会自动指向。`hi` 就是这样设置的。
- **文字守卫：** [tools/i18n_render.py](../../tools/i18n_render.py) 中的 `SCRIPTS` 记录了每种语言的标签必须包含的文字。如果回复中完全没有——`ja` 部分曾经被填满了俄文——则会被拒绝并重试，而非提交。该表中缺失的语言只是没有守卫，因此向 `i18n.json` 添加语言永远不会出问题；添加条目即可获得检查。

## 5. 推送前可以运行的检查

```bash
python tools/check_repo.py
```

验证翻译机器人可能破坏而其他工具无法捕获的内容：每个相对链接都能解析，每个 `labels.json` 部分与 `i18n.json` 匹配并携带与主语言部分相同的键和相同的 `str.format` 占位符，每个规范文档在每种语言中都有镜像，每个 markdown 文件都有其语言栏。CI 在两个工作流中都运行它；它不需要任何依赖。

CI 的其余部分（[ci.yml](../../.github/workflows/ci.yml)）编译脚本并运行整个图表流水线。要精确复现它——包括已提交的图表——请安装锁定的工具链，而非松散的：

```bash
python -m pip install -r tools/requirements-ci.txt
```
