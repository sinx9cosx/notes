---
tags:
  - 计算化学
  - research
Category:
  - 笔记
---
# s1

## 吸收发射

S0->S1吸收：2.6307 eV 471.29 nm f=0.2021

S1->S0发射：2.0554 eV  603.22 nm  f=0.2105
     135 ->136 （HOMO->LUMO）        0.68425
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54373777

## 几何结构

几何结构上，五元环键长变得更均匀，七元环无显著变化，二面角变化不大

## s1-nacme

s1-nacme：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`
这个文件我太清楚该怎么分析：

HOMO-LUMO能隙：= 0.15196 Ha ≈ 4.135 eV

跃迁偶极矩：在平面内
Ground to excited state transition electric dipole moments (Au):
       state          X           Y           Z        Dip. S.      Osc.
         1         1.2787     -1.5955      0.0000      4.1807      0.2105


ESP电荷（S0→S1 电子转移）：
19  C   -0.309325
22  C    0.307953
25  C   -0.216200
电子转移集中在五元环

## s1-NTO

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf em=gd3bj`

不知道为什么没有读到NTO，所以看了分子轨道

结果：