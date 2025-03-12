from typing import List

def bool_array_to_binary_string(bool_array: List[bool]) -> str:
    """
    Converts the array of Boolean values to a binary string representation,
    which converts to the character '1' if the Boolean value is true.
    Otherwise, it is converted to the character '0', and the final string is returned.

    Args:
        bool_array (list[bool]): An array of boolean values.

    Returns:
        str: A binary string where '1' represents true and '0' represents false.
    """
    return ''.join('1' if b else '0' for b in bool_array)
import unittest


class TestBoolArrayToBinaryString(unittest.TestCase):

    def test_converts_all_true_values(self):
        bool_array = [True, True, True]
        expected = '111'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_converts_all_false_values(self):
        bool_array = [False, False, False]
        expected = '000'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_converts_mixed_true_and_false_values(self):
        bool_array = [True, False, True, False]
        expected = '1010'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_handles_empty_array(self):
        bool_array = []
        expected = ''
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

    def test_handles_single_boolean_value(self):
        bool_array = [True]
        expected = '1'
        self.assertEqual(bool_array_to_binary_string(bool_array), expected)

if __name__ == '__main__':
    unittest.main()