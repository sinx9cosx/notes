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

目标：S1->S0内转换

输入文件：`TBR-s1-nacme.com`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)
`
结果：

跃迁偶极矩
Ground to excited state transition electric dipole moments (Au):
       state          X           Y           Z        Dip. S.      Osc.
         1         1.2787     -1.5955      0.0000      4.1807      0.2105

ESP电荷：
19  C   -0.309325
22  C    0.307953
25  C   -0.216200

HOMO-LUMO能隙：
最后一个Alpha  occ. eigenvalues --  -0.22187 Hartree
第一个Alpha virt. eigenvalues --   -0.06991

## s1 NTO

目标：电荷转移的方向

输入文件：`TBR-s1-NTO.gjf`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：

Alpha virt. eigenvalues --    0.97683 