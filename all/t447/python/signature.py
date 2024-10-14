from typing import Union


def calculate_age(birth_date_string: str) -> Union[str,int]:
    """
    Calculate age based on the birth date string entered by the user.

    Input birth_date_string format such as "2000-01-01".

    Args:
        birth_date_string (str): The birth date in string format.

    Returns:
        str | int: The age as an integer or an error message as a string
                    if the date format is invalid.
    """