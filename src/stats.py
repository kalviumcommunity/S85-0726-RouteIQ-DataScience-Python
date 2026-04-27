import pandas as pd

# Sample DataFrame (you can replace with your dataset)
data = {
    "Age": [18, 20, 22, 19, 21, 23, 100],
    "Marks": [70, 75, 80, 72, 78, 85, 90]
}

df = pd.DataFrame(data)

# Select a single column
age_col = df["Age"]

# Compute summary statistics
print("Age Statistics:")
print("Count:", age_col.count())
print("Mean:", age_col.mean())
print("Median:", age_col.median())
print("Min:", age_col.min())
print("Max:", age_col.max())
print("Standard Deviation:", age_col.std())

print("\nMarks Statistics:")
print(df["Marks"].describe())