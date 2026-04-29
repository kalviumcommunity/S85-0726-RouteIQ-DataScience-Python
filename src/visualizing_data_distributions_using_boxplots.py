import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")  # replace with your dataset file

# Display first few rows
print(df.head())

# Select numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64'])

# -----------------------------
# 1. Single Column Boxplot
# -----------------------------
col = numeric_cols.columns[0]  # selecting first numeric column

plt.figure()
plt.boxplot(numeric_cols[col])
plt.title(f"Boxplot of {col}")
plt.ylabel(col)
plt.show()

# -----------------------------
# 2. Multiple Columns Boxplot
# -----------------------------
plt.figure()
numeric_cols.boxplot()
plt.title("Boxplot Comparison of Numeric Columns")
plt.xticks(rotation=45)
plt.show()