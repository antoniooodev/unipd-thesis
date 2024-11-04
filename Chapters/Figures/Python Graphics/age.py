import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data creation
data = {
    'Age Group': ['Young', 'Young', 'Adult', 'Adult', 'Senior', 'Senior'] * 2,
    'Noise Sensitivity': ['Low', 'High'] * 6,
    'Acoustic Condition': ['Low Noise'] * 6 + ['High Noise'] * 6,
    'Food Enjoyment': [8, 6, 7, 5, 6, 4, 5, 3, 6, 4, 5, 3]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(
    x='Age Group',
    y='Food Enjoyment',
    hue='Noise Sensitivity',
    ci=None,
    data=df[df['Acoustic Condition'] == 'Low Noise'],
    palette='muted'
)
plt.ylabel('Food Enjoyment (scale 1-10)')
plt.xlabel('Age Group')
plt.legend(title='Noise Sensitivity')
plt.ylim(0, 10)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(
    x='Age Group',
    y='Food Enjoyment',
    hue='Noise Sensitivity',
    ci=None,
    data=df[df['Acoustic Condition'] == 'High Noise'],
    palette='muted'
)
plt.title('Food Enjoyment Under High Noise Conditions')
plt.ylabel('Food Enjoyment (scale 1-10)')
plt.xlabel('Age Group')
plt.legend(title='Noise Sensitivity')
plt.ylim(0, 10)
plt.show()
