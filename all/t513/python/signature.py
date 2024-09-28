import re


def is_phrase_in_string_ignore_case(phrase: str, string: str) -> bool:
    """
    Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.

    Args:
        phrase (str): The phrase to search for in the string.
        string (str): The target string in which to search for the phrase.

    Returns:
        bool: True if the phrase is found as a whole word in the string, False otherwise.
    """
