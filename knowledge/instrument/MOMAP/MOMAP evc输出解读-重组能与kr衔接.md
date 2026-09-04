---
tags:
  - 计算化学
  - research
  - 后处理
Category:
  - 讲义
---

# MOMAP evc 输出解读：重组能与 kr 衔接

以 DHR 的 S1 荧光路线（`evc-kr-s1`，水溶剂 CAM-B3LYP/6-31g(d,p)）的实际数据为例，解读 evc 输出、重组能的物理意义，以及 evc 为下一步 kr 提供了什么。

## 1. 重组能的物理意义

电子跃迁瞬间原子核来不及动（Franck-Condon 原理），电子云先变、几何后弛豫；重组能 λ 就是"几何追赶电子云"过程中涉及的能量。

- **λ(S0)**（lam1 列之和，1748.98 cm⁻¹）：S0 态"摁"在 S1 优化几何上时，比自己的极小点高出的能量——S0 在 S1 几何下的形变能。
- **λ(S1)**（lam2 列之和，1746.51 cm⁻¹）：S1 态在 S0 几何下的形变能。
- **总重组能** λ_total = λ(S0) + λ(S1) = 3495.5 cm⁻¹ ≈ 0.433 eV，是吸收峰与发射峰之间 Stokes 位移的根源：吸收峰 = 0-0 + λ(S1)，发射峰 = 0-0 − λ(S0)。

> [!tip] 交叉验证
> 垂直吸收 2.3487 eV − 垂直发射 1.9357 eV = 0.413 eV = 3331 cm⁻¹，与 λ_total = 3495 cm⁻¹ 差约 5%，吻合良好（小偏差来自 Duschinsky 混合与频率变化）。

λ 越大 → 谱带越宽、Stokes 位移越大、振子结构越长；DHR 的 0.43 eV 属中等电子-振动耦合。

## 2. evc-kr 计算了什么

输入：momap.inp 里 `ffreq(1)="DHR-s0opt.log"`、`ffreq(2)="DHR-s1opt.log"` + 同名 .fchk。evc.exe 读出两态的优化几何、简正频率 ω、简正模式矢量、零点能 ZPE，然后用 Duschinsky 变换连接两套简正坐标：

$$
Q(\text{基态}) = S \cdot Q(\text{激发态}) + D
$$

- **S**：126×126 旋转矩阵（本体系 Delta DUSH = 55.85%，混合强，故 DUSHIN=.t. 必须开）；
- **D**：位移矢量（两几何之差投影到各模式）。

逐模式表格（17 列）：`n m sym freq D δ HR lam | 态2同组 | g e S(g,e)`

- `freq`：模式频率（cm⁻¹）
- `D`：质量加权位移（a.u.）
- `δ`：无量纲位移 = D·√freq
- `HR`：Huang-Rhys 因子 = ½δ²，跃迁在该模式平均激发的振动量子数；HR 大的模式主导光谱形状（DHR 是 m91≈1422、m104≈1582 cm⁻¹ 等 C–C 伸缩）
- `lam`：该模式重组能 = HR·ħω
- `S(g,e)`：Duschinsky 元素，≈±1 模式原样保留，≈0 被强烈打散
- 前 6 行 m=0 是平转，物理振动从 m=1 起共 126 个

输出：evc.cart.dat（笛卡尔全套）、evc.dint.dat（内坐标重组能+笛卡尔 S 矩阵）、头部记录 ZPE2−ZPE1 = −638.36 cm⁻¹ 与 Delta DUSH。

> [!tip] cart 还是 dint
> 搜 `Total reorganization energy` 比较两文件：cart 1748.98/1746.51 vs dint 1748.27/1747.34，差 <1 cm⁻¹ ≪ 1000 → 用 cart。

## 3. 为下一步 kr 提供了什么

kr 步骤（spec_tvcf）的输入：

| 输入 | DHR 值 | 作用 |
|---|---|---|
| DSFile=evc.cart.dat | ω、S、D、HR、ZPE | 构建发射 Franck-Condon 重叠积分，光谱振动结构全靠它 |
| Ead | 0.078804 au | 定电子跃迁原点（谱的位置） |
| EDMA / EDME | 6.93 / 7.25 D | 跃迁偶极强度（谱高与速率量级） |
| Temp/tmax/dt/展宽 | 300 K / 1000 fs / 0.01 fs / 200 cm⁻¹ | 温度、积分参数、展宽 |

程序把 FC 因子带相位求和成时间相关函数 C(t)，傅里叶变换得荧光光谱（spec.tvcf.spec.dat），按 ω³ 加权积分得 kr（spec.tvcf.log 末尾）；收敛看 spec.tvcf.ft.dat 前两列是否衰减到零。

## 4. 来源总表

| 物理量 | 值 | 来源 | 读哪里 |
|---|---|---|---|
| 频率/模式/几何/ZPE | — | DHR-s0opt.log+.fchk、DHR-s1opt.log+.fchk | opt freq 作业（水） |
| 重组能 λ | 1748.98 / 1746.51 cm⁻¹ | evc.cart.dat | `Total reorganization energy` 行 |
| ZPE 差 | −638.36 cm⁻¹ | 同上 / 两 log 的 `Zero-point correction` | 0-0 修正 |
| Duschinsky S | 55.85% | evc.cart.dat | `BEGIN_DUSH_1` 后矩阵 |
| Ead | 0.078804 au | s1td.log `E(TD-HF/TD-DFT)` −1151.02771258 减 s0opt.log `SCF Done` −1151.10651698 | 垂直发射口径 |
| EDMA | 6.93 D | s0td.log `Dip. S.` state1=7.4283 | √×2.5417 |
| EDME | 7.25 D | s1td.log `Dip. S.` state1=8.1315 | √×2.5417 |
| NAC（仅 kic） | — | DHR-s1-nacme.log | `prop=(fitcharge,field)` → evc.cart.nac |

一句话：Gaussian 给几何/频率/能量/偶极 → evc 缝合成两态势能面间的振动学（S、D、HR、λ）→ kr 用 Ead 定位、EDME 定强度、evc 数据铺振动结构，积分出光谱与速率。

## 相关笔记

- [[MOMAP 3  Duschinsky旋转矩阵和振动分析]]
- [[MOMAP 4 荧光光谱计算]]
- [[MOMAP 5 NACME]]
- [[MOMAP 7 QC准备]]
- [[MOMAP光谱+速率.canvas]]