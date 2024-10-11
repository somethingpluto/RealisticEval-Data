# Written by ChatGPT
from datetime import datetime


def date_range_string(start_date: str, end_date: str) -> str:
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')

    # Extract the month and day information
    start_month = start_dt.strftime('%B')
    end_month = end_dt.strftime('%B')
    start_day = str(int(start_dt.strftime('%d')))
    end_day = str(int(end_dt.strftime('%d')))

    # Check if the start and end dates are in the same month
    if start_month == end_month:
        return f"{start_month} {start_day} to {end_day}"
    else:
        return f"{start_month} {start_day} to {end_month} {end_day}"