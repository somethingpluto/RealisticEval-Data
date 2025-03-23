def check(candidate):

    # Check some simple cases
    assert candidate([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert candidate([1.2]) == ['D+']
    assert candidate([0.5]) == ['D-']
    assert candidate([0.0]) == ['E']
    assert candidate([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
    assert candidate([0, 0.7]) == ['E', 'D-']

    # Check some edge cases that are easy to work out by hand.
    assert True


def numerical_letter_grade(grades):
    """
    Given a list of GPAs, return a list of letter grades in the format A+, A,
    A-, B+, B, B-, C+, C, C-, D+, D, D-, E.
    
    Example:
    grades = [4.0, 3.0, 1.7, 2.0, 3.5]
    grade_equation = numerical_letter_grade(grades)
    print(grade_equation) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    # Create a dictionary to store the letter grades
    letter_grades = {}
    for GPA in grades:
        # Determine the letter grade based on the GPA
        if GPA > 4.0:
            letter_grades[GPA] = 'A+'
        elif GPA > 3.7:
            letter_grades[GPA] = 'A'
        elif GPA > 3.3:
            letter_grades[GPA] = 'A-'
        else:
            letter_grades[GPA] = 'B+'
        else:
            letter_grades[GPA] = 'B'
            
        # Update the dictionary for the next student
        if GPA in letter_grades:
            letter_grades[GPA] +=''
        else:
            letter_grades[GPA] = 'B+'
    
    # Output the list of letter grades
    grade_equation = [letter_grades.get(row, 'E') for row in zip(grades, grades[1:])]
    print(grade_equation)

candidate = numerical_letter_grade
check(candidate)