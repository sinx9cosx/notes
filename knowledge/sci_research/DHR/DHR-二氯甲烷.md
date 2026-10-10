---
tags:
  - research
  - Gaussian
---
# s0
## s0 opt+freq

输入文件：DHR-s0opt.gjf

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：收敛成功，无虚频
SCF Done:  E(RCAM-B3LYP) =  -1151.10502586     A.U.

## s0 td

oldchk:DHR-s0opt.gjf

输入文件：DHR-s0td.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：

| 激发态 | 能量        | 波长        | 振子强度     | Dip.S. |
| --- | --------- | --------- | -------- | ------ |
| s1  | 2.3368 eV | 530.56 nm | f=0.4504 | 7.8665 |
| s9  | 4.3810 eV | 283.01 nm | f=0.7217 | 6.7245 |

# s1
## s1 opt+freq

oldchk:DHR-s0opt.gjf

输入文件：DHR-s1opt.gjf

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：收敛，无虚频

 Excited State   1:      Singlet-A'     1.8289 eV  677.93 nm  f=0.5886 
      97 -> 98         0.69974
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1151.03028453

## s1 td

oldchk:DHR-s1opt.chk

输入文件：DHR-s1td.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：
Excited State   1:      Singlet-A'     1.9254 eV  643.95 nm  f=0.4051 
      97 -> 98         0.69564
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1151.02673840


## s1 NTO

oldchk:DHR-s1td.chk

输入文件：DHR-s1-NTO.gjf

关键词：`# cam-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：

## s1 nacme

oldchk:DHR-s1opt.chk

输入文件：DHR-s1nacme.gjf

关键词：`#p td(nstate=20) cam-b3lyp/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

结果：normal termination

# s9
## s9 opt

oldchk:DHR-s0opt.gjf

输入文件：DHR-s9opt.gjf

关键词：`# opt td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：收敛

## s9 freq

oldchk:DHR-s9opt.chk

输入文件：DHR-s9freq.gjf

关键词：`# freq td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：无虚频

## s9 td

oldchk:DHR-s9freq.chk

输入文件：TBR-s9td.chk

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：

## s9 NTO 

## s9 nacme

oldchk:DHR-s9freq.chk

输入文件：DHR-s9nacme.gjf

关键词：

结果：