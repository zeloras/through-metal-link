# 通过金属壁的超声波能量和数据传输

> [English (primary)](../../README.md) · [Русский](../ru/README.md) · [Deutsch](../de/README.md) · [Português](../pt/README.md) · 中文 · [日本語](../ja/README.md)

一个开放的平台，用于通过实心金属壁传输超声波能量和数据——“无需打孔”，使用车库级设备。

**状态：** 阶段 0 — 准备 · 💰 **[$250 首次独立构建悬赏](https://github.com/zeloras/through-metal-link/issues)** · 购买清单：[QUICKSTART.md](../../QUICKSTART.md)

[![CI](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/ci.yml) [![REUSE](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml/badge.svg)](https://github.com/zeloras/through-metal-link/actions/workflows/reuse.yml)

文档是多语言的：英语是主要语言，位于规范路径；其他语言在 [translations/](../../translations/) 下镜像树。编辑任何语言 — CI 翻译并提交其余部分（请参阅 [CONTRIBUTING.md](../../CONTRIBUTING.md)）。

<p align="center"><img src="../../docs/img/sim0-rig-sketch.png" alt="第一阶段设备：Pi → DDS → 半桥 → 变压器 → 压电发射器 | 金属 | 压电接收器 → 桥接 → ADC → Pi" width="900"></p>

## 概念

无线电波不能通过金属（法拉第笼），而电缆穿透意味着一个孔、一个密封和一个故障点。另一方面，超声波可以通过金属传输：每侧的压电元件将墙壁变成能量和数据的通道。实验室文献已经在较高水平上证明了物理原理（RPI：50 W + 12 Mbit/s 通过 63.5 mm 的钢；NASA JPL：最高可达 ~kW 通过 5 mm 的钛）—— 这些是使用专用硬件的存在证明，而不是这个仓库的车库 BOM。基础专利已经过期，没有开放的可复制平台 —— 本仓库正在构建一个，从 **瓦级能量和 kbit/s 数据通过 3–5 mm 钢** 开始，一旦第二阶段被测量。

## 路线图

| 阶段 | 交付物 | 成功标准 | 预期 |
|---|---|---|---|
| 1. 扫描图 | “Langevin–3 mm 钢–Langevin” 通道的频率响应 | 对称谐振找到，图表在 [experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md) 中 | [sim1](../../docs/img/sim1-sweep-contacts.png)，[sim2](../../docs/img/sim2-pair-mismatch.png) |
| 2. 瓦特 | 负载在谐振时的功率 | ≥0.5 W 通过 3 mm 的钢，协议在 [experiments/002](../../experiments/002-watts-3mm-steel/README.md) 中 | [sim4](../../docs/img/sim4-power-budget.png) |
| 3. 数据 | FSK/OOK 在同一对设备上 | ≥1 kbit/s 无错误 | [sim5](../../docs/img/sim5-ook-datarate.png) |
| 4. 节点 | ESP32 + 传感器在焊接的盒子中，仅通过声音供电和遥测 | ≥1 小时的自主运行 | [sim4](../../docs/img/sim4-power-budget.png) |
| 5. 发布 | 仓库公开，文章/教程 | 第三方复制 | — |

## 仓库地图

每个块下面展开：内部是足够的摘要，以及一个链接到全文档。

<details>
<summary><b>🛒 从零开始到一个可用的设备：什么需要购买以及购买的顺序</b> — <a href="../../QUICKSTART.md">QUICKSTART.md</a></summary>

**预算：** ~210 美元的最低限度，~300 美元的舒适预算（如果您已经拥有 Pi、焊接铁和实验室电源，则可以节省 ~120 美元）。三个篮子：工具（~120 美元），设备电子元件（~70 美元，[完整的 BOM](../../hardware/bom/bom-stage1.csv)），机械元件（~20 美元）。可选但强烈推荐：USB 示波器（~60–80 美元）。

**关键路径 — AliExpress 发货（3–4 周）：** 在第一天订购电子元件。关键决策：购买 **4 个来自同一批次的 Langevin 转换器** — 扫描将选择最好的对（[为什么](../../docs/img/sim2-pair-mismatch.png)）。

**在它发货时：** 使用没有硬件的管道进行干跑 —

```bash
python3 ../../software/sweep-map/sweep_map.py --mock
```

**完成时（按阶段）：** 第一阶段 — 跨两个运行内的扫描峰值重现 <200 Hz（[experiments/001](../../experiments/001-sweep-map-3mm-steel/README.md)）；第二阶段 — ≥0.5 W 输入已知负载通过 3 mm 的钢和 RX 侧的 LED 照明（[experiments/002](../../experiments/002-watts-3mm-steel/README.md)）。

</details>

<details>
<summary><b>📚 理论在一分钟内</b> — <a href="../../docs/00-theory.md">docs/00-theory.md</a></summary>

压电发射器被按压在墙上并驱动一个纵波进入其中；另一侧的压电接收器将其转换回电力。钢中的声速：~5900 m/s。

两种操作模式：

| 模式 | 频率 | 谐振由以下设置 | 得到 | 状态 |
|---|---|---|---|---|
| **A** — Langevin 转换器 | 40 kHz | 转换器对（墙 ≪ λ — 一个“膜”） | 瓦特，kbit/s | 启动模式（阶段 1–4，[ADR-0001](../../docs/decisions/0001-frequency-mode-choice.md)） |
| **B** — 圆盘 | 0.6–1 MHz | 墙的厚度谐振 ([梳状](../../docs/img/sim3-thickness-comb.png)) | 数百毫瓦，数百 kbit/s | 分支后第一次获得瓦特；需要自动频率跟踪 |

主要损失：对内的谐振不匹配（±1 kHz 低于廉价的 Langevin 转换器），声学接触质量（环氧树脂 >润滑剂耦合 + 夹子 > 干压），错位，谐振随温度漂移。所有这些问题的答案都是相同的：**每次设置更改之前的扫描图**。

</details>

<details>
<summary><b>📈 设备应该显示的内容：模拟器的预期图</b> — <a href="../../software/simulator/channel_sim.py">software/simulator/channel_sim.py</a></summary>

一个半经验的通道模型（不是 FEM，**不是实验室数据** —— 对“扫描应该是什么样子以及应该瞄准什么”的直觉）。假设在 `channel_sim.py` 中是明确的（载入 Q≈40，接触 k 因子，链 η≤40%）。使用 `python3 channel_sim.py --out ../../docs/img` 重新生成。

**第一阶段 — 扫描。** 一个在 ~40 kHz 附近的窄峰；模型的占位符接触乘数是润滑剂：干燥：间隙 = 1 : 0.25 : 0.02（即润滑剂 ≈4× 干燥和 ≈50× 空气间隙）。没有峰值意味着接触或对的故障：

<img src="../../docs/img/sim1-sweep-contacts.png" width="720">

**为什么是 4 个 Langevin 转换器，而不是 2 个。** 在 Q≈40 下，对内的 1.5 kHz 谐振不匹配会将模型功率降低 ~10×：

<img src="../../docs/img/sim2-pair-mismatch.png" width="720">

**第三阶段 — 数据。** OOK 遇到谐振器环形（模型 Q~40 → τ≈0.3 ms）：1 kbit/s 是干净的，在 5 kbit/s 时眼是关闭的。更快需要模式 B：

<img src="../../docs/img/sim5-ook-datarate.png" width="720">

**接收器功率预算。** 阴影带是 **目标**（模式 A 0.5–5 W 如果第二阶段实现；模式 B 更低）。实际的第一负载是周期 ESP32 / BLE / LED；Wi-Fi 作为一个峰值吸收标记，而不是持续的承诺：

<img src="../../docs/img/sim4-power-budget.png" width="720">

**稍后（模式 B）。** 板在厚度谐振的梳状图中变得透明 —— 频率必须被跟踪：

<img src="../../docs/img/sim3-thickness-comb.png" width="720">

</details>

<details>
<summary><b>⚠️ 安全 — 请在第一次上电前阅读</b> — <a href="../../docs/02-safety.md">docs/02-safety.md</a></summary>

1. **压电元件上的几十到几百伏** 一旦第二阶段驱动器上线 —— RX 侧的 TVS 在第一次上电前就安装好了；请将您的双手从引线上移开。
2. **主电源** —— 仅通过实验室电源 / 隔离；超声波清洗器驱动器板与主电源是电气连接的。
3. **耳朵** —— 在非平凡的功率下，操作压电元件时将其按压在金属上；永远不要在没有外壳的情况下运行高功率的空气超声波。
4. **热量** —— 未夹紧的 Langevin 转换器在几分钟内在功率下过热；在提高电流之前夹紧（仅电气启动 —— 参见驱动器 README）。
5. **碎片** —— 压电陶瓷是脆的：过紧的螺栓或撞击意味着碎片；进行任何机械工作时请戴上安全眼镜。

第一次驱动器上电：实验室电源电流限制 0.2 A；完整序列在 [hardware/driver/](../../hardware/driver/README.md) 和 [docs/02-safety.md](../../docs/02-safety.md) 中。

</details>

<details>
<summary><b>🧭 先前的艺术和专利卫生</b> — <a href="../../docs/01-prior-art.md">docs/01-prior-art.md</a></summary>

每个技术决策必须追溯到“免费”的来源（过期专利，论文）。基础：**US5982297**（航空航天公司 —— 通过墙壁压电对的基本配方），**US7902943**（加州理工学院 / JPL —— Sherrit 的馈通），**US9361877**（俄克拉荷马大学 —— 一个完整的收发器系统）；所有这些都已死亡。关键论文：Lawry 2013 年（50 W + 12.4 Mbit/s 通过 63.5 mm 的钢），Sherrit/NASA（100 W 灯），Yang 2015 年（调查）。

在 ~2032 年之前不应被复制（仅限美国；阶段 1–4 不需要）：RPI 的 OFDM 分配，RPI 的全双工方案，Drexel 的符合性转换器。

架构决策记录在 [docs/decisions/](../../docs/decisions/0001-frequency-mode-choice.md)（ADR）中。

</details>

<details>
<summary><b>🔌 硬件和固件</b> — hardware/，firmware/</summary>

- [hardware/bom/bom-stage1.csv](../../hardware/bom/bom-stage1.csv) — 第一阶段购物清单。
- [hardware/schematics/](../../hardware/schematics/README.md) — **电路图**（从代码生成）：驱动器，接收器，Pi 引脚，收集器节点。
- [hardware/driver/](../../hardware/driver/README.md) — TX 驱动器：IR2110 半桥 + 2×IRF540，匹配变压器（Langevin 转换器是电容负载！）。KiCad 板在面包板原型检查后。
- [hardware/receiver/](../../hardware/receiver/README.md) — 接收器，逐步：Schottky 桥 → ADC（第一阶段）→ 负载（第二阶段）→ LTC3588 + 超级电容器 + ESP32（第四阶段）。
- [firmware/node-esp32/](../../firmware/node-esp32/README.md) — 第四阶段节点（存根）：深度睡眠，传感器读取，BLE 广告，预算 1–5 mW 平均。

</details>

<details>
<summary><b>💻 软件：测量和模拟器</b> — software/</summary>

- [software/sweep-map/sweep_map.py](../../software/sweep-map/sweep_map.py) — 第一阶段的工作马：DDS 扫描 → ADC 读数 → CSV + 频率响应图。具有 `--mock` 以在没有硬件的情况下运行。在 Pi 上：`raspi-config` → 启用 SPI 和 I2C；`pip install spidev smbus2 matplotlib`。
- [software/simulator/channel_sim.py](../../software/simulator/channel_sim.py) — 预期图的生成器（`pip install numpy matplotlib`）。
- [data/](../../data/README.md) — 原始日志；CSV/PNG 保持在 git 之外，只有策划的图表进入 git 内部的实验目录。

</details>

<details>
<summary><b>🗺️ 应用此技术的位置：屏障，通道，市场</b> — <a href="../../docs/04-hybrid-channels.md">docs/04</a>，<a href="../../docs/05-applications-map.md">docs/05</a></summary>

没有通用的通道 —— 该平台将物理学与屏障相匹配：压电声学（主要：钢/铝与接触 —— 瓦特和 kbit/s），EMAT（脏/热金属，无接触 —— 数据），低频磁性（真空夹层墙 —— 位/s）。诚实的死胡同：橡胶衬里/复合墙，路径中的气泡液体。

市场优先级：**(1)** 实验室真空室和低温箱 —— 开源硬件受众，无认证；**(2)** 发酵罐 —— 步行距离内的证明场；**(3)** 密封电池包 —— 旗舰案例（无需穿透包即可检测热失控）。接收器发现和自动调谐协议（类似于 Qi）：[docs/03-discovery-protocol.md](../../docs/03-discovery-protocol.md)。

</details>

<details>
<summary><b>📁 目录布局</b></summary>

```
docs/            理论，先前的艺术，安全，应用，决策日志（ADR）
docs/img/        预期图（由 software/simulator/channel_sim.py 生成）
hardware/        BOM，驱动器（半桥），接收器（整流器/收集器）
firmware/        节点固件（ESP32 —— 存根，直到第四阶段）
software/        测量脚本（频率响应扫描图）和通道模拟器
experiments/     实验协议 —— 从模板，一个目录 = 一个实验
data/            原始日志（大文件保持在 git 之外）
```

</details>

## 原则

1. **从零开始的可复制性。** 任何拥有焊接铁和 ~210 美元的人都可以仅从这个仓库中复制结果。
2. **每个实验都是一个协议。** 没有“它大致有效”的说法：[experiments/TEMPLATE.md](../../experiments/TEMPLATE.md) 是强制性的。
3. **专利卫生。** 我们建立在过期的层上 ([docs/01-prior-art.md](../../docs/01-prior-art.md))；决策记录在 [docs/decisions/](../../docs/decisions/0001-frequency-mode-choice.md) 中。
4. **测量优先于意见。** 每次设置更改之前的扫描图。

## 许可证和专利

代码 — Apache-2.0，硬件 — CERN-OHL-W v2，文档 — CC-BY-4.0；完整文本在 [LICENSES/](../../LICENSES/) 中。任何人都可以分叉和在此基础上进行商业建设；专利保护来自许可证中的授权和报复条款以及先前艺术策略。完整的方案和防御性出版协议：[LICENSES.md](../../LICENSES.md)；贡献规则：[CONTRIBUTING.md](../../CONTRIBUTING.md)。
