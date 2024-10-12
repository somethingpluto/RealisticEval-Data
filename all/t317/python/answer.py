import re

def count_letters(s: str) -> int:
    """Count the number of letters in a string.

    Args:
        s (str): The input string from which to count letters.

    Returns:
        int: The count of letters in the string.
    """
    # Use a regular expression to match all letter characters (both uppercase and lowercase)
    letters = re.findall(r'[a-zA-Z]', s)
    # Return the number of letters found, or 0 if none are found
    return len(letters)
