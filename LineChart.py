import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset into a DataFrame
iris = load_iris(as_frame=True)
df = iris.frame
df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

# Create a line chart (illustrative for non-time-series data)
plt.figure(figsize=(10, 6))
df.groupby('species')['sepal length (cm)'].mean().plot(kind='line', marker='o')
plt.title('Average Sepal Length per Species', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Average Sepal Length (cm)', fontsize=12)
plt.grid(True)
plt.show()