def get_positive_float(prompt):
    """Prompt for a positive numeric value and return it."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def validate_split(prompt):
    """Prompt for a positive whole number and return it."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a valid positive number of people.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_total_with_tip(amount, percentage):
    """Return the total bill including the tip percentage."""
    return amount * (1 + percentage / 100)

def calculate_split_amount(total, num_people):
    """Return bill amount per person."""
    return total / num_people

def print_bill_summary(amount_per_person, grand_total):
    """Prints formatted bill summary."""
    print("\n---------------- FINAL BILL PER PERSON ----------------")
    print(f"Total bill with tip: {grand_total:.2f}")
    print(f"Amount to pay per person: {amount_per_person:.2f}")

def main():
    """Program entry point."""
    while True:
        total_bill = get_positive_float("Enter total bill amount: ")
        tip_percentage = get_positive_float("Enter tip percentage (e.g., 10, 12, 15): ")
        num_people = validate_split("Enter number of people splitting: ")

        grand_total = calculate_total_with_tip(total_bill, tip_percentage)

        if num_people == 1:
            print(f"\nTotal bill with tip: {grand_total:.2f}")
            print("Only one person — no split required.")
        else:
            amount_per_person = calculate_split_amount(grand_total, num_people)
            print_bill_summary(amount_per_person, grand_total)

        while True:
            again = input("\nCalculate another bill? (y/n): ").lower().strip()
            if again in ("y", "yes"):
                break
            elif again in ("n", "no"):
                print("Thank you for using the tip calculator.")
                return
            else:
                print("Invalid choice — enter 'y' or 'n'.")

if __name__ == "__main__":
    main()