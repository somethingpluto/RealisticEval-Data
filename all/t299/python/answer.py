from datetime import datetime


def calculate_age(birth_date_string):
    """
    Calculates the age based on the birth date string.

    Args:
        birth_date_string (str): The birth date in string format (e.g., 'YYYY-MM-DD').

    Returns:
        str: A string representing the birth date and age, or an empty string if the input is invalid.
    """
    # Check if the input is valid
    if not birth_date_string:
        return ''

    try:
        birth_date = datetime.strptime(birth_date_string, '%Y-%m-%d')
    except ValueError:
        return ''  # Return empty string if the date is invalid

    today = datetime.now()
    age = today.year - birth_date.year

    # Check if the birthday has passed this year
    is_birthday_passed = (today.month > birth_date.month or
                          (today.month == birth_date.month and today.day >= birth_date.day))

    if not is_birthday_passed:
        age -= 1

    return f"{birth_date_string} ({age})"
