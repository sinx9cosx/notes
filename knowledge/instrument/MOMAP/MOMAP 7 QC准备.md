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

在优化的s0几何结构下使用TDDFT方法计算跃迁偶极矩（吸收）。在平衡结构的输出`.log`文件中找到`Excited State 1`的信息，以获取优化后s0几何结构下的垂直激发态能和跃迁偶极矩（吸收）。
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

`prop=(fitcharge, field)`：关键指令。让 Gaussian 在计算中输出**拟合静电势电荷**（FitCharge）和各原子核位置上的电势与电场矢量（Field）。

MOMAP 算内转换要用"跃迁电场"（transition electric field） (field那张表的 X/Y/Z 三列)。MOMAP 自己的 `evc.out` 里会把这张表原样打印成 `========= Transition Elecric Field (atomic unit) ======`，然后做变换（`.nac`  STEP 1 读入 → STEP 2 把核坐标 x 变换到简正坐标 Q），得到 `<\Psi_b|∂H/∂x_{iα}|\Psi_a>`，再除以两态能隙。

`iop(6/22=-4)`：selection of density（密度） matrix。

| 值         | 含义                              |
| --------- | ------------------------------- |
| -4        | iop(6/29)与iop(6/30)所指定两态之间的跃迁密度 |
| -5        | 所有可用的跃迁密度                       |
| -3        | iop(6/29)指定的激发态的密度              |
| -2        | 全部可用密度                          |
| -1        | 当前方法/HF密度                       |
| -1x/+1x   | 从.chk读密度矩阵                      |
| N$\geq$ 0 | 方法N的密度                          |

`iop(6/29=1)` 和 `iop(6/30=0)`：excited state to use if requested by iop(6/22) 

选取计算6/29与6/30之间的跃迁密度

`iop(6/17=2)`：是否计算核的贡献

| 值   | 含义      |
| --- | ------- |
| 0   | 全部贡献    |
| 1   | 只算核贡献   |
| 2   | 只算电子贡献  |
| -N  | 只算第N个壳层 |
