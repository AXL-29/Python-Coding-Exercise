"""
Expense Tracker Program

This program allows the user to:
1. Add new expenses and save them to a file.
2. View the current session's expense summary.
3. View the all-time expense summary from saved data.
4. Exit the program.

Features:
- Preserves old data when adding new expenses.
- Validates numeric inputs and descriptions.
- Shows confirmation message after saving new data.
"""

import os

current_data = {}

def get_positive_int(prompt):
    """
    Prompt the user for a positive integer input.

    Args:
        prompt (str): The input message to show the user.

    Returns:
        int: A positive integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid numeric value.")

def get_positive_float(prompt):
    """
    Prompt the user for a positive float input.

    Args:
        prompt (str): The input message to show the user.

    Returns:
        float: A positive float entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive numeric number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid numeric value.")

def get_valid_description(prompt):
    """
    Prompt the user for a valid description (letters and spaces only).

    Args:
        prompt (str): The input message to show the user.

    Returns:
        str: A valid description entered by the user.
    """
    while True:
        value = input(prompt).strip().lower()
        if value and value.replace(" ", "").isalpha():
            return value
        else:
            print("Invalid input, letters and spaces only.")

def save_file():
    """
    Add new expenses to the current session and save them to 'data.txt'.
    Preserves old data from previous sessions.
    """
    # Load old file data
    file_data = {}
    if os.path.exists("data.txt"):
        with open("data.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                key, value = line.split(":", 1)
                file_data[key] = float(value)

    # Ask user for new expenses
    count = get_positive_int("How many expenses do you want to enter (1-20)?: ")
    for i in range(count):
        while True:
            description = get_valid_description("Enter description: ")
            if description in file_data or description in current_data:
                print("Description already exists. Please enter a new description.")
                continue
            break
        amount = get_positive_float("Enter amount: ")
        current_data[description] = amount

    # Merge old and new data and save
    file_data.update(current_data)
    with open("data.txt", "w") as file:
        for key, value in file_data.items():
            file.write(f"{key}: {value:.2f}\n")

    print("\n✅ Data has been successfully saved!")

def calculate_summary(data_dict):
    """
    Calculate total, highest, lowest, and average expenses for a given dataset.

    Args:
        data_dict (dict): Dictionary of expenses {description: amount}.

    Returns:
        tuple: (total, highest, lowest, average) expenses, or None if empty.
    """
    if not data_dict:
        return None
    total = sum(data_dict.values())
    highest = max(data_dict.values())
    lowest = min(data_dict.values())
    average = total / len(data_dict)
    return total, highest, lowest, average

def display_summary(total, highest, lowest, average, saved=False):
    """
    Display a formatted expense summary.

    Args:
        total (float): Total expense.
        highest (float): Highest expense.
        lowest (float): Lowest expense.
        average (float): Average expense.
        saved (bool): If True, shows a confirmation that data has been saved.
    """
    print("\n-------------- EXPENSE SUMMARY --------------")
    print(f"Total expense: {total:.2f}")
    print(f"Highest expense: {highest:.2f}")
    print(f"Lowest expense: {lowest:.2f}")
    print(f"Average expense: {average:.2f}")
    if saved:
        print("\n✅ Data has been successfully saved!")

def main():
    """
    Main program loop that allows the user to interact with the expense tracker.
    """
    while True:
        print("\nSelect an option:")
        print("1. Add new expenses")
        print("2. Show current session summary")
        print("3. Show all-time summary")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            save_file()
            # Show summary for current session after saving
            summary = calculate_summary(current_data)
            if summary:
                display_summary(*summary, saved=True)
        elif choice == "2":
            summary = calculate_summary(current_data)
            if summary:
                display_summary(*summary)
            else:
                print("No expenses entered in this session yet.")
        elif choice == "3":
            # Load all saved data from file
            if os.path.exists("data.txt"):
                file_data = {}
                with open("data.txt", "r") as file:
                    for line in file:
                        line = line.strip()
                        if not line:
                            continue
                        key, value = line.split(":", 1)
                        file_data[key] = float(value)
                summary = calculate_summary(file_data)
                if summary:
                    display_summary(*summary)
                else:
                    print("No saved expenses found.")
            else:
                print("No saved expenses found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()