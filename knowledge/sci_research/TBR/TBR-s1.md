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
 Excited State   1:      Singlet-A      1.9879 eV  623.69 nm  f=0.3727 
     135 ->136         0.68700
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54621684

## s1 td

目标：s1的发射情况

输入文件：`TBR-s1td.com`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：Excited State   1:      Singlet-A      2.0554 eV  603.22 nm  f=0.2105  
     135 ->136 （HOMO->LUMO）        0.68425
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54373777

Dip.S.=4.1807 
## s1 nacme

目标：S1几何性质

输入文件：`TBR-s1-nacme.com`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)
`
结果：Excited State   1:      Singlet-A      2.0554 eV  603.22 nm  f=0.2105  
     135 ->136         0.68425
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54373777


## s1 NTO

目标：电荷转移的方向

输入文件：`TBR-s1-NTO.gjf`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：

Alpha virt. eigenvalues --    0.97683 
由唯一一对空穴-电子主导的激发。
135：
![[TBR-S1-NTO135.png]]

136：
![[TBR-S1-NTO136.png]]

> 都主要分布在 π 共轭骨架，二者具有较明显空间重叠。
