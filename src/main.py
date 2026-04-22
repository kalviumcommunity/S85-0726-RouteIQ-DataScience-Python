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


# ============================================================================
# DataFrame Inspection Milestone: Using head(), info(), and describe()
# ============================================================================

import pandas as pd

print("\n" + "="*70)
print("DATAFRAME INSPECTION MILESTONE")
print("="*70)

# Load the sample dataset
df = pd.read_csv("data/raw/sample_routes.csv")

print("\n---- 1. Inspecting Data with head() ----")
print("Purpose: Preview the first few rows of the DataFrame")
print("Default: Shows first 5 rows")
print("\nUsing df.head():")
print(df.head())

print("\n\nUsing df.head(3) to show only 3 rows:")
print(df.head(3))

print("\n\nWhat head() reveals:")
print("- Column names and their order")
print("- Sample values in each column")
print("- Data alignment (e.g., dates, IDs)")
print("- Quick visual confirmation of data structure")


print("\n" + "-"*70)
print("\n---- 2. Inspecting Structure with info() ----")
print("Purpose: Understand DataFrame structure, data types, and memory usage")
print("\nUsing df.info():")
df.info()

print("\n\nWhat info() reveals:")
print("- Total number of rows (entries)")
print("- Column names and their data types (int, float, object, etc.)")
print("- Non-null count for each column (identifies missing values)")
print("- Memory usage of the DataFrame")
print("- Which columns may need type conversion or cleaning")


print("\n" + "-"*70)
print("\n---- 3. Summarizing Data with describe() ----")
print("Purpose: Get statistical summary of numeric columns")
print("\nUsing df.describe():")
print(df.describe())

print("\n\nWhat describe() reveals:")
print("- count: Number of non-null values")
print("- mean: Average value")
print("- std: Standard deviation (spread of data)")
print("- min: Minimum value")
print("- 25%: First quartile (25th percentile)")
print("- 50%: Median (50th percentile)")
print("- 75%: Third quartile (75th percentile)")
print("- max: Maximum value")
print("\nThis helps identify:")
print("- Potential outliers (values far from min/max)")
print("- Data distribution patterns")
print("- Range of values in each numeric column")


print("\n" + "-"*70)
print("\n---- 4. When to Use Each Method ----")
print("\nhead() - Use for:")
print("  - Quick visual preview of data")
print("  - Checking column names and sample values")
print("  - Verifying data loaded correctly")
print("  - Understanding data format before analysis")

print("\ninfo() - Use for:")
print("  - Understanding DataFrame structure")
print("  - Checking data types of columns")
print("  - Identifying missing values (non-null counts)")
print("  - Estimating memory usage")

print("\ndescribe() - Use for:")
print("  - Understanding numeric distributions")
print("  - Identifying potential outliers")
print("  - Getting quick statistical overview")
print("  - Understanding data range and spread")


print("\n" + "-"*70)
print("\n---- 5. Best Practice: Always Inspect Before Analysis ----")
print("\nInspection prevents:")
print("- Working with wrong data types")
print("- Missing hidden null values")
print("- Drawing incorrect conclusions")
print("- Wasting time on incorrect assumptions")

print("\nInspection workflow:")
print("1. Load data")
print("2. Use head() to preview")
print("3. Use info() to check structure")
print("4. Use describe() to understand numeric data")
print("5. Then proceed with cleaning and analysis")

print("\n" + "="*70)
print("DataFrame Inspection Milestone Complete")
print("="*70)