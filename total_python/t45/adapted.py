import datetime
import calendar
from typing import Tuple


def get_current_time_details() -> Tuple[int, int, int, int]:
    """
    Get the current year, month, week of the month, and day of the week.

    :return: A dictionary containing the current year, month, week of the month, and day of the week.
    """
    now = datetime.datetime.now()

    # Get the current year and month
    year = now.year
    month = now.month

    # Calculate the day of the week (0=Monday, 6=Sunday)
    day_of_week = now.weekday()

    # Calculate the first day of the month and today's day
    first_day_of_month = now.replace(day=1)
    day_of_month = now.day

    # Calculate the week of the month
    _, days_in_month = calendar.monthrange(year, month)
    weeks_in_month = [calendar.monthcalendar(year, month)[i] for i in range(5)]
    week_of_month = 0
    for week in weeks_in_month:
        if day_of_month in week:
            week_of_month = weeks_in_month.index(week) + 1
            break

    return year, month, week_of_month, day_of_week
