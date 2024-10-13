from datetime import date, timedelta


def calculate_good_friday(year: int) -> date:
    """
    Calculates the date of Good Friday for a given year using the anonymous Gregorian algorithm
    to compute the date of Easter Sunday. Good Friday is two days before Easter Sunday.

    Args:
        year (int): The year for which to calculate Good Friday.

    Returns:
        date: The date of Good Friday.
    """
    # Anonymous Gregorian algorithm to compute the date of Easter Sunday
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = (h + l - 7 * m + 114) % 31 + 1

    # Easter Sunday date
    easter = date(year, month, day)

    # Good Friday is two days before Easter Sunday
    good_friday = easter - timedelta(days=2)

    return good_friday
