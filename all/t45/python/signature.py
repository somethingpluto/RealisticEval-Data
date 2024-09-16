def get_current_date_info(test_date=None) -> dict:
    """
    Returns the current time information including year, month, week of the month, and day of.eg {
            'year': 2024,
            'month': 'February',
            'week_of_the_month': 5,
            'day_of_the_week': 'Thursday'
        }

    Args:
        test_date (datetime.date): The date to compute information for, defaults to today's date if not provided.

    Returns:
        dict: A dictionary containing the year, month, week of the month, and day of the week.
    """
