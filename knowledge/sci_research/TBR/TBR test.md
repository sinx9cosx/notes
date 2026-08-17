---
tags:
  - 计算化学
  - research
Category:
  - 笔记
---
## s0 opt

目标：基态结构优化

输入文件：`TBR-s0opt.com`

关键词：`# opt freq B3LYP/def2svp scrf em=gd3bj`

结果：优化成功，无虚频

## s0 td

目标：计算吸收，看一下有没有高激发态

输入文件：`TBR-s0td.gjf`

关键词：`#p B3LYP/def2svp scrf em=gd3bj td=(singlets,nstates=20) geom=allcheck`

结果