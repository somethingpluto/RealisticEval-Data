from typing import Tuple
import math

def decompose(n: int, shape: Tuple[int]) -> Tuple[int]:
    if any(x < 0 for x in shape):
        raise ValueError("All dimensions in shape must be non-negative.")

    if n < 0 or n >= sum(shape):
        raise ValueError(f"Index {n} is out of bounds for the array defined by {shape}.")

    result = []
    for i, s in enumerate(reversed(shape)):
        result.append(math.floor(n / s))
        n -= result[-1] * s

    if n!= 0:
        raise ValueError(f"Index {n} is out of bounds for the array defined by {shape}.")

    return tuple(reversed(result))
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