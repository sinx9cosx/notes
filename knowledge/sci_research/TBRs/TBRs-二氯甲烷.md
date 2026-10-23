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

结果：


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


evc.dint.dat:


**kr：**
evc.cart.dat:


evc.dint.dat:


## 速率

kic=

kr=

# s10

## s10 opt

oldchk：TBRs-s0opt.chk

输入文件：TBRs-s10opt.gjf

关键词：`# opt td(nstate=20,root=10) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：

## s10 freq

oldchk:TBR-s9opt.chk

输入文件：TBR-s9freq.gjf

关键词：`# freq td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：无虚频
Excited State   9: 

Dip.S.=

## s10 td

oldchk:TBR-s9freq.chk

输入文件：TBR-s9td.gjf

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：
Excited State   9

## s10 NTO 

oldchk:TBR-s9td.chk

输入文件：TBR-s9-NTO.gjf

关键词：`# cam-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=9) pop=(minimal,nto,savento) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：
135-136


## s10 nacme

oldchk:TBR-s9opt.chk

输入文件：TBR-s9nacme.gjf

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=9, 6/30=0, 6/17=2)`

结果：

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