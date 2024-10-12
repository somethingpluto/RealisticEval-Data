from datetime import datetime

def calculate_age(birth_date_string: str) -> int:
    """
    Calculates the age based on the provided birth date string.

    Args:
        birth_date_string (str): The birth date in string format (e.g., "YYYY-MM-DD").

    Returns:
        int: The calculated age or an error message if the date format is invalid.
    """
    try:
        # Parse the birth date string into a datetime object
        birth_date = datetime.strptime(birth_date_string, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please enter a valid date."

    # Get the current date
    today = datetime.now()

    # Calculate the age
    age = today.year - birth_date.year
    month_difference = today.month - birth_date.month

    # Adjust age if the current month is before the birth month
    # or if it's the birth month and the current date is before the birth date
    if month_difference < 0 or (month_difference == 0 and today.day < birth_date.day):
        age -= 1

    return age
