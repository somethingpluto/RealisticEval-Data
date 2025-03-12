import locale

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
    locale.setlocale(locale.LC_ALL, locale_str)
    return locale.currency(value, symbol=True, grouping=True, curr=currency_code)
import unittest

class TestFormatCurrency(unittest.TestCase):
    
    def test_format_currency_usd(self):
        value = 1234.56
        currency_code = 'USD'
        locale = 'en-US'
        expected_output = '\$1,234.56'  # Expected format for USD
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_euro(self):
        value = 1234.56
        currency_code = 'EUR'
        locale = 'en-US'
        expected_output = '€1,234.56'  # Expected format for EUR
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_gbp(self):
        value = 1234.56
        currency_code = 'GBP'
        locale = 'en-GB'
        expected_output = '£1,234.56'  # Expected format for GBP
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_negative(self):
        value = -1234.56
        currency_code = 'USD'
        locale = 'en-US'
        expected_output = '-\$1,234.56'  # Expected format for negative USD
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_zero(self):
        value = 0
        currency_code = 'JPY'
        locale = 'en-JP'
        expected_output = '¥0'  # Expected format for JPY (no decimals)
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)
if __name__ == '__main__':
    unittest.main()