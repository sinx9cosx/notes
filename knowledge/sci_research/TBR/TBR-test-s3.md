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

打开`TBR-s3opt.log`，`Displacement`输入了$\pm 0.3$并保存结构。<mark style="background: #FFB8EBA6;">为什么</mark>

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