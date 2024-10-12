def calculate_age(birth_date_string: str) -> str:
    """
    Calculates the age from the given birth date string and returns a string containing
    the original birth date and the calculated age. If the entered date string is invalid
    or empty, the function returns an empty string.

    Args:
        birth_date_string (str): The birth date as a string in a recognizable date format
                                  (e.g., 'YYYY-MM-DD').

    Returns:
        str: A string that includes the original birth date and the calculated age in the
             format 'birth_date_string (age)', or an empty string if the input is invalid.
    """