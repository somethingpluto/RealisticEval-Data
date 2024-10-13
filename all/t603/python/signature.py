def is_leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.

    A year is a leap year if:
    1. It is divisible by 4 AND
    2. It is NOT divisible by 100, OR it is divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """