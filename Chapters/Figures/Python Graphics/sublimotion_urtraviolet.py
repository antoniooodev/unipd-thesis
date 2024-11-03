import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def create_technical_section():
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
    
    # Room boundaries
    ax.plot([0, 10, 10, 0, 0], [0, 0, 5, 5, 0], 'k-', linewidth=2)
    
    # Table
    ax.fill([4, 6, 6, 4], [0, 0, 1, 1], color='gray', alpha=0.3)
    
    # Projectors
    projector_positions = [(2, 4), (8, 4)]
    for pos in projector_positions:
        ax.scatter(*pos, color='#2C3E50', s=100)
        
        # Projection beams
        angles = np.linspace(-30, 30, 50)
        for angle in angles[::5]:
            angle_rad = np.radians(angle)
            length = 3
            dx = length * np.cos(angle_rad)
            dy = length * np.sin(angle_rad)
            ax.plot([pos[0], pos[0] + dx], [pos[1], pos[1] - dy], 
                   color='#2C3E50', alpha=0.1)
    
    # Speakers
    speaker_positions = [(0.5, 4), (9.5, 4)]
    for pos in speaker_positions:
        ax.scatter(*pos, color='#34495E', s=100)
        
        # Sound waves
        circle_radii = [0.5, 1, 1.5]
        for radius in circle_radii:
            circle = plt.Circle(pos, radius, fill=False, 
                              color='#34495E', alpha=0.2)
            ax.add_artist(circle)
    
    # Labels
    ax.text(5, 0.5, 'Dining Area', ha='center', color='#2C3E50')
    ax.text(2, 4.3, 'Projector', ha='center', color='#2C3E50')
    ax.text(0.5, 4.3, 'Speaker', ha='center', color='#34495E')
    
    # Set limits and remove axes
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 6)
    ax.axis('off')
    
    # Title
    plt.title('Immersive Dining Environment - Technical Section', 
             pad=20, color='#2C3E50', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

# Create and save the figure
fig = create_technical_section()
plt.savefig('immersive_dining_section.png', 
            dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()