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