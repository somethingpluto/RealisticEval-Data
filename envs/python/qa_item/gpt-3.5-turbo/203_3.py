from typing import List

def reverse_range(v: List[int], a: int, b: int) -> None:
    """
    Reverse the order of elements in the list v within the specified range [a, b].

    Args:
        v (List[int]): Reference to the list of integers to be modified.
        a (int): The starting index of the range to be reversed.
        b (int): The ending index of the range to be reversed.

    Returns:

    """
    if a < 0 or a >= len(v) or b < 0 or b >= len(v) or a >= b:
        return
    
    while a < b:
        v[a], v[b] = v[b], v[a]
        a += 1
        b -= 1
import unittest


class Tester(unittest.TestCase):

    def test_reverse_entire_vector(self):
        v = [1, 2, 3, 4, 5]
        reverse_range(v, 0, 4)
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(v, expected)

    def test_reverse_subrange_in_the_middle(self):
        v = [1, 2, 3, 4, 5, 6, 7, 8]
        reverse_range(v, 2, 5)
        expected = [1, 2, 6, 5, 4, 3, 7, 8]
        self.assertEqual(v, expected)

    def test_reverse_single_element_range(self):
        v = [1, 2, 3, 4, 5]
        reverse_range(v, 2, 2)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(v, expected)

    def test_reverse_range_with_invalid_indices(self):
        v = [1, 2, 3, 4, 5]
        reverse_range(v, -1, 3)  # Invalid start index
        expected = [1, 2, 3, 4, 5]  # No change
        self.assertEqual(v, expected)

    def test_reverse_range_at_end_of_vector(self):
        v = [1, 2, 3, 4, 5, 6]
        reverse_range(v, 3, 5)
        expected = [1, 2, 3, 6, 5, 4]
        self.assertEqual(v, expected)

if __name__ == '__main__':
    unittest.main()