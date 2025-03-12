
def shuffle(array: list) -> list:
    """
    Randomly shuffles the elements of the input list in place.

    Args:
        array (list): The list of elements to be shuffled.

    Returns:
        list: The shuffled list with its elements in random order.
    """
    # Get a random index for the first element
    random_index = random.randint(0, len(array) - 1)
    # Move the first element to the index
    array[0] = array[random_index]
    # Move the rest of the elements to the indices
    for i in range(1, len(array)):
        array[i] = array[random_index + i]
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