import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crea la figura e l'asse
fig, ax = plt.subplots(figsize=(8, 8))

# Aggiungi i rettangoli per le zone
# Area tranquilla (blu chiaro)
quiet_area = patches.Rectangle((0.1, 0.1), 0.6, 0.4, facecolor='lightblue', edgecolor='black', label="Quiet Area")
ax.add_patch(quiet_area)

# Area musica live (verde)
live_music_area = patches.Rectangle((0.1, 0.6), 0.4, 0.3, facecolor='lightgreen', edgecolor='black', label="Live Music Area")
ax.add_patch(live_music_area)

# Area sociale (giallo)
social_area = patches.Rectangle((0.6, 0.6), 0.3, 0.3, facecolor='yellow', edgecolor='black', label="Social Area")
ax.add_patch(social_area)

# Aggiungi etichette per ogni zona
ax.text(0.4, 0.3, 'Quiet Area\n(For noise-sensitive customers)', fontsize=12, ha='center', va='center')
ax.text(0.3, 0.75, 'Live Music Area\n(Higher noise levels)', fontsize=12, ha='center', va='center')
ax.text(0.75, 0.75, 'Social Area\n(Moderate background noise)', fontsize=12, ha='center', va='center')

# Imposta i limiti, titolo e nascondi gli assi
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('Conceptual Design of Acoustically Optimized Dining Area', fontsize=14)
ax.axis('off')

# Aggiungi una legenda
handles = [patches.Patch(color='lightblue', label='Quiet Area'),
           patches.Patch(color='lightgreen', label='Live Music Area'),
           patches.Patch(color='yellow', label='Social Area')]
ax.legend(handles=handles, loc='upper right')

# Mostra il grafico
plt.tight_layout()

fig.savefig('dining_area.pdf')
plt.show()
