def is_significant_number(input_value: str) -> bool:
    """
    Check if the given input is a significant number.

    A significant number is defined as a string that:
    - Has a length between 5 and 18 characters (inclusive).
    - Contains only digit characters.
    - Cannot start with '0' if its length is greater than 1.
    Args:
        input_value (str): The input value to be checked.

    Returns:
        bool: True if the input is a significant number, False otherwise.
    """
