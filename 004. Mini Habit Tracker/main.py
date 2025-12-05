# Mini Habit Tracker
# Concepts: dictionaries, loops, input validation, functions, basic calculations
# Objective: Build a small program that helps a user track daily habits and calculates completion stats.
# Requirements:
    # Collect Habits
    # Ask the user how many habits they want to track today.
    # For each habit, collect:
    # Habit name (string)
    # Did you complete it today? (yes/no)
# Store Data
    # Use a dictionary where:
    # Keys = habit names
    # Values = boolean (True for yes, False for no)
# Summary
    # Show a numbered list of habits with their completion status.
    # Show how many habits were completed and the percentage of completion.
    # Input Validation
    # Habit name cannot be empty
    # Completion input must be "yes" or "no" (case-insensitive).
# Rules to Follow
    # Use functions for adding habits and printing the summary.
    # Keep the main program loop clean and modular.
    # Handle all invalid inputs gracefully.
    # Display completion percentage rounded to 2 decimal places.

def get_positive_int(prompt):
    """Ask the user for a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_unique_habit(existing_habits):
    """Ask for a habit name that is not already in the dictionary."""
    while True:
        habit = input("Enter habit name: ").strip()
        if habit == "":
            print("Habit name cannot be empty.")
        elif habit in existing_habits:
            print("Habit already exists. Enter a different habit.")
        else:
            return habit

def get_yes_no(prompt):
    """Ask a yes/no question and return True for yes, False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        print("Please type 'yes' or 'no' only.")

def track_habits():
    habit_count = get_positive_int("How many habits do you want to track today?: ")
    habits = {}

    for _ in range(habit_count):
        name = get_unique_habit(habits)
        completed = get_yes_no("Did you complete it today? (yes/no): ")
        habits[name] = completed

    return habits

def display_summary(habits):
    print("\n--- Daily Habit Summary ---")
    completed_count = 0

    for idx, (name, done) in enumerate(habits.items(), start=1):
        status = "Completed" if done else "Incomplete"
        print(f"{idx}. {name} - {status}")
        if done:
            completed_count += 1

    percentage = round((completed_count / len(habits)) * 100, 2)
    print(f"Habit Completion Percentage: {percentage}%")

def main():
    habits = track_habits()
    display_summary(habits)

if __name__ == "__main__":
    main()
