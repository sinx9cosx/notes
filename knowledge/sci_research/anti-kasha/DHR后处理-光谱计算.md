---
tags:
  - 后处理
  - 计算化学
  - research
Category:
  - 笔记
---
使用[[MOMAP后处理荧光光谱+速率]]

# s1

## log文件提取数据

Ead（绝热激发能）=2.144 eV=0.078792a.u.
EDMA（吸收电子偶极矩）=6.92738 debye
EDME（发射电子偶极矩）=7.24786 debye

## evc-kr

目标：得到evc.cart.dat，用于后续荧光光谱和辐射速率计算

结果：evc.cart.dat与evc.dint.dat重组能相差很小。

## evc-kir

目标：得到evc.cart.nac用于后续非辐射速率计算

结果：

## kr

目标：获得荧光光谱信息

1. 验证相关函数收敛：使用spec.tvcf.ft.dat中的前两列绘制图形
2. 获取结果：辐射衰减速率常数可在spec.tvcf.log文件末尾找到，而荧光光谱信息可从spec.tvcf.spec.dat文件中获取

# s9

## evc-kr

目标：得到evc.cart.dat，用于后续荧光光谱和辐射速率计算
momap.inp填入log提取的数据

结果：

## evc-kir

目标：得到evc.cart.nac用于后续非辐射速率计算

结果：
