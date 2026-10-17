---
tags:
  - 热力学
  - 物理化学
Category:
  - 笔记
---

# Gibbs-Duhem 方程

## 从加和公式推出约束

恒 $T$、$p$ 下的二组分系统，体积由加和公式给出：
$$
V=n_AV_A+n_BV_B
$$
两边微分。注意 $V_A$、$V_B$ 也随组成变，所以它们也要微分：
$$
\mathrm{d}V=n_A\mathrm{d}V_A+V_A\mathrm{d}n_A+n_B\mathrm{d}V_B+V_B\mathrm{d}n_B
$$
另一方面，体积是 $n_A$、$n_B$ 的函数，直接全微分并对两个偏导用偏摩尔体积的定义：
$$
\mathrm{d}V=\left(\frac{\partial V}{\partial n_A}\right)_{T,p,n_B}\mathrm{d}n_A+\left(\frac{\partial V}{\partial n_B}\right)_{T,p,n_A}\mathrm{d}n_B=V_A\mathrm{d}n_A+V_B\mathrm{d}n_B
$$
两式相减，含 $\mathrm{d}n_A$、$\mathrm{d}n_B$ 的项抵消，只剩
$$
n_A\mathrm{d}V_A+n_B\mathrm{d}V_B=0
$$
两边再除以总物质的量 $n_A+n_B$：
$$
x_A\mathrm{d}V_A+x_B\mathrm{d}V_B=0
$$

## 通则

把 $V$ 换成任意偏摩尔量、把组分数从二推广到多，恒 $T$、$p$ 下同样成立。

<mark style="background: #ADCCFFA6;">Gibbs-Duhem 方程</mark>
$$
\sum_B x_B\mathrm{d}X_B=0
$$
它也可以写成物质的量形式：
$$
\sum_B n_B\mathrm{d}X_B=0
$$
它是加和公式微分的结果，所以只要系统处在平衡态、$T$ 和 $p$ 恒定，就必须满足，与有几个组分、各组分含量多少无关。

## 二组分系统的形式

对二组分系统，把上式解出 $B$ 的微分：
$$
\mathrm{d}V_B=-\frac{x_A}{x_B}\mathrm{d}V_A
$$
这个式子能读出三件事。若 $\mathrm{d}V_A>0$，则 $\mathrm{d}V_B<0$：一个组分的偏摩尔量增加，另一个必然减少。变化的比例与两组分的摩尔分数成反比。两个偏摩尔量的变化不独立、互相制约，所以知道一个就能求另一个。

用途之一是由一个求另一个：测得 $V_A$ 随组成的变化后，用这个式子求出 $V_B$ 的变化，再配合加和公式定出 $V_B$ 的绝对值。另一个用途是检验数据：实验测得的偏摩尔量若明显不满足这个方程，说明数据或处理有问题，这就是热力学一致性检验。

## 化学势形式的 Gibbs-Duhem 方程（拓展）

取 $X=G$。把 $G=\sum_B n_B\mu_B$ 微分，再与 $\mathrm{d}G=-S\mathrm{d}T+V\mathrm{d}p+\sum_B\mu_B\mathrm{d}n_B$ 比较，两边相同的 $\sum_B\mu_B\mathrm{d}n_B$ 相消，得
$$
\sum_B n_B\mathrm{d}\mu_B=-S\mathrm{d}T+V\mathrm{d}p
$$
恒温恒压时右端为零，于是
$$
\sum_B n_B\mathrm{d}\mu_B=0,\qquad \sum_B x_B\mathrm{d}\mu_B=0
$$
这一形式在后续求活度、活度系数时要用，先在这里补出来：由蒸气压数据求出一个组分的化学势变化后，就是靠它推到另一个组分。推导时把它和[[热力学#化学势|化学势]]里的 $\mathrm{d}G$ 基本方程对照着看，条件才不容易弄错。

## 和前面笔记的联系

与[[热力学#Maxwell 关系式|Maxwell 关系式]]一样，Gibbs-Duhem 方程讲的也是热力学量之间不独立：Maxwell 关系式说二阶偏导可以交换次序，Gibbs-Duhem 方程说各组分偏摩尔量的变化必须互相补偿。

上一篇[[偏摩尔量]]的加和公式是代数关系，这一篇的方程是它的微分关系。两者合起来，才能由一个已知组分的偏摩尔量推出另一个未知组分。
