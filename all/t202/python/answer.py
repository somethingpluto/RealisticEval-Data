class InvalidMonthError(Exception):
    """Custom exception for invalid month values."""
    pass

def get_days_in_month(year: int, month: int) -> int:
    """
    Returns the number of days in a given month of a specific year.

    This function accounts for leap years when calculating the number of days in February.

    :param year: The year for which to get the number of days in the month. This should be
                 a valid integer representing a year (e.g., 2024).
    :param month: The month for which to get the number of days. It should be an integer
                  between 1 and 12, where 1 corresponds to January and 12 to December.
    :return: The number of days in the specified month of the specified year.
    """
    # Check if the month is valid
    if month < 1 or month > 12:
        raise InvalidMonthError("Month must be between 1 and 12.")

    # Days in each month (index 0 is unused)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Handle February case for leap years
    if month == 2:
        # Check if it is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29  # Leap year
        else:
            return 28  # Non-leap year

    # Return the number of days for the specified month
    return days_in_month[month]