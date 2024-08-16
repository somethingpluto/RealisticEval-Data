def gen_timeout_timedelta(time_string:str):
    """
    Converts a time duration string into a timedelta object.
    The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
    eg."1d 2h 3m 4s 500ms"
    Each unit should be specified by an integer followed by its corresponding unit letter.
    Args:
        time_string ():A string representing the time duration.

    Returns:
        timedelta: A timedelta object representing the input duration.
    """