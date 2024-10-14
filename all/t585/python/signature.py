def is_camel_case(input: str) -> bool:
    """
    Detects whether the string is in CAMEL_CASE.

    In CAMEL_CASE, the first letter of the first word is lowercase,
    and each subsequent word starts with an uppercase letter, with no spaces or underscores
    separating the words.

    Args:
        input (str): The string to check.

    Returns:
        bool: True if the string is in CAMEL_CASE, otherwise False.
    """