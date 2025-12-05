import random

COIN = [
    ("🪙 T", 0),
    ("🪙 H", 1)
]

def get_positive_int(prompt):
    """Ask the user for a positive integer and return it."""
    while True:
        try:
            value = int(input(prompt))
            if 0 < value <= 10:
                return value
            else:
                print("Invalid input: please enter a number greater than 0 but less than or equal 10")
        except ValueError:
            print("Invalid input: please enter a numeric value.")

def flip_coin(flip_count):
    """Get the number of flip count and return faces and values."""
    faces = []
    values = []

    for _ in range(flip_count):
        face, value = random.choice(COIN)
        faces.append(face)
        values.append(value)

    return faces, values

def display_results(faces, values):
    """Display Coin Flip and the total count of Tail and Head."""
    tail = values.count(0)
    head = values.count(1)

    print("\n------------- FLIP COIN GAME RESULTS -------------\n")
    print("Flip Coin:", " ".join(faces))
    print(f"Tail: {tail}")
    print(f"Head: {head}")

    # optional fun message
    if all(v == 1 for v in values):
        print("\nAll heads: Lucky!")
    elif all(v == 0 for v in values):
        print("\nAll tails: Better Luck Next Time!")

def game():
    """Main Loop"""
    while True:
        count = get_positive_int("How many times would you like to roll?: ")
        faces, values = flip_coin(count)
        display_results(faces, values)

        while True:
            flip_again = input("\nDo you want to flip again? (y/n): ").strip().lower()
            if flip_again in ("y", "yes"):
                break
            elif flip_again in ("n", "no"):
                print("Thank you for playing!")
                return
            else:
                print("Invalid input, please enter y or n.")

if __name__ == "__main__":
    game()