def abbreviate_number(number: float) -> str:
    """
    Abbreviates a number to a string with a suffix based on its magnitude.

    The function uses the following suffixes based on the number's magnitude:
    - "" (no suffix) for values less than 1,000
    - "k" for thousands (1,000)
    - "M" for millions (1,000,000)
    - "B" for billions (1,000,000,000)
    - "T" for trillions (1,000,000,000,000)

    For example:
        - Input: 999             Output: "999"
        - Input: 1549            Output: "1.5k"
        - Input: 1000            Output: "1k"
        - Input: 1234567890123   Output: "1.2T"

    Args:
        number (float): The number to abbreviate.

    Returns:
        str: The abbreviated string representation of the number.
    """