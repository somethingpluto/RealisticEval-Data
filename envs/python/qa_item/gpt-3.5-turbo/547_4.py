from typing import List


def calculate_column_widths(data: List[List[str]]) -> List[int]:
    max_column_widths = []
    
    # Initialize the max_column_widths list with zeros
    if data:
        num_columns = len(data[0])
        max_column_widths = [0] * num_columns
    
    # Iterate through each row of data
    for row in data:
        # Iterate through each element in the row to update column widths
        for i, value in enumerate(row):
            if len(value) > max_column_widths[i]:
                max_column_widths[i] = len(value)
    
    return max_column_widths
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