---
tags:
  - 热力学
  - 物理化学
Category:
  - 笔记
---
# Gibbs-Duhem 方程

## 推导

恒 $T$、$p$ 下的二组分系统，体积由[[偏摩尔量#加和公式|加和公式]]给出：
$$
V=n_AV_A+n_BV_B
$$
两边微分：
$$
\mathrm{d}V=n_A\mathrm{d}V_A+V_A\mathrm{d}n_A+n_B\mathrm{d}V_B+V_B\mathrm{d}n_B
$$

另一方面，体积是 $n_A$、$n_B$ 的函数，直接全微分并对两个偏导用偏摩尔体积的定义：
$$
\mathrm{d}V=\left(\frac{\partial V}{\partial n_A}\right)_{T,p,n_B}\mathrm{d}n_A+\left(\frac{\partial V}{\partial n_B}\right)_{T,p,n_A}\mathrm{d}n_B=V_A\mathrm{d}n_A+V_B\mathrm{d}n_B
$$
两式相减
$$
n_A\mathrm{d}V_A+n_B\mathrm{d}V_B=0
$$
两边再除以总物质的量 $n_A+n_B$：
$$
x_A\mathrm{d}V_A+x_B\mathrm{d}V_B=0
$$

<mark style="background: #FFB86CA6;">推广：</mark>
把 $V$ 换成任意偏摩尔量、把组分数从二推广到多，恒 $T$、$p$ 下同样成立。

<mark style="background: #ADCCFFA6;">Gibbs-Duhem 方程</mark>
$$
\sum_B x_B\mathrm{d}X_B=0
$$
它也可以写成物质的量形式：
$$
\sum_B n_B\mathrm{d}X_B=0
$$

## 二组分系统的形式

对二组分系统，把上式解出 $B$ 的微分：
$$
\mathrm{d}V_B=-\frac{x_A}{x_B}\mathrm{d}V_A
$$
这个式子能读出三件事。若 $\mathrm{d}V_A>0$，则 $\mathrm{d}V_B<0$：一个组分的偏摩尔量增加，另一个必然减少。变化的比例与两组分的摩尔分数成反比。两个偏摩尔量的变化不独立、互相制约，所以知道一个就能求另一个。

用途之一是由一个求另一个：测得 $V_A$ 随组成的变化后，用这个式子求出 $V_B$ 的变化，再配合加和公式定出 $V_B$ 的绝对值。另一个用途是检验数据：实验测得的偏摩尔量若明显不满足这个方程，说明数据或处理有问题，这就是热力学一致性检验。

## 化学势形式的 Gibbs-Duhem 方程

取 $X=G$。把 $G=\sum_B n_B\mu_B$ 微分，再与 $\mathrm{d}G=-S\mathrm{d}T+V\mathrm{d}p+\sum_B\mu_B\mathrm{d}n_B$ 比较，两边相同的 $\sum_B\mu_B\mathrm{d}n_B$ 相消，得
$$
\sum_B n_B\mathrm{d}\mu_B=-S\mathrm{d}T+V\mathrm{d}p
$$
恒温恒压时右端为零，于是
$$
\sum_B n_B\mathrm{d}\mu_B=0,\qquad \sum_B x_B\mathrm{d}\mu_B=0
$$
这一形式在后续求活度、活度系数时要用，先在这里补出来：由蒸气压数据求出一个组分的化学势变化后，就是靠它推到另一个组分。
