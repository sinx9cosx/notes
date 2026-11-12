---
tags:
  - research
  - 后处理
Category:
  - 笔记
---
# 操作步骤

## multiwfn

用s0td上计算出来的TBR-s9和TBRs做初步筛选

1. 把 `TBRs-s0td-full.fchk` 和 `TBRs-s0td-full.log` 放在同一个文件夹里。
2. 启动 Multiwfn，点击主菜单 `18 Electron excitation analysis`。
3. 在子菜单中选 `1`，然后输入 log 文件的路径。
4. 在输入“Perform the analysis for which excited state”时，输入 `4`。
5. 先检查屏幕上显示的两行：`Sum of square of excitation coefficients` 应约为 0.5，`Deviation` 应小于 0.001；如果该值大于 0.05，说明 log 的组态系数被截断，不要继续使用。
6. 在接下来的菜单中选 `3`，再选 `1`（Mulliken）。
7. 屏幕会列出每个非氢原子的 Hole/Electron 百分比；选 `2`，把数据导出成当前文件夹的 `he_atm.txt`。
8. 逐层选 `0` 返回，最后输入 `q` 退出。

## excel

然后用 Excel 把对应环上的原子加总：

- 完整薁的五元环：`6,10,13,28,37`
- 同一个薁的七元环：`3,6,7,10,20,22,26`
- 另一个五元环：`9,19,21,27,44`

把 Hole 列和 Electron 列分别加总即可喵。

![[dark-state.png]]

 Excited State   4:      Singlet-A      3.5944 eV  344.94 nm  f=0.0073 
    <mark style="background: #FFB8EBA6;"> 133 ->137</mark>        -0.32958
     134 ->137         0.19952
     135 ->138         0.20189
     135 ->139        -0.20209
     <mark style="background: #FFB8EBA6;">136 ->138 </mark>        0.45398
     136 ->139        -0.12687


# TBRs-S2

## s4 opt

oldchk：TBRs-s0opt.chk

输入文件：TBRs-s4opt1.gjf

关键词：`# opt td(nstate=20,root=4) cam-B3LYP/6-31g(d,p) scrf# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：normal termination

Excited State   1:      Singlet-A      2.1061 eV  588.69 nm  f=0.3857
     136 ->137        -0.68842
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1611.73360097
 
Dip.S.=7.4754

## s2 freq

oldchk:TBRs-s4opt1.chk

输入文件：TBR-s2freq.gjf

关键词：`# freq td(nstate=20,root=2) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

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
Dip.S.=3.3997

## s4 td

oldchk: TBRs-s1opt.chk

输入文件：TBRs-s1td.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check`

结果：normal termination
Excited State   1:      Singlet-A      2.1511 eV  576.37 nm  f=0.2706 
     136 ->137         0.68505
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -1611.73194666

## s4 NTO

oldchk:TBRs-s1td.chk

输入文件：TBRs-s1-NTO.gjf

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj`

结果：normal termination
0.98739

## s4 nacme

oldchk:TBRs-s1opt.chk

输入文件：TBR-s1nacme.gjf

关键词：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf=(IEFPCM,Solvent=Dichloromethane) em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

结果：

## evc数据

Ead=

EDMA=$\sqrt{4.7465}\times 2.5417=$ debye

EDME=$\sqrt{ 7.4754}\times 2.5417=$  debye

## evc

**kic：**
evc.cart.dat:

evc.dint.dat:


**kr：**
evc.cart.dat:


evc.dint.dat:


## 速率

