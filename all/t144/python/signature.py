def arabic_to_english_numbers(value: str) -> str:
    """
    Converts Arabic numerals in a string to English numerals.
    This function iterates over each character in the input string, replacing Arabic numerals (٠-٩)
    with their corresponding English numerals (0-9) while leaving other characters unchanged.
    For example:
         input: ٠١٢٣٤٥٦٧٨٩
         output: 012345678

    Args:
        value (str): The string containing Arabic numerals to be converted.

    Returns:
        str: The converted string with Arabic numerals replaced by English numerals.
    """