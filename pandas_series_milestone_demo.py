"""
Milestone Demo: Creating Pandas Series from Lists and Arrays
============================================================
This script demonstrates:
1) Series creation from Python lists
2) Series creation from NumPy arrays
3) Inspecting Series index and values
4) Why label-based alignment matters in Pandas
"""

import numpy as np
import pandas as pd

print("PANDAS SERIES MILESTONE DEMO")
print("=" * 28)

# === 1) SERIES FROM PYTHON LIST ===
student_scores_list = [88, 92, 79, 95]
scores_series_from_list = pd.Series(student_scores_list)

print("\n1) Series from Python list")
print(scores_series_from_list)
print("Default index:", scores_series_from_list.index)
print("Values:", scores_series_from_list.values)

# === 2) SERIES FROM NUMPY ARRAY ===
temperature_array = np.array([36.5, 37.0, 38.2, 36.8], dtype=float)
temperature_series_from_array = pd.Series(temperature_array)

print("\n2) Series from NumPy array")
print(temperature_series_from_array)
print("Default index:", temperature_series_from_array.index)
print("Values:", temperature_series_from_array.values)
print("Dtype preserved from NumPy:", temperature_series_from_array.dtype)

# === 3) LABELS ADD MEANING ===
weekday_sales = pd.Series(
    [1200, 1500, 1100],
    index=["monday", "tuesday", "wednesday"],
)

print("\n3) Labeled Series example")
print(weekday_sales)
print("Access by position (0):", weekday_sales.iloc[0])
print("Access by label ('tuesday'):", weekday_sales.loc["tuesday"])

# === 4) WHY INDEX AWARENESS MATTERS (MANDATORY SCENARIO) ===
series_a = pd.Series([10, 20, 30], index=["a", "b", "c"])
series_b = pd.Series([1, 2, 3], index=["b", "c", "d"])
aligned_sum = series_a + series_b

print("\n4) Index alignment behavior")
print("Series A:")
print(series_a)
print("Series B:")
print(series_b)
print("A + B (aligned by label, not just position):")
print(aligned_sum)
print("Notice NaN where a label exists in only one Series.")

print("\nWhy this differs from NumPy:")
print("- NumPy arrays operate position-by-position")
print("- Pandas Series align by index labels first")
print("- Incorrect index assumptions can cause unexpected results")

print("\nVideo checklist:")
print("- Show list -> Series conversion")
print("- Show NumPy array -> Series conversion")
print("- Show Series index and values")
print("- Explain default indexing and labeled indexing")
print("- Explain index alignment scenario (A + B example)")

print("\nDemo complete!")
