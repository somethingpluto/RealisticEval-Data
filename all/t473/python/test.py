import unittest


class TestFlattenFunction(unittest.TestCase):

    def test_flatten_simple(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3], "Should flatten a simple flat list")

    def test_flatten_one_level_nesting(self):
        self.assertEqual(flatten([1, [2, 3], 4]), [1, 2, 3, 4], "Should flatten a list with one level of nesting")

    def test_flatten_multiple_nested_lists(self):
        self.assertEqual(flatten([[1, 2], [3, 4], 5]), [1, 2, 3, 4, 5],
                         "Should flatten multiple nested lists at one level")

    def test_flatten_multiple_levels_nesting(self):
        self.assertEqual(flatten([1, [2, [3, 4], 5], 6]), [1, 2, 3, 4, 5, 6],
                         "Should flatten a list with multiple levels of nesting")

    def test_flatten_with_empty_lists(self):
        self.assertEqual(flatten([1, [], [2, [3, []], 4]]), [1, 2, 3, 4], "Should flatten a list with empty lists")