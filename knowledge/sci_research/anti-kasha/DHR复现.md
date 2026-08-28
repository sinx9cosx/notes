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
Excited State 1: 1.9357 eV 640.53 nm f=0.3856
97->98 0.69521

Excited State 2: 2.6682 eV 464.67 nm f=0.0206
95->98 0.12255
96->100 0.12726
97->99 0.67256

## s1 NTO

目标：电子转移情况

输入文件：`DHR-s1-NTO.gjf`

old chk：`DHR-s1td.chk`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：

## s2 opt

输入文件：`DHR-s2opt.gjf`

关键词：`# opt freq td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：优化成功，无虚频

## s2 td

输入文件：`DHR-s2td.gjf`

关键词：`td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：
Excited State 2: 2.2135 eV 560.13 nm f=0.0349
97->99 0.68047
97->100 0.10262

## s2 NTO

目标：电子转移情况

输入文件：`DHR-s2-NTO.gjf`

old chk：`DHR-s2td.chk`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=2) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：