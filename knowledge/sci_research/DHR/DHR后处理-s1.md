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

Ead（绝热激发能）=2.144 eV=0.078792a.u.（已弃用）
EDMA（吸收电子偶极矩）=6.92738 debye
EDME（发射电子偶极矩）=7.24786 debye

## evc-kr

目标：得到evc.cart.dat，用于后续荧光光谱和辐射速率计算
momap.inp填入log提取的数据

结果：evc.cart.dat与evc.dint.dat重组能相差很小。

## kr

1. 检查收敛spec.tvcf.ft.dat

2. spec.tvcf.log
	radiative rate:辐射速率：5.49796738E+07 s 辐射寿命:18.17 ns

3. 主峰在601？文献在658？


————用s1opt的数据计算Ead=0.0733699 au————

## kr



## kic
