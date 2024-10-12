def set_eur_value(value):
    """
    Converts a numerical value into a string representation with appropriate
    suffixes ('k' for thousands, 'm' for millions) or returns the number as a string
    if the value is below 1000. Returns an empty string for non-numeric or invalid inputs.

    Args:
        value (str | int | float): The value to convert.

    Returns:
        str: The formatted string or an empty string if the input is invalid.
    """
    # Check for empty, None, or invalid inputs directly
    if value is None or (isinstance(value, (int, float)) and value == ''):
        return ''

    # Attempt to convert the input value to a float
    try:
        number = float(value)
    except ValueError:
        return ''

    # Check if the number is valid
    if number < 0:
        return ''

    # Determine the suffix and division based on the size of the number
    if number >= 1_000_000:
        return f"{number / 1_000_000:.1f}m"  # Format for millions
    elif number >= 1_000:
        return f"{number / 1_000:.1f}k"  # Format for thousands
    else:
        return str(int(number))  # Return as string for smaller numbers
