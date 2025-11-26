import matplotlib.pyplot as plt
import numpy as np

# 1. Define the Data
generations = np.arange(1, 16) # Generations 1 to 15
avg_fitness = np.array([22.3, 24.1, 27.5, 29.8, 32.4, 34.2, 36.7, 38.5, 35.9, 
                        37.2, 39.8, 41.6, 38.9, 40.3, 42.1])
best_fitness = np.array([27.5, 29.3, 32.8, 35.1, 37.6, 39.4, 41.9, 43.7, 41.1, 
                         42.4, 44.9, 46.7, 44.0, 45.5, 47.2])

# 2. Setup the Plot
plt.figure(figsize=(9, 6), dpi=300)

# 3. Plot Lines
# Best Fitness (Champion) - Solid Black with Triangles
plt.plot(generations, best_fitness, marker='^', markersize=8, 
         linestyle='-', linewidth=2.5, color='black', 
         label='Best Fitness (Champion Design)')

# Average Fitness - Dashed Gray with Circles
plt.plot(generations, avg_fitness, marker='o', markersize=6, 
         linestyle='--', linewidth=2, color='#666666', 
         label='Average Population Fitness')

# 4. Formatting
plt.xlabel('Generation', fontsize=12, color='black')
plt.ylabel('Fitness Score (Composite Metric)', fontsize=12, color='black')
plt.grid(True, linestyle=':', alpha=0.6, color='gray')
plt.xticks(generations, color='black')
plt.yticks(color='black')
plt.ylim(20, 50)

# 5. Annotations
plt.annotate('Initial Random Population', xy=(1.0, 22.3), xytext=(3, 22),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, color='black')

plt.annotate('Converged Optimal Design\n(Fitness: 47.2)', xy=(15, 47.2), xytext=(10, 48),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='black', fontweight='bold')

# Legend
plt.legend(loc='lower right', fontsize=10, frameon=True, fancybox=True, shadow=True)

# 6. Save
plt.tight_layout()
plt.savefig('fig5_fitness_evolution.png', bbox_inches='tight')
print("Figure 6 generated")
plt.show()
