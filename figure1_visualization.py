import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Setup the Plot
fig, ax = plt.subplots(figsize=(12, 4), dpi=300) # Adjusted height since title is gone
ax.set_xlim(0, 12)
ax.set_ylim(0, 5) # Adjusted limit
ax.axis('off')

# 2. Helper Functions
def draw_box(x, y, width, height, title, details, color='white', edge='black'):
    # Shadow
    shadow = patches.FancyBboxPatch((x+0.05, y-0.05), width, height, boxstyle="round,pad=0.1", 
                                    ec="none", fc='gray', alpha=0.3)
    ax.add_patch(shadow)
    # Main Box
    box = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                 ec=edge, fc=color, linewidth=1.5)
    ax.add_patch(box)
    # Text
    ax.text(x + width/2, y + height - 0.4, title, ha='center', va='center', 
            fontsize=11, fontweight='bold', color='black')
    ax.text(x + width/2, y + height/2 - 0.3, details, ha='center', va='center', 
            fontsize=9, color='black', linespacing=1.4)

def draw_arrow(x_start, y_start, x_end, y_end):
    ax.annotate('', xy=(x_end, y_end), xytext=(x_start, y_start),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))

# 3. Draw Stages
# Stage 1
draw_box(0.5, 1.5, 2.0, 2.0, "1. Data Collection", "ICMR Anthropometry\nRural India Survey\n(Height, Weight, BMI)")
draw_arrow(2.7, 2.5, 3.3, 2.5)

# Stage 2
draw_box(3.3, 1.5, 2.0, 2.0, "2. Biomechanical\nModeling", "SymPy Equations\nHalo Ring Design\nStress Calculation")
draw_arrow(5.5, 2.5, 6.1, 2.5)

# Stage 3
draw_box(6.1, 1.5, 2.0, 2.0, "3. FEA Simulations", "FreeCAD Analysis\nLoad Distribution Curves\nStress < 50 MPa")
draw_arrow(8.3, 2.5, 8.9, 2.5)

# Stage 4
draw_box(8.9, 1.5, 2.0, 2.0, "4. Evolutionary\nOptimization", "NEAT / SciPy\nGenetic Algorithms\nFitness > 45")

# Feedback Loop Arrow
ax.annotate('', xy=(4.3, 3.7), xytext=(7.1, 3.7),
            arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=0.4", color='black', lw=1.5))
ax.text(5.7, 3.8, "Design Refinement\n(Add 45° Elbows)", ha='center', fontsize=9, color='black')

# 4. Save (NO TITLE)
plt.tight_layout()
plt.savefig('fig1.png', bbox_inches='tight')
plt.show()
