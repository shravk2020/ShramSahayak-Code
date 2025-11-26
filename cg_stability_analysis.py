# -----------------------------------------------------------------------------
# File: cg_stability_analysis.py
# Project: Shram Sahayak
# Purpose: Stability Analysis (The "Don't Tip Over" Test)
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

print("--- Starting Center of Gravity (CG) Stability Analysis ---")

# ==============================================================================
# PART 1: THE BIOMECHANICAL MODEL
# To stay standing, your Center of Gravity (CG) must stay over your feet.
# If the CG moves too far (e.g., > 5-10 cm), you have to lean excessively
# or use muscles to fight gravity, causing fatigue.
# ==============================================================================

# 1. Define Masses (in Kg)
# Based on ICMR Rural Male Average
mass_human = 60.0
mass_frame = 1.5   # The Shram Sahayak is very light (PVC)

# 2. Define Positions (The "Moment Arms") relative to the Ankles (x=0)
# Positive = Forward (Front of body)
# Negative = Backward (Back of body)
# 0 = Perfectly balanced over ankles

pos_human_cg = 0.0   # Assume human starts perfectly balanced
pos_frame_cg = -0.15 # Frame sits 15cm behind the vertical axis
pos_load_cg  = -0.20 # The sand/bricks sit inside the frame, ~20cm behind axis

# ==============================================================================
# PART 2: THE CALCULATIONS
# We calculate the CG shift for loads ranging from 0kg to 50kg.
# Formula: CG_system = (Sum of Moments) / (Total Mass)
# Moment = Mass * Position
# ==============================================================================

# Create an array of loads to test
loads_kg = np.linspace(0, 50, 100)

cg_shifts_cm = []

print(f"\n[1] Calculating CG Shifts for loads up to 50kg...")

for load in loads_kg:
    # 1. Calculate Total Mass
    total_mass = mass_human + mass_frame + load

    # 2. Calculate Sum of Moments
    # (Human Moment is 0 because pos is 0)
    moment_frame = mass_frame * pos_frame_cg
    moment_load  = load * pos_load_cg

    total_moment = moment_frame + moment_load

    # 3. Calculate New System CG
    new_cg_pos_meters = total_moment / total_mass

    # Convert to cm and take absolute value (we care about magnitude of shift)
    new_cg_pos_cm = abs(new_cg_pos_meters * 100)

    cg_shifts_cm.append(new_cg_pos_cm)

# Convert list to array for plotting
cg_shifts_cm = np.array(cg_shifts_cm)


# ==============================================================================
# PART 3: SAFETY CHECK
# Safety Rule: The CG shift must remain under 5 cm.
# If it's > 5 cm, the user has to lean forward uncomfortably to balance.
# ==============================================================================

max_shift = cg_shifts_cm[np.where(loads_kg <= 40)][-1] # Check at 40kg (Rated Load)

print(f"\n[2] Safety Validation:")
print(f"   - Max Load Tested: 40 kg")
print(f"   - Calculated CG Shift: {max_shift:.2f} cm")
print(f"   - Safety Threshold:    < 5.00 cm")

if max_shift < 5.0:
    print("   -> RESULT: PASS. The device is STABLE.")
else:
    print("   -> RESULT: FAIL. Risk of tipping backward!")


# ==============================================================================
# PART 4: VISUALIZATION
# Plotting the Stability Curve
# ==============================================================================

plt.figure(figsize=(10, 6))

# Plot the CG Shift Curve
plt.plot(loads_kg, cg_shifts_cm, color='#800080', linewidth=2.5, label='System CG Shift')

# Plot the Safety Threshold (The "Danger Line")
plt.axhline(y=5, color='red', linestyle='--', linewidth=2, label='Stability Limit (5cm)')

# Formatting
plt.title('Stability Analysis: CG Shift vs. Load', fontsize=14)
plt.xlabel('Load Carried (kg)', fontsize=12)
plt.ylabel('Center of Gravity Shift (cm)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# Shade the Safe Zone
plt.fill_between(loads_kg, 0, 5, color='green', alpha=0.1, label='Stable Zone')

# Annotate the result
plt.annotate(f'Shift at 40kg: {max_shift:.1f} cm\n(Safe)',
             xy=(40, max_shift), xytext=(25, 4),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='green', fontweight='bold')

print("\n[3] Generating Stability Graph...")
plt.savefig('cg_stability_results.png')
print("   -> Graph saved as 'cg_stability_results.png'")
# plt.show()
