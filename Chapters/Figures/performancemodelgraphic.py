import matplotlib.pyplot as plt
import numpy as np

# Dati per il grafico
models = ['ANN-HHO', 'Traditional ANN', 'Statistical Mixed Models']
r2 = [0.70, 0.61, 0.42]
rmse = [0.80, 1.10, 1.80]
mae = [0.70, 0.80, 1.30]

# Impostazioni del grafico
width = 0.2  # Larghezza delle barre
x = np.arange(len(models))  # Posizione delle barre sull'asse x

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, r2, width, label='R²')
rects2 = ax.bar(x, rmse, width, label='RMSE')
rects3 = ax.bar(x + width, mae, width, label='MAE')

# Aggiungere etichette, titolo e legenda
ax.set_ylabel('Valore')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

fig.savefig('performancemodel.pdf')

plt.show()