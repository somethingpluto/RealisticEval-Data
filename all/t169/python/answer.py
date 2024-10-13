def convert_to_roman(num: int) -> str:
    """
    Converts an Arabic numeral to its Roman numeral equivalent.

    Args:
        num (int): The number to convert.

    Returns:
        str: The Roman numeral representation of the input number.

    Raises:
        ValueError: Will raise an error if the input is not a positive integer.
    """
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Input must be a positive integer')

    roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""

    for i in range(len(roman_numerals)):
        while num >= roman_values[i]:
            result += roman_numerals[i]
            num -= roman_values[i]

    return result