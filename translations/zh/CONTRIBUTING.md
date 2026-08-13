# 贡献指南

> [English (primary)](../../CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md) · 中文 · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md)

感谢您愿意为开放的通过钢墙的通道做出贡献。以下三个规则不是官僚主义 —— 它们是项目的专利盾牌（请参阅 [LICENSES.md](../../LICENSES.md) 以了解原因）。

## 1. 贡献许可（入站 = 出站）

通过提交贡献，您同意它与其目录中的其他材料具有相同的许可：

- `software/`、`firmware/` → Apache-2.0；
- `hardware/` → CERN-OHL-W v2；
- `docs/`、`experiments/` → CC-BY-4.0。

**专利授权**。此外 —— 由于 CC-BY-4.0 不许可专利 —— 您授予项目及其所有接收者对您的贡献的永久、不可撤销、全球、免版税、非独占的专利许可，以制造、允许制造、使用、提供销售、销售、进口和转让您的贡献，无论是单独还是作为项目的一部分 —— 在您的专利权利要求必然被贡献本身或其与所提交项目的组合所侵犯的范围内。这些条款遵循 Apache-2.0 的 §3，无论贡献落在哪个目录中。如果您对任何人（包括反诉）提起专利诉讼，声称项目的材料侵犯您的专利，则您从项目及其贡献者获得的所有 **专利** 许可在诉讼提交日期终止。

## 2. DCO：签名的出处

每个提交都带有签署 (`git commit -s`)，表示同意 [开发者原创证书 1.1](https://developercertificate.org/)：您确认您有权在项目许可下提交此贡献。

```
Signed-off-by: Firstname Lastname <email@example.com>
```

没有签署的 PR 不会被合并；检查是自动的 —— CI 作业 [.github/workflows/dco.yml](../../.github/workflows/dco.yml) 如果提交缺少签署，则会失败 PR。文档层的专利保护正依赖于此链 —— 没有例外。

**在层之间移动材料**。材料生活在它落下的层（并在该层的许可下）。仅当它是您自己的材料或带有原始许可的明确说明时，才允许在具有不同许可的层之间移动文本/代码。

## 3. 专利卫生和实验协议

- 每个技术决策必须追溯到一个免费的来源 —— 一个过期的专利或 [docs/01-prior-art.md](../../docs/01-prior-art.md) 中的一篇论文。直到这些权利要求过期之前，不接受对活权利的实现。
- 实验结果 —— 仅通过 [experiments/TEMPLATE.md](../../experiments/TEMPLATE.md) 模板：一个有日期、可复制的协议正是构成了我们的先前艺术。
- 体系结构决策通过 [docs/decisions/](../../docs/decisions) 中的 ADR 进行。
- 代码注释、文档字符串、标识符和提交消息仅为英语。文档是多语言的（见下文）；用户可见的图形标签位于 `labels.json` 中。

## 4. 多语言文档：编辑一种语言，CI 同步其余语言

英语是主要语言，拥有规范路径。每种其他语言都是 [translations/](../) 下具有相同文件名的镜像树 —— 包括 markdown、BOM CSV 和生成的图形；图形文本由 `labels.json` 驱动。你不需要手动维护镜像：

- 编辑您感到舒适的语言。在推送时，[翻译同步](../../.github/workflows/translate.yml) 工作流使用开源权重 LLM（Ollama Cloud 上的 `glm-5.2`）翻译对应语言，更新 `labels.json` 时重新生成图形，并使用 `[translate-sync]` 标记将结果提交回去。任何 OpenAI 兼容的端点都可以 —— 设置 `OPENAI_BASE_URL` 和 `TRANSLATE_MODEL`。
- 仍然需要工作的内容在 `translations/.sync-state.json` 中跟踪，该文件记录了每个翻译所使用的主要内容。因此，中断的运行不会丢失任何内容：未完成的对将保持为过时状态，并将在下一次推送或每晚运行时被拾取。请勿手动编辑该文件。
- 如果您编辑了文档的 **多种** 语言，则您触摸的每个版本都将保持您编写的状态；机器人只填充您未触摸的语言。
- 提交机器翻译；如果机器人错过语气，请浏览机器人的提交并调整措辞；您的修复不会被覆盖（机器人将您的版本记录为当前版本）。
- 如果回复返回时被截断或具有损坏的 `labels.json` 占位符，则不会提交，而是重试该对 —— 因此，镜像中的奇怪间隙是过时的对，而不是决定。
- **外部 PR：** 机器人在 `master` 上运行，因此 PR 可能只更改一种语言 —— 镜像（包括英语）在合并后会自动跟上。您不需要知道英语才能贡献文档。
- **添加语言：** 将其代码和名称添加到 [i18n.json](../../i18n.json)（例如 `"fr": "Français"`），然后推送 —— 流水线将构建整个 `translations/fr/` 镜像：每个文档，`labels.json` 中的 `fr` 部分，图形集，以及每个地方的语言切换器。
- **非拉丁脚本（CJK 等）：** 图形渲染目前仅提供拉丁语 + 西里尔字体；在将例如日语添加到 i18n.json 之前，必须将 CJK 字体连接到渲染脚本 —— 请先打开一个问题。

## 5. 推送前可以运行的检查

```bash
python tools/check_repo.py
```

验证机器人翻译能够破坏的内容以及其他内容不会捕获：每个相对链接都可以解析，每个 `labels.json` 部分都与 `i18n.json` 匹配，并且具有相同的键和与主语言相同的 `str.format` 占位符，每个规范文档在每种语言中都有镜像，每个 markdown 文件都有语言栏。CI 在两个工作流中运行它；它不需要任何依赖项。

其余 CI ([ci.yml](../../.github/workflows/ci.yml)) 编译脚本并运行整个图形管道。要完全复制它，包括提交的图形 —— 安装固定工具链，而不是松散的工具链：

```bash
python -m pip install -r tools/requirements-ci.txt
