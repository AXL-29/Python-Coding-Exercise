# Task 3 – Emoji Dice Roller
# Concepts: random, lists, indexing, loops, conditionals
# Objective
    # Create a mini dice-rolling game that uses emojis to represent dice faces. This exercise helps practice randomness, lists, and basic branching logic.
# Requirements
    # Dice Faces
        # Prepare a set of 6 dice faces, each with a unique emoji or text representation (e.g., 🎲1, 🎲2… or any emojis you like).
        # Each face should correspond to a numeric value 1–6 internally.
    # User Input
        # Ask the user how many dice they want to roll.
        # Valid input range: 1–5.
    # Rolling the Dice
        # Simulate rolling the chosen number of dice using randomness.
        # Display each dice roll’s emoji face.
        # Show the total sum of all dice rolled.
    # Input Validation
        # If the user enters a number less than 1 or greater than 5, display an error message and don’t roll.
        # Make sure invalid input (non-numeric) is handled gracefully.
# Optional Enhancements
    # Allow the user to roll again without restarting the program.
    # Give fun messages for certain totals (e.g., “Jackpot!” if all dice show 6).
    # Include a short menu for rolling 1–5 dice multiple times.
# Rules to Follow
    # Use lists to store dice faces.
    # Use random.choice() or random.randint() for rolling.
    # Keep user input validation robust.
    # Show individual dice faces and total sum.

import random

DICE = [
    ("🎲 1", 1),
    ("🎲 2", 2),
    ("🎲 3", 3),
    ("🎲 4", 4),
    ("🎲 5", 5),
    ("🎲 6", 6)
]

def get_user_dice_count():
    """Ask user how many dice to roll, return integer 1-5."""
    while True:
        try:
            dice_count = int(input("How many dice do you want to roll? (1-5): "))
            if 1 <= dice_count <= 5:
                return dice_count
            print("Invalid number. Please enter between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number input")

def roll_dice(count):
    """
    Roll `count` dice.
    Returns two lists: faces (emojis) and values (ints).
    """

    faces = []
    values = []

    for _ in range(count):
        face, value = random.choice(DICE)
        faces.append(face)
        values.append(value)

    return faces, values

def display_results(faces, values):
    """Display individual dice rolled and their sum."""
    print("\n--- Dice Result ---")
    print("Rolled:", " ".join(faces))
    print("Total:", sum(values))

    # Optional fun message
    if all(v == 6 for v in values):
        print("Jackpot! ALL sixes!")
    elif sum(values) >= (6 * len(values)) - 1:
        print("Almost perfect roll!")

def game():
    """Main game loop"""
    while True:
        count = get_user_dice_count()
        faces, values = roll_dice(count)
        display_results(faces, values)

        again = input("\nRoll again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    game()