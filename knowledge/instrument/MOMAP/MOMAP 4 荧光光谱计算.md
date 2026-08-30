---
tags:
  - 后处理
  - 计算化学
  - research
Category:
  - 讲义
---

# 4. 荧光光谱计算

## 4.1 概述

MOMAP能够基于TVCORF_SPEC和TVSPEC_SPEC子程序模拟荧光光谱并计算相应的辐射衰减速率常数。TVCORF_SPEC子程序用于计算热振动相关函数（TVCF），而TVSPEC_SPEC子程序用于模拟荧光光谱。

在本指南的以下部分，这类计算将被简称为rad_FL计算。

## 4.2 开始计算

要开始rad_FL计算，您需要一个`*.dat`文件、一个MOMAP控制文件，以及一个可选的并行控制文件。`*.dat`文件来自前面提到的evc计算。MOMAP控制文件用于控制TVCORF_SPEC和TVSPEC_SPEC子程序的行为。可选的并行控制文件用于控制将使用多少个计算进程。

使用azulene进行rad_FL计算的示例位于目录tests/azulene/kr中。该计算所需的文件如下：

（1）evc.cart.dat
evc计算结果文件。

（2）momap.inp
MOMAP控制文件。

（3）nodefile（可选，可通过运行选项 –n # 自动生成）
并行机器文件，用于控制将使用多少个计算进程。

## 4.3 修改控制文件

以下是一个rad_FL计算的MOMAP控制文件示例，它显示了各参数及其含义。用户在进行rad_FL计算前可能需要相应修改这些参数。

```bash
[kr]$ cat momap.inp
do_spec_tvcf_ft = 1 # 切换相关函数计算，1或0
do_spec_tvcf_spec = 1 # 切换荧光光谱计算，1或0
&spec_tvcf
DUSHIN = .t. # 切换Duschinsky旋转效应，.t.或.f.
Temp = 300 K # 温度
tmax = 5000 fs # 积分时间，至少5000 fs
dt = 0.001 fs # 积分步长，最大不超过0.001 fs
Ead = 0.075092 au # 绝热激发能
EDMA = 0.92694 debye # 吸收（基态）电子偶极矩
EDME = 0.64751 debye # 发射（激发态）电子偶极矩
FreqScale = 1.0 # 频率缩放因子
DSFile = "evc.cart.dat" # 输入dushin文件
Emax = 0.3 au # 谱频率上限
dE = 0.00001 au # 输出能量间隔
logFile = "spec.tvcf.log" # 日志输出文件
FtFile = "spec.tvcf.ft.dat" # 相关函数信息输出文件
FoFile = "spec.tvcf.fo.dat" # 谱函数信息输出文件
FoSFile = "spec.tvcf.spec.dat" # 谱信息输出文件
/
```

如果用户希望使用求和法（sum-over-states）在绝对零度（0 K）下计算光谱，请参阅目录examples/azulene/sumstat了解更多详情。

## 4.4 验证相关函数收敛并获取结果

在获得任何计算结果之前，相关函数必须收敛。为验证收敛，使用spec.tvcf.ft.dat中的前两列绘制图形，这两列分别是时间和相关函数的实部（TVCF_RE）。TVCF_RE应在到达积分时间限制之前非常接近于零并停止振荡。图3展示了一个收敛的相关函数图。

辐射衰减速率常数可在spec.tvcf.log文件末尾找到，而荧光光谱信息可从spec.tvcf.spec.dat文件中获取。

图3 时间与收敛相关函数实部的分布
![[fig-3.jpg]]
