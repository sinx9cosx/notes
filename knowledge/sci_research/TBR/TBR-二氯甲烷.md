---
tags:
  - research
  - Gaussian
---
# s0
## s0 opt+freq

输入文件：TBR-s0opt.gjf

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：无虚频
SCF Done:  E(RCAM-B3LYP) =  -1610.62818550     A.U.

## s0 td

oldchk:TBR-s0opt.chk

输入文件：TBR-s0td.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：

| 激发态 | 能量        | 波长        | 振子强度     | Dip.S. |
| --- | --------- | --------- | -------- | ------ |
| s1  | 2.6253 eV | 472.26 nm | f=0.2155 | 3.3497 |
| s9  | 4.1361 eV | 4.1361 eV | f=0.7539 | 7.4396 |

# s1
## s1 opt+freq

oldchk：TBR-s0opt.chk

输入文件：TBR-s1opt.gjf

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：收敛，无虚频
 Excited State   1:      Singlet-A      2.0050 eV  618.37 nm  f=0.3254
     135 ->136         0.68620
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54371263
 
Dip.S.=6.6253

## s1 td

oldchk: TBR-s1opt.chk

输入文件：TBR-s1td.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：
Excited State   1:      Singlet-A      2.0491 eV  605.08 nm  f=0.2211
     135 ->136         0.68431
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54209412

## s1 NTO

oldchk:TBR-s1td.chk

输入文件：TBR-s1-NTO.gjf

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：

## s1 nacme

oldchk:TBR-s1opt.chk

输入文件：TBR-s1nacme.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

结果：normal termination

# s9
## s9 opt

oldchk:TBR-s0opt.chk

输入文件：TBR-s9opt.gjf

关键词：`# opt td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：收敛成功

## s9 freq

oldchk:TBR-s9opt.chk

输入文件：TBR-s9freq.gjf

关键词：`# freq td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：无虚频
Excited State   9:      Singlet-A      3.8979 eV  318.08 nm  f=1.0291 
     131 ->136        -0.30668
     133 ->139        -0.14480
     134 ->137         0.53143
     135 ->140         0.24953
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.48170429

Dip.S.=10.7764

## s9 td

oldchk:TBR-s9freq.chk

输入文件：TBR-s9td.gjf

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：
Excited State   9:      Singlet-A      3.9762 eV  311.81 nm  f=0.7205 
     131 ->136        -0.30992
     133 ->139        -0.12732
     134 ->137         0.53419
     135 ->140         0.23444
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1610.47882514

## s9 NTO 

oldchk:TBR-s9td.chk

输入文件：TBR-s9-NTO.gjf

关键词：`# cam-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=9) pop=(minimal,nto,savento) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：


## s9 nacme

oldchk:TBR-s9opt.chk

输入文件：TBR-s9nacme.gjf

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=9, 6/30=0, 6/17=2)`

结果：normal termination