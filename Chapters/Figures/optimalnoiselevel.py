import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Optimal noise ranges for different environments
ax.fill_between([30, 47], 0, 1, color='green', alpha=0.3, label='Music (30-47 dBA)')
ax.fill_between([30, 35], 1, 2, color='yellow', alpha=0.3, label='Restaurant Noise (~30 dBA)')
ax.fill_between([35, 40], 2, 3, color='orange', alpha=0.3, label='Traffic Noise (~35 dBA)')

# Add grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Vertical lines to highlight optimal points
ax.axvline(x=30, color='yellow', linestyle='-', linewidth=2)
ax.axvline(x=35, color='orange', linestyle='-', linewidth=2)
ax.axvline(x=47, color='green', linestyle='-', linewidth=2)

# Titles and labels
ax.set_title('Optimal Noise Levels for Different Dining Environments', fontsize=16)
ax.set_xlabel('Decibels (dBA)', fontsize=12)
ax.set_ylabel('Environment Type', fontsize=12)
ax.set_yticks([0.5, 1.5, 2.5])
ax.set_yticklabels(['Music', 'Restaurant Noise', 'Traffic Noise'])

# Set x-axis range
ax.set_xlim(20, 60)

# Add legend
music_patch = mpatches.Patch(color='green', alpha=0.3, label='Music (30-47 dBA)')
restaurant_patch = mpatches.Patch(color='yellow', alpha=0.3, label='Restaurant Noise (~30 dBA)')
traffic_patch = mpatches.Patch(color='orange', alpha=0.3, label='Traffic Noise (~35 dBA)')
ax.legend(handles=[music_patch, restaurant_patch, traffic_patch], loc='upper left')

# Add a note explaining the values
plt.figtext(0.5, -0.05, 'Optimal values determined by the ANN-HHO model', ha='center', fontsize=10, color='gray')

# Save the plot as PDF
plt.tight_layout()
plt.savefig("optimal_noise_levels_improved.pdf")
plt.show()
