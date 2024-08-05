import re


def contains_phone_number(output_to_test):
    """
    Checks if the given string contains a phone number using a regular expression.
    Supports various international and local formats.
    """
    # Regex pattern to identify phone numbers
    pattern = r"\+?\d{1,3}[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2,4}|\(\d{3}\)\s?\d{3}[-\s]?\d{4}"

    # Use re.search to find a match
    if re.search(pattern, output_to_test):
        return True
    else:
        return False