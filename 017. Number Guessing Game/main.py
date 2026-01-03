from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 100


def generate_number():
    """Generate a random number within the defined range."""
    return randint(LOWER_LIMIT, UPPER_LIMIT)


def get_guess(prompt):
    """Prompt the user for a valid guess within range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid numeric number only!")
        else:
            if value < LOWER_LIMIT or value > UPPER_LIMIT:
                print(f"Please choose a number between {LOWER_LIMIT} - {UPPER_LIMIT} only!")
            else:
                return value


def check_guess(guess, target):
    """Compare the user's guess with the target number."""
    if guess < target:
        return "low"
    elif guess > target:
        return "high"
    else:
        return "correct"


def play_game():
    """Control the game flow and track attempts."""
    attempts = 0
    target = generate_number()

    print(f"Guess the number between {LOWER_LIMIT} and {UPPER_LIMIT}")

    while True:
        guess = get_guess("Enter your guess: ")
        attempts += 1

        result = check_guess(guess, target)

        if result == "correct":
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
        else:
            print(f"Too {result}!")


if __name__ == "__main__":
    play_game()
