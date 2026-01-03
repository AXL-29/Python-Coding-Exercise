import random
from quiz_data import quiz_data

def ask_question(question_data):
    """
    Display a question, get the user's answer, and check if it is correct.
    Returns True if the answer is correct, otherwise False.
    """
    print(question_data["question"])
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == question_data["answer"].lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {question_data['answer']}\n")
        return False


def calculate_percentage(score, total_questions):
    """Calculate and return the percentage score."""
    return (score / total_questions) * 100


def run_quiz(question_data):
    """
    Run the quiz, track the score, and display the final results.
    """
    score = 0
    questions = question_data.copy()
    random.shuffle(questions)

    print("Welcome to the Python Quiz!\n")

    for question in questions:
        if ask_question(question):
            score += 1

    percentage = calculate_percentage(score, len(quiz_data))

    print("Quiz Finished!")
    print(f"Final Score: {score} / {len(quiz_data)}")
    print(f"Percentage: {percentage:.0f}%")

    if percentage >= 60:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def main():
    """Main entry point of the program."""
    run_quiz(quiz_data)


if __name__ == "__main__":
    main()