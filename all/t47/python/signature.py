import datetime


def find_nth_weekday_of_specific_year(y: int, m: int, n: int, k: int) -> datetime:
    """
    Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
    If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
    This function extends the capability to handle edge cases where the nth weekday might not be present,
    by providing the closest previous weekday in such cases
    Args:
        y (int): The year for which the date is to be calculated.
        m (int): The month for which the date is to be calculated, where January is 1 and December is 12.
        n (int): The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
        k (int): The weekday, where Monday is 0 and Sunday is 6.

    Returns:
        datetime: The calculated date of the nth occurrence of the weekday in the given month and year.
      If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    """