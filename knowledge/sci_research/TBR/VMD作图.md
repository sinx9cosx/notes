---
tags:
  - research
  - 后处理
Category:
  - 笔记
---
# 作图对象

TBR-S9-NTO
DHR-S9-NTO

# Multiwfn处理

## 生成NTO文件

启动Multiwfn，将NTO含有基函数信息的 `.fchk` 文件直接拖入 Multiwfn 的命令行窗口（或手动输入完整路径）。Multiwfn 载入后会显示体系的基本信息，确认无误后继续。

在 Multiwfn 主功能菜单提示符下，输入18
程序会显示电子激发分析功能的子菜单列表，输入6
此时 Multiwfn 会要求你载入含有电子激发信息的文件（例如s9-td.log）。

输入你想做 NTO 分析的激发态序号，例如分析 S1 态就输入1
Multiwfn 会立即进行 NTO 变换，并在控制台输出该激发态的前几对 NTO 的本征值。

程序询问是否将 NTO 导出为文件，
选择 2（输出为 `.fch` 文件），然后输入输出路径和文件名

回车后，Multiwfn 会生成一个包含该激发态所有 NTO 轨道的新 `.fch` 文件。这个文件就是后续导出 cube 文件的输入来源。

## 生成cube文件

完全关闭之前的 Multiwfn 窗口，重新启动 Multiwfn。将上一步生成的 NTO `.fch` 文件拖入 Multiwfn 命令行窗口。


在主功能菜单提示符下，输入200

在子菜单中，输入3
该子功能的名称为“Generate cube file for multiple orbital wavefunctions”，即批量导出多个轨道波函数的 cube 文件。
程序会提示你输入轨道序号范围。

程序会列出格点质量选项
选择 3（High quality），这是期刊发表推荐的质量级别，生成的 cube 文件格点足够精细，等值面平滑无锯齿。

程序会询问是否将每个轨道输出为单独的 cube 文件。确认后Multiwfn 开始逐个计算每个轨道的波函数格点数据并输出 cube 文件。文件命名格式为 `orb000001.cub`、`orb000002.cub` 等，序号与轨道序号对应。

计算完成后，当前工作目录下会生成一组 `.cub` 文件。

# VMD参数设置

## 分子骨架

drawing method:CPK

coloring method: element
C:tan
H:silver

material:AOEdgy

sphere scale:0.7
sphere resolution:37
bond radius:0.4
bond resolution:12

## 等值面

coloring method:colorID
+:22
-:32

material:AOShiny
ambient:0.30
diffuse:0.85
specular:0.30
shininess:0.65
opacity:0.60

isovalue:$\pm$ 0.03
