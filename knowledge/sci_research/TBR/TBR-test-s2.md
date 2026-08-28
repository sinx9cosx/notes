---
tags:
  - 计算化学
  - Gaussian
  - research
Category:
  - 笔记
---
## s2 opt

目标：优化激发态s2结构

输入文件：`TBR-s2opt.com`

关键词：`# opt freq td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：优化成功，没有虚频，没有态翻转

<mark style="background: #FFB8EBA6;">几何结构：</mark>

## s2 td

目标：s2的发射情况

输入文件：`TBR-s2td.com`

关键词：`# td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：：Excited State   2:      Singlet-A      2.8864 eV  429.55 nm  f=0.5448 
     134 ->136         0.65149
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.51766487

## s2 NTO

目标：电荷转移情况

输入文件：`TBR-s2-NTO.com`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=2) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：