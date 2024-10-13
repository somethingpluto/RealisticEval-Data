def get_days_in_month(year, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Validate month input
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")

    # Adjust for leap years if the month is February (month == 2)
    if month == 2:
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return 29 if is_leap_year else 28  # Return 29 if leap year, otherwise 28

    # Return the number of days in the specified month
    return days_in_month[month]