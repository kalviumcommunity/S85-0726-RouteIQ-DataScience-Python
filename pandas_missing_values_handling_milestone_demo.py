"""
Milestone Demo: Handling Missing Values with Drop and Fill Strategies
=====================================================================
This script demonstrates:
1) Detecting missing values before cleaning
2) Dropping missing values with dropna()
3) Filling missing values with fillna()
4) Comparing shape and data impact across strategies
5) Making intentional, explainable cleaning decisions
"""

import numpy as np
import pandas as pd

print("PANDAS MISSING-VALUE HANDLING MILESTONE DEMO")
print("=" * 45)

# ---------------------------------------------------------------------
# 1) BUILD SAMPLE DATAFRAME WITH MISSING VALUES
# ---------------------------------------------------------------------
df = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "region": ["North", "South", None, "West", "East", "North", np.nan, "South"],
        "sales_amount": [500.0, np.nan, 420.0, 610.0, np.nan, 580.0, 460.0, 490.0],
        "units_sold": [5, 4, np.nan, 6, 3, np.nan, 4, 5],
        "channel": ["Online", None, "Retail", "Online", "Retail", "Online", "Retail", None],
        "notes": [None, None, "priority", None, None, "follow-up", None, None],
    }
)

print("\n1) Original DataFrame")
print(df)
print("Original shape:", df.shape)

print("\nMissing values per column (before handling):")
missing_before = df.isna().sum()
print(missing_before)

# ---------------------------------------------------------------------
# 2) DROP STRATEGIES
# ---------------------------------------------------------------------
print("\n2) DROP STRATEGIES")

# 2a) Drop rows containing any missing value
drop_rows_any = df.dropna(axis=0, how="any")
print("\n2a) Drop rows with ANY missing value")
print("Shape after row drop:", drop_rows_any.shape)
print(drop_rows_any)

# 2b) Drop columns with excessive missing values
# Threshold: keep columns with at least 6 non-missing values (out of 8 rows)
drop_cols_threshold = df.dropna(axis=1, thresh=6)
print("\n2b) Drop columns with too many missing values (thresh=6 non-null required)")
print("Shape after column drop:", drop_cols_threshold.shape)
print("Remaining columns:", list(drop_cols_threshold.columns))

print("\nDrop strategy notes:")
print("- Dropping rows simplifies cleaning but can remove substantial data.")
print("- Dropping columns may be reasonable when missingness is high and column value is low.")

# ---------------------------------------------------------------------
# 3) FILL STRATEGIES
# ---------------------------------------------------------------------
print("\n3) FILL STRATEGIES")

fill_df = df.copy()

# Numeric fills: mean/median
sales_mean = fill_df["sales_amount"].mean()
units_median = fill_df["units_sold"].median()
fill_df["sales_amount"] = fill_df["sales_amount"].fillna(sales_mean)
fill_df["units_sold"] = fill_df["units_sold"].fillna(units_median)

# Categorical fills: mode or explicit constant
region_mode = fill_df["region"].mode(dropna=True)[0]
fill_df["region"] = fill_df["region"].fillna(region_mode)
fill_df["channel"] = fill_df["channel"].fillna("Unknown")

# Optional text column with high missingness: constant placeholder
fill_df["notes"] = fill_df["notes"].fillna("No note")

print("\nFilled DataFrame")
print(fill_df)
print("Shape after fill strategy:", fill_df.shape)

print("\nMissing values per column (after fill):")
missing_after_fill = fill_df.isna().sum()
print(missing_after_fill)

print("\nFill strategy notes:")
print("- Filling preserves row count but introduces assumptions.")
print("- Numeric columns use summary statistics (mean/median).")
print("- Categorical/text columns use mode or explicit labels, not numeric values.")

# ---------------------------------------------------------------------
# 4) COMPARISON: DROP VS FILL
# ---------------------------------------------------------------------
print("\n4) DROP VS FILL COMPARISON")
print("Original shape:", df.shape)
print("After dropping rows with any missing:", drop_rows_any.shape)
print("After dropping high-missing columns:", drop_cols_threshold.shape)
print("After filling missing values:", fill_df.shape)

print("\nDecision guidance:")
print("- Prefer drop when missing rows/columns are few and non-critical.")
print("- Prefer fill when a critical column has missing values and data loss is risky.")
print("- Always explain trade-offs and verify results after cleaning.")

# ---------------------------------------------------------------------
# 5) VIDEO CHECKLIST + MANDATORY SCENARIO
# ---------------------------------------------------------------------
print("\nVideo checklist (~2 minutes):")
print("- Show missing-value detection before cleaning (isna().sum())")
print("- Demonstrate row/column dropping with shape changes")
print("- Demonstrate fillna() with mean/median/mode/constants")
print("- Compare outcomes: drop vs fill")
print("- Explain which strategy you choose and why")

print("\nMandatory scenario answer (talking points):")
print("- Dropping rows in a critical numeric column can remove valuable evidence and bias results.")
print("- Filling can preserve data size, especially when missingness is moderate.")
print("- Choice depends on missing-rate, column importance, and downstream analysis sensitivity.")
print("- Decisions must be intentional, documented, and checked after cleaning.")

print("\nDemo complete!")
