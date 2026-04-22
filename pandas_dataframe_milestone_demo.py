"""
Milestone Demo: Creating Pandas DataFrames from Dictionaries and Files
======================================================================
This script demonstrates:
1) Creating a DataFrame from a Python dictionary
2) Loading a DataFrame from a CSV file
3) Inspecting rows, columns, shape, and data types
"""

from pathlib import Path

import pandas as pd

print("PANDAS DATAFRAME MILESTONE DEMO")
print("=" * 32)

# === 1) CREATE DATAFRAME FROM DICTIONARY ===
employee_data = {
    "employee_id": [1, 2, 3],
    "employee_name": ["Anika", "Bashir", "Chayan"],
    "team": ["Data", "ML", "Data"],
    "monthly_salary": [55000, 62000, 58000],
}

employees_df = pd.DataFrame(employee_data)

print("\n1) DataFrame from dictionary")
print(employees_df)
print("Columns:", list(employees_df.columns))
print("Shape (rows, columns):", employees_df.shape)
print("Data types:")
print(employees_df.dtypes)

# === 2) LOAD DATAFRAME FROM FILE ===
csv_path = Path("data/sample_students.csv")
students_df = pd.read_csv(csv_path)

print("\n2) DataFrame loaded from CSV file")
print(f"Source file: {csv_path}")
print(students_df)

# === 3) INSPECT DATAFRAME STRUCTURE ===
print("\n3) Inspecting loaded DataFrame")
print("First 3 rows:")
print(students_df.head(3))
print("Columns:", list(students_df.columns))
print("Shape (rows, columns):", students_df.shape)
print("Data types:")
print(students_df.dtypes)

print("\nWhy DataFrames are useful:")
print("- They store tabular data with row and column structure")
print("- They support labeled columns for readable workflows")
print("- They are the standard starting point for data cleaning and analysis")

print("\nVideo checklist:")
print("- Show DataFrame creation from dictionary")
print("- Show DataFrame loading from CSV")
print("- Show head(), columns, shape, and dtypes")
print("- Explain why DataFrames are central in Pandas")

print("\nDemo complete!")
