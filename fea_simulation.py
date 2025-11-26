# -----------------------------------------------------------------------------
# File: fea_simulation.py
# Project: Shram Sahayak
# Purpose: Biomechanical Stress Analysis (The "Will it Break?" Test)
# -----------------------------------------------------------------------------

import sympy as sp  # Use SymPy for the "Symbolic" math (like doing algebra on paper)
import numpy as np  # Use NumPy for the "Number Crunching" (calculating arrays of data)
import matplotlib.pyplot as plt # Use Matplotlib to visualize the results

print("--- Starting Shram Sahayak Structural Analysis ---")

# ==============================================================================
# PART 1: THE PHYSICS MODEL (Symbolic Math)
# We use Euler-Bernoulli Beam Theory here. We treat the PVC pipe as a beam
# that bends when a load is applied at the top.
# ==============================================================================

# 1. Define our Physics variables as symbols
# F = Force applied (Load)
# L = Length of the pipe (Moment arm)
# y = Distance from neutral axis (Outer radius of pipe)
# I = Moment of Inertia (Resistance to bending)
F, L, y, I = sp.symbols('F L y I')

# 2. Define the Formula for Bending Moment (M)
# Think of this like a wrench: Force x Distance.
# The further the load is from the support, the higher the bending moment.
M = F * L

# 3. Define the Formula for Bending Stress (sigma)
# This is the "Flexure Formula": sigma = (M * y) / I
# It tells us how much internal pressure is building up in the plastic.
stress_eq = (M * y) / I

print("\n[1] Derived Stress Equation:")
sp.pprint(stress_eq) # Prints the math formula neatly to the console


# ==============================================================================
# PART 2: REAL WORLD PARAMETERS
# Here we input the actual numbers for the Shram Sahayak Prototype.
# ==============================================================================

# Material: Schedule 40 PVC Pipe (1 inch)
# We assume the frame has 2 vertical supports sharing the load.

# Radius calculations (in meters)
outer_diameter_inch = 1.315 # Standard 1" PVC outer diameter
inner_diameter_inch = 1.049 # Standard 1" PVC inner diameter

# Convert inches to meters (Science uses Metric!)
R_outer = (outer_diameter_inch / 2) * 0.0254
R_inner = (inner_diameter_inch / 2) * 0.0254

# Beam Geometry
# Length of the vertical spine of the frame (approx 60cm or 0.6m)
length_m = 0.6

# MATERIAL LIMITS (The "Do Not Cross" Line)
# Yield Strength of PVC is approx 52 MegaPascals (MPa).
# If our stress crosses this number, the plastic deforms permanently (breaks).
YIELD_STRENGTH_PVC = 52 * 10**6  # 52,000,000 Pascals

print(f"\n[2] Simulation Parameters:")
print(f"   - Material: Schedule 40 PVC")
print(f"   - Yield Strength: {YIELD_STRENGTH_PVC / 10**6} MPa")
print(f"   - Spine Length: {length_m} m")


# ==============================================================================
# PART 3: THE NUMERICAL SIMULATION (The Stress Test)
# We will simulate loads from 20kg to 60kg to see how the frame behaves.
# ==============================================================================

# 1. Create an array of Loads (Mass in kg)
# np.linspace creates a list of numbers from 20 to 60
loads_kg = np.linspace(20, 60, 50)

# 2. Convert Mass to Force (Newtons)
# F = m * g (Gravity is 9.81 m/s^2)
# We divide by 2 because the frame has TWO vertical pipes sharing the weight!
force_newtons = (loads_kg * 9.81) / 2

# 3. Calculate Moment of Inertia (I) for a Hollow Tube
# Formula: I = (pi/4) * (R_outer^4 - R_inner^4)
# This number represents how "hard" it is to bend the tube shape.
I_val = (np.pi / 4) * (R_outer**4 - R_inner**4)

# 4. Calculate Stress for every load in our list
# sigma = (Force * Length * Radius) / I
stress_pascals = (force_newtons * length_m * R_outer) / I_val

# Convert Pascals to MegaPascals (MPa) so it's easier to read
stress_mpa = stress_pascals / 10**6


# ==============================================================================
# PART 4: VALIDATION & SAFETY CHECK
# Did we break the frame? Let's calculate the "Safety Factor".
# Safety Factor = Strength of Material / Actual Stress
# SF > 1 means Safe. SF > 2 means Very Safe. SF < 1 means CRACK!
# ==============================================================================

safety_factors = (YIELD_STRENGTH_PVC / 10**6) / stress_mpa

print("\n[3] Simulation Results (Sample):")
# Let's look at the result for the heaviest load (60kg)
print(f"   At MAX Load (60kg):")
print(f"   - Stress Generated: {stress_mpa[-1]:.2f} MPa")
print(f"   - PVC Limit:        52.00 MPa")
print(f"   - Safety Factor:    {safety_factors[-1]:.2f}")

if stress_mpa[-1] < 52:
    print("   -> RESULT: PASS. The frame will not break under 60kg.")
else:
    print("   -> RESULT: FAIL. The frame needs reinforcement!")


# ==============================================================================
# PART 5: VISUALIZATION
# Let's generate a graph like the ones in the paper to prove it works.
# ==============================================================================

plt.figure(figsize=(10, 6))

# Plot the Stress Curve (Blue Line)
plt.plot(loads_kg, stress_mpa, label='Frame Stress', color='blue', linewidth=2)

# Draw the "Danger Zone" Line (Red Dashed Line)
plt.axhline(y=52, color='red', linestyle='--', label='PVC Failure Limit (52 MPa)')

# Add labels and titles to make it look professional
plt.title('Structural Integrity Analysis: Shram Sahayak PVC Frame', fontsize=14)
plt.xlabel('Load Carried (kg)', fontsize=12)
plt.ylabel('Von Mises Stress (MPa)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# Highlight the safety margin
plt.fill_between(loads_kg, stress_mpa, 52, where=(stress_mpa < 52),
                 color='green', alpha=0.1, label='Safety Margin')

print("\n[4] Generating Stress Analysis Graph...")
# plt.show() # Uncomment this if running on your local machine
plt.savefig('fea_results_graph.png') # Saves the graph to a file
print("   -> Graph saved as 'fea_results_graph.png'")
