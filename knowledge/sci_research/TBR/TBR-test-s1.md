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

目标：看s1的发射情况

输入文件：`TBR-s1td.com`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：

## s1 nacme

目标：<mark style="background: #FFB8EBA6;">为什么</mark>

输入文件：`TBR-s1-nacme.com`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)
`
结果：