def count_dashes(s: str) -> int:
    """Count the number of dashes in a string.

    Args:
        s (str): The string to count dashes in.

    Returns:
        int: The total count of dashes found in the string.
    """
    dash_count = 0
    for char in s:
        if char == '-':
            dash_count += 1
    return dash_count