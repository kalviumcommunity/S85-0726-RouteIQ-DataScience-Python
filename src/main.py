# Basic Data Analysis Script

# Sample data
numbers = [10, 20, 30, 40, 50]

# Calculate sum
total = sum(numbers)

# Calculate average
average = total / len(numbers)

# Print results
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)

# Simple string example
name = "Nishant"
print("Hello,", name)

# Data insight message
if average > 25:
    print("Average is greater than 25")
else:
    print("Average is 25 or less")
    
    
    
    # Working with dictionary (data-like structure)
student = {
    "name": "Nishant",
    "marks": [80, 85, 90]
}

avg_marks = sum(student["marks"]) / len(student["marks"])
print("Student Average Marks:", avg_marks)



# Conditional Statements Demo

print("---- Basic if ----")
number = 10

if number > 5:
    print("Number is greater than 5")


print("\n---- if-else ----")
age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


print("\n---- if-elif-else ----")
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


print("\n---- Logical Operators ----")
temperature = 30
is_sunny = True

if temperature > 25 and is_sunny:
    print("It's a great day to go outside")

if temperature < 20 or not is_sunny:
    print("Maybe stay inside or carry a jacket")


print("\n---- String Condition ----")
name = "Nishant"

if name == "Nishant":
    print("Welcome Nishant!")
else:
    print("Unknown user")
    
    
    
    
    # Demonstrating readable variable names and meaningful comments (PEP 8)

# ❌ Poor variable naming (example - do not use in real code)
x = [10, 20, 30]
s = sum(x)
a = s / len(x)

print("Bad Example Output:", a)


# ✅ Good variable naming (PEP 8 style)
numbers_list = [10, 20, 30]

# Calculate total sum of numbers
total_sum = sum(numbers_list)

# Calculate average value of numbers
average_value = total_sum / len(numbers_list)

print("\nGood Example Output:")
print("Numbers:", numbers_list)
print("Total:", total_sum)
print("Average:", average_value)


# ✅ Using meaningful variable names for clarity
student_name = "Nishant"
student_marks = [80, 85, 90]

# Compute average marks to evaluate performance
average_marks = sum(student_marks) / len(student_marks)

# Decide grade based on average marks
if average_marks >= 85:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
else:
    grade = "C"

print("\nStudent Report:")
print("Name:", student_name)
print("Average Marks:", average_marks)
print("Grade:", grade)



# NumPy Basics: Element-wise operations and scalar operations

import numpy as np

print("---- Create NumPy Arrays ----")
array_a = np.array([10, 20, 30])
array_b = np.array([1, 2, 3])

print("Array A:", array_a)
print("Array B:", array_b)


print("\n---- Element-wise Operations ----")
addition_result = array_a + array_b
subtraction_result = array_a - array_b
multiplication_result = array_a * array_b
division_result = array_a / array_b

print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)


print("\n---- Scalar Operations ----")
add_scalar = array_a + 5          # add 5 to each element
multiply_scalar = array_a * 2     # multiply each element by 2

print("Array A + 5:", add_scalar)
print("Array A * 2:", multiply_scalar)


print("\n---- Python List vs NumPy Array ----")
list_a = [10, 20, 30]
list_b = [1, 2, 3]

print("List addition (concatenation):", list_a + list_b)
print("NumPy addition (element-wise):", array_a + array_b)


print("\n---- Shape Check (avoid mistakes) ----")
print("Shape of array_a:", array_a.shape)
print("Shape of array_b:", array_b.shape)