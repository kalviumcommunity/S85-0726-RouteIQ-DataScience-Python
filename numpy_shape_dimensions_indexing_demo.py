"""
Video Demonstration Script for NumPy Shape, Dimensions, and Indexing
====================================================================
This script is optimized for a ~2-minute screen recording.
Demonstrates shape, ndim, and index positions in 1D, 2D, and 3D arrays.
"""

import numpy as np

print("NUMPY ARRAY STRUCTURE - MILESTONE DEMO")
print("=" * 40)

# === 1) 1D ARRAY: SHAPE AND DIMENSIONS ===
print("\n1) 1D ARRAY: SHAPE AND DIMENSIONS")
print("-" * 34)

scores_1d = np.array([10, 20, 30, 40, 50])
print(f"1D array: {scores_1d}")
print(f"Shape: {scores_1d.shape}")
print(f"Number of dimensions (ndim): {scores_1d.ndim}")
print("Explanation: shape (5,) means 5 elements in a single dimension.")

# Accessing 1D elements with zero-based indexing
print("\n1D indexing examples:")
print(f"scores_1d[0] -> {scores_1d[0]} (first element)")
print(f"scores_1d[3] -> {scores_1d[3]} (fourth element)")

# === 2) 2D ARRAY: SHAPE AND DIMENSIONS ===
print("\n2) 2D ARRAY: SHAPE AND DIMENSIONS")
print("-" * 34)

matrix_2d = np.array([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33],
])
print("2D array:")
print(matrix_2d)
print(f"Shape: {matrix_2d.shape}")
print(f"Number of dimensions (ndim): {matrix_2d.ndim}")
print("Explanation: shape (3, 3) means 3 rows and 3 columns.")

# === 3) 2D INDEXING: ROW FIRST, COLUMN SECOND ===
print("\n3) 2D INDEXING (ROW, COLUMN)")
print("-" * 29)

print(f"matrix_2d[0, 0] -> {matrix_2d[0, 0]} (row 0, col 0)")
print(f"matrix_2d[1, 2] -> {matrix_2d[1, 2]} (row 1, col 2)")
print(f"matrix_2d[2, 1] -> {matrix_2d[2, 1]} (row 2, col 1)")

# === 4) HIGHER-DIMENSION (3D) BASICS ===
print("\n4) 3D ARRAY BASICS")
print("-" * 18)

cube_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
])
print("3D array:")
print(cube_3d)
print(f"Shape: {cube_3d.shape}")
print(f"Number of dimensions (ndim): {cube_3d.ndim}")
print("Explanation: shape (2, 2, 2) means 2 blocks, each with 2 rows and 2 cols.")
print(f"cube_3d[1, 0, 1] -> {cube_3d[1, 0, 1]} (block 1, row 0, col 1)")

# === 5) VISUALIZING LAYOUT ===
print("\n5) VISUALIZING ARRAY LAYOUT")
print("-" * 26)
print("Grid view with index positions:")
print("[row, col] -> value")
print("[0, 0] -> 11   [0, 1] -> 12   [0, 2] -> 13")
print("[1, 0] -> 21   [1, 1] -> 22   [1, 2] -> 23")
print("[2, 0] -> 31   [2, 1] -> 32   [2, 2] -> 33")

# === 6) SAFE INDEXING CHECK ===
print("\n6) SAFE INDEXING CHECK")
print("-" * 22)

row_index = 2
col_index = 2
row_count, col_count = matrix_2d.shape

if 0 <= row_index < row_count and 0 <= col_index < col_count:
    print(
        f"Safe access at [{row_index}, {col_index}] -> "
        f"{matrix_2d[row_index, col_index]}"
    )
else:
    print("Index out of range: check shape before indexing.")

# Demonstrate handling a bad index without crashing the script.
print("\nIntentional out-of-range example:")
bad_row_index = 5
try:
    print(matrix_2d[bad_row_index, 0])
except IndexError as error:
    print(f"Handled IndexError for row {bad_row_index}: {error}")

print("\nImportant reminders:")
print("- Always check shape before indexing")
print("- Indexing starts at zero")
print("- In 2D arrays, use [row, column] order")
print("- For 3D arrays, use [block, row, column] order")

print("\nVideo checklist:")
print("- Show a 1D array and explain shape + ndim")
print("- Show a 2D array and explain rows/columns in shape")
print("- Briefly show a 3D array as a higher-dimensional example")
print("- Access values using index positions")
print("- Explain zero-based indexing and row/column order")

print("\nDemo complete!")
