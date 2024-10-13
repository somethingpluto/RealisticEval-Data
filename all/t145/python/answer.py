import locale
from babel.numbers import format_currency as babel_format_currency

def format_currency(value: float, currency_code: str, locale_str: str = "en_US") -> str:
    """
    Formats a number as currency according to the specified locale and currency code.

    Args:
        value (float): The numerical value to be formatted.
        currency_code (str): The currency code (e.g., "USD", "EUR").
        locale_str (str): The locale string (e.g., "en_US", "fr_FR"). Default is "en_US".

    Returns:
        str: The formatted currency string.
    """
    return babel_format_currency(value, currency_code, locale=locale_str)