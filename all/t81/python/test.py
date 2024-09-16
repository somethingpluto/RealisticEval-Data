import unittest

class TestFindClosestElement(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError, msg="Should raise ValueError for empty list"):
            find_closest_element(5, [])

    def test_basic_functionality(self):
        self.assertEqual(find_closest_element(5, [1, 3, 7, 8, 9]), 3, "Should return 3 as it is the first closest element to 5")

    def test_exact_match(self):
        self.assertEqual(find_closest_element(7, [1, 3, 7, 8, 9]), 7, "Should return 7 as it exactly matches the target")

    def test_multiple_closest_values(self):
        self.assertEqual(find_closest_element(5, [4, 6, 8, 9]), 4, "Should return 4 as it is the first closest element to 5")

    def test_float_values(self):
        self.assertEqual(find_closest_element(5.5, [1.1, 3.3, 7.7, 8.8]), 3.3, "Should return 3.3 as it is the first closest element to 5.5")

