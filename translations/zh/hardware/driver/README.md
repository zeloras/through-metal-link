# 驱动级（第 2 级）：IR2110 半桥

> [English (primary)](../../../../hardware/driver/README.md) · [Русский](../../../ru/hardware/driver/README.md) · [Deutsch](../../../de/hardware/driver/README.md) · [Português](../../../pt/hardware/driver/README.md) · [Español](../../../es/hardware/driver/README.md) · [Français](../../../fr/hardware/driver/README.md) · [Italiano](../../../it/hardware/driver/README.md) · [Polski](../../../pl/hardware/driver/README.md) · [Türkçe](../../../tr/hardware/driver/README.md) · [Українська](../../../uk/hardware/driver/README.md) · [Tiếng Việt](../../../vi/hardware/driver/README.md) · 中文 · [日本語](../../../ja/hardware/driver/README.md) · [한국어](../../../ko/hardware/driver/README.md) · [हिन्दी](../../../hi/hardware/driver/README.md)

**原理图：** [../schematics/sch1-driver-halfbridge.png](../schematics/sch1-driver-halfbridge.png)（由 [../schematics/render_schematics.py](../../../../hardware/schematics/render_schematics.py) 生成）

信号链：Pi（SPI）→ AD9833 **方波模式**（OPBITEN 位置位：MSB 直接路由到输出，轨到轨摆幅——无需单独的比较器）→ **74HC14 + RC + 1N4148** 整形电路（互补 HIN/LIN，死区时间约 1 µs）→ IR2110 → 2×IRF540（半桥）→ 1 µF 隔直电容 → 匹配变压器（铁氧体，约 1:3..1:5，在实验台上调试）→ Langevin 换能器 TX。

AD9833 的正弦输出（约 0.6 Vpp）不适合 IR2110 的逻辑电平——如果你确实需要 DDS 输出正弦波，在两者之间加一个比较器（例如 LM393，不在 BOM 中）。

功率级供电：12–24 V 实验室电源，带限流功能（**从 0.2 A 起调**）。

注意：第 1 级扫频直接用 DDS 弱正弦信号驱动压电片（约 0.6 Vpp，见 `sweep_map.py`）——**本驱动级仅在第 2 级（瓦特级）接入信号链**。不要指望第 1 级仅用 DDS 直连就能输出 ≥0.5 W。

注意事项：
- Langevin 换能器是容性负载（通常几 nF）。串联电感或匹配变压器是必须的；否则 MOSFET 会消耗无功电流并烧毁。
- **匹配变压器（常见故障点）。** 从小型铁氧体磁环开始（例如 FT50-43 / 类似型号），初级绕几圈，次级约 3–5 倍，初级串联 1 µF 薄膜隔直电容。在 TX **夹紧到钢板**且 RX 带载的情况下，调到*第 1 级谐振频率*下电源电流最小。匝比和漏感靠经验确定——原理图上标注 `*` 是有原因的。最终匝数记录到实验日志中。
- **死区时间**：IR2110 本身不产生死区时间。分立元件方案——在 74HC14 输入端加 RC+1N4148（仅延迟上升沿，约 1 µs；40 kHz 时周期 25 µs，损耗 <5%）。简单方案——用 EGS002 模块，一切都内置好了。
- **3.3 V 逻辑**：IR2110 的 VDD 与 AD9833 和 74HC14 共用 3.3 V 供电——在 VDD=5 V 时 VIH 阈值约为 3.1 V，3.3 V 方波勉强能通过（数据手册允许 VDD 低至 3.3 V）。
- **去耦必须到位**：VDD 和 VCC 处各加 100 nF（VCC 再加 47 µF），功率轨在半桥臂处加 470–1000 µF + 100 nF 陶瓷电容——否则面包板跳线上的半桥会拾取自身的开关尖峰。功率回路走线尽量短；如果开关节点振铃严重，在提高电流之前先从面包板转到覆铜板 dead-bug / 洞洞板铺地。
- **首次上电步骤**（与 [docs/02-safety.md](../../docs/02-safety.md) 一致）：
  1. 次级先不接 Langevin。电源 = 12 V，限流 0.2 A。用示波器观察栅极驱动（HIN/LIN）和开关节点——确认死区时间正常且无直通。
  2. 装上匹配变压器 + TX Langevin，**夹紧到钢板**（或厚金属牺牲块）。仍然限流 0.2 A。仅在第 1 级峰值频率下短暂上电，看到电流和 RX 电压即可。
  3. 逐步提高限流值，同时监测 MOSFET 和变压器温度。绝不要让未夹紧的 Langevin 带电工作——空气中满功率运行是陶瓷开裂、驱动器烧毁的典型原因。

TODO：面包板（或 dead-bug）原型验证通过后，做 KiCad 工程（PCB）。在此之前，[`../schematics/`](../schematics/) 中的原理图是设计唯一可信源。
