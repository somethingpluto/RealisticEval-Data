def calculate_time_difference(given_date: str) -> dict:
    """
    Calculates the time difference between a given date and the current date.

    Args:
        given_date (str): The date to compare against the current date.

    Returns:
        dict: A dictionary containing days, hours, and minutes elapsed.
              {
                  'days': days,
                  'hours': remaining_hours,
                  'minutes': remaining_minutes,
              }
    """