import pygraphviz as pgv

# Creazione del grafo utilizzando AGraph
G = pgv.AGraph(strict=False, directed=True)

# Aggiunta dei nodi al grafo con attributi migliorati
G.add_node("Remote Devices", shape="ellipse", style="filled", fillcolor="#ffebc6", fontsize=14, fontname="Helvetica")
G.add_node("Mopidy Server", shape="ellipse", style="filled", fillcolor="#ffcccc", fontsize=14, fontname="Helvetica")
G.add_node("Iris Web Client", shape="ellipse", style="filled", fillcolor="#b3d9ff", fontsize=14, fontname="Helvetica")
G.add_node("Snapcast Server", shape="ellipse", style="filled", fillcolor="#ffcccc", fontsize=14, fontname="Helvetica")
G.add_node("Server Raspberry Pi", shape="ellipse", style="filled", fillcolor="#ffcccc", fontsize=14, fontname="Helvetica")
G.add_node("Client R-Pi 1", shape="ellipse", style="filled", fillcolor="#ccffcc", fontsize=14, fontname="Helvetica")
G.add_node("Client R-Pi 2", shape="ellipse", style="filled", fillcolor="#ccffcc", fontsize=14, fontname="Helvetica")
G.add_node("Client R-Pi 3", shape="ellipse", style="filled", fillcolor="#ccffcc", fontsize=14, fontname="Helvetica")
G.add_node("Speaker 1", shape="ellipse", style="filled", fillcolor="#e0e0e0", fontsize=14, fontname="Helvetica")
G.add_node("Speaker 2", shape="ellipse", style="filled", fillcolor="#e0e0e0", fontsize=14, fontname="Helvetica")
G.add_node("Speaker 3", shape="ellipse", style="filled", fillcolor="#e0e0e0", fontsize=14, fontname="Helvetica")

# Aggiunta delle connessioni con attributi migliorati
G.add_edge("Remote Devices", "Mopidy Server", label="HTTP/HTTPS", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Remote Devices", "Iris Web Client", label="Control", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Mopidy Server", "Snapcast Server", label="Audio Stream", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Snapcast Server", "Client R-Pi 1", label="Sync Audio", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Snapcast Server", "Client R-Pi 2", label="Sync Audio", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Snapcast Server", "Client R-Pi 3", label="Sync Audio", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Client R-Pi 1", "Speaker 1", label="Audio Output", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Client R-Pi 2", "Speaker 2", label="Audio Output", fontsize=10, color="#666666", fontname="Helvetica")
G.add_edge("Client R-Pi 3", "Speaker 3", label="Audio Output", fontsize=10, color="#666666", fontname="Helvetica")

# Personalizzazione del layout per renderlo più estetico
G.graph_attr['rankdir'] = 'LR'  # Layout da sinistra a destra
G.graph_attr['splines'] = 'true'  # Connessioni più fluide e non lineari
G.graph_attr['nodesep'] = '1'  # Aumenta la distanza tra i nodi
G.graph_attr['ranksep'] = '1.5'  # Spazio tra livelli orizzontali

# Layout e output in formato immagine (es. PNG)
G.layout(prog='dot')
G.draw('improved_diagram.png')

print("Il diagramma è stato generato e salvato come 'improved_diagram.png'")
