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
    """Rolls dice and returns the faces and total value."""
    faces = []
    total = 0

    for _ in range(num_of_dice):
        face, value = random.choice(DICE)
        faces.append(face)
        total += value

    return faces, total

def number_of_dice(prompt):
    """Prompts the user for a valid number of dice to roll."""
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Please enter a number greater than 0")
            elif value > 5:
                print("Please enter a number between 1 and 5 only")
            else:
                return value
        except ValueError:
            print("Please enter a numeric value only!")

def display_outputs(dice_faces, dice_total):
    """Displays the rolled dice faces and their total value."""
    print(f"Faces rolled: {dice_faces}")
    print(f"Total: {dice_total}")

def main():
    """Runs the dice roller application loop."""
    while True:
        dice_count = number_of_dice("Enter a number of dice to roll: ")
        faces, total = rolling_dice(dice_count)
        display_outputs(faces, total)

        if input("Do you want to roll again (yes/no): ").lower() != "yes":
            print("Thank you for using the dice roller application!")
            break

if __name__ == "__main__":
    main()
