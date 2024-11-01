import matplotlib.pyplot as plt
import numpy as np

operations = ["Interface Navigation", "Playlist Management", "Audio Playback"]
cpu_usage = [7.5, 7.5, 25]  # Average CPU usage in percentage
mem_usage = [150, 150, 150]  # Constant memory usage in MB

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Operations')
ax1.set_ylabel('CPU Usage (%)', color=color)
ax1.bar(operations, cpu_usage, color=color, alpha=0.7, label="CPU Usage")
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Memory Usage (MB)', color=color)  
ax2.plot(operations, mem_usage, color=color, marker='o', linestyle='--', linewidth=2, label="Memory Usage")
ax2.tick_params(axis='y', labelcolor=color)

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.tight_layout()
plt.show()
