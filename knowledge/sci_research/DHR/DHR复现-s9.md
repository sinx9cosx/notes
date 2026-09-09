---
tags:
  - Gaussian
  - research
Category:
  - 笔记
---
## s9 opt（2）

输入文件：`DHR-s9opt2.gjf`

关键词：`# opt td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：收敛成功
SCF Done: -1151.10219537 a.u.
<mark style="background: #ABF7F7A6;">3.9952 eV  310.34 nm  f=0.1547</mark>
94 -> 98         0.52870
95 -> 99         0.15959
## s9 freq

输入文件：`DHR-s9freq.gjf`

关键词：`# freq td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：无虚频
Total Energy, E(TD-HF/TD-DFT) =  -1150.95108647
<mark style="background: #FFB8EBA6;">4.1119 eV  301.53 nm  f=1.1829 95 -> 99         0.54087</mark>
## s9 td

oldchk：s9opt2

输入文件：`DHR-s9td.gjf`

关键词：`# td(nstate=20,root=9) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check`

结果：normal termination
Dip.S.：5.9939
<mark style="background: #ADCCFFA6;">4.2129 eV  294.30 nm  f=0.6186 95 -> 99         0.52369</mark>
## s9 nacme

oldchk：s9opt2

输入文件：`DHR-s9-nacme.gjf`

关键词：`#p td(nstate=20,root=9) scrf em=gd3bj cam-b3lyp/6-31g(d,p) guess=read geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`

结果：normal termination
<mark style="background: #FFB8EBA6;">4.2129 eV  294.30 nm  f=0.6186 95 -> 99         0.52369</mark>
————缺少关键词，重新计算————
关键词：`#p td(nstate=20,root=9) cam-b3lyp/6-31g(d,p) scrf em=gd3bj guess=read geom=check prop=(fitcharge,field) density=transition=9 iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`
## s9 NTO

oldchk：s9td

输入文件：`DHR-s9-NTO.gjf`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=9) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：normal termination

> [!note]
> opt2 优化跟踪的 root9 是 94→98 弱态（f≈0.15），freq/td/nacme 锚定的是 95→99 强态（f≈0.6–1.2），两者近简并、opt 期间态序抖动；发光 S9 判定为 95→99 型。

