"""
Python Data Types Fundamentals
=============================
This script demonstrates Python's core numeric and string data types
as required for the Kalvium Data Science milestone.

Author: Data Science Student
Date: April 2026
"""

print("=" * 60)
print("PYTHON NUMERIC AND STRING DATA TYPES DEMONSTRATION")
print("=" * 60)

# 1. WORKING WITH NUMERIC DATA TYPES
print("\n1. NUMERIC DATA TYPES")
print("-" * 30)

# Integers (whole numbers)
integer_var = 42
negative_integer = -17
zero = 0

print(f"Integer examples:")
print(f"  Positive integer: {integer_var} (type: {type(integer_var)})")
print(f"  Negative integer: {negative_integer} (type: {type(negative_integer)})")
print(f"  Zero: {zero} (type: {type(zero)})")

# Floating-point numbers (decimal numbers)
float_var = 3.14159
negative_float = -2.718
scientific_notation = 1.5e4  # 15000

print(f"\nFloat examples:")
print(f"  Pi: {float_var} (type: {type(float_var)})")
print(f"  Negative float: {negative_float} (type: {type(negative_float)})")
print(f"  Scientific notation: {scientific_notation} (type: {type(scientific_notation)})")

# Basic arithmetic operations
print(f"\nArithmetic Operations:")
a = 10
b = 3

print(f"  Addition: {a} + {b} = {a + b}")
print(f"  Subtraction: {a} - {b} = {a - b}")
print(f"  Multiplication: {a} * {b} = {a * b}")
print(f"  Division: {a} / {b} = {a / b} (always returns float)")
print(f"  Integer division: {a} // {b} = {a // b}")
print(f"  Modulus: {a} % {b} = {a % b}")
print(f"  Exponentiation: {a} ** {b} = {a ** b}")

# Understanding division behavior
print(f"\nDivision Behavior:")
print(f"  5 / 2 = {5 / 2} (float division)")
print(f"  5 // 2 = {5 // 2} (integer division)")
print(f"  5 % 2 = {5 % 2} (remainder)")

# 2. UNDERSTANDING STRING DATA TYPES
print("\n\n2. STRING DATA TYPES")
print("-" * 30)

# Creating string variables
simple_string = "Hello, World!"
single_quotes = 'Python is fun'
multi_line = """This is a
multi-line string
that spans multiple lines"""

print(f"String examples:")
print(f"  Double quotes: {simple_string} (type: {type(simple_string)})")
print(f"  Single quotes: {single_quotes} (type: {type(single_quotes)})")
print(f"  Multi-line: {multi_line} (type: {type(multi_line)})")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(f"\nString Concatenation:")
print(f"  First name: {first_name}")
print(f"  Last name: {last_name}")
print(f"  Full name: {full_name}")

# String methods
text = "python programming"
print(f"\nString Methods:")
print(f"  Original: '{text}'")
print(f"  Uppercase: '{text.upper()}'")
print(f"  Capitalized: '{text.capitalize()}'")
print(f"  Length: {len(text)} characters")
print(f"  Contains 'python': {'python' in text}")

# String formatting
age = 25
height = 5.75
formatted_string = f"Name: {full_name}, Age: {age}, Height: {height}"
print(f"\nString Formatting:")
print(f"  {formatted_string}")

# 3. MIXING NUMBERS AND STRINGS SAFELY
print("\n\n3. MIXING NUMBERS AND STRINGS")
print("-" * 30)

# Common error - trying to concatenate numbers and strings
number = 42
text_message = "The answer is "

print("Type Mixing Examples:")
print(f"  Number: {number} (type: {type(number)})")
print(f"  Text: '{text_message}' (type: {type(text_message)})")

# This would cause an error:
# error_example = text_message + number  # TypeError!

# Correct way - convert number to string
correct_concatenation = text_message + str(number)
print(f"  Correct concatenation: '{correct_concatenation}'")

# Using f-strings (recommended approach)
f_string_example = f"The answer is {number}"
print(f"  f-string approach: '{f_string_example}'")

# Converting strings to numbers
string_number = "123"
string_float = "45.67"
non_numeric = "hello"

print(f"\nString to Number Conversion:")
print(f"  String '{string_number}' to int: {int(string_number)}")
print(f"  String '{string_float}' to float: {float(string_float)}")

# This would cause an error:
# try:
#     print(f"  String '{non_numeric}' to int: {int(non_numeric)}")
# except ValueError as e:
#     print(f"  Error converting '{non_numeric}': {e}")

# Safe conversion with error handling
def safe_to_int(value, default=0):
    """Safely convert string to integer with default fallback."""
    try:
        return int(value)
    except ValueError:
        print(f"    Warning: Could not convert '{value}' to int, using default {default}")
        return default

def safe_to_float(value, default=0.0):
    """Safely convert string to float with default fallback."""
    try:
        return float(value)
    except ValueError:
        print(f"    Warning: Could not convert '{value}' to float, using default {default}")
        return default

print(f"  Safe conversion examples:")
print(f"    '{string_number}' -> {safe_to_int(string_number)}")
print(f"    '{string_float}' -> {safe_to_float(string_float)}")
print(f"    '{non_numeric}' -> {safe_to_int(non_numeric)}")

# 4. INSPECTING DATA TYPES
print("\n\n4. INSPECTING DATA TYPES")
print("-" * 30)

# Create variables of different types
variables = {
    "integer": 42,
    "float": 3.14,
    "string": "hello",
    "boolean": True,
    "none": None,
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    "dict": {"key": "value"}
}

print("Type Inspection Examples:")
for name, value in variables.items():
    print(f"  {name}: {value} -> type: {type(value).__name__}")

# Type checking functions
print(f"\nType Checking Functions:")
x = 42
y = "42"

print(f"  Variable x = {x}")
print(f"    Is integer? {isinstance(x, int)}")
print(f"    Is string? {isinstance(x, str)}")
print(f"    Is number? {isinstance(x, (int, float))}")

print(f"  Variable y = '{y}'")
print(f"    Is integer? {isinstance(y, int)}")
print(f"    Is string? {isinstance(y, str)}")
print(f"    Is number? {isinstance(y, (int, float))}")

# 5. PRACTICAL EXAMPLES
print("\n\n5. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Simple calculator
print("Example 1: Simple Calculator")
def simple_calculator(a, b, operation):
    """Perform basic arithmetic operations."""
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b if b != 0 else "Error: Division by zero"
        else:
            return "Error: Unknown operation"
    except TypeError:
        return "Error: Invalid data types"

result1 = simple_calculator(10, 5, "add")
result2 = simple_calculator(10, 5, "divide")
result3 = simple_calculator("10", "5", "add")  # This will work with string concatenation

print(f"  10 + 5 = {result1}")
print(f"  10 / 5 = {result2}")
print(f"  '10' + '5' = {result3}")

# Example 2: Data processing simulation
print(f"\nExample 2: Data Processing Simulation")
student_data = [
    ("Alice", "85", "92.5"),
    ("Bob", "78", "88.0"),
    ("Charlie", "92", "95.5")
]

def process_student_data(data):
    """Process student data with proper type handling."""
    processed = []
    for name, midterm_str, final_str in data:
        try:
            midterm = float(midterm_str)
            final = float(final_str)
            average = (midterm + final) / 2
            processed.append({
                "name": name,
                "midterm": midterm,
                "final": final,
                "average": average,
                "grade": "A" if average >= 90 else "B" if average >= 80 else "C"
            })
        except ValueError as e:
            print(f"    Error processing {name}: {e}")
    
    return processed

processed_data = process_student_data(student_data)
print("  Processed Student Data:")
for student in processed_data:
    print(f"    {student['name']}: Avg={student['average']:.1f}, Grade={student['grade']}")

# Example 3: String formatting for reports
print(f"\nExample 3: Report Generation")
def generate_report(title, data):
    """Generate a formatted report."""
    report = f"""
{'=' * 40}
{title.upper()}
{'=' * 40}
"""
    for i, item in enumerate(data, 1):
        report += f"{i}. {item}\n"
    
    report += f"\nTotal items: {len(data)}"
    return report

report_data = ["Introduction to Python", "Data Types", "Control Flow", "Functions"]
report = generate_report("Python Course Outline", report_data)
print(report)

# 6. COMMON PITFALLS AND SOLUTIONS
print("\n\n6. COMMON PITFALLS AND SOLUTIONS")
print("-" * 30)

print("Common Issues and How to Avoid Them:")

# Pitfall 1: Integer division in Python 2 vs Python 3
print(f"\n1. Division Behavior:")
print(f"  Python 3: 5 / 2 = {5 / 2} (always float)")
print(f"  Python 3: 5 // 2 = {5 // 2} (integer division)")

# Pitfall 2: String vs number comparison
print(f"\n2. Comparison Issues:")
print(f"  10 == '10': {10 == '10'} (False - different types)")
print(f"  str(10) == '10': {str(10) == '10'} (True - same types)")

# Pitfall 3: Precision with floats
print(f"\n3. Float Precision:")
print(f"  0.1 + 0.2 = {0.1 + 0.2}")
print(f"  Is 0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
print(f"  Use round() for comparison: round(0.1 + 0.2, 10) == round(0.3, 10) = {round(0.1 + 0.2, 10) == round(0.3, 10)}")

# Pitfall 4: String immutability
print(f"\n4. String Immutability:")
text = "hello"
print(f"  Original: {text}")
# text[0] = "H"  # This would cause an error!
new_text = text.upper()  # Create new string instead
print(f"  Modified: {new_text}")

print("\n" + "=" * 60)
print("END OF DEMONSTRATION")
print("=" * 60)
print("\nKey Takeaways:")
print("1. Always be aware of your variable types")
print("2. Use type() and isinstance() to check types")
print("3. Convert types explicitly when needed")
print("4. Use f-strings for clean string formatting")
print("5. Handle type conversion errors gracefully")
print("6. Understand the difference between / and // operators")
