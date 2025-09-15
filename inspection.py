import pandas as pd

# Example: Load a dataset into df (replace with your actual data source)
# df = pd.read_csv('your_dataset.csv')
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())