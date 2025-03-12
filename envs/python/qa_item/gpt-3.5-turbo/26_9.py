import re

def convert_to_comma_separated(input_string: str) -> str:
    """
    convert input strings that contain multiple separators (for example, * ; /) to comma-separated formatted strings

    Args:
        input_string (str): The input string containing various separators like *, ;, /, -, :

    Returns:
        str: A comma-separated string where all specified separators have been replaced with commas.
    """
    separators = ['*', ';', '/', '-', ':']
    
    for separator in separators:
        input_string = re.sub(re.escape(separator), ',', input_string)
    
    return input_string
import unittest


class TestConvertToCommaSeparated(unittest.TestCase):
    def test_basic_separators(self):
        self.assertEqual(convert_to_comma_separated("apple;banana*orange/mango"), "apple,banana,orange,mango",
                         "Failed to convert basic separators.")

    def test_mixed_separators(self):
        self.assertEqual(convert_to_comma_separated("grapes;lemon/melon*kiwi;litchi"), "grapes,lemon,melon,kiwi,litchi",
                         "Failed to convert mixed separators in a string.")
    def test_mixed_separators2(self):
        self.assertEqual(convert_to_comma_separated("grapes/lemon/melon*kiwi*litchi"), "grapes,lemon,melon,kiwi,litchi",
                         "Failed to convert mixed separators in a string.")

    def test_no_separators(self):
        self.assertEqual(convert_to_comma_separated("watermelon"), "watermelon",
                         "Failed when no separators are present.")
if __name__ == '__main__':
    unittest.main()