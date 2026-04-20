import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV
try:
    df = pd.read_csv('forces.csv')
except FileNotFoundError:
    print("Error: forces.csv not found. Please run the C++ program first.")
    exit(1)

# Separate individual forces and resultant
# Using the updated 'label' column
forces = df[df['label'] != 'Resultant'].copy()
resultant = df[df['label'] == 'Resultant'].iloc[0]

fig, ax = plt.subplots(figsize=(10, 10))

# Plot each force vector from origin
origin = np.array([0, 0])
colors = plt.cm.tab10(np.linspace(0, 1, len(forces)))

for i, row in forces.iterrows():
    ax.annotate('', 
                xy=(row['fx'], row['fy']),
                xytext=origin,
                arrowprops=dict(arrowstyle='->', 
                               color=colors[i % len(colors)],
                               lw=2,
                               mutation_scale=20))
    # Offset label slightly to avoid overlap with arrow tip
    ax.text(row['fx']*1.1, row['fy']*1.1, 
            f"{row['label']}\n{row['magnitude']:.1f}N @ {row['angle']:.1f}°",
            fontsize=9, color=colors[i % len(colors)],
            ha='center', va='center')

# Plot resultant in black
ax.annotate('',
            xy=(float(resultant['fx']), float(resultant['fy'])),
            xytext=origin,
            arrowprops=dict(arrowstyle='->', color='black', lw=3, mutation_scale=25))
ax.text(float(resultant['fx'])*1.1, float(resultant['fy'])*1.1,
        f"RESULTANT\n{float(resultant['magnitude']):.1f}N\n@ {float(resultant['angle']):.1f}°",
        fontsize=11, fontweight='bold', color='black',
        ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# Formatting
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel('Fx (N)', fontsize=12)
ax.set_ylabel('Fy (N)', fontsize=12)
ax.set_title('2D Force System Visualization', fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)

# Set equal aspect ratio
ax.set_aspect('equal')

# Dynamically set limits to prevent clipping of labels
# Calculate max extent based on components
all_fx = df['fx'].tolist() + [0]
all_fy = df['fy'].tolist() + [0]
max_val = max(max(np.abs(all_fx)), max(np.abs(all_fy)))
limit = max_val * 1.3 
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

plt.tight_layout()
# Save the plot as well
plt.savefig('force_plot.png', dpi=300)
print("Plot saved as force_plot.png")
plt.show()
