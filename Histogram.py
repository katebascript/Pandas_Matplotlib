import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

# Load the iris dataset into a DataFrame
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='sepal width (cm)', bins=20, kde=True, color='purple')
plt.title('Distribution of Sepal Width', fontsize=16)
plt.xlabel('Sepal Width (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()