import random

def shuffle(array: list) -> list:
    random.shuffle(array)
    return array
import unittest


class TestShuffleFunction(unittest.TestCase):

    def test_shuffles_array_of_numbers(self):
        array = [1, 2, 3, 4, 5]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), len(array))
        self.assertTrue(all(item in array for item in shuffled_array))
        self.assertEqual(len(set(shuffled_array)), len(set(array)))  # Ensure no duplicates

    def test_shuffles_array_of_strings(self):
        array = ["apple", "banana", "cherry", "date", "elderberry"]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), len(array))
        self.assertTrue(all(item in array for item in shuffled_array))

    def test_shuffles_array_with_duplicate_elements(self):
        array = [1, 1, 2, 2, 3, 3]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), len(array))
        self.assertTrue(all(item in array for item in shuffled_array))

    def test_shuffles_array_with_single_element(self):
        array = [42]
        shuffled_array = shuffle(array.copy())
        self.assertEqual(shuffled_array, array)

    def test_shuffles_empty_array(self):
        array = []
        shuffled_array = shuffle(array.copy())
        self.assertEqual(len(shuffled_array), 0)

if __name__ == '__main__':
    unittest.main()