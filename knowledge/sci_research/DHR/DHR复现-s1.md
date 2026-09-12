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

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) scrf em=gd3bj`

结果：优化成功，没有虚频
SCF Done:-1151.10651698 a.u.

## s0 td

目标：跃迁偶极矩（吸收）

输入文件：`DHR-s0td.gjf`

关键词：`td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：
Dip.S.（$\mu^2$）：7.4283 a.u.
换算1 a.u.=2.5417 Debye

## s1 opt

输入文件：`DHR-s1opt.gjf`

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：优化成功，无虚频
SCF Done:-1151.09884677 a.u.（s0基态在s1几何下的能量）
Total Energy, E(TD-HF/TD-DFT) =  -1151.03314709
## s1 td

输入文件：`DHR-s1td.gjf`

关键词：`#p td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：
Excited State 1: 1.9357 eV 640.53 nm f=0.3856
97->98 0.69521

Excited State 2: 2.6682 eV 464.67 nm <mark style="background: #FFB8EBA6;">f=0.0206</mark>
95->98 0.12255
96->100 0.12726
97->99 0.67256

Dip. S.：8.1315 a.u.

## s1 nacme

输入文件：`DHR-s1-nacme.gjf`

关键词：`#p td(nstate=20) cam-b3lyp/6-31g(d,p) scrf em=gd3bj guess=read geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

结果：normal termination
## s1 NTO

目标：电子转移情况

输入文件：`DHR-s1-NTO.gjf`

old chk：`DHR-s1td.chk`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：0.98422 由一对空穴->电子轨道贡献

97（空穴轨道）->98（电子轨道）：
  <table><tr>
  <td align="center"><img src="DHR-s1-NTO-97.jpg" width="380"><br>97空穴</td>
  <td align="center"><img src="DHR-s1-NTO-98.jpg" width="380"><br>98电子</td>
  </tr></table>

---

# s2

## s2 opt

输入文件：`DHR-s2opt.gjf`

关键词：`# opt freq td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：优化成功，无虚频

## s2 td

输入文件：`DHR-s2td.gjf`

关键词：`td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：
Excited State 2: 2.2135 eV 560.13 nm f=0.0349（很弱的发射，波长与文献对不上）
97->99 0.68047
97->100 0.10262

## s2 nacme

输入文件：`DHR-s2-nacme.gjf`

关键词：`#p td(nstate=20,root=2) cam-b3lyp/6-31g(d,p) guess=read geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

结果：normal termination

## s2 NTO

目标：电子转移情况

输入文件：`DHR-s2-NTO.gjf`

old chk：`DHR-s2td.chk`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=2) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：0.99014 由一对空穴->电子轨道贡献

97（空穴）->98（电子）：
  <table><tr>
  <td align="center"><img src="DHR-s2-NTO-97.jpg" width="380"><br>97空穴</td>
  <td align="center"><img src="DHR-s2-NTO-98.jpg" width="380"><br>98电子</td>
  </tr></table>


---

