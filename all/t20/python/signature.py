import re


def transform_parentheses(text: str) -> str:
    """
    Transforms the input text by finding and modifying patterns that match the format '(*...*)'.
    Specifically, it removes any asterisks inside the parentheses while preserving the outer format.

    Args:
        text (str): The input text containing patterns to be transformed.

    Returns:
        str: The transformed text with asterisks inside '(*...*)' patterns removed.
    """
