"""
A menu-driven calculator that performs basic arithmetic operations,
validates numeric input, and continues running until the user exits.
"""


def get_number(prompt):
    """
    Prompt the user for a floating-point number and keep asking
    until a valid numeric value is entered.
    """
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            # Handles non-numeric input
            print("Please enter a valid numeric value")
        else:
            return value


def valid_int(prompt):
    """
    Prompt the user for an integer value and keep asking
    until a valid integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            # Handles invalid integer input
            print("Please enter a valid numeric number")
        else:
            return value


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Return the quotient of two numbers.
    If the divisor is zero, return None to indicate an invalid operation.
    """
    if b == 0:
        return None
    return a / b


def menu():
    """Display the calculator menu options."""
    print("\nCalculator Menu")
    print("---------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit\n")


def main():
    """
    Control the main program flow by displaying the menu,
    handling user choices, performing calculations,
    and exiting when requested.
    """
    while True:
        # Show menu options
        menu()

        # Get and validate the user's menu choice
        user_choice = valid_int("Enter your choice: ")

        # Exit condition
        if user_choice == 5:
            print("Thank you for using the Mini-Driven Calculator App!")
            break
        elif user_choice < 1 or user_choice > 5:
            # Handles invalid menu selections
            print("Invalid Choice, please type from 1 - 5 only!")
            continue

        # Collect numeric inputs for calculation
        first_number = get_number("Enter first number: ")
        second_number = get_number("Enter second number: ")

        # Perform the selected operation
        if user_choice == 1:
            result = add(first_number, second_number)
            print(f"The sum of two numbers is {result:.2f}")

        elif user_choice == 2:
            result = subtract(first_number, second_number)
            print(f"The difference of two numbers is {result:.2f}")

        elif user_choice == 3:
            result = multiply(first_number, second_number)
            print(f"The product of two numbers is {result:.2f}")

        else:
            result = divide(first_number, second_number)
            if result is None:
                # Handle division by zero safely
                print("Error: Cannot divide by zero")
            else:
                print(f"The quotient of two numbers is {result:.2f}")


# Entry point of the program
if __name__ == "__main__":
    main()
