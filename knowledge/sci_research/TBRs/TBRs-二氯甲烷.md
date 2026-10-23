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

Ead=

EDMA=$\sqrt{}\times 2.5417=$ debye

EDME=$\sqrt{ }\times 2.5417=$ debye

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

## s10 opt+freq

oldchk：TBRs-s0opt.chk

输入文件：TBRs-s10opt.gjf

关键词：`# opt freq td(nstate=20,root=10) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：