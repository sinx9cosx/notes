---
tags:
  - 计算化学
  - MOMAP
  - 量子力学
Category:
  - 讲义
---

# Huang-Rhys 因子与电声耦合

## 1. Huang-Rhys 因子的物理定义

Huang-Rhys 因子 $S_k$（笔记中常记为 HR）描述的是第 $k$ 个振动模式在电子跃迁过程中平均激发的振动量子数。它量化了电子态改变时，原子核平衡位置发生位移所导致的振动激发程度。

两种常用的等价表达式为：

$$
S_k = \frac{1}{2}\delta_k^2
$$

其中 $\delta_k$ 为**无量纲位移**。

$$
S_k = \frac{\omega_k \Delta Q_k^2}{2\hbar}
$$

其中 $\Delta Q_k$ 为该模式在两个电子态势能面之间的**简正坐标位移**，$\omega_k$ 为振动频率。

> [!note] 核心结论
> $S_k$ 越大，说明电子跃迁时该振动模式被激发的程度越高，光谱中出现的振动子峰越强。

---

## 2. 严格量子力学推导

### 2.1 两电子态的谐振子势能面

考虑第 $k$ 个振动模式，其初态（$i$）和末态（$f$）的谐振子势能面分别为：

$$
V_i = \frac{1}{2}\omega_k^2 Q_k^2
$$

$$
V_f = \frac{1}{2}\omega_k^2 (Q_k - \Delta Q_k)^2 + E_{ad}
$$

其中 $E_{ad}$ 为绝热激发能，$\Delta Q_k$ 为两态势能面平衡位置的简正坐标位移。

### 2.2 无量纲位移与产生湮灭算符

引入无量纲位移：

$$
\delta_k = \sqrt{\frac{\omega_k}{\hbar}} \Delta Q_k
$$

利用谐振子的产生/湮灭算符 $a^\dagger, a$，简正坐标可写为：

$$
Q_k = \sqrt{\frac{\hbar}{2\omega_k}}(a^\dagger + a)
$$

初态（$i$）的振动基态记为 $|\\chi_{i,0}\\rangle$，对应真空态 $|0\\rangle$。末态（$f$）的势能面相对于初态发生了平移，其基态可通过**位移算符**（Displacement Operator）作用在初态基态上得到：

$$
D(\\alpha) = \\exp(\\alpha a^\dagger - \\alpha^* a), \\quad \\alpha = \\frac{\delta_k}{\sqrt{2}}
$$

末态势能面的第 $v$ 个振动本征态与初态基态的重叠积分即为 Franck-Condon 因子：

$$
\\langle \\chi_{f,v} | \\chi_{i,0} \\rangle = \\langle v | D(\\alpha) | 0 \\rangle
$$

### 2.3 Franck-Condon 因子的解析形式

位移算符作用在真空态上产生一个相干态：

$$
D(\\alpha)|0\\rangle = |\\alpha\\rangle = e^{-|\\alpha|^2/2} \\sum_{v=0}^{\\infty} \\frac{\\alpha^v}{\\sqrt{v!}} |v\\rangle
$$

因此，一维 Franck-Condon 因子的模方可直接读出：

$$
|\\langle v | 0 \\rangle|^2 = \\frac{e^{-S_k} S_k^v}{v!}, \\quad S_k = |\\alpha|^2 = \\frac{\delta_k^2}{2}
$$

这正是**泊松分布**（Poisson distribution）！

### 2.4 平均振动量子数

由泊松分布的统计性质，其均值为：

$$
\\langle v \\rangle = \\sum_{v=0}^{\\infty} v \\cdot \\frac{e^{-S_k} S_k^v}{v!} = S_k
$$

> [!tip] 关键推导结果
> Huang-Rhys 因子 $S_k$ 的严格量子力学意义即为：电子跃迁后，第 $k$ 个振动模式平均被激发的振动量子数。

---

## 3. 与重组能的关系

单模式重组能 $\lambda_k$ 定义为将该模式从初态平衡位置移动到末态平衡位置所需的能量，它与 Huang-Rhys 因子的关系极为简洁：

$$
\\lambda_k = S_k \\cdot \\hbar\\omega_k
$$

对所有振动模式求和，得到**总重组能**：

$$
\\lambda = \\sum_k \\lambda_k = \\sum_k S_k \\hbar\\omega_k
$$

> [!note] 重组能的物理图像
> 重组能反映了两个电子态势能面在几何结构上的差异所带来的能量代价。重组能越大，说明跃迁前后的几何变化越剧烈，Stokes 位移也越大。

---

## 4. 在 Fermi 黄金规则中的角色

分子体系中的辐射或非辐射跃迁速率通常由 Fermi 黄金规则给出：

$$
\\Gamma = \\frac{2\\pi}{\\hbar}|H'|^2 \\rho(E_f)
$$

其中 $H'$ 为微扰哈密顿量。在分子体系中，终态密度 $\rho(E_f)$ 被替换为**Franck-Condon 加权态密度**（Franck-Condon Weighted Density of States, FCWD），它综合了所有振动模式的贡献：

$$
\\text{FCWD} = \\sum_{\\{v_k\\}} \\left( \\prod_k \\frac{e^{-S_k} S_k^{v_k}}{v_k!} \\right) \\delta\\left(E_{i,0} - E_{f,\\{v_k\\}}\\right)
$$

> [!warning] Huang-Rhys 因子的核心作用
> FCWD 中每个振动模式的贡献以泊松分布 $e^{-S_k}S_k^{v_k}/v_k!$ 的形式出现。因此，$S_k$ 直接决定了各振动子峰的相对强度：$S_k$ 大的模式，其 $v_k \\geq 1$ 的峰越强。

---

## 5. MOMAP 中的具体体现

MOMAP 的 `evc` 模块完成电声耦合计算后，会在 `evc.cart.dat` 文件中输出各振动模式的耦合信息。各列含义如下：

| 列名 | 符号 | 物理含义 |
| :--- | :--- | :--- |
| `freq` | $\omega_k$ | 振动频率（单位通常为 cm⁻¹） |
| `D` | $\Delta Q_k$ | 质量加权坐标位移 |
| `delta` | $\delta_k$ | 无量纲位移 |
| `HR` | $S_k = \\frac{1}{2}\\delta_k^2$ | Huang-Rhys 因子 |
| `lam` | $\lambda_k = \\text{HR} \\cdot \\hbar\\omega_k$ | 该模式的重组能 |

> [!warning] 注意平动转动伪模式
> `evc.cart.dat` 文件的前 6 行对应平动和转动伪模式（频率接近 0），这些不是真实的分子振动，在分析 Huang-Rhys 因子和重组能时必须忽略。

典型的数据读取方式：从第 7 行开始，筛选 `HR` 值显著大于 0 的模式，这些模式对光谱的振动精细结构有实质性贡献。

---

## 6. 物理图像与判断标准

根据 Huang-Rhys 因子的大小，可以定性判断该模式在光谱中的表现：

| HR 取值范围 | 物理图像 | 光谱表现 |
| :--- | :--- | :--- |
| **HR ≈ 0** | 该模式在跃迁中几乎不被激发 | 对振动结构无贡献，$v=0$ 峰占绝对主导 |
| **HR ≈ 1** | 振动激发程度中等 | 0-0、0-1、0-2 等峰的强度可比，振动结构明显 |
| **HR ≫ 1** | 多声子过程主导 | 谱带显著变宽，出现大量高量子数振动峰，Stokes 位移大 |

> [!example] 举例
> 若第 15 个模式的 HR 为 1.2，而其余模式的 HR 均小于 0.1，则荧光光谱中 0-1 峰将主要对应第 15 个模式的单量子激发，该振动峰将成为光谱中最显著的振动子峰。

---

## 7. 与 Duschinsky 旋转的区分

Huang-Rhys 因子与 Duschinsky 旋转是描述电声耦合的两个独立但互补的概念：

| 概念 | 数学描述 | 物理图像 |
| :--- | :--- | :--- |
| **Huang-Rhys 因子** | $S_k = \\frac{1}{2}\\delta_k^2$ | 描述**同一振动模式**在两个电子态势能面上的平衡位置**位移**（平移） |
| **Duschinsky 旋转** | $\mathbf{Q}_f = \\mathbf{J} \\mathbf{Q}_i + \\boldsymbol{\\Delta}$ | 描述**不同振动模式之间**的混合（旋转），即两个电子态的简正坐标系不完全平行 |

> [!note] 综合作用
> 两者共同决定光谱的振动精细结构：HR 决定"峰有多强"，Duschinsky 旋转决定"峰之间如何混合"。在简谐近似且 Duschinsky 效应较弱时，光谱可近似为各模式独立泊松分布的卷积。

---

## 8. 相关笔记链接

- [[Fermi黄金规则]]
- [[MOMAP 3  Duschinsky旋转矩阵和振动分析]]
- [[MOMAP 荧光光谱与速率：完整流程与结果解读]]
- [[MOMAP 4 荧光光谱计算]]
- [[MOMAP 5 NACME]]
