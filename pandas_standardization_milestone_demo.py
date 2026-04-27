"""
Milestone Demo: Standardizing Column Names and Data Formats in Pandas
=====================================================================
This script demonstrates:
1) Why standardization is important for reliable workflows
2) Cleaning and normalizing column names with a consistent convention
3) Standardizing text values for predictable categories
4) Converting numeric and date columns to consistent formats
5) Comparing before/after outputs for milestone submission and video walkthrough
"""

import re

import pandas as pd

print("PANDAS STANDARDIZATION MILESTONE DEMO")
print("=" * 38)


def standardize_column_name(column_name: str) -> str:
    """Convert messy column names to clean snake_case."""
    cleaned = column_name.strip().lower()
    cleaned = re.sub(r"[^\w\s]", "", cleaned)  # remove special characters
    cleaned = re.sub(r"\s+", "_", cleaned)  # replace spaces with underscore
    cleaned = re.sub(r"_+", "_", cleaned)  # collapse repeated underscores
    return cleaned


def standardize_text(series: pd.Series) -> pd.Series:
    """Lowercase text and remove extra whitespace."""
    return series.astype("string").str.strip().str.lower()


# ---------------------------------------------------------------------
# 1) BUILD A SAMPLE DATAFRAME WITH MESSY NAMES/FORMATS
# ---------------------------------------------------------------------
raw_df = pd.DataFrame(
    {
        "Customer Name ": ["  Alice  ", "BOB", "charlie", "Alice"],
        "Order Date": ["2026/01/05", "05-02-2026", "2026.03.14", "April 02, 2026"],
        "Sales Amount ($)": ["1200", " 2,500 ", "1900.50", "N/A"],
        "Region ": [" North", "south ", "SOUTH", " north "],
        "Product Category": ["Electronics", "electronics ", " Home ", "HOME"],
    }
)

print("\n1) Original DataFrame (before standardization)")
print(raw_df)
print("\nOriginal column names:")
print(list(raw_df.columns))
print("\nOriginal data types:")
print(raw_df.dtypes)


# ---------------------------------------------------------------------
# 2) STANDARDIZE COLUMN NAMES (SNAKE_CASE)
# ---------------------------------------------------------------------
standardized_df = raw_df.copy()
standardized_df.columns = [standardize_column_name(col) for col in standardized_df.columns]

print("\n2) Column names after standardization")
print(list(standardized_df.columns))


# ---------------------------------------------------------------------
# 3) STANDARDIZE TEXT COLUMNS
# ---------------------------------------------------------------------
standardized_df["customer_name"] = standardize_text(standardized_df["customer_name"])
standardized_df["region"] = standardize_text(standardized_df["region"])
standardized_df["product_category"] = standardize_text(standardized_df["product_category"])

print("\n3) Sample text columns after normalization")
print(standardized_df[["customer_name", "region", "product_category"]])

print("\nUnique values check after text cleanup")
print("region:", sorted(standardized_df["region"].dropna().unique().tolist()))
print(
    "product_category:",
    sorted(standardized_df["product_category"].dropna().unique().tolist()),
)


# ---------------------------------------------------------------------
# 4) STANDARDIZE NUMERIC AND DATE COLUMNS
# ---------------------------------------------------------------------
# Numeric cleanup: remove commas/spaces, convert invalid values to NaN
standardized_df["sales_amount"] = (
    standardized_df["sales_amount"]
    .astype("string")
    .str.replace(",", "", regex=False)
    .str.strip()
)
standardized_df["sales_amount"] = pd.to_numeric(
    standardized_df["sales_amount"], errors="coerce"
)

# Date cleanup: parse mixed date strings into consistent datetime format
standardized_df["order_date"] = pd.to_datetime(
    standardized_df["order_date"], errors="coerce", dayfirst=True
)

print("\n4) Numeric + date columns after type conversion")
print(standardized_df[["order_date", "sales_amount"]])
print("\nData types after conversion:")
print(standardized_df.dtypes)


# ---------------------------------------------------------------------
# 5) BEFORE/AFTER COMPARISON FOR MILESTONE VIDEO
# ---------------------------------------------------------------------
print("\n5) BEFORE vs AFTER COMPARISON")
print("\nBefore columns:", list(raw_df.columns))
print("After columns: ", list(standardized_df.columns))

print("\nBefore (first 3 rows):")
print(raw_df.head(3))
print("\nAfter (first 3 rows):")
print(standardized_df.head(3))

print("\nWhy this matters:")
print("- Clean column names make code predictable and easier to read.")
print("- Standardized text avoids hidden category mismatches.")
print("- Proper numeric/date types enable valid filtering, math, and grouping.")
print("- Standardization early in workflow improves merge reliability.")

print("\nVideo checklist (~2 minutes):")
print("- Show messy input and inconsistent column names")
print("- Demonstrate column name cleaning into snake_case")
print("- Standardize at least one text, one numeric, and one date column")
print("- Compare before and after DataFrame outputs")
print("- Explain how standardization reduces errors and improves reuse")

print("\nDemo complete!")
