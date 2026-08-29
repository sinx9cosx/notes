---
title: Multiwfn命令行操作完整教程
tags:
  - 计算化学
  - research
  - 后处理
Category:
  - 讲义
---

# Multiwfn命令行操作完整教程

> [!info] 本教程是什么
> 本教程是 [[Multiwfn手册5.2-5.5]] 的实操展开版，把手册 5.2–5.5 节的每个技巧写成可直接照抄运行的完整命令，并参考卢天博文（见文末参考来源）补充了批量运行的完整示例。所有例子都不跳步骤、不简写，复制即可运行。

> [!warning] 版本警告
> 本教程中的菜单序号交叉核实自 Multiwfn 3.8 dev 时代的官方材料（卢天博文），并已在主人本机 Multiwfn 2026.7.15 上实测验证：主功能编号（0/5/6/7/9/12/13/18/100）与教程涉及的关键子菜单序号（格点函数 1/5/9/12、后处理菜单 0/2/5、13→11→5→0、9→1、9→8、7→5→1、6→3、18→1、100→2 及其 2/10）当前仍然有效。**但实测也发现若干处旧版材料与 2026.7.15 的差异**（输出行格式、新增提问等），各涉及小节内有单独提醒，运行前仍建议以屏幕菜单为准。

## 第 1 节：运行环境准备

### 1.1 三种命令行环境

| 项目 | cmd | PowerShell | Git Bash |
|---|---|---|---|
| 窗口标题 | 命令提示符 | Windows PowerShell（或终端） | MINGW64 / Git Bash |
| 提示符 | `C:\Users\用户名>` | `PS C:\Users\用户名>` | `用户名@计算机 MINGW64 ~` |
| 打开方式 | Win+R 输入 `cmd` 回车 | Win+R 输入 `powershell` 回车，或右键开始菜单选"终端" | 开始菜单搜 Git Bash，或在文件夹空白处右键选 "Git Bash Here" |
| 判断方法 | 提示符以 `>` 结尾 | 提示符以 `PS` 开头 | 标题栏含 MINGW64，提示符以 `$` 结尾 |

一句话原则：本教程 `bash 代码块` 只能在 Git Bash 里跑；`batch 代码块` 存成 .bat 双击或在 cmd 里运行；PowerShell 有专属写法（见 2.4 节）。

另外注意：heredoc、`for ((...))`、`$(...)`、`${inf//...}` 都是 bash 专属语法，写进 cmd 或 PowerShell 会报错；反过来 batch 的 `%%i` 也不能写进 bash 脚本。

### 1.2 把 Multiwfn 加入 PATH（Windows 10/11 完整步骤）

1. 找到 Multiwfn 安装目录：该目录里应同时有 `Multiwfn.exe` 和 `settings.ini`。
2. 按 Win+R，输入 `sysdm.cpl`，回车。
3. 在"系统属性"窗口点"高级"选项卡，再点"环境变量"。
4. 在"用户变量"区域选中 `Path`，点"编辑"。
5. 点"新建"，填入 Multiwfn 安装目录（即 Multiwfn.exe 所在目录），点"确定"。
6. 回到"环境变量"窗口，再点"新建"，变量名填 `Multiwfnpath`，变量值填 settings.ini 所在目录，点"确定"。
7. 关闭所有打开的窗口。
8. **重新打开**命令行窗口（已打开的窗口不会加载新环境变量）。
9. 在任意目录输入 `Multiwfn` 回车，看到版本信息界面即配置成功。

原理：
- `Path` 让系统能在任意目录找到 exe；
- `Multiwfnpath` 让程序找到配置文件 settings.ini（也可临时用 `-set 路径` 指定）。

> [!note] 关于线程数
> 主人的 settings.ini 已配置 nthreads=18，启动参数 `-nt` 可以省略。

### 1.3 工作目录

建议每个任务建一个独立目录（如 `F:\mwfn_demo`），把 .wfn/.fch 等波函数文件和指令文件都放进去，在该目录打开命令行窗口运行。原因是 Multiwfn 生成的 cub、out.txt 等产物全部落在**当前工作目录**，每个任务独立一个文件夹不容易互相覆盖。

### 1.4 启动参数表

命令行格式为 `Multiwfn [输入文件路径] [选项/参数]`，例如 `Multiwfn xxx.molden -nt 18 -silent`（选项放文件名前后均可，输入文件缺省时程序会提示手动输入路径）。

| 参数 | 含义 | 备注 |
|---|---|---|
| `-nt 18` | 指定并行线程数为 18 | settings.ini 已配 nthreads=18，可省略 |
| `-silent` | 不自动弹出图形窗口 | **批量运行必用**，否则每算一个体系就要手动关一次图形窗口 |
| `-set 路径` | 指定 settings.ini 的位置 | 临时覆盖默认配置 |
| `-uf 序号` | 调用用户自定义函数 | 高级用法，本教程不涉及 |

## 第 2 节：三种传指令方式

统一示例：对 xxx.molden 计算拉普拉斯键级（主功能 9 → 子项 8 → 确认 y），三种方式各写一遍。

### 2.1 指令文件重定向（最通用，三种环境都行）

指令文件 LBO.txt 的完整内容：

```txt
9
8
y
```

运行命令：

```bash
Multiwfn xxx.molden < LBO.txt > out.txt
```

讲解：
- 指令文件里每行 = 程序里按一次键；
- 空行 = 直接按一次回车；
- **指令文件里不能写注释**，任何多余字符都会被当成指令按下。

再给 ELF 指令文件 genELFcub.txt 的完整内容：

```txt
5
9
2
2
```

逐行含义：
- `5`：主功能 5，计算格点数据；
- `9`：选择 ELF；
- `2`：中等质量格点；
- `2`：导出为 cub 文件（默认文件名 ELF.cub）。

> [!warning] ELF 序号可能随版本变化
> `9` 是 Multiwfn 3.3.x 时代 ELF 在主功能 5 子菜单里的序号，已在主人本机 2026.7.15 实测确认 ELF 仍为 9（本流程实测可跑通并生成 ELF.cub）。以后版本若调整，运行前先交互式进入主功能 5，看屏幕上 ELF 是几号，不一致就把指令文件里这一行改掉。

### 2.2 echo -e 管道直传（仅 bash 系）

```bash
echo -e "9\n8\ny" | Multiwfn xxx.molden > out.txt
```

讲解：
- `\n` = 一次回车，所以引号里写 `9\n8\ny` 等价于依次输入 9、回车、8、回车、y；
- 最后一项 y 之后不用写 `\n`。

> [!warning] 只能在 Git Bash 用
> cmd 的 echo 不认识 `\n`，会把反斜杠和 n 原样输出，此写法只能在 Git Bash 使用。

### 2.3 heredoc（仅 bash 系）

直接运行版：

```bash
Multiwfn xxx.molden << EOF > out.txt
9
8
y
EOF
```

存成脚本运行版，完整 sh 文件内容：

```bash
#!/bin/bash
Multiwfn xxx.molden << EOF > out.txt
9
8
y
EOF
```

运行方式：

```bash
chmod +x foo.sh
./foo.sh
```

或者 `bash foo.sh` 也行。EOF 只是约定俗成的标记名，可以换成任意标记（如 DONE），但首尾两处必须完全一致。

### 2.4 PowerShell 等价写法

> [!note] 说明
> 以下为 PowerShell 的标准等价写法。PowerShell 把文本传给 Fortran 程序偶有编码/换行问题，遇到怪现象时用 `cmd /c` 包一层最稳。

指令文件方式（PowerShell 不支持 `<` 重定向）：

```powershell
Get-Content LBO.txt | Multiwfn xxx.molden > out.txt
```

兜底写法（借 cmd 完成重定向）：

```powershell
cmd /c "Multiwfn xxx.molden < LBO.txt > out.txt"
```

echo 等价写法（`` `n `` 是 PowerShell 的换行转义）：

```powershell
"9`n8`ny" | Multiwfn xxx.molden > out.txt
```

heredoc 等价写法（here-string）：

```powershell
@"
9
8
y
"@ | Multiwfn xxx.molden > out.txt
```

### 2.5 三种方式对比表

| 方式 | 适用环境 | 优点 | 缺点 | 推荐场景 |
|---|---|---|---|---|
| 指令文件重定向 | 三种环境全支持 | 最通用，文件可复用可存档 | 要维护一个额外文件 | cmd 用户首选；长期重复的任务 |
| echo -e 管道 | 仅 bash 系 | 单行敲完，适合临时任务 | 指令一多引号里难读 | 随手单次计算 |
| heredoc / here-string | bash 系 / PowerShell | 指令直接写在脚本里，最直观 | 仅限各自 shell | Git Bash 用户；批量循环内嵌指令 |

结论：cmd 用户用指令文件；Git Bash 用户自由选择；批量循环必须用 heredoc 或指令文件。

## 第 3 节：输出处理

以下均以 LBO 任务为例，每条都是完整可运行的命令。

覆盖保存（`>` 会先清空再写入）：

```bash
Multiwfn xxx.molden < LBO.txt > out.txt
```

追加保存（`>>` 接着文件末尾写；批量循环里提取多行数据必须用 `>>`，否则每轮覆盖只剩最后一行）：

```bash
Multiwfn xxx.molden < LBO.txt >> out.txt
```

边显示边存（仅 Git Bash）：

```bash
Multiwfn xxx.molden < LBO.txt | tee out.txt
```

> [!warning] cmd 和 PowerShell 没有 tee 命令
> cmd 无等价命令；PowerShell 可用 `| Tee-Object out.txt` 代替。

丢弃输出：

Git Bash：

```bash
Multiwfn xxx.molden < LBO.txt > /dev/null
```

cmd：

```batch
Multiwfn xxx.molden < LBO.txt > NUL
```

丢弃错误信息：

Git Bash：

```bash
Multiwfn xxx.molden < LBO.txt 2> /dev/null
```

cmd：

```batch
Multiwfn xxx.molden < LBO.txt 2> NUL
```

输出和错误一起存：

Git Bash：

```bash
Multiwfn xxx.molden < LBO.txt &> out.txt
```

cmd（cmd 不支持 `&>`，要写成 `> file 2>&1`）：

```batch
Multiwfn xxx.molden < LBO.txt > out.txt 2>&1
```

## 第 4 节：forrtl: severe (24) 错误

现象：指令全部执行完后程序被强制结束，屏幕末尾出现类似这样的报错：

```txt
forrtl: severe (24): end-of-file during read, unit -4, file CONIN$
Image              PC                Routine            Line        Source
Multiwfn.exe       00007FF6C2B8A4A0  Unknown               Unknown  Unknown
Multiwfn.exe       00007FF6C2B8C8F0  Unknown               Unknown  Unknown
Multiwfn.exe       00007FF6C2B9A1E0  Unknown               Unknown  Unknown
KERNEL32.DLL       00007FFA5E3F7374  Unknown               Unknown  Unknown
```

原因：指令执行完没有优雅退出、程序被强制关闭，程序还在等待输入时输入流突然结束，Intel Fortran 运行时把"输入突然没了"报成 end-of-file（文件意外结束）错误。**结果文件已经正常生成，这个报错无害**。

消除方法一（推荐）：在指令末尾追加 `0`（返回主菜单）和 `q`（退出），让程序优雅退出。

对比，会报错的写法：

```bash
echo -e "9\n8\ny" | Multiwfn xxx.molden > out.txt
```

干净退出的写法：

```bash
echo -e "9\n8\ny\n0\nq" | Multiwfn xxx.molden > out.txt
```

注意：如果指令结束时停在二级菜单，要先按一次 `0` 回到上一级菜单，再按一次 `0` 回到主菜单，最后 `q` 退出。例如第 5.4 节 7→5→1 流程的收尾是 `n`、`0`、`0`、`q` 共四步：`n` 回答当前二级菜单的提问；第一个 `0` 从二级菜单返回上一级（布居分析菜单）；第二个 `0` 从布居分析菜单返回主菜单；`q` 在主菜单退出。

消除方法二：把错误信息丢弃。

Git Bash：

```bash
Multiwfn xxx.molden < LBO.txt > out.txt 2> /dev/null
```

cmd：

```batch
Multiwfn xxx.molden < LBO.txt > out.txt 2> NUL
```

## 第 5 节：数据提取通用套路（grep + awk + cut）

套路图：

```txt
程序输出 → out.txt → grep 定位行 → awk/cut 切出数值 → 写进文件或变量
```

### 5.1 "Estimated density" 提取与 $(...) 变量捕获

完整脚本（直接照抄）：

```bash
#!/bin/bash
echo "Running:" $1
Multiwfn $1 << EOF > out.txt
12
0
-1
-1
q
EOF
t1=$(grep "Estimated density" out.txt | awk -F : '{print $2}' | awk '{print $1}')
echo "M/Vm:" $t1 "g/cm^3"
rm -f out.txt
```

逐行讲解：
- `echo "Running:" $1`：打印正在处理的文件名（`$1` 是脚本的第一个参数）；
- `Multiwfn $1 << EOF > out.txt`：对参数指定的文件运行 Multiwfn，后续直到 EOF 之间的行是喂给程序的指令，输出重定向到 out.txt；
- `12`：主功能 12，定量分子表面分析；
- `0`：开始计算；
- `-1`、`-1`：逐级返回主菜单；
- `q`：退出程序；
- `t1=$(...)`：把命令的输出捕获进变量 t1；
- 被提取的原行是 `Estimated density according to mass and volume (M/V):    1.8045 g/cm^3`；
- `awk -F : '{print $2}'`：按冒号切分，取第 2 段（即 `1.8045 g/cm^3`）；
- 再 `awk '{print $1}'`：按空格切分，取第 1 段，得到 `1.8045`；
- `echo "M/Vm:" $t1 "g/cm^3"`：打印提取结果；
- `rm -f out.txt`：删除临时输出文件。

### 5.2 awk 传参数做线性运算

```bash
echo "$t1 $t2" | awk '{ print "Predicted density: " a*$1+b*$2+g " g/cm^3"}' a=0.9183 b=0.0028 g=0.0443
```

讲解：
- `a=0.9183 b=0.0028 g=0.0443` 是传给 awk 的命名参数，对应晶体密度预测公式 ρ=a·(M/Vm)+b·νσ²tot+g 的拟合参数；
- `$1`、`$2` 对应 echo 出来的两个值（t1 和 t2）；
- 输出示例：`Predicted density: 1.77441 g/cm^3`。

不需要传参时也可以把系数直接写进算式：

```bash
awk '{ print "Predicted density: " 0.9183*$1+0.0028*$2+0.0443 " g/cm^3"}'
```

### 5.3 HOMO-LUMO gap 提取（方案 A：主功能 0 直接打印 / 方案 B：主功能 6 → 3 自算）

#### 方案 A（推荐）：主功能 0 直接打印 gap 行（适用 .fch/.molden 等含轨道信息的文件）

单个体系完整版：

```bash
Multiwfn H2O.fch -silent << EOF > out.txt
0
q
EOF
grep "HOMO-LUMO gap" out.txt | awk '{print $5}'
```

逐行讲解：
- `0`：主功能 0，显示分子结构和轨道信息；
- `q`：退出程序。

被提取的原行形如（2026.7.15 实测，H2O.fch）：

```txt
       HOMO-LUMO gap:    0.357308 a.u.    9.722836 eV    938.111318 kJ/mol
```

讲解：
- 按空格切分：`$3`=gap 的 a.u. 值，`$5`=eV 值，`$7`=kJ/mol 值，`awk '{print $5}'` 提取 eV（实测 9.722836）；
- 该行只在输入文件**含轨道信息**时打印：.fch/.molden 有，.wfn 不打印（.wfn 请用方案 B）；
- 开壳层体系会打印 alpha/beta 两行（实测乙醇三重态输出形如 `HOMO-LUMO gap of alpha orbitals:    0.097328 a.u.    2.648436 eV` 和 `HOMO-LUMO gap of beta orbitals: ...`），两行都会被 grep 抓到且 `$5` 不再是数值；只算闭壳层体系时把 grep 串改成 `"HOMO-LUMO gap: "`（冒号后带空格，开壳层行是 `gap of ...` 不会被匹配，实测可过滤）。

批量版完整脚本（把当前目录下所有闭壳层 .fch 的 gap 写进 gap.txt；变量捕获、`>>` 追加、删除临时文件等讲解要点与下方方案 B 批量版相同）：

```bash
#!/bin/bash
rm -f gap.txt
for inf in *.fch
do
echo Processing $inf ...
Multiwfn $inf -silent << EOF > out.txt
0
q
EOF
gapthis=$(grep "HOMO-LUMO gap" out.txt | awk '{print $5}')
echo "$inf: $gapthis eV" >> gap.txt
done
rm -f out.txt
echo "Done! See gap.txt"
```

#### 方案 B（.wfn 等不打印 gap 行的文件）：主功能 6 → 3 列轨道能量自算

单个体系完整版：

```bash
Multiwfn H2O.fch -silent << EOF > out.txt
6
3
-1
q
EOF
awk '/^ Orb:/ {if ($7>0) {HOMO=$4} else if (LUMO=="") {LUMO=$4}} END {printf "%.4f eV\n", (LUMO-HOMO)*27.2114}' out.txt
```

逐行讲解：
- `6`：主功能 6，查看/修改波函数；
- `3`：列出全部轨道（2026.7.15 主功能 6 的子项 3 = List all orbitals）；
- `-1`：返回主菜单；
- `q`：退出。

> [!warning] 主功能 6 里返回主菜单要按 -1，不是 0
> 2026.7.15 主功能 6 的菜单里 `-1` 才是 Return；`0` 是 "Save the present wavefunction to new.wfn file in current folder"（把当前波函数存成 new.wfn）。按旧版习惯按 0 会生成 new.wfn 且回不到主菜单。

被提取的原行形如（2026.7.15 实测，H2O.fch）：

```txt
 Orb:     5 Ene(au/eV):    -0.291961      -7.9447 Occ: 2.000000 Type:A+B
 Orb:     6 Ene(au/eV):     0.065347       1.7782 Occ: 0.000000 Type:A+B
```

讲解：
- 每行按空格切分：`$2`=轨道序号，`$4`=能量(a.u.)，`$5`=能量(eV)，`$7`=占据数；
- 列表按能量从低到高排列，最后一个占据数 > 0 的轨道是 HOMO，第一个占据数 = 0 的是 LUMO；
- awk 取两个能量的 a.u. 值相减再乘 27.2114 换成 eV，输出 `9.7229 eV`。

> [!note] 为什么还提供方案 B
> 方案 A 依赖主功能 0 的打印行为：.wfn 不打印 gap 行；开壳层体系打印 alpha/beta 两行（`awk '{print $5}'` 会取错列）。方案 B 的 6 → 3 轨道列表法不依赖该打印行为，还能同时拿到 HOMO/LUMO 能量与占据数，通用性更强。

批量版完整脚本（把当前目录下所有闭壳层 .fch 的 gap 写进 gap.txt）：

```bash
#!/bin/bash
rm -f gap.txt
for inf in *.fch
do
echo Processing $inf ...
Multiwfn $inf -silent << EOF > out.txt
6
3
-1
q
EOF
gapthis=$(awk '/^ Orb:/ {if ($7>0) {HOMO=$4} else if (LUMO=="") {LUMO=$4}} END {printf "%.4f", (LUMO-HOMO)*27.2114}' out.txt)
echo "$inf: $gapthis eV" >> gap.txt
done
rm -f out.txt
echo "Done! See gap.txt"
```

讲解：
- `$(...)` 把提取值捕获进变量；
- 写入 gap.txt 用 `>>` 追加，所以每轮循环不会互相覆盖；
- 循环结束后删掉临时文件 out.txt；
- awk 里 `/^ Orb:/` 的行首锚定不能省：输出里还有 `GTF: ... Orb: ...` 这类信息行，不加锚定会把它们误当成轨道行。

> [!warning] 开壳层体系不适用
> 开壳层（unrestricted）体系的轨道列表格式不同：行首没有 `Orb:` 前缀，且 Alpha 轨道全部排在 Beta 轨道之前（实测乙醇三重态输出形如 `    14          E(au/eV):    -0.01014      -0.2759 Occ: 1.000000 Typ: A`）。本脚本对开壳层文件会输出空值或错误值，提取前先 `cat out.txt` 看真实格式再改 awk。

> [!note] 关于卢天原版 getgap.sh
> 卢天原版脚本还用 bc 统计平均值/最小值，但 cmder 里没有 bc，本教程给出的是纯 awk 版。原脚本见博文 http://sobereva.com/612。

### 5.4 Mulliken 布居 / 原子自旋布居提取（主功能 7）

> [!warning] 输入文件要含基函数信息
> Mulliken 分析需要基函数，输入必须是 .fch/.molden/.molden.input 这类带基函数信息的文件；.wfn 不含基函数，跑 7 → 5 会直接崩溃（本机 2026.7.15 实测 forrtl severe (157) access violation）。

闭壳层完整版（H2O.fch，提取 O 的 Population）：

```bash
Multiwfn H2O.fch << EOF > out.txt
7
5
1
n
0
0
q
EOF
grep "Population of atoms:" -A 100 out.txt | grep "1(O )" | awk '{print $5}'
```

逐行讲解：
- `7`：主功能 7，布居分析；
- `5`：选择 Mulliken 方法；
- `1`：输出布居结果；
- `n`：不导出 chg 文件（回答 "If outputting atom coordinates with charges to H2O.chg in current folder? (y/n)"）；
- `0`、`0`：逐级返回主菜单；
- `q`：退出。

2026.7.15 闭壳层输出原表形如：

```txt
Atom     1(O )    Population:  8.60985977    Net charge: -0.60985977
Atom     2(H )    Population:  0.69507012    Net charge:  0.30492988
```

讲解：
- 新版闭壳层输出只有 Population 和 Net charge 两列，3.8 时代的 Alpha pop./Beta pop./Spin pop./Atomic charge 四列表不再打印；
- 按空格切分：`$2`、`$3` 合起来是原子标签（元素名占两个字符宽，O 后面带一个空格，标签被切成了 `1(O` 和 `)` 两段），`$5`=Population、`$8`=Net charge；
- 提取 Net charge 把 `awk '{print $5}'` 改成 `awk '{print $8}'` 即可。

开壳层完整版（乙醇三重态，提取 4 号氢的自旋布居）：

```bash
Multiwfn ethanol_triplet.fch << EOF > out.txt
7
5
1
n
0
0
q
EOF
grep "Population of atoms:" -A 100 out.txt | grep "4(H )" | awk '{print $5}'
```

2026.7.15 开壳层输出原表形如：

```txt
     Atom      Alpha pop.   Beta pop.    Spin pop.     Atomic charge
     4(H )      0.46846      0.43410      0.03437         0.09744
```

讲解：
- 开壳层保留四列格式：`$3`=Alpha pop.、`$4`=Beta pop.、`$5`=Spin pop.、`$6`=Atomic charge，提取自旋布居用 `awk '{print $5}'`（实测 4(H ) 得 0.03437）；
- 闭壳层不打印 Spin pop. 列，对闭壳层体系提取自旋布居会得到空值。

两条命令共用的讲解：
- `-A 100` 锚定 "Population of atoms:" 之后的 100 行区域，防止文件别处也出现 `4(H )` 造成误抓；
- 列位置随版本变化，若提取出空值，先 `cat out.txt` 查看原始输出行再调整列号。

批量版完整脚本（循环当前目录所有 .fch，把每个体系 4 号氢原子的自旋布居追加写入 4.txt）：

```bash
#!/bin/bash
rm -f 4.txt
for inf in *.fch
do
echo Processing $inf ...
Multiwfn $inf << EOF > out.txt
7
5
1
n
0
0
q
EOF
spinthis=$(grep "Population of atoms:" -A 100 out.txt | grep "4(H )" | awk '{print $5}')
echo "$inf: $spinthis" >> 4.txt
done
rm -f out.txt
echo "Done! See 4.txt"
```

讲解：
- 批量提取自旋布居只对开壳层体系有意义：闭壳层输出没有 Spin pop. 列（提取到空值），且体系里必须真的有 4 号氢原子；
- 实测：ethanol_triplet.fch 得 0.03437，闭壳层的 H2O.fch 得空值。

### 5.5 Mayer 键级提取（主功能 9）

完整版（H2O.fch，提取 O1-H2 键级）：

```bash
Multiwfn H2O.fch << EOF > out.txt
9
1
n
0
q
EOF
grep "1(O )    2(H )" out.txt | awk '{print $NF}'
```

逐行讲解：
- `9`：主功能 9，键级分析；
- `1`：Mayer 键级；
- `n`：不导出键级矩阵（回答 "If outputting bond order matrix to bndmat.txt in current folder? (y/n)"）；
- `0`：返回主菜单；
- `q`：退出。

2026.7.15 输出原行示例：

```txt
 #    1:         1(O )    2(H )    0.89827717
```

讲解：
- 新版只有一列 Total 数值，3.8 时代的 Alpha/Beta/Total 三列不再打印；
- `awk '{print $NF}'` 直接取行尾最后一个字段，就是键级值（实测 0.89827717）；
- 键级绝对值小于 0.05 的原子对不会打印（表头上写着 "Bond orders with absolute value >= 0.050000"）。

> [!warning] 两个坑
> 一是 grep 串 `"1(O )    2(H )"` 里的**空格个数必须和输出行完全一致**（元素名占两个字符宽，`(O` 和 `)` 之间有一个空格），不放心可用 `grep -E "1\(O \) +2\(H \)"` 更稳；二是输出列格式随版本变化，**提取出空值时先 `cat out.txt` 看原始行**（用 `$NF` 取行尾值本身就比固定列号更抗版本变化）。

### 5.6（选学）拉普拉斯键级（主功能 9 的子项 8，导出 bndmat.txt）

完整版：

```bash
Multiwfn xxx.molden << EOF > out.txt
9
8
y
0
q
EOF
```

讲解：
- `9`：主功能 9，键级分析；
- `8`：拉普拉斯键级（Laplacian bond order）；
- `y`：确认导出 bndmat.txt；
- `0`：返回主菜单；
- `q`：退出。

运行结束后当前目录会多出 bndmat.txt。注意 8 是 3.8 dev 时代的序号，主人版本请以屏幕菜单为准。

> [!warning] 为什么 y 之后要多按一次 0
> 2026.7.15 实测：主功能 9 的菜单里没有 `q` 选项，`y` 确认导出后直接 `q` 会被当成菜单序号读入，触发 forrtl severe (59)（bndmat.txt 已正常生成，但报错吓人）。正确做法就是这里演示的"先 0 回菜单再 q"——即第 4 节的原则：指令结束时停在二级菜单，要先逐级 0 回主菜单再 q。

## 第 6 节：批量循环（ELF 计算，两种 shell 完整版）

### 6.1 Git Bash 版

存成 run_elf.sh，完整内容：

```bash
#!/bin/bash
for inf in *.wfn
do
echo Running $inf ...
Multiwfn $inf < genELFcub.txt > /dev/null
mv ELF.cub ${inf//.wfn}_ELF.cub
done
```

逐行讲解：
- `for inf in *.wfn`：通配目录下所有 wfn 文件，逐个赋给变量 inf；
- `Multiwfn $inf < genELFcub.txt > /dev/null`：用 2.1 节的指令文件静默运行；
- `${inf//.wfn}_ELF.cub`：把文件名里的 .wfn 替换掉、接上 `_ELF.cub`（如 Kanan.wfn 变成 Kanan_ELF.cub）。

> [!warning] 为什么必须改名
> Multiwfn 每次生成的 cub 都叫 ELF.cub，不改名的话每算完一个就被下一个覆盖，最后只剩最后一个分子的结果。

运行方式：

```bash
chmod +x run_elf.sh
./run_elf.sh
```

或者 `bash run_elf.sh`。

### 6.2 Windows batch 版

存成 run_elf.bat，完整内容：

```batch
for /f %%i in ('dir *.wfn /b') do (
Multiwfn %%i < genELFcub.txt > NUL
rename ELF.cub %%~ni_ELF.cub
)
```

逐行讲解：
- `for /f %%i in ('dir *.wfn /b')`：让 dir 列出所有 wfn 文件名，逐个交给循环变量；
- bat 文件里循环变量写 `%%i`（在 cmd 里手动敲才写 `%i`）；
- `%%~ni` 取文件名主体（不含扩展名）；
- `> NUL` 是 cmd 的丢弃输出写法。

运行方式：双击 .bat 文件，或在 cmd 里输入文件名。

### 6.3 两版对照表

| 项目 | Git Bash 版 | Windows batch 版 |
|---|---|---|
| 循环变量 | `$inf` | `%%i` |
| 丢弃输出 | `> /dev/null` | `> NUL` |
| 文件改名 | `mv ELF.cub ${inf//.wfn}_ELF.cub` | `rename ELF.cub %%~ni_ELF.cub` |
| 运行方式 | `bash run_elf.sh` | 双击 .bat 或在 cmd 输入文件名 |

## 第 7 节：批量计算多个激发态（动态生成指令文件）

完整脚本（直接照抄）：

```bash
#!/bin/bash
cat << EOF > calcall.txt
18
1
D-pi-A.out
EOF
for ((i=1;i<=3;i=i+1))
do
cat << EOF >> calcall.txt
$i
1
2
0
0
1
EOF
done
Multiwfn D-pi-A.fchk < calcall.txt | tee out.txt
rm -f calcall.txt result.txt
grep "Sr index" out.txt | nl >> result.txt; echo >> result.txt
grep "D index" out.txt | nl >> result.txt; echo >> result.txt
grep "RMSD of hole in" out.txt | nl >> result.txt; echo >> result.txt
grep "RMSD of electron in" out.txt | nl >> result.txt; echo >> result.txt
grep "H index" out.txt | nl >> result.txt; echo >> result.txt
grep "t index" out.txt | nl >> result.txt
echo "Finished!"
```

讲解：
- 第一段 heredoc 用 `>` **创建**指令文件头：`18`=电子激发分析主功能；`1`=空穴-电子分析；`D-pi-A.out`=读取组态系数的 Gaussian TD 输出文件名；
- 循环里的 heredoc 用 `>>` **追加**，`$i` 会被展开成 1、2、3；
- 每个激发态的六条指令：`$i`=激发态序号；`1`=分析空穴电子；`2`=中等质量格点；`0`=后处理菜单返回；`0`=返回主功能 18 的菜单；`1`=再进空穴-电子分析，以便处理下一个态；
- `nl` 给每行加行号（行号即激发态序号）；
- `;` 让两条命令写在同一行。

result.txt 输出示例（数值为示意，以实际输出为准）：

```txt
     1  Sr index:    1.2213 a.u.
     2  Sr index:    0.9812 a.u.
     3  Sr index:    1.1034 a.u.

     1  D index:    0.8891 A
     2  D index:    1.2045 A
     3  D index:    0.7762 A

     1  RMSD of hole in X,Y,Z:    1.8823 A
     2  RMSD of hole in X,Y,Z:    1.6654 A
     3  RMSD of hole in X,Y,Z:    2.0145 A

     1  RMSD of electron in X,Y,Z:    2.3312 A
     2  RMSD of electron in X,Y,Z:    2.1187 A
     3  RMSD of electron in X,Y,Z:    2.5501 A

     1  H index:    1.5532 A
     2  H index:    1.4012 A
     3  H index:    1.7105 A

     1  t index:    -1.4452 A
     2  t index:    -1.2214 A
     3  t index:    -1.6607 A
```

> [!tip] 要算 N 个激发态
> 把 `i<=3` 改成 `i<=N` 即可。

> [!warning] 版本提醒
> 本流程菜单序号核实自 3.8 dev 时代，主人版本 2026.7.15 运行前请先交互式进入主功能 18 确认序号。

> [!note] 关于 ./Multiwfn 与 PATH
> 卢天原文脚本里写的是 `./Multiwfn`（Linux 下运行当前目录里的程序）；主人已把 Multiwfn 加入 PATH，直接写 `Multiwfn` 即可。若未加入 PATH，就写完整路径（如 `D:\Multiwfn\Multiwfn.exe`）。

## 第 8 节：网格文件（cub）处理

### 8.1 生成密度 cub 和静电势 cub（含 -ESPrhoiso 加速）

指令文件 ESPiso.txt 完整内容：

```txt
5
1
2
2
0
5
12
1
2
```

运行：

```bash
Multiwfn 1.fch -ESPrhoiso 0.001 < ESPiso.txt
```

逐行含义：
- `5`：主功能 5，计算格点数据；
- `1`：电子密度；
- `2`：中等质量格点；
- `2`：导出为 cub（默认名 density.cub）；
- `0`：返回主菜单；
- `5`：再进主功能 5；
- `12`：静电势；
- `1`：**低质量**格点（ESP 计算贵且表面变化平滑，低一档足够）；
- `2`：导出（默认名 totesp.cub）。

`-ESPrhoiso 0.001` 讲解：只在 ρ=0.001 a.u. 等值面附近的格点上计算 ESP，跳过分子内部深处不关心的点，大幅加速表面静电势计算。

> [!tip] -ESPrhoiso 的适用场景
> 该参数一般与主功能 5 的静电势计算配合使用。

批量改名防覆盖（与第 6 节同原理），完整 batch 示例：

```batch
for /f %%i in ('dir *.fch /b') do (
Multiwfn %%i < ESPiso.txt > NUL
move /Y density.cub %%~ni_density.cub
move /Y totesp.cub %%~ni_totesp.cub
)
```

讲解：
- `move /Y` 强制覆盖不询问；
- 用 `%%~ni` 前缀保证每个分子的产物独立命名（否则 density.cub 和 totesp.cub 每次同名生成，批量跑互相覆盖）。

### 8.2 totesp.cub 乘 27.2114 转 eV（主功能 13→11→5，分两次运行）

先按 8.1 生成 a.u. 版的 totesp.cub，再**另起一次** Multiwfn 对 totesp.cub 做乘法。第二次的指令文件 totesp_eV.txt 完整内容：

```txt
13
11
5
27.2114
0
totesp.cub
-1
q
```

运行：

```bash
Multiwfn totesp.cub < totesp_eV.txt
```

逐行含义：
- `13`：主功能 13，格点数据处理；
- `11`：Grid data calculation（格点数据计算）；
- `5`：乘以一个数（Multiplied by a constant）；
- `27.2114`：Hartree→eV 换算系数（回答 "Input the value for the calculation"）；
- `0`：把内存中的新数据导出为 cub——乘完常数必须走这一步才真正保存（回答 "Input path of the new cube file"）；
- `totesp.cub`：导出文件名（写同名覆盖原文件，写新名字则另存）；
- `-1`：返回主菜单（格点数据菜单里没有 q 选项）；
- `q`：退出。

> [!warning] 为什么要分两次运行
> `r`（重新载入文件）只在**主菜单**有效，而 8.1 的 ESPiso.txt 结束时停在格点数据的后处理菜单（该菜单没有 r 选项）。把 `r` 和乘法指令直接拼到 ESPiso.txt 后面，`r` 会被当成菜单序号读入，触发 forrtl severe (59) 崩溃、乘法根本不执行（2026.7.15 实测）。所以必须分两次：第一次按 8.1 生成 totesp.cub，第二次重新启动 Multiwfn 载入 totesp.cub 做乘法。同理，第二次的收尾要先 `-1` 回主菜单再 `q`（第 4 节原则，格点数据菜单没有 q 选项）。

> [!warning] 两个提醒
> 一是不走"0 导出"这一步，乘法只在内存里、关掉程序就没了；二是想同时保留 a.u. 版和 eV 版，导出时换个文件名（如 totesp_eV.cub）。

第二次运行也可以写成 bash heredoc：

```bash
Multiwfn totesp.cub << EOF > out.txt
13
11
5
27.2114
0
totesp.cub
-1
q
EOF
```

### 8.3（选学）自旋密度 cub 批量生成（主功能 5 的子项 5）

指令文件 spindensity.txt 完整内容：

```txt
5
5
2
2
```

逐行含义：
- `5`：主功能 5，计算格点数据；
- `5`：自旋密度；
- `2`：中等质量格点；
- `2`：导出为 cub（默认名 spindensity.cub）。

> [!warning] 自旋密度序号可能随版本变化
> `5` 核实自 3.8 dev 时代的材料，已在主人本机 2026.7.15 实测确认自旋密度仍为 5（本流程实测可跑通并生成 spindensity.cub）。以后版本若调整，运行前先交互式进入主功能 5，看屏幕上自旋密度是几号，不一致就把指令文件里这一行改掉。

批量 bash 循环完整版（含改名防覆盖）：

```bash
#!/bin/bash
for inf in *.wfn
do
echo Running $inf ...
Multiwfn $inf < spindensity.txt > /dev/null
mv spindensity.cub ${inf//.wfn}_spindensity.cub
done
```

## 第 9 节：批量格式转换

### 9.1 主功能 100 → 2 格式转换

单个示例（导出 xyz）：

```bash
Multiwfn xxx.molden << EOF > /dev/null
100
2
2
tmp.xyz
0
q
EOF
```

逐行含义：
- `100`：其它功能（Other functions）；
- `2`：导出文件/产生输入文件；
- `2`：xyz 格式；
- `tmp.xyz`：输出文件名；
- `0`：返回主菜单；
- `q`：退出。

> [!warning] 100→2 子菜单格式序号以屏幕为准
> 子菜单里的具体格式序号（molden/fch 等）以屏幕菜单为准，本教程只核实了 2=xyz、10=Gaussian 输入文件 gjf。

批量版：把所有 Gaussian .out 转成 .gjf 的完整脚本（取自卢天博文 4.1 节原文，脚本内的注释已剥离，见下方逐行讲解）：

```bash
#!/bin/bash
icc=0
nfile=`ls *.out|wc -l`
for inf in *.out
do
((icc++))
echo Converting $inf to ${inf//out/gjf} ... \($icc of $nfile\)
Multiwfn $inf << EOF > /dev/null
100
2
10
${inf//out/gjf}
n
0
q
EOF
done
```

逐行讲解：
- `icc=0`：初始化累加变量，用于统计已处理文件数；
- `nfile=\`ls *.out|wc -l\``：ls 列出所有 out 文件，wc -l 统计行数，即 out 文件总数；
- `for inf in *.out`：循环当前目录下所有 out 文件；
- `((icc++))`：icc 加 1，表示正在处理第几个文件；
- `echo Converting $inf to ${inf//out/gjf} ... \($icc of $nfile\)`：打印进度（`\(`、`\)` 是原作者脚本的习惯写法，bash 的 echo 不加 `-e` 时反斜杠会原样显示为 `\(5 of 151\)`，不影响功能；若想去掉反斜杠，把 `\(`、`\)` 改成 `(`、`)` 即可）；`${inf//out/gjf}` 把文件名的扩展名从 out 改成 gjf；
- heredoc 内各行：`100`=主功能 100；`2`=导出文件和产生输入文件；`10`=产生 Gaussian 输入文件；`${inf//out/gjf}`=新产生的 gjf 文件名（heredoc 未加引号，变量会被 bash 展开）；`n`=回答 2026.7.15 新增的提问 "Do you also want to write current wavefunction as initial guess into the .gjf file? (y/n)"，选 n 表示不把当前波函数写入 gjf 初猜（想生成带初猜的 gjf 可改 y）；`0`=返回主菜单；`q`=优雅退出。

> [!warning] 新增提问只在输入文件含波函数时出现
> 实测：含波函数的 .fch 转 gjf 会问上面这句话，不答 n 就会 severe (59)；但只含几何的 Gaussian .out（如官方 examples 里的 DMNAO/NAOMO/极化率任务输出，载入时只有 "Geometry ... has been loaded from this file"、没有 "Loading orbitals..."）**不会**问这句话，此时脚本里的 `n` 行是多余输入，会导致 forrtl severe (59) 报错（gjf 文件本身已正常生成）。这类文件把 heredoc 里的 `n` 行删掉即可（100/2/10/文件名/0/q，本机实测 exit=0）。判断方法：看启动输出的载入信息里有没有 "Loading orbitals..."。

运行示例提示：

```txt
Converting B2H6.out to B2H6.gjf ... \(5 of 151\)
Converting Benzaldehyde.out to Benzaldehyde.gjf ... \(6 of 151\)
```

> [!note] 脚本来源
> 本脚本由 curl 抓取 http://sobereva.com/612 第 4.1 节原文核实，对应 Multiwfn 官方包里的 examples\scripts\outgjf.sh。

### 9.2 orca_2mkl 批量把 gbw 转 molden

```bash
#!/bin/bash
for inf in *.gbw
do
echo converting $inf ...
name=${inf//.gbw}
orca_2mkl $name -molden
done
```

讲解：
- `${inf//.gbw}` 去掉 .gbw 扩展名（orca_2mkl 接文件名主体）；
- 转换产物 xxx.molden.input 可直接交给 Multiwfn；
- settings.ini 里 `orca_2mklpath` 配好后，Multiwfn 甚至能直接读 gbw；本脚本用于"本机没有同版本 ORCA"的情形。

## 第 10 节：动画合成（ffmpeg 两遍法）

前置：用 VMD（或其它工具）把每一帧渲染成连续编号的 bmp 文件：00001.bmp、00002.bmp、00003.bmp……（VMD 的渲染操作不属于本教程范围，本教程只讲随后的 ffmpeg 合成两步，两步命令与帧文件名编号方式均完整给出）。

第一遍生成调色板：

```bash
ffmpeg -i 00027.bmp -vf palettegen palette.png
```

第二遍合并成 gif：

```bash
ffmpeg -r 5 -i %05d.bmp -i palette.png -lavfi paletteuse video.gif
```

参数讲解：
- `palettegen`：从某一帧提取代表色生成调色板（选中间帧 00027 效果较好）；
- `paletteuse`：按调色板逐帧合成；
- `-r 5`：每秒 5 帧；
- `%05d.bmp`：按 5 位零填充数字匹配文件名。

> [!warning] 为什么不直接合成
> 直接 `ffmpeg -i %05d.bmp video.gif` 也能合，但颜色只有 256 色且抖动严重，两遍法质量明显更好。

## 第 11 节：剪贴板与缓冲区（手册 5.4 / 5.5 改写）

### 11.1 复制命令行输出到剪贴板

Windows 11：
1. 按住 ALT 键；
2. 用鼠标左键在窗口中拖出矩形选框；
3. 按回车；
4. 已复制，可直接粘贴到任何位置。

旧版 Windows：右键窗口**标题栏** → "编辑" → "标记" → 拖选 → 回车复制。

Linux/Mac：终端里鼠标选中即可。

### 11.2 增大窗口缓冲区（记录更多输出）

症状：输出太长（如波函数修改模块导出大密度矩阵）只能看到末尾。

解决：
1. 右键窗口**标题栏** → "属性"；
2. 选"布局"选项卡；
3. 屏幕缓冲区大小"高度"从默认 300 改成 9999；
4. 点"确定"。

永久生效，无需每次设置；还不够就继续加大。Linux/Mac 终端在首选项里有同类"回滚行数"设置。

## 附录 A：菜单序号速查表

| 用途 | 菜单路径 | 版本状态 |
|---|---|---|
| 查看结构 / HOMO-LUMO gap | 0（含轨道信息文件，grep gap 行取第 5 列）；6 → 3（.wfn 等，自算 gap） | 2026.7.15 实测（见 5.3 节：0 的 gap 行 .wfn 不打印、开壳层打印 α/β 两行） |
| 计算格点数据（密度 1 / ELF 9 / 自旋密度 5 / 静电势 12） | 5 → 序号 → 格点质量 → 2 | ELF 的 9、自旋密度的 5 需以屏幕为准 |
| Mulliken 布居分析（自旋布居） | 7 → 5 → 1 | 2026.7.15 实测（输入须含基函数信息；闭壳层无 Spin pop. 列，开壳层才有） |
| Mayer 键级 | 9 → 1 | 2026.7.15 实测（输出单列 Total） |
| 拉普拉斯键级 | 9 → 8 → y（收尾 0 → q） | 2026.7.15 实测 |
| 定量分子表面分析（Estimated density） | 12 → 0 | 已核实（3.8 dev 时代） |
| 格点数据乘常数 | 13 → 11 → 5 → 0 导出 | 2026.7.15 实测 |
| 空穴-电子分析 | 18 → 1 | 已核实（3.8 dev 时代） |
| 导出文件 / 格式转换 | 100 → 2 | 子格式序号以屏幕为准；10=gjf 视输入是否含波函数多一问（见 9.1 节） |

## 附录 B：三种 shell 语法速查表

| 操作 | Git Bash | cmd | PowerShell |
|---|---|---|---|
| 输入重定向 | `< file` | `< file` | 不支持，用 `Get-Content file \|` |
| 覆盖输出 | `> file` | `> file` | `> file` |
| 追加输出 | `>> file` | `>> file` | `>> file` |
| 边显示边存 | `\| tee file` | 不支持 | `\| Tee-Object file` |
| 丢弃输出 | `> /dev/null` | `> NUL` | `> $null` |
| 丢弃错误 | `2> /dev/null` | `2> NUL` | `2>$null` |
| 输出+错误一起存 | `&> file` | `> file 2>&1` | `*> file` |
| 多行指令 | echo -e / heredoc | 指令文件 | here-string |
| 批量循环 | `for inf in *.wfn` | `for /f %%i in (...) do` | `Get-ChildItem *.wfn \| ForEach-Object` |

## 参考来源

- [[Multiwfn手册5.2-5.5]]
- [卢天《详谈Multiwfn的命令行方式运行和批量运行的方法》](http://sobereva.com/612)
- [卢天《通过键级曲线和ELF/LOL/RDG等值面动画研究化学反应过程》](http://sobereva.com/200)
- [卢天《谈谈自旋密度、自旋布居以及在Multiwfn中的绘制和计算》](http://sobereva.com/353)
