import unittest


class TestCompareArrays(unittest.TestCase):

    def test_identical_arrays_same_order(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3]
        self.assertTrue(compare_arrays(arr1, arr2))

    def test_identical_arrays_different_order(self):
        arr1 = [3, 2, 1]
        arr2 = [1, 2, 3]
        self.assertTrue(compare_arrays(arr1, arr2))

    def test_different_elements(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        self.assertFalse(compare_arrays(arr1, arr2))

    def test_different_lengths(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2]
        self.assertFalse(compare_arrays(arr1, arr2))

    def test_duplicate_elements_same_unique_set(self):
        arr1 = [1, 1, 2, 3, 3]
        arr2 = [3, 2, 1, 1]
        self.assertTrue(compare_arrays(arr1, arr2))