---
tags:
  - research
  - 后处理
  - 计算化学
  - Gaussian
Category:
  - 笔记
---
# s0

## s0 opt

输入文件：`DHR-s0opt.gjf`

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj`

结果：normal termination
SCF Done:  E(RCAM-B3LYP) =  -1151.10472780     A.U.
## s0 td

oldchk：

输入文件：`DHR-s0td.gjf`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj guess=read geom=check`

结果：normal termination

| state | Dip.S.  |
| ----- | ------- |
| 1     | 7.7614  |
| 2     | 0.3393  |
| 9     | 6.6166  |

# s1

## s1 opt

oldchk：s0 opt

输入文件：`DHR-s1opt.gjf`

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj guess=read geom=check`

结果：normal termination
Excited State   1:      Singlet-A'     1.8370 eV  674.92 nm  f=0.5730
      97 -> 98         0.69945
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1151.02971108

## s1 td

oldchk：s1 opt

输入文件：`DHR-s1td.gjf`

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj guess=read geom=check`

结果：normal termination
Dip.S.=8.4620

## evc-kr

evc.cart.dat：
Total reorganization energy      (cm-1):         1712.313150       1705.380094

evc.dint.dat：
Total reorganization energy      (cm-1):         1711.661481       1706.194780

## log

Ead=0.07501672 a.u.

EDMA=7.08 debye

EDME=7.39 debye

# s2

## s2 opt

oldchk：s0 opt

输入文件：`DHR-s2opt.gjf`

关键词：`# opt freq td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj guess=read geom=check`

结果：normal termination
Excited State   2:      Singlet-A'     2.1942 eV  565.06 nm  f=0.0542 
      97 -> 99         0.68344
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1151.00866790

## s2 td

oldchk：s2 opt

输入文件：`DHR-s2td.gjf`

关键词：`# td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj guess=read geom=check`

结果：normal termination
Dip.S.=0.6858

## evc-kr

evc.cart.dat：
Total reorganization energy      (cm-1):         3523.491414       3298.381604

evc.dint.dat：
Total reorganization energy      (cm-1):         3526.037622       3302.195939

## log

Ead=0.0960599 a.u.

EDMA=1.48 debye

EDME=2.10 debye

# s9

## s9 opt

oldchk：s0 opt

输入文件：`DHR-s9opt.gjf`

关键词：`# opt td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj guess=read geom=check`

结果：normal termination
Excited State   9:      Singlet-A'     4.0719 eV  304.49 nm  f=1.2330 
      94 ->100        -0.12964
      95 -> 99        -0.63549
      97 ->102         0.11804
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1150.95049944

## s9 td

oldchk：s2 opt

输入文件：`DHR-s9td.gjf`

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(solvent=THF) em=gd3bj guess=read geom=check`

结果：normal termination
Dip.S.=7.4264

## evc-kr

evc.cart.dat：
Total reorganization energy      (cm-1):         1020.497353       1007.798667

evc.dint.dat：
Total reorganization energy      (cm-1):         1021.508001       1006.977213

## log

Ead=0.15422836 a.u.

EDMA=6.54 debye

EDME=6.93 debye