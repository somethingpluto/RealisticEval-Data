def format_number(num: float) -> str:
    """Format the number into a more readable string representation, returning the original form if the number is less than 1,000.

    If it is greater than or equal to a thousand and less than a million, it is formatted as "x.xK".
    For a million or more, format it as "x.xM".

    Args:
        num (float): The number to be formatted.

    Returns:
        str: The formatted number as a string.
    """
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)