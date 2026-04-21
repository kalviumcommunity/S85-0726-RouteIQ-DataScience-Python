"""
NumPy Broadcasting Demonstration Script
========================================
This script demonstrates NumPy broadcasting with simple, intuitive examples.
Optimized for a 2-minute screen recording.

Broadcasting concepts demonstrated:
1. Scalar-to-array broadcasting
2. 1D-to-2D array broadcasting
3. Shape inspection and alignment rules
4. Understanding why broadcasting works
"""

# ============================================================================
# SECTION 1: IMPORTS
# ============================================================================
import numpy as np


# ============================================================================
# SECTION 2: HELPER FUNCTIONS
# ============================================================================

def print_section_header(section_number, title):
    """Print a formatted section header."""
    header = f"{section_number}) {title}"
    print(f"\n{header}")
    print("-" * len(header))

def inspect_array(name, arr):
    """Print array shape and values for inspection."""
    print(f"{name}:")
    print(f"  Shape: {arr.shape}")
    print(f"  Values: {arr}")


# ============================================================================
# SECTION 3: MAIN EXECUTION LOGIC
# ============================================================================

def main():
    """Main function containing all broadcasting demonstrations."""
    print("NUMPY BROADCASTING - VIDEO DEMO")
    print("=" * 50)

    # -------------------------------------------------------------------------
    # Demonstration 1: Scalar-to-Array Broadcasting
    # -------------------------------------------------------------------------
    print_section_header("1", "SCALAR-TO-ARRAY BROADCASTING")
    
    # Create a simple 1D array
    arr_1d = np.array([1, 2, 3, 4, 5])
    scalar = 10
    
    inspect_array("Original array", arr_1d)
    print(f"Scalar value: {scalar}")
    
    # Add scalar to array (broadcasting happens here)
    result = arr_1d + scalar
    print(f"\nOperation: arr_1d + {scalar}")
    inspect_array("Result", result)
    print("Explanation: Scalar 10 is 'stretched' to match array shape [1,2,3,4,5] + [10,10,10,10,10]")

    # -------------------------------------------------------------------------
    # Demonstration 2: 1D-to-2D Broadcasting (Row-wise)
    # -------------------------------------------------------------------------
    print_section_header("2", "1D-TO-2D BROADCASTING (ROW-WISE)")
    
    # Create a 2D array (3x4)
    arr_2d = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]])
    
    # Create a 1D array that matches the columns
    arr_1d_cols = np.array([10, 20, 30, 40])
    
    inspect_array("2D array (3x4)", arr_2d)
    inspect_array("1D array (4,)", arr_1d_cols)
    
    # Add 1D array to 2D array
    result_2d = arr_2d + arr_1d_cols
    print(f"\nOperation: arr_2d + arr_1d_cols")
    inspect_array("Result (3x4)", result_2d)
    print("Explanation: 1D array [10,20,30,40] is broadcast across each row")

    # -------------------------------------------------------------------------
    # Demonstration 3: 1D-to-2D Broadcasting (Column-wise)
    # -------------------------------------------------------------------------
    print_section_header("3", "1D-TO-2D BROADCASTING (COLUMN-WISE)")
    
    # Create a 1D array that needs reshaping for column-wise
    arr_1d_rows = np.array([100, 200, 300])
    
    inspect_array("2D array (3x4)", arr_2d)
    inspect_array("1D array (3,)", arr_1d_rows)
    
    # Reshape to (3,1) for column-wise broadcasting
    arr_1d_reshaped = arr_1d_rows.reshape(3, 1)
    inspect_array("Reshaped to (3,1)", arr_1d_reshaped)
    
    result_col = arr_2d + arr_1d_reshaped
    print(f"\nOperation: arr_2d + reshaped_1d")
    inspect_array("Result (3x4)", result_col)
    print("Explanation: Reshaped to (3,1), then broadcast across each column")

    # -------------------------------------------------------------------------
    # Demonstration 4: Broadcasting Rules Visualization
    # -------------------------------------------------------------------------
    print_section_header("4", "BROADCASTING RULES")
    
    print("NumPy compares shapes from RIGHT to LEFT:")
    print("  - Dimensions must match OR")
    print("  - One dimension must be 1 (expandable)")
    print()
    print("Example: (3,4) + (4,) → (3,4)")
    print("  Compare: 4 vs 4 ✓ match")
    print("           3 vs  -  ✓ broadcast")
    print()
    print("Example: (3,4) + (3,1) → (3,4)")
    print("  Compare: 4 vs 1 ✓ expand 1 to 4")
    print("           3 vs 3 ✓ match")
    print()
    print("Incompatible: (3,4) + (2,)")
    print("  Compare: 4 vs 2 ✗ neither matches nor is 1")

    # -------------------------------------------------------------------------
    # Demonstration 5: Common Mistake (Incompatible Shapes)
    # -------------------------------------------------------------------------
    print_section_header("5", "INCOMPATIBLE SHAPES ERROR")
    
    arr_wrong = np.array([1, 2, 3])
    inspect_array("2D array (3,4)", arr_2d)
    inspect_array("1D array (3,)", arr_wrong)
    
    print(f"\nAttempting: arr_2d + arr_wrong")
    print("This will raise ValueError because shapes (3,4) and (3,) are incompatible")
    print("Reason: Last dimensions 4 and 3 don't match, and neither is 1")

    # -------------------------------------------------------------------------
    # Video Checklist
    # -------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("VIDEO CHECKLIST:")
    print("- Show scalar-to-array: arr + scalar")
    print("- Show 1D-to-2D: arr_2d + arr_1d")
    print("- Inspect shapes before and after operations")
    print("- Explain shape alignment (right-to-left comparison)")
    print("- Mention that broadcasting doesn't copy data (it's virtual)")
    print("- Show incompatible shape example for contrast")
    print("\nDemo complete!")


# ============================================================================
# SECTION 4: ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
