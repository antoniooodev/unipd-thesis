import numpy as np

x_smooth = np.linspace(spl_values.min(), spl_values.max(), 300)
spl_values = np.array([20, 30, 40, 50, 60, 70])  # Example SPL values


traffic_wave = np.sin((x_smooth - 35) / 10) * 0.3 - 0.75
all_stimuli_wave = np.sin((x_smooth - 40) / 10) * 0.25 - 0.65
restaurant_wave = np.sin((x_smooth - 30) / 10) * 0.2 - 0.75

# Keeping confidence intervals for smoother curves within bounds as well
traffic_ci_low_wave = np.clip(traffic_wave - 0.3, -2, 0)
traffic_ci_high_wave = np.clip(traffic_wave + 0.3, -2, 0)

all_stimuli_ci_low_wave = np.clip(all_stimuli_wave - 0.25, -2, 0)
all_stimuli_ci_high_wave = np.clip(all_stimuli_wave + 0.25, -2, 0)

restaurant_ci_low_wave = np.clip(restaurant_wave - 0.2, -2, 0)
restaurant_ci_high_wave = np.clip(restaurant_wave + 0.2, -2, 0)

# For plot a), keeping a straight line
music_means_straight = np.linspace(-0.5, -1.5, len(spl_values))
music_ci_low_straight = np.linspace(-1, -2, len(spl_values))
music_ci_high_straight = np.linspace(0, -1, len(spl_values))

# Create the figure and axis objects again, focusing on all four subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot a) Music as a straight line
axs[0, 0].plot(spl_values, music_means_straight, label='Mean')
axs[0, 0].fill_between(spl_values, music_ci_low_straight, music_ci_high_straight, color='blue', alpha=0.3, label='95% CI')
axs[0, 0].set_title('a) Music')
axs[0, 0].set_ylabel('Relative food liking rating')
axs[0, 0].set_ylim(-2, 0)
axs[0, 0].legend()

# Plot b) Restaurant noise with wave-like curve
axs[0, 1].plot(x_smooth, restaurant_wave, label='Mean')
axs[0, 1].fill_between(x_smooth, restaurant_ci_low_wave, restaurant_ci_high_wave, color='blue', alpha=0.3, label='95% CI')
axs[0, 1].set_title('b) Restaurant noise')
axs[0, 1].set_ylim(-2, 0)

# Plot c) Road traffic noise with wave-like curve
axs[1, 0].plot(x_smooth, traffic_wave, label='Mean')
axs[1, 0].fill_between(x_smooth, traffic_ci_low_wave, traffic_ci_high_wave, color='blue', alpha=0.3, label='95% CI')
axs[1, 0].set_title('c) Road traffic noise')
axs[1, 0].set_ylabel('Relative food liking rating')
axs[1, 0].set_xlabel('SPL (dBA)')
axs[1, 0].set_ylim(-2, 0)

# Plot d) All stimuli with wave-like curve
axs[1, 1].plot(x_smooth, all_stimuli_wave, label='Mean')
axs[1, 1].fill_between(x_smooth, all_stimuli_ci_low_wave, all_stimuli_ci_high_wave, color='blue', alpha=0.3, label='95% CI')
axs[1, 1].set_title('d) All stimuli')
axs[1, 1].set_xlabel('SPL (dBA)')
axs[1, 1].set_ylim(-2, 0)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()