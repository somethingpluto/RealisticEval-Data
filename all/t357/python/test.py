class Tester(unittest.TestCase):
    def test_hill_sort(self):
        # Test case: Sort an already sorted array
        arr = [1, 2, 3, 4, 5]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array in reverse order
        arr = [5, 4, 3, 2, 1]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array with duplicate values
        arr = [3, 1, 2, 3, 2]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array with all identical values
        arr = [1, 1, 1, 1, 1]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an empty array
        arr = []
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort an array with one element
        arr = [42]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))

        # Test case: Sort a large random array
        arr = [3, 7, 2, 5, 1, 4, 6, 0, 9, 8]
        hill_sort(arr)
        self.assertTrue(is_sorted(arr))
