<<<<<<< HEAD
import re
from typing import Optional


def convert_hms_to_milliseconds(time_str: str) -> Optional[int]:
    """
    Convert a time duration string in the format 'XhYminZs' to milliseconds.

    This function takes a string representing a time duration, where hours, minutes, and seconds
    are optionally provided, and converts this duration into the equivalent number of milliseconds.

    Args:
        time_str (str): A string representing the time duration, e.g., '1h20min30s'.

    Returns:
        Optional[int]: The equivalent duration in milliseconds, or None if the input is invalid.
=======
def convert_time_hms_string_to_ms(s):
    """
    convert a string containing hours, minutes, and seconds to milliseconds, for example, convert the string "1h20 min30s" to milliseconds

    Args:
        s (str): The time duration string (e.g., '2h15m30s').

    Returns:
        int: The time duration in milliseconds.
>>>>>>> main
    """