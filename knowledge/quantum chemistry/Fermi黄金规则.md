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
\frac{\sin^2(\omega_{mn}t/2)}{(\omega_{mn}/2)^2}
$$