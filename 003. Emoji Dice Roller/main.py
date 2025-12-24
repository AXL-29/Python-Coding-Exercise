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

def rolling_dice(num_of_dice):
    faces = []
    values = []

    for _ in range(num_of_dice):
        face, value = random.choice(DICE)
        faces.append(face)
        values.append(value)

    return faces, values

def number_of_dice(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive numeric value")
            elif value > 5:
                print("Please enter a number between 1 and 5 only")
            else:
                return value
        except ValueError:
            print("Please enter a numeric value only!")

def total_sum(rolled_dice_values):
    results = sum(rolled_dice_values)
    return results

def display_outputs(s_dice_faces,  s_sum_of_dice):
    print(f"Faces rolled: {s_dice_faces}")
    print(f"Total: {s_sum_of_dice}")

roll_to_dice = number_of_dice("Enter a number of dice to roll: ")
dice_faces, dice_values = rolling_dice(roll_to_dice)
sum_of_dice = total_sum(dice_values)
display_outputs(dice_faces, sum_of_dice)
