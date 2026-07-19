---
tags:
  - Gaussian
  - research
Category:
  - 课内/作业
---
# 计算目标

获得苯和萘的第一激发态跃迁回基态（$S_{1}\to S_{0}$）的荧光光谱数据

# 计算步骤

1. 对分子基态的几何构型进行优化
2. 对分子激发态的几何构型进行优化
3. 在S1结构上计算发射能量

# 计算设置

- 基态几何构型优化：

> # opt freq b3lyp/6-31g(d) geom=connectivity

- 激发态几何构型优化：

> # opt freq td=(nstates=10,root=1) b3lyp/6-31g(d) geom=connectivity


# 计算结果