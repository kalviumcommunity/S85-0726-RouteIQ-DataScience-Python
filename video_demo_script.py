"""
Video Demonstration Script for Python Data Types
==============================================
This is a simplified script perfect for a 2-minute video demonstration.
It focuses on the most important concepts for the milestone.

Run this script while recording your screen for the video submission.
"""

print("🎬 PYTHON DATA TYPES - VIDEO DEMONSTRATION")
print("=" * 50)

# === NUMERIC DATA TYPES ===
print("\n📊 NUMERIC DATA TYPES")
print("-" * 25)

# Integer examples
age = 25
temperature = -5
count = 0

print(f"Integer examples:")
print(f"  Age: {age} (type: {type(age).__name__})")
print(f"  Temperature: {temperature} (type: {type(temperature).__name__})")
print(f"  Count: {count} (type: {type(count).__name__})")

# Float examples
price = 19.99
pi = 3.14159
average = 87.5

print(f"\nFloat examples:")
print(f"  Price: ${price} (type: {type(price).__name__})")
print(f"  Pi: {pi} (type: {type(pi).__name__})")
print(f"  Average: {average}% (type: {type(average).__name__})")

# Basic arithmetic
print(f"\nBasic arithmetic:")
print(f"  10 + 5 = {10 + 5}")
print(f"  10 / 3 = {10 / 3} (always returns float)")
print(f"  10 // 3 = {10 // 3} (integer division)")

# === STRING DATA TYPES ===
print("\n📝 STRING DATA TYPES")
print("-" * 25)

# String creation
name = "Alice"
message = 'Hello, Python!'
multi_line = """Line 1
Line 2"""

print(f"String examples:")
print(f"  Name: {name} (type: {type(name).__name__})")
print(f"  Message: {message} (type: {type(message).__name__})")
print(f"  Length of name: {len(name)} characters")

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(f"\nString operations:")
print(f"  First name: {first_name}")
print(f"  Last name: {last_name}")
print(f"  Combined: {full_name}")
print(f"  Uppercase: {full_name.upper()}")

# === TYPE MIXING AND CONVERSION ===
print("\n🔄 TYPE MIXING & CONVERSION")
print("-" * 30)

# Common issue: mixing types
number = 42
text = "The answer is "

print(f"Type mixing:")
print(f"  Number: {number} (type: {type(number).__name__})")
print(f"  Text: '{text}' (type: {type(text).__name__})")

# Correct ways to combine
method1 = text + str(number)  # Convert to string
method2 = f"The answer is {number}"  # f-string (recommended)

print(f"  Method 1 (str()): {method1}")
print(f"  Method 2 (f-string): {method2}")

# String to number conversion
age_string = "25"
price_string = "19.99"

print(f"\nString to number conversion:")
print(f"  '{age_string}' → {int(age_string)} (integer)")
print(f"  '{price_string}' → {float(price_string)} (float)")

# === TYPE INSPECTION ===
print("\n🔍 TYPE INSPECTION")
print("-" * 20)

# Check types of different variables
variables = [42, 3.14, "hello", True, None]

print(f"Checking types:")
for var in variables:
    var_type = type(var).__name__
    print(f"  {var} → {var_type}")

# Using isinstance for type checking
value = 42
print(f"\nType checking with isinstance():")
print(f"  Is {value} an integer? {isinstance(value, int)}")
print(f"  Is {value} a string? {isinstance(value, str)}")
print(f"  Is {value} a number? {isinstance(value, (int, float))}")

# === KEY TAKEAWAYS ===
print("\n🎯 KEY TAKEAWAYS")
print("-" * 20)
print("1. Numbers: int (whole) and float (decimal)")
print("2. Strings: text data, use quotes")
print("3. Convert types explicitly with str(), int(), float()")
print("4. Use f-strings for clean formatting")
print("5. Check types with type() and isinstance()")
print("6. Always be aware of your data types!")

print(f"\n✅ Demo complete! Ready for video recording.")
