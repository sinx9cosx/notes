---
tags:
  - Gaussian
  - research
Category:
  - 课内/作业
---
# 一、计算目标

通过TD-DFT研究苯和萘的电子激发性质，计算其基态结构、激发态结构以及第一激发态到基态（$S_{1}\to S_{0}$）的跃迁性质。

# 二、计算步骤

1. 对分子基态的几何构型进行优化
2. 对分子激发态的几何构型进行优化
3. 在S1结构上计算发射能量

# 三、计算设置（苯&萘）

- 基态几何构型优化：

`# opt freq b3lyp/6-31g(d) geom=connectivity`

- 激发态几何构型优化：

`# opt freq td=(nstates=10,root=1) b3lyp/6-31g(d) geom=connectivity`

- 计算S1发射能量：

`# td=(nstates=10,root=1) b3lyp/6-31g(d) geom=connectivity`

# 四、计算结果（苯&萘）

## 4.1 基态优化结构

**4.1.1 优化是否成功**

 > 苯：Normal termination of Gaussian 16 at Sat Jul 18 17:08:21 2026.
 > 萘： Normal termination of Gaussian 16 at Sat Jul 18 19:04:03 2026.

**4.1.2 虚频检查**

| molecule    | imaginary frequency |
| ----------- | ------------------- |
| benzene     | none                |
| naphthalene | none                |

**4.1.3 基态能量**

苯： SCF Done:  E(RB3LYP) =  -232.248650991     A.U. after    1 cycles
萘： SCF Done:  E(RB3LYP) =  -385.892706628     A.U. after    1 cycles

## 4.2 激发态优化结构

**4.2.1 优化是否收敛**

>  Optimization completed.
    -- Stationary point found.

**4.2.2 S1能量**

苯：

``` text
 Excited State   1:      Singlet-A      5.2715 eV  235.20 nm  f=0.0000  <S**2> =0.000
      20 -> 22        -0.47803
      20 -> 23         0.14601
      21 -> 22         0.14601
      21 -> 23         0.47803
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -232.049919231    
 Copying the excited state density for this state as the 1-particle RhoCI density.
```

萘：

``` text
Excited State   1:      Singlet-A      4.4604 eV  277.97 nm  f=0.0600  <S**2> =0.000
      33 -> 36         0.15732
      34 -> 35         0.68510
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -385.728790123    
 Copying the excited state density for this state as the 1-particle RhoCI density.

```

| molecule    | state | energy    | $\lambda$ | f      |
| ----------- | ----- | --------- | --------- | ------ |
| benzene     | S1    | 5.2715 eV | 235.20 nm | 0.0000 |
| naphthalene | S1    | 4.4604 eV | 277.97 nm | 0.0600 |

## 4.3 S1优化后重新计算

**4.3.1 emission calculation**

苯：

``` text
Excited State   1:      Singlet-A      5.5446 eV  223.61 nm  f=0.0000  <S**2> =0.000
      20 -> 22         0.49411
      21 -> 23        -0.49407
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -232.044892243    
 Copying the excited state density for this state as the 1-particle RhoCI density.

```

萘：

``` text
Excited State   1:      Singlet-A      4.4604 eV  277.97 nm  f=0.0600  <S**2> =0.000
      33 -> 36         0.15732
      34 -> 35         0.68510
 This state for optimization and/or second-order correction.
 Total Energy, E(TD-HF/TD-DFT) =  -385.728790114    
 Copying the excited state density for this state as the 1-particle RhoCI density.
```

| molecule    | vertical emission energy | $\lambda$ | f      |
| ----------- | ------------------------ | --------- | ------ |
| benzene     | 5.5446 eV                | 223.61 nm | 0.0000 |
| naphthalene | 4.4604 eV                | 277.97 nm | 0.0600 |