def day_of_week(year: int, month: int, day: int) -> int:
    """
    Calculates the day of the week for a given date.

    Args:
        year (int): The year of the date (e.g., 2024).
        month (int): The month of the date (1 = January, 2 = February, ..., 12 = December).
        day (int): The day of the month (1 to 31, depending on the month).

    Returns:
        int: An integer representing the day of the week:
            - 1 for Monday
            - 2 for Tuesday
            - 3 for Wednesday
            - 4 for Thursday
            - 5 for Friday
            - 6 for Saturday
            - 7 for Sunday
    """