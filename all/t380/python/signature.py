from typing import Tuple


def calculate_total_seconds(time: Tuple[int]):
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
