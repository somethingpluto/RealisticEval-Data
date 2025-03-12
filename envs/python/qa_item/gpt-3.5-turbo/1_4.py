from typing import Union

def numerical_str_convert(value: str) -> Union[int, float, str]:
    try:
        # Try converting to an integer
        return int(value)
    except ValueError:
        try:
            # If it's not an integer, try converting to a float
            return float(value)
        except ValueError:
            # If it's neither an integer nor a float, return the original string
            return value
import unittest


class TestSmartConvert(unittest.TestCase):
    def test_convert_integer(self):
        self.assertEqual(numerical_str_convert("123"), 123, "Should convert to integer")

    def test_convert_float(self):
        self.assertEqual(numerical_str_convert("123.45"), 123.45, "Should convert to float")

    def test_convert_non_numeric_string(self):
        self.assertEqual(numerical_str_convert("abc"), "abc", "Should remain a string")

    def test_convert_negative_integer(self):
        self.assertEqual(numerical_str_convert("-456"), -456, "Should convert to negative integer")

    def test_convert_negative_float(self):
        self.assertEqual(numerical_str_convert("-456.78"), -456.78, "Should convert to negative float")

if __name__ == '__main__':
    unittest.main()