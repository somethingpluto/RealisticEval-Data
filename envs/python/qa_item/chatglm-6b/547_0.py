
from typing import List

def calculate_column_widths(data: List[List[str]]) -> List[int]:
    """
    Calculate the maximum width of each column in a list of lists where each sub-list represents a row of table data.

    Args:
        data (List[List[str]]): A two-dimensional list containing rows of data, where each inner list contains string elements representing the values in each column.

    Returns:
        List[int]: A list containing the maximum width (in characters) of each column across all rows. The width of a column is defined by the longest string present in that column.
    """
    # Iterate over the data list and column list
    for row in data:
        for column in row:
            # Get the longest string in the current column
            longest_string = max(column.split())
            # Calculate the width of the current column
            width = len(longest_string)
            # Add the width to the list of column width
            column_widths.append(width)
    return column_widths

import unittest


class TestCalculateColumnWidths(unittest.TestCase):

    def test_standard_case(self):
        data = [["Name", "Age", "City"],
                ["Alice", "22", "New York"],
                ["Bob", "30", "San Francisco"]]
        expected = [5, 3, 13]
        self.assertEqual(calculate_column_widths(data), expected)


    def test_single_element(self):
        data = [["Name"]]
        expected = [4]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_varied_length(self):
        data = [["a", "bb", "ccc"],
                ["dddd", "ee", "f"]]
        expected = [4, 2, 3]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_all_empty_strings(self):
        data = [["", "", ""],
                ["", "", ""]]
        expected = [0, 0, 0]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_mixed_content(self):
        data = [["1234", "567", "890"],
                ["abc", "defg", "h"]]
        expected = [4, 4, 3]
        self.assertEqual(calculate_column_widths(data), expected)

    def test_single_column_multiple_rows(self):
        data = [["one"],
                ["two"],
                ["three"]]
        expected = [5]
        self.assertEqual(calculate_column_widths(data), expected)

if __name__ == '__main__':
    unittest.main()