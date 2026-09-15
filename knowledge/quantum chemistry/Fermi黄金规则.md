---
tags:
  - 计算化学
Category:
  - 笔记
---
在[[含时微扰理论#代入方程求解|微扰]]$\hat{H'}(t)$作用下，t1时刻处于$\psi_{m}^0$的系数为
$$
\begin{aligned}
&c_{m}(t_{1})=\frac{1}{i\hbar}\int_{0}^{t_{1}} H'_{mn}e^{i\omega_{mn}t}dt\\ \\
&\omega_{mn}=\frac{E_{m}^0-E_{n}^0}{\hbar}\\ \\
&P_{nm}=|c_{m}(t_{1})|^2
\end{aligned}
$$

若微扰与时间无关：
$$
\begin{aligned}
c_{m}(t)&=\frac{1}{i\hbar}H'_{mn}\int_{0}^{t} e^{i\omega_{mn}t}dt\\ \\
&=\frac{H'_{mn}}{i\hbar}\cdot \frac{e^{i\omega_{mn}t}-1}{i\omega_{mn}}
\end{aligned}
$$

跃迁概率
$$
P_{nm}=\frac{|H'_{mn}|^2}{i\hbar}\cdot \frac{\sin^2(\omega_{mn}t/2)}{(\omega_{mn}/2)^2}
$$
当t足够大时，这个尖峰函数趋近$\delta$函数：
$$
\frac{\sin^2(\omega_{mn}t/2)}{(\omega_{mn}/2)^2} \rightarrow 2\pi t\delta(\omega_{mn})
$$

---

<mark style="background: #BBFABBA6;">简单的解释：</mark>

> [!note]- $\delta$函数的性质
> - 从负无穷到正无穷的积分面积为1
> - 在一点有值，其他地方为0


积分，令$x=\frac{\omega_{mn}t}{2}$：
$$
\int_{-\infty}^{+\infty}\frac{\sin^2(\omega_{mn}t/2)}{(\omega_{mn}/2)^2}dt=\int_{-\infty}^{+\infty} \frac{\sin^2x}{(x / t)^2} \frac{2}{t}dx
=2t\int_{{-\infty}}^{+\infty} \frac{\sin^2x}{x^2}dx=2\pi t
$$
则函数的积分面积为$2\pi t$

$\omega=0$时函数取极大值$t^2$，零点为$\pm 2\pi /t$，峰高~$t^2$，峰宽~$\frac{1}{t}$

---

跃迁概率
$$
P_{nm}=\frac{|H'_{mn}|^2}{\hbar^2}2\pi t\delta(\omega_{mn})
$$

跃迁速率
$$
\frac{P_{nm}}{t}=\frac{2\pi}{\hbar^2}|H'_{mn}|^2\delta(\omega_{mn})
$$

$$
\delta(\omega_{mn})=\delta\left( \frac{E_{m}^0-E_{n}^0}{\hbar} \right)=\hbar \delta(E_{m}^0-E_{n}^0)
$$

则跃迁速率为
$$
\frac{P_{nm}}{t}=\frac{2\pi}{\hbar}|H'_{mn}|^2\delta(E_{m}^0-E_{n}^0)
$$

只有当$E_{m}^0=E_{n}^0$（终态能量与始态相等）时，跃迁速率才不为0.
因此终态需要落在连续谱区间内才能跃迁。

引入态密度$\rho(E)$：单位能量间隔内的状态数

<mark style="background: #FFB86CA6;">Fermi黄金规则</mark>：

跃迁速率
$$
\begin{aligned}
\Gamma_{n\to f}&=\frac{2\pi}{\hbar}|H'_{fn}|^2\int\delta(E_{m}^0-E_{n}^0)\rho(E_{m}^0)dE_{m}^0\\ \\
&=\frac{2\pi}{\hbar}|H'_{fn}|\rho(E_{f})
\end{aligned}
$$

<mark style="background: #BBFABBA6;">说明：</mark>

-  t要足够长， $\sin^2$因子才能 $\delta$函数化（要求$t\gg \hbar / \Delta E$ ，$\Delta E$为终态能级间隔）；
- 但一级微扰近似要求跃迁概率远小于 1（弱微扰），即 $t\ll \hbar / |H'_{mn}|$。

两条同时成立，即微扰矩阵元远小于能级间隔、态密度足够大。如果微扰太强（矩阵元大）或终态太稀疏，黄金规则失效。