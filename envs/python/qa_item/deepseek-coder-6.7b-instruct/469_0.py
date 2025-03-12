from typing import Tuple
import numpy as np

def get_scale(matrix: np.ndarray) -> Tuple[np.float64, np.float64]:
    """
    Given a 3x3 affine transformation matrix, return the corresponding scaling factors
    along the x and y axes.

    Args:
        matrix (np.ndarray): A 3x3 affine transformation matrix.

    Returns:
        Tuple[np.float64, np.float64]: A tuple containing the scale factors (scale_x, scale_y).
    """
    # Extract the relevant elements from the matrix
    scale_x = np.sqrt(matrix[0, 0]**2 + matrix[0, 1]**2)
    scale_y = np.sqrt(matrix[1, 0]**2 + matrix[1, 1]**2)
    
    return (scale_x, scale_y)
import numpy as np
import unittest


# Assume the get_scale function is defined as provided

class TestGetScaleFunction(unittest.TestCase):

    def test_identity_matrix(self):
        """ Test for the identity matrix (no scaling) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_scale = (1.0, 1.0)
        self.assertEqual(get_scale(matrix), expected_scale)

    def test_scaling_matrix(self):
        """ Test for a scaling matrix (2x in x and 3x in y) """
        matrix = np.array([[2, 0, 0],
                           [0, 3, 0],
                           [0, 0, 1]])
        expected_scale = (2.0, 3.0)
        self.assertEqual(get_scale(matrix), expected_scale)


    def test_uniform_scaling(self):
        # Test case with uniform scaling
        matrix = np.array([[2, 0, 0],
                           [0, 2, 0],
                           [0, 0, 1]])
        expected = (2.0, 2.0)
        self.assertEqual(get_scale(matrix), expected)

    def test_non_uniform_scaling(self):
        # Test case with non-uniform scaling
        matrix = np.array([[3, 0, 0],
                           [0, 5, 0],
                           [0, 0, 1]])
        expected = (3.0, 5.0)
        self.assertEqual(get_scale(matrix), expected)

    def test_reflection_matrix(self):
        # Test case with reflection matrix
        matrix = np.array([[-1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected = (1.0, 1.0)
        self.assertEqual(get_scale(matrix), expected)
if __name__ == '__main__':
    unittest.main()