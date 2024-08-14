import unittest



class TestParseAndFormat(unittest.TestCase):

    def test_none_input(self):
        self.assertIsNone(parse_and_format(None))

    def test_list_input(self):
        self.assertEqual(parse_and_format(["apple", "banana", "cherry"]), "'apple', 'banana', 'cherry'")

    def test_string_input_with_asterisks(self):
        input_str = "* apple * banana * cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_string_input_with_commas(self):
        input_str = "apple, banana, cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_string_input_with_semicolons(self):
        input_str = "apple; banana; cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_mixed_separators(self):
        input_str = "* apple, banana; cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_multiline_input(self):
        input_str = """
        apple
        * banana
        cherry, date
        """
        expected_output = "'apple', 'banana', 'cherry', 'date'"
        self.assertEqual(parse_and_format(input_str), expected_output)
from typing import Any, Optional


def parse_and_format(input_data: Optional[Any]) -> Optional[str]:
    """
    Parse the input data and format it as a comma-separated string.

    Args:
        input_data (Optional[Any]): The input data which could be a string or a list.

    Returns:
        Optional[str]: A comma-separated string or None if input_data is None.
    """
    if input_data is None:
        return None

    if isinstance(input_data, list):
        return ", ".join(map(str, input_data))

    items = []
    lines = str(input_data).strip().splitlines()

    for line in lines:
        if '*' in line:
            items.extend([item.strip() for item in line.split('*') if item.strip()])
        elif ';' in line:
            items.extend([item.strip() for item in line.split(',') if item.strip()])
        elif ',' in line:
            items.extend([item.strip() for item in line.split(';') if item.strip()])
        else:
            items.append(line.strip())

    cleaned_items = [item for item in items if item]
    return ", ".join(repr(item) for item in cleaned_items)
