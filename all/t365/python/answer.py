def day_of_week(year: int, month: int, day: int) -> int:
    """Calculate the day of the week for a given date.

    Args:
        year (int): The year of the date.
        month (int): The month of the date (1-12).
        day (int): The day of the month.

    Returns:
        int: The day of the week (1=Monday, 2=Tuesday, ..., 7=Sunday).
    """
    # Array representing the adjustment for the month
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # Adjust the year for January and February
    if month < 3:
        year -= 1

    # Calculate the day of the week
    result = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

    # Adjust result to correctly map Sunday as 7
    return 7 if result == 0 else result
