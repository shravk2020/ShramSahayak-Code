import matplotlib.pyplot as plt
import numpy as np

# Data
total_load = np.array([0, 10, 20, 30, 40])
neck_load_percent = np.array([100, 92.5, 85, 77.5, 70, 55, 40, 25, 10]) # For Fig 2
total_load_f2 = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40])
neck_load_kg = np.array([0, 4.5, 6.0, 5.5, 4.0]) # For Fig 3
waist_load_kg = total_load - neck_load_kg

# --- FIGURE 2 ---
plt.figure(figsize=(8, 6), dpi=300)
plt.plot(total_load_f2, neck_load_percent, 'k-o', linewidth=2, label='Neck Load %')
plt.title('Figure 2: Neck Load Percentage Reduction', fontsize=12)
plt.xlabel('Total Load (kg)')
plt.ylabel('Neck Load (%)')
plt.grid(True, linestyle=':', color='gray')
plt.ylim(0, 105)
plt.annotate('Without Frame', xy=(0, 100), xytext=(10, 95), arrowprops=dict(arrowstyle='->', facecolor='black'))
plt.annotate('With Frame', xy=(40, 10), xytext=(30, 25), arrowprops=dict(arrowstyle='->', facecolor='black'))
plt.savefig('fig2_neck_percentage_bw.png', bbox_inches='tight')
plt.close()

# --- FIGURE 3 ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)

# Plot A (Waist)
ax1.plot(total_load, waist_load_kg, 'k-o', label='Waist/Shoulder')
ax1.plot(total_load, total_load, 'k--', alpha=0.5, label='Total Weight Ref')
ax1.set_title('(a) Load on Waist (kg)', fontsize=12)
ax1.set_xlabel('Total Load (kg)')
ax1.set_ylabel('Load (kg)')
ax1.grid(True, linestyle=':', color='gray')
ax1.legend()

# Plot B (Neck)
ax2.plot(total_load, neck_load_kg, 'k-s', label='Neck Load')
ax2.plot(total_load, total_load, 'k--', alpha=0.5, label='Without Frame')
ax2.set_title('(b) Load on Neck (kg)', fontsize=12)
ax2.set_xlabel('Total Load (kg)')
ax2.set_ylabel('Load (kg)')
ax2.grid(True, linestyle=':', color='gray')
ax2.legend()

plt.tight_layout()
plt.savefig('fig3_load_kg_final_bw.png', bbox_inches='tight')
plt.show()
