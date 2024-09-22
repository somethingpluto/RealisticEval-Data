def calculate_total_seconds(time):
    """
    Calculate the total number of seconds given a tuple or list of time periods in the order of
    days, hours, minutes, and seconds.

    :param time: tuple or list, where
        time[0] - number of days (optional)
        time[1] - number of hours (optional)
        time[2] - number of minutes (optional)
        time[3] - number of seconds (optional)
    :return: int, total number of seconds

    Examples:
        calculate_total_seconds([1, 2, 3, 4]) returns 93784
        calculate_total_seconds([0, 2, 3]) returns 7380
    """
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    # Unpacking the time with defaults
    days, hours, minutes, seconds = (list(time) + [0] * 4)[:4]

    total_seconds = (
            days * SECONDS_PER_DAY +
            hours * SECONDS_PER_HOUR +
            minutes * SECONDS_PER_MINUTE +
            seconds
    )
    return total_seconds
