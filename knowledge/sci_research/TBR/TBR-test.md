---
Category:
  - 笔记
tags:
  - 计算化学
  - research
  - Gaussian
---
## s0 opt

目标：优化基态结构（实验的那种）

输入文件：`TBR-s0opt.com`

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) scrf em=gd3bj`

结果：优化成功没有虚频

## s0 td

目标：

输入文件：`TBR-s0td.com`

关键词：`# td(nstates=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read geom=check`

结果：只有一次excitation energies and oscillator strengths



# s1 opt

目标：优化激发态s1结构

输入文件：`TBR-s1opt.com`

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：

## s3 opt

目标：优化激发态s3结构

输入文件：`TBR-s3opt.com`

关键词：`# opt freq td(nstate=20,root=3) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：

