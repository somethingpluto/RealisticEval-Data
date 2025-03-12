from typing import List

def flatten_array(multi_dim_array: List) -> List:
    """
    convert a multi-dimensional array into a one-dimensional array
    Args:
        multi_dim_array (List): A multi-dimensional list (nested list).

    Returns:
        list: A one-dimensional list containing all elements of the input.
    """
    flattened_list = []
    for sublist in multi_dim_array:
        if isinstance(sublist, list):
            flattened_list.extend(flatten_array(sublist))
        else:
            flattened_list.append(sublist)
    return flattened_list
import unittest


class TestFlattenArray(unittest.TestCase):
    def test_deeply_nested_array(self):
        """Test a deeply nested array."""
        nested_array = [1, [2, [3, [4, [5]]]]]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_array(nested_array), expected_result)

    def test_mixed_types(self):
        """Test an array with mixed question types."""
        mixed_array = ["a", ["b", 2, [True, [3.14]]], False]
        expected_result = ["a", "b", 2, True, 3.14, False]
        self.assertEqual(flatten_array(mixed_array), expected_result)

    def test_empty_array(self):
        """Test an empty array."""
        empty_array = []
        expected_result = []
        self.assertEqual(flatten_array(empty_array), expected_result)

    def test_array_with_empty_subarrays(self):
        """Test an array that includes empty subarrays."""
        complex_array = [1, [], [2, [], 3], [4, [5, [], 6], 7], []]
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_array(complex_array), expected_result)

    def test_no_nested_array(self):
        """Test an array that has no nested structure."""
        flat_array = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_array(flat_array), expected_result)

if __name__ == '__main__':
    unittest.main()