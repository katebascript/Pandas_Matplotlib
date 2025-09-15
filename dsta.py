import pandas as pd

# Example: Load a DataFrame from a CSV file
# df = pd.read_csv('your_file.csv')

# For demonstration, create a sample DataFrame
df = pd.DataFrame({
	'A': [1, 2, 3, 4],
	'B': [5, 6, 7, 8]
})

# Compute basic statistics
print("\nBasic statistics of numerical columns:")
print(df.describe())