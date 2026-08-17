---
tags:
  - 计算化学
  - research
Category:
  - 讲义
---


# 2 一般信息

## 2.1 安装

### 2.1.1 Windows版本

您只需要解压缩程序包，然后双击图标即可开始使用。

Multiwfn中的少数功能依赖于Gaussian，如果您需要进行这些分析，需要手动为Gaussian设置环境变量，请参见附录1。

强烈建议将settings.ini中的“nthreads”设置为您机器上CPU物理核心的实际数量，以便在计算过程中充分利用CPU的所有计算能力。更多细节请参见第2.4节。

如果您希望Multiwfn能够直接打开Gaussian生成的.chk文件，请在settings.ini中将“formchkpath”设置为Gaussian软件包中formchk可执行文件的实际路径。

**2.1.2 Linux版本**

注意：本节的中文版本是我的博文“Linux下安装Multiwfn的中文说明”（http://sobereva.com/688）。

* 解压缩Multiwfn二进制包。
* 确保您已安装motif包，它提供libXm.so.4文件，没有此文件完整版Multiwfn无法启动。该motif可免费从 https://motif.ics.com/motif/downloads 获取。如果您是CentOS或Red Hat Linux用户且尚未安装motif，可以直接运行 yum install motif 安装；或者，您可以下载相应的rpm包（例如 motif-2.3.4-1.x86_64.rpm）并手动安装；如果您是Ubuntu用户，运行 sudo apt-get install libxm4 libgl1 安装，或下载deb包（例如 libmotif4_2.3.4-1_amd64.deb）并手动安装。
* 将以下几行添加到~/.bashrc文件中（例如使用 vi ~/.bashrc 命令）：
 export OMP_STACKSIZE=1000M
 ulimit -s unlimited
 这些行用于解除堆栈内存大小的限制，并为并行计算中的每个OpenMP线程定义1000MB的堆栈大小，详情请参见第2.4节。
 注意：如果 ulimit -s unlimited 在您的系统上无法正常工作，请尝试改用 ulimit -Sn unlimited。
* 运行 cat /proc/sys/kernel/shmmax 检查SysV共享内存段的大小是否足够大（单位为字节）；如果该值太小，Multiwfn在分析大型波函数时可能会崩溃。要扩大该大小，例如，您可以在/etc/sysctl.conf中添加 kernel.shmmax = 5000000000 并重启系统，则上限将扩大到约5GB。
* 假设您使用的是Bash shell，并且已将Multiwfn包解压到“/sob/Multiwfn_3.6_bin_Linux”文件夹，您应该将以下几行添加到~/.bashrc文件中：
 export Multiwfnpath=/sob/Multiwfn_3.6_bin_Linux
 export PATH=$PATH:/sob/Multiwfn_3.6_bin_Linux
* 运行以下命令，为Multiwfn可执行文件添加可执行权限：
 chmod +x /sob/Multiwfn_3.6_bin_Linux/Multiwfn
* 按照上一节所述的方式配置Multiwfn文件夹中的settings.ini文件。

重新进入终端后，您只需运行 Multiwfn 命令即可在任何位置启动Multiwfn。

如果您通过远程连接以纯文本模式使用Multiwfn服务器，并发现Multiwfn在加载输入文件后会卡顿约两秒，请在~/.bashrc文件中添加 export DISPLAY=":0"。

Multiwfn的Linux版本在CentOS 6/7/8、Rocky Linux 9以及Ubuntu 12/14/16/22上运行良好。我无法保证该程序与所有其他Linux发行版完全兼容。如果系统提示您在启动Multiwfn时缺少某些动态链接库（.so文件），请尝试查找并安装包含相应.so文件的软件包。

如果您因缺少某些图形相关库文件或不兼容而无法运行/编译Multiwfn，并且同时您不需要Multiwfn的任何可视化功能，您可以运行/编译不支持GUI的Multiwfn，所有与GUI和地图绘制无关的功能仍将正常工作。请查看源代码包中的“COMPLIATION_METHOD.txt”文件，了解如何编译这个特殊版本，该版本的预编译可执行文件也可以从Multiwfn网站下载（称为“noGUI”版本）。

**2.1.3 Mac OS版本**

由于我不是MacOS用户，因此没有MacOS版本的Multiwfn发布。如果您想在MacOS上编译Multiwfn，请查看 https://github.com/digital-chemistry-laboratory/multiwfn-mac-build。如果您能阅读中文，请参见 http://bbs.keinsci.com/thread-46059-1-1.html。

编译Multiwfn后，您应该执行以下步骤（但我无法保证以下前两步在最新版本的MacOS上仍然有效）：

(1) 将以下行添加到您的.profile文件（例如 /Users/sob/.profile）中，使其自动生效，然后重启您的终端。如果.profile不存在，您应该手动创建它。
export OMP_STACKSIZE=64000000
OMP_STACKSIZE定义了并行实现中每个线程的堆栈大小（以字节为单位），详情请参见第2.4节。

(2) 运行 sysctl -a|grep shmmax 检查SysV共享内存段的大小是否足够大（单位为字节），如果该值太小，Multiwfn在分析大型波函数时可能会崩溃。为了扩大大小，您应该编辑或创建文件 /etc/sysctl.conf，并向其中添加 kern.sysv.shmmax = 512000000 然后重启系统，则上限将扩大到约512MB。

(3) 如有需要，设置Multiwfnpath环境变量，参见第2.1.2节第5点。

(4) 按照第2.1.1节所述的方式配置settings.ini文件。

一位Multiwfn用户Maciej Spiegel提供了在MacOS上运行Multiwfn的替代方法：
首先，用户应下载最新版本的Unofficial Wineskin (https://github.com/Gcenx/WineskinServer/releases/tag/V1.8.4)。之后，运行它，更新wrapper版本并下载一个最新的引擎。这些引擎是 WS11WineCX64Bit19.0.1-1（用于64位系统）或 WS11WineCX19.0.1-1（用于32位系统）。最后，创建一个新的wrapper并使用Windows GUI安装程序。

**2.2 使用Multiwfn**

使用Multiwfn非常简单，只需阅读屏幕上显示的提示，您就会知道下一步应该输入什么。如果您遇到困难，请仔细阅读第3章中的相应部分或第4章中的相应教程。

在Windows中，Multiwfn通常通过直接双击可执行文件的图标启动，然后您应该输入要加载的文件路径。您也可以通过命令行启动Multiwfn，同时可以给出输入文件的路径，例如运行 Multiwfn /sob/test.wfn。

如果输入文件在当前目录中，您可以直接输入文件名而不带目录路径。如果输入文件是上次使用的那个，您可以在进入Multiwfn后直接输入字母 o（上次成功读取的输入文件路径已记录在settings.ini中）。如果输入文件与上次使用的文件在同一文件夹中，为了方便，可以用符号 ? 替换路径。例如，上次您加载了 C:\sob\wives\K-ON\Mio.wfn，这次您可以简单地输入 ?Azusa.fch 来加载 C:\sob\wives\K-ON\Azusa.fch。如果您希望在GUI窗口中选择输入文件，可以在进入Multiwfn后直接按ENTER键，然后会显示一个GUI窗口用于选择输入文件。

您可以随时按CTRL+C或点击Multiwfn窗口右上角的“×”按钮退出Multiwfn，但更优雅的退出方式是在主菜单中输入 q。当屏幕上显示图形窗口时，您可以点击“RETURN”按钮关闭窗口，如果没有此按钮，可以右键单击图形将其关闭。

如果您想将另一个文件加载到Multiwfn中，可以重启Multiwfn或启动一个新的Multiwfn实例。或者，在主菜单中您可以输入 r 来初始化Multiwfn并加载新文件，同时settings.ini也会被重新加载。但是请注意，加载新文件最安全的方式是重启Multiwfn。

Multiwfn也可以以静默模式而非交互模式运行，这样用户在运行过程中无需按任何键盘按钮。这对于批处理很有用，请参考第5.2和5.3节。

**支持的参数**

为了方便，通过命令行运行Multiwfn时可以添加一些参数：

* -nt：并行计算的线程数
* -uf：用户自定义函数的索引
* -silent：以静默模式运行Multiwfn
* -set：settings.ini的路径

例如：
Multiwfn COCl2.fch -nt 36 -set /sob/tmp/settings.ini -silent

这些参数的优先级高于settings.ini中的参数。如果在Multiwfn启动时找不到settings.ini，这些参数将不会生效，只会使用默认参数。

**2.3 Multiwfn的文件**

解压Multiwfn包后，您会看到以下文件，只有加粗的文件是运行Multiwfn所必需的：

* **Multiwfn.exe (Windows) 或 Multiwfn (Linux/Mac OS)**：Multiwfn的可执行文件。
* **libiomp5md.dll (Windows)**：Intel OpenMP运行时库。
* **settings.ini**：这里记录了运行Multiwfn的所有详细参数，其中大部分不需要频繁修改。启动时，Multiwfn会尝试在当前文件夹中查找并使用此文件，如果当前文件夹中不存在，将使用“Multiwfnpath”环境变量定义路径中的文件；如果仍然找不到该文件，将使用默认设置。如果您通过命令行运行Multiwfn，也可以通过“-set”参数直接指定此文件的位置，例如：Multiwfn test.wfn -set /sob/3.7/settings.ini。
 本手册不系统地记录settings.ini中所有参数的含义，因为它们已经有详细的注释，本手册只会提及那些重要的参数。我建议您通读settings.ini，找出对您有用的参数。
* “examples”文件夹：一些有用的文件、脚本以及第4章示例中涉及的文件。
* LICENSE.txt：所有用户必须遵守的条款。
* Multiwfn快速入门.pdf：一份简短文档，让新用户立即了解如何使用Multiwfn完成非常常见的任务。
* How to cite Multiwfn.pdf：请根据此文档正确引用Multiwfn。

**2.4 并行实现**

Multiwfn的大部分耗时代码已通过OpenMP技术并行化。如果您的CPU有多个核心，您可以极大地受益于并行化。要启用并行化，只需将settings.ini中的“nthreads”参数修改为合适的数字。例如，您的计算机有一个12核物理核心的CPU，那么通常您应该将“nthreads”改为12。

如果在处理非常大的体系时并行计算导致Multiwfn崩溃，请尝试增大settings.ini中的“ompstacksize”（对于Windows版本）或增大环境变量OMP_STACKSIZE的值（对于Linux或Mac OS版本）。

**2.5 输入文件和波函数类型**

Multiwfn支持的波函数类型包括限制性/非限制性单行列式波函数、限制性开壳层波函数和后HF波函数（以自然轨道形式）。

支持角动量最高到h的Cartesian或球谐Gaussian函数。Multiwfn对原子/基函数/GTF/轨道的数量没有上限，实际上限仅由您计算机的可用内存决定。Multiwfn通过文件扩展名来确定输入文件类型。请注意，不同的功能需要不同类型的信息，您应该选择合适的输入文件类型，见下表。例如，Hirshfeld布居分析只需要由GTF表示的波函数，因此您可以使用.mwfn/.fch/.molden/.gms/.31~.40/.wfn/.wfx文件作为输入，但不能使用.pdb、.xyz、.mol等文件，因为它们不携带任何波函数信息；相反，在分子态近似下生成RDG函数的网格数据仅需要原子坐标，因此所有支持的文件格式都可以使用（纯文本文件除外）。每个功能对信息类型的要求通常在第3章相应部分的末尾用红色文本说明。

**文件格式** | **提供的信息类型**
:--- | :---
| **基函数** | **GTFs** | **原子坐标** | **格点数据** | **原子电荷**
.fch/.fchk/.chk | ✓ | ✓ | ✓ | ✗ | ✗
.mwfn, .molden, .gbw, .gms | ✓ | ✓ | ✓ | ✗ | ✗
NBOplot文件 (.31 to .40) | ✗ | ✓ | ✓ | ✗ | ✗
.wfn and .wfx | ✗ | ✓ | ✓ | ✗ | ✗
.pdb, .xyz, .mol/sdf, .mol2, .gro, .cif, .mop, Gaussian/ORCA输入/输出文件, CP2K输入/重启文件, POSCAR, Quantum ESPRESSO输入文件, Turbomole坐标文件 | ✗ | ✗ | ✓ | ✗ | ✗
.chg and .pqr | ✗ | ✗ | ✓ | ✗ | ✓
.cub/.cube, CHGCAR/CHG/ELFCAR/LOCPOT | ✗ | ✗ | ✓ | ✓ | ✗
.vti, .grd, .dx | ✗ | ✗ | ✗ | ✓ | ✗
其他（纯文本文件） | ✗ | ✗ | ✗ | ✗ | ✗

关于幽灵原子：在下面描述的任何波函数格式中，都允许出现幽灵原子（有基函数但没有核电荷的点）。它们的元素索引应为0，如果文件格式记录了元素名称，幽灵原子的元素名称应为Bq。Multiwfn以常规方式从文件中加载它们的核电荷，但原则上，由于它们是幽灵原子，核电荷应为零。

**Multiwfn波函数文件 (.mwfn)**：此格式自Multiwfn 3.7起定义并支持。这是存储和交换波函数信息最理想的格式。此文件以严格、简洁、紧凑且可扩展的格式记录所有波函数分析所需的信息。此格式的介绍和定义已在我的论文中详细描述：ChemRxiv (2020) DOI: 10.26434/chemrxiv.11872524。

**AIM波函数文件 (.wfn)**：此格式最初由Bader的AIMPAC程序引入，目前被许多主流量子化学软件支持，如Gaussian、ORCA、GAMESS-US/UK、Firefly、Q-Chem和NWChem。.wfn文件中的信息包括原子坐标、元素、轨道能量、占据数、Cartesian Gaussian型函数(GTF)的展开系数。支持的GTF角动量最高到f。wfn文件不包含任何虚轨道。生成.wfn文件的方法在第4章开头有说明。

注意：虽然g和h角动量的GTF并未被原始.wfn格式正式支持，但如果g和h型GTF以下列方式记录，Multiwfn能够识别它们：“TYPE ASSIGNMENT”中的21~35分别对应YZZZ、XYYY、XXYY、XYZZ、YZZZ、XYYZ、XXXX、XXXY、XZZZ、XXYZ、XXXZ、XXZZ、YYYY、YYYZ、ZZZZ。36~56分别对应ZZZZZ、YZZZZ、YYZZZ、YYYZZ、YYYYZ、YYYYY、XZZZZ、XYZZZ、XYYZZ、XYYYZ、XYYYY、XXZZZ、XXYZZ、XXYYZ、XXYYY、XXXZZ、XXXYZ、XXXYY、XXXXZ、XXXXY、XXXXX。这里显示的顺序实际上也是Molden2AIM和Gaussian09（自B.01版起）输出的.wfn中使用的顺序。

**AIM扩展波函数文件 (.wfx)**：这是作为.wfn扩展而引入的一种格式，自G09 B.01版起得到支持。相对于.wfn格式，.wfx支持更高的数据记录精度和无限高的GTF角动量。此格式最特别之处是新添加的电子密度函数（EDF）字段，即使用多个GTFs来表示使用有效核势（ECP）的波函数的内壳层电子密度。因此，对使用ECP的波函数进行电子密度分析的结果几乎与全电子波函数的结果相同。目前Multiwfn中支持EDFs的实空间函数包括：电子密度、其梯度和Laplacian、局域信息熵、约化密度梯度以及Sign(λ2(r))。同时，对电子密度及其Laplacian的拓扑分析也考虑了EDFs。请注意，EDF信息对ESP以及依赖于波函数的实空间函数（如动能密度、ELF）没有影响。如果您想分析重元素的这些性质，应使用全电子基组，至少使用小核ECP。目前EDF字段中唯一支持的GTF类型是S型（实际上S型足以拟合内层密度，因为内层密度几乎是球对称的）。与.wfn一样，Multiwfn不允许.wfx文件中出现虚轨道。

Multiwfn有一个强大的内置EDF库，取自Wenli Zou开发的Molden2aim程序。只要输入文件包含GTF信息（例如.fch、.wfn、.molden、.gms...），Multiwfn总会在使用ECP的原子处自动从该库加载EDF信息。只有当您使用.wfx文件作为输入且.wfx文件本身已包含EDF字段时，EDF信息才会从.wfx文件加载而不是从EDF库加载。详细信息请参见附录4。

请注意，虽然Gaussian以外的其他程序（例如ORCA）也能生成.wfx文件，但这些.wfx文件无法提供EDF字段。

注意：对于特定版本的Gaussian（例如G09 B.01），我发现极少数情况下.wfx中记录的EDF字段存在问题，即EDF字段表示的电子数与ECP实际体现的核心电子数不等。为了验证EDF字段是否正确，您可以使用主功能100中的子功能4来获取总电子密度在全空间的积分，如果结果约等于总电子数（核心+价电子），则表示EDF字段正确。

**Gaussian格式化检查点文件 (.fch/.fchk)**：Gaussian程序的检查点文件(.chk)可以通过Gaussian软件包中的formchk工具转换为格式化检查点文件(.fch/.fchk)。.fch和.fchk之间没有任何区别。“fch”(“fchk”)是Windows（Linux）版formchk生成的默认扩展名。

如果您希望Multiwfn能够直接加载.chk文件，则必须在settings.ini中将“formchkpath”设置为Gaussian软件包中formchk可执行文件的实际路径。在这种情况下，Multiwfn将自动调用formchk将.chk文件转换为.fch/fchk文件，如果转换成功，.fch/fchk文件将被加载，并在加载完成后自动删除。

.fch/.fchk文件包含比.wfn/.wfx文件更丰富的信息，虚轨道波函数也被包含在内，同时它为Multiwfn提供了基函数信息。如果您想使用.fch/.fchk文件作为后HF波函数的载体，请仔细阅读第4章开头的内容！

Q-Chem和PSI4生成的.fchk文件也可以用作Multiwfn的输入文件。（如果.fchk文件是由相对较旧版本的Q-Chem生成的，您必须将settings.ini中的“ifchprog”设置为2。如果您的Q-Chem版本等于或新于5.0，则无需执行此操作）。

**Molden输入文件 (.molden 或 .molden.input 或 molden.inp)**：目前，许多量子化学软件包，如Molpro、Molcas、ORCA、Q-Chem、CFour、Turbomole、PSI4、MRCC和NWChem，以及第一性原理代码CP2K，都能生成Molden可视化程序的输入文件。此类型文件记录了原子坐标、基组定义、所有占据和虚轨道的信息（包括基函数的展开系数、占据数、自旋、能量和对称性），同时没有仅特定于Molden的信息。因此，实际上可以将Molden输入文件视为交换波函数信息的标准通用文件格式。对于Multiwfn，此类型文件可以提供原子坐标、基函数信息和GTF信息。

请注意，许多程序生成的Molden输入文件非常不规范！目前Multiwfn只正式支持由Molpro、ORCA、xtb、Dalton、NWChem（仅限球谐函数且同时禁用对称性）、MRCC（仅限球谐函数）、deMon2k、BDF、CP2K（仅限球谐函数）生成的Molden输入文件。如果您使用的Molden输入文件是由其他程序生成的，分析结果可能正确也可能不正确，您应该首先使用附录5中描述的方法检查波函数是否正确加载。

提示：Multiwfn完全支持由molden2aim工具标准化的Molden输入文件（详见第5.1节），该工具能够正确识别由许多其他量子化学代码（如CFOUR和Molcas）生成的Molden输入文件。

.molden文件正式只支持角动量最高到g的基函数。但是，主功能100的子功能2可以生成包含h函数的.molden文件，Multiwfn可以正常加载它。即使存在h函数，Multiwfn也能正常加载ORCA和Dalton生成的.molden文件。

虽然Molden输入文件也支持Slater型轨道(STO)，Multiwfn只能利用记录Gaussian型基函数的Molden输入文件。

Molden格式的一个严重缺点是它不像wfn和fch等其他格式那样明确记录核电荷，因此当使用ECP时，依赖核电荷的结果（如静电势和原子电荷）将出现问题。为了解决这个问题，Multiwfn会加载文件中的原子索引（即[Atoms]字段中的第三列）作为核电荷，因此，如果您手动将原子索引更改为量子化学计算中明确表示的原子价电子数（等效于有效核电荷），则结果将是正确的。如果您对此感到困惑，请查看此帖：http://sobereva.com/wfnbbs/viewtopic.php?pid=721。或者，您可以在此文件开头手动插入[Nval]字段，以明确指定特定元素的价电子数；例如，以下几行要求Multiwfn将Na和Cl的价电子数分别设置为9和7，而其他元素的保持不变。
[Nval]
Na 9
Cl 7

值得注意的是，如果您使用ORCA >=6.0，则无需对molden文件执行上述修改，因为ORCA导出的molden文件包含[Pseudo]字段，该字段为使用ECP的原子提供了正确的核电荷，Multiwfn会自动加载它（在这种情况下，molden文件的标题行必须包含orca字样，以便Multiwfn识别它是由ORCA生成的）。

使用Molden输入文件作为波函数载体的另一个明显缺点是此格式不如.mwfn和.fch紧凑。因此，对于相同的波函数，加载.molden文件的速度比.mwfn和.fch慢得多。因此，如果您需要频繁分析.molden文件，我建议您使用主功能100的子功能2将其转换为.mwfn格式。

如何通过一些量子化学程序生成Molden输入文件在第4章开头有描述。如果您是ORCA用户，并且不想通过ORCA中的orca_2mkl工具手动将.gbw文件转换为Molden输入文件，您可以在settings.ini中设置"orca_2mklpath"为ORCA文件夹中orca_2mkl可执行文件的实际路径，这样Multiwfn就能直接加载.gbw文件。

附：关于.molden格式的详细描述可以在Molden官方网站找到：https://www3.cmbi.umcn.nl/molden/molden_format.html。

**GAMESS-US或Firefly输出文件 (.gms)**：如果您想使用GAMESS-US或Firefly（原PC-GAMESS）输出文件作为输入，可以将其扩展名更改为.gms，然后Multiwfn将正确识别它。目前，我只能保证使用默认NPRINT选项的HF/DFT/TDDFT计算输出文件能被Multiwfn正常加载。如果点群不是C1，Multiwfn将无法处理该输出文件。

.gms文件的作用类似于.molden和.fch文件，即它们都提供原子坐标、GTF和基函数信息。

由于我不是资深的Firefly用户，我无法保证与Firefly输出文件的兼容性像GAMESS-US输出文件那样好。对于前者，我只测试了DFT单点任务和TDDFT任务。

**NBO程序的绘图文件 (.31~.40)**：支持这些文件类型的主要目的是可视化PNAO/NAO/PNHO/NHO/PNBO/NBO/PNLMO/NLMO/MO（它们的轨道系数分别记录在.32~.40中），.31记录基函数信息。启动Multiwfn后，您应该先输入.31文件的路径，然后输入.32~.40中一个文件的路径（为简单起见，当文件名相同时，您可以只输入后缀）。

请注意，在NBO程序生成的所有类型的轨道中，只有使用NBO或NLMO计算实空间函数才有意义！

**蛋白质数据库格式 (.pdb), .xyz, MDL Molfile (.mol/sdf), .mol2**：这些是记录原子坐标最广泛使用的格式。它们不携带任何波函数信息，但对于仅需要原子坐标的功能，使用这些文件作为输入是足够的。.mol和.mol2相对于.pdb和.xyz的一个优势是它们包含原子连接性表，Multiwfn的一些功能需要用到它，例如计算EEM原子电荷。如果.xyz文件包含多个帧，则只加载第一帧。

请注意，Multiwfn支持的.mol文件是V2000版本，可以记录的最大原子数和键数均为999。关于.mol格式的更多描述可以在 https://en.wikipedia.org/wiki/Chemical_table_file 找到。.sdf文件只是.mol文件的包装，附加了额外信息。

在标准的.xyz文件中，每个原子的名称是元素名称。然而，VMD基于一些分子动力学程序的轨迹导出的.xyz文件使用的是模拟中使用的原子名称，在这种情况下，Multiwfn无法总是正确地从原子名称中识别出实际元素，因此Multiwfn中有一个特殊规则来规避此问题：如果输入.xyz文件的同一文件夹中存在同名.pdb文件，则将使用.pdb文件中的元素名称（但是，如果.pdb文件中某个原子的元素名称缺失，Multiwfn仍将根据.xyz文件中的原子名称猜测元素）。

**.pqr文件**：此格式与.pdb格式非常相似，但内容不同。在对应于原子X/Y/Z坐标的列之后，有两列分别记录原子电荷和原子半径（这两列的小数位数不重要，字段必须用空白分隔）。这种文件可以向Multiwfn提供原子信息以及原子电荷信息。下面是一个水的.pqr文件示例。REMARK字段可以存在以记录注释，加载文件时会跳过它们。
REMARK From file m1charges.out
REMARK ESP charges
ATOM 1 O O 1 1 0.000 0.123 0.000 -0.680698 2.9000
ATOM 2 H O 1 1 0.757 -0.490 0.000 0.340338 2.6000
ATOM 3 H O 1 1 -0.757 -0.490 0.000 0.340361 2.6000

**电荷文件 (.chg)**：这种类型的纯文本文件可以由Multiwfn的一些功能生成（例如布居分析功能），它包含元素名称（少于或等于两个字符）、原子坐标（前三列，单位Å）和电荷（第四列），用户可以手动修改它们。此文件格式自由，所有字段必须用空白分隔。此文件可以提供原子电荷信息，主要用途是基于原子电荷可视化和分析分子表面上的静电势，也可以使用主功能7的子功能-2以.chg文件作为输入来评估基于原子电荷的静电相互作用能。加载.chg文件时，屏幕上将显示所有原子电荷的总和以及使用原子电荷计算的电偶极矩。

下面给出一个水分子.chg文件的示例：
O 0.000000 0.000000 0.119308 -0.301956
H 0.000000 0.758953 -0.477232 0.150977
H 0.000000 -0.758953 -0.477232 0.150977

**.gro文件**：GROMOS结构格式。这种文件最常用于GROMACS分子动力学程序。.gro文件只能为Multiwfn提供原子信息。请注意，由于此文件记录的是原子名称而不是元素，Multiwfn在加载时会根据原子名称和残基名称自动猜测实际元素。但是，有时猜测的元素可能不正确，因此建议在加载文件后检查打印的分子式。

**.cif文件**：这是记录晶体结构的标准格式。对称操作必须在此文件中明确给出，否则无法生成等价原子的位置。

**Gaussian型cube文件 (.cub 或 .cube)**：这是最流行的体积数据格式，可以由大量计算化学软件生成，并且可以被大多数分子图形程序识别。此文件可以记录原子坐标、一组实空间函数网格数据或多组分子轨道网格数据。将cube文件加载到Multiwfn后，您可以选择主功能0来可视化等值面，或使用主功能13来处理网格数据。

**.vti, .dx 和 DMol3网格文件 (.grd)**
.vti是“ParaView VTK Image Data”格式，可以记录标量场和矢量场。这种文件可以由例如GIMIC 2.0和ParaView程序生成。只支持包含ASCII类型标量数据的.vti文件。简而言之，此文件与.cub文件非常相似，但没有原子信息。
.dx是可以由例如VMD程序的Volmap插件导出的体积数据格式。
.grd文件是DMol3程序主要使用的体积数据格式。.grd中不记录原子信息。

**Gaussian输入文件 (.gjf), ORCA输入文件和MOPAC输入文件 (.mop)**：这些文件可以为Multiwfn提供原子坐标信息以及α和β电子数的信息。请注意，原子必须记录为Cartesian坐标。.gjf还可以通过“Tv”字段向Multiwfn提供晶胞信息。

**Gaussian和ORCA输出文件**
Gaussian和ORCA输出文件可以为Multiwfn提供原子信息。
* Gaussian输出文件：当settings.ini中的"iloadGaugeom"设置为1（默认，加载输入取向）或2（加载标准取向）时，Multiwfn将从此文件加载（最终）几何和电子数。
* ORCA输出文件：当settings.ini中的"iloadORCAgeom"设置为1（默认）时，Multiwfn将从此文件加载（最终）几何。

**CP2K输入和重启文件 (.inp 和 .restart)**：这些文件可以为Multiwfn提供原子坐标信息和晶胞信息。请注意，原子必须以Å为单位的Cartesian坐标记录。

**Quantum ESPRESSO输入 (.inp 或 .in)**：它可以为Multiwfn提供原子坐标信息和晶胞信息。只支持ibrav=0。

**Turbomole坐标文件**：如果纯文本文件的第一行是&coord，则它将作为Turbomole坐标文件加载。$coord字段提供原子信息。如果存在$periodic和$lattice，它们也将提供晶胞信息。

**VASP相关文件**
以下文件与VASP代码相关。Multiwfn能够加载它们，文件名必须包含相应的字符串，且没有.in或.inp扩展名。例如，要将文件作为POSCAR加载，文件名可以是POSCAR_Si8和MOF.POSCAR。
* POSCAR：这是VASP的输入文件之一，记录晶胞和原子信息。
* CHGCAR或CHG：此文件记录VASP生成的电子密度。对于自旋极化情况，它也同时记录自旋密度。
* ELFCAR：此文件记录VASP生成的ELF。对于自旋极化情况，它分别记录α和β电子的ELF。
* LOCPOT：此文件记录VASP生成的一个电子感受到的外部势。对于自旋极化情况，它分别记录α和β电子的势。如果LVHAR=.TRUE.，该势对应于静电势的负值；而如果LVHAR=.FALSE.，它对应于“分子中一个电子感受到的势”（PAEM，在第2.7节中描述）。

**纯文本文件**：此文件类型仅用于特殊功能，例如绘制DOS图、绘制光谱、生成具有初始猜测的Gaussian输入文件。请参阅相应部分的说明。

---

第二章的第2.1至2.5节翻译完毕。这部分详细介绍了Multiwfn在不同操作系统下的安装方法、基本使用方式、程序文件构成、并行计算设置，以及最重要的部分——各种支持的输入文件格式及其用途。

接下来是否继续翻译第2.6节“Real space functions”（实空间函数）？
