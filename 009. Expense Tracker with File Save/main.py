def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid numeric value.")\

def get_positive_float(prompt):
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
    while True:
        description = input(prompt).strip().lower()
        if description and description.replace(" ", "").isalpha():
            break
        else:
            print("Invalid input, letters and spaces only.")

get_positive_int("How may expenses do you want to enter (1-20)?: ")
get_valid_description("Enter description: ")
get_positive_float("Enter amount: ")