---
tags:
  - 计算化学
Category:
  - 笔记
---
# QC准备

1. 分子s0几何结构优化+频率计算，并生成`.fchk`文件。在`.log`文件最后找到`SCF done`以获取优化后s0几何结构下的单点能，如：
	```
	SCF Done: E(RB3LYP) = -849.172438992 A.U.
	```
2. 在优化的s0几何结构下使用TDDFT方法计算跃迁偶极矩（吸收）。在输出`.log`文件中找到`Excited State 1`的信息，以获取优化后s0几何结构下的垂直激发态能和跃迁偶极矩（吸收）。
	```
	Ground to excited state transition electric dipole moments (Au):
state X Y Z Dip. S. Osc.
1 -4.6693 -0.0118 0.0112 21.8029 1.7826
Excited State 1: Singlet-A 3.3372 eV 371.52 nm f=1.7826 <S**2>=0.000 75 -> 76 0.70728
This state for optimization and/or second-order correction.
Total Energy, E(TD-HF/TD-KS) = -848.655200149
	```
跃迁偶极矩（吸收可通过DIp.S获得）：
$$
21.8029 \times 2.54 Debye=11.86 Debye
$$
3. 优化s1几何结构和频率计算，使用TDDFT方法。获取优化后s1几何结构下的单点能。生成`fchk`文件。
	```
	SCF Done: E(RB3LYP) = -849.165742659 A.U.
	```

4. 在优化后的s1几何结构下计算跃迁偶极矩（发射）。在`.log`文件中找到`Excited State 1`的信息，，以获取优化后s1几何结构下的垂直激发态能和跃迁偶极矩（发射）。
5. s0和s1态之间的绝热能量差，可以用1和3的单点能结果计算，取绝对值。
6. 在优化后的s1几何结构下计算跃迁电场和NACME
	关键词：`#p td b3lyp/6-31g(d) prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`
# 生成evc文件

# 生成NACME文件

# 计算kr和荧光光谱

# 计算kic