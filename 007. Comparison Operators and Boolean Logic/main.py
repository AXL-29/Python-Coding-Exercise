def validate_number(prompt):
     """Validates that the number entered is a valid numeric value."""

     while True:
         try:
             value = float(input(prompt))
             return value
         except ValueError:
             print("Please enter a valid numeric value.")

def compare_numbers(num1, num2):
    """
    Compares two numbers and prints if:
    - They are equal
    - At least one number is negative
    - Both numbers are greater than 10.
    - if num1 is less than num2 or num1 is greater than num2.
    """

    if num1 > num2:
        print("The first number is greater than the second number.")
    elif num1 < num2:
        print("The first number is less than the second number.")
    else:
        print("The numbers are equal.")

    if num1 > 10 and num2 > 10:
        print("Both numbers are greater than 10.")
    if num1 < 0 or num2 < 0:
        print("At least one number is negative.")

def display_result():
    """Displays the result of the comparison."""

    number1 = validate_number("Enter first number: ")
    number2 = validate_number("Enter second number: ")

    print("\n----------------- COMPARISON RESULTS ----------------")
    compare_numbers(number1, number2)

def main():
    """The main function of the program."""
    while True:
        display_result()

        while True:
            compare_again = input("\nDo you want to compare again? (y/n): ").strip().lower()
            if compare_again in ("y", "yes"):
                break
            elif compare_again in ("n", "no"):
                print("Thank you for using comparison program.")
                return
            else:
                print("Please enter either 'y, yes' or 'no' only, please try again.")

if __name__ == "__main__":
    main()