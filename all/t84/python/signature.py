from collections import Counter
from typing import Optional


def find_min_window_substring(source: str, target: str) -> Optional[str]:
    """
    Finds the smallest window in the source string that contains all characters of the target string.

    Args:
        source (str): The source string in which to search for the window.
        target (str): The target string containing the characters to be matched.

    Returns:
        Optional[str]: The smallest window in the source string that contains all characters of the target string.
                       Returns an empty string if no such window exists.
    """