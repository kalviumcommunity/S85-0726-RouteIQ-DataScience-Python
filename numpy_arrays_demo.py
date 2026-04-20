"""
Video Demonstration Script for Creating NumPy Arrays from Python Lists
======================================================================
This script demonstrates the fundamentals of NumPy arrays for efficient numerical computing.
Optimized for a 2-minute screen recording.

Key concepts demonstrated:
1. Importing NumPy
2. Creating arrays from Python lists
3. Inspecting array properties (shape, dtype, ndim)
4. Basic arithmetic operations on arrays
5. Comparing array vs list behavior
"""

# ============================================================================
# SECTION 1: IMPORTS
# ============================================================================
import numpy as np


# ============================================================================
# SECTION 2: HELPER FUNCTIONS
# ============================================================================

def print_section_header(section_number, title):
    """Print a formatted section header - avoids repetition."""
    header = f"{section_number}) {title}"
    print(f"\n{header}")
    print("-" * len(header))

def print_array_info(array, name="array"):
    """Print array properties in a consistent format."""
    print(f"{name}:")
    print(f"  Values: {array}")
    print(f"  Shape: {array.shape}")
    print(f"  Data type: {array.dtype}")
    print(f"  Dimensions: {array.ndim}")


# ============================================================================
# SECTION 3: MAIN EXECUTION LOGIC
# ============================================================================

def main():
    """Main function containing all execution logic."""
    print("NUMPY ARRAYS FROM PYTHON LISTS - VIDEO DEMO")
    print("=" * 50)

    # Demonstrate 1: Creating 1D arrays from lists
    print_section_header("1", "CREATING 1D ARRAYS FROM LISTS")
    
    # Create a simple list and convert to array
    python_list = [1, 2, 3, 4, 5]
    array_1d = np.array(python_list)
    print(f"Python list: {python_list}")
    print(f"NumPy array: {array_1d}")
    print(f"Type: {type(array_1d)}")

    # Demonstrate 2: Creating 2D arrays from nested lists
    print_section_header("2", "CREATING 2D ARRAYS FROM NESTED LISTS")
    
    nested_list = [[1, 2, 3], [4, 5, 6]]
    array_2d = np.array(nested_list)
    print(f"Nested list: {nested_list}")
    print(f"2D NumPy array:\n{array_2d}")

    # Demonstrate 3: Inspecting array properties
    print_section_header("3", "INSPECTING ARRAY PROPERTIES")
    
    print("1D array properties:")
    print_array_info(array_1d, "array_1d")
    
    print("\n2D array properties:")
    print_array_info(array_2d, "array_2d")

    # Demonstrate 4: Basic arithmetic operations
    print_section_header("4", "BASIC ARITHMETIC OPERATIONS")
    
    # Element-wise operations
    numbers = np.array([10, 20, 30, 40])
    print(f"Original array: {numbers}")
    print(f"Add 5: {numbers + 5}")
    print(f"Multiply by 2: {numbers * 2}")
    print(f"Square: {numbers ** 2}")

    # Demonstrate 5: Array vs List comparison
    print_section_header("5", "ARRAY VS LIST BEHAVIOR")
    
    # List behavior (repetition)
    list_example = [1, 2, 3]
    print(f"List: {list_example}")
    print(f"List * 2: {list_example * 2}  (repeats the list)")
    
    # Array behavior (element-wise)
    array_example = np.array([1, 2, 3])
    print(f"\nArray: {array_example}")
    print(f"Array * 2: {array_example * 2}  (element-wise multiplication)")

    print("\nVideo checklist:")
    print("- Show importing NumPy as np")
    print("- Demonstrate creating 1D array from simple list")
    print("- Demonstrate creating 2D array from nested list")
    print("- Show array.shape, array.dtype, and array.ndim")
    print("- Demonstrate element-wise arithmetic operations")
    print("- Compare array multiplication vs list multiplication")

    print("\nDemo complete!")


# ============================================================================
# SECTION 4: ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
