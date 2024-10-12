import re

def remove_punctuation(s: str) -> str:
    """
    Removes all punctuation from a given string, converts the string to lowercase,
    and trims whitespace from both ends.

    Args:
        s (str): The string from which to remove punctuation.

    Returns:
        str: The cleaned and formatted string.
    """
    # Define a regex pattern that matches common punctuation characters.
    # This includes Unicode punctuation and ASCII punctuation.
    punctuation_regex = r'[\u2000-\u206F\u2E00-\u2E7F!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]'
    
    # Replace punctuation with an empty string, convert to lowercase, and trim whitespace.
    return re.sub(punctuation_regex, '', s).lower().strip()