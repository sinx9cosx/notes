---
tags:
  - 计算化学
  - research
Category:
  - 草稿
---
# 空穴-电子图
  
  <table><tr>
  <td align="center"><img src="97.png" width="380"><br>DHR-S9-97空穴</td>
  <td align="center"><img src="98.png" width="380"><br>DHR-S9-98电子</td>
  </tr></table>


  <table><tr>
  <td align="center"><img src="135-0.png" width="380"><br>TBR-S9-135空穴</td>
  <td align="center"><img src="136-0.png" width="380"><br>TBR-S9-136电子</td>
  </tr></table>
  
---

# 机理解释

<mark style="background: #FFB86CA6;">机理解释：</mark>

DHR 和 TBR 的高激发态 NTO 存在相似性  
↓  
两者的跃迁都涉及五元环/七元环相关的 π 共轭体系  
↓  
说明 TBR 中这种环状共轭结构可以形成与 DHR 类似的高激发态电子结构  
↓  
为 TBR 的高激发态发光行为提供电子结构上的解释

The natural transition orbital (NTO) analysis reveals similar excited state electronic structures for DHR and TBR. They are highly connected with the conjugated system, which includes a pentagon and a heptagon. Just like DHR, the hole of TBR S9 is distributed near the pentagon, while the electron orbital is distributed near the heptagon. The correspondence between the NTO patterns of TBR and DHR suggests that this specific structure provides a similar high energy excited state luminescence mechanism.

The natural transition orbital (NTO) analysis reveals similar electronic structures for the highly excited states of DHR and TBR. In both molecules, the relevant electronic transitions are associated with the conjugated framework involving the five-membered and seven-membered rings. Similar to DHR, the hole NTO in TBR-S9 shows relatively little contribution from the seven-membered-ring region, whereas the electron NTO extends further toward the seven-membered ring. The similarity between the NTO distributions of DHR and TBR suggests that their cyclic conjugated frameworks can support similar highly excited-state electronic structures, providing an electronic-structure basis for understanding the highly excited-state luminescence behavior of TBR.

---

# 方法描述

<mark style="background: #FFB86CA6;">（参考）DHR的文章-计算方法描述</mark>

2.2 Computational details for the absorption and emission spectra simulations  

All the molecular geometry structures in the S0, S1 and S2 states were optimized at CASSCF/`631G*`/(12,12) level with symmetry contained as D2H group point. The excitation energies and oscillator strengths were calculated at CASPT2/`6-31G*`/(12,12) level based on CASSCF orbitals. S4  The above calculations were performed by using MOLCAS 7.0 program7. Because CASSCF method cannot deal with the frequency calculation owing to expensive computational cost, DFT and TDDFT were used to calculate the frequencies and analyze the normal modes of DHR in the S0, S1 and S2 states, respectively, at $\omega$B97xd/6-311+g* level with Gaussian 16 program8. Further the vibrational absorption and emission spectra of isolated DHR were simulated by using the thermal vibration correlation function method in MOMAP program9, for which the fine structures of the spectra were assigned in detail.

S9 opt+freq -> S9 td -> S9 NTO

The S9 states of DHR and TBR were optimized at the CAM-B3LYP/6-31G(d,p) level with Gaussian 16. TDDFT was used to calculate excitation energies of S9 and prepare for the NTO calculation. NTOs were analyzed at the same level of theory.


The ground-state geometries of DHR and TBR were optimized using density functional theory (DFT) at the CAM-B3LYP/6-31G(d,p) level with Gaussian 16. Solvent effects were considered using the polarizable continuum model (PCM) with water as the solvent, and empirical dispersion corrections were included using the D3(BJ) scheme. The S9 excited-state geometries were subsequently optimized using time-dependent density functional theory (TD-DFT) at this level of theory. Frequency calculations were performed to confirm the nature of the optimized excited-state structures. The excitation energies and oscillator strengths of the S9 states were calculated using TD-DFT, and natural transition orbitals (NTOs) were generated and analyzed at this level of theory.

---

# 光谱

![[TBR-s19-water.png]]

kr-s1=5.62414777E+07 /s 
kic-s1=kic=4.47073007E+09 /s

kr-s9=6.73725189E+08 /s
kic-s9=1.01347331E+09 /s


![[DHR-s19-water.png]]

kr-s1=4.29854076E+07 /s
kic-s1=1.34470125E+10 /s

kr-s9=4.07746649E+08 /s
kic-s9=