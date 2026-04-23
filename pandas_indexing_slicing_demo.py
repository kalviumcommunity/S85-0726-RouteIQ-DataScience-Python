"""
Pandas Indexing and Slicing Comprehensive Demo
Demonstrates row and column selection using various methods
"""

import pandas as pd

print("="*70)
print("PANDAS INDEXING AND SLICING DEMO")
print("="*70)

# Load sample dataset
df = pd.read_csv("data/raw/sample_routes.csv")

# Set route_id as index for label-based indexing examples
df_indexed = df.set_index('route_id')

print("\n" + "="*70)
print("ORIGINAL DATAFRAME (First 5 rows)")
print("="*70)
print(df.head())
print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")

print("\n" + "="*70)
print("1. SELECTING COLUMNS BY NAME")
print("="*70)

# Single column selection
print("\n1.1 Single Column (df['origin']):")
print(df['origin'].head())

print("\n1.2 Single Column with dot notation (df.origin):")
print(df.origin.head())

print("\n1.3 Multiple Columns (list of names):")
print(df[['origin', 'destination', 'fare_usd']].head())

print("\n1.4 Result Type Explanation:")
print(f"Single column type: {type(df['origin'])}")
print(f"Multiple columns type: {type(df[['origin', 'destination']])}")

print("\n" + "="*70)
print("2. SELECTING ROWS BY POSITION (iloc)")
print("="*70)

# Position-based indexing
print("\n2.1 Single Row by Position (df.iloc[0]):")
print(df.iloc[0])

print("\n2.2 Multiple Rows by Position (df.iloc[[0, 2, 4]]):")
print(df.iloc[[0, 2, 4]])

print("\n2.3 Slice Rows by Position (df.iloc[0:5]):")
print(df.iloc[0:5])

print("\n2.4 Slice with Step (df.iloc[0:10:2]):")
print(df.iloc[0:10:2])

print("\n2.5 Negative Indexing (df.iloc[-1]):")
print(df.iloc[-1])

print("\n2.6 Last 3 Rows (df.iloc[-3:]):")
print(df.iloc[-3:])

print("\n" + "="*70)
print("3. SELECTING ROWS BY LABEL (loc)")
print("="*70)

print("\n3.1 DataFrame with route_id as index:")
print(df_indexed.head())

print("\n3.2 Single Row by Label (df_indexed.loc['R001']):")
print(df_indexed.loc['R001'])

print("\n3.3 Multiple Rows by Label (df_indexed.loc[['R001', 'R003', 'R005']]):")
print(df_indexed.loc[['R001', 'R003', 'R005']])

print("\n3.4 Slice Rows by Label (df_indexed.loc['R001':'R005']):")
print(df_indexed.loc['R001':'R005'])

print("\n3.5 Label-based with condition (df_indexed.loc[df_indexed['fare_usd'] > 30]):")
print(df_indexed.loc[df_indexed['fare_usd'] > 30])

print("\n" + "="*70)
print("4. SELECTING ROWS AND COLUMNS TOGETHER")
print("="*70)

print("\n4.1 Using iloc for rows and columns (df.iloc[0:5, 0:3]):")
print(df.iloc[0:5, 0:3])

print("\n4.2 Using iloc with specific column positions (df.iloc[0:5, [0, 2, 6]]):")
print(df.iloc[0:5, [0, 2, 6]])

print("\n4.3 Using loc for rows and columns (df_indexed.loc['R001':'R005', ['origin', 'destination', 'fare_usd']]):")
print(df_indexed.loc['R001':'R005', ['origin', 'destination', 'fare_usd']])

print("\n4.4 Combined selection with condition (df.loc[df['vehicle_type'] == 'SUV', ['route_id', 'origin', 'destination', 'fare_usd']]):")
print(df.loc[df['vehicle_type'] == 'SUV', ['route_id', 'origin', 'destination', 'fare_usd']])

print("\n" + "="*70)
print("5. COMMON SELECTION PATTERNS")
print("="*70)

print("\n5.1 Select first N rows and specific columns:")
print(df.head(3)[['origin', 'destination', 'fare_usd']])

print("\n5.2 Select rows where condition is met:")
print(df[df['passenger_count'] > 10][['route_id', 'passenger_count', 'fare_usd']])

print("\n5.3 Select rows with multiple conditions:")
print(df[(df['vehicle_type'] == 'Sedan') & (df['fare_usd'] > 20)][['route_id', 'origin', 'destination', 'fare_usd']])

print("\n5.4 Select using isin():")
print(df[df['vehicle_type'].isin(['SUV', 'Minivan'])][['route_id', 'vehicle_type', 'fare_usd']])

print("\n" + "="*70)
print("6. AVOIDING COMMON MISTAKES")
print("="*70)

print("\n6.1 Chained Indexing (AVOID THIS):")
print("❌ df['origin'][0:5] - Creates a copy, can cause SettingWithCopyWarning")
print("✅ df.loc[0:5, 'origin'] - Single operation, safer")

print("\n6.2 Confusing iloc vs loc:")
print("❌ df.loc[0] - Uses label '0', not position")
print("✅ df.iloc[0] - Uses position 0")

print("\n6.3 Forgetting that loc is inclusive:")
print("df.loc['R001':'R005'] - Includes both R001 AND R005")
print("df.iloc[0:5] - Includes 0,1,2,3,4 (excludes 5)")

print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("✓ Use df['column'] or df.column for single column selection")
print("✓ Use df[['col1', 'col2']] for multiple columns")
print("✓ Use iloc for position-based indexing (integer positions)")
print("✓ Use loc for label-based indexing (index values)")
print("✓ Combine row and column selection in one operation")
print("✓ Avoid chained indexing - use .loc or .iloc directly")
print("✓ loc is inclusive, iloc is exclusive on the end")
print("\nAlways verify your selection results!")
print("="*70)
