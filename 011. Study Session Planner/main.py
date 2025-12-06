def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid numeric value.")