
from typing import List

def reverse_range(v: List[int], a: int, b: int) -> None:
    if len(v)!= 3:
        raise ValueError("The input list must have 3 elements")

    if a < 0 or a >= len(v):
        raise ValueError("The starting index a must be within the range [1, len(v)-1])")

    if b < 0 or b >= len(v):
        raise ValueError("The ending index b must be within the range [1, len(v)-1])")

    v[a-1] = v[b-1]
    v[b-1] = v[a-1]

    return None

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