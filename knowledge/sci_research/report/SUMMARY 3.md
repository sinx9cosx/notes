---
tags:
  - 计算化学
  - research
Category:
  - 笔记
---
# DHR

## Spectrum

DHR 分别计算了水相、气相和 THF 条件下的 S1/S2/S9 发射谱，三种条件下的结果都没有与文献 394 nm 的峰对应上，因此溶剂差异大概不是主要原因，可能还是计算方法的问题。

| DHR计算发射峰 | S1     | S2     | S9     |
| -------- | ------ | ------ | ------ |
| 水相       | 647 nm | 484 nm | 299 nm |
| 气相       | 591 nm | 477 nm | 292 nm |
| THF      | 634 nm | 483 nm | 287 nm |
| 文献计算值    | 658 nm | 394 nm | 394 nm |
<div style="page-break-after: always;"></div>
---

![[DHR-spec-s129-water.png]]

kr-s1=4.29854076E+07 /s
kic-s1=1.34470125E+10 /s

kr-s2=6.72519946E+06 /s

kr-s9=4.07746649E+08 /s

---

![[DHR-spec-s129-gas.png]]

kr-s1=3.89894052E+07 /s

kr-s2=5.73859741E+06 /s

kr-s9=2.58755190E+08 /s

---

![[DHR-spec-s129-THF.png]]

kr-s1=4.83472314E+07 /s

kr-s2=7.19431997E+06 /s

kr-s9=5.54629861E+08 /s

---

## NTO

> 本征值：0.98422

  <table><tr>
  <td align="center"><img src="s1-NTO-97.png" width="380"><br>S1-97空穴</td>
  <td align="center"><img src="s1-NTO-98.png" width="380"><br>S1-98电子</td>
  </tr></table>

---

> 本征值：0.99014
> 空穴与电子均离域分布在整个分子骨架，覆盖五元环与七元环的区域。电子往左边的七元环转移更多。

  <table><tr>
  <td align="center"><img src="s2-NTO-97.png" width="380"><br>S2-97空穴</td>
  <td align="center"><img src="s2-NTO-98.png" width="380"><br>S2-98电子</td>
  </tr></table>

---

> 本征值：0.73127
> 主导轨道（97-98）能看出电子向七元环转移，空穴主要分布在五元环附近，电子轨道覆盖大部分分子骨架（包括五元环和七元环区域）。

  <table><tr>
  <td align="center"><img src="s9-NTO-97.png" width="380"><br>S9-97空穴</td>
  <td align="center"><img src="s9-NTO-98.png" width="380"><br>S9-98电子</td>
  </tr></table>

> 本征值：0.14587

  <table><tr>
  <td align="center"><img src="s9-NTO-96.png" width="380"><br>S9-96空穴</td>
  <td align="center"><img src="s9-NTO-99.png" width="380"><br>S2-99电子</td>
  </tr></table>


---

# TBR

## Spectrum

计算光谱
![[TBR-spec-s129.png]]

实验光谱
![[experiment.png]]

---

TBR 根据S0 td的计算结果，选择了振子强度较大的S2和S9进行高激发态计算。目前完成 S1/S2/S9 的发射谱计算，S1 发射峰约 622 nm，与实验的长波主发射区域比较接近；S2 和 S9 分别约为 320 nm 和 443 nm，目前与实验约 380 nm 的高能发射峰不能直接对应。


计算得到的辐射速率：
kr-s1=3.07717900E+07 /s
kic-s1=kic=4.47073007E+09 /s

kr-s2=1.26280895E+08 /s

kr-s9=3.86206659E+08 /s

---

## NTO

> 本征值：0.97683
> 空穴局域在五元环区域，电子往七元环上转移。

  <table><tr>
  <td align="center"><img src="s1-NTO-135.png" width="380"><br>S1-135空穴</td>
  <td align="center"><img src="s1-NTO-136.png" width="380"><br>S1-136电子</td>
  </tr></table>

---

> 本征值：0.95147
> 空穴主要分布在分子的五元环中心，电子主要分布在七元环及其周围，五元环也有。空穴/电子分离不明显。

  <table><tr>
  <td align="center"><img src="s2-NTO-135.png" width="380"><br>S2-135空穴</td>
  <td align="center"><img src="s2-NTO-136.png" width="380"><br>S2-136电子</td>
  </tr></table>

---

> 本征值：0.60264
> 主导轨道（135-136）的空穴主要在五元环区域，电子分布在七元环周围。两端贡献较小。次级轨道（134-137）类似。

  <table><tr>
  <td align="center"><img src="s9-NTO-135.png" width="380"><br>S9-135空穴</td>
  <td align="center"><img src="s9-NTO-136.png" width="380"><br>S9-136电子</td>
  </tr></table>

> 本征值：0.24583

  <table><tr>
  <td align="center"><img src="s9-NTO-134.png" width="380"><br>S9-134空穴</td>
  <td align="center"><img src="s9-NTO-137.png" width="380"><br>S9-137电子</td>
  </tr></table>
