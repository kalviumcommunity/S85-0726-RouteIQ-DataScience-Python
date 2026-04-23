"""
Pandas Indexing and Slicing Video Demo Script
Optimized for 2-minute screen recording demonstration
"""

import pandas as pd

print("="*70)
print("INDEXING AND SLICING DEMO")
print("="*70)

# Load sample dataset
df = pd.read_csv("data/raw/sample_routes.csv")
df_indexed = df.set_index('route_id')

print("\n" + "-"*70)
print("1. Selecting Columns by Name")
print("-"*70)
print("Single column:")
print(df['origin'].head())
print("\nMultiple columns:")
print(df[['origin', 'destination', 'fare_usd']].head())

print("\n" + "-"*70)
print("2. Selecting Rows by Position (iloc)")
print("-"*70)
print("Single row by position:")
print(df.iloc[0])
print("\nSlice rows by position:")
print(df.iloc[0:5])

print("\n" + "-"*70)
print("3. Selecting Rows by Label (loc)")
print("-"*70)
print("Single row by label:")
print(df_indexed.loc['R001'])
print("\nSlice rows by label:")
print(df_indexed.loc['R001':'R005'])

print("\n" + "-"*70)
print("4. Selecting Rows and Columns Together")
print("-"*70)
print("Using iloc for rows and columns:")
print(df.iloc[0:5, [0, 2, 6]])
print("\nUsing loc with labels:")
print(df_indexed.loc['R001':'R005', ['origin', 'destination', 'fare_usd']])

print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("Column selection: df['col'] or df[['col1', 'col2']]")
print("Row by position: df.iloc[row] or df.iloc[start:end]")
print("Row by label: df.loc[label] or df.loc[start:end]")
print("Combined: df.iloc[row, col] or df.loc[row, col]")
print("\nUse iloc for positions, loc for labels")
print("loc is inclusive, iloc is exclusive on end")
print("="*70)
