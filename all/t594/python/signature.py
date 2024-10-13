from typing import List


def split_comma(s: str) -> List[str]:
    """
    Splits a comma-separated string into individual tokens.
    This function takes a string containing comma-separated values, trims
    leading and trailing whitespace from each token, and stores the non-empty
    tokens in the provided list.

    Args:
        s (str): The input string to be split, which may contain leading and trailing whitespace around the tokens.

    Returns:
        List[str]: A list where the resulting tokens will be stored. The list will be cleared before storing the new tokens.
    """
