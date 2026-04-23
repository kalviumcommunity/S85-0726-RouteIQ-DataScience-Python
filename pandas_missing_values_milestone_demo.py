"""
Milestone Demo: Detecting Missing Values in Pandas DataFrames
=============================================================
This script demonstrates:
1) Understanding missing-value representations in Pandas
2) Detecting missing values with boolean masks
3) Counting missing values per column
4) Inspecting rows that contain missing entries
5) Interpreting why early missing-value checks matter
"""

import numpy as np
import pandas as pd

print("PANDAS MISSING-VALUE DETECTION MILESTONE DEMO")
print("=" * 44)

# === 1) CREATE A DATAFRAME WITH INTENTIONAL MISSING VALUES ===
orders_df = pd.DataFrame(
    {
        "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
        "customer_name": ["Asha", "Rafi", None, "Imran", "Nila", "Tariq"],
        "city": ["Dhaka", "Chattogram", "Dhaka", "", "Khulna", pd.NA],
        "discount_pct": [5.0, np.nan, 10.0, 0.0, np.nan, 7.5],
        "payment_status": ["paid", "paid", "pending", "paid", None, "pending"],
    }
)

print("\n1) Example DataFrame")
print(orders_df)

print("\nUnderstanding missing representations:")
print("- None, np.nan, and pd.NA are treated as missing by isna().")
print("- Empty strings ('') are not missing unless converted intentionally.")

# === 2) DETECT MISSING VALUES ===
missing_mask = orders_df.isna()

print("\n2) Missing-value boolean mask (True means missing)")
print(missing_mask)

columns_with_missing = missing_mask.any()
print("\nColumns containing at least one missing value:")
print(columns_with_missing)

# === 3) COUNT MISSING VALUES ===
missing_count_per_column = orders_df.isna().sum()
missing_ratio_per_column = (missing_count_per_column / len(orders_df)).round(2)

print("\n3) Missing-value count per column")
print(missing_count_per_column)

print("\nMissing-value proportion per column")
print(missing_ratio_per_column)

total_missing_cells = int(missing_count_per_column.sum())
print("\nTotal missing cells in DataFrame:", total_missing_cells)

# === 4) INSPECT ROWS WITH MISSING VALUES ===
rows_with_missing = orders_df[orders_df.isna().any(axis=1)]

print("\n4) Rows containing at least one missing value")
print(rows_with_missing)

print("\nInterpretation notes:")
print("- customer_name, city, discount_pct, and payment_status need attention.")
print("- city has an empty string in one row, which is NOT counted as missing.")
print("- Detect first, then choose intentional cleaning/imputation steps.")

print("\nVideo checklist (~2 minutes):")
print("- Show DataFrame and explain missing-value representations")
print("- Run isna() and explain boolean mask output")
print("- Show missing counts per column using isna().sum()")
print("- Show rows with missing data using isna().any(axis=1)")
print("- Explain why detection happens before cleaning")

print("\nDemo complete!")
