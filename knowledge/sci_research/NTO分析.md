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
