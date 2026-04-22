"""
DataFrame Inspection Video Demo Script
Optimized for 2-minute screen recording demonstration
"""

import pandas as pd

print("="*70)
print("DATAFRAME INSPECTION DEMO")
print("="*70)

# Load sample dataset
df = pd.read_csv("data/raw/sample_routes.csv")

print("\n" + "-"*70)
print("1. Using head() - Preview First 5 Rows")
print("-"*70)
print(df.head())

print("\n" + "-"*70)
print("2. Using head(3) - Preview First 3 Rows")
print("-"*70)
print(df.head(3))

print("\n" + "-"*70)
print("3. Using info() - Check Structure and Data Types")
print("-"*70)
df.info()

print("\n" + "-"*70)
print("4. Using describe() - Statistical Summary of Numeric Columns")
print("-"*70)
print(df.describe())

print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("head()  → Quick visual preview of data")
print("info()  → Structure, data types, and missing values")
print("describe() → Statistical summary for numeric columns")
print("\nAlways inspect data before analysis!")
print("="*70)
