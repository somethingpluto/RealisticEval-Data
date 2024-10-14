def is_kebab_case(input: str) -> bool:
    """
    Detects whether the string is in KEBAB_CASE.

    KEBAB_CASE is defined as a string that:
    - Contains only lowercase letters (a-z).
    - May contain digits (0-9).
    - Uses hyphens (-) as word separators.
    - Does not start or end with a hyphen.
    - Does not contain consecutive hyphens.

    Args:
        input (str): The string to check.

    Returns:
        bool: True if the string is in KEBAB_CASE, otherwise False.
    """