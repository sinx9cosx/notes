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


## NTO

  <table><tr>
  <td align="center"><img src="s1-NTO-97.png" width="380"><br>S1-97空穴</td>
  <td align="center"><img src="s1-NTO-98.png" width="380"><br>S1-98电子</td>
  </tr></table>


  <table><tr>
  <td align="center"><img src="s2-NTO-97.png" width="380"><br>S2-97空穴</td>
  <td align="center"><img src="s2-NTO-98.png" width="380"><br>S2-98电子</td>
  </tr></table>

  <table><tr>
  <td align="center"><img src="s9-NTO-97.png" width="380"><br>S9-97空穴</td>
  <td align="center"><img src="s9-NTO-98.png" width="380"><br>S9-98电子</td>
  </tr></table>

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

## NTO

  <table><tr>
  <td align="center"><img src="s1-NTO-135.png" width="380"><br>S1-135空穴</td>
  <td align="center"><img src="s1-NTO-136.png" width="380"><br>S1-136电子</td>
  </tr></table>


  <table><tr>
  <td align="center"><img src="s2-NTO-135.png" width="380"><br>S2-135空穴</td>
  <td align="center"><img src="s2-NTO-136.png" width="380"><br>S2-136电子</td>
  </tr></table>


  <table><tr>
  <td align="center"><img src="s9-NTO-135.png" width="380"><br>S9-135空穴</td>
  <td align="center"><img src="s9-NTO-136.png" width="380"><br>S9-136电子</td>
  </tr></table>


  <table><tr>
  <td align="center"><img src="s9-NTO-97.png" width="380"><br>S2-97空穴</td>
  <td align="center"><img src="s2-NTO-98.png" width="380"><br>S2-98电子</td>
  </tr></table>