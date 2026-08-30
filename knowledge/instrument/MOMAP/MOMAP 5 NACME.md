---
tags:
  - 后处理
  - 计算化学
  - research
Category:
  - 讲义
---
# 5. 内转换（IC）速率常数

## 5.1 概述

MOMAP还能够基于TVCORF_IC和TVSPEC_IC子程序计算内转换（IC）速率常数。TVCORF_IC子程序用于计算热振动相关函数（TVCF），而TVSPEC_IC子程序用于确定IC速率常数与能隙之间的关系。

在本指南的以下部分，这类计算将被简称为非辐射计算。

## 5.2 计算非绝热耦合矩阵元（NACME）

与辐射荧光计算不同，在进行非辐射计算之前，必须先获得NACME。

在MOMAP中，get-nacme函数用于从Gaussian输出中读取跃迁电场和振动信息，并计算电子耦合项。该过程集成在evc_int和evc_cart子程序中。用户需要提供Gaussian电场计算结果，并在MOMAP控制文件momap.inp中启用NACME计算。其余步骤与常规evc计算相同。计算完成后，将生成一个*.nac文件，用于非辐射计算。

5.3 开始计算
要开始非辐射计算，您需要一个*.dat文件、一个*.nac文件、一个MOMAP控制文件，以及一个可选的并行控制文件。*.dat文件是evc结果文件。*.nac是NACME计算结果文件。与所有MOMAP计算一样，TVCORF_IC和TVSPEC_IC子程序需要一个MOMAP控制文件。并行控制文件用于控制将使用多少个计算进程。

使用azulene进行非辐射计算的示例位于目录tests/azulene/kic/kic中。该示例所需的文件如下：

（1）evc.cart.dat
evc计算结果文件。

（2）evc.cart.nac
NACME结果文件。

（3）momap.inp
MOMAP控制文件。

（4）nodefile（可选，可通过运行选项 –n # 自动生成）
并行机器文件，用于控制将使用多少个计算进程。

5.4 修改控制文件
以下是一个非辐射计算的MOMAP控制文件示例，它显示了各参数及其含义。用户在进行非辐射计算前可能需要相应修改这些参数。

```bash
[kic/kic]$ cat momap.inp
do_ic_tvcf_ft = 1 # 切换内转换相关函数计算，1或0
do_ic_tvcf_spec = 1 # 切换内转换谱计算，1或0
&ic_tvcf
DUSHIN = .t. # 切换Duschinsky旋转效应，.t.或.f.
Temp = 300 K # 温度
tmax = 5000 fs # 相关函数的积分区间，至少5000 fs
dt = 0.001 fs # 相关函数的积分步长，不超过0.001 fs
Ead = 0.075092 au # 两个态之间的绝热激发能差
DSFile = "evc.cart.dat" # 输入dushin文件
CoulFile = "evc.cart.nac" # 输入nacme信息文件
Emax = 0.3 au # 谱频率上限
logFile = "ic.tvcf.log" # 日志输出文件
FtFile = "ic.tvcf.ft.dat" # 相关函数信息输出文件
FoFile = "ic.tvcf.fo.dat" # 谱函数信息输出文件
/
```

5.5 验证相关函数收敛并获取结果
确保相关函数已收敛，这一点非常重要。验证过程可参见本指南第4.4节。

内转换（IC）速率常数可在ic.tvcf.log文件末尾找到。IC速率常数与能隙之间的关系也可从ic.tvcf.log文件中获取。

---

³ TVCORF_IC_para子程序可用于并行计算。