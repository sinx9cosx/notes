---
tags:
  - 计算化学
  - research
Category:
  - 笔记
---
# s1

## 吸收发射

S0->S1吸收：2.6307 eV 471.29 nm f=0.2021

S1->S0发射：2.0554 eV  603.22 nm  f=0.2105
     135 ->136 （HOMO->LUMO）        0.68425
 Total Energy, E(TD-HF/TD-DFT) =  -1610.54373777

## 几何结构

几何结构上，五元环键长变得更均匀，七元环无显著变化，二面角变化不大

## s1-nacme

s1-nacme：`# td(nstate=20) cam-B3LYP/6-31g(d,p) scrf em=gd3bj guess=read  geom=check prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2)`
这个文件我不太清楚该怎么分析：

HOMO-LUMO能隙：= 0.15196 Ha ≈ 4.135 eV

跃迁偶极矩：在平面内
Ground to excited state transition electric dipole moments (Au):
       state          X           Y           Z        Dip. S.      Osc.
         1         1.2787     -1.5955      0.0000      4.1807      0.2105


ESP电荷（S0→S1 电子转移）：
19  C   -0.309325
22  C    0.307953
25  C   -0.216200
电子转移集中在五元环

## s1-NTO

关键词：`# CAM-B3LYP/6-31g(d,p) geom=allcheck guess=(read,only) density=(check,transition=1) pop=(minimal,nto,savento) scrf em=gd3bj`

不知道为什么看不到NTO轨道，所以看了分子轨道

结果：Alpha virt. eigenvalues --    0.97683 
由唯一一对空穴-电子主导的激发。
  <table><tr>
  <td align="center"><img src="TBR-S1-NTO135.png" width="380"><br>HOMO</td>
  <td align="center"><img src="TBR-S1-NTO136.png" width="380"><br>LUMO</td>
  </tr></table>

HOMO和LUMO都主要分布在 π 共轭骨架，二者具有较明显空间重叠。

# s2 s3

s0几何上：
Excited State   2:      Singlet-A      3.2093 eV  386.32 nm  f=0.4636 
     131 ->136        -0.18233
     **134 ->136         0.62527**
     134 ->137        -0.15311
     135 ->136         0.14334
 
 Excited State   3:      Singlet-A      3.2156 eV  385.58 nm  f=0.0000 
     132 ->136        -0.15731
     **133 ->136         0.64135**
     135 ->138         0.17948

> s2和s3能级间隙很小，且s3是暗态。


s3进行了两次结构优化，第一次有-733的虚频，正负移动0.3之后第二次最后都落在同一个结构上，但是有-224的虚频。

第一次的几何上（最终）：
 Excited State   2:      Singlet-A      2.8187 eV  439.86 nm  f=1.0248
     131 ->136        -0.10784
     **134 ->136        -0.67254**
     135 ->136         0.11032
 
 Excited State   3:      Singlet-A      2.7236 eV  455.22 nm  f=0.0000
     132 ->136        -0.12473
     **133 ->136         0.66324**
     135 ->138        -0.14460

> 但是优化过程中出现了交叉。

优化过程的能量变化：

| s2         | s3         |
| ---------- | ---------- |
| 3.1087     | 3.1974     |
| 2.9078     | 2.8518     |
| 2.8240     | 2.7304     |
| **2.7994** | **2.6982** |
| **2.8160** | **2.7210** |
| 2.8185     | 2.7236     |
| 2.8187     | 2.7236     |
| 2.8187     | 2.7236     |

第二次的几何上：
 Excited State   2:      Singlet-A      2.8624 eV  433.15 nm  f=0.2169
     133 ->137         0.10237
     134 ->137         0.11108
     135 ->136        -0.10935
     **135 ->137         0.65150**
 
 Excited State   3:      Singlet-A      2.9611 eV  418.72 nm  f=0.5413 
     131 ->136         0.12758
     **134 ->136         0.64743**
     134 ->137         0.13174

> s3变成了亮态，主要跃迁成分也发生变化。可能是和s2交叉了，这一次优化的几何不是s3态的。