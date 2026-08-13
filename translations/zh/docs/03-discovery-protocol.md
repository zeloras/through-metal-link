# 接收端发现与自动调谐协议（草案；实现分阶段 2–4 完成）

> [English (primary)](../../../docs/03-discovery-protocol.md) · [Русский](../../ru/docs/03-discovery-protocol.md) · [Deutsch](../../de/docs/03-discovery-protocol.md) · [Português](../../pt/docs/03-discovery-protocol.md) · [Español](../../es/docs/03-discovery-protocol.md) · [Français](../../fr/docs/03-discovery-protocol.md) · [Italiano](../../it/docs/03-discovery-protocol.md) · [Polski](../../pl/docs/03-discovery-protocol.md) · [Türkçe](../../tr/docs/03-discovery-protocol.md) · [Українська](../../uk/docs/03-discovery-protocol.md) · [Tiếng Việt](../../vi/docs/03-discovery-protocol.md) · 中文 · [日本語](../../ja/docs/03-discovery-protocol.md) · [한국어](../../ko/docs/03-discovery-protocol.md) · [हिन्दी](../../hi/docs/03-discovery-protocol.md)

目标：设备自行判断墙后是否有接收端，自行选择频率和功率，如果有人"忘了把接收端焊上去"，也不会白白把墙烤热。

参考模型是 Qi 充电器：它们正是用完全相同的流程来解决同样的问题（线圈上有没有手机？）。我们的声学类比：

## 阶段 0 — 模拟 ping（接收端可能完全放电）
TX 在整个频段上做低功率扫频，并测量**自身的电流和相位**（分流电阻 + 峰值检波器 → ADS1115）。墙后的谐振接收端是通过墙壁耦合到 TX 的负载：即使内部一切未上电，它的存在也会在 TX 阻抗曲线上表现为一个特征性的凹陷/凸起。原理与金属探测器和 Qi 的模拟 ping 相同。
- 检测到特征 → 进入阶段 1。无特征 → "未找到接收端"，保持待机 ping（每 N 秒一次），不提升功率。
- 额外好处："空"墙的阻抗曲线在安装时作为参考记录下来——这样我们就能区分"没有接收端"和"接收端脱落 / 对位偏移"。

## 阶段 1 — 数字握手
TX 停在候选频率上（阶段 0 的峰值点）并开始输送功率。RX 能量收集器给超级电容充电，MCU 唤醒后以**负载调制**方式回复：一个 MOSFET 按照编码（ID + 协议版本）周期性地短路其压电片。TX 将此视为自身电流的调制。内部完全不需要发射器——这是一种 RFID 方案，与已放弃的 DOE/RPI 申请 US20100027379 中的方案相同（免费现有技术）。

## 阶段 2 — 频率伺服调谐（扰动观察法）
RX 可以上报其总线电压（通过负载调制传输遥测数据）。TX 以 ±Δf 步进并保持接收功率最大——经典的 MPPT 环路。这解决了温度引起的谐振漂移问题（该领域的头号陷阱：约 6% 的偏移 = 约 10 倍效率下降）。

## 阶段 3 — 功率协商与看门狗
RX 请求一个功率等级（存活 / 充电中 / 给我更多），TX 将功率上限设为请求值。连续 M 个周期未收到回复 → TX 以低功率回退到阶段 0。

## 所需硬件（BOM 条目 12，原理图 — hardware/schematics/sch4）
- TX：0.1 Ω 分流电阻 + 整流器/峰值检波器接在 ADS1115 第二通道（电流），可选相位比较器。
- RX：2N7002 + ~100 Ω 接在整流器的**直流侧**（LTC3588 模块的 VIN 引脚）+ GPIO——负载在桥之后切换，TX 将其视为自身电流的调制。单个 MOSFET 跨接在交流压电片上不工作（体二极管会旁路半个波形，栅极在浮空节点上没有参考点）；跨接压电片的方案只有用一对背靠背串联 MOSFET 才可行。

## 局限性
模拟 ping 随着壁厚和接触损耗增大而减弱（特征淹没在噪声中）——检测阈值必须通过专门实验来测定（experiments/）。对于厚壁，后备方案是：RX 在积攒足够电荷后，周期性地用自己的信标"敲门"。
