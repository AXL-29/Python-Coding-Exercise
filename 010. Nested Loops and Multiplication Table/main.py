"""
Task 7 – Multiplication Table Program (Interactive Version)

This program allows the user to:
1. Enter a number 'n' (1-12).
2. Print the multiplication table from 1 to 'n'.
3. Store the results in a dictionary where:
   - Key = multiplier (1 to n)
   - Value = tuple of results of multiplying the key with 1 to n.
4. Display the multiplication table and the dictionary.
5. Ask if the user wants to generate another table.
"""

def get_positive_int(prompt, min_value=1, max_value=12):
    """
    Prompt the user for a positive integer within a range.

    Args:
        prompt (str): Message to show the user.
        min_value (int): Minimum allowed value (default = 1)
        max_value (int): Maximum allowed value (default = 12)

    Returns:
        int: A valid positive integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def generate_multiplication_table(n):
    """
    Generate a multiplication table up to n x n and store it in a dictionary.

    Args:
        n (int): The highest multiplier and multiplicand.

    Returns:
        dict: Dictionary where key = multiplier, value = tuple of results.
    """
    table_dict = {}
    for i in range(1, n + 1):  # outer loop for multiplier
        row = []
        for j in range(1, n + 1):  # inner loop for multiplicand
            result = i * j
            print(f"{i} x {j} = {result}")  # print the multiplication
            row.append(result)
        table_dict[i] = tuple(row)  # store results as tuple
    return table_dict

def main():
    """Main function to run the multiplication table program interactively."""
    print("=== Multiplication Table Program ===")

    while True:  # loop for repeating the program
        n = get_positive_int("Enter a number for multiplication table (1-12): ")
        print(f"\nMultiplication Table (1 to {n}):")
        multiplication_dict = generate_multiplication_table(n)

        print("\nDictionary of results:")
        print(multiplication_dict)

        # Ask if the user wants to run the program again
        while True:
            again = input("\nDo you want to generate another table? (y/n): ").lower().strip()
            if again in ("y", "yes"):
                break
            elif again in ("n", "no"):
                print("Thank you for using the multiplication table program. Goodbye!")
                return
            else:
                print("Invalid choice — please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
