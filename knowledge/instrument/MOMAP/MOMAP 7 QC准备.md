---
tags:
  - 计算化学
  - research
  - 后处理
Category:
  - 讲义
---
# QC准备

## 7.1 s0 opt freq

分子s0几何结构优化+频率计算，并生成`.fchk`文件。在`.log`文件最后找到`SCF done`以获取优化后s0几何结构下的单点能，如：
```
SCF Done: E(RB3LYP) = -849.172438992 A.U.
```

## 7.2 s0 td

在优化的s0几何结构下使用TDDFT方法计算跃迁偶极矩（吸收）。在输出`.log`文件中找到`Excited State 1`的信息，以获取优化后s0几何结构下的垂直激发态能和跃迁偶极矩（吸收）。
```
	Ground to excited state transition electric dipole moments (Au):
state X Y Z Dip. S. Osc.
1 -4.6693 -0.0118 0.0112 21.8029 1.7826
Excited State 1: Singlet-A 3.3372 eV 371.52 nm f=1.7826 <S**2>=0.000 75 -> 76 0.70728
This state for optimization and/or second-order correction.
Total Energy, E(TD-HF/TD-KS) = -848.655200149
```
跃迁偶极矩（吸收可通过Dip.S获得）：
$$
21.8029 \times 2.54 Debye=11.86 Debye
$$

## 7.3 s1 opt freq

优化s1几何结构和频率计算，使用TDDFT方法。获取优化后s1几何结构下的单点能。生成`fchk`文件。
```
	SCF Done: E(RB3LYP) = -849.165742659 A.U.
```


## 7.4 s1 td

在优化后的s1几何结构下计算跃迁偶极矩（发射）。在`.log`文件中找到`Excited State 1`的信息，，以获取优化后s1几何结构下的垂直激发态能和跃迁偶极矩（发射）。

## 7.5 绝热能量差

s0和s1态之间的绝热能量差，可以用1和3的单点能结果计算，取绝对值。
Ead=E(S1@S1平衡几何-S0@S0平衡几何)，即两个势能面极小点之间的能量差
## 7.6 s1 nacme

在优化后的s1几何结构下计算NACME：

关键词：`#p td b3lyp/6-31g(d) prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

计算完成后将这里获得的跃迁电场`.log`和s0优化结构频率计算的`.log`文件复制到一个新的目录中。

然后使用`get-nacme`开始计算NACME。MOMAP 会读取这两个 .log 文件，将电子结构信息与振动模式信息结合，进行Duschinsky振动分析，最终输出一个 **`evc.cart.nac`** 文件。

<mark style="background: #ABF7F7A6;">关键词解释：</mark>

`prop=(fitcharge, field)`：关键指令。让 Gaussian 在计算中输出拟合静电势电荷（FitCharge）和电场（Field）相关的积分，这里的“电场”本质上就是指跃迁偶极矩（Transition Dipole Moment）及其对坐标的导数信息。

`iop(6/22=-4)`：将导数积分（包括跃迁偶极矩导数）写入 checkpoint 文件并以文本形式输出到 .log 中，方便 MOMAP 读取。

`iop(6/29=1)` 和 `iop(6/30=0)`：专门用于激活非绝热耦合（NAC）矩阵元所需积分的输出。

`iop(6/17=2)`：指示 Gaussian 计算激发态的解析导数，以得到跃迁偶极矩对原子位移的偏导数值。

