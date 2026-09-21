---
Category:
  - 笔记
tags:
  - 计算化学
  - research
---

# Frank-Condon 因子

## 1. 定义与核心结论

电子跃迁（如 $S_0 \to S_1$ 吸收、$S_1 \to S_0$ 荧光）发生在两个**不同的电子态势能面**之间。初、末总态分别是电子波函数与振动波函数的乘积，其中振动部分属于各自的势能面。

定义：两个不同电子态势能面上的振动波函数重叠积分的模方，称为 **Franck-Condon 因子**（FC 因子）：

$$
|\langle \chi_{f,v'} \mid \chi_{i,v} \rangle|^2
$$

其中 $\chi_{i,v}$ 是初电子态势能面上第 $v$ 个振动本征态，$\chi_{f,v'}$ 是末电子态势能面上第 $v'$ 个振动本征态。

<mark style="background: #FFB86CA6;">跃迁强度公式（Condon 近似下）</mark>：

$$
I \propto |\mu_{fi}|^2 \cdot |\langle \chi_{f,v'} \mid \chi_{i,v} \rangle|^2
$$

其中 $\mu_{fi}$ 是初末电子态之间的电子跃迁偶极矩。

<mark style="background: #BBFABBA6;">一句话总结：</mark> $|\mu_{fi}|^2$ 决定整条谱带的**总强度**（这个电子跃迁允不允许、有多强），FC 因子决定总强度在**各振动子峰之间如何分配**——即光谱的振动精细结构。FC 因子本身不含任何电子态信息，纯由两态势能面的几何关系（位移、频移、模式混合）决定。

## 2. 问题由来：一个选律矛盾

在[[光谱选律]]中推导过：**纯振动跃迁**（红外光谱，初末态在同一电子态的同一势能面内）的选律是 $\Delta v = \pm 1$。推导的关键有两步：

- 同一势能面内的谐振子波函数正交：$\langle \chi_{i,v} \mid \chi_{i,v'} \rangle = \delta_{vv'}$
- $x$ 的矩阵元只连接相邻能级，由递推公式 $x\psi_{m} = \sqrt{\frac{m+1}{2\beta}}\psi_{m+1} + \sqrt{\frac{m}{2\beta}}\psi_{m-1}$ 保证

但实验上分子**电子光谱**是带状的（见[[光谱分类总览]]：电子光谱位于 UV-Vis 区，电子跃迁叠加振动精细结构呈带状），一条电子跃迁带内包含大量振动子峰，初末振动量子数 $v \to v'$ 似乎可以任意取值，没有 $\Delta v = \pm 1$ 的限制。

**问题：为什么电子跃迁不受 $\Delta v = \pm 1$ 限制？**

答案在下面的推导中：电子跃迁的初末振动波函数**属于不同的势能面**，彼此不正交，因此选律推理的第一块基石（正交性）不存在了。

## 3. 推导主线：从跃迁偶极矩到 FC 因子

### 3.1 起点：跃迁概率 ∝ |R_mn|²

根据[[电磁波照射下的跃迁概率公式]]，单位时间的跃迁概率（各向同性连续谱情形）：

$$
\frac{P_{nm}}{t_1} = \frac{8\pi^3}{3h^2} R_{mn}^2 \rho(\nu_{mn})
$$

其中 $R_{mn} = \langle m | \hat{R} | n \rangle$ 是初末态之间的跃迁电偶极矩，跃迁概率与 $R_{mn}^2$ 成正比。分子电子光谱的振动精细结构全部藏在 $R_{mn}$ 里，下面把它具体算出来。

### 3.2 Born-Oppenheimer 近似：波函数分离

在 Born-Oppenheimer 近似下（见[[光谱分类总览]]：$E = E_{电子} + E_{振动} + E_{转动}$），分子总波函数写为电子部分与振动部分的乘积：

$$
\Psi = \psi_{el}(r; Q)\,\chi_{vib}(Q)
$$

注意记号 $\psi_{el}(r;Q)$：电子波函数是电子坐标 $r$ 的函数，以核坐标 $Q$ 为**参数**——核构型变化时电子波函数随之变化，但电子运动本身在 $r$ 上积分。

设初态为电子态 $i$、振动量子数 $v$，末态为电子态 $f$、振动量子数 $v'$：

$$
\Psi_{i,v} = \psi_{el,i}(r;Q)\,\chi_{i,v}(Q), \qquad \Psi_{f,v'} = \psi_{el,f}(r;Q)\,\chi_{f,v'}(Q)
$$

### 3.3 偶极算符拆分：电子部分与核部分

体系的偶极矩算符 = 电子的贡献 + 核的贡献：

$$
\hat{\mu} = \hat{\mu}_e + \hat{\mu}_N = -e\sum_j \hat{r}_j + \sum_A Z_A e \hat{R}_A
$$

（$j$ 遍历电子，$A$ 遍历核。）代入跃迁偶极矩：

$$
R_{fi} = \langle \Psi_{f,v'} | \hat{\mu}_e + \hat{\mu}_N | \Psi_{i,v} \rangle
$$

先对电子坐标 $r$ 积分（此时核坐标 $Q$ 是固定参数），两项分别写成：

**电子项**

$$
\int \chi_{f,v'}^*(Q) \left[ \int \psi_{el,f}^*(r;Q)\,\hat{\mu}_e\,\psi_{el,i}(r;Q)\,dr \right] \chi_{i,v}(Q)\,dQ
$$

**核项**

$$
\int \chi_{f,v'}^*(Q)\,\hat{\mu}_N(Q) \left[ \int \psi_{el,f}^*(r;Q)\,\psi_{el,i}(r;Q)\,dr \right] \chi_{i,v}(Q)\,dQ
$$

### 3.4 核偶极项消失：电子态正交

核项方括号里的积分是

$$
\int \psi_{el,f}^*(r;Q)\,\psi_{el,i}(r;Q)\,dr = \langle \psi_{el,f} \mid \psi_{el,i} \rangle_{el}
$$

在固定核构型 $Q$ 下，$\psi_{el,i}$ 和 $\psi_{el,f}$ 是同一电子哈密顿量 $\hat{H}_{el}(Q)$ 的两个不同本征态，**彼此正交**：

$$
\langle \psi_{el,f} \mid \psi_{el,i} \rangle_{el} = 0
$$

所以核偶极项**整个为零**。物理上：核偶极矩只能"拨动"核，不能改变电子态——电子跃迁完全由 $\hat{\mu}_e$ 驱动。这是与红外振动光谱（由分子永久偶极矩随核坐标的变化驱动）的本质区别。

### 3.5 电子跃迁偶极矩 $\mu_{fi}(Q)$

电子项方括号里的积分记为

$$
\mu_{fi}(Q) = \langle \psi_{el,f} \mid \hat{\mu}_e \mid \psi_{el,i} \rangle_{el} = \int \psi_{el,f}^*(r;Q)\,\hat{\mu}_e\,\psi_{el,i}(r;Q)\,dr
$$

称为**电子跃迁偶极矩**。注意它仍是核坐标 $Q$ 的函数：不同核构型下电子云不同，偶极矩也不同。于是

$$
R_{fi} = \int \chi_{f,v'}^*(Q)\,\mu_{fi}(Q)\,\chi_{i,v}(Q)\,dQ
$$

到这里为止还没有做任何近似。

### 3.6 Condon 近似

Condon 近似的核心假定：$\mu_{fi}(Q)$ 随 $Q$ 变化**缓慢**（电子跃迁偶极矩对核构型不敏感）。将它绕初态势能面平衡位置 $Q_0$ 展开：

$$
\mu_{fi}(Q) = \mu_{fi}(Q_0) + \sum_k \left( \frac{\partial \mu_{fi}}{\partial Q_k} \right)_{Q_0} (Q_k - Q_{0,k}) + \cdots
$$

只保留第一项（高阶项对应 Herzberg-Teller 修正，见 §9），常数 $\mu_{fi}(Q_0)$ 提出积分外：

$$
R_{fi} \approx \mu_{fi}(Q_0) \int \chi_{f,v'}^*(Q)\,\chi_{i,v}(Q)\,dQ = \mu_{fi}(Q_0)\,\langle \chi_{f,v'} \mid \chi_{i,v} \rangle
$$

<mark style="background: #FFB86CA6;">Condon 近似下的跃迁偶极矩</mark>：

$$
R_{fi} \approx \mu_{fi}(Q_0)\cdot\langle \chi_{f,v'} \mid \chi_{i,v} \rangle
$$

取模方得跃迁强度：

$$
I \propto |R_{fi}|^2 = |\mu_{fi}(Q_0)|^2 \cdot |\langle \chi_{f,v'} \mid \chi_{i,v} \rangle|^2
$$

其中 $|\langle \chi_{f,v'} \mid \chi_{i,v} \rangle|^2$ 就是 Franck-Condon 因子。

<mark style="background: #BBFABBA6;">结论：</mark> 电子跃迁偶极矩 $\mu_{fi}$ 只出现一次，对整个跃迁带是**公共因子**；各振动子峰的相对强度完全由 FC 因子决定。这就是"电子跃迁的强度分配交给振动重叠积分"的来历。

## 4. 物理图像：垂直跃迁（Franck-Condon 原理）

### 4.1 时间尺度论证

- 电子运动的特征时间：$\sim 10^{-15}$ s（可见/紫外光子的周期、电子绕核运动周期同量级）；
- 核振动的周期：振动频率 $\tilde{\nu} = 100 \sim 3000\ \mathrm{cm}^{-1}$，对应周期

$$
T_{vib} = \frac{1}{c\,\tilde{\nu}} \sim \frac{1}{3\times 10^{10}\ \mathrm{cm/s} \times 10^{3}\ \mathrm{cm}^{-1}} = 3\times 10^{-14}\ \mathrm{s}
$$

即 $10^{-14} \sim 10^{-13}$ s。

> [!note] 时间尺度对比
> 电子跃迁（$10^{-15}$ s 量级）比核振动（$10^{-14} \sim 10^{-13}$ s 量级）快 1~2 个数量级。电子"跳"的这一瞬间，核还来不及完成一次振动，因此跃迁过程中核坐标 $Q$ 视为**冻结**。

### 4.2 势能面图上的竖直箭头

既然跃迁过程中 $Q$ 不变，在势能面图上跃迁就是一个**竖直箭头**：从始态（通常 $v=0$，波函数峰值在初态势能面平衡位置 $Q_0$ 处）竖直向上（吸收）投射到末态势能面上。

经典图像：从始态平衡位置竖直投射，落点在上态势能面上的某个能量处。在该能量附近，末态振动波函数振幅最大的那个 $v'$（大致是经典转折点与落点重合的态）FC 因子最大。

<mark style="background: #BBFABBA6;">最重要的推论：</mark> 跃迁最强的终态 $v'$ 是**波函数重叠最大的那个**，而不是能量差最小的那个。重叠最大的位置对应"竖直投影点"附近的 $v'$，它一般比 $v' = 0$ 高——所以吸收谱中最强峰往往不是 0-0 峰（$S$ 较大时尤其如此，见 §7.1）。

### 4.3 易混点：原理 vs 因子

> [!warning] Franck-Condon 原理 vs Franck-Condon 因子
> - **FC 原理**：经典陈述——跃迁瞬时完成、核几何冻结、势能面图上垂直跃迁。它是**物理图像**。
> - **FC 因子**：量子重叠积分 $|\langle \chi_{f,v'} \mid \chi_{i,v} \rangle|^2$。它是原理的**定量表达**。
>
> 两者常被混用。严格地说，强度分配依据的是重叠积分（量子说法），"垂直跃迁"只是它的经典近似图像；当波函数弥散较大时（低质量原子、软模式），垂直图像会偏差，重叠积分仍是准的。

## 5. 为什么电子跃迁中 Δv 不受限

对比两种情形：

### 5.1 同一电子态（红外振动光谱）：Δv = ±1

纯振动跃迁的初末振动波函数属于**同一个势能面**：

$$
R_{mn} = \langle \chi_{i,v} | \hat{\mu}(Q) | \chi_{i,v'} \rangle
$$

- 正交性：$\langle \chi_{i,v} \mid \chi_{i,v'} \rangle = \delta_{vv'}$
- 偶极矩展开保留 $Q$ 的一次项后，矩阵元 $\propto \langle v | Q | v' \rangle \propto \langle v | a^\dagger + a | v' \rangle$，只连接 $\Delta v = \pm 1$ 的态（见[[光谱选律]]中线性谐振子部分）

### 5.2 不同电子态（电子光谱）：任意 v → v'

电子跃迁的初末振动波函数属于**两个不同的势能面**：

$$
\langle \chi_{f,v'} \mid \chi_{i,v} \rangle \neq \delta_{vv'}
$$

不同势能面的波函数之间**没有正交性**，重叠积分可以取 0 到 1 之间的任意值（只受完备性约束 $\sum_{v'} |\langle \chi_{f,v'} \mid \chi_{i,v} \rangle|^2 = 1$——初态 $v$ 的强度必定全部"分配"给所有可能的 $v'$）。

<mark style="background: #BBFABBA6;">一句话：</mark> 红外选律 $\Delta v = \pm 1$ 来自"同一势能面 + 正交性 + $Q$ 一次项"三件事的配合；电子跃迁打破了第一件（初末在不同势能面），所以 $\Delta v$ 不再受限，任意 $v \to v'$ 都有强度，具体数值由 FC 因子定量给出。

## 6. 一维解析解：泊松分布

（本节与[[Huang-Rhys因子与电声耦合]]互为补充：那里以 HR 因子为主线推导，这里以 FC 因子为主线重走完整推导。）

### 6.1 模型

两个电子态都是简谐势能面，**频率相同**（都取 $\omega$），末态相对初态整体平移 $\Delta Q$：

$$
V_i = \frac{1}{2}\omega^2 Q^2, \qquad V_f = \frac{1}{2}\omega^2 (Q - \Delta Q)^2 + E_{ad}
$$

其中 $E_{ad}$ 是绝热激发能（两势能面最低点之差）。

### 6.2 无量纲位移与 Huang-Rhys 因子

定义无量纲位移：

$$
\delta = \sqrt{\frac{\omega}{\hbar}}\,\Delta Q
$$

Huang-Rhys 因子：

$$
S = \frac{\delta^2}{2} = \frac{\omega\,\Delta Q^2}{2\hbar}
$$

（$S$ 的物理意义是跃迁后平均激发的振动量子数，下面重新证明。）

### 6.3 产生/湮灭算符与位移算符

谐振子的简正坐标用产生/湮灭算符表示为：

$$
Q = \sqrt{\frac{\hbar}{2\omega}}\,(a^\dagger + a)
$$

末态势能面相对初态势能面平移了 $\Delta Q$，即坐标作平移变换 $Q \to Q + \Delta Q$。量子力学中坐标平移由**位移算符**实现：

$$
D(\alpha) = \exp(\alpha a^\dagger - \alpha^* a), \qquad \alpha = \frac{\delta}{\sqrt{2}}
$$

初态势能面的振动基态记为 $|0\rangle$（真空态）。末态势能面的振动本征态由位移算符从初态势能面的本征态生成，因此 FC 重叠积分化为

$$
\langle \chi_{f,v} \mid \chi_{i,0} \rangle = \langle v | D(-\alpha) | 0 \rangle
$$

（$\alpha = \delta/\sqrt{2} > 0$；末态波函数中心右移 $\Delta Q$，即 $\chi_{f,v} = D(\alpha)|v\rangle$，重叠积分中取其共轭 $D(-\alpha)$；模方与方向无关。）

### 6.4 相干态展开

位移算符作用在真空态上产生**相干态**：

$$
D(\alpha)|0\rangle = e^{-|\alpha|^2/2} \sum_{v=0}^{\infty} \frac{\alpha^v}{\sqrt{v!}}\,|v\rangle
$$

（相干态在数态基下的展开，$v$ 是数态量子数。）

两边与 $\langle v |$ 做内积，利用数态正交归一性 $\langle v | v' \rangle = \delta_{vv'}$：

$$
\langle v | D(-\alpha) | 0 \rangle = e^{-|\alpha|^2/2}\,\frac{(-\alpha)^v}{\sqrt{v!}}
$$

取模方，即得 FC 因子：

$$
|\langle \chi_{f,v} \mid \chi_{i,0} \rangle|^2 = |\langle v | D(-\alpha) | 0 \rangle|^2 = e^{-|\alpha|^2}\,\frac{|\alpha|^{2v}}{v!}
$$

代入 $S = |\alpha|^2 = \delta^2/2$：

<mark style="background: #FFB86CA6;">一维 FC 因子 = 泊松分布</mark>：

$$
|\langle \chi_{f,v} \mid \chi_{i,0} \rangle|^2 = \frac{e^{-S} S^v}{v!}
$$

这正是**泊松分布** $\mathrm{Pois}(S)$。

### 6.5 泊松分布的性质

- **均值**（跃迁后平均激发的振动量子数）：

$$
\langle v \rangle = \sum_{v=0}^{\infty} v \cdot \frac{e^{-S} S^v}{v!} = S
$$

这就是 HR 因子 $S$ 的量子力学意义——电子跃迁后该模式平均被激发的振动量子数。

- **0-0 峰强度**（$v' = 0$）：

$$
|\langle \chi_{f,0} \mid \chi_{i,0} \rangle|^2 = e^{-S}
$$

$S$ 越大，0-0 峰越弱（强度"流失"到高 $v'$ 峰）。

- **最强峰位置**：泊松分布在 $v \approx S$ 处取最大，与"竖直投影点"的经典图像一致——位移越大，最强峰对应的振动量子数越高。

### 6.6 频率不同的情形

若两态势能面频率不同（$\omega_i \neq \omega_f$，即跃迁伴随键的软化或硬化），FC 因子**无简单解析式**。计算思路：频率变化可写成产生/湮灭算符的压缩变换，配合位移算符统一处理（如 Doktorov 方法），或用 Hermite 多项式重叠积分的递推关系数值求解。不展开，实践中交给程序（§11）。

## 7. 谱形预测与实验现象

### 7.1 按 S 分类的谱形

| $S$ 取值 | 物理图像 | 谱形表现 |
| :--- | :--- | :--- |
| $S \approx 0$ | 两态势能面几乎重合，跃迁几乎不激发振动 | 只有 0-0 峰，谱带窄 |
| $S \approx 1$ | 中等程度的振动激发 | 0-0、0-1、0-2 峰强度相当，振动结构清晰 |
| $S \gg 1$ | 多声子过程主导 | 大量子峰叠加，包络趋于高斯，谱带变宽，最强峰远离 0-0 |

（此表与[[Huang-Rhys因子与电声耦合]]中的判断标准一致。）

### 7.2 吸收-发射镜像对称

比较吸收（$S_0(v=0) \to S_1(v')$）与发射（$S_1(v'=0) \to S_0(v)$）两条谱。简谐近似且频率相同时：

$$
|\langle \chi_{f,v} \mid \chi_{i,0} \rangle|^2 = |\langle \chi_{i,v} \mid \chi_{f,0} \rangle|^2 = \frac{e^{-S} S^v}{v!}
$$

吸收包络与发射包络**形状相同**，关于 0-0 峰**镜像对称**。

> [!warning] 破坏镜像对称的因素
> - 频率变化（$\omega_i \neq \omega_f$）：对称性被破坏；
> - Duschinsky 混合（见 §8）：进一步破坏。
>
> 实际分子中激发态通常键更弱（频率更低），发射谱振动结构更"密"，镜像对称只是近似。

### 7.3 Stokes 位移 = 2λ

简谐近似下（单模式，多模式时求和）：

- 吸收能量（从 $S_0$ 平衡位置竖直上跳）：$E_{abs} = T_e + \lambda$
- 发射能量（从 $S_1$ 平衡位置竖直下跳）：$E_{em} = T_e - \lambda$

两者之差即竖直跃迁能量差：

<mark style="background: #FFB86CA6;">Stokes 位移</mark>：

$$
E_{abs} - E_{em} = 2\lambda
$$

其中 $\lambda = \sum_k S_k \hbar\omega_k$ 是重组能（见[[Huang-Rhys因子与电声耦合]]）。重组能越大，几何驰豫越大，吸收峰与发射峰离得越远。

### 7.4 0-0 跃迁能量

0-0 跃迁（两电子态各自振动基态之间）的能量：

$$
E_{00} = T_e + \frac{1}{2}\sum_k \hbar(\omega_{f,k} - \omega_{i,k})
$$

即**绝热能差加零点能差**。上下态频率相同时 $E_{00} = T_e$。

> [!tip] 实验与理论对标
> $E_{00}$ 是实验-理论对标的常用量：实验中取吸收谱与发射谱的交点（镜像对称的交点即 0-0 峰），理论上由绝热激发能加零点能修正得到。

### 7.5 温度效应：热带

- 低温：只有 $v=0$ 布居，吸收从 $v=0$ 出发（"冷带"）；
- 升温：高 $v$ 态按 Boltzmann 因子 $e^{-E_v/k_BT}$ 热布居，吸收谱低能侧出现从 $v>0$ 出发的额外峰——**热带（hot bands）**，例如 $v=1 \to v'=0$ 的跃迁能量为 $E_{00} - \hbar\omega_i$，比 0-0 峰红移一个振动量子。

热带位于 0-0 峰的红侧（低能侧），其相对强度随温度升高而增强，是判断样品热布居的线索。

## 8. 多维推广

真实分子有 $3N-6$ 个振动模式，FC 因子推广到多维：

- **各模式独立**（无 Duschinsky 混合，且各模式频率不变）：总 FC 因子是各模式泊松分布的乘积：

$$
\prod_k \frac{e^{-S_k} S_k^{v_k}}{v_k!}
$$

此时多模式谱形是各模式泊松分布的**卷积**（逐模式展宽）。

- **有 Duschinsky 旋转**（两电子态的简正坐标系不平行）：

$$
Q_f = J Q_i + \Delta
$$

FC 因子不再是简单乘积，需要处理模式之间的混合，见[[MOMAP 3  Duschinsky旋转矩阵和振动分析]]。

## 9. 超出 Condon 近似：Herzberg-Teller 项

若 $\mu_{fi}(Q_0) = 0$（对称性禁阻的电子跃迁），Condon 项整体为零，FC 因子再大也"无米下锅"——跃迁强度恒为零。

把 §3.6 的展开多保留一项（已取初态平衡位置为坐标原点，即 $Q_{0,k}=0$）：

$$
\mu_{fi}(Q) = \mu_{fi}(Q_0) + \sum_k \left( \frac{\partial \mu_{fi}}{\partial Q_k} \right)_{Q_0} Q_k + \cdots
$$

代回跃迁偶极矩，多出一系列项：

$$
R_{fi} = \mu_{fi}(Q_0)\,\langle \chi_{f,v'} \mid \chi_{i,v} \rangle + \sum_k \left( \frac{\partial \mu_{fi}}{\partial Q_k} \right)_{Q_0} \langle \chi_{f,v'} \mid Q_k \mid \chi_{i,v} \rangle + \cdots
$$

第一项是 Condon 项（FC 因子所在），第二项是 **Herzberg-Teller（HT）项**。

<mark style="background: #BBFABBA6;">HT 项的作用：</mark> 让对称性禁阻的跃迁"借"振动强度——只要电子跃迁偶极矩沿某个振动模式变化（导数非零），该模式一量子激发即可使跃迁部分放开。HT 项还常导致允许跃迁中出现对称性较低的"假原点"振动峰。

> [!note] FC / HT / Duschinsky 三件套
> 振动分辨电子光谱理论的三要素：**FC**（几何位移 → 谱线强度分配）、**HT**（跃迁偶极矩的核坐标依赖 → 禁阻跃迁借强度）、**Duschinsky**（模式混合）。对应[[光谱分类总览]]中"振动分辨光谱 | FC/HT/Duschinsky"一栏。

## 10. 在跃迁速率理论中的位置

辐射与非辐射跃迁同出于[[Fermi黄金规则]]框架，FC 因子在其中扮演不同角色：

- **辐射跃迁**（光谱）：跃迁速率（强度）$\propto |\mu_{fi}|^2 \times \mathrm{FC}$。每个振动子峰是一条谱线，强度被 FC 因子标度；FC 因子只是"分配系数"，不改变谱带总强度。
- **非辐射跃迁**（内转换、系间窜越）：终态是准连续的振动态集合，态密度按 FC 因子加权，得到 **FCWD**（Franck-Condon 加权态密度，Franck-Condon Weighted Density of States）：

$$
\mathrm{FCWD} = \sum_{\{v_k\}} \left( \prod_k \frac{e^{-S_k} S_k^{v_k}}{v_k!} \right) \delta\left(E_{i,0} - E_{f,\{v_k\}}\right)
$$

（见[[Huang-Rhys因子与电声耦合]]§4。）此时 FC 因子不仅分配强度，还**直接进入速率**：非辐射速率 $k_{nr} \propto |H'|^2 \times \mathrm{FCWD}$。

> [!tip] 两种"用法"的联系
> 辐射跃迁把 FC 因子"一项一项"看（分立的谱线），非辐射跃迁把 FC 因子"一团一团"卷积（连续的 FCWD）。同一个 FC 因子，两种用法。

## 11. 计算化学实践

- **Gaussian**：FCHT 模块（Franck-Condon / Herzberg-Teller 分析）可做振动分辨光谱模拟；流程是先分别优化两个电子态并算频率，再算 FC/HT/Duschinsky。
- **独立工具**：ezFCF、FCclasses3（衔接[[光谱分类总览]]的表格）。
- **MOMAP** 流程：`evc` 模块读入两电子态的振动分析输出，给出各模式 HR 因子/重组能/Duschinsky 旋转矩阵，之后的光谱模拟模块（衔接[[MOMAP 荧光光谱与速率：完整流程与结果解读]]）用它生成谱。

> [!warning] 提醒
> `evc.cart.dat` 的前 6 行为平动/转动伪模式（频率接近 0），不是真实振动，分析 HR 因子和重组能时必须忽略（衔接[[Huang-Rhys因子与电声耦合]]§5）。

## 12. 注意事项 / 易混淆点

- **FC 原理 vs FC 因子**：原理是经典图像（垂直跃迁），因子是定量重叠积分（见 §4.3），两者常被混用。
- **垂直跃迁是近似**：严格说法是"跃迁最强的终态是波函数重叠最大的态"；经典"竖直箭头"只在波函数局域化好时与之一致。
- **Stokes 位移 = 2λ 与镜像对称**：只在简谐近似（镜像对称还要求频率相同）下严格成立；频率变化或 Duschinsky 混合都会破坏。
- **FC 因子 ≠ 跃迁概率本身**：还差 $|\mu_{fi}|^2$ 这个公共因子；吸收谱线强度还带 $\nu$ 一次方权重（$I_{abs} \propto \nu |\mu_{fi}|^2 \cdot \mathrm{FC}$），发射谱线强度带 $\nu^3$ 权重（$I_{em} \propto \nu^3 |\mu_{fi}|^2 \cdot \mathrm{FC}$；$\nu^3$ 来自 Einstein 自发辐射系数 $A_{m\to n} = 8\pi h \tilde{\nu}_{mn}^3 B_{m \to n}$，见[[电磁波照射下的跃迁概率公式]]）。用 FC 因子跨跃迁比较强度（如吸收 vs 发射）时要小心。
- **0-0 峰可观测的前提是 $S$ 不太大**：$S$ 很大时 $e^{-S} \to 0$，0-0 峰弱到测不出，光谱失去"锚点"。

## 相关笔记

- [[光谱选律]]：$\Delta v = \pm 1$ 选律的推导
- [[Fermi黄金规则]]：跃迁速率的统一框架
- [[电磁波照射下的跃迁概率公式]]：$R_{mn}$ 与 Einstein 系数
- [[光谱分类总览]]：带状光谱与 FC/HT/Duschinsky 三件套
- [[Huang-Rhys因子与电声耦合]]：HR 因子、泊松分布、FCWD、重组能
- [[MOMAP 3  Duschinsky旋转矩阵和振动分析]]：模式混合

## 笔记小记

- [ ] 待补充：频率不同（$\omega_i \neq \omega_f$）时 FC 因子的 Doktorov 公式具体形式
- [ ] 待补充：HT 项的具体计算例子（如苯的 $^1B_{2u} \leftarrow {}^1A_{1g}$ 借模跃迁）
- [ ] 待补充：FC 因子与电子耦合（非绝热耦合）的区分
