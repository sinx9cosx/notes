---
tags:
  - Gaussian
  - 计算化学
  - research
Category:
  - 笔记
---
## s10 opt

输入文件：`TBR-s10opt.gjf`

关键词：`# opt freq td(nstate=20,root=10) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：几何结构收敛，有一个虚频-802.1719

————正负移动0.2————

## s10 opt+freq plus

输入文件：`TBR-s10-opt-plus.gjf`和`TBR-s10freq-plus.gjf`

关键词：`# opt(+)freq td(nstate=20,root=10) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：几何结构收敛，有一个虚频-1386.0280

## s10 opt+freq minus

输入文件：`TBR-s10-opt-minus.gjf`和`TBR-s10freq-minus.gjf`

关键词：`# opt(+)freq td(nstate=20,root=10) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：几何结构收敛，有一个虚频-1386.0280

**比较两个结构的频率和state 10的 E(TD-HF/TD-DFT)一致，确认为同一结构**
Excited State  10:      Singlet-A      4.0797 eV  303.90 nm  f=0.7008 
     130 ->136         0.14484
     133 ->139        -0.27875
     133 ->141         0.16383
     134 ->137        -0.23387
     135 ->140         0.48532
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.47691239

初步判断交叉落在0和0.2之间

沿`TBR-s10-opt`的结构位移0.05，0.10，0.15做单点计算，得到s10和s9的能隙随位移的变化曲线

## s9-s10-td

输入文件：
`TBR-s10-1.gjf`对应位移0.05
`TBR-s10-2.gjf`对应位移0.10
`TBR-s10-3.gjf`对应位移0.15

关键词：`td(nstate=25) cam-b3lyp/6-31g(d,p) scrf em=gd3bj`

结果：