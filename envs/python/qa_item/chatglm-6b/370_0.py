
from typing import Tuple

def decompose(n: int, shape: Tuple) -> Tuple:
    """
    Decompose a flat index `n` into a multidimensional index based on the given shape.

    Args:
        n: Flat index (non-negative integer).
        shape: Tuple representing the dimensions of the multi-dimensional array.

    Returns:
        Tuple: Tuple representing the multidimensional index corresponding to `n`.
    Raises:
        ValueError: If `n` is out of bounds for the array defined by `shape`.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if len(shape)!= len(n):
        raise ValueError("shape and n must have the same length")
    if n % len(shape)!= 0:
        raise ValueError("n must be a multiple of the length of the shape")

    # Convert the shape tuple to a list of dimensions
    shape_list = list(shape)
    shape_list.sort()

    # Create a dictionary to store the multidimensional indices
    multidimensional_index = {}

    # Iterate over the dimensions of the shape tuple
    for dim in shape_list:
        # Calculate the index of the flat index in the multidimensional array
        multidimensional_index[n] = dim

    return multidimensional_index

import unittest


class TestDecomposeFunction(unittest.TestCase):

    def test_edge_case_with_larger_shap(self):
        self.assertEqual(decompose(60, (4, 4, 4)), (3, 3, 0))

    def test_last_valid_index(self):
        self.assertEqual(decompose(63, (4, 4, 4)), (3, 3, 3))

    def test_single_dimension_case(self):
        self.assertEqual(decompose(2, (5,)), (2,))

    def test_invalid_cases(self):
        # Test case 5: Out of bounds case (negative index)
        with self.assertRaises(ValueError):
            decompose(-1, (3, 4, 5))

        # Test case 6: Out of bounds case (index too large)
        with self.assertRaises(ValueError):
            decompose(100, (3, 4, 5))

if __name__ == '__main__':
    unittest.main()