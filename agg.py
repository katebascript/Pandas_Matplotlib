import pandas as pd

# Load your data into df, for example using the iris dataset:
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Group by 'target' and compute the mean of numerical columns
print("\nMean of numerical columns grouped by species:")
# The target column needs to be mapped to species names for clarity
df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
print(df.groupby('species').mean())