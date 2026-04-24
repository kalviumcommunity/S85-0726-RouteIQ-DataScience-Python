"""
Duplicate Handling Video Demo Script
Optimized for 2-minute screen recording demonstration
Demonstrates identifying and removing duplicate records in Pandas
"""

import pandas as pd

print("="*70)
print("DUPLICATE HANDLING DEMO")
print("="*70)

# Create a DataFrame with intentional duplicates
data = {
    'route_id': ['R001', 'R002', 'R003', 'R001', 'R004', 'R002', 'R005'],
    'origin': ['Downtown', 'Airport', 'Downtown', 'Downtown', 'Suburb_A', 'Airport', 'Mall'],
    'destination': ['Airport', 'Downtown', 'Suburb_A', 'Airport', 'Downtown', 'Downtown', 'Downtown'],
    'distance_km': [25.5, 25.5, 12.3, 25.5, 12.3, 25.5, 8.7],
    'fare_usd': [35.50, 35.50, 18.00, 35.50, 18.00, 35.50, 12.50]
}

df = pd.DataFrame(data)

print("\n" + "-"*70)
print("1. Original DataFrame (with duplicates)")
print("-"*70)
print(df)
print(f"\nShape: {df.shape}")

print("\n" + "-"*70)
print("2. Detecting Duplicates - duplicated() method")
print("-"*70)
# duplicated() returns True for duplicate rows (first occurrence is False)
duplicates = df.duplicated()
print(duplicates)
print(f"\nNumber of duplicate rows: {duplicates.sum()}")

print("\n" + "-"*70)
print("3. Inspecting Duplicate Rows")
print("-"*70)
# Show only the duplicate rows
duplicate_rows = df[duplicates]
print(duplicate_rows)

print("\n" + "-"*70)
print("4. Removing Duplicates - drop_duplicates() method")
print("-"*70)
# By default, keeps first occurrence and removes subsequent duplicates
df_deduped = df.drop_duplicates()
print(df_deduped)
print(f"\nOriginal shape: {df.shape}")
print(f"After deduplication: {df_deduped.shape}")
print(f"Rows removed: {df.shape[0] - df_deduped.shape[0]}")

print("\n" + "-"*70)
print("5. Verifying No Duplicates Remain")
print("-"*70)
remaining_duplicates = df_deduped.duplicated().sum()
print(f"Remaining duplicates: {remaining_duplicates}")
print("✅ All duplicates successfully removed!")

print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("duplicated()     → Boolean mask identifying duplicate rows")
print("drop_duplicates() → Removes duplicate rows (keeps first by default)")
print("Always inspect before removing → Understand what you're deleting")
print("Verify after removal → Ensure data integrity")
print("\nDuplicate data corrupts analysis - deduplication is essential!")
print("="*70)
