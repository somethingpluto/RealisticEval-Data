def convert_time_hms_string_to_ms(s):
    """
    convert a string containing hours, minutes, and seconds to milliseconds, for example, convert the string "1h20 min30s" to milliseconds

    Args:
        s (str): The time duration string (e.g., '2h15m30s').

    Returns:
        int: The time duration in milliseconds.
    """