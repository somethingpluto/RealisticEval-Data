import datetime


def get_current_time_details():
    # Get the current datetime
    now = datetime.datetime.now()

    # Extract the year, month, and weekday
    year = now.year
    month = now.month
    day = now.day
    weekday = now.strftime("%A")  # Gets the full weekday name, e.g., "Monday"

    # Calculate the week of the month for today
    first_day_of_month = datetime.date(year, month, 1)
    day_of_week_first_day = first_day_of_month.weekday()  # Monday is 0 and Sunday is 6
    week_of_month = (day + day_of_week_first_day) // 7 + 1

    return year, month, week_of_month, weekday
