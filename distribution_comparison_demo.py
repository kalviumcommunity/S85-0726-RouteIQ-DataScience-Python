"""
Distribution Comparison Demo Script
Demonstrates comparing distributions across multiple columns in a Pandas DataFrame
Optimized for 2-minute screen recording demonstration
"""

import pandas as pd

print("="*70)
print("COMPARING DISTRIBUTIONS ACROSS MULTIPLE COLUMNS")
print("="*70)

# Load sample dataset with multiple numeric columns
df = pd.read_csv("data/raw/sample_routes.csv")

# Select numeric columns for comparison
numeric_cols = ['distance_km', 'travel_time_min', 'passenger_count', 'fare_usd', 'driver_rating']
df_numeric = df[numeric_cols]

print("\n" + "-"*70)
print("1. Summary Statistics for All Numeric Columns")
print("-"*70)
print(df_numeric.describe())

print("\n" + "-"*70)
print("2. Comparing Central Tendency (Mean and Median)")
print("-"*70)
means = df_numeric.mean()
medians = df_numeric.median()
comparison = pd.DataFrame({'Mean': means, 'Median': medians})
print(comparison)

print("\n" + "-"*70)
print("3. Comparing Spread and Variability")
print("-"*70)
ranges = df_numeric.max() - df_numeric.min()
std_devs = df_numeric.std()
spread_comparison = pd.DataFrame({'Range': ranges, 'Std Dev': std_devs})
print(spread_comparison)

print("\n" + "-"*70)
print("4. Identifying Patterns and Anomalies")
print("-"*70)

# Calculate coefficient of variation (CV) for relative variability
cv = (df_numeric.std() / df_numeric.mean()) * 100
print("Coefficient of Variation (CV %):")
print(cv.round(2))

print("\n" + "-"*70)
print("5. Key Insights from Distribution Comparison")
print("-"*70)

# Compare means
highest_mean = means.idxmax()
lowest_mean = means.idxmin()
print(f"Highest average: {highest_mean} ({means[highest_mean]:.2f})")
print(f"Lowest average: {lowest_mean} ({means[lowest_mean]:.2f})")

# Compare variability
highest_cv = cv.idxmax()
lowest_cv = cv.idxmin()
print(f"\nMost variable column: {highest_cv} (CV: {cv[highest_cv]:.2f}%)")
print(f"Most stable column: {lowest_cv} (CV: {cv[lowest_cv]:.2f}%)")

# Check for skew (mean vs median)
skewed_cols = []
for col in numeric_cols:
    if abs(means[col] - medians[col]) / medians[col] > 0.1:
        skewed_cols.append(col)

if skewed_cols:
    print(f"\nPotentially skewed columns: {', '.join(skewed_cols)}")
else:
    print("\nAll columns show relatively symmetric distributions")

print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Summary statistics (describe()) give overview of all columns")
print("2. Compare means to understand central tendency differences")
print("3. Compare range and std dev to understand variability")
print("4. Coefficient of variation normalizes variability for comparison")
print("5. Mean vs median comparison reveals potential skew")
print("6. Distribution comparison reveals patterns single-column analysis misses")
print("\nAlways compare distributions, not just raw values!")
print("="*70)
