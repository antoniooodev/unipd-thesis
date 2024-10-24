import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_neural_brain(num_nodes=2000, connectivity=0.02):
    # Creiamo un grafo casuale per simulare la struttura della rete neurale
    G = nx.erdos_renyi_graph(num_nodes, connectivity)
    
    # Generiamo le posizioni dei nodi in uno spazio tridimensionale per dare l'idea di una forma cerebrale simmetrica
    pos = {}
    for i in range(num_nodes):
        hemisphere = 1 if i < num_nodes / 2 else -1  # Dividiamo i nodi in due emisferi
        theta = np.random.uniform(0, np.pi)  # Limitiamo theta per creare due lati distinti
        phi = np.random.uniform(0, np.pi)
        radius = np.random.uniform(0.8, 1.2)  # Leggero rumore per un aspetto più naturale
        
        x = hemisphere * radius * np.sin(phi) * np.cos(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(phi)
        
        pos[i] = (x, y, z)
    
    # Crea la figura e l'asse 3D
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot dei nodi con colori differenti per gli emisferi
    xs, ys, zs = zip(*pos.values())
    colors = ['skyblue' if i < num_nodes / 2 else 'lightcoral' for i in range(num_nodes)]
    ax.scatter(xs, ys, zs, color=colors, s=15, alpha=0.9)
    
    # Plot delle connessioni con maggiore densità
    for edge in G.edges():
        x_values = [pos[edge[0]][0], pos[edge[1]][0]]
        y_values = [pos[edge[0]][1], pos[edge[1]][1]]
        z_values = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x_values, y_values, z_values, color='black', alpha=0.05, linewidth=0.3)
    
    # Impostazioni per migliorare l'aspetto del grafico
    ax.set_axis_off()
    ax.set_title("Realistic Neural Network Inspired Brain Visualization", fontsize=18)
    plt.show()

# Genera il cervello con la rappresentazione della rete neurale
generate_neural_brain(num_nodes=2000, connectivity=0.02)
