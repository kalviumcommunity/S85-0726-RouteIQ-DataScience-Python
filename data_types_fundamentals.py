"""
Python Collections Fundamentals
==============================
Milestone demonstration for lists, tuples, and dictionaries.
"""


def section(title):
    print(f"\n{title}")
    print("-" * len(title))


print("=" * 64)
print("PYTHON COLLECTIONS: LISTS, TUPLES, AND DICTIONARIES")
print("=" * 64)

# 1) LISTS
section("1. Working with Lists (ordered + mutable)")

tasks = ["Read instructions", "Write code", "Record video"]
print(f"Original list: {tasks}")
print(f"First task (index 0): {tasks[0]}")
print(f"Last task (index -1): {tasks[-1]}")

tasks[1] = "Write collections examples"
tasks.append("Submit PR")
removed_task = tasks.pop(0)

print(f"Updated list after modify/append/pop: {tasks}")
print(f"Removed task: {removed_task}")

print("\nIterating through list items:")
for position, task in enumerate(tasks, start=1):
    print(f"  {position}. {task}")

# 2) TUPLES
section("2. Working with Tuples (ordered + immutable)")

coordinates = (12.9716, 77.5946)
print(f"Tuple value: {coordinates}")
print(f"Latitude (index 0): {coordinates[0]}")
print(f"Longitude (index 1): {coordinates[1]}")

print("\nTuple immutability check:")
try:
    coordinates[0] = 10.0
except TypeError as error:
    print(f"  Cannot modify tuple item -> {error}")

print("Tuples are useful for fixed data (e.g., coordinates, IDs, constants).")

# 3) DICTIONARIES
section("3. Working with Dictionaries (key-value pairs)")

student = {"name": "Anita", "age": 21, "track": "Data Science"}
print(f"Original dictionary: {student}")
print(f"Access by key 'name': {student['name']}")
print(f"Access by key 'track': {student['track']}")

student["age"] = 22
student["city"] = "Bengaluru"
print(f"After update/add key-value pairs: {student}")

removed_track = student.pop("track")
print(f"Removed key 'track' with value: {removed_track}")
print(f"Dictionary now: {student}")

# 4) CHOOSING THE RIGHT STRUCTURE
section("4. Choosing the Right Data Structure")

choices = {
    "shopping_list": "list (items can be added/removed often)",
    "rgb_color": "tuple (fixed 3 values that should not change)",
    "user_profile": "dictionary (named fields like name/email/age)",
}

for scenario, recommendation in choices.items():
    print(f"- {scenario}: {recommendation}")

print("\nKey difference:")
print("  Lists and dictionaries are mutable.")
print("  Tuples are immutable.")

print("\n" + "=" * 64)
print("Collections milestone demonstration complete.")
print("=" * 64)
