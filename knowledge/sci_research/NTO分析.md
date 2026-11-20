---
tags:
  - 计算化学
  - research
  - 后处理
Category:
  - 笔记
---
# 空穴-电子分析

## multiwfn步骤

空穴-电子分析：片段对空穴-电子密度的贡献

18 Electron excitation analysis->
1 Analyze and visualize hole&electron distribution, transition density, and transition electric/magnetic dipole moment density->
拖入`Sx-td.log`
输入待计算的激发态
3 Show atom or fragment contribution to hole and electron and plot the contributions as heat map->
精度：2
-1 Load fragment definition
定义片段
2 Export the data as he_atm.txt in current folder


## TBR-S9

五元环：23,22,25,1,17
七元环：25,22,21,16,9,30,26
重叠贡献：
$$
Overlap=\sqrt{Hole×Electron  }​
$$
如果一个片段对空穴和电子的贡献都很大，那么它们的重叠值会很高，说明该片段内发生的激发具有很强的**局域特征（LE）**。
反之，如果空穴和电子分布在不同片段，那么每个片段自身的重叠值会很低，这是**电荷转移（CT）**的典型信号。

|     | 空穴密度   | 电子密度   | 重叠贡献   |
| --- | ------ | ------ | ------ |
| 五元环 | 12.539 | 15.474 | 13.929 |
| 七元环 | 17.007 | 20.825 | 18.820 |

## TBRs-S9

五元环：13,28,10,6,37
七元环：10,6,3,26,22,7,20

|     | 空穴密度   | 电子密度   | 重叠贡献   |
| --- | ------ | ------ | ------ |
| 五元环 | 20.175 | 6.796  | 11.709 |
| 七元环 | 24.870 | 11.395 | 16.835 |

## TBRs-S2

|     | 空穴密度   | 电子密度   | 重叠贡献   |
| --- | ------ | ------ | ------ |
| 五元环 | 24.983 | 18.205 | 21.327 |
| 七元环 | 34.002 | 15.105 | 22.663 |

这么看起来TBRs-S2的态性质和TBR-S9其实不像，可能是因为按照TBR-S9最大的NTO筛选的。但是TBR-S9是多组态混合的，TBRs-S2只有那一对轨道。

## NTO轨道组成分析

8 Orbital composition analysis
8 Calculate atom and fragment contributions by Hirshfeld method
 1 Use build-in sphericalized atomic densities in free-states (recommended)
 

## TBR-S9

135-136 0.58923

五元环
 Orb#    Type       Ene(a.u.)     Occ    Composition    Population
  135 Alpha&Beta       0.5892    2.000     18.034 %       0.360679
  136 Alpha&Beta       0.5892    0.000      7.908 %       0.000000
 Population of this fragment in these orbitals:    0.360679

七元环
 Orb#    Type       Ene(a.u.)     Occ    Composition    Population
  135 Alpha&Beta       0.5892    2.000     15.541 %       0.310816
  136 Alpha&Beta       0.5892    0.000     24.183 %       0.000000
 Population of this fragment in these orbitals:    0.310816

| TBR-S9 | 五元环      | 七元环      |
| ------ | -------- | -------- |
| 空穴轨道   | 18.034 % | 15.541 % |
| 电子轨道   | 7.908 %  | 24.183 % |

## TBRs-S2

136-137 0.97381

五元环
 Orb#    Type       Ene(a.u.)     Occ    Composition    Population
  136 Alpha&Beta       0.9738    2.000     24.983 %       0.499654
  137 Alpha&Beta       0.9738    0.000      8.662 %       0.000000
 Population of this fragment in these orbitals:    0.499654

七元环
 Orb#    Type       Ene(a.u.)     Occ    Composition    Population
  136 Alpha&Beta       0.9738    2.000     34.001 %       0.680015
  137 Alpha&Beta       0.9738    0.000     37.006 %       0.000000
 Population of this fragment in these orbitals:    0.680015

| TBRs-S2 | 五元环      | 七元环      |
| ------- | -------- | -------- |
| 空穴轨道    | 24.983 % | 34.001 % |
| 电子轨道    | 8.662 %  | 37.006 % |

## TBRs-S9

136-137 0.47269
135-138 0.34663

五元环
 Orb#    Type       Ene(a.u.)     Occ    Composition    Population
  135 Alpha&Beta       0.3466    2.000     15.096 %       0.301930
  136 Alpha&Beta       0.4727    2.000     31.697 %       0.633940
  137 Alpha&Beta       0.4727    0.000     10.084 %       0.000000
  138 Alpha&Beta       0.3466    0.000     14.557 %       0.000000
 Population of this fragment in these orbitals:    0.935870

七元环
 Orb#    Type       Ene(a.u.)     Occ    Composition    Population
  135 Alpha&Beta       0.3466    2.000     15.194 %       0.303879
  136 Alpha&Beta       0.4727    2.000     28.719 %       0.574374
  137 Alpha&Beta       0.4727    0.000     19.956 %       0.000000
  138 Alpha&Beta       0.3466    0.000     22.766 %       0.000000
 Population of this fragment in these orbitals:    0.878254

| TBRs-S2 | 五元环      | 七元环      |
| ------- | -------- | -------- |
| 空穴轨道136 | 31.697 % | 28.719 % |
| 电子轨道137 | 10.084 % | 19.956 % |
| 空穴轨道135 | 15.096 % | 15.194 % |
| 电子轨道138 | 14.557 % | 22.766 % |