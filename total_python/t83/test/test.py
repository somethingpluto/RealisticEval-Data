import unittest


class TestRotateList(unittest.TestCase):
    def test_standard_list(self):
        # Test a standard list with multiple elements
        self.assertEqual(rotate_list([1, 2, 3, 4]), [2, 3, 4, 1])

    def test_single_element_list(self):
        # Test a list with only one element
        self.assertEqual(rotate_list([1]), [1])

    def test_empty_list(self):
        # Test an empty list
        self.assertEqual(rotate_list([]), [])

    def test_list_with_duplicates(self):
        # Test a list that contains duplicate values
        self.assertEqual(rotate_list([1, 2, 2, 3]), [2, 2, 3, 1])

    def test_list_with_varied_types(self):
        # Test a list containing elements of different types
        self.assertEqual(rotate_list(['a', 123, None, True]), [123, None, True, 'a'])
