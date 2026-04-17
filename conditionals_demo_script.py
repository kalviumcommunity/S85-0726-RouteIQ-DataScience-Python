"""
Video Demonstration Script for Python Conditionals
=================================================
This script is optimized for a ~2-minute screen recording.
Demonstrates if, if-else, if-elif-else, and logical operators.
"""

print("PYTHON CONDITIONALS - VIDEO DEMONSTRATION")
print("=" * 52)

# === 1) BASIC IF STATEMENTS ===
print("\n1) BASIC IF STATEMENT")
print("-" * 22)

temperature_c = 31
print(f"Temperature: {temperature_c}C")
if temperature_c > 30:
    print("It is a hot day.")

temperature_c = 25
print(f"Temperature: {temperature_c}C")
if temperature_c > 30:
    print("This line will not run because the condition is False.")
print("Condition checked; program continues.")

# === 2) IF-ELSE BRANCHING ===
print("\n2) IF-ELSE BRANCHING")
print("-" * 21)

age = 16
print(f"Age: {age}")
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote yet.")

# === 3) IF-ELIF-ELSE MULTIPLE CONDITIONS ===
print("\n3) IF-ELIF-ELSE EXAMPLE")
print("-" * 25)

score = 84
print(f"Score: {score}")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs improvement")

# === 4) STRING CONDITIONS ===
print("\n4) STRING-BASED CONDITION")
print("-" * 26)

status = "active"
print(f"Status: {status}")
if status == "active":
    print("Account is active.")
elif status == "pending":
    print("Account setup is pending.")
else:
    print("Account is inactive.")

# === 5) LOGICAL OPERATORS (and, or, not) ===
print("\n5) LOGICAL OPERATORS")
print("-" * 20)

hours_studied = 3
attendance_percent = 92
print(f"Hours studied: {hours_studied}, attendance: {attendance_percent}%")
if hours_studied >= 2 and attendance_percent >= 90:
    print("Ready for assessment (and example).")

payment_method = "card"
has_coupon = False
print(f"Payment method: {payment_method}, has coupon: {has_coupon}")
if payment_method == "card" or has_coupon:
    print("Discount rule applies (or example).")

is_weekend = False
print(f"Is weekend: {is_weekend}")
if not is_weekend:
    print("Today is a weekday (not example).")

# === 6) SIMPLE DATA WORKFLOW SCENARIO ===
print("\n6) SIMPLE DATA WORKFLOW SCENARIO")
print("-" * 33)

order_total = 120.0
is_member = True
country = "US"
print(f"Order total: ${order_total}, member: {is_member}, country: {country}")

if order_total >= 100 and is_member:
    shipping = 0
    print("Free shipping applied (member + minimum spend).")
elif country == "US":
    shipping = 8
    print("Standard domestic shipping applied.")
else:
    shipping = 15
    print("International shipping applied.")

print(f"Final shipping charge: ${shipping}")

print("\nVideo checklist:")
print("- Show simple if with true and false outcomes")
print("- Show if-else with two clear branches")
print("- Show if-elif-else with ordered conditions")
print("- Show and/or/not in practical examples")
print("- Explain why each branch ran")

print("\nDemo complete!")
