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

结果：