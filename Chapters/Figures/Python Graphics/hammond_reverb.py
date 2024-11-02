import matplotlib.pyplot as plt
import numpy as np

def create_spring_reverb_diagram():
   fig, ax = plt.subplots(figsize=(10, 6))
   
   x = np.linspace(0, 10, 1000)
   y = 0.3 * np.sin(2 * np.pi * x)
   
   ax.plot(x, y, 'b-', linewidth=2)
   
   ax.add_patch(plt.Rectangle((-0.5, -0.5), 0.5, 1, color='gray'))
   ax.add_patch(plt.Rectangle((10, -0.5), 0.5, 1, color='gray'))
   
   plt.text(-0.5, -1, 'Input\nTransducer', ha='center')
   plt.text(10.25, -1, 'Output\nTransducer', ha='center')
   plt.text(5, 0.8, 'Spring', ha='center')
   
   ax.arrow(-1, 0, 0.3, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
   ax.arrow(10.5, 0, 0.3, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
   
   ax.set_xlim(-1.5, 11.5)
   ax.set_ylim(-1.5, 1.5)
   ax.set_xticks([])
   ax.set_yticks([])
   
   
   ax.spines['top'].set_visible(False)
   ax.spines['right'].set_visible(False)
   ax.spines['bottom'].set_visible(False)
   ax.spines['left'].set_visible(False)
   
   plt.tight_layout()
   return fig

fig = create_spring_reverb_diagram()
plt.savefig('hammond_reverb_diagram.png', dpi=300, bbox_inches='tight')
plt.show()