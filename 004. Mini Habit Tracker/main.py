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


def habit_count():
    while True:
        try:
            number = int(input("How many habit you want to track today?: "))
            if number <= 0:
                print("Invalid input, please input a number more than 0.")
            else:
                return number
        except ValueError:
            print("Invalid input: Please type a numeric input only.")

def is_habit_completed(count):
    habit = {}
    for _ in range(count):
        while True:
            habit_name = input("What habit it is?: ")
            if habit_name not in habit:
                break
            else:
                print("Habit can't be the same, please enter different habit of yours.")
        while True:
            is_completed = input("Did you complete it today? (yes/no): ").lower()
            if is_completed == "yes":
                done = True
                break
            elif is_completed == "no":
                done = False
                break
            else:
                print("Please typed 'yes' or 'no' only. Try again.")

        # adding in dictionaries
        habit[habit_name] = done

    return habit

def calculate_completion(habits_dictionary, count):
    completed = 0
    for value in habits_dictionary.values():
        if value:
            completed += 1

    completion_percentage = round((completed / count), 2) * 100
    return completion_percentage


def display_habits_completion(habits_dictionary):
    """
    Displays the completion status (True/False) of habits.
    """
    idx = 1
    for habit_name, is_completed in habits_dictionary.items():
        if is_completed:
            status = "Completed"
        else:
            status = "Incomplete"
        # This print statement runs exactly once per habit
        print(f"{idx}. {habit_name} - {status}")
        idx += 1

def display_results():
    counts = habit_count()
    habits = is_habit_completed(counts)
    habit_percentage = calculate_completion(habits, counts)
    display_habits_completion(habits)
    print(f"Habit Completion Status: {habit_percentage}%")

display_results()


