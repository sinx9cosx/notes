# Thermochemistry in *Gaussian*

<div align="center">

**Joseph W. Ochterski, Ph.D.**  
`help@gaussian.com`  
©2000, Gaussian, Inc.

June 2, 2000

</div>

<div align="center">

## Abstract

The purpose of this paper is to explain how various thermochemical values are computed in *Gaussian*. The paper documents what equations are used to calculate the quantities, but doesn't explain them in great detail, so a basic understanding of statistical mechanics concepts, such as partition functions, is assumed. *Gaussian* thermochemistry output is explained, and a couple of examples, including calculating the enthalpy and Gibbs free energy for a reaction, the heat of formation of a molecule and absolute rates of reaction are worked out.

</div>

---

## Contents

1. Introduction .................................................................................... 2
2. Sources of components for thermodynamic quantities .................. 2
   2.1 Contributions from translation .............................................. 3
   2.2 Contributions from electronic motion .................................... 4
   2.3 Contributions from rotational motion .................................... 4
   2.4 Contributions from vibrational motion .................................. 6
3. Thermochemistry output from *Gaussian* ...................................... 8
   3.1 Output from a frequency calculation ...................................... 8
   3.2 Output from compound model chemistries ............................ 11
4. Worked-out Examples ................................................................... 11
   4.1 Enthalpies and Free Energies of Reaction ............................. 12
   4.2 Rates of Reaction .................................................................. 12
   4.3 Enthalpies and Free Energies of Formation ........................... 14
5. Summary ...................................................................................... 17

---

## 1 Introduction

The equations used for computing thermochemical data in *Gaussian* are equivalent to those given in standard texts on thermodynamics. Much of what is discussed below is covered in detail in "Molecular Thermodynamics" by McQuarrie and Simon (1999). I've cross-referenced several of the equations in this paper with the same equations in the book, to make it easier to determine what assumptions were made in deriving each equation. These cross-references have the form [McQuarrie, §7-6, Eq. 7.27] which refers to equation 7.27 in section 7-6.

One of the most important approximations to be aware of throughout this analysis is that all the equations assume non-interacting particles and therefore apply *only* to an ideal gas. This limitation will introduce some error, depending on the extent that any system being studied is non-ideal. Further, for the electronic contributions, it is assumed that the first and higher excited states are entirely inaccessible. This approximation is generally not troublesome, but can introduce some error for systems with low lying electronic excited states.

The examples in this paper are typically carried out at the HF/STO-3G level of theory. The intent is to provide illustrative examples, rather than research grade results.

The first section of the paper is this introduction. The next section of the paper, I give the equations used to calculate the contributions from translational motion, electronic motion, rotational motion and vibrational motion. Then I describe a sample output in the third section, to show how each section relates to the equations. The fourth section consists of several worked out examples, where I calculate the heat of reaction and Gibbs free energy of reaction for a simple bimolecular reaction, and absolute reaction rates for another. Finally, an appendix gives a list of the all symbols used, their meanings and values for constants I've used.

---

## 2 Sources of components for thermodynamic quantities

In each of the next four subsections of this paper, I will give the equations used to calculate the contributions to entropy, energy, and heat capacity resulting from translational, electronic, rotational and vibrational motion. The starting point in each case is the partition function $q(V,T)$ for the corresponding component of the total partition function. In this section, I'll give an overview of how entropy, energy, and heat capacity are calculated from the partition function.

The partition function from any component can be used to determine the entropy contribution $S$ from that component, using the relation [McQuarrie, §7-6, Eq. 7.27]:

$$S = Nk_B + Nk_B \ln\left(\frac{q(V,T)}{N}\right) + Nk_BT\left(\frac{\partial \ln q}{\partial T}\right)_V$$

The form used in *Gaussian* is a special case. First, molar values are given, so we can divide by $n = N/N_A$, and substitute $N_Ak_B = R$. We can also move the first term into the logarithm (as $e$), which leaves (with $N=1$):

$$
\begin{aligned}
S &= R + R\ln\left(q(V,T)\right) + RT\left(\frac{\partial \ln q}{\partial T}\right)_V \\
  &= R\ln\left(q(V,T)e\right) + RT\left(\frac{\partial \ln q}{\partial T}\right)_V \\
  &= R\left(\ln(q_t q_e q_r q_v e) + T\left(\frac{\partial \ln q}{\partial T}\right)_V\right)
\end{aligned}
\tag{1}
$$

The internal thermal energy $E$ can also be obtained from the partition function [McQuarrie, §3-8, Eq. 3.41]:

$$E = Nk_BT^2\left(\frac{\partial \ln q}{\partial T}\right)_V, \tag{2}$$

and ultimately, the energy can be used to obtain the heat capacity [McQuarrie, §3.4, Eq. 3.25]:

$$C_V = \left(\frac{\partial E}{\partial T}\right)_{N,V} \tag{3}$$

These three equations will be used to derive the final expressions used to calculate the different components of the thermodynamic quantities printed out by *Gaussian*.

---

### 2.1 Contributions from translation

The equation given in McQuarrie and other texts for the translational partition function is [McQuarrie, §4-1, Eq. 4.6]:

$$q_t = \left(\frac{2\pi mk_BT}{h^2}\right)^{3/2}V.$$

The partial derivative of $q_t$ with respect to $T$ is:

$$\left(\frac{\partial \ln q_t}{\partial T}\right)_V = \frac{3}{2T}$$

which will be used to calculate both the internal energy $E_t$ and the third term in Equation 1.

The second term in Equation 1 is a little trickier, since we don't know $V$. However, for an ideal gas, $PV = NRT = \left(\frac{n}{N_A}\right)N_Ak_BT$, and $V = \frac{k_BT}{P}$. Therefore,

$$q_t = \left(\frac{2\pi mk_BT}{h^2}\right)^{3/2}\frac{k_BT}{P}.$$

which is what is used to calculate $q_t$ in *Gaussian*. Note that we didn't have to make this substitution to derive the third term, since the partial derivative has $V$ held constant.

The translational partition function is used to calculate the translational entropy (which includes the factor of $e$ which comes from Stirling's approximation):

$$
\begin{aligned}
S_t &= R\left(\ln(q_t e) + T\left(\frac{3}{2T}\right)\right) \\
    &= R(\ln q_t + 1 + 3/2).
\end{aligned}
$$

---

### 2.2 Contributions from electronic motion

The electronic partition function is:

$$q_e = g_e e^{-\epsilon_e/k_BT}$$

where $g_e$ is the degeneracy of the electronic state (almost always 2 for a radical, 1 for a closed shell). The derivative with respect to $T$ is:

$$\left(\frac{\partial \ln q_e}{\partial T}\right)_V = \frac{\epsilon_e}{k_BT^2}$$

The contribution to the entropy is:

$$S_e = R\left(\ln q_e + T\left(\frac{\epsilon_e}{k_BT^2}\right)\right) = R(\ln q_e + \epsilon_e/k_BT)$$

and the contribution to the internal thermal energy is:

$$E_e = RT^2\left(\frac{\epsilon_e}{k_BT^2}\right) = \frac{\epsilon_e}{k_B}R = N_A\epsilon_e$$

so the contribution to the heat capacity is zero:

$$C_e = 0$$

For a singlet molecule, $g_e = 1$ and the energy is typically taken as zero, so $q_e = 1$ and $S_e = E_e = C_e = 0$.

---

### 2.3 Contributions from rotational motion

For a linear molecule, the rotational partition function is [McQuarrie, §4-6, Eq. 4.38]:

$$q_r = \frac{1}{\sigma_r}\left(\frac{T}{\Theta_r}\right)$$

where $\Theta_r = h^2/8\pi^2Ik_B$. $I$ is the moment of inertia. The rotational contribution to the entropy is

$$
\begin{aligned}
S_r &= R\left(\ln q_r + T\left(\frac{\partial \ln q_r}{\partial T}\right)_V\right) \\
    &= R(\ln q_r + 1).
\end{aligned}
$$

The contribution of rotation to the internal thermal energy is

$$
\begin{aligned}
E_r &= RT^2\left(\frac{\partial \ln q_r}{\partial T}\right)_V \\
    &= RT^2\left(\frac{1}{T}\right) \\
    &= RT
\end{aligned}
$$

and the contribution to the heat capacity is

$$
\begin{aligned}
C_r &= \left(\frac{\partial E_r}{\partial T}\right)_V \\
    &= R.
\end{aligned}
$$

For the general case for a nonlinear polyatomic molecule, the rotational partition function is [McQuarrie, §4-8, Eq. 4.56]:

$$q_r = \frac{\pi^{1/2}}{\sigma_r}\left(\frac{T^{3/2}}{(\Theta_{r,x}\Theta_{r,y}\Theta_{r,z})^{1/2}}\right)$$

Now we have $\left(\frac{\partial \ln q}{\partial T}\right)_V = \frac{3}{2T}$, so the entropy for this partition function is

$$
\begin{aligned}
S_r &= R\left(\ln q_r + T\left(\frac{\partial \ln q_r}{\partial T}\right)_V\right) \\
    &= R(\ln q_r + \frac{3}{2}).
\end{aligned}
$$

Finally, the contribution to the internal thermal energy is

$$
\begin{aligned}
E_r &= RT^2\left(\frac{\partial \ln q_r}{\partial T}\right)_V \\
    &= RT^2\left(\frac{3}{2T}\right) \\
    &= \frac{3}{2}RT
\end{aligned}
$$

and the contribution to the heat capacity is

$$
\begin{aligned}
C_r &= \left(\frac{\partial E_r}{\partial T}\right)_V \\
    &= \frac{3}{2}R.
\end{aligned}
$$

The average contribution to the internal thermal energy from each rotational degree of freedom is $RT/2$, while it's contribution to $C_r$ is $R/2$.

---

### 2.4 Contributions from vibrational motion

The contributions to the partition function, entropy, internal energy and constant volume heat capacity from vibrational motions are composed of a sum (or product) of the contributions from each vibrational mode, $K$. Only the real modes are considered; modes with imaginary frequencies (i.e. those flagged with a minus sign in the output) are ignored. Each of the $3n_{\text{atoms}}-6$ (or $3n_{\text{atoms}}-5$ for linear molecules) modes has a characteristic vibrational temperature, $\Theta_{v,K} = h\nu_K/k_B$.

There are two ways to calculate the partition function, depending on where you choose the zero of energy to be: either the bottom of the internuclear potential energy well, or the first vibrational level. Which you choose depends on whether or not the contributions arising from zero-point energy will be coputed separately or not. If they are computed separately, then you should use the bottom of the well as your reference point, otherwise the first vibrational energy level is the appropriate choice.

If you choose the zero reference point to be the bottom of the well (`BOT`), then the contribution to the partition function from a given vibrational mode is [McQuarrie, §4-4, Eq. 4.24]:

$$q_{v,K} = \frac{e^{-\Theta_{v,K}/2T}}{1-e^{-\Theta_{v,K}/T}}$$

and the overall vibrational partition function is[McQuarrie, §4-7, Eq. 4.46]:

$$q_v = \prod_K \frac{e^{-\Theta_{v,K}/2T}}{1-e^{-\Theta_{v,K}/T}}$$

On the other hand, if you choose the first vibrational energy level to be the zero of energy (`V=0`), then the partition function for each vibrational level is

$$q_{v,K} = \frac{1}{1-e^{-\Theta_{v,K}/T}}$$

and the overall vibrational partition function is:

$$q_v = \prod_K \frac{1}{1-e^{-\Theta_{v,K}/T}}$$

*Gaussian* uses the bottom of the well as the zero of energy (`BOT`) to determine the other thermodynamic quantities, but also prints out the `V=0` partition function. Ultimately, the only difference between the two references is the additional factor of $\Theta_{v,K}/2$, (which is the zero point vibrational energy) in the equation for the internal energy $E_v$. In the expressions for heat capacity and entropy, this factor disappears since you differentiate with respect to temperature ($T$).

The total entropy contribution from the vibrational partition function is:

$$
\begin{aligned}
S_v &= R\left(\ln(q_v) + T\left(\frac{\partial \ln q}{\partial T}\right)_V\right) \\
    &= R\left(\ln(q_v) + T\left(\sum_K \frac{\Theta_{v,K}}{2T^2} + \sum_K \frac{(\Theta_{v,K}/T^2)e^{-\Theta_{v,K}/T}}{1-e^{-\Theta_{v,K}/T}}\right)\right) \\
    &= R\left(\sum_K\left(\frac{\Theta_{v,K}}{2T} + \ln(1-e^{-\Theta_{v,K}/T})\right) + T\left(\sum_K \frac{\Theta_{v,K}}{2T^2} + \sum_K \frac{(\Theta_{v,K}/T^2)e^{-\Theta_{v,K}/T}}{1-e^{-\Theta_{v,K}/T}}\right)\right) \\
    &= R\left(\sum_K \ln(1-e^{-\Theta_{v,K}/T}) + \left(\sum_K \frac{(\Theta_{v,K}/T)e^{-\Theta_{v,K}/T}}{1-e^{-\Theta_{v,K}/T}}\right)\right) \\
    &= R\sum_K\left(\frac{\Theta_{v,K}/T}{e^{\Theta_{v,K}/T}-1} - \ln(1-e^{-\Theta_{v,K}/T})\right)
\end{aligned}
$$

To get from the fourth line to the fifth line in the equation above, you have to multiply by $\frac{e^{\Theta_{v,K}/T}}{e^{\Theta_{v,K}/T}}$.

The contribution to internal thermal energy resulting from molecular vibration is

$$E_v = R\sum_K \Theta_{v,K}\left(\frac{1}{2} + \frac{1}{e^{\Theta_{v,K}/T}-1}\right)$$

Finally, the contribution to constant volume heat capacity is

$$C_v = R\sum_K e^{\Theta_{v,K}/T}\left(\frac{\Theta_{v,K}/T}{e^{-\Theta_{v,K}/T}-1}\right)^2$$

Low frequency modes (defined below) are *included* in the computations described above. Some of these modes may be internal rotations, and so may need to be treated separately, depending on the temperatures and barriers involved. In order to make it easier to correct for these modes, their contributions are printed out separately, so that they may be subtracted out. A low frequency mode in *Gaussian* is defined as one for which more than five percent of an assembly of molecules are likely to exist in excited vibrational states at room temperature. In other units, this corresponds to about 625 cm$^{-1}$, $1.9\times10^{13}$ Hz, or a vibrational temperature of 900 K.

It is possible to use *Gaussian* to automatically perform some of this analysis for you, via the `Freq=HindRot` keyword. This part of the code is still undergoing some improvements, so I will not go into it in detail. See P. Y. Ayala and H. B. Schlegel, J. Chem. Phys. **108** 2314 (1998) and references therein for more detail about the hindered rotor analysis in *Gaussian* and methods for correcting the partition functions due to these effects.

---

## 3 Thermochemistry output from *Gaussian*

This section describes most of the *Gaussian* thermochemistry output, and how it relates to the equations I've given above.

---

### 3.1 Output from a frequency calculation

In this section, I intentionally used a non-optimized structure, to show more output. For production runs, it is *very* important to use structures for which the first derivatives are zero — in other words, for minima, transition states and higher order saddle points. It is occasionally possible to use structures where one of the modes has non-zero first derivatives, such as along an IRC. For more information about why it is important to be at a stationary point on the potential energy surface, see my white paper on "Vibrational Analysis in *Gaussian*".

Much of the output is self-explanatory. I'll only comment on some of the output which may not be immediately clear. Some of the output is also described in "Exploring Chemistry with Electronic Structure Methods, Second Edition" by James B. Foresman and Æleen Frisch.

```
-------------------
- Thermochemistry -
-------------------

Temperature   298.150 Kelvin.  Pressure   1.00000 Atm.
Atom  1 has atomic number  6 and mass   12.00000
Atom  2 has atomic number  6 and mass   12.00000
Atom  3 has atomic number  1 and mass    1.00783
Atom  4 has atomic number  1 and mass    1.00783
Atom  5 has atomic number  1 and mass    1.00783
Atom  6 has atomic number  1 and mass    1.00783
Atom  7 has atomic number  1 and mass    1.00783
Atom  8 has atomic number  1 and mass    1.00783
Molecular mass:    30.04695 amu.
```

The next section gives some characteristics of the molecule based on the moments of inertia, including the rotational temperature and constants. The zero-point energy is calculated using only the non-imaginary frequencies.

```
Principal axes and moments of inertia in atomic units:
                 1         2         3
EIGENVALUES --  23.57594  88.34097  88.34208
          X      1.00000   0.00000   0.00000
          Y      0.00000   1.00000   0.00001
          Z      0.00000  -0.00001   1.00000
THIS MOLECULE IS AN ASYMMETRIC TOP.
ROTATIONAL SYMMETRY NUMBER  1.
ROTATIONAL TEMPERATURES (KELVIN)     3.67381    0.98044    0.98043
```

```
ROTATIONAL CONSTANTS (GHZ)        76.55013   20.42926   20.42901
Zero-point vibrational energy   204885.0 (Joules/Mol)
                                 48.96870 (Kcal/Mol)
```

If you see the following warning, it can be a sign that one of two things is happening. First, it often shows up if your structure is not a minimum with respect to all non-imaginary modes. You should go back and re-optimize your structure, since all the thermochemistry based on this structure is likely to be wrong. Second, it may indicate that there are internal rotations in your system. You should correct for errors caused by this situation.

```
WARNING-- EXPLICIT CONSIDERATION OF   1 DEGREES OF FREEDOM AS
          VIBRATIONS MAY CAUSE SIGNIFICANT ERROR
```

Then the vibrational temperatures and zero-point energy (ZPE):

```
VIBRATIONAL TEMPERATURES:    602.31  1607.07  1607.45  1683.83  1978.85
     (KELVIN)                1978.87  2303.03  2389.95  2389.96  2404.55
                             2417.29  2417.30  4202.52  4227.44  4244.32
                             4244.93  4291.74  4292.31
```

Zero-point correction=                          0.078037 (Hartree/Particle)

Each of the next few lines warrants some explanation. All of them include the zero-point energy. The first line gives the correction to the internal thermal energy, $E_{\text{tot}} = E_t + E_r + E_v + E_e$.

Thermal correction to Energy=                   0.081258

The next two lines, respectively, are

$$H_{\text{corr}} = E_{\text{tot}} + k_BT$$

and

$$G_{\text{corr}} = H_{\text{corr}} - TS_{\text{tot}},$$

where $S_{\text{tot}} = S_t + S_r + S_v + S_e$.

Thermal correction to Enthalpy=                 0.082202
Thermal correction to Gibbs Free Energy=        0.055064

The Gibbs free energy includes $\Delta PV = \Delta NRT$, so when it's applied to calculating $\Delta G$ for a reaction, $\Delta NRT \approx \Delta PV$ is already included. This means that $\Delta G$ will be computed correctly when the number of moles of gas changes during the course of a reaction.

The next four lines are estimates of the total energy of the molecule, after various corrections are applied. Since I've already used $E$ to represent internal thermal energy, I'll use $\mathcal{E}_0$ for the total electronic energy.

Sum of electronic and zero-point energies = $\mathcal{E}_0 + \mathcal{E}_{\text{ZPE}}$

Sum of electronic and thermal energies = $\mathcal{E}_0 + E_{\text{tot}}$

Sum of electronic and thermal enthalpies = $\mathcal{E}_0 + H_{\text{corr}}$

Sum of electronic and thermal free energies = $\mathcal{E}_0 + G_{\text{corr}}$

```
Sum of electronic and zero-point Energies=      -79.140431
Sum of electronic and thermal Energies=         -79.137210
Sum of electronic and thermal Enthalpies=       -79.136266
Sum of electronic and thermal Free Energies=    -79.163404
```

The next section is a table listing the individual contributions to the internal thermal energy ($E_{\text{tot}}$), constant volume heat capacity ($C_{\text{tot}}$) and entropy ($S_{\text{tot}}$). For every low frequency mode, there will be a line similar to the last one in this table (labeled `VIBRATION 1`). That line gives the contribution of that particular mode to $E_{\text{tot}}$, $C_{\text{tot}}$ and $S_{\text{tot}}$. This allows you to subtract out these values if you believe they are a source of error.

```
                         E (Thermal)         CV                S
                         KCAL/MOL      CAL/MOL-KELVIN    CAL/MOL-KELVIN
TOTAL                    50.990            8.636           57.118
ELECTRONIC               0.000             0.000            0.000
TRANSLATIONAL            0.889             2.981           36.134
ROTATIONAL               0.889             2.981           19.848
VIBRATIONAL              49.213            2.674            1.136
VIBRATION  1             0.781             1.430            0.897
```

Finally, there is a table listing the individual contributions to the partition function. The lines labeled `BOT` are for the vibrational partition function computed with the zero of energy being the bottom of the well, while those labeled with (`V=0`) are computed with the zero of energy being the first vibrational level. Again, special lines are printed out for the low frequency modes.

```
                         Q              LOG10(Q)         LN(Q)
TOTAL BOT           0.470577D-25      -25.327369       -58.318422
TOTAL V=0           0.368746D+11       10.566728        24.330790
VIB (BOT)           0.149700D-35      -35.824779       -82.489602
VIB (BOT)  1        0.419879D+00       -0.376876        -0.867789
VIB (V=0)           0.117305D+01        0.069318         0.159610
VIB (V=0)  1        0.115292D+01        0.061797         0.142294
ELECTRONIC          0.100000D+01        0.000000         0.000000
TRANSLATIONAL       0.647383D+07        6.811161        15.683278
ROTATIONAL          0.485567D+04        3.686249         8.487901
```

---

### 3.2 Output from compound model chemistries

This section explains what the various thermochemical quantities in the summary out of a compound model chemistry, such as CBS-QB3 or G2, means.

I'll use a CBS-QB3 calculation on water, but the discussion is directly applicable to all the other compound models available in Gaussian. The two lines of interest from the output look like:

```
CBS-QB3 (0 K)=           -76.337451 CBS-QB3 Energy=           -76.334615
CBS-QB3 Enthalpy=        -76.333671 CBS-QB3 Free Energy=      -76.355097
```

Here are the meanings of each of those quantities.

- **CBS-QB3 (0 K):** This is the total electronic energy as defined by the compound model, including the zero-point energy scaled by the factor defined in the model.

- **CBS-QB3 Energy:** This is the total electronic energy plus the internal thermal energy, which comes directly from the thermochemistry output in the frequency part of the output. The scaled zero-point energy is included.

- **CBS-QB3 Enthalpy:** This is the total electronic energy plus $H_{\text{corr}}$, as it is described above with the unscaled zero-point energy removed. This sum is appropriate for calculating enthalpies of reaction, as described below.

- **CBS-QB3 Free Energy:** This is the total electronic energy plus $G_{\text{corr}}$, as it is described above, again with the unscaled zero-point energy removed. This sum is appropriate for calculating Gibbs free energies of reaction, also as described below.

---

## 4 Worked-out Examples

In this section I will show how to use these results to generate various thermochemical information.

I've run calculations for each of the reactants and products in the reaction where ethyl radical abstracts a hydrogen atom from molecular hydrogen:

$$C_2H_5 + H_2 \rightarrow C_2H_6 + H$$

as well as for the transition state (all at 1.0 atmospheres and 298.15K). The thermochemistry output from *Gaussian* is summarized in Table 1.

Once you have the data for all the relevant species, you can calculate the quantities you are interested in. Unless otherwise specified, all enthalpies are at 298.15K. I'll use $298K \approx 298.15K$ to shorten the equations.

---

**Table 1:** Calculated thermochemistry values from *Gaussian* for the reaction $C_2H_5 + H_2 \rightarrow C_2H_6 + H$. All values are in Hartrees.

|                | C$_2$H$_5$ | H$_2$     | C$_2$H$_6$ | H         | C         |
|----------------|------------|-----------|------------|-----------|-----------|
| $\mathcal{E}_0$          | $-$77.662998 | $-$1.117506 | $-$78.306179 | $-$0.466582 | $-$37.198393 |
| $\mathcal{E}_{\text{ZPE}}$ | 0.070833   | 0.012487  | 0.089704   | 0.000000  | 0.000000  |
| $E_{\text{tot}}$         | 0.074497   | 0.014847  | 0.093060   | 0.001416  | 0.001416  |
| $H_{\text{corr}}$        | 0.075441   | 0.015792  | 0.094005   | 0.002360  | 0.002360  |
| $G_{\text{corr}}$        | 0.046513   | 0.001079  | 0.068316   | $-$0.010654 | $-$0.014545 |
| $\mathcal{E}_0+\mathcal{E}_{\text{ZPE}}$ | $-$77.592165 | $-$1.105019 | $-$78.216475 | $-$0.466582 | $-$37.198393 |
| $\mathcal{E}_0+E_{\text{tot}}$ | $-$77.588501 | $-$1.102658 | $-$78.213119 | $-$0.465166 | $-$37.196976 |
| $\mathcal{E}_0+H_{\text{corr}}$ | $-$77.587557 | $-$1.101714 | $-$78.212174 | $-$0.464221 | $-$37.196032 |
| $\mathcal{E}_0+G_{\text{corr}}$ | $-$77.616485 | $-$1.116427 | $-$78.237863 | $-$0.477236 | $-$37.212938 |

---

### 4.1 Enthalpies and Free Energies of Reaction

The usual way to calculate enthalpies of reaction is to calculate heats of formation, and take the appropriate sums and difference.

$$\Delta_r H^\circ(298K) = \sum_{\text{products}} \Delta_f H^\circ_{\text{prod}}(298K) - \sum_{\text{reactants}} \Delta_f H^\circ_{\text{react}}(298K).$$

However, since Gaussian provides the sum of electronic and thermal enthalpies, there is a short cut: namely, to simply take the difference of the sums of these values for the reactants and the products. This works since the number of atoms of each element is the same on both sides of the reaction, therefore all the atomic information cancels out, and you need only the molecular data.

For example, using the information in Table 1, the enthalpy of reaction can be calculated simply by

$$
\begin{aligned}
\Delta_r H^\circ(298K) &= \sum(\mathcal{E}_0 + H_{\text{corr}})_{\text{products}} - \sum(\mathcal{E}_0 + H_{\text{corr}})_{\text{reactants}} \\
&= ((-78.212174 + -0.464221) - (-77.587557 + -1.101714)) * 627.5095 \\
&= 0.012876 * 627.5095 \\
&= 8.08 \text{ kcal/mol}
\end{aligned}
$$

The same short cut can be used to calculate Gibbs free energies of reaction:

$$
\begin{aligned}
\Delta_r H^\circ(298K) &= \sum(\mathcal{E}_0 + G_{\text{corr}})_{\text{products}} - \sum(\mathcal{E}_0 + G_{\text{corr}})_{\text{reactants}} \\
&= ((-78.237863 + -0.477236) - (-77.616485 + -1.116427)) * 627.5095 \\
&= 0.017813 * 627.5095 \\
&= 11.18 \text{ kcal/mol}
\end{aligned}
$$

---

### 4.2 Rates of Reaction

In this section I'll show how to compute rates of reaction using the output from *Gaussian*. I'll be using results derived from transition state theory in section 28-8 of "Physical Chemistry, A Molecular Approach" by D. A. McQuarrie and J. D. Simon. The key equation (number 28.72, in that text) for calculating reaction rates is

$$k(T) = \frac{k_BT}{hc^\circ}e^{-\Delta^\ddagger G^\circ/RT}$$

---

**Table 2:** Total HF/STO-3G electronic energies and sum of electronic and thermal free energies for atoms molecules and transition state complex of the reaction FH + Cl $\rightarrow$ F + HCl and the deuterium substituted analog.

| Compound | $\mathcal{E}_0$ | $\mathcal{E}_0 + G_{\text{corr}}$ |
|----------|----------------|----------------------------------|
| HF       | $-$98.572847   | $-$98.579127                     |
| HD       | $-$98.572847   | $-$98.582608                     |
| Cl       | $-$454.542193  | $-$454.557870                    |
| HCl      | $-$455.136012  | $-$455.146251                    |
| DCl      | $-$455.136012  | $-$455.149092                    |
| F        | $-$97.986505   | $-$98.001318                     |
| FHCl     | $-$553.090218  | $-$553.109488                    |
| FDCl     | $-$553.090218  | $-$553.110424                    |

I'll use $c^\circ = 1$ for the concentration. For simple reactions, the rest is simply plugging in the numbers. First, of course, we need to get the numbers. I've run HF/STO-3G frequency calculation for reaction FH + Cl $\rightarrow$ F + HCl and also for the reaction with deuterium substituted for hydrogen. The results are summarized in Table 2. I put the total electronic energies of each compound into the table as well to illustrate the point that the final geometry and electronic energy are independent of the masses of the atoms. Indeed, the cartesian force constants themselves are independent of the masses. Only the vibrational analysis, and quantities derived from it, are mass dependent.

The first step in calculating the rates of these reactions is to compute the free energy of activation, $\Delta^\ddagger G^\circ$ ((H) is for the hydrogen reaction, (D) is for deuterium reaction):

$$
\begin{aligned}
\Delta^\ddagger G^\circ(H) &= -553.109488 - (-98.579127 + -454.557870) \\
&= 0.027509 \text{ Hartrees} \\
&= 0.027509 * 627.5095 = 17.26 \text{ kcal/mol}
\end{aligned}
$$

$$
\begin{aligned}
\Delta^\ddagger G^\circ(D) &= -553.110424 - (-98.582608 + -454.557870) \\
&= 0.030054 \text{ Hartrees} \\
&= 0.030054 * 627.5095 = 18.86 \text{ kcal/mol}
\end{aligned}
$$

Then we can calculate the reaction rates. The values for the constants are listed in the appendix. I've taken $c^\circ = 1$.

$$
\begin{aligned}
k(298, H) &= \frac{k_BT}{hc^\circ}e^{-\Delta^\ddagger G^\circ/RT} \\
&= \frac{1.380662\times10^{-23}(298.15)}{6.626176\times10^{-34}(1)} \exp\left(\frac{-17.26*1000}{1.987*298.15}\right) \\
&= 6.2125\times10^{12}e^{-29.13} \\
&= 1.38 \text{s}^{-1}
\end{aligned}
$$

$$
\begin{aligned}
k(298, D) &= 6.2125\times10^{12} \exp\left(\frac{-18.86*1000}{1.987*298.15}\right) \\
&= 6.2125\times10^{12}e^{-31.835} \\
&= 0.0928 \text{s}^{-1}
\end{aligned}
$$

So we see that the deuterium reaction is indeed slower, as we would expect. Again, these calculations were carried out at the HF/STO-3G level, for illustration purposes, not for research grade results. More complex reactions will need more sophisticated analyses, perhaps including careful determination of the effects of low frequency modes on the transition state, and tunneling effects.

---

### 4.3 Enthalpies and Free Energies of Formation

Calculating enthalpies of formation is a straight-forward, albeit somewhat tedious task, which can be split into a couple of steps. The first step is to calculate the enthalpies of formation ($\Delta_f H^\circ(0K)$) of the species involved in the reaction. The second step is to calculate the enthalpies of formation of the species at 298K.

Calculating the Gibbs free energy of reaction is similar, except we have to add in the entropy term:

$$\Delta_f G^\circ(298) = \Delta_f H^\circ(298K) - T(S^\circ(M,298K) - \sum S^\circ(X,298K))$$

To calculate these quantities, we need a few component pieces first. In the descriptions below, I will use $M$ to stand for the molecule, and $X$ to represent each element which makes up $M$, and $x$ will be the number of atoms of $X$ in $M$.

- **Atomization energy of the molecule, $\sum D_0(M)$:**
  These are readily calculated from the total energies of the molecule ($\mathcal{E}_0(M)$), the zero-point energy of the molecule ($\mathcal{E}_{\text{ZPE}}(M)$) and the constituent atoms:
  $$\sum D_0(M) = \sum_{\text{atoms}} x\mathcal{E}_0(X) - \mathcal{E}_0(M) - \mathcal{E}_{\text{ZPE}}(M)$$

- **Heats of formation of the atoms at 0K, $\Delta_f H^\circ(X,0K)$:**
  I have tabulated recommended values for the heats of formation of the first and second row atomic elements at 0K in Table 3. There are (at least) two schools of thought with respect to the which atomic heat of formation data is most appropriate. Some authors prefer to use purely experimental data for the heats of formation (Curtiss, et. al., J. Chem. Phys. **106**, 1063 (1997)). Others (Ochterski, et. al., J. Am. Chem. Soc. **117**, 11299 (1995)), prefer to use a combination of experiment and computation to obtain more accurate values. The elements of concern are boron, beryllium and silicon. I have arranged Table 3 so that either may be used; the experimental results are on the top, while the computational results for the three elements with large experimental uncertainty are listed below that.

- **Enthalpy corrections of the atomic elements, $H^\circ_X(298K) - H^\circ_X(0K)$ :**
  The enthalpy corrections of the first and second row atomic elements are also included in Table 3. These are used to convert the atomic heats of formation at 0K to those at 298.15K, and are given for the elements in their standard states. Since they do not depend on the accuracy of the heat of formation of the atom, they are the same for both the calculated and experimental data.

  This is generally *not* the same as the output from *Gaussian* for a calculation on an isolated gas-phase atom. These values are referenced to the standard states of the elements. For example, the value for hydrogen atom is 1.01 kcal/mol. This is $(H^\circ_{H_2}(298K) - H^\circ_{H_2}(0K))/2$, and not $H^\circ_H(298K) - H^\circ_H(0K)$, which is what *Gaussian* calculates.

- **Enthalpy correction for the molecule, $H^\circ_M(298K) - H^\circ_M(0K)$ :**
  For a molecule, this is $H_{\text{corr}} - \mathcal{E}_{\text{ZPE}}(M)$, where $H_{\text{corr}}$ is the value printed out in the line labeled "Thermal correction to Enthalpy" in *Gaussian* output. Remember, though, that the output is in Hartrees/particle, and needs to be converted to kcal/mol. The conversion factor is 1 Hartree = 627.5095 kcal/mol.

- **Entropy for the atoms, $S^\circ_X(298K)$ :**
  These are summarized in Table 3. The values were taken from the JANAF tables (M. W. Chase, Jr., C. A. Davies, J. R. Downey, Jr., D. J. Frurip, R. A. McDonald, and A. N. Syverud, J. Phys. Ref. Data **14** Suppl. No. 1 (1985)). Again, these values are referenced to the standard states of the elements, and will disagree with values *Gaussian* calculates for the gas-phase isolated atoms.

- **Entropy for the molecule, $S^\circ_M(298K)$ :**
  *Gaussian* calculates $G = H - TS$, and prints it out on the line labeled "Thermal correction to Gibbs Free Energy". The entropy can be teased out of this using $S = (H-G)/T$.

Putting all these pieces together, we can finally take the steps necessary to calculate $\Delta_f H^\circ(298K)$ and $\Delta_f G^\circ(298K)$:

1. Calculate $\Delta_f H^\circ(M,0K)$ for each molecule:
   $$
   \begin{aligned}
   \Delta_f H^\circ(M,0K) &= \sum_{\text{atoms}} x\Delta_f H^\circ(X,0K) - \sum D_0(M) \\
   &= \sum_{\text{atoms}} x\Delta_f H^\circ(X,0K) - \left(\sum_{\text{atoms}} x\mathcal{E}_0(X) - \mathcal{E}_0(M)\right)
   \end{aligned}
   $$

---

**Table 3:** Experimental and calculated enthalpies of formation of elements (kcal mol$^{-1}$) and entropies of atoms (cal mol$^{-1}$ K$^{-1}$). $^a$ Experimental enthalpy values taken from J. Chem. Phys. **106**, 1063 (1997). $^b$ Calculated enthalpy values taken from J. Am. Chem. Soc. **117**, 11299 (1995). $H^\circ(298K)-H^\circ(0K)$ is the same for both calculated and experimental, and is taken for elements in their standard states. $^c$ Entropy values taken from JANAF Thermochemical Tables: M. W. Chase, Jr., C. A. Davies, J. R. Downey, Jr., D. J. Frurip, R. A. McDonald, and A. N. Syverud, J. Phys. Ref. Data **14** Suppl. No. 1 (1985). $^d$ No error bars are given for Mg in JANAF.

| Element | $\Delta_f H^\circ(0K)$ | $H^\circ(298K)-H^\circ(0K)$ | $S^\circ(298K)$ |
|---------|------------------------|------------------------------|-----------------|
| **Experimental**$^a$ | | | |
| H       | 51.63$\pm$0.001       | 1.01                         | 27.418$\pm$0.004 |
| Li      | 37.69$\pm$0.2         | 1.10                         | 33.169$\pm$0.006 |
| Be      | 76.48$\pm$1.2         | 0.46                         | 32.570$\pm$0.005 |
| B       | 136.2 $\pm$0.2        | 0.29                         | 36.672$\pm$0.008 |
| C       | 169.98$\pm$0.1        | 0.25                         | 37.787$\pm$0.21  |
| N       | 112.53$\pm$0.02       | 1.04                         | 36.640$\pm$0.01  |
| O       | 58.99$\pm$0.02        | 1.04                         | 38.494$\pm$0.005 |
| F       | 18.47$\pm$0.07        | 1.05                         | 37.942$\pm$0.001 |
| Na      | 25.69$\pm$0.17        | 1.54                         | 36.727$\pm$0.006 |
| Mg      | 34.87$\pm$0.2         | 1.19                         | 8.237$\pm^d$    |
| Al      | 78.23$\pm$1.0         | 1.08                         | 39.329$\pm$0.01  |
| Si      | 106.6 $\pm$1.9        | 0.76                         | 40.148$\pm$0.008 |
| P       | 75.42$\pm$0.2         | 1.28                         | 39.005$\pm$0.01  |
| S       | 65.66$\pm$0.06        | 1.05                         | 40.112$\pm$0.008 |
| Cl      | 28.59$\pm$0.001       | 1.10                         | 39.481$\pm$0.001 |
| **Calculated**$^b$ | | | |
| Be      | 75.8 $\pm$0.8         | 0.46                         | 32.570$\pm$0.005 |
| B       | 136.2 $\pm$0.2        | 0.29                         | 36.672$\pm$0.008 |
| Si      | 108.1 $\pm$0.5        | 0.76                         | 40.148$\pm$0.008 |

2. Calculate $\Delta_f H^\circ(M,298K)$ for each molecule:
   $$
   \begin{aligned}
   \Delta_f H^\circ(M,298K) =& \ \Delta_f H^\circ(M,0K) + (H^\circ_M(298K) - H^\circ_M(0K)) \\
   &- \sum_{\text{atoms}} x(H^\circ_X(298K) - H^\circ_X(0K))
   \end{aligned}
   $$

3. Calculate $\Delta_f G^\circ(M,298K)$ for each molecule:
   $$\Delta_f G^\circ(M,298K) = \Delta_f H^\circ(298K) - 298.15(S^\circ(M,298K) - \sum S^\circ(X,298K))$$

Here is a worked out example, where I've calculated $\Delta_f H^\circ(298K)$ for the reactants and products in the reaction I described above.

First, I'll calculate $\Delta_f H^\circ(0K)$ for one of the species:

$$
\begin{aligned}
\Delta_f H^\circ(C_2H_6,0K) &= 2*169.98 + 6*51.63 \\
&\quad -627.5095*(2*(-37.198393) + 6*(-0.466582) - (-78.216475)) \\
&= 649.74 - 627.5095*1.020197 \\
&= 9.56
\end{aligned}
$$

The next step is to calculate the $\Delta_f H^\circ(298K)$:

$$
\begin{aligned}
\Delta_f H^\circ(C_2H_6,298K) &= 9.56 + 627.5095*(0.094005 - 0.089704) - (2*0.25 + 6*1.01) \\
&= 9.56 + 2.70 - 6.56 \\
&= 5.70
\end{aligned}
$$

To calculate the Gibbs free energy of formation, we have (the factors of 1000 are to convert kcal to or from cal):

$$
\begin{aligned}
\Delta_f G^\circ(C_2H_6,298K) &= 5.70 + 298.15(627.5095*(0.094005 - 0.068316)/298.15 - \\
&\qquad (2*37.787 + 6*27.418)/1000 \\
&= 5.70 + 298.15*(0.054067 - 0.240082) \\
&= -49.76
\end{aligned}
$$

---

## 5 Summary

The essential message is this: the basic equations used to calculate thermochemical quantities in *Gaussian* are based on those used in standard texts. Since the vibrational partition function depends on the frequencies, you must use a structure that is either a minimum or a saddle point. For electronic contributions to the partition function, it is assumed that the first and all higher states are inaccessible at the temperature the calculation is done at. The data generated by *Gaussian* can be used to calculate heats and free energies of reactions as well as absolute rate information.

---

## Appendix

### Symbols

$C_e$ = contribution to the heat capacity due to electronic motion

$C_r$ = contribution to the heat capacity due to rotational motion

$C_{\text{tot}}$ = total heat capacity ($C_t + C_r + C_v + C_e$)

$C_t$ = contribution to the heat capacity due to translation

$C_v$ = contribution to the heat capacity due to vibrational motion

$E_e$ = internal energy due to electronic motion

$E_r$ = internal energy due to rotational motion

$E_{\text{tot}}$ = total internal energy ($E_t + E_r + E_v + E_e$)

$E_t$ = internal energy due to translation

$E_v$ = internal energy due to vibrational motion

$G_{\text{corr}}$ = correction to the Gibbs free energy due to internal energy

$H_{\text{corr}}$ = correction to the enthalpy due to internal energy

$I$ = moment of inertia

$K$ = index of vibrational modes

$N$ = number of moles

$N_A$ = Avogadro's number

$P$ = pressure (default is 1 atmosphere)

$R$ = gas constant = 8.31441 J/(mol K) = 1.987 kcal/(mol K)

$S_e$ = entropy due to electronic motion

$S_r$ = entropy due to rotational motion

$S_{\text{tot}}$ = total entropy ($S_t + S_r + S_v + S_e$)

$S_t$ = entropy due to translation

$S_v$ = entropy due to vibrational motion

$T$ = temperature (default is 298.15)

$V$ = volume

$\Theta_r, \Theta_{r,(xyz)}$ = characteristic temperature for rotation (in the $x$, $y$ or $z$ plane)

$\Theta_{v,K}$ = characteristic temperature for vibration $K$

$k_B$ = Boltzmann constant = $1.380662 \times 10^{-23}$ J/K

$\epsilon_n$ = the energy of the $n$-th energy level

$\omega_n$ = the degeneracy of the $n$-th energy level

$\sigma_r$ = symmetry number for rotation

$h$ = Planck's constant = $6.626176 \times 10^{-34}$ J s

$m$ = mass of the molecule

$n$ = number of particles (always 1)

$q_e$ = electronic partition function

$q_r$ = rotational partition function

$q_t$ = translational partition function

$q_v$ = vibrational partition function

$\mathcal{E}_{\text{ZPE}}$ = zero-point energy of the molecule

$\mathcal{E}_0$ = the total electronic energy, the MP2 energy for example

$H^\circ, S^\circ, G^\circ$ = standard enthalpy, entropy and Gibbs free energy — each compound is in its standard state at the given temperature

$\Delta^\ddagger G^\circ$ = Gibbs free energy of activation

$c^\circ$ = concentration (taken to be 1)

$k(T)$ = reaction rate at temperature T
