import os

# ---------------- VALIDATION FUNCTIONS ---------------- #

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


# ---------------- FILE HANDLING ---------------- #

def load_file():
    file_data = {}
    stats = {"high": None, "low": None, "average": None}

    if not os.path.exists("grade.txt"):
        return file_data, stats

    section = "data"

    with open("grade.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line == "data:":
                section = "data"
                continue
            elif line == "stats:":
                section = "stats"
                continue

            # student data
            if section == "data" and line:
                parts = line.split(":")
                if len(parts) == 3:
                    name = parts[0].strip()
                    score = float(parts[1].strip())
                    grade = parts[2].strip()
                    file_data[name] = (score, grade)

            # statistics
            elif section == "stats" and line:
                key, value = line.split(":")
                key = key.strip()
                value = value.strip()

                if key in ["high", "low", "average"]:
                    stats[key] = float(value)

    return file_data, stats


def save_file(student_data, stats):
    with open("grade.txt", "w") as file:
        file.write("data:\n")
        for name, (score, grade) in student_data.items():
            file.write(f"{name}:{score}:{grade}\n")

        file.write("\nstats:\n")
        file.write(f"high:{stats['high']}\n")
        file.write(f"low:{stats['low']}\n")
        file.write(f"average:{stats['average']}\n")


# ---------------- CORE FUNCTIONS ---------------- #

def add_students(student_data, stats):
    num = get_valid_int("How many students do you want to add? ")

    new_added = False

    for _ in range(num):
        student_name = validate_name("Enter student name: ")

        if student_name in student_data:
            print("⚠️ Student already exists. Skipping...")
            continue

        score = get_valid_float("Enter score (1-100): ")

        if 90 <= score <= 100:
            letter = "A"
        elif 80 <= score < 90:
            letter = "B"
        elif 70 <= score < 80:
            letter = "C"
        elif 60 <= score < 70:
            letter = "D"
        else:
            letter = "F"

        student_data[student_name] = (score, letter)
        new_added = True

    if new_added:
        scores = [score for score, _ in student_data.values()]
        stats["high"] = max(scores)
        stats["low"] = min(scores)
        stats["average"] = sum(scores) / len(scores)

        save_file(student_data, stats)
        print("\n✅ Data saved.")
    else:
        print("\n⚠️ No new student added.")

    return student_data, stats


def display_data(student_data, stats):
    if not student_data:
        print("\n⚠️ No data saved yet.")
        return

    print("\n------ SAVED STUDENT GRADES ------")

    sorted_data = sorted(
        student_data.items(),
        key=lambda x: x[1][0],
        reverse=True
    )

    for i, (name, (score, grade)) in enumerate(sorted_data, start=1):
        print(f"{i}. {name.title()} - {grade} ({score})")

    print("\n------ SAVED STATISTICS ------")
    print(f"High: {stats['high']}")
    print(f"Low: {stats['low']}")
    print(f"Average: {stats['average']:.2f}")


def search_student(student_data):
    name = validate_name("Enter student name to search: ")

    if name in student_data:
        score, grade = student_data[name]
        print(f"\n🔎 RESULT: {name.title()} - {grade} ({score})")
    else:
        print("\n❌ Student not found.")


def reset_data():
    if os.path.exists("grade.txt"):
        os.remove("grade.txt")
        print("\n🗑️ All data deleted.")
    else:
        print("\n⚠️ No data file found.")


# ---------------- MAIN MENU ---------------- #

def main():
    while True:
        student_data, stats = load_file()

        print("\n========== MENU ==========")
        print("1. Add student grades")
        print("2. View saved data and statistics")
        print("3. Search student")
        print("4. Reset / Clear all data")
        print("5. Exit")
        print("==========================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_students(student_data, stats)

        elif choice == "2":
            display_data(student_data, stats)

        elif choice == "3":
            search_student(student_data)

        elif choice == "4":
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == "yes":
                reset_data()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
