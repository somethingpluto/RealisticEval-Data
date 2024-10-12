def increment_number(num: float) -> float:
    """
    Increments the entered number.

    If the number is non-positive (<= 0), returns the original value.
    If the number is positive, returns the value plus 1.

    Args:
        num (float): The number to increment.

    Returns:
        float: The incremented value or the original number.
    """
    if num > 0:
        return num + 1  # Increment if positive
    return num  # Return original value if non-positive