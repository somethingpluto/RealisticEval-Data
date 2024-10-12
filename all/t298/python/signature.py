def set_eur_value(value):
    """
    Converts a numerical value into a string representation with appropriate
    suffixes ('k' for thousands, 'm' for millions) or returns the number as a string
    if the value is below 1000. Returns an empty string for non-numeric or invalid inputs.

    Args:
        value (Union[str, int, float]): The value to convert.

    Returns:
        str: The formatted string or an empty string if the input is invalid.
    """