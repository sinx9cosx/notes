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

Ead（绝热激发能）=0.0733699 au
EDMA（吸收电子偶极矩）=6.92738 debye
EDME（发射电子偶极矩）=$\sqrt{ 15.2084 }\times 2.5417=9.91$debye

## evc-kr

目标：得到evc.cart.dat，用于后续荧光光谱和辐射速率计算
momap.inp填入log提取的数据

结果：evc.cart.dat与evc.dint.dat重组能相差很小。


## kr

1. 收敛检验 `spec.tvcf.ft.dat` 第 1 列（time）vs 第 4 列（emi_FC_Re）
	成功

2. log 末尾 `radiative rate` 行取 `/s` 与 `ns` 两个数:
	radiative rate     (0):     1.03976729E-09    4.29854076E+07 /s,      23.26 ns
3. 画光谱。 `spec.tvcf.spec.dat` x 取第 4 列波长（或第 3 列波数），y 取第 7 列 `FC_emi_intensity`。
（待s9计算好之后完成）


## kic

1. 收敛检验。`ic.tvcf.ft.dat`
	成功

2.  log 末尾 `Calculate absorption and emission spectra` 表只有一行（在 Ead 处），取 `6kic(s^{-1})` 列的值；同行的 time(ps) 即 1/kic。
