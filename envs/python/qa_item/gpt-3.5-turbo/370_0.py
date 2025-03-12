from typing import Tuple

def decompose(n: int, shape: Tuple) -> Tuple:
    if n < 0:
        raise ValueError("Flat index must be a non-negative integer.")
    
    total_elements = 1
    for dimension in shape:
        if dimension <= 0:
            raise ValueError("Shape dimensions must be positive integers.")
        total_elements *= dimension
        
    if n >= total_elements:
        raise ValueError("Flat index is out of bounds for the given shape.")
        
    result = []
    for dimension in reversed(shape):
        total_elements //= dimension
        result.append(n // total_elements)
        n = n % total_elements
        
    return tuple(result)
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