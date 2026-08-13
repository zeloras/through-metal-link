# 实验 002：首次穿透 3 mm 钢板的功率传输（计划中）

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · 中文 · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **阶段：** 2（在 [001](../001-sweep-map-3mm-steel/README.md) 中找到的谐振点处向已知负载输入功率）。
- **目标：** 使用半桥驱动器和匹配变压器，测量通过 3 mm 钢板传输的真实直流功率。
- **假设：** 使用同批次 Langevin 换能器对、油脂+夹具（或环氧树脂）接触，以及调谐好的匹配变压器，在阶段 1 的峰值频率下向电阻负载传输 ≥0.5 W 是可实现的。（文献中的多瓦/千瓦级数据使用了不同的换能器和粘合方式——应将其视为上限，而非通过标准。）
- **前置条件：**
  - 实验 001 已完成（可复现的峰值，频率已记录）。
  - 在任何驱动器上电之前，RX 链路已安装 TVS（[docs/02-safety.md](../../docs/02-safety.md)）。
  - 已遵循驱动器调试流程（[hardware/driver/README.md](../../hardware/driver/README.md)）。
- **实验装置（最低要求）：**
  - TX：Pi → AD9833 方波 → 死区时间整形器 → IR2110 半桥 → 匹配变压器 → 夹紧在钢板上的 Langevin（[sch1](../../hardware/schematics/sch1-driver-halfbridge.png)）。
  - 隔壁：3 mm 钢板，记录接触方式（油脂+夹具 / 环氧树脂 / 其他）。
  - RX：Langevin → 肖特基桥 → 已知 R_load（功率电阻）和/或 LED；测量桥后的 V_dc 和 I_dc（[sch2](../../hardware/schematics/sch2-receiver-stage1.png) 拓扑，负载替代仅 ADC 接入）。
- **步骤（概要）：**
  1. 在 0.2 A 电源限流下进行电气调试，不声称有声功率输出。
  2. 夹紧 TX/RX，将驱动频率设为实验 001 的峰值频率。
  3. 缓慢提高电流限制；记录电源 V/I、MOSFET/变压器温度、负载上的 V_dc 和 I_dc。
  4. P_load = V_dc · I_dc。可选：在已知 P_load 后拍摄 LED 演示照片。
  5. 冷却后重复一次；峰值频率可能随温度漂移——若功率下降，用小范围扫频重新检查。
- **成功标准：**
  1. 在记录的频率和接触方式下，通过 3 mm 钢板 P_load ≥ 0.5 W。
  2. 在相同夹具/耦合剂条件下，两次运行的 P_load 一致性在 ~20% 以内（数量级稳定性，尚非计量级精度）。
  3. LED（或其他负载）照片 + CSV/日志链接至本文件下的 `data/` 目录。
- **失败也是数据：** 如果 P_load 始终 ≪ 0.5 W，记录换能器对 Δf（来自 001）、接触方式、变压器匝数比和波形——这是下一个 ADR 的输入，而不是悄悄修改仿真器的理由。
