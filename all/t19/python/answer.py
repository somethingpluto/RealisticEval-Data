import re


def contains_phone_number(s: str) -> bool:
    """
    Determines whether the string contains a phone number; a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234
    """
    # Regex pattern to identify phone numbers
    pattern = r"(\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4})"
    # Use re.search to find a match
    if re.search(pattern, s):
        return True
    else:
        return False
