import datetime
import calendar


def get_current_date_info():
    """
    Returns the current time information including year, month, week of the month, and day of the week.

    Returns:
        dict: A dictionary containing the year, month, week of the month, and day of the week.
    """
    today = datetime.date.today()
    year = today.year
    month = today.month
    day_of_week = calendar.day_name[today.weekday()]

    # Calculate the week of the month
    first_day_of_month = today.replace(day=1)
    first_day_weekday = first_day_of_month.weekday()
    week_of_month = (today.day + first_day_weekday - 1) // 7 + 1

    return {
        'year': year,
        'month': calendar.month_name[month],
        'week_of_the_month': week_of_month,
        'day_of_the_week': day_of_week
    }
