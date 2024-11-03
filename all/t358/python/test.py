import unittest


class Tester(unittest.TestCase):
    def test_sort_names_same_numbers(self):
        arr = ["Alice10", "Charlie10", "Bob10"]
        expected = ["Alice10", "Bob10", "Charlie10"]
        self.assertEqual(sort_names(arr), expected)

    def test_sort_names_mixed_case(self):
        arr = ["Alice3", "Bob2", "Charlie3", "Bob1"]
        expected = ["Bob1", "Bob2", "Alice3", "Charlie3"]
        self.assertEqual(sort_names(arr), expected)

    def test_sort_names_single_element(self):
        arr = ["Alice5"]
        expected = ["Alice5"]
        self.assertEqual(sort_names(arr), expected)

    def test_sort_names_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(sort_names(arr), expected)