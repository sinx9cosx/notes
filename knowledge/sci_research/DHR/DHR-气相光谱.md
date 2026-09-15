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
SCF Done:  E(RCAM-B3LYP) =  -1151.09868773     A.U.
## s0 td

oldchk：s0opt

输入文件：`DHR-s0td.gjf`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read  geom=check`

结果：normal termination

| state | Dip.S. |
| ----- | ------ |
| 1     | 5.1418 |
| 2     | 0.1995 |
| 9     | 3.8736 |
# s1

## s1 opt

oldchk：s0opt

输入文件：`DHR-s1opt.gjf`

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read  geom=check`

结果：normal termination
Excited State   1:      Singlet-A'     1.9981 eV  620.52 nm  f=0.2642 
      95 -> 98         0.10866
      97 -> 98         0.68913
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1151.01799955

## s1 td

oldchk：s1 opt

输入文件：`DHR-s1td.gjf`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read geom=check`

结果：normal termination


# s2

## s2 opt

oldchk：s0opt

输入文件：`DHR-s2opt.gjf`

关键词：`# opt freq td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read  geom=check`

结果：normal termination
Excited State   2:      Singlet-A'     2.2281 eV  556.46 nm  f=0.0279  
      97 -> 99         0.67660
      97 ->100         0.10554
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1151.00204809
## s2 td

oldchk：s2 opt

输入文件：`DHR-s2td.gjf`

关键词：`# td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read  geom=check`

结果：

# s9

## s9 opt

oldchk：s0opt

输入文件：`DHR-s2opt.gjf`

关键词：`# opt freq td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read  geom=check`

结果：normal termination
 Excited State   9:      Singlet-A'     4.1754 eV  296.94 nm  f=0.3611
      91 -> 98         0.15106
      94 ->100         0.13858
      95 -> 99        -0.57158
      96 ->100        -0.23151
      97 ->104        -0.10400
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1150.94058314

## s9 td

oldchk：s9 opt

输入文件：`DHR-s9td.gjf`

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) em=gd3bj guess=read  geom=check`

结果：