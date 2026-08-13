# 现有技术：我们站在谁的肩膀上

> [English (primary)](../../../docs/01-prior-art.md) · [Русский](../../ru/docs/01-prior-art.md) · [Deutsch](../../de/docs/01-prior-art.md) · [Português](../../pt/docs/01-prior-art.md) · [Español](../../es/docs/01-prior-art.md) · [Français](../../fr/docs/01-prior-art.md) · [Italiano](../../it/docs/01-prior-art.md) · [Polski](../../pl/docs/01-prior-art.md) · [Türkçe](../../tr/docs/01-prior-art.md) · [Українська](../../uk/docs/01-prior-art.md) · [Tiếng Việt](../../vi/docs/01-prior-art.md) · 中文 · [日本語](../../ja/docs/01-prior-art.md) · [한국어](../../ko/docs/01-prior-art.md) · [हिन्दी](../../hi/docs/01-prior-art.md)

## 规则
本仓库中的每一项技术决策都必须能追溯到"自由"清单中的某个来源（已过期专利、论文）。有效专利仅供阅读——从中挖掘对问题的洞察，绝不照搬其权利要求（这对美国商业化至关重要；参见项目中的专利地图）。

## 自由基石（已过期/放弃的专利 = 公共领域）
- **US5982297**（Aerospace Corp，1997）——基本配方：穿过壁面的压电片对，同时传输功率和双向数据。主菜谱。
- US5594705（Dynamotive，1994）——穿过船壳的"声学变压器"。
- US6037704、US6127942（Aerospace Corp）——为传感器供电、读取回传数据。
- **US7902943**（Caltech/JPL，因未缴维持费于2019年失效）——Sherrit 馈通结构：反射器、声学变压器。
- US9748870（Caltech/JPL）——穿过壁面做机械功。
- **US9361877**（俄克拉荷马大学，因未缴维持费而失效）——一套现代完整的收发系统。
- US20100027379 / WO2008105947（DOE+RPI，已放弃）——外部载波 + 内部负载调制。

## 关键论文
- Lawry 等，IEEE TUFFC 2013（10.1109/TUFFC.2013.2550）——50 W + 12.4 Mbit/s，63.5 mm 钢壁。
- Sherrit 等，NASA NTRS 20080048150——一盏 100 W 灯通过壁面供电。
- Yang 等，Sensors 2015（10.3390/s151229870）——综述，对各项数值的最佳总结。
- Ji 等，Phys. Rev. Applied 21, 014059（2024）——超材料，1 mm 不锈钢透过率从 2%→66%（截至 07.2026 未找到专利）。

这些论文是**物理基础与专利合规底线**。其中的功率/比特率数据使用的是实验室换能器、键合工艺和阻抗匹配——而非 [QUICKSTART.md](../QUICKSTART.md) 中 AliExpress 朗之万换能器 + 导热脂的 BOM。把它们当作存在性证明来引用；项目自身的通过标准见 [experiments/](../experiments/)。

## 在专利有效期内不照搬的内容（仅限美国，有效期至约2032年；阶段1–4反正也用不到）
用子载波规避功率通道谐波的 OFDM（RPI US9054826）；将"AM 下行链路 + 负载调制上行链路 + 频率跟踪"作为单一方案的全双工设计（RPI US9455791）；Drexel 方案中用于曲面的共形换能器（US10594409）。
