from datetime import datetime
from typing import Tuple


def get_time_since_born_until_now(birth_date: datetime) -> Tuple[int, int, int, int, int]:
    """
    Calculate the years, months, days, hours, and minutes that have passed
    from the birth date to the current date and return them as a tuple.

    Args:
        birth_date (datetime): The birth date as a datetime object.

    Returns:
        Tuple[int, int, int, int, int]: A tuple containing the values of years, months, days, hours, and minutes.
    """
