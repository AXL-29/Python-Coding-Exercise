# Online Store Shipping & Split Cost Calculator
# Concepts:
# Numeric input
# Arithmetic operations
# Rounding
# Conditional statements (if / elif / else)
# Functions with return values
# Task Description: You are building a shopping/shipping helper for an online store. The program should:
# 1️⃣ Ask the user for:
    # Total purchase amount (a number, e.g., 1500.75)
    # Shipping type (local or international)
    # Number of people splitting the cost
# 2️⃣ Calculate:
    # Shipping cost based on your rules:
    # Local shipping → cheaper rate
    # International shipping → higher rate
    # Total amount including shipping
    # How much each person should pay (split evenly, rounded to 2 decimal places)
# 3️⃣ Handle input validation:
    # Purchase amount must be positive
    # Number of people must be at least 1
    # Shipping type must be either local or international
# Rules & Requirements
# Use a function that calculates the per-person cost, given purchase amount, shipping type, and number of people.
# If the number of people is less than 1 → display an error and do not do the calculation.
# Round the per-person amount to 2 decimal places.
# Print a clear summary:
    # Total purchase amount
    # Shipping cost
    # Total including shipping
    # Amount per person
# Optional Enhancements (not required)
    # Let the user enter shipping rates instead of hardcoding them
    # Show a friendly message if per-person cost is very high or very low
    # Add currency formatting (e.g., ₱ or $)

LOCAL = 100.00
INTERNATIONAL = 200.00
shipping_cost = 0

def per_person_cost(total_cost, to_split):
    per_people_bill = total_cost / to_split
    return round(per_people_bill, 2)

def format_currency(value):
    return f"${round(value, 2):,.2f}"

while True:
    try:
        total_purchased = float(input("Please enter the total purchase amount (e.g., 1599.50): $"))
        if total_purchased <= 0:
            print("Invalid input. Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number. Input must be a numeric value.")

while True:
    shipping_type = input("Select shipping type — local or international: ").lower()
    if shipping_type == "local":
        shipping_cost = LOCAL
        break
    elif shipping_type == "international":
        shipping_cost = INTERNATIONAL
        break
    else:
        print("Invalid option. Please type 'local' or 'international'.")

while True:
    try:
        split_count = int(input("How many people will split the total cost?: "))
        if split_count >= 1:
            if split_count == 1:
                print("No splitting actually happens")
            break
        else:
            print("Invalid number. Please enter a whole number greater than 0.")
    except ValueError:
        print("Invalid number. Please enter a valid number. Input must be a numeric value.")

total_amount = total_purchased + shipping_cost
amount_per_person = per_person_cost(total_amount, split_count)


print("\n------------------ ORDER SUMMARY ------------------")
print(f"Purchase Amount: {format_currency(total_purchased)}")
print(f"Shipping Type: {shipping_type.title()}")
print(f"Shipping Cost: {format_currency(shipping_cost)}")
print("---------------------------------------------------")
print(f"Total Amount (with shipping): {format_currency(total_amount)}")
print(f"Split Between: {split_count} person(s)")
print(f"Amount Per Person: {format_currency(amount_per_person)}")
print("---------------------------------------------------")
print("Thank you for using the Shipping & Split Calculator!")