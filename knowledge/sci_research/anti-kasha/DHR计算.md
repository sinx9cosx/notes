---
tags:
  - 计算化学
  - research
  - Gaussian
Category:
  - 笔记
---
## s0 opt

目标：优化s0基态几何结构

输入文件：`DHR-s0opt.gjf`

关键词：`# opt casscf(12,12)/6-31g(d)`

结果：没有优化成功，没有正常终止信息

——换了一个服务器——

结果：异常终止。换关键词，因为文献用的不是Gaussian计算的哎呀。老师说用一样的方法算这个体系

———换关键词——

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) scrf em=gd3bj`

结果：优化成功，没有虚频

## s1 opt

输入文件：`DHR-s1opt.gjf`

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：优化成功，无虚频

## s1 td

输入文件：`DHR-s1td.gjf`

关键词：`td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：

## s2 opt

输入文件：`DHR-s2opt.gjf`

关键词：`# opt freq td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：优化成功，无虚频

## s2 td

输入文件：`DHR-s2td.gjf`

关键词：`td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：