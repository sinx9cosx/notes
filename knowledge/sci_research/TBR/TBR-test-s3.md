---
tags:
  - 计算化学
  - Gaussian
  - research
Category:
  - 笔记
---

## s3 opt

目标：优化激发态s3结构

输入文件：`TBR-s3opt.com`

关键词：`# opt freq td(nstate=20,root=3) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：最后一次Converged?的Maximum Displacement是NO，但是只差0.000004，有一个虚频-733.4626$cm^{-1}$，分子振动模式是整体伸缩

打开`TBR-s3opt.log`，`Displacement`输入了$\pm 0.3$并保存结构。

## s3 td

目标：为计算NTO做准备

输入文件：`TBR-s3td.com`

关键词：`# td(nstate=20,root=3) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：
Excited State 3: 2.9299 eV 423.17 nm f=0.4999
131->136 0.13427
134->136 0.65479
134->137 0.11256
135->136 -0.11246

## s3 NTO

目标：电荷转移情况

输入文件：`TBR-s3-NTO.gjf`

old chk：`TBR-s3td.chk`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=3) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：

## s3 opt plus 0.3

目标：优化激发态s3结构

输入文件：`TBR-s3-plus.gjf`

关键词：`# opt freq td(nstate=20,root=3) cam-B3LYP/6-31g(d,p) scrf em=gd3bj
`
结果：几何优化收敛，但是频率没算上，文件没有终止信息。
## s3 opt minus 0.3

目标：优化激发态s3结构

输入文件：`TBR-s3-plus.gjf`

关键词：`# opt freq td(nstate=20,root=3) cam-B3LYP/6-31g(d,p) scrf em=gd3bj

结果：几何优化收敛，频率没计算上，文件没有终止信息。

——确认为同一个结构，接下来进行频率计算——

## s3 freq

目标：确认没有虚频

输入文件：`TBR-s3freq.com`

关键词：`# freq td(nstate=20,root=3) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read geom=check`

结果：有一个虚频，-224.7992（推测是混合态的几何）

