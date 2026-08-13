# Experiment 002: First Watts Through 3 mm Steel (PLANNED)

> [English (primary)](../../../../experiments/002-watts-3mm-steel/README.md) · [Русский](../../../ru/experiments/002-watts-3mm-steel/README.md) · [Deutsch](../../../de/experiments/002-watts-3mm-steel/README.md) · [Português](../../../pt/experiments/002-watts-3mm-steel/README.md) · [Español](../../../es/experiments/002-watts-3mm-steel/README.md) · [Français](../../../fr/experiments/002-watts-3mm-steel/README.md) · [Italiano](../../../it/experiments/002-watts-3mm-steel/README.md) · [Polski](../../../pl/experiments/002-watts-3mm-steel/README.md) · [Türkçe](../../../tr/experiments/002-watts-3mm-steel/README.md) · [Українська](../../../uk/experiments/002-watts-3mm-steel/README.md) · [Tiếng Việt](../../../vi/experiments/002-watts-3mm-steel/README.md) · 中文 · [日本語](../../../ja/experiments/002-watts-3mm-steel/README.md) · [한국어](../../../ko/experiments/002-watts-3mm-steel/README.md) · [हिन्दी](../../../hi/experiments/002-watts-3mm-steel/README.md)

- **阶段：** 2 (将功率输入已知负载，位于 [001](../001-sweep-map-3mm-steel/README.md) 中找到的谐振频率处)。
- **目标：** 测量使用半桥驱动器和匹配变压器通过 3 mm 钢板传递的实际直流功率。
- **假设：** 使用同批次的朗兹文转ducer，grease+clamp（或环氧树脂）接触，以及调谐的匹配变压器，在阶段 1 的峰值处可以实现 ≥0.5 W 的功率输入到阻性负载。（文献中的多瓦/千瓦数值使用了不同的转ducer和键合方式——将其视为上限，而不是合格标准。）
- **先决条件：**
  - Experiment 001 已完成（可重复的峰值，记录的频率）。
  - 在驱动器供电之前，在 RX 链上安装了 TVS ([docs/02-safety.md](../../docs/02-safety.md))。
  - 遵循驱动器启动顺序 ([hardware/driver/README.md](../../../../hardware/driver/README.md))。
- **设置（最低）：**
  - TX：Pi → AD9833 方波 → 死区整形器 → IR2110 半桥 → 匹配变压器 → 朗兹文转ducer夹在板上 ([sch1](../../hardware/schematics/sch1-driver-halfbridge.png))。
  - 墙：3 mm 钢，记录接触方法（grease+clamp / 环氧树脂 / 其他）。
  - RX：朗兹文转ducer → 肖特基桥 → 已知 R_load（功率电阻）和/或 LED；在桥后测量 V_dc 和 I_dc ([sch2](../../hardware/schematics/sch2-receiver-stage1.png) 拓扑，负载代替仅 ADC）。
- **过程（大纲）：**
  1. 在 0.2 A PSU 限制下进行电气启动，不声称声学功率。
  2. 夹紧 TX/RX，设置驱动频率为实验 001 的峰值。
  3. 慢慢提高电流限制；记录 PSU V/I、MOSFET/变压器温度、负载上的 V_dc 和 I_dc。
  4. P_load = V_dc · I_dc。可选：一旦知道 P_load，就拍摄 LED 演示照片。
  5. 冷却后再次重复；峰值频率可能会随温度而漂移——如果功率下降，请使用迷你扫描重新检查。
- **成功标准：**
  1. 通过 3 mm 钢在记录的频率和接触方法下实现 P_load ≥ 0.5 W。
  2. 两个运行在相同的夹持/耦合剂下对 P_load 达到 ~20% 的一致性（数量级稳定性，而不是计量级）。
  3. LED（或其他负载）照片 + CSV/log 链接到此文件下的 `data/`。
- **失败即数据：** 如果 P_load 保持 ≪ 0.5 W，请记录对 Δf（来自 001）、接触方法、变压器匝数和波形 —— 这是下一个 ADR 的输入，而不是编辑模拟器的理由。
