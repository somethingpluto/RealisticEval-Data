def is_compliant_four_digit(number):
    """
    Determines whether the given number is a compliant four-digit number.
    Compliance is defined as the number being between 1000 and 9999, inclusive.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if the number is a compliant four-digit number, False otherwise.
    """
    if not isinstance(number, int):
        return False  # Ensures the function only processes integers

    # Check if the number is strictly between 1000 and 9999
    return 1000 <= number <= 9999