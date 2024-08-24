import unittest


class TestRotateListElements(unittest.TestCase):

    def test_basic_rotation(self):
        self.assertEqual(rotate_list_elements([1, 2, 3, 4]), [2, 3, 4, 1], "Should rotate the list elements correctly")

    def test_single_element_list(self):
        self.assertEqual(rotate_list_elements([10]), [10], "Single element list should remain unchanged")

    def test_empty_list(self):
        self.assertEqual(rotate_list_elements([]), [], "Empty list should remain unchanged")

    def test_two_element_list(self):
        self.assertEqual(rotate_list_elements([5, 9]), [9, 5], "Should correctly rotate a two-element list")

    def test_large_list(self):
        large_list = list(range(1, 1001))
        rotated_list = rotate_list_elements(large_list)
        self.assertEqual(rotated_list, list(range(2, 1001)) + [1], "Should correctly rotate a large list")


