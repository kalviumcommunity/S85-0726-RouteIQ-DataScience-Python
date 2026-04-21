"""
Milestone Demo: Applying Vectorized Operations Instead of Python Loops
======================================================================
This script demonstrates:
1) Loop-based numerical operations on NumPy arrays
2) Equivalent vectorized operations
3) Output equality checks for correctness
4) Basic vectorized comparisons and shape pitfall handling
"""

import numpy as np

print("VECTORIZATION MILESTONE DEMO")
print("=" * 32)

# === 1) CREATE ARRAYS ===
values = np.array([2, 4, 6, 8, 10], dtype=float)
print("\nOriginal array:")
print(values)

# === 2) LOOP-BASED OPERATION ===
# Operation: for each value x, compute x * 2 + 3
loop_result = []
for value in values:
    transformed_value = value * 2 + 3
    loop_result.append(transformed_value)
loop_result = np.array(loop_result)

print("\nLoop-based result (x * 2 + 3):")
print(loop_result)

# === 3) VECTORIZED OPERATION ===
vectorized_result = values * 2 + 3

print("\nVectorized result (x * 2 + 3):")
print(vectorized_result)

# === 4) CORRECTNESS CHECK ===
results_match = np.array_equal(loop_result, vectorized_result)
print("\nDo loop and vectorized outputs match?")
print(results_match)

# === 5) VECTORIZED ARITHMETIC EXAMPLES ===
print("\nVectorized arithmetic examples:")
print("values + 5 ->", values + 5)
print("values / 2 ->", values / 2)
print("values ** 2 ->", values**2)

# === 6) VECTORIZED COMPARISON EXAMPLES ===
print("\nVectorized comparison examples:")
print("values > 5 ->", values > 5)
print("values == 8 ->", values == 8)

# === 7) COMMON PITFALL: SHAPE MISMATCH ===
print("\nShape mismatch demonstration:")
array_a = np.array([1, 2, 3])
array_b = np.array([10, 20])
print("array_a shape:", array_a.shape)
print("array_b shape:", array_b.shape)

try:
    print(array_a + array_b)
except ValueError as error:
    print("Cannot add these arrays due to incompatible shapes.")
    print("Error:", error)

# === 8) VIDEO TALK TRACK (FOR SCENARIO ANSWER) ===
print("\nWhy vectorization is preferred:")
print("- Improves readability by removing manual element-by-element loops")
print("- Usually faster because NumPy operations run in optimized native code")
print("- Scales better as array size grows")
print("- Trade-off: avoid forcing vectorization when logic becomes less clear")
print("- Keep code readable and ensure array shapes are compatible")

print("\nDemo complete!")
