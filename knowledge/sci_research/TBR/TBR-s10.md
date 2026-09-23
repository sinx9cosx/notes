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