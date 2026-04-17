"""
Video Demonstration Script for Function Parameters and Return Values
=====================================================================
This script is optimized for a 2-minute screen recording.
"""

print("FUNCTION PARAMETERS AND RETURN VALUES - VIDEO DEMO")
print("=" * 55)

# === 1. FUNCTION WITH PARAMETERS ===
print("\n1) FUNCTION WITH PARAMETERS")
print("-" * 30)

def greet_person(name, age):
    """Accept parameters and return a greeting."""
    return f"Hello {name}, you are {age} years old!"

# Call function with arguments
result = greet_person("Alice", 25)
print(f"Function call: greet_person('Alice', 25)")
print(f"Returned: {result}")

# === 2. CALCULATION FUNCTION ===
print("\n2) CALCULATION FUNCTION")
print("-" * 28)

def calculate_area(length, width):
    """Calculate area and return result."""
    return length * width

# Use returned value for further computation
area = calculate_area(10, 5)
cost = area * 50
print(f"Area: calculate_area(10, 5) = {area}")
print(f"Cost calculation: {area} * 50 = ${cost}")

# === 3. MULTIPLE RETURN VALUES ===
print("\n3) MULTIPLE RETURN VALUES")
print("-" * 30)

def get_stats(numbers):
    """Return multiple statistics."""
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Store multiple returned values
numbers = [10, 20, 30, 40]
total, average = get_stats(numbers)
print(f"Stats for {numbers}:")
print(f"Total: {total}, Average: {average}")

# === 4. FUNCTION CHAINING ===
print("\n4) FUNCTION CHAINING")
print("-" * 24)

def add_five(n):
    return n + 5

def multiply_by_two(n):
    return n * 2

# Chain functions together
result = multiply_by_two(add_five(3))
print(f"Chaining: multiply_by_two(add_five(3)) = {result}")
print(f"Step 1: add_five(3) = {add_five(3)}")
print(f"Step 2: multiply_by_two({add_five(3)}) = {result}")

# === 5. BEST PRACTICES ===
print("\n5) BEST PRACTICES")
print("-" * 18)

# GOOD: Accept parameters, return value
def calculate_discount(price, percentage):
    """Good example - accepts parameters and returns value."""
    return price * (percentage / 100)

# Use the returned value
discount = calculate_discount(100, 10)
final_price = 100 - discount
print(f"Discount: ${discount}, Final price: ${final_price}")

print("\nVideo checklist:")
print("- Show function definition with parameters")
print("- Demonstrate calling function with arguments")
print("- Show return statement and returned value")
print("- Use returned value in further calculation")
print("- Explain function chaining concept")

print("\nDemo complete!")
