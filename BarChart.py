import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset into a DataFrame
iris = load_iris(as_frame=True)
df = iris.frame
df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

# Create a bar chart
plt.figure(figsize=(10, 6))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Average Petal Length per Species', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Average Petal Length (cm)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()