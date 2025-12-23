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

"""Online store shipping and bill-splitting calculator with input validation."""

LOCAL = 100
INTERNATIONAL = 200


def decimal_validation(prompt):
    """Validate and return a positive decimal number from user input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please input a positive number!")
            else:
                return value
        except ValueError:
            print("Please input a valid numeric value.")


def positive_int_validation(prompt):
    """Validate and return a positive integer greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")


def shipping_type(prompt):
    """Prompt for shipping type and return its name and cost."""
    while True:
        value = input(prompt).lower().strip()
        if value == "local":
            return value, LOCAL
        elif value == "international":
            return value, INTERNATIONAL
        else:
            print("Please choose either 'local' or 'international'.")


def calculate_total_bill(total_amount, shipping_cost):
    """Return the total bill including shipping cost."""
    return total_amount + shipping_cost


def calculate_split_bills(total_bill, people):
    """Return the evenly split bill amount per person."""
    return total_bill / people


def display_bills(total_amount, shipping_cost, total_bill, per_person, ship_type):
    """Display a formatted summary of the billing details."""
    print("\n--- BILL SUMMARY ---")
    print(f"Purchase amount: ${total_amount:.2f}")
    print(f"{ship_type.title()} shipping cost: ${shipping_cost:.2f}")
    print(f"Total including shipping: ${total_bill:.2f}")
    print(f"Amount per person: ${per_person:.2f}\n")


def main():
    """Control program flow and handle user interaction."""
    while True:
        total_amount = decimal_validation("Total purchase amount: $")
        ship_type, shipping_cost = shipping_type("Enter shipping type (local/international): ")
        people = positive_int_validation("Number of people splitting the bill: ")

        total_bill = calculate_total_bill(total_amount, shipping_cost)

        if people == 1:
            print("\nNothing to split.")
            print(f"Total bill: ${total_bill:.2f}")
        else:
            per_person = calculate_split_bills(total_bill, people)
            display_bills(total_amount, shipping_cost, total_bill, per_person, ship_type)

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using the split calculator app!")
            break


if __name__ == "__main__":
    main()