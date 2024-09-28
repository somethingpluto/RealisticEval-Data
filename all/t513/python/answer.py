import re


def is_phrase_in_string_ignore_case(phrase, string):
    """
    Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.

    Args:
        phrase (str): The phrase to search for in the string.
        string (str): The target string in which to search for the phrase.

    Returns:
        bool: True if the phrase is found as a whole word in the string, False otherwise.
    """
    # Convert both phrase and string to lower case
    phrase = phrase.lower()
    string = string.lower()

    # Escape special characters in the phrase
    escaped_phrase = re.escape(phrase)

    # Replace spaces in the phrase with \s+ to allow for any whitespace variations
    escaped_phrase = escaped_phrase.replace(r'\ ', r'\s+')

    # Construct the regex pattern with word boundaries
    pattern = r'\b' + escaped_phrase + r'\b'

    # Search for the pattern in the target string
    return bool(re.search(pattern, string))