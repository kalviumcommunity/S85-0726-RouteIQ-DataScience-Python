import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (use any CSV you have)
df = pd.read_csv("data.csv")

# Show basic info
print(df.head())

# Select numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64'])

# -------------------------------
# 1. Histogram for a single column
# -------------------------------
column = numeric_cols.columns[0]  # pick first numeric column

plt.figure()
plt.hist(df[column], bins=10)
plt.title(f"Histogram of {column}")
plt.xlabel(column)
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# 2. Histograms for multiple columns
# -------------------------------
numeric_cols.hist(bins=10, figsize=(10, 6))
plt.suptitle("Histograms of Numeric Columns")
plt.show()