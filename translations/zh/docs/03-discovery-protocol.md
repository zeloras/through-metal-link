# 接收器发现和自动调谐协议（草图；在第2-4阶段实现）

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · 中文 · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

目标：设备自己确定是否有接收器在墙后，自己选择频率和功率，并且如果有人“忘记了将接收器焊接在墙上”，则不会白白地烤墙。

参考模型是Qi充电器：它们解决了同样的问题（线圈上是否有手机？）并且使用了同样的序列。我们的声学模拟：

## 阶段0 — 模拟ping（接收器可能完全放电）
TX以低功率扫描整个频带，并测量**其自身的电流和相位**（电压分压器 + 峰值检测器 → ADS1115）。墙后有一个谐振接收器：它的存在表现为TX阻抗曲线上的特征性凹陷/隆起，即使内部一切都没有电源。与金属探测器和Qi的模拟ping相同的原理。
- 存在特征 → 阶段1。没有特征 → “未找到接收器”，保持在待机ping（每N秒一次），不要提高功率。
-奖励：在安装时，空墙的阻抗曲线被记录为参考 —— 因此我们可以区分“没有接收器”和“接收器松动/失去对齐”。

## 阶段1 — 数字握手
TX停留在候选频率（阶段0的峰值）并提供功率。RX收集器为超级电容器充电，MCU唤醒并使用**负载调制**进行回复：MOSFET周期性地短路其压电材料，按照代码（ID + 协议版本）进行操作。TX将其视为其自身电流的调制。内部根本不需要传输器 —— 这是一个RFID方案，与废弃的DOE/RPI申请US20100027379（免费先前艺术）相同。

## 阶段2 — 频率伺服调谐（扰乱和观察）
RX可以报告其总线电压（通过负载调制的遥测）。TX步进±Δf并保持接收到的最大功率 —— 一个经典的MPPT循环。这可以关闭温度（这个领域的主要问题：~6%的偏移 = ~10×效率下降）引起的谐振漂移。

## 阶段3 — 功率协商和看门狗
RX请求一个级别（存活/充电/给我更多），TX将功率限制在所请求的功率。M个周期内缺少回复 → TX回退到阶段0，功率较低。

## 所需硬件（BOM项目12，原理图 —— 硬件/原理图/sch4）
- TX：0.1 Ω电压分压器 + 第二个ADS1115通道上的整流器/峰值检测器（电流），可选的相位比较器。
- RX：2N7002 + ~100 Ω在**直流侧**的整流器（LTC3588模块的VIN引脚）+ GPIO —— 负载在桥接后切换，TX将其视为其自身电流的调制。单个MOSFET跨越AC压电材料不起作用（体二极管短路了一半波，门没有浮动节点的参考）；跨压电材料的变体仅适用于一对背靠背的串联MOSFET。

## 限制
模拟ping随着墙厚度和接触损失的增加而减弱（特征被噪音淹没）—— 检测阈值必须在专用实验（实验/）中测量。对于厚墙，fallback：RX，一旦它存储了电荷，就会周期性地用自己的信标“敲门”。
