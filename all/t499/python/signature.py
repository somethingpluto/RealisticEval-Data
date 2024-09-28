import re
from typing import Union


def clean_pattern(x: str, pattern: str) -> Union[str,float]:
    """
    Extracts a numeric value from the input string based on the given regex pattern.

    Args:
        x (str or any): The input from which to extract the value. It will be converted to a string.
        pattern (str): The regular expression pattern to use for matching.

    Returns:
        Union[str,float]: The extracted weight value if a match is found, otherwise an empty string.
    """
