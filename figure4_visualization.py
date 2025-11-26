import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Setup the Plot
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 7) # Adjusted limit
ax.axis('off')

# Helper function
def draw_phone(x, y, label, screen_color='#F5F5F5'):
    body = patches.FancyBboxPatch((x, y), 3, 6, boxstyle="round,pad=0.1", ec='#333333', fc='white', lw=2)
    ax.add_patch(body)
    screen = patches.Rectangle((x + 0.2, y + 0.8), 2.6, 4.8, ec='#CCCCCC', fc=screen_color)
    ax.add_patch(screen)
    ax.add_patch(patches.Circle((x + 1.5, y + 0.4), 0.15, fc='#EEEEEE', ec='#999999')) # Home btn
    ax.add_patch(patches.Circle((x + 1.5, y + 5.7), 0.05, fc='#333333')) # Camera
    ax.text(x + 1.5, y - 0.5, label, ha='center', fontsize=12, fontweight='bold', color='black')

# --- Screen 1 (a) ---
draw_phone(0.5, 0.5, "(a) Input & Upload")
ax.text(2.0, 4.5, "Shram Sahayak", ha='center', fontsize=10, fontweight='bold', color='black')
ax.add_patch(patches.Circle((2.0, 3.3), 0.6, fc='#D3D3D3'))
ax.add_patch(patches.Arc((2.0, 2.3), 1.8, 2.0, theta1=0, theta2=180, fc='#D3D3D3'))
btn1 = patches.FancyBboxPatch((1.0, 1.0), 2.0, 0.6, boxstyle="round,pad=0.05", fc='black', ec='none')
ax.add_patch(btn1)
ax.text(2.0, 1.2, "Take/Upload Selfie", ha='center', color='white', fontsize=9)

ax.annotate('', xy=(4.4, 3.5), xytext=(3.6, 3.5), arrowprops=dict(facecolor='black', shrink=0.05, width=2))

# --- Screen 2 (b) ---
draw_phone(4.5, 0.5, "(b) AI Analysis")
ax.text(6.0, 4.5, "Processing...", ha='center', fontsize=10, color='black')
ax.add_patch(patches.Circle((6.0, 3.0), 0.7, fc='none', ec='black', lw=1, linestyle='--'))
ax.plot([5.8, 6.2, 6.0, 5.7, 6.3], [3.2, 3.2, 3.0, 2.8, 2.8], 'o', color='black', markersize=3)
ax.plot([5.3, 6.7], [2.5, 2.5], '-', color='black', lw=1)
ax.text(6.0, 2.1, "Shoulder Width", ha='center', fontsize=7, color='black')
ax.text(6.0, 1.5, "Torso Length: 85cm", ha='center', fontsize=8, color='black')

ax.annotate('', xy=(8.4, 3.5), xytext=(7.6, 3.5), arrowprops=dict(facecolor='black', shrink=0.05, width=2))

# --- Screen 3 (c) ---
draw_phone(8.5, 0.5, "(c) Assembly Guide")
ax.text(10.0, 4.7, "Success!", ha='center', fontsize=10, fontweight='bold', color='black')
ax.text(10.0, 4.3, "Model: Size M", ha='center', fontsize=9, color='black')
pdf_doc = patches.Rectangle((9.3, 2.5), 1.4, 1.6, fc='white', ec='black')
ax.add_patch(pdf_doc)
ax.text(10.0, 3.3, "PDF", ha='center', fontsize=14, fontweight='bold', color='black')
ax.plot([9.5, 10.5], [3.0, 3.0], '-', color='black')
ax.plot([9.5, 10.5], [2.8, 2.8], '-', color='black')
btn3 = patches.FancyBboxPatch((9.0, 1.0), 2.0, 0.6, boxstyle="round,pad=0.05", fc='black', ec='none')
ax.add_patch(btn3)
ax.text(10.0, 1.2, "Download Guide", ha='center', color='white', fontsize=9)

# 4. Save (NO TITLE)
plt.tight_layout()
plt.savefig('fig4_app_screenshots.png', bbox_inches='tight')
print("Figure 4 generated without title.")
plt.show()
