"""
Study Session Planner with Per-Subject Breaks

This program allows the user to:
1. Enter multiple subjects and their study durations.
2. Optionally add breaks per subject.
3. Calculate and display total study time including breaks.
4. Repeat planning for new sessions.
"""

def get_positive_integer(prompt):
    """Prompt the user for a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def collect_subjects_info(number_of_subjects):
    """
    Collect subject names and study durations from the user.

    Args:
        number_of_subjects (int): Number of subjects to enter.

    Returns:
        dict: Dictionary of {subject_name: study_duration_minutes}.
    """
    study_schedule = {}
    for _ in range(number_of_subjects):
        while True:
            subject_name = input("Enter subject name: ").strip().title()
            if not subject_name.replace(" ", "").isalpha():
                print("Subject name must contain only letters.")
            elif subject_name in study_schedule:
                print(f"Subject '{subject_name}' already exists. Please choose another name.")
            else:
                break
        duration = get_positive_integer(f"Enter study time in minutes for {subject_name}: ")
        study_schedule[subject_name] = duration
    return study_schedule

def add_breaks_per_subject(subjects):
    """
    Ask user if they want to add breaks per subject and calculate per-subject and total break time.

    Args:
        subjects (dict): Dictionary of subjects and their study durations.

    Returns:
        tuple: (breaks_per_subject, total_break_time)
    """
    breaks_per_subject = 0
    total_break_time = 0
    add_break = input("Do you want to add a break per subject? (yes/no): ").lower().strip()
    if add_break == "yes":
        breaks_per_subject = get_positive_integer("Enter break duration in minutes per subject: ")
        total_break_time = breaks_per_subject * len(subjects)
    return breaks_per_subject, total_break_time

def calculate_total_session_time(subjects, total_break):
    """
    Calculate total study time including breaks.

    Args:
        subjects (dict): Dictionary of subjects and their study durations.
        total_break (int): Total break time in minutes.

    Returns:
        int: Total session duration including breaks.
    """
    return sum(subjects.values()) + total_break

def display_session_summary(subjects, breaks_per_subject, total_session_time):
    """Display a formatted summary of the study session including per-subject breaks."""
    print("\n--------- STUDY SESSION SUMMARY ---------")
    for idx, (subject, duration) in enumerate(subjects.items(), start=1):
        if breaks_per_subject > 0:
            print(f"{idx}. {subject}: {duration} minutes + {breaks_per_subject} min break")
        else:
            print(f"{idx}. {subject}: {duration} minutes")
    print(f"\nTotal study time including breaks: {total_session_time} minutes\n")

def run_study_session_planner():
    """Main program loop for the Study Session Planner."""
    while True:
        num_subjects = get_positive_integer("How many subjects would you like to plan for?: ")
        study_schedule = collect_subjects_info(num_subjects)
        breaks_per_subject, total_break = add_breaks_per_subject(study_schedule)
        total_session_time = calculate_total_session_time(study_schedule, total_break)
        display_session_summary(study_schedule, breaks_per_subject, total_session_time)

        repeat = input("Do you want to plan another session? (yes/no): ").lower().strip()
        if repeat != "yes":
            print("Thank you for using the Study Session Planner!")
            break

if __name__ == "__main__":
    run_study_session_planner()
