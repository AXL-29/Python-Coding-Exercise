from datetime import date

def name_validation(prompt):
    """Prompts the user until a valid name containing only letters and spaces is entered."""
    while True:
        value = input(prompt)
        if value.replace(" ", "").strip().isalpha():
            return value
        else:
            print("Please enter a valid name that only consist of space and letters.")

def birth_year_validation(prompt):
    """Prompts the user until a valid numeric birth year within a realistic range is entered."""
    current_year = date.today().year
    while True:
        try:
            value = int(input(prompt))
            if value < 1900 or value > current_year:
                print("Please enter a valid birth year.")
            else:
                return value
        except ValueError:
            print("Please enter numbers only")

def calculate_age(s_birth_year):
    """Calculates the user's age based on the current year and given birth year."""
    return date.today().year - s_birth_year

def display_output(s_name, s_birth_year, s_age, s_goal):
    """Displays a formatted profile summary and a motivational message using different output styles."""
    print(f"My name is {s_name}. I am {s_age} years old, born in {s_birth_year}.")
    print("My current goal this year is to become a " + s_goal + ". I'm working on it every day!")

def main_loop():
    """Controls the program flow by collecting input, calculating age, and displaying results."""
    name = name_validation("Enter your name: ")
    birth_year = birth_year_validation("Enter your birth year: ")
    goal = input("Enter your goal this year: ")
    age = calculate_age(birth_year)

    display_output(name, birth_year, age, goal)

if __name__ == "__main__":
    main_loop()
