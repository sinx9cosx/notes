---
tags:
  - research
  - 后处理
Category:
  - 笔记
---
作图对象
TBR-S9-NTO
DHR-S9-NTO

Multiwfn处理：
先用 NTO 分析生成 NTO 轨道文件，再载入该文件批量导出 cube 文件。

启动Multiwfn，将NTO含有基函数信息的 `.fchk` 文件直接拖入 Multiwfn 的命令行窗口（或手动输入完整路径）。Multiwfn 载入后会显示体系的基本信息，确认无误后继续。


在 Multiwfn 主功能菜单提示符下，输入18
程序会显示电子激发分析功能的子菜单列表，输入6
此时 Multiwfn 会要求你载入含有电子激发信息的文件。


程序提示输入 Gaussian 输出文件的路径，输入你的 TD-DFT 输出文件（`.log` 或 `.out`）的完整路径，例如：

```
examples\NTO\uracil.out
```

回车后，Multiwfn 会读取该文件中所有激发态的组态系数信息，并列出可分析的激发态编号及对应的激发能、振子强度。

### 第 4 步：选择 NTO 生成功能

在电子激发分析子菜单中，输入：

```
6
```

回车。这个选项对应“Generate natural transition orbitals (NTOs)”功能。Multiwfn 会提示你输入要分析的激发态编号。

### 第 5 步：输入激发态编号

输入你想做 NTO 分析的激发态序号，例如分析 S1 态就输入：

```
1
```

回车。Multiwfn 会立即进行 NTO 变换，并在控制台输出该激发态的前几对 NTO 的本征值（eigenvalue）。本征值最大的那一对 NTO（占据轨道与空轨道之间的跃迁）即代表该激发态的主要跃迁特征。如果最大本征值接近 1（如 0.95 以上），说明该激发态可以用这一对 NTO 很好地描述。

### 第 6 步：导出 NTO 轨道文件

程序询问是否将 NTO 导出为文件，会给出以下选项：

```
1 Output NTO orbitals to .molden file
2 Output NTO orbitals to .fch file
```

选择 **`2`**（输出为 `.fch` 文件），然后输入输出路径和文件名，例如：

```
C:\NTO_S1.fch
```

回车后，Multiwfn 会生成一个包含该激发态所有 NTO 轨道的新 `.fch` 文件。这个文件就是后续导出 cube 文件的输入来源。

> **批量分析多个激发态**：如果需要对多个激发态做 NTO 分析，可以重复第 4–6 步，每次输入不同的激发态编号并输出到不同的 `.fch` 文件。也可以使用 Multiwfn 的批处理脚本（`examples\scripts\` 目录下提供了 NTO 批量生成脚本）一次性完成所有激发态的 NTO 分析。

---

## 阶段二：批量导出 NTO 轨道的 cube 文件（主功能 200 → 子功能 3）

### 第 7 步：重新启动 Multiwfn 并载入 NTO 文件

**完全关闭** 之前的 Multiwfn 窗口（不要用同一个窗口继续操作），重新启动 Multiwfn。将上一步生成的 NTO `.fch` 文件（如 `NTO_S1.fch`）拖入 Multiwfn 命令行窗口。

载入后，Multiwfn 会显示该文件中的轨道信息。此时轨道能量字段对应的是 NTO 的本征值（eigenvalue），而非原始的 Kohn-Sham 轨道能量。

### 第 8 步：进入 Other functions part 2

在主功能菜单提示符下，输入：

```
200
```

回车。这是“Other functions (part 2)”主功能。

### 第 9 步：选择批量生成 cube 的子功能

在子菜单中，输入：

```
3
```

回车。该子功能的名称为“Generate cube file for multiple orbital wavefunctions”，即批量导出多个轨道波函数的 cube 文件。

### 第 10 步：指定要导出的轨道范围

程序会提示你输入轨道序号范围。NTO 分析生成的 `.fch` 文件中，轨道按本征值从大到小排列：前面的轨道是占据 NTO，后面的是空 NTO。例如，如果你只需要导出本征值最大的那一对 NTO（即占据 NTO #1 和空 NTO #1），可以输入：

```
1, N
```

其中 `N` 是该文件中占据 NTO 的总数加 1（即第一个空 NTO 的序号）。具体数值可以从第 7 步载入文件时 Multiwfn 显示的轨道列表中查看。

如果只想导出前几对 NTO，也可以输入具体的轨道序号，如 `1-4`。

### 第 11 步：选择格点质量

程序会列出格点质量选项，通常为：

```
1 Low quality (fast)
2 Medium quality
3 High quality
4 Ultra-high quality
```

选择 **`3`**（High quality），这是期刊发表推荐的质量级别，生成的 cube 文件格点足够精细，等值面平滑无锯齿。如果体系非常大（原子数超过 100），生成时间可能较长，可退而选择 `2`。如需更高精度，可选择 `4`，但计算时间会显著增加。

### 第 12 步：确认输出并等待完成

程序会询问是否将每个轨道输出为单独的 cube 文件。确认后（通常直接回车或选择默认选项），Multiwfn 开始逐个计算每个轨道的波函数格点数据并输出 cube 文件。文件命名格式为 `orb000001.cub`、`orb000002.cub` 等，序号与轨道序号对应。

计算完成后，当前工作目录下会生成一组 `.cub` 文件。将这些文件拷贝到本地电脑，供 VMD 加载使用。

> **关于格点质量**：Multiwfn 的 High quality 模式对应约 120×120×120 的格点密度，步长约 0.1–0.15 Å，足以满足期刊插图的分辨率要求。如果等值面边缘出现明显的阶梯状锯齿，可以尝试 Ultra-high quality 模式。

---

## 阶段三：在 VMD 中加载并渲染（简要）

cube 文件生成后，后续步骤简要概括如下：

1. 打开 VMD，依次拖入 NTO 的 cube 文件（占据 NTO 和空 NTO 各一个）。
2. 将背景设为白色，关闭坐标轴。
3. 为分子骨架创建一个 CPK 表示，调小 Sphere Scale。
4. 为每个 cube 文件创建一个 Isosurface 表示：Isovalue 设为 `0.03`（正值）显示正相位，再为同一文件创建第二个表示 Isovalue 设为 `-0.03` 显示负相位，分别使用不同颜色（如红色和蓝色）区分。
5. 调整好视角后，选择 Tachyon 渲染器，设置高分辨率（如 `-res 3000 3000`），点击 Start Rendering 输出高质量图像。

如需更详细的 VMD 渲染参数设置和 Tachyon 渲染命令，可以进一步说明。