---
tags:
  - 计算化学
  - research
  - Gaussian
  - 后处理
Category:
  - 笔记
---
# s0

## s0 opt

输入文件：`DHR-s0opt.gjf`

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) em=gd3bj`

结果：normal termination

## s0 td

oldchk：s0opt

输入文件：

关键词：

# s1

## s1 opt

oldchk：s0opt

输入文件：`DHR-s1opt.gjf`

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read  geom=check`

## s1 td

oldchk：s1opt

# s2

## s2 opt

oldchk：s0opt

输入文件：`DHR-s2opt.gjf`
## s2 td

oldchk：s2opt

# s9

## s9 opt

oldchk：s0opt

输入文件：`DHR-s2opt.gjf`

## s9 td

oldchk：s9opt