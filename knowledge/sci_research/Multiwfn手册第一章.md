---
tags:
  - 计算化学
  - research
Category:
  - 讲义
---

# 第一章

## 1概述

Multiwfn是一个功能强大的波函数分析程序，它支持几乎所有最重要的波函数分析方法。Multiwfn是免费、开源、高效、非常用户友好且灵活的程序。您可以在Multiwfn官方网站 http://sobereva.com/multiwfn 下载Multiwfn。该代码由北京科音自然科学研究中心（http://www.keinsci.com）的卢天开发。

## Multiwfn支持的输入文件

Multiwfn接受多种文件格式来加载波函数信息：.mwfn（Multiwfn波函数文件）、.wfn/.wfx（常规/扩展PROAIM波函数文件）、.fch（Gaussian格式化检查文件）、.molden（Molden输入文件）、.31~.40（NBO绘图文件）和.gms（GAMESS-US和Firefly输出文件）。其他类型如Gaussian输入和输出文件、.cub、.grd、.pdb、.xyz和.mol文件可用于特定功能。

简而言之，Multiwfn可以基于几乎所有知名量子化学程序（如Gaussian、ORCA、GAMESS-US、Molpro、NWChem、Dalton、xtb、PSI4、Molcas、Q-Chem、MRCC、deMon2k、Firefly、CFOUR、Turbomole...）的输出文件执行波函数分析。由于也支持CP2K导出的.molden文件，Multiwfn不仅能够处理分子体系，还可以分析周期性体系（尽管可使用功能有限，详见手册第2.9节）。

## Multiwfn的特殊之处

(1) **功能非常全面。** 几乎所有最重要的波函数分析方法都已得到Multiwfn的良好支持。

(2) **极其用户友好。** Multiwfn被设计成一个交互式程序（但也可以静默运行并嵌入到shell脚本中），屏幕上显示的每一步提示都清楚地告诉用户下一步应该输入什么。Multiwfn也从不打印晦涩难懂的信息，因此即使是初学者也没有任何障碍。此外，所有波函数分析理论都有非常详细的文档记录，手册中有一百多个编写良好的示例；此外，还有一个“快速入门”文档，指导新用户立即掌握常见分析。而且，开发者总是非常及时和耐心地在Multiwfn官方论坛上回复所有用户的问题。

(3) **高度灵活。** Multiwfn的整体框架、功能和人机界面的设计相当灵活，但这并不以牺牲易用性为代价。Multiwfn的不同模块有机地集成在一起，使得许多单一模块无法实现的分析变得可行。

(4) **高效率。** Multiwfn的代码经过了大量优化。大部分部分通过OpenMP技术进行了并行化。对于计算密集型的任务，Multiwfn的效率显著超过同类程序。

(5) **结果可直接可视化。** Multiwfn内部自动调用高级图形库DISLIN来可视化结果，大多数绘图参数都可以在交互界面中控制。这极大地简化了波函数分析，特别是对于研究实空间函数的分布。

## Multiwfn的主要功能

PS：尽管Multiwfn有这么多功能，手册也很厚，但您可以通过查看Multiwfn软件包中的“Multiwfn快速入门”文档轻松学会如何实现下面列出的功能。

* **显示分子结构和查看轨道（MO、NBO、自然轨道、NTO、LMO等）。** 生成轨道图形的速度极快，使用也非常方便。
* **在一点处输出所有支持的实空间函数以及所指定函数的梯度和Hessian矩阵。** 数值可以分解为轨道贡献。
* **沿一条线计算实空间函数并绘制曲线图。**
* **在平面内计算实空间函数并绘制平面图。** 支持的图形类型包括彩色填充图、等高线图、浮雕图（带/不带投影）、梯度图和矢量场图。
* **在空间范围内计算实空间函数，** 数据可以导出为Gaussian型cube网格文件（.cub），并可作为等值面可视化。
* **对于一维、二维和三维实空间函数的计算，用户可以定义多个波函数文件生成的数据之间的运算。** 因此，可以非常容易地计算和绘制如Fukui函数、双描述符和密度差等。同时，所有实空间函数的分子态和形变性质都可以直接计算。
* **对任何实空间函数进行拓扑分析，** 例如电子密度（AIM分析）、Laplacian、ELF、LOL、静电势等。可以定位临界点（CPs），生成拓扑路径和跨盆地表面，然后可以在3D GUI窗口中直接可视化或在平面图中绘制。可以在临界点或沿拓扑路径计算各种实空间函数的值。CP属性可以分解为轨道贡献。
* **检查和修改波函数。** 例如，打印轨道和基函数信息，手动设置轨道占据数和类型，平移和复制系统，丢弃指定原子的波函数信息。
* **布居分析。** 支持ADCH（原子偶极矩校正的Hirshfeld）、Hirshfeld、Hirshfeld-I、MBIS、VDD、Mulliken、Löwdin、修正的Mulliken（包括三种方法：SCPA、Stout & Politzer、Bickelhaupt）、Becke、CM5、1.2`*`CM5、CHELPG、Merz-Kollmann、RESP、RESP2、AIM（分子中的原子）和EEM（电负性均衡方法）。可以基于原子电荷计算两个给定片段间的静电相互作用能。
* **轨道成分分析。** 支持Mulliken、Stout & Politzer、SCPA、Hirshfeld、Hirshfeld-I、Becke、自然原子轨道（NAO）和AIM方法获取轨道成分。可以计算轨道离域指数（ODI）或空间离域指数（SDI）来量化轨道的空间离域程度。
* **键级/强度分析。** Mayer键级；多中心键级（MCBO）和多中心指数（MCI）（在AO或自然原子轨道(NAO)基下，任意中心数）；Löwdin正交基下的Wiberg键级；Mulliken键级；AV1245指数；固有键强度指数（IBSI）。Mayer和Mulliken键级可以分解为轨道贡献。Wiberg键级可以分解为各种NAO对相互作用的贡献。
* **绘制总态密度、分波态密度、重叠布居态密度（TDOS、PDOS、OPDOS）和MO-PDOS。** 可以非常灵活方便地定义最多10个片段。也可以为一点绘制局域态密度（LDOS）曲线图或为一条线绘制彩色填充图。此外，完全支持基于（广义）Koopmans定理绘制光电子能谱（PES），并可计算d带和p带中心。还可以绘制晶体轨道Hamilton布居（COHP）。
* **绘制各种光谱：** IR（红外）、常规/预共振Raman、UV-Vis、方向UV-Vis、ECD（电子圆二色）、VCD（振动圆二色）、拉曼光学活性（ROA）和NMR。对于振动光谱，不仅可以绘制谐波光谱，还可以绘制非谐波基频、泛频和组合频带。电子光谱可以考虑自旋-轨道耦合效应。用户可以自定义丰富的参数（展宽函数、FWHM、比例因子等）。可以打印光谱的最大值和最小值，并直接在地图上标注。可以在图形底部添加尖峰以清晰指示跃迁能级的位置和简并度。总光谱可以分解为每个跃迁的单独贡献。可以方便地同时绘制多个体系的光谱。可以轻松绘制构象加权光谱。此外，对于振动类型的光谱，可以绘制局域振动谱（PVS）以直观理解不同原子或内坐标如何参与光谱，并可绘制重叠局域振动谱（OPVS）以可视化各种项的耦合。也可以绘制局域振动态密度（PVDOS）。可以根据理论上模拟和实验测定的UV-Vis光谱精确预测化学物质显示的颜色。
* **分子表面定量分析。** 可以为整个分子表面或局域表面计算表面性质，如（总/正/负/极性/非极性）表面积、包围体积、映射函数的平均值和标准差；可以评估各种GIPF描述符和分子极性指数（MPI）；可以定位表面上映射函数的最小值和最大值；可以基于ESP计算特征区域（例如σ/π空穴和孤对电子）的面积；可以实现对分子表面上任意映射函数的类盆地分析。
* **处理网格数据（可以从.cub/.grd/.vti/.dx/CHGCAR...加载或由Multiwfn直接生成）。** 用户可以对网格数据执行非常丰富的数学运算，设置特定范围内的值，提取指定平面中的数据，绘制（局域）积分和平面平均曲线，执行平移等。
* **自适应自然密度划分（AdNDP）分析。** 界面是交互式的，AdNDP轨道可以直接可视化。可以获取AdNDP轨道的能量和轨道成分。
* **Fuzzy原子空间分析。** 支持Becke、Hirshfeld、Hirshfeld-I和MBIS原子空间划分方法，可以计算以下量：实空间函数在原子空间或原子空间重叠区域中的积分，原子/片段/分子的偶极矩和多极矩，原子多极矩，原子重叠矩阵（AOM），片段重叠矩阵（FOM），局域化和非局域化指数（LI, DI），片段间DI（IFDI）和片段LI（FLI），凝聚线性响应核，多中心DI，以及五个芳香性指数，即FLU、FLU-p、PDI、PLR和信息论芳香性指数。还可以根据Tkatchenko-Scheffler方法计算原子有效体积、自由体积、极化率和C6色散系数。
* **电荷分解分析（CDA）和扩展CDA分析。** 可以绘制轨道相互作用图。可以定义无限数量的片段。
* **盆地分析。** 可以为任何实空间函数定位吸引子，生成相应的盆地并同时可视化。可以在生成的盆地中积分所有实空间函数。可以计算盆地的电多极矩、盆地/原子重叠矩阵（BOM/AOM）、局域化指数（LI）和非局域化指数（DI）。可以获得原子对盆地布居的贡献。可以自动分配ELF盆地的标签。可以评估高ELF定域域布居和体积（HELP和HELV）。
* **电子激发分析：** 可视化和分析空穴-电子分布、跃迁密度、跃迁电/磁偶极矩和电荷密度差；计算空穴和电子之间的Coulomb吸引能（激子结合能）；计算Mulliken原子跃迁电荷和TrEsp（来自静电势的跃迁电荷）；将跃迁电/磁偶极矩分解为MO对贡献或基函数/原子贡献；通过JCTC, 7, 2498中提出的方法分析电荷转移；绘制原子/片段跃迁密度矩阵、跃迁偶极矩矩阵和电荷转移矩阵的热图；计算Δr指数 (JCTC, 9, 3118) 和Λ指数 (JCP, 128, 044118) 以揭示电子激发特性；计算激发态之间的跃迁电/磁偶极矩；生成自然跃迁轨道（NTOs）；计算ghost-hunter指数 (JCC, 38, 2151)；通过IFCT方法计算片段间电荷转移量；为一批激发态生成自然轨道；快速检查所有激发态的主要MO跃迁；绘制电荷转移谱 (Carbon, 187, 78)；基于电子激发的电子密度极化分析 (JPCA, 124, 633)；计算手性体系的ECD/CPL不对称因子 (g)。
* **轨道定域化分析：** 支持Pipek-Mezey（基于Mulliken、Löwdin或Becke布居）和Foster-Boys定域化方法。可以推导所得LMOs的成分、能量和偶极矩，可以轻松可视化LMOs的形状和中心。此外，基于LMOs，可以通过LOBA方法 (PCCP, 11, 11297) 或修正的LOBA方法评估氧化态。
* **弱相互作用的可视研究：** 相互作用区域指示器（IRI和IRI-π，Chem.-Methods, 1, 231）；RDG/NCI方法 (JACS, 132, 6498)；aNCI方法（波动环境中的非共价相互作用分析，JCTC, 9, 2226）；DORI方法 (JCTC, 10, 3745)；独立梯度模型（IGM）方法 (PCCP, 19, 17928)；基于Hirshfeld分子密度划分的IGM（IGMH）(JCC, 43, 539)；修正的IGM（mIGM，Struct. Bond., 190, 297）；平均IGM和平均修正IGM（aIGM和amIGM，Struct. Bond., 190, 297）。可以对这些实空间函数等值面包围的各个区域进行积分以进行定量分析。还支持Becke和Hirshfeld表面分析以及指纹分析。可以可视化范德华势 (J. Mol. Model., 26, 315) 并定位其极值。
* **概念密度泛函理论（CDFT）分析：** Fukui函数和双描述符，及其凝聚形式和轨道加权变体；Fukui势和双描述符势；Mulliken电负性；硬度；亲电性和亲核性指数；亲电描述符；软度；凝聚局域软度；相对亲电性和亲核性；亲电和亲核超离域度，键双描述符等。支持特定模型以适当处理（准）简并HOMO和LUMO的情况。
* **扩展跃迁态 - 化学价自然轨道（ETS-NOCV）：** 可以定义任意数量的片段，支持闭壳层和开壳层情况。可以获取NOCV特征值、能量和成分，许多相关函数可以作为等值面轻松可视化，包括NOCV轨道波函数、NOCV对密度、冻结态轨道、Pauli形变密度、轨道形变密度和总密度差。
* **能量分解分析：** sobEDA和sobEDAw (J. Phys. Chem. A, 127, 7023 (2023))，基于UFF/AMBER/GAFF分子力场的EDA（EDA-FF）；Shubin Liu能量分解（EDA-SBL）；原子对色散能贡献的分析和色散密度的评估。
* **电子离域和芳香性分析：** 多中心键级（MCBO），AV1245和AVmin；等化学屏蔽表面（ICSS）；非平面或倾斜体系的NICS_ZZ；ELF-π和ELF-σ；谐振子芳香性度量（HOMA）和Bird指数；重新参数化的HOMA（HOMAc和HOMER指数）；Shannon芳香性指数；对位离域指数（PDI）；芳香性涨落指数（FLU）和FLU-π；对位线性响应指数（PLR）；信息论（ITA）芳香性指数；环临界点性质；NICS-1D扫描曲线图；积分NICS（INICS）和FiPC-NICS指数；NICS-2D扫描平面图等。
* **（超）极化率研究：** 解析Gaussian“polar”任务的输出文件并计算许多与（超）极化率相关的数据；计算与Hyper-Rayleigh散射（HRS）相关的量；绘制（超）极化率密度；获取原子对（超）极化率的贡献；通过求和态（SOS）方法计算（超）极化率；两能级和三能级模型分析；（超）极化率张量的单位球和矢量表示；计算分子中的原子极化率。
* **结构和几何相关分析：** 分子范德华（vdW）体积；整个体系或单个片段的vdW表面积；分子长/高/宽，vdW直径和动力学直径；空腔体积和直径；原子间连接性和原子配位数；原子团簇的平均键长；键长交替（BLA）、键级交替（BOA）以及键角和二面角交替；分子平面性参数（MPP）和平面偏差跨度（SDP）；可视化和评估晶胞中的自由区域（孔隙）及其体积；非常丰富的几何操作；绘制表面距离投影图；两个片段之间的最小/最大和几何/质心距离；特定环的面积和周长。
* **其他功能（不完全列表）：** 通过Becke多中心方法在全空间积分实空间函数；评估alpha和beta轨道之间的重叠积分；评估两个轨道之间的重叠和质心距离；通过组合片段波函数生成新波函数；计算LOLIPOP指数；计算分子间轨道重叠；Yoshizawa的电子传输路径分析；在Hilbert空间中计算原子和键偶极矩；为实空间函数绘制径向分布函数；计算两个不同波函数中轨道之间的重叠积分；输出轨道之间的各种积分；评估实空间函数的一阶和二阶矩以及回转半径；将加载的结构/波函数导出为许多流行格式，如.wfn、.wfx、.molden、.fch、NBO .47、.pdb、.xyz，并为许多已知的量子化学代码生成输入文件；计算键极性指数（BPI）；域分析（在实空间函数定义的等值面内获取性质）；计算电子相关指数；检测π轨道并评估轨道的π成分；在alpha和beta轨道之间执行双正交化以最大程度地配对它们；评估核-价电子分叉（CVB）指数；评估轨道对密度差（例如Fukui函数）或其他类型网格数据的贡献；键级密度（BOD）和自然自适应轨道（NAdO）分析；将原子径向密度拟合为STO或GTF；模拟扫描隧道显微镜（STM）图像；评估电偶极/四极/八极/十六极矩和电子空间延展度等。

**Multiwfn支持的实空间函数**

实空间函数分析是Multiwfn最强大的功能之一，支持超过100种实空间函数，列表如下，详细描述可在手册第2.6和2.7节中找到：

* 电子密度
* 电子密度梯度范数
* 电子密度Laplacian
* 轨道的波函数值和概率密度
* 电子自旋密度
* Hamiltonian动能密度 K(r)
* Lagrangian动能密度 G(r)
* Becke定义的电子定域化函数 (ELF) 和Tsirelson定义的ELF
* Becke定义的定域轨道定位符 (LOL) 和Tsirelson定义的LOL
* 相互作用区域指示器 (IRI) 和IRI-π
* 独立梯度模型 (IGM) 中定义的δg函数以及基于Hirshfeld划分的IGM (IGMH)
* 局域信息熵
* 静电势 (ESP)，以及来自核/电子/原子电荷的ESP
* 范德华势
* 带/不带分子态近似的约化密度梯度 (RDG)
* 带/不带分子态近似的sign(λ2)ρ（电子密度Hessian矩阵的第二大特征值符号与电子密度的乘积）
* 交换相关密度、相关空穴和相关因子
* 平均局域电离能 (ALIE) 和局域电子附着能 (LEAE)
* 源函数
* 电子离域范围函数 EDR(r;d) 和轨道重叠距离函数 D(r)
* 其他（不完全列表）：势能密度、电子能量密度、轨道加权Fukui函数和双描述符、强共价相互作用指数 (SCI) 、超强相互作用 (USI) 、成键和非共价相互作用 (BNI) 、局域电子亲和能/电负性/硬度、电子密度椭圆度和刚度、eta指数、on-top pair density、多种形式的DFT交换相关势、多种形式的DFT动能密度、Weizsäcker势、Fisher信息熵、Ghosh/Shannon熵密度、Rényi熵的被积函数、形状函数、局域温度、键金属性、线性响应核、位阻能/势/电荷、Pauli势/力/电荷、量子势/力/电荷、PAEM、密度重叠区域指示器 (DORI) 、慢电子区域 (RoSE) 、PS-FID、单指数衰减检测器 (SEDD) 、电子线动量密度、电/磁偶极矩密度、局域电子相关函数、电场强度、应力张量刚度、应力张量极化率、分数占据数加权电子密度 (FOD) 等。

在Multiwfn中实现一个新的实空间函数非常容易，如手册第2.7节所示。

**Multiwfn能做的事情**

Multiwfn对不同主题支持的分析简要列举如下，您可以通过搜索“Multiwfn快速入门.pdf”文档轻松找到相关手册章节。当您感到困惑时，不要忘记在Multiwfn官方论坛提问！

* **可视化各种程序生成的各种形式的轨道**
* **表征化学键：** 各种形式的AIM分析；研究实空间函数（ELF、LOL、∇²ρ、动能/势能密度、IRI和IRI-π、价电子密度、片段密度差、形变密度、源函数、键椭圆度、键度、eta指数、V(r)/G(r)、SCI、PAEM、IGM...）；各种键级分析（Mayer、Laplacian、Mulliken、Wiberg、Fuzzy和多中心键级，以及Mayer、Mulliken和Wiberg键级的分解分析）；固有键强度指数（IBSI）；定域化/非定域化指数；轨道定域化分析；键级密度（BOD）和自然自适应轨道（NAdO）分析；各种测量键极性和键偶极矩的方法；电荷分解分析（CDA）；扩展跃迁态 - 化学价自然轨道（ETS-NOCV）；重叠布居态密度（OPDOS）；能量分解分析等。概述请参见手册4.A.11节。还可以通过shell脚本轻松研究扫描和IRC过程中化学键各种性质的变化，请参见手册4.A.1节。
* **表征电子分布和变化：** 原子电荷（AIM、Mulliken、SCPA、Hirshfeld、Hirshfeld-I、Voronoi、Löwdin、ADCH、CM5、MBIS、EEM、CHELPG、MK、RESP、RESP2...）；基函数/壳层/原子/片段的总和自旋布居分析；原子电偶极矩和多极矩分析（也可以通过Multiwfn提供的绘图脚本在VMD程序中可视化）；绘制密度差的图 / 盆地分析 / 域分析；电荷位移曲线。
* **芳香性和电子离域分析：** 概述请参见手册4.A.3节。
* **表征分子内和分子间弱相互作用：** AIM分析（键径可视化和键临界点各种性质的分析）；弱相互作用的可视化分析（NCI、IGM、IGMH、aIGM、IRI、DORI）；基于IGM或IGMH的原子和原子对δg指数；静电势（ESP）的定量分子表面分析；以各种形式绘制ESP；绘制范德华势；基于力场的能量分解分析（EDA-FF）；Hirshfeld/Becke表面分析；LOLIPOP；相互穿透距离和穿透体积分析；原子电荷和多极矩分析；电荷转移分析（密度差图、CDA、布居变化...）；ELF和核-价电子分叉（CVB）指数等。概述请参见手册4.A.5节。
* **电子激发分析：** 空穴和电子分析（分布、原子/片段/轨道贡献、质心位置、位移和重叠、激子结合能）；电荷转移分析（IFCT、密度差...）；NTO；关键MO之间的重叠和质心距离；绘制原子/片段跃迁密度矩阵和电荷转移矩阵；Δr指数；跃迁偶极矩分解为基函数/原子/片段/MO对贡献；各种激发态之间的跃迁偶极矩；跃迁原子电荷；ghost-hunter指数；揭示激发过程中电子结构（键合和布居）的变化；打印所有激发态的主要MO跃迁；绘制电荷转移谱以图形方式揭示UV-Vis光谱的本质等。概述请参见手册4.A.12节。
* **预测反应位点和反应性分析：** 分子表面上的ESP和ALIE分析；原子电荷；前线分子轨道的轨道成分分析；π电子布居；轨道重叠距离函数分析；自动计算概念密度泛函理论框架中定义的所有量；评估轨道（MO、NBO、NAO等）对Fukui函数的贡献。概述请参见手册4.A.4节。
* **预测分子凝聚相性质：** 使用vdW表面上的ESP分布经验性地预测汽化热、升华热、分子晶体密度、沸点、熔化热、表面张力、pKb等。可以量化分子极性。请参见手册第3.15.1节。
* **绘制光谱：** IR、Raman、UV-Vis、ECD、VCD、ROA、NMR和光电子能谱。在UV-Vis的情况下，可以精确预测显示的颜色。
* **表征几何结构**
* **(超)极化率研究**
* **导电分析：** TDOS和PDOS；相邻单体之间的轨道重叠分析；Yoshizawa的传输路径分析；键长/键级交替（BLA/BOA）。
* **许多其他功能：** 结构化学教学；模拟扫描隧道显微镜（STM）图像；转换包含几何或波函数信息的文件格式；研究电子相关效应；实现对DFT泛函的ELF-tuning和LOL-tuning；通过LOBA或修正的LOBA方法评估氧化态；研究实空间函数的分布（以径向分布函数、质心、一阶和二阶矩、全空间和局域区域积分的形式...）；评估分子轨道中的σ或π成分，几何变换等。

**引用Multiwfn**

如果您的研究中使用了Multiwfn，至少必须在正文中引用以下论文，这些是Multiwfn程序的原始论文：

* Tian Lu, Feiwu Chen, Multiwfn: A Multifunctional Wavefunction Analyzer, J. Comput. Chem. 33, 580-592 (2012) DOI: 10.1002/jcc.22885
* Tian Lu, A comprehensive electron wavefunction analysis toolbox for chemists, Multiwfn, J. Chem. Phys., 161, 082503 (2024) DOI: 10.1063/5.0216272

根据您在工作中使用的方法和功能，可能还需要引用我的其他论文。请仔细检查Multiwfn软件包中的“How to cite Multiwfn.pdf”文档。只要有可能，请在正文中提及并引用Multiwfn，而不是在补充信息中，否则不仅读者难以注意到Multiwfn，而且论文也不会被纳入引用统计。

**讨论区**

有两个Multiwfn官方论坛，使用不同的语言。您可以在任何一个论坛中讨论关于Multiwfn和波函数分析的任何内容。如果您在使用Multiwfn时遇到问题，请随时在这些论坛上发帖！

* Multiwfn英文论坛： http://sobereva.com/wfnbbs
* Multiwfn中文论坛： http://bbs.keinsci.com/wfn

顺便提一下：Multiwfn的YouTube频道包含一些有价值的Multiwfn演示视频，强烈建议查看它们并订阅该频道。


---
## 🤖 deepseek-v4-flash

好的，这是Multiwfn手册第二章“2 General information”（一般信息）中第2.1至2.5节的完整中文翻译。

---

**2 一般信息**

**2.1 安装**

**2.1.1 Windows版本**

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
