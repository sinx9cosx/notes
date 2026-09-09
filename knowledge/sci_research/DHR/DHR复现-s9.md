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
Electrostatic Properties Using The Transition Density Between Ground State And State  1
<mark style="background: #ABF7F7A6;">（怎么解决？）</mark>

oldchk:s9-td

关键词：`#p cam-b3lyp/6-31g(d,p) scrf em=gd3bj guess=(read,only) geom=allcheck density=(check,transition=9) prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`
————报错————修改————

## s9 NTO

oldchk：s9td

输入文件：`DHR-s9-NTO.gjf`

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=9) pop=(minimal,nto,savento) scrf em=gd3bj`

结果：normal termination

> [!note]
> opt2 优化跟踪的 root9 是 94→98 弱态（f≈0.15），freq/td/nacme（？） 锚定的是 95→99 强态（f≈0.6–1.2），两者近简并、opt 期间态序抖动；发光 S9 判定为 95→99 型。


97->98(0.73127)

  <table><tr>
  <td align="center"><img src="DHR-s9-97.jpg" width="380"><br>97空穴</td>
  <td align="center"><img src="DHR-s9-98.jpg" width="380"><br>98电子</td>
  </tr></table>

96->99(0.14587)

  <table><tr>
  <td align="center"><img src="DHR-s9-96.jpg" width="380"><br>96空穴</td>
  <td align="center"><img src="DHR-s9-99.jpg" width="380"><br>99电子</td>
  </tr></table>

95->100(0.08428)

  <table><tr>
  <td align="center"><img src="DHR-s9-95.jpg" width="380"><br>95空穴</td>
  <td align="center"><img src="DHR-s9-100.jpg" width="380"><br>100电子</td>
  </tr></table>

### NTO 判读（2026-09-09）

前三对本征值 0.73127 + 0.14587 + 0.08428 累计 96.1%，需看三对。

| NTO 对 | 空穴 | 电子 | 空间分布判读 |
| --- | --- | --- | --- |
| 第 1 对（73.1%） | 97 | 98 | 全分子离域，左右镜像对称 |
| 第 2 对（14.6%） | 96 | 99 | 全分子离域，中央桥瓣最大 |
| 第 3 对（8.4%） | 95 | 100 | 全分子离域，左右大体对称 |

**结论：S9 是分子内高度离域的 ππ* 激发（LE 型），不是薁单元间 CT。** 理由：

1. 三对 NTO 的空穴与电子都遍布左右薁 + 中央桥，没有一对是"空穴在左薁、电子在右薁"；空穴-电子空间高度重叠 → 跃迁偶极矩大，与 f=0.62~1.18 强发射自洽（纯 CT 态通常 f<0.1）。
2. 与文献设计思想呼应：双薁 J-耦合的高激发态是两单元跃迁偶极的集体组合态，离域全分子是预期图像。
3. 组态混合散（7 个组态、主组态 95→99 系数²仅 27%）正是离域型高激发态的特征，NTO 压缩后仍需三对覆盖 96%。

> [!note]
> 判读基于轨道图视觉分析 + f 数值 + 组态特征三方互证；定量验证可用 Multiwfn 空穴-电子分析（Sr/D 指数）。

