"""
A console-based program that collects user information, validates input,
calculates the user's age and favorite number parity, and displays
a formatted personal profile summary.
"""

from datetime import datetime


def validate_name(prompt):
    """Prompt the user for a valid name containing only letters and spaces."""
    while True:
        value = input(prompt)

        # Check if name contains only alphabet characters and spaces
        if value.strip().replace(" ", "").isalpha():
            return value
        else:
            print("Please try again, name can only consist of letter and space. Thank you")


def validate_positive_int(prompt):
    """Prompt the user for a positive integer value."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            # Handles non-numeric input
            print("Please try again, kindly enter a number only!")
        else:
            # Ensure the number is not negative
            if value < 0:
                print("Please try again, only positive numbers are accepted.")
            else:
                return value


def valid_birth_year(prompt, self_current_year):
    """Prompt the user for a valid birth year within an acceptable range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please try again, kindly enter a number only!")
        else:
            # Validate year range
            if value < 0:
                print("Please try again, only positive numbers are accepted.")
            elif value < 1970 or value > self_current_year:
                print("Please enter a valid year range from 1970 to present only")
            else:
                return value


def calculate_age(self_current_year, self_birth_year):
    """Calculate the user's age based on the current year and birth year."""
    age = self_current_year - self_birth_year
    return age


def favorite_number_type(self_favorite_number):
    """Determine whether the favorite number is even or odd."""
    if self_favorite_number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def display_profile(self_name, self_age, self_favorite_number, self_favorite_number_type):
    """Display the user's profile summary in a formatted output."""
    print("\nProfile Summary")
    print("---------------")
    print(f"Name: {self_name}")
    print(f"Age: {self_age}")
    print(f"Favorite Number: {self_favorite_number} ({self_favorite_number_type})")


def main():
    """Main function that controls program flow and function calls."""
    current_year = datetime.today().year

    # Collect and validate user inputs
    name = validate_name("Enter your name: ")
    birth_year = valid_birth_year("Enter your birth year: ", current_year)
    favorite_number = validate_positive_int("Enter your favorite number: ")

    # Perform calculations
    age = calculate_age(current_year, birth_year)
    number_type = favorite_number_type(favorite_number)

    # Display final profile
    display_profile(name, age, favorite_number, number_type)


# Entry point of the program
if __name__ == "__main__":
    main()
