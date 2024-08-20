import unittest


class TestConvertToCommaSeparated(unittest.TestCase):
    def test_basic_separators(self):
        self.assertEqual(convert_to_comma_separated("apple;banana*orange/mango"), "apple,banana,orange,mango",
                         "Failed to convert basic separators.")

    def test_mixed_separators(self):
        self.assertEqual(convert_to_comma_separated("grapes;lemon/melon*kiwi;litchi"), "grapes,lemon,melon,kiwi,litchi",
                         "Failed to convert mixed separators in a string.")

    def test_no_separators(self):
        self.assertEqual(convert_to_comma_separated("watermelon"), "watermelon",
                         "Failed when no separators are present.")

    def test_repeated_separators(self):
        self.assertEqual(convert_to_comma_separated("pear;;apple**banana//orange"), "pear,,apple,,banana,,orange",
                         "Failed to handle repeated separators correctly.")

    def test_multiple_types(self):
        self.assertEqual(convert_to_comma_separated("papaya;guava*fig/tomato:carrot-lettuce"),
                         "papaya,guava,fig,tomato,carrot,lettuce",
                         "Failed to handle multiple types of separators.")

import re


def convert_to_comma_separated(input_string):
    """
    Converts an input string with multiple separators to a comma-separated string.
    Now handles additional separators: hyphens (-) and colons (:).

    Args:
    input_string (str): The input string containing various separators like *, ;, /, -, :

    Returns:
    str: A comma-separated string where all specified separators have been replaced with commas.
    """
    # The pattern includes *, ;, /, -, :
    pattern = r'[\*;/\-\:]'  # Correctly escaped hyphen and included colon in the character class
    comma_separated_string = re.sub(pattern, ',', input_string)
    return comma_separated_string