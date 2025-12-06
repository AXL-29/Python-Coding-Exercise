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


def get_student_score(students):
    student_grades = {}

    for _ in range(students):
        while True:
            student_name = validate_name("Enter student name: ")
            if student_name in student_grades:
                print("Student name already exists, please try another name.")
                continue
            else:
                break
        student_score = get_valid_float("Enter student score (1-100): ")

        if 90 <= student_score <= 100:
            letter_grade = 'A'
        elif 80 <= student_score < 90:
            letter_grade = 'B'
        elif 70 <= student_score < 80:
            letter_grade = 'C'
        elif 60 <= student_score < 70:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        student_grades[student_name] = (student_score, letter_grade)

    scores = [score for score, grade in student_grades.values()]

    high_score = max(scores)
    low_score = min(scores)
    average_score = sum(scores) / len(scores)

    return student_grades, high_score, low_score, average_score


def display_student_grades(student_grades, high_score, low_score, average_score):
    # Sort by score highest → lowest
    sorted_grades = sorted(
        student_grades.items(),
        key=lambda item: item[1][0],  # item[1][0] = score
        reverse=True
    )

    for idx, (student_name, (student_score, letter_grade)) in enumerate(sorted_grades, start=1):
        print(f"{idx}. {student_name.title()}: {letter_grade} - score: {student_score:.2f}")

    print("\n----------------- STATISTICS -----------------")
    print(f"Highest score: {high_score}")
    print(f"Lowest score: {low_score}")
    print(f"Average score: {average_score:.2f}")

def main():
    while True:
        num_of_students = get_valid_int("Enter number of students: ")
        grades, high, low, avg = get_student_score(num_of_students)
        display_student_grades(grades, high, low, avg)

        again = input("\nWould you like to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using this program, have a nice day!")
            break

if __name__ == "__main__":
    main()