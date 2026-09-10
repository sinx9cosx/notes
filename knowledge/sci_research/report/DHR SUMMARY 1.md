---
tags:
  - 计算化学
  - research
Category:
  - 总结
---
# DHR 反-Kasha 发光复现：进展与待解决问题

日期：2026-09-10

## 一、总体进展

  
目前，S1（最低激发态）已完成全链计算，发射峰 647 nm 与文献 658 nm 相差 11 nm；文献所指的高态发光初步判断为 S9（第九激发态），光谱与辐射速率已完成，但发射峰与文献不符，内转换速率因问题暂缺。

## 二、方法与工作内容

计算使用 Gaussian 16 完成几何优化与激发态计算（CAM-B3LYP/6-31G(d,p)，scrf，em=gd3bj），荧光光谱、辐射速率与内转换速率由 MOMAP 2022B 计算。

## 三、主要结果

### 光谱计算

| 态   | 计算发射峰  | 文献发射峰  | 辐射速率 kr     | 内转换速率 kic    | 量子产率  | 寿命          |
| --- | ------ | ------ | ----------- | ------------ | ----- | ----------- |
| S1  | 648 nm | 658 nm | 4.3×10⁷ s⁻¹ | 1.3×10¹⁰ s⁻¹ | ≈0.3% | ≈74 ps（总寿命） |
| S9  | 299nm  | 394 nm | 4.1×10⁸ s⁻¹ | 暂缺           | —     | —           |

  ![[DHR-spec.png]]

S1 内转换速率远大于辐射速率，发光效率低。
S9 为强跃迁态，计算辐射速率 4.1×10⁸ s⁻¹（辐射寿命 2.45 ns）；但发射峰与文献绿线相差约 1 eV。

### NTO分析

s1结果：0.98422 
由一对空穴->电子轨道贡献
97（空穴轨道）->98（电子轨道）：
  <table><tr>
  <td align="center"><img src="DHR-s1-NTO-97.jpg" width="380"><br>97空穴</td>
  <td align="center"><img src="DHR-s1-NTO-98.jpg" width="380"><br>98电子</td>
  </tr></table>


s9结果：主要由3对轨道gong'xi
97->98(0.73127)

  <table><tr>
  <td align="center"><img src="DHR-s9-97.jpg" width="380"><br>97空穴</td>
  <td align="center"><img src="DHR-s9-98.jpg" width="380"><br>98电子</td>
  </tr></table>

96->99(0.14587)

  <table><tr>
  <td align="center"><img src="DHR-s9-96.jpg" width="380"><br>96空穴</td>
  <td align="center"><img src="DHR-s9-99.jpg" width="380"><br>99电子</td>
  </tr></table>

95->100(0.08428)

  <table><tr>
  <td align="center"><img src="DHR-s9-95.jpg" width="380"><br>95空穴</td>
  <td align="center"><img src="DHR-s9-100.jpg" width="380"><br>100电子</td>
  </tr></table>
## 四、遇到的问题

1. S9 的内转换速率无法计算：该速率需要Gaussian的nacme计算，而程序始终未能生成 S9 对应的量——已产出的输出中，要么只有最低激发态的版本，要么缺少该内容，部分尝试直接报错；已调整计算设置尝试 5 种方案，均未成功。

2. S9 发射峰与文献相差约 1 eV：计算值 298 nm，文献绿线 394 nm；且文献绿线所处的能量在已算出的激发态能级中没有对应态，发光态归属需对照文献重新核对。

3. 可能需要注意的地方：S9 附近存在另一个能量非常接近的激发态，几何优化中两者能量次序发生过交换，发光态的指认需要更谨慎。

> [!note]
> opt2 优化跟踪的 root9 是 94→98 弱态（f≈0.15），freq/td/nacme（？） 锚定的是 95→99 强态（f≈0.6–1.2），两者近简并、opt 期间态序抖动；发光 S9 判定为 95→99 型。