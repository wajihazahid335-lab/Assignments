def validate_marks(scores):
    """Check the number of marks and their allowed range."""
    if len(scores) != 3:
        raise ValueError("Enter exactly three marks.")
    for score in scores:
        if not 0 <= score <= 100:
            raise ValueError("Marks must be between 0 and 100.")


def calculate_total(scores):
    return sum(scores)


def calculate_average(scores):
    return calculate_total(scores) / len(scores)


def determine_grade(average_marks):
    if average_marks >= 80:
        return "A"
    if average_marks >= 70:
        return "B"
    if average_marks >= 60:
        return "C"
    if average_marks >= 50:
        return "D"
    return "F"


def display_result(student_name, total_marks, average_marks, letter_grade):
    """Print values that have already been calculated."""
    print("\nStudent Result")
    print("----------------")
    print("Name:", student_name)
    print("Total:", total_marks)
    print("Average:", average_marks)
    print("Grade:", letter_grade)


def process_student(student_name, scores):
    """Coordinate validation, calculation, grading and display."""
    validate_marks(scores)
    total_marks = calculate_total(scores)
    average_marks = calculate_average(scores)
    letter_grade = determine_grade(average_marks)
    display_result(student_name, total_marks, average_marks, letter_grade)


def main():
    student_name = input("Enter student name: ")
    scores = []
    for subject_number in range(1, 4):
        scores.append(float(input(f"Enter marks for subject {subject_number}: ")))
    try:
        process_student(student_name, scores)
    except ValueError as validation_error:
        print("Invalid marks:", validation_error)


if __name__ == "__main__":
    main()
