"""
Video Demonstration Script for Python Collections
=================================================
This script is optimized for a 2-minute screen recording.
"""

print("PYTHON COLLECTIONS - VIDEO DEMONSTRATION")
print("=" * 50)

# === LISTS ===
print("\n1) LIST EXAMPLE")
print("-" * 15)

fruits = ["apple", "banana", "mango"]
print(f"Original list: {fruits}")
print(f"First item: {fruits[0]}")

fruits[1] = "orange"
fruits.append("grapes")
removed_item = fruits.pop(0)

print(f"After modify/add/remove: {fruits}")
print(f"Removed item: {removed_item}")

# === TUPLES ===
print("\n2) TUPLE EXAMPLE")
print("-" * 16)

weekdays = ("Mon", "Tue", "Wed")
print(f"Tuple: {weekdays}")
print(f"First day: {weekdays[0]}")

try:
    weekdays[0] = "Sunday"
except TypeError as error:
    print(f"Immutability behavior: {error}")

# === DICTIONARIES ===
print("\n3) DICTIONARY EXAMPLE")
print("-" * 21)

employee = {"name": "Ravi", "role": "Analyst", "id": 101}
print(f"Original dictionary: {employee}")
print(f"Access by key name: {employee['name']}")

employee["role"] = "Senior Analyst"
employee["location"] = "Remote"

print(f"After update/add: {employee}")

# === DIFFERENCES AND USE CASES ===
print("\n4) DIFFERENCES + USE CASES")
print("-" * 27)
print("List: mutable, best for dynamic ordered items.")
print("Tuple: immutable, best for fixed values.")
print("Dictionary: key-value mapping, best for entity data.")

print("\nVideo checklist:")
print("- Show list indexing and updates.")
print("- Show tuple indexing and immutability error.")
print("- Show dictionary key access and updates.")
print("- Explain when each structure is preferred.")

print("\nDemo complete.")
