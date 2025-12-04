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
    # Show individual dice faces and total sum.`



import random

dice_faces = ["🎲 1", "🎲 2", "🎲 3", "🎲 4", "🎲 5", "🎲 6"]
dice_value = [1, 2, 3, 4, 5, 6]

rolled_dice_faces = []

def roll_dice():
    global rolled_dice_faces
    while True:
        try:
            number_of_dice = int(input("How many dice you want to roll?: "))
            for dice in range(number_of_dice):
                dice = random.choice(dice_faces)
                rolled_dice_faces.append(dice)
            rolled_dice_faces = " ".join(rolled_dice_faces)
            return rolled_dice_faces
        except ValueError:
            print("Invalid Input: Only input a valid number.")

print(roll_dice())