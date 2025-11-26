import matplotlib.pyplot as plt
import numpy as np

# 1. Define the Data (Exact values from your Results section)
simulations = np.arange(1, 11) # 1 to 10
stress_values = np.array([32.9, 34.9, 28.5, 42.1, 37.2, 29.8, 41.6, 26.4, 39.1, 30.7])
cg_shifts = np.array([2.9, 0.9, 3.5, 1.8, 4.2, 2.1, 3.8, 1.4, 4.0, 2.5])

# 2. Setup the Plot (Dual Axis)
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)

# --- Primary Axis (Left): Von Mises Stress ---
# Using light gray for bars with black edges for high contrast
color_stress_bar = '#D3D3D3' # Light Gray
color_stress_edge = 'black'

ax1.set_xlabel('FEA Simulation ID', fontsize=12, color='black')
ax1.set_ylabel('Von Mises Stress (MPa)', color='black', fontsize=12)

bars = ax1.bar(simulations, stress_values, color=color_stress_bar, edgecolor=color_stress_edge,
               alpha=1.0, width=0.6, label='Stress (MPa)')

ax1.tick_params(axis='y', labelcolor='black')
ax1.set_ylim(0, 60) # Give room for the limit line
ax1.set_xticks(simulations)

# Add Stress Limit Line (50 MPa)
# Using dashed black line
ax1.axhline(y=50, color='black', linestyle='--', linewidth=1.5)
ax1.text(0.5, 51, 'Safety Limit (50 MPa)', color='black', fontsize=9, fontweight='bold')

# --- Secondary Axis (Right): CG Shift ---
ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis

ax2.set_ylabel('Center of Gravity Shift (cm)', color='black', fontsize=12)

# Using black line with diamond markers
line = ax2.plot(simulations, cg_shifts, color='black', marker='D', markerfacecolor='white',
                markeredgewidth=1.5, linewidth=2, markersize=6, label='CG Shift (cm)')

ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylim(0, 6) # Give room for the limit line

# Add CG Stability Limit Line (5 cm)
# Using dotted black line to distinguish from the stress limit line
ax2.axhline(y=5, color='black', linestyle=':', linewidth=2.0)
ax2.text(8.5, 5.1, 'Stability Limit (5 cm)', color='black', fontsize=9, fontweight='bold')

# 3. Formatting
plt.title('Stress vs. Stability', fontsize=14, pad=15, color='black')
ax1.grid(True, axis='x', linestyle='-', alpha=0.3, color='gray')

# Combined Legend
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)

# 4. Save
plt.tight_layout()
output_file = 'fig5_fea_stress_cg_bw.png'
plt.savefig(output_file, bbox_inches='tight')
print(f"Successfully generated {output_file}")
plt.show()
