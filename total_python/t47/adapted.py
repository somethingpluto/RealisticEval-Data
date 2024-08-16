import datetime


def find_nth_weekday(year, month, weekday, nth):
    """
    Finds the nth occurrence of a specific weekday in a given month and year.

    Parameters:
        year (int): The year
        month (int): The month
        weekday (int): The weekday, where Monday is 0 and Sunday is 6
        nth (int): The nth occurrence of the weekday to find

    Returns:
        datetime.date: The date of the nth occurrence, or the last occurrence of the weekday if nth is not available.
    """
    # Start with the first day of the month
    first_day = datetime.date(year, month, 1)

    # Find the first occurrence of the given weekday
    first_weekday = first_day.weekday()
    if first_weekday <= weekday:
        first_occurrence = first_day + datetime.timedelta(days=(weekday - first_weekday))
    else:
        first_occurrence = first_day + datetime.timedelta(days=(7 - first_weekday + weekday))

    # Calculate the nth occurrence
    nth_occurrence = first_occurrence + datetime.timedelta(days=(nth - 1) * 7)

    # Check if the nth occurrence is within the same month
    if nth_occurrence.month == month:
        return nth_occurrence
    else:
        # If not, find the last occurrence of the weekday in the month
        # Go back one week from the first of the next month
        first_of_next_month = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
        last_day_of_month = first_of_next_month - datetime.timedelta(days=1)
        last_weekday = last_day_of_month.weekday()

        if last_weekday >= weekday:
            last_occurrence = last_day_of_month - datetime.timedelta(days=(last_weekday - weekday))
        else:
            last_occurrence = last_day_of_month - datetime.timedelta(days=(7 - (weekday - last_weekday)))

        return last_occurrence