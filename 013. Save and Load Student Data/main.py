def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number, kindly try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, kindly try again.")


def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 1 or value > 100:
                print("Please enter a valid numeric value between 1 - 100, kindly try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid numeric value, kindly try again.")


def validate_name(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value and value.replace(" ", "").isalpha():
            return value
        else:
            print("Invalid input, letters and spaces only.")

grades = {"Jade": (98, "A")}
count = get_valid_int("Enter a number: ")
for i in range(count):
    name = validate_name("Enter a name: ")
    score = get_valid_float("Enter a score: ")
    grade = input("Enter a grade: ")

    grades[name] = (score, grade)

    with open("grade.txt", "w") as file:
        for name, (score, grade) in grades.items():
            file.write(f"{name}: {score} : {grade}\n")