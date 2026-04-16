"""
Video Demonstration Script for Python Loops
===========================================
This script is optimized for a 2-minute screen recording.
Demonstrates for loops, while loops, break, continue, and infinite loop prevention.
"""

print("PYTHON LOOPS - VIDEO DEMONSTRATION")
print("=" * 50)

# === FOR LOOPS ===
print("\n1) FOR LOOP EXAMPLES")
print("-" * 20)

# For loop with range
print("For loop with range:")
for i in range(5):
    print(f"  Count: {i}")

# For loop with list
print("\nFor loop with list:")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(f"  Fruit: {fruit}")

# For loop with enumerate
print("\nFor loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# === WHILE LOOPS ===
print("\n2) WHILE LOOP EXAMPLES")
print("-" * 22)

# Basic while loop
print("While loop countdown:")
countdown = 3
while countdown > 0:
    print(f"  T-minus {countdown}")
    countdown -= 1
print("  Liftoff!")

# While loop with user input simulation
print("\nWhile loop with condition:")
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    print(f"  Attempt {attempts + 1} of {max_attempts}")
    attempts += 1
    if attempts == 2:
        print("  Success on attempt 2!")
        break

# === LOOP CONTROL ===
print("\n3) LOOP CONTROL: BREAK AND CONTINUE")
print("-" * 35)

# Break example
print("Break example (stop when found):")
numbers = [1, 3, 5, 7, 9, 2, 4, 6]
target = 2
for num in numbers:
    print(f"  Checking {num}")
    if num == target:
        print(f"  Found {target}! Stopping search.")
        break

# Continue example
print("\nContinue example (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  Odd number: {i}")

# === INFINITE LOOP PREVENTION ===
print("\n4) INFINITE LOOP PREVENTION")
print("-" * 27)

print("Safe while loop pattern:")
safe_counter = 0
max_iterations = 10
while safe_counter < max_iterations:
    print(f"  Safe iteration {safe_counter + 1}")
    safe_counter += 1
    # Always ensure loop condition changes!

print("\nCommon infinite loop causes to avoid:")
print("- Forgetting to update loop variable")
print("- Using wrong comparison operator")
print("- Loop condition that never becomes false")

# === PRACTICAL DATA PROCESSING ===
print("\n5) PRACTICAL DATA PROCESSING")
print("-" * 26)

# Process a list of numbers
data = [10, 20, 30, 40, 50]
print("Processing data with for loop:")
total = 0
for value in data:
    total += value
    print(f"  Added {value}, total: {total}")
print(f"Final total: {total}")

# Find items with while loop
print("\nFinding items with while loop:")
search_list = ["red", "blue", "green", "yellow"]
color_to_find = "green"
index = 0
while index < len(search_list):
    color = search_list[index]
    print(f"  Checking index {index}: {color}")
    if color == color_to_find:
        print(f"  Found {color_to_find} at index {index}")
        break
    index += 1

print("\nVideo checklist:")
print("- Show for loop with range and list")
print("- Show while loop with countdown")
print("- Demonstrate break stopping search early")
print("- Demonstrate continue skipping iterations")
print("- Explain infinite loop prevention")
print("- Show practical data processing examples")

print("\nDemo complete!")
