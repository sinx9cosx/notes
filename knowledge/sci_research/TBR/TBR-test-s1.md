---
tags:
  - 计算化学
  - Gaussian
  - research
Category:
  - 笔记
---
## s1 opt

目标：优化激发态s1结构

输入文件：`TBR-s1opt.com`

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：优化成功，没有虚频


## s1 td

目标：s1的发射情况

输入文件：`TBR-s1td.com`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：Excited State   1:      Singlet-A      2.0554 eV  603.22 nm  f=0.2105  
     135 ->136 （HOMO->LUMO）        0.68425
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54373777

$$
\begin{aligned}
&k_{r}=3.9\times 10^{7}s^{-1}\\ \\
&\tau_{r}=26 ns
\end{aligned}
$$

## s1 nacme

目标：S1几何性质

输入文件：`TBR-s1-nacme.com`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)
`
结果：

跃迁偶极矩
Ground to excited state transition electric dipole moments (Au):
       state          X           Y           Z        Dip. S.      Osc.
         1         1.2787     -1.5955      0.0000      4.1807      0.2105

（|μ| = √4.1807 ≈ 2.045 a.u. ≈ 5.2 Debye，面内偏振；f=0.2105 与 s1 td 一致 ✓）

ESP电荷：
19  C   -0.309325
22  C    0.307953
25  C   -0.216200

注：此 ESP 电荷来自 **S0→S1 跃迁密度**拟合（prop=field 触发），不是基态电荷，物理含义是 S0→S1 电子转移图：C22（+）为电子到达端，C19/C25（−）为空穴端。C2 关联原子对精确反号 → S1 为 B 对称态（面内偏振），激发局域在五元环。

HOMO-LUMO能隙：
最后一个Alpha  occ. eigenvalues --  -0.22187 Hartree
第一个Alpha virt. eigenvalues --   -0.06991

（能隙 = 0.15196 Ha ≈ 4.135 eV）

补充：
- ⚠ **log 中无 NAC 输出**：该 IOP 配方需两步（先 `iop(9/40=1)` 存 chk，再 `td=read` 读取），且即使成功也只输出激发态间耦合，**不含 S0–S1**。S0–S1 耦合需换程序或数值微分。
- SCF 能量 E(S0@S1几何) = −1610.61927151 Ha（与 s0opt.log 的 E(S0@S0几何) 相减即得重组能 λ）
- S1 几何下 20 个激发态，关键态如下：

| 态 | 能量 | f | 主导组态 |
| --- | --- | --- | --- |
| S1 | 2.0554 eV | 0.2105 | 135→136 (0.684) |
| S2 | 2.7840 eV | 0.0001 | 133→136 (0.656) |
| S3 | 2.9153 eV | 0.4916 | 134→136 (0.665) |

> S2/S3 近简并对沿弛豫重排：S0 几何下 S2=134→136（亮）与 S3=133→136（暗）仅差 0.006 eV；S1 几何下次序翻转。S1→S2 能隙仅 0.73 eV。

## s1 NTO

目标：电荷转移的方向

输入文件：`TBR-s1-NTO.gjf`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：

Alpha virt. eigenvalues --    0.97683 
由唯一一对空穴-电子主导的激发。
135：
![[TBR-S1-NTO135.png]]

![[TBR-S1-NTO136.png]]

> HOMO和LUMO都主要分布在 π 共轭骨架，二者具有较明显空间重叠。
