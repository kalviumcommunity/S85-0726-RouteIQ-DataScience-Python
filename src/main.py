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