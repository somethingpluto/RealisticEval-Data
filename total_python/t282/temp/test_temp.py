import unittest


class TestFlattenArray(unittest.TestCase):
    def test_deeply_nested_array(self):
        """Test a deeply nested array."""
        nested_array = [1, [2, [3, [4, [5]]]]]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_array(nested_array), expected_result)

    def test_mixed_types(self):
        """Test an array with mixed data types."""
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

def flatten_array(multi_dim_array):
    """
    Flattens a multi-dimensional array into a one-dimensional array.

    Args:
    multi_dim_array (list): A multi-dimensional list (nested list).

    Returns:
    list: A one-dimensional list containing all elements of the input.
    """
    flat_list = []

    def flatten(sub_array):
        for item in sub_array:
            if isinstance(item, list):
                flatten(item)  # Recursively flatten if the current item is a list
            else:
                flat_list.append(item)  # Append the non-list item to the flat_list

    flatten(multi_dim_array)
    return flat_list
