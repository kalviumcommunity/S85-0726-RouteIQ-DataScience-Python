"""
Function Parameters and Return Values Demonstration Script
========================================================
This script demonstrates passing data into functions and returning results.
"""

print("FUNCTION PARAMETERS AND RETURN VALUES - DEMONSTRATION")
print("=" * 60)

# === 1. BASIC FUNCTION WITH PARAMETERS ===
print("\n1) BASIC FUNCTION WITH PARAMETERS")
print("-" * 40)

def greet_person(name, age):
    """Function that accepts two parameters and returns a greeting."""
    return f"Hello {name}, you are {age} years old!"

# Calling the function with arguments
result1 = greet_person("Alice", 25)
print(f"Function call: greet_person('Alice', 25)")
print(f"Returned result: {result1}")

# Reusing the same function with different arguments
result2 = greet_person("Bob", 30)
print(f"Function call: greet_person('Bob', 30)")
print(f"Returned result: {result2}")

# === 2. FUNCTION THAT PERFORMS CALCULATIONS ===
print("\n2) FUNCTION THAT PERFORMS CALCULATIONS")
print("-" * 45)

def calculate_area(length, width):
    """Calculate rectangle area and return the result."""
    area = length * width
    return area

# Using the returned value in further computation
rectangle_area = calculate_area(10, 5)
total_cost = rectangle_area * 50  # $50 per square unit

print(f"Area calculation: calculate_area(10, 5)")
print(f"Returned area: {rectangle_area}")
print(f"Using returned area for cost: {rectangle_area} * 50 = ${total_cost}")

# === 3. FUNCTION WITH MULTIPLE RETURN VALUES ===
print("\n3) FUNCTION WITH MULTIPLE RETURN VALUES")
print("-" * 45)

def get_circle_properties(radius):
    """Calculate circle properties and return multiple values."""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Storing multiple returned values
circle_area, circle_circumference = get_circle_properties(5)
print(f"Circle properties for radius 5:")
print(f"Area: {circle_area:.2f}")
print(f"Circumference: {circle_circumference:.2f}")

# === 4. FUNCTION THAT ACCEPTS DIFFERENT DATA TYPES ===
print("\n4) FUNCTION WITH DIFFERENT DATA TYPES")
print("-" * 42)

def process_data(data, multiplier):
    """Process different types of data and return results."""
    if isinstance(data, (int, float)):
        return data * multiplier
    elif isinstance(data, str):
        return data * multiplier  # String repetition
    elif isinstance(data, list):
        return [item * multiplier for item in data if isinstance(item, (int, float))]
    else:
        return "Unsupported data type"

# Testing with different data types
num_result = process_data(10, 3)
str_result = process_data("Hello", 2)
list_result = process_data([1, 2, 3], 4)

print(f"Number processing: process_data(10, 3) = {num_result}")
print(f"String processing: process_data('Hello', 2) = '{str_result}'")
print(f"List processing: process_data([1, 2, 3], 4) = {list_result}")

# === 5. FUNCTION COMPOSITION (CHAINING) ===
print("\n5) FUNCTION COMPOSITION - CHAINING FUNCTIONS")
print("-" * 50)

def add_five(number):
    """Add 5 to a number."""
    return number + 5

def multiply_by_two(number):
    """Multiply a number by 2."""
    return number * 2

def square(number):
    """Square a number."""
    return number ** 2

# Chaining functions together
initial_value = 3
step1 = add_five(initial_value)
step2 = multiply_by_two(step1)
final_result = square(step2)

print(f"Function chaining demonstration:")
print(f"Initial value: {initial_value}")
print(f"After add_five({initial_value}): {step1}")
print(f"After multiply_by_two({step1}): {step2}")
print(f"After square({step2}): {final_result}")

# One-liner chaining
chained_result = square(multiply_by_two(add_five(3)))
print(f"One-liner chaining: square(multiply_by_two(add_five(3))) = {chained_result}")

# === 6. COMMON FUNCTION MISTAKES (WHAT NOT TO DO) ===
print("\n6) COMMON FUNCTION MISTAKES - BEST PRACTICES")
print("-" * 50)

# BAD: Hardcoded values
def calculate_tax_bad():
    """Bad example - hardcoded values."""
    income = 50000  # Hardcoded!
    tax_rate = 0.2  # Hardcoded!
    return income * tax_rate

# GOOD: Accept parameters
def calculate_tax_good(income, tax_rate):
    """Good example - accepts parameters."""
    return income * tax_rate

# BAD: Printing instead of returning
def calculate_discount_bad(price):
    """Bad example - prints instead of returns."""
    discount = price * 0.1
    print(f"Discount: ${discount}")  # Should return instead!

# GOOD: Return the value
def calculate_discount_good(price):
    """Good example - returns the value."""
    return price * 0.1

# Demonstrate the difference
print("Bad example (hardcoded):")
bad_tax = calculate_tax_bad()
print(f"Result: ${bad_tax}")

print("\nGood example (with parameters):")
good_tax = calculate_tax_good(75000, 0.25)
print(f"Result: ${good_tax}")

print("\nPrint vs Return comparison:")
print("Function that prints (can't reuse the value):")
calculate_discount_bad(100)  # Only prints, can't reuse

print("Function that returns (can reuse the value):")
discount_amount = calculate_discount_good(100)
final_price = 100 - discount_amount
print(f"Discount: ${discount_amount}, Final price: ${final_price}")

print("\n" + "=" * 60)
print("DEMONSTRATION COMPLETE")
print("Key takeaways:")
print("- Functions should accept parameters instead of hardcoding values")
print("- Use return statements to send results back")
print("- Store returned values in variables for reuse")
print("- Chain functions together for complex operations")
print("- Avoid printing inside functions when you need to reuse results")
