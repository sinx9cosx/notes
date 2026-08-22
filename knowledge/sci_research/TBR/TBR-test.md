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

# s1 opt

输入文件

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`