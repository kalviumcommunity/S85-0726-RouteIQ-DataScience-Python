# Understanding DataFrame shape and column data types

import pandas as pd

# Load CSV
file_path = "data/raw/sample_data.csv"
df = pd.read_csv(file_path)

print("---- Data Preview ----")
print(df.head())


print("\n---- Data Shape ----")
print(df.shape)

# Interpreting shape
num_rows, num_columns = df.shape
print(f"Number of rows (observations): {num_rows}")
print(f"Number of columns (features): {num_columns}")


print("\n---- Column Names ----")
print(df.columns)


print("\n---- Data Types ----")
print(df.dtypes)


print("\n---- Detailed Info ----")
df.info()


# Example: why types matter
print("\n---- Type Check Example ----")
if df["marks"].dtype == "int64":
    print("Marks column is numeric → calculations can be performed")
else:
    print("Marks column is NOT numeric → needs conversion")