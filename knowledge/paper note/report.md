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

# 四、计算结果

## 4.1 基态优化结构（苯&萘）

**优化是否成功**

 > 苯：Normal termination of Gaussian 16 at Sat Jul 18 17:08:21 2026.
 > 萘： Normal termination of Gaussian 16 at Sat Jul 18 19:04:03 2026.

**虚频检查**

| molecule    | imaginary frequency |
| ----------- | ------------------- |
| benzene     | none                |
| naphthalene | none                |

**基态能量**

