import unittest
from typing import Union


def numerical_str_convert(value: str) -> Union[int, float, str]:
    """
    convert the input string, first see if it is an integer, if it is converted to an integer, if it is not, see if it is a floating point number, if yes, convert to a floating point number, if neither, return the original string

    Args:
        value (str): input str

    Returns:
        Union[int, float, str]: convert result
    """
    try:
        return int(value)
    except ValueError:
        # 如果不是整数，尝试将字符串转换为浮点数
        try:
            return float(value)
        except ValueError:
            # 如果不是整数也不是浮点数，返回原始字符串
            return value


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
