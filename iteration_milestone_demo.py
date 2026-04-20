"""
Video Demonstration Script for Python Iteration (Loops)
======================================================
This script is optimized for a ~2-minute screen recording.
Demonstrates for loops, while loops, break/continue, and safe termination.
"""

print("PYTHON LOOPS - ITERATION MILESTONE DEMO")
print("=" * 45)

# === 1) FOR LOOPS OVER RANGE ===
print("\n1) FOR LOOP WITH RANGE")
print("-" * 24)

print("Counting from 1 to 5:")
for number in range(1, 6):
    print(f"  Number: {number}")

# === 2) FOR LOOPS OVER COLLECTION ===
print("\n2) FOR LOOP WITH LIST")
print("-" * 23)

cities = ["Dhaka", "Chittagong", "Khulna", "Sylhet"]
print("Iterating through a list of cities:")
for city in cities:
    print(f"  City: {city}")

# === 3) WHILE LOOP WITH CONDITION ===
print("\n3) WHILE LOOP WITH CONDITION")
print("-" * 29)

attempt = 1
max_attempts = 3
while attempt <= max_attempts:
    print(f"  Attempt {attempt} of {max_attempts}")
    attempt += 1
print("While loop ended because condition became False.")

# === 4) LOOP FLOW CONTROL (BREAK / CONTINUE) ===
print("\n4) LOOP FLOW CONTROL")
print("-" * 20)

print("Break example: stop when value is found")
values = [4, 7, 9, 12, 15]
target = 12
for value in values:
    print(f"  Checking {value}")
    if value == target:
        print(f"  Found {target}; exiting loop with break.")
        break

print("\nContinue example: skip even numbers")
for number in range(1, 8):
    if number % 2 == 0:
        continue
    print(f"  Odd number: {number}")

# === 5) INFINITE LOOP PREVENTION ===
print("\n5) INFINITE LOOP PREVENTION")
print("-" * 28)

print("Safe while loop with clear update:")
counter = 0
limit = 5
while counter < limit:
    print(f"  Counter: {counter}")
    counter += 1  # Important: update loop variable so loop terminates
print("Loop stopped safely at the limit.")

print("\nCommon infinite loop causes:")
print("- Missing variable update inside while loop")
print("- Condition that never becomes False")
print("- Wrong comparison operator in condition")

# === 6) SIMPLE DATA WORKFLOW EXAMPLE ===
print("\n6) SIMPLE DATA WORKFLOW")
print("-" * 23)

numbers = [10, 20, 30, 40]
running_total = 0
for value in numbers:
    running_total += value
    print(f"  Added {value}, running total: {running_total}")
print(f"Final total: {running_total}")

print("\nVideo checklist:")
print("- Show for loop with range")
print("- Show for loop with a list")
print("- Show while loop with condition-based stopping")
print("- Demonstrate break and continue")
print("- Explain how infinite loops are prevented")

print("\nDemo complete!")
