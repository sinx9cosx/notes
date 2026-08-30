---
tags:
  - 计算化学
  - research
  - 后处理
Category:
  - 讲义
---

# 生成evc文件

## 3.1 概述

MOMAP能够分析Duschinsky旋转和简正模式振动，这是基于evc_int和evc_cart子程序实现的。在本指南以下部分，这类计算将被称为evc计算。

evc计算可以使用其他QC程序的输出，如Gaussian、Q-Chem、TURBOMOLE、ChemShell、Dalton、MOLPRO、DFTB和MOPAC等。它也可以从输出文件中读取数据，包括振动频率和力常数矩阵，并在内坐标和笛卡尔坐标下计算初始和最终电子态之间的简正模式位移、Huang-Rhys因子、重组能和Duschinsky旋转矩阵。

## 3.2 开始计算

evc计算需要初始和最终电子态的基本信息。因此，要开始evc计算，您需要在MOMAP输入文件（即momap.inp）中指定相关文件名。

以下是最简单的evc输入文件示例。对于Gaussian输出文件，您还需要提供相应的`.fchk`文件。

以tests/azulene/evc为例，编辑momap.inp，并在文件中添加以下内容：

```bash
[evc]$ cat momap.inp
do_evc = 1 # 切换evc计算，1或0
&evc
ffreq(1) = "azulene-s0.log" # 基态（GS）的log文件
ffreq(2) = "azulene-s1.log" # 激发态（ES）的log文件
/
```

当evc输入文件准备好后，用户可以通过运行以下命令进行计算：

```bash
$ momap.py -i momap.inp -n 4
```

该示例还包含一个运行脚本文件，用户可以修改该文件，例如将np选项从4改为8，并通过运行脚本文件来执行计算：

```bash
$ ./run
```

除了ffreq(1)和ffreq(2)参数外，evc程序还允许用户将重组能投影到内坐标上、考虑同位素效应，以及配置许多其他高级设置等。更多参数设置请参考附录。

3.3 程序输出
该计算获得的主要结果是初始和最终电子态之间的性质——简正模式位移、Huang-Rhys因子、重组能和Duschinsky旋转矩阵。这些信息保存在evc.cart.dat和evc.dint.dat中。

1. **evc.cart.dat**
   使用笛卡尔坐标计算上述性质。

2. **evc.dint.dat**
   使用内坐标计算简正模式位移、Huang-Rhys因子和重组能，而Duschinsky旋转矩阵则使用笛卡尔坐标计算。

请检查evc.cart.dat和evc.dint.dat之间的重组能结果。如果能量差较小（< 1000 cm⁻¹），则使用evc.cart.dat中的结果进行后续计算；如果能量差较大，则使用evc.dint.dat进行后续计算。

