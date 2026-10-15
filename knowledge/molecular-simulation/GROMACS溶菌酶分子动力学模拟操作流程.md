---
tags:
  - 分子模拟
  - GROMACS
  - 计算化学
Category:
  - 笔记
---
# 溶菌酶模拟操作流程

本笔记记录 GROMACS 溶菌酶（lysozyme）分子动力学模拟的完整命令流程、mdp 参数与结果核对。

> **作业要求**：
> 完整执行溶菌酶分子动力学模拟例子；
> 精读各步命令使用说明和讲解
> 最后用“gmxgyrate”命令计算NPT模拟获得的溶菌酶蛋白在水溶液中的均方回转半径，将计算结果导入originlab画图，
> 将显示的图拍照或截图，发到老师邮箱，作为这次课后作业。

## 环境与目录

- 软件：GROMACS 2018.8 原生 Windows 64 位版，由 Sobereva 在 Visual Studio 2017 下编译（http://sobereva.com/458）
- 安装路径：`F:\projects\molecular-simulation-hw\3n\gmx2018.8_win64`
- `RUN.bat` 调用 `set_env.bat`，后者执行 `set path=%path%;%cd%\bin`，作用是将 `bin` 加入 `PATH` 后开启一个 cmd 窗口，使 `gmx` 命令可用
- 工作目录：`F:\projects\molecular-simulation-hw\3n\tu1n`，全部命令在此目录执行
- 并行方式：thread-MPI，18 线程
- 实测性能：NPT 11.5 ns/day，NVT 17.3 ns/day
- 自带力场（force field）目录含 `oplsaa.ff`（OPLS-AA），水模型文件为 `spc216.gro`

### 起始结构

`1aki.pdb` 为鸡蛋清溶菌酶（Hen Egg-White Lysozyme）1.5 Å X 射线晶体结构，单链 A，129 个残基，1001 个重原子，不含氢。该结构含 78 个结晶水（HOH）与 1 个额外 HOH 记录，用 HOH 过滤可全部去除。

## 操作流程

### 1 去除结晶水

```bash
grep -v HOH 1aki.pdb > 1AKI_clean.pdb
```

产物为 `1AKI_clean.pdb`。cmd.exe 无 `grep`，需在 Git Bash 中执行，或改用 `findstr /V HOH 1aki.pdb > 1AKI_clean.pdb`。

### 2 生成拓扑（topology）

```bash
gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce
```

- 交互一：力场菜单选择 OPLS-AA（本机列表中为第 15 项）
- 交互二：HIS15 质子化态菜单，选项为 HISD（质子在 ND1）、HISE（质子在 NE2）、HISH（双质子化带正电）；中性组氨酸选择 HISD 或 HISE
- `-water spce` 已指定水模型为 SPC/E，故不再询问水模型

产物为 `1AKI_processed.gro`、`topol.top`、`posre.itp`。

### 3 建立模拟盒

```bash
gmx editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.0 -bt cubic
```

`-c` 将蛋白置于盒中心，`-d 1.0` 要求蛋白表面与盒壁的最小距离为 1.0 nm，`-bt cubic` 指定立方盒。产物为 `1AKI_newbox.gro`。

### 4 溶剂化（solvation）

```bash
gmx solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top
```

`-p topol.top` 将加入的水分子数写入拓扑。产物为 `1AKI_solv.gro`。

### 5 加抗衡离子（counter ions）

```bash
gmx grompp -f ions.mdp -c 1AKI_solv.gro -p topol.top -o ions.tpr
gmx genion -s ions.tpr -o 1AKI_solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

交互中选择被替换的组，选 SOL（本机列表中为第 13 项）。`-neutral` 表示只加入恰好中和蛋白净电荷的离子数；溶菌酶为碱性蛋白、净电荷为 +8，故加入 8 个 Cl⁻。产物为 `ions.tpr`、`1AKI_solv_ions.gro`。

### 6 能量最小化（energy minimization）

```bash
gmx grompp -f minim.mdp -c 1AKI_solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -v -deffnm em
gmx energy -f em.edr -o potential.xvg
```

`gmx energy` 交互中选择 Potential 项，再输入 0 退出。产物为 `em.gro`、`em.log`、`em.edr`、`em.trr`。

### 7 NVT 平衡

```bash
gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
gmx mdrun -deffnm nvt
gmx energy -f nvt.edr -o temperature.xvg
```

`gmx energy` 交互中选择 Temperature 项。产物为 `nvt.gro`、`nvt.cpt`、`nvt.tpr`、`nvt.trr`、`nvt.edr`、`nvt.log`。

### 8 NPT 平衡

```bash
gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
gmx mdrun -deffnm npt
gmx energy -f npt.edr -o pressure.xvg
```

`gmx energy` 交互中选择 Pressure 项。产物为 `npt.tpr`、`npt.gro`、`npt.cpt`、`npt.trr`、`npt.edr`、`npt.log`。

### 9 回转半径

```bash
gmx gyrate -f npt.trr -s npt.tpr -o gyrate.xvg
```

交互中选择组，选 Protein（本机列表中为第 1 项）。输出文件的列含义见「回转半径」一节。

## mdp 参数

### 通用参数

| 参数 | minim.mdp / ions.mdp |
| --- | --- |
| `integrator` | `steep`（最速下降法） |
| `emtol` | `1000.0`，即最大力小于 1000 kJ/mol/nm 时停止 |
| `nsteps` | `50000` |

### 平衡参数

| 参数 | nvt.mdp | npt.mdp |
| --- | --- | --- |
| `integrator` | `md` | `md` |
| `dt` | `0.002` ps | `0.002` ps |
| `nsteps` | `1000`（合计 2 ps） | `1000`（合计 2 ps） |
| `define` | `-DPOSRES` | `-DPOSRES` |
| `constraints` | `h-bonds` | `h-bonds` |
| `tcoupl` | `V-rescale` | `V-rescale` |
| `tc-grps` | `Protein Non-Protein` | `Protein Non-Protein` |
| `ref_t` | `300 300` | `300 300` |
| `gen_vel` | `yes` | `no` |
| `continuation` | — | `yes` |
| `pcoupl` | `no` | `Parrinello-Rahman` |
| `pcoupltype` | — | `isotropic` |
| `ref_p` | — | `1.0` bar |
| `tau_p` | — | `2.0` ps |
| `refcoord_scaling` | — | `com` |
| `nstxout` / `nstvout` / `nstenergy` / `nstlog` | `100` | `100` |

NVT 阶段不做压力耦合，故 `pcoupl = no`。`constraints = h-bonds` 表示以 LINCS 约束含氢键的键长。输出频率 100 步对应 0.2 ps 一次。

### 长模拟变体

| 参数 | npt1.mdp | npt2.mdp |
| --- | --- | --- |
| `nsteps` | `1000000`（合计 2000 ps） | `1000000`（合计 2000 ps） |
| `define` | `-DPOSRES` 一行已注释，位置限制关闭 | 同 npt1.mdp |
| `nstxout` 等 | `1000` | `1000` |
| `ref_t` | `300 300` | `370 370` |

`npt2.mdp` 与 `npt1.mdp` 的唯一差别是 `ref_t = 370 370`。

## 结果核对

### 体系组成

| 组分 | 数量 | 原子数 |
| --- | --- | --- |
| 蛋白 | 1 | 1960 |
| SPC/E 水 | 10636 | 31908 |
| Cl⁻ | 8 | 8 |
| 合计 | — | 33876 |

蛋白的 1960 个原子为 1001 个重原子补氢后所得，体系总电荷为 0.000。NPT 模拟后的盒子为 6.967 × 6.967 × 6.967 nm。

### 最小化收敛

| 项目 | 数值 |
| --- | --- |
| 收敛信息 | Steepest Descents converged to Fmax < 1000 in 726 steps |
| Potential Energy | −5.8456×10⁵ kJ/mol |
| Maximum force | 934.8 kJ/mol/nm |
| 判据 | Maximum force < 1000 kJ/mol/nm |

最大力 934.8 kJ/mol/nm 低于判据 1000 kJ/mol/nm，收敛成立。

### 平衡平均值

| 阶段 | 温度 | 蛋白组温度 | 非蛋白组温度 | 压力 |
| --- | --- | --- | --- | --- |
| NVT | 293.3 K | 293.8 K | 293.2 K | −1.03×10³ bar |
| NPT | 300.8 K | 301.2 K | 300.7 K | 10.3 bar |

NVT 阶段未做压力耦合，其压力值不具物理意义。NPT 阶段压力为 10.3 bar，参考值为 1 bar。

## 回转半径

均方回转半径（radius of gyration）的定义为

$$R_g=\sqrt{\frac{\sum_i m_i\left|\mathbf r_i-\mathbf r_{\rm com}\right|^2}{\sum_i m_i}}$$

其中 $\mathbf r_{\rm com}$ 为所选组的质心，$m_i$ 为原子质量。该量度量一组原子相对其质心的空间展布，数值越小表示构象越紧凑。

### gyrate.xvg 文件结构

文件共 38 行。前 27 行是以 `#` 和 `@` 开头的注释行：`#` 为普通说明，`@` 为 Grace/xmgrace 绘图指令，其中 `@ s0 legend "Rg"` 与 `@ s1`~`@ s3` 分别描述各列名称。第 28 行起为数据，共 11 行。

数据共 5 列：

| 列 | 内容 | 单位 |
| --- | --- | --- |
| 1 | 时间 | ps |
| 2 | Rg 总量 | nm |
| 3 | 绕 X 轴的 Rg 分量 | nm |
| 4 | 绕 Y 轴的 Rg 分量 | nm |
| 5 | 绕 Z 轴的 Rg 分量 | nm |

三个分量满足 $R_g^2=(R_{gX}^2+R_{gY}^2+R_{gZ}^2)/2$，其中 $R_{gX}$ 为原子到 X 轴的垂直距离的均方根，而非沿 X 方向的投影。作业要求的「均方回转半径」对应第 2 列，因此画图只需第 1 列作 X、第 2 列作 Y。

### 本次结果

`gyrate.xvg` 的时间范围为 0~2 ps，共 11 帧，间隔 0.2 ps；Rg 值在 1.40407 ~ 1.40801 nm 之间。蛋白组的 Rg 为 1.40 nm 量级，与溶菌酶的实验值一致，可作为流程正确性的校验。

曲线近似为水平直线的原因：`npt.mdp` 中 `define = -DPOSRES` 生效，位置限制（position restraints）将蛋白重原子约束在 NVT 的参考坐标附近，蛋白构象在 2 ps 内的变化极小，故 Rg 的变化幅度仅约 0.004 nm。关闭位置限制（如 `npt1.mdp`）或延长模拟时间之后，Rg 才会体现构象涨落。

## OriginLab 画图

1. 选择 `File > Import > ASCII`，或使用导入向导
2. 文件前 27 行为注释头，需设置跳过 27 行；也可指定分隔符为空格或 Tab，由程序自动识别
3. 第 1 列设为 X，第 2 列设为 Y，绘制折线图
4. 第 3~5 列不使用

## 已知问题

- `gmx energy` 是纯后处理命令，只读取已由 `mdrun` 生成的 `.edr` 能量文件并导出为文本，不参与任何模拟计算，也不修改 `em.gro`、`em.tpr`、`em.edr`。因此跳过该步对后续 NVT、NPT、gyrate 的结果没有影响，但会失去对能量最小化收敛情况的直接观察，该收敛性也可从 `em.log` 中直接读取
- `gmx energy` 的编号随体系与运行类型变化，应以程序打印的菜单名称选择，不宜固定记忆编号
- grompp 默认将实际生效的参数回写到当前目录的 `mdout.mdp`
