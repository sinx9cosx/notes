---
tags:
  - research
  - 后处理
Category:
  - 笔记
---
# 操作步骤

## multiwfn

1. 把 `TBRs-s0td-full.fchk` 和 `TBRs-s0td-full.log` 放在同一个文件夹里。
2. 启动 Multiwfn，点击主菜单 `18 Electron excitation analysis`。
3. 在子菜单中选 `1`，然后输入 log 文件的路径。
4. 在输入“Perform the analysis for which excited state”时，输入 `4`。
5. 先检查屏幕上显示的两行：`Sum of square of excitation coefficients` 应约为 0.5，`Deviation` 应小于 0.001；如果该值大于 0.05，说明 log 的组态系数被截断，不要继续使用。
6. 在接下来的菜单中选 `3`，再选 `1`（Mulliken）。
7. 屏幕会列出每个非氢原子的 Hole/Electron 百分比；选 `2`，把数据导出成当前文件夹的 `he_atm.txt`。
8. 逐层选 `0` 返回，最后输入 `q` 退出。

## excel

然后用 Excel 把对应环上的原子加总：

- 完整薁的五元环：`6,10,13,28,37`
- 同一个薁的七元环：`3,6,7,10,20,22,26`
- 另一个五元环：`9,19,21,27,44`

把 Hole 列和 Electron 列分别加总即可喵。