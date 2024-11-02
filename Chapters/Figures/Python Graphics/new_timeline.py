import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

def create_curved_timeline():
    fig, ax = plt.subplots(figsize=(15, 8), facecolor='white')
    
    # Create curved line using Bezier curve
    t = np.linspace(0, 1, 100)
    x = np.linspace(1950, 1980, 100)
    # Create subtle wave effect
    y = 0.1 * np.sin(2 * np.pi * t)
    
    # Timeline data
    years = [1950, 1960, 1970, 1980]
    events = [
        'Early Reverberation',
        'Hammond Era',
        'Analog Innovation',
        'Digital Dawn'
    ]
    descriptions = [
        'First acoustic chambers',
        'Spring reverb systems',
        'Electronic processing',
        'Digital algorithms'
    ]
    
    # Color scheme
    line_color = '#1a2634'  # Dark navy
    point_color = '#2c3e50'  # Dark blue-gray
    text_color = '#2c3e50'  # Dark blue-gray
    
    # Plot curved timeline
    ax.plot(x, y, '-', color=line_color, linewidth=2, zorder=1)
    
    # Add events
    for i, (year, event, desc) in enumerate(zip(years, events, descriptions)):
        # Find y-coordinate on curve
        idx = np.abs(x - year).argmin()
        y_pos = y[idx]
        
        # Plot point
        ax.plot(year, y_pos, 'o', color=point_color, markersize=10, zorder=2)
        
        # Add year
        ax.text(year, y_pos - 0.15, str(year), 
                ha='center', va='top',
                color=text_color, fontsize=10, fontweight='bold')
        
        # Add event text alternating above and below
        text_y = y_pos + (0.2 if i % 2 == 0 else -0.2)
        
        # Add event name
        ax.text(year, text_y, event,
                ha='center', va='bottom' if i % 2 == 0 else 'top',
                color=text_color, fontsize=12, fontweight='bold')
        
        # Add description
        desc_y = text_y + (0.1 if i % 2 == 0 else -0.1)
        ax.text(year, desc_y, desc,
                ha='center', va='bottom' if i % 2 == 0 else 'top',
                color=text_color, fontsize=10, style='italic')
        
        # Add connecting lines
        ax.plot([year, year], [y_pos, text_y], '--', 
                color=point_color, alpha=0.3, linewidth=1)
    
    # Customize appearance
    ax.set_xlim(1945, 1985)
    ax.set_ylim(-0.5, 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Remove axis lines
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    
    plt.tight_layout()
    return fig

# Create and save the timeline
fig = create_curved_timeline()
plt.savefig('reverb_evolution_timeline.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()