import re

def find_placeholders(text):
    """
    Find and return a list of all placeholders in the format {{ placeholder }} from the input text.

    Args:
        text (str): The input string containing potential placeholders.

    Returns:
        list: A list of matching placeholders.
    """