"""
Video Demonstration Script for Readable Naming and Comments
==========================================================
This script is optimized for a ~2-minute screen recording.
Demonstrates readable variable names, basic PEP 8 conventions, and useful comments.
"""

print("READABLE PYTHON CODE - NAMING AND COMMENTS DEMO")
print("=" * 50)

# === 1) GOOD VS POOR VARIABLE NAMES ===
print("\n1) GOOD VS POOR VARIABLE NAMES")
print("-" * 31)

print("Poor naming example:")
x = 45000
y = 6
z = x / y
print(f"  x={x}, y={y}, z={z}")
print("  Problem: names do not explain what values represent.")

print("\nImproved naming example:")
monthly_revenue = 45000
active_customers = 6
average_revenue_per_customer = monthly_revenue / active_customers
print(
    "  monthly_revenue="
    f"{monthly_revenue}, active_customers={active_customers}, "
    f"average_revenue_per_customer={average_revenue_per_customer}"
)
print("  Improvement: names communicate intent clearly.")

# === 2) BASIC PEP 8 NAMING CONVENTIONS ===
print("\n2) BASIC PEP 8 NAMING CONVENTIONS")
print("-" * 34)

print("Using snake_case for variables:")
user_age = 24
is_profile_complete = True
total_session_minutes = 95
print(
    f"  user_age={user_age}, is_profile_complete={is_profile_complete}, "
    f"total_session_minutes={total_session_minutes}"
)

print("\nUsing UPPER_CASE for constants:")
MAX_LOGIN_ATTEMPTS = 5
DEFAULT_COUNTRY_CODE = "BD"
print(
    f"  MAX_LOGIN_ATTEMPTS={MAX_LOGIN_ATTEMPTS}, "
    f"DEFAULT_COUNTRY_CODE={DEFAULT_COUNTRY_CODE}"
)

# === 3) WRITING USEFUL COMMENTS (WHY, NOT WHAT) ===
print("\n3) USEFUL COMMENTS")
print("-" * 18)

order_amount = 120.0
customer_type = "member"

# Business rule: members spending at least 100 get free shipping.
if customer_type == "member" and order_amount >= 100:
    shipping_fee = 0
else:
    shipping_fee = 10

print(
    f"  customer_type={customer_type}, order_amount={order_amount}, "
    f"shipping_fee={shipping_fee}"
)
print("  Comment explains why this condition exists.")

print("\nAvoid obvious comments:")
print("  Bad: '# add 1 to counter' before 'counter += 1'")
print("  Better: comment only when logic needs context.")

# === 4) AVOIDING COMMON READABILITY MISTAKES ===
print("\n4) COMMON READABILITY MISTAKES TO AVOID")
print("-" * 39)
print("- Vague names like data, value, temp, x")
print("- Inconsistent style like userName and user_name in one file")
print("- Outdated comments that no longer match code behavior")
print("- Large blocks of commented-out old code")

# === 5) MINI CLEAN CODE EXAMPLE ===
print("\n5) MINI CLEAN CODE EXAMPLE")
print("-" * 26)

daily_steps = [4200, 7600, 8100, 5000]
step_goal = 7000
days_meeting_goal = 0

# Track how many days meet the fitness goal for weekly reporting.
for step_count in daily_steps:
    if step_count >= step_goal:
        days_meeting_goal += 1

print(f"  Daily steps: {daily_steps}")
print(f"  Step goal: {step_goal}")
print(f"  Days meeting goal: {days_meeting_goal}")

print("\nVideo checklist:")
print("- Show poor names and improved names")
print("- Show snake_case variables and UPPER_CASE constants")
print("- Show comments that explain why a rule exists")
print("- Explain why readability helps reviews and teamwork")

print("\nDemo complete!")
