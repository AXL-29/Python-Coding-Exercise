def validate_number(prompt):
    """Validates that the input is a numeric value."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid numeric value.")

def operators(prompt, num1, num2):
    """
    Let the user choose between +, -, *, / and return its calculated value.
    Prompt an error message that a user can't divide a number by zero.
    """
    while True:
        operator = input(prompt)
        if operator == "+":
            return num1 + num2, operator
        elif operator == "-":
            return num1 - num2, operator
        elif operator == "*":
            return num1 * num2, operator
        elif operator == "/":
            if num2 == 0:
                print("Sorry, you cannot divide a number by zero!")
                continue
            return num1 / num2, operator
        else:
            print("Please enter  a valid operator such as +, -, *, /.")

def display_result(result, num1, num2, operator):
    """Display the result of the calculation."""
    print(f"\nThe result is: {num1} {operator} {num2} = {result:.2f}")

def main():
    """Main function."""
    while True:
        number1 = validate_number("Please enter your first number: ")
        number2 = validate_number("Please enter your second number: ")
        calculated_result, user_operator = operators("Please select an operator (+, -, *, /): ", number1, number2)
        display_result(calculated_result, number1, number2, user_operator)

        calculate_again = input("\nDo you want to calculate again? (y/n): ").strip().lower()
        if calculate_again in ("y", "yes"):
            continue
        elif calculate_again in ("n", "no"):
            print("Thank you for using the calculator!")
            return
        else:
            print("Please typed 'y', 'yes', 'n' or 'no' only. Please try again.")

if __name__ == "__main__":
    main()