
# 5 技巧

## 第1节：命令行方式运行

- 命令行格式：`Multiwfn [输入文件路径] [选项/参数]`
- 常用选项：
  - -nt 线程数：并行线程数（已配 nthreads=18，可省略）
  - -silent：不自动弹图形窗口，批量运行必用（否则每算一个体系就要手动关一次窗口）
  - -set 路径：指定 settings.ini 位置
  - -uf 序号：用户自定义函数
- 三种传入指令的方式：
  - 重定向：Multiwfn xxx.fch < 指令.txt（指令文件每行一条命令）
  - Bash heredoc：Multiwfn xxx.fch << EOF ... EOF
  - 管道直传：echo -e "9\n8\ny" | Multiwfn xxx.fch
- 输出处理：> out.txt 存屏显、| tee out.txt 既显示又存、> NUL（cmd）丢弃
- 关键技巧：任务完成后直接结束会报 forrtl: severe (24): end-of-file 错误，完全无害不用管；想消除就在指令末尾加 0（返回主菜单）q（优雅退出），或把 2> /dev/null 加到命令尾部

## 第2节：脚本实例（数据提取技巧）

- 通用套路：grep "关键词" out.txt | awk '...' 从输出文件提取数值
- 例：t1=$(grep "Estimated density" out.txt | awk -F : '{print $2}' | awk '{print $1}') —— grep 定位行 → awk 按分隔符切字段
- awk 里可以传参做运算：awk '{print a*$1+b*$2+g}' a=0.9183 b=0.0028 g=0.0443
- -ESPrhoiso 0.001 特殊参数：只在密度等值面附近算 ESP，大幅加速表面静电势计算
- eV 单位转换技巧：把 totesp.cub 重新载入 → 主功能13 → 11 → 5（乘常数）→ 输入 27.2114（Hartree→eV）
- 用 for ((i=1;i<=3;i++)) 循环 + heredoc 追加，动态生成指令文件批量算多个激发态

## 第3节：批量运行（两种循环写法）

- Bash 版：`for inf in *.wfn; do Multiwfn $inf < genELFcub.txt > /dev/null; mv ELF.cub ${inf//.wfn}_ELF.cub; done`
- 字符串替换技巧：`${inf//.wfn}_ELF.cub `把扩展名换成 `_ELF.cub`
- Windows batch 版：`for /f %%i in ('dir *.wfn /b') do (...)，用 %%~ni 取文件名主体`

## 第4节：批量实例（现成的提取命令）

- HOMO-LUMO gap 提取：grep "HOMO-LUMO gap" out.txt | awk '{print $5}'（第5列是 eV 值，主功能0输出）
- 原子自旋布居：grep "Population of atoms:" -A 100 out.txt | grep "4(H )" | cut -c 41-51（先锚定区域再按列截取）
- Mayer 键级：grep "1(C )    3(C )" out.txt | cut -c 69-78（Total 列）
- 批量格式转换：主功能100 → 子功能2 → 选导出格式
- gbw 批量转 molden：orca_2mkl $name -molden
- ffmpeg 合成动画：先 palettegen 生成调色板，再 -lavfi paletteuse 合并 gif
## 5.4 将命令行窗口的输出复制到剪贴板

有时，Multiwfn在命令行窗口中的输出需要被永久保存或加载到第三方软件中，以便通过纯文本文件进行处理。下面我介绍如何将这些输出复制到Windows剪贴板。

如果您使用的是Windows 11，您只需按住“ALT”键，用鼠标左键在窗口中拖出一个矩形区域，然后按ENTER键，该区域的内容将被复制到剪贴板。

如果您使用的是较旧的Windows版本，则需要按照下面显示的步骤操作。假设您想复制电子密度的Hessian矩阵。

在窗口标题栏上点击鼠标右键，选择“编辑”-“标记”，然后将鼠标移动到窗口中的某个点并按住左键拖动，直到目标内容全部被高亮显示。

在您选择“标记”后，从点A拖到点B

然后按ENTER键，白色矩形高亮显示的信息将被复制到剪贴板，您可以将其粘贴到任何位置，例如纯文本文件。

对于在图形环境下运行的Mac OS或Linux系统，您也可以通过类似方式将Multiwfn在控制台中的输出复制到纯文本文件中。

## 5.5 使命令行窗口能够记录更多输出

有时您可能会发现命令行窗口无法记录Multiwfn的全部输出。例如，您选择波函数修改模块中的选项6以获取相对较大的波函数的密度矩阵，但命令行窗口中只能找到矩阵的最后一部分。解决这个问题的方法是增大窗口的缓冲区大小，请遵循以下步骤。

启动Multiwfn，在窗口标题上点击鼠标右键，点击“属性”，选择“布局”页，您会看到窗口的默认缓冲区大小为300（见下面的截图），这意味着窗口中最多只能记录300行，这显然太小了。将该值更改为更大的值，例如9999，然后点击“确定”按钮。之后，您将发现该窗口能够记录更多的输出（如果仍然无法记录完整输出，请再次增大缓冲区大小）。

缓冲区大小设置会永久保存在系统中，下次启动Multiwfn时您无需再次设置此值。

对于Linux和Mac OS，您也可以找到类似的选项来设置终端缓冲区大小。

