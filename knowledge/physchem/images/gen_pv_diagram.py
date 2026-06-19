import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Use Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'KaiTi']
plt.rcParams['axes.unicode_minus'] = False

# PV diagram: Isothermal vs Adiabatic
V0, p0 = 1.0, 5.0
gamma = 5/3

C_iso = p0 * V0
C_ad = p0 * V0**gamma

V = np.linspace(V0, 5.0, 500)
p_iso = C_iso / V
p_ad = C_ad / V**gamma

fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(V, p_iso, 'r--', linewidth=2, label='等温过程')
ax.plot(V, p_ad, 'b-', linewidth=2, label='绝热过程')

ax.scatter([V0], [p0], color='black', zorder=5)
ax.annotate(r'$(V_0, p_0)$', xy=(V0, p0), xytext=(V0+0.3, p0+0.2),
            fontsize=11, arrowprops=dict(arrowstyle='->', color='gray'))

# Vertical line showing the difference at a specific volume
V_mid = 3.0
p_iso_mid = C_iso / V_mid
p_ad_mid = C_ad / V_mid**gamma
ax.plot([V_mid, V_mid], [p_ad_mid+0.05, p_iso_mid-0.05], 'k-', linewidth=0.8)
ax.annotate('Adiabatic\nsteeper', xy=(V_mid+0.15, (p_iso_mid+p_ad_mid)/2),
            fontsize=9, color='gray', ha='left', va='center')

ax.set_xlabel('Volume $V$', fontsize=13)
ax.set_ylabel('Pressure $p$', fontsize=13)
ax.set_title('等温过程与绝热过程的 P-V 图', fontsize=14, fontweight='bold')
ax.legend(fontsize=12, loc='upper right')
ax.set_xlim(0.8, 5.3)
ax.set_ylim(0, p0+1)
ax.grid(True, alpha=0.3)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(out_dir, 'isothermal_vs_adiabatic_PV.png')
plt.savefig(filepath, dpi=150, bbox_inches='tight')
print(f'Saved to: {filepath}')
