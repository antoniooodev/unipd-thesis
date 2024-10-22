import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Funzione per aggiungere icone
def getImage(path, zoom=0.15):
    return OffsetImage(plt.imread(path), zoom=zoom)

# Dati
phases = ['Dataset\nImprovement', 'Real-time\nOptimization', 'Multi-modal\nIntegration', 'Advanced\nPersonalization', 'Advanced AI']
years = [2023, 2024, 2025, 2026, 2027]
icons = ['database.png', 'clock.png', 'multimodal.png', 'person.png', 'brain.png']

# Creazione del plot
fig, ax = plt.subplots(figsize=(15, 5))

# Colori per il gradiente
colors = plt.cm.Blues(np.linspace(0.3, 0.7, len(phases)))

# Creazione timeline
for i, (phase, year, icon, color) in enumerate(zip(phases, years, icons, colors)):
    ax.scatter(i, 0, s=50, color=color, zorder=2)
    ax.annotate(phase, (i, -0.15), ha='center', va='top', fontweight='bold', fontsize=10)
    ax.annotate(str(year), (i, 0.15), ha='center', va='bottom', fontsize=10)
    
    try:
        ab = AnnotationBbox(getImage(icon), (i, 0.4), frameon=False)
        ax.add_artist(ab)
    except FileNotFoundError:
        print(f"Icona non trovata: {icon}")

# Linea della timeline
ax.plot(range(len(phases)), [0] * len(phases), color='lightblue', linewidth=1.5, zorder=1)

# Personalizzazione del grafico
ax.set_ylim(-0.3, 0.6)
ax.set_xlim(-0.5, len(phases) - 0.5)
ax.axis('off')

plt.figtext(0.5, -0.05, "Note: Timeline represents estimated progression of model development and is subject to adjustment based on research outcomes.", 
            ha="center", fontsize=8, style='italic')

plt.tight_layout()
plt.savefig('improved_future_roadmap.png', dpi=300, bbox_inches='tight')
plt.show()