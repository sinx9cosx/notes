# DHA计算细节

## 芳香性

所有元素的基组：6-31G(d)3

各向同性化学屏蔽表面（？）-(ICSS)4，相关量程序：Multiwfn 3.7.

NICS（衡量芳香性、反芳香性）：B3LYP/def2svp

## 吸收、发射光谱

opt s0 s1 s2：CASSCF/6-31G\*/(12,12)

对称性：D2H

激发能和振子强度：CASPT2/6-31G\*/(12,12)

程序：MOLCAS7.0

freq s0 s1 s2：\omegaB97xd\6-311+g\*

程序：Gaussian 16

方法：DFT,TDDFT

振动吸收和发射光谱：MOMAP

> 文献的s1 s2是实验谱带编号。
