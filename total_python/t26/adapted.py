import re


def convert_to_comma_separated(input_string):
    """
    Converts an input string with multiple separators to a comma-separated string.
    Now handles additional separators: hyphens (-) and colons (:).

    Args:
    input_string (str): The input string containing various separators like *, ;, /, -, :

    Returns:
    str: A comma-separated string where all specified separators have been replaced with commas.
    """
    # The pattern includes *, ;, /, -, :
    pattern = r'[\*;/\-\:]'  # Correctly escaped hyphen and included colon in the character class
    comma_separated_string = re.sub(pattern, ',', input_string)
    return comma_separated_string