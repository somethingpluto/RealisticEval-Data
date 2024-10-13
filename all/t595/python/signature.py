def get_days_in_month(year: int, month: int) -> int:
    """
    Returns the number of days in a given month of a given year.
    This function accounts for leap years when determining the number of
    days in February. It raises a ValueError if the month is invalid.

    Args:
        year (int): The year to check (should be a positive integer).
        month (int): The month to check (1 for January, 12 for December).

    Returns:
        int: The number of days in the specified month of the specified year.
    """
