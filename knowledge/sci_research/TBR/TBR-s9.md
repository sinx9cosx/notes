---
tags:
  - 计算化学
  - Gaussian
  - research
Category:
  - 笔记
---
## s9 opt

oldchk：s0opt

输入文件：`TBR-s9opt.gjf`

关键词：`# opt td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：normal termination
 Excited State   9:      Singlet-A      3.8699 eV  320.38 nm  f=1.1292 
     131 ->136         0.30605
     133 ->139         0.14421
     134 ->137        -0.53645
     135 ->140        -0.24262
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.48466851
## s9 freq

oldchk：s9opt

输入文件：`TBR-s9freq.gjf`

关键词：`# freq td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：
## s9 td

## s9 NTO

## s9 nacme