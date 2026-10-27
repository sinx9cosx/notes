---
tags:
  - research
  - Gaussian
---
# s0
## s0 opt+freq

输入文件：TBRs-s0opt.gjf

关键词：`# opt freq CAM-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：normal termination
SCF Done:  E(RCAM-B3LYP) =  -1611.82271929

## s0 td

oldchk:TBRs-s0opt.chk

输入文件：TBRs-s0td.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：normal termination

| 激发态 | 能量        | 波长        | 振子强度     | Dip.S. |
| --- | --------- | --------- | -------- | ------ |
| s1  | 2.7784 eV | 446.25 nm | f=0.3231 | 3.3497 |
| s9  | 4.1361 eV | 4.1361 eV | f=0.7539 | 7.4396 |

S1-Dip.S.=4.7465

# s1
## s1 opt+freq

oldchk：TBRs-s0opt.chk

输入文件：TBRs-s1opt.gjf

关键词：`# opt freq td(nstate=20) cam-B3LYP/6-31g(d,p) scrf# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：normal termination

Excited State   1:      Singlet-A      2.1061 eV  588.69 nm  f=0.3857
     136 ->137        -0.68842
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1611.73360097
 
Dip.S.=7.4754

## s1 td

oldchk: TBRs-s1opt.chk

输入文件：TBRs-s1td.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：normal termination
Excited State   1:      Singlet-A      2.1511 eV  576.37 nm  f=0.2706 
     136 ->137         0.68505
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1611.73194666

## s1 NTO

oldchk:TBRs-s1td.chk

输入文件：TBRs-s1-NTO.gjf

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：normal termination
0.98739

## s1 nacme

oldchk:TBRs-s1opt.chk

输入文件：TBR-s1nacme.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

结果：normal termination

## evc数据

Ead= -1611.73360097 -(-1611.82271929)=0.08911832 au

EDMA=$\sqrt{4.7465}\times 2.5417=5.54$ debye

EDME=$\sqrt{ 7.4754}\times 2.5417=$ 6.95debye

## evc

**kic：**
evc.cart.dat:
Total reorganization energy      (cm-1):         2626.961112       2546.877394

evc.dint.dat:
Total reorganization energy      (cm-1):         2622.274554       2555.670285

**kr：**
evc.cart.dat:
Total reorganization energy      (cm-1):         2626.961112       2546.877394

evc.dint.dat:
Total reorganization energy      (cm-1):         2622.274554       2555.670285

## 速率

kic=3.64427732E+09 /s

kr=6.59924393E+07 /s

# s9

## s10 opt

oldchk：TBRs-s0opt.chk

输入文件：TBRs-s10opt.gjf

关键词：`# opt td(nstate=20,root=10) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：normal termination 收敛到S9
 Excited State  10:      Singlet-A      4.0067 eV  309.44 nm  f=0.3337
     130 ->137        -0.11128
     131 ->137         0.15497
     132 ->137        -0.14411
     132 ->139         0.10617
     133 ->140         0.10171
     135 ->138         0.32043
     135 ->139         0.10312
     135 ->140        -0.15305
     136 ->139         0.24888
     136 ->140         0.32593
     136 ->142         0.14455
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1611.67229675

## s9 freq

oldchk:TBRs-s10opt.chk

输入文件：TBR-s9freq.gjf

关键词：`# freq td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：无虚频
 Excited State   9:      Singlet-A      4.0067 eV  309.44 nm  f=0.3337  
     130 ->137        -0.11128
     131 ->137         0.15497
     132 ->137        -0.14411
     132 ->139         0.10617
     133 ->140         0.10171
     135 ->138         0.32043
     135 ->139         0.10312
     135 ->140        -0.15305
     136 ->139         0.24888
     136 ->140         0.32593
     136 ->142         0.14455
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1611.67229671


## s9 td

oldchk:TBRs-s9freq.chk

输入文件：TBRs-s9td.gjf

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：normal termination
 Excited State   9:      Singlet-A      4.0313 eV  307.56 nm  f=0.2452
     130 ->137        -0.14012
     131 ->137         0.16195
     132 ->139         0.11409
     135 ->138         0.32537
     135 ->140        -0.16489
     136 ->139         0.19454
     136 ->140         0.34184
     136 ->141        -0.11632
     136 ->142         0.14296
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1611.67139505

## s9 NTO 

oldchk:TBR-s9td.chk

输入文件：TBR-s9-NTO.gjf

关键词：`# cam-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=9) pop=(minimal,nto,savento) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：
135-136


## s9 nacme

oldchk:TBRs-s9freq.chk

输入文件：TBRs-s9nacme.gjf

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=9, 6/30=0, 6/17=2)`

结果：normal termination

## evc数据

Ead= 

EDMA=$\sqrt{ }\times 2.5417=$ debye

EDME=$\sqrt{  }\times 2.5417=$ debye

## evc

**kic:**
evc.cart.dat:


evc.dint.dat:


**kr:**
evc.cart.dat:


evc.dint.dat:


## 速率

kic=

kr=