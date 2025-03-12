from typing import List


def convert_to_ring_format(holes: List[int]) -> List[int]:
    """
    Convert a list of hole positions to the ring format (list of 1s and 0s).

    Args:
        holes (list): A list of integers representing the positions of the holes (0-indexed).

    Returns:
        List: A list of length 32, where positions with holes are 0 and others are 1.

    """
    ring_format = [1] * 32
    for hole in holes:
        ring_format[hole] = 0
    return ring_format
import unittest


class TestConvertToRingFormat(unittest.TestCase):

    def test_no_holes(self):
        """ Test with no holes provided. """
        holes = []
        expected = [1] * 32  # All positions should be 1
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_single_hole(self):
        """ Test with a single hole position. """
        holes = [5]
        expected = [1] * 32
        expected[5] = 0  # Only position 5 should be 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_multiple_holes(self):
        """ Test with multiple hole positions. """
        holes = [0, 2, 4, 8, 16]
        expected = [1] * 32
        for hole in holes:
            expected[hole] = 0  # Set specified positions to 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_hole_out_of_bounds(self):
        """ Test with some hole positions out of bounds. """
        holes = [-1, 32, 5, 10]  # -1 and 32 are out of bounds
        expected = [1] * 32
        expected[5] = 0  # Only position 5 and 10 should be 0
        expected[10] = 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)

    def test_all_holes(self):
        """ Test with all positions as holes. """
        holes = list(range(32))  # All positions from 0 to 31
        expected = [0] * 32  # All positions should be 0
        result = convert_to_ring_format(holes)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()