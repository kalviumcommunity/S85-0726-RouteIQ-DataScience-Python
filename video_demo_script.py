"""
Video Demonstration Script for Code Structure and Reuse
========================================================
This script demonstrates proper Python code organization for readability and reuse.
Optimized for a 2-minute screen recording.

Structure principles demonstrated:
1. Clear section organization (imports, constants, functions, execution)
2. Function reuse to avoid duplication
3. Separation of logic and execution
4. Readable, maintainable code patterns
"""

# ============================================================================
# SECTION 1: IMPORTS
# ============================================================================
# Standard library imports would go here
# Example: import math, random, datetime


# ============================================================================
# SECTION 2: CONSTANTS
# ============================================================================
# Configuration values that don't change during execution
COST_PER_UNIT = 50
DISCOUNT_PERCENTAGE = 10


# ============================================================================
# SECTION 3: HELPER FUNCTIONS
# ============================================================================

def print_section_header(section_number, title):
    """Print a formatted section header - avoids repetition."""
    header = f"{section_number}) {title}"
    print(f"\n{header}")
    print("-" * len(header))

def print_function_call(func_name, args, result):
    """Print function call details - reusable formatting."""
    print(f"Function call: {func_name}{args}")
    print(f"Returned: {result}")

def greet_person(name, age):
    """Accept parameters and return a greeting."""
    return f"Hello {name}, you are {age} years old!"

def calculate_area(length, width):
    """Calculate area and return result."""
    return length * width

def get_stats(numbers):
    """Return multiple statistics."""
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

def add_five(n):
    """Add 5 to a number - reusable building block."""
    return n + 5

def multiply_by_two(n):
    """Multiply a number by 2 - reusable building block."""
    return n * 2

def calculate_discount(price, percentage):
    """Calculate discount amount - accepts parameters, returns value."""
    return price * (percentage / 100)


# ============================================================================
# SECTION 4: MAIN EXECUTION LOGIC
# ============================================================================

def main():
    """Main function containing all execution logic."""
    print("CODE STRUCTURE AND REUSE - VIDEO DEMO")
    print("=" * 50)

    # Demonstrate 1: Function with parameters
    print_section_header("1", "FUNCTION WITH PARAMETERS")
    result = greet_person("Alice", 25)
    print_function_call("greet_person", "('Alice', 25)", result)

    # Demonstrate 2: Calculation with returned value
    print_section_header("2", "CALCULATION FUNCTION")
    area = calculate_area(10, 5)
    cost = area * COST_PER_UNIT
    print(f"Area: calculate_area(10, 5) = {area}")
    print(f"Cost calculation: {area} * {COST_PER_UNIT} = ${cost}")

    # Demonstrate 3: Multiple return values
    print_section_header("3", "MULTIPLE RETURN VALUES")
    numbers = [10, 20, 30, 40]
    total, average = get_stats(numbers)
    print(f"Stats for {numbers}:")
    print(f"Total: {total}, Average: {average}")

    # Demonstrate 4: Function chaining
    print_section_header("4", "FUNCTION CHAINING")
    chained_result = multiply_by_two(add_five(3))
    print(f"Chaining: multiply_by_two(add_five(3)) = {chained_result}")
    print(f"Step 1: add_five(3) = {add_five(3)}")
    print(f"Step 2: multiply_by_two({add_five(3)}) = {chained_result}")

    # Demonstrate 5: Best practices
    print_section_header("5", "BEST PRACTICES")
    discount = calculate_discount(100, DISCOUNT_PERCENTAGE)
    final_price = 100 - discount
    print(f"Discount: ${discount}, Final price: ${final_price}")

    print("\nVideo checklist:")
    print("- Show clear section organization (imports, constants, functions, main)")
    print("- Demonstrate helper functions that avoid code repetition")
    print("- Explain separation of logic (functions) from execution (main)")
    print("- Show how structure improves readability and maintainability")
    print("- Highlight that constants make code easier to modify")

    print("\nDemo complete!")


# ============================================================================
# SECTION 5: ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
