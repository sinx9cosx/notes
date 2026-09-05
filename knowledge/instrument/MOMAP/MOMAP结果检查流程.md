---
tags:
  - 计算化学
  - research
  - 后处理
Category:
  - 笔记
---

# MOMAP 结果检查流程（evc / kr / kic）

跑完 evc 或 kr/kic 计算后，按本笔记三步走：① evc 输出体检 → ② 相关函数收敛验证 → ③ 取速率与光谱结果。kr（荧光光谱 + 辐射速率）与 kic（内转换速率）两条路线的输出文件对照如下：

| 环节 | kr 路线（荧光/kr） | kic 路线（IC/kic） |
| --- | --- | --- |
| evc 输入 | 基态 + 激发态 opt freq .log/.fchk | 同左，另加激发态 nacme .log |
| evc 输出 | `evc.cart.dat`、`evc.dint.dat`、`evc.out` | 同左，另加 `evc.cart.nac` |
| 速率计算 | `spec.tvcf.*` | `ic.tvcf.*` |

kr 路线无 nac 文件，这是两条路线目录最直观的区别。

## 一、evc 输出检查

1. **log 成功标志**：`log`（momap.py 输出）中应有 ==`ALL SUCCESSFULLY DONE`== 与 ==`Normal finish of evc calculation`==，且同目录生成 `evc.cart.dat` / `evc.dint.dat` / `evc.out`。
2. **cart vs dint 重组能对比**：`evc.cart.dat` 与 `evc.dint.dat` 各自尾部的 `Total reorganization energy`（cm⁻¹）应接近；两者之差 ==**< 1000 cm⁻¹ 用 cart，否则用 dint**==（MOMAP 官方手册标准）。后续 momap.inp 的 `DSFile` 要对应所选文件。
3. **evc.cart.dat 关键信息位置**：
   - 头部：`ZPE1 (Ground)` / `ZPE2 (Excited)` / `ZPE2 - ZPE1`（cm⁻¹）。
   - 中部模式表各列：`n / m / sym / freq(cm⁻¹) / D(a.u.) / delta / HR / lam(cm⁻¹)`，其中 $HR = 0.5 \cdot \delta^2$，$\lambda = HR \cdot \hbar \cdot \omega$。
   - 尾部：`Total reorganization energy`（重组能）。
   - Duschinsky 段：`Delta DUSH = xx %`（Duschinsky 混合程度）。
4. **虚频检查**：模式表中 freq 不应有负值；**前 6 个模式是平转动伪模式，freq≈0 属正常**，不参与后续物理量。
5. **DUSHIN 设置依据**：Delta DUSH 大（经验上 >50% 算显著）说明 Duschinsky 混合显著，后续 momap.inp 必须 ==`DUSHIN = .t.`==。
6. **正交性检验**：cart.dat 中 `BEGIN_DUSH_ORTH_TEST EPS = 0.001` 段若无 FAIL 输出 → Duschinsky 矩阵正交性通过。
7. **nac 文件（仅 kic 路线有，重点）**：
   - 头部 `Energy Difference ... a.u. = ... eV`：应等于该电子对的垂直发射能（自洽性核对）。
   - 前 6 行是平转动伪模式（freq≈0），其 nacm 数值无物理意义，MOMAP 会自动排除，忽略即可。
   - 真振动模式看 `nacm_jpca(s-1)` 列，量级大的模式是 IC 的主要贡献通道；若日后 kic 结果异常，优先回来核对 nac 文件的能量差与 nacme 输入的 route 是否含溶剂（scrf）。
8. **易混点**：kr 路线的 evc 目录（momap.inp 只有 ffreq 两项）**不产 nac**；kic 必须用含 `fnacme` 的 evc 目录里的 `evc.cart.nac`，别拿错目录。

## 二、相关函数收敛验证（ft.dat）

1. **列结构**：kr 的 `spec.tvcf.ft.dat` 与 kic 的 `ic.tvcf.ft.dat` 列数不同：
   - kr：5 列

     ```
     #time(fs)  abs_FC_Re  abs_FC_Im  emi_FC_Re  emi_FC_Im
     ```

     时间轴为 −tmax ~ +tmax 对称。
   - kic：仅 3 列，无 abs/emi 之分

     ```
     #time(fs)  IC_ft_Re(au)  IC_ft_Im(au)
     ```

2. **画哪列（重要细节）**：官方手册说"用前两列"是笼统说法——前两列是 time + **abs**（吸收）相关函数实部；**荧光（发射）谱的收敛应画第 1 列 vs 第 4 列 `emi_FC_Re`**，吸收谱才画第 2 列 `abs_FC_Re`。两者衰减行为通常同步。

3. **收敛判据**：相关函数实部的包络应在到达 tmax 之前 ==衰减到接近 0、并停止大幅振荡==（可接受的情形：衰减到初值的 ~0.1% 以下；曲线中间允许有振荡回弹，关键是整体包络下降、末端不翘起）。

4. **dt/tmax 参数常识**：官方手册建议 tmax ≥ 5000 fs、dt ≤ 0.001 fs；但大分子实际常用 tmax = 1000 fs、dt = 0.01 fs——计算成本与步数（tmax/dt）近似线性增长，tmax 加大几倍成本翻几倍。dt = 0.01 fs 的 Nyquist 频率上限 $\nu_{max} = \frac{1}{2 \Delta t} \approx 1.7\times10^{6}\ \mathrm{cm^{-1}}$，远超谱上限 `Emax = 0.3 au`（≈6.6×10⁴ cm⁻¹）与分子最高振动频率（~3000 cm⁻¹），时间分辨率足够，不必照手册拉满。

5. 绘图工具任意（Origin 等），画 |t| 一侧即可。

## 三、取结果

1. **kr（辐射速率）**：`spec.tvcf.log` 末尾搜 `radiative rate`：取 `/s` 与 `ns` 两个数（如 `X.XXE+07 /s, XX.XX ns`）；同行的前一个极小数值是 a.u. 单位，不用。速率与寿命、振子强度的关系可参见 [[激发态的平均寿命]] 与 [[振子强度]]。
2. **荧光光谱**：`spec.tvcf.spec.dat` 共 7 列：

   ```
   #1Energy(Hartree) 2Energy(eV) 3WaveNumber(cm-1) 4WaveLength(nm) 5FC_abs 6FC_emi 7FC_emi_intensity
   ```

   绘图：x 取波长（第 4 列，或波数第 3 列），y 取第 7 列 ==**FC_emi_intensity**==（发射谱强度）。
3. **谱峰参考值**：log 里的 `E0-0`（0-0 跃迁，cm⁻¹）与 `Vertical Energy`（垂直发射/吸收，cm⁻¹）可作谱峰位置参考；log 开头（第 1 行）`Calculate D1:` 表与 evc.cart.dat 模式表同源、可互核（列名不同：imode/Freq/D/Huang_Rhys/Reog. Energy，按 |D| 降序）。
4. **kic（内转换速率）**：`ic.tvcf.log` 末尾读 kic 值；收敛判据同第二节（包络在 tmax 前衰减近零、停止振荡），但画图时 kic 画 `ic.tvcf.ft.dat` 的第 1 列 vs 第 2 列（`IC_ft_Re`）。
5. **干净性检查**：对 log 全文搜 `Warning`/`Error`（区分大小写），应无匹配；==无警告才算干净输出==。

## 四、常见疑点清单

> [!warning] f 值为 0 而速率正常
> `spec.tvcf.log` 末尾 `Oscillator strength = 0.0000000000` 而 radiative rate 数值正常 → 疑为该行显示问题，f 值不要取它（需要 f 可从 kr 按爱因斯坦关系反推或另算）。

> [!tip] radiative rate 一行两个数值
> `radiative rate` 同行出现两个数值 → 前者是 a.u.，取 `/s` 与 `ns`。

> [!note] nac 前 6 行无意义
> nac 文件前 6 个平转动伪模式的 nacm 数值无意义（已由 MOMAP 排除）。

> [!warning] ft.dat 画错列
> ft.dat 画错列（画了 abs 列去判断发射收敛）→ 荧光看 `emi_FC_Re`。

> [!warning] kic 拿错 evc 目录
> kic 拿错 evc 目录（用了 kr 路线目录的 dat，那里没有 nac）→ 必须用含 `fnacme` 的 evc 目录里的 `evc.cart.nac`。
