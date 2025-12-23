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