"""
Boxplot Visualization Demo Script
Demonstrates visualizing data distributions using boxplots
Optimized for 2-minute screen recording demonstration
"""

import pandas as pd
import matplotlib.pyplot as plt

print("="*70)
print("BOXPLOT VISUALIZATION DEMO")
print("="*70)

# Load sample dataset
df = pd.read_csv("data/raw/sample_routes.csv")

# Select numeric columns for boxplot visualization
numeric_cols = ['distance_km', 'travel_time_min', 'passenger_count', 'fare_usd', 'driver_rating']
df_numeric = df[numeric_cols]

print("\n" + "-"*70)
print("1. Understanding Boxplot Components")
print("-"*70)
print("Boxplot shows:")
print("  - Median (middle line in box)")
print("  - Q1 (25th percentile) and Q3 (75th percentile) - box edges")
print("  - IQR (Interquartile Range) = Q3 - Q1")
print("  - Whiskers (typically 1.5 * IQR from Q1/Q3)")
print("  - Outliers (points beyond whiskers)")

print("\n" + "-"*70)
print("2. Single Column Boxplot - fare_usd")
print("-"*70)
print(df['fare_usd'].describe())

# Create single column boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df['fare_usd'], vert=True)
plt.title('Boxplot of Fare (USD)')
plt.ylabel('Fare (USD)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('boxplot_single_column.png', dpi=100)
print("Boxplot saved as 'boxplot_single_column.png'")
plt.close()

print("\n" + "-"*70)
print("3. Interpreting the fare_usd Boxplot")
print("-"*70)
fare_median = df['fare_usd'].median()
fare_q1 = df['fare_usd'].quantile(0.25)
fare_q3 = df['fare_usd'].quantile(0.75)
fare_iqr = fare_q3 - fare_q1
print(f"Median: ${fare_median:.2f}")
print(f"Q1 (25th percentile): ${fare_q1:.2f}")
print(f"Q3 (75th percentile): ${fare_q3:.2f}")
print(f"IQR: ${fare_iqr:.2f}")
print(f"50% of fares fall between ${fare_q1:.2f} and ${fare_q3:.2f}")

print("\n" + "-"*70)
print("4. Multiple Column Boxplot - Comparing Distributions")
print("-"*70)
print("Creating boxplots for all numeric columns...")

# Create multiple column boxplot
plt.figure(figsize=(12, 6))
plt.boxplot([df[col] for col in numeric_cols], tick_labels=numeric_cols, vert=True)
plt.title('Boxplots of All Numeric Columns')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('boxplot_multiple_columns.png', dpi=100)
print("Boxplot saved as 'boxplot_multiple_columns.png'")
plt.close()

print("\n" + "-"*70)
print("5. Comparing Spread and Variability")
print("-"*70)
for col in numeric_cols:
    col_median = df[col].median()
    col_iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
    col_range = df[col].max() - df[col].min()
    print(f"{col:20s} | Median: {col_median:7.2f} | IQR: {col_iqr:7.2f} | Range: {col_range:7.2f}")

print("\n" + "-"*70)
print("6. Identifying Potential Outliers")
print("-"*70)
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
    if len(outliers) > 0:
        print(f"{col}: {len(outliers)} potential outlier(s) - {outliers.tolist()}")
    else:
        print(f"{col}: No potential outliers detected")

print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Boxplots summarize distribution in a single visual")
print("2. Median line shows central tendency (not affected by outliers)")
print("3. Box height (IQR) shows spread of middle 50% of data")
print("4. Whiskers show typical range (1.5 * IQR from quartiles)")
print("5. Points beyond whiskers are potential outliers")
print("6. Side-by-side boxplots enable easy comparison across columns")
print("7. Outliers need context - not all are errors")
print("8. Combine boxplots with describe() for complete picture")
print("\nBoxplots are powerful for EDA and distribution comparison!")
print("="*70)
