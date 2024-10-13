def get_days_in_month(year: int, month: int) -> int:
    """
    Returns the number of days in a given month of a specific year.

    This function accounts for leap years when calculating the number of days in February.

    Args:
        year (int): The year for which to get the number of days in the month. This should be
                     a valid integer representing a year (e.g., 2024).
        month (int): The month for which to get the number of days. It should be an integer
                      between 1 and 12, where 1 corresponds to January and 12 to December.

    Returns:
        int: The number of days in the specified month of the specified year.
    """