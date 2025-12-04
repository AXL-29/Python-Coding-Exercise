# Personal Profile Generator (Days 1–3)
# Concepts:
# variables
    # input
    # basic math
    # f-strings
    # string concatenation
# Task:
    # Make a program that collects:
    # Full name
    # Birth year
    # A goal for this year
# Then:
    # Calculate the user’s current age (using the current year of your choice)
    # Print a short “profile summary” message
    # Include the goal in a motivational sentence
# Rule:
    # Use two different ways to display variables in output.

from datetime import datetime

current_year = datetime.now().year
birth_year = 0

while True:
    full_name = input("Please enter your full name: ").title()
    if full_name.strip() == "" or not full_name.replace(" ", "").isalpha():  # isalpha() - checks if character is a letter (A-Z, a-z)
        print("Invalid input: names can only contain letters and spaces. Please try again.")
        continue
    else:
        break

while True:
    try:
        birth_year = int(input("Please enter your birth year (e.g., 2005): "))
        if birth_year >= current_year:
            print("Hmm… that year seems to be in the future. Please enter a valid birth year.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a valid year as a number.")

while True:
    goal = input("What is your goal for this year?: ")
    if goal.strip() == "":
        print("Goal cannot be empty. Please type something.")
        continue
    else:
        break


current_age = current_year - birth_year
in_another_five_years = current_age + 5

print("\n------------------- PROFILE SUMMARY -------------------")
print(f"Hello! My name is {full_name}, and I am currently {current_age} years old.")
print("My goal for this year is to become a " + goal + ", and I’m determined to achieve it!")
print(f"In 5 years, I will be {in_another_five_years} years old. Keep working towards your goal, you’ve got this!")