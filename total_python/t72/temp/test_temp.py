import unittest


class TestGet3DCoordinates(unittest.TestCase):
    def setUp(self):
        # Define a common intrinsic matrix for testing
        self.K = np.array([[1000, 0, 320],
                           [0, 1000, 240],
                           [0, 0, 1]])

    def test_center_coordinates(self):
        """ Test with center pixel coordinates where x and y should map to zero in NDC. """
        result = get_3d_coordinates(self.K, 100, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, 100]))

    def test_boundary_coordinates(self):
        """ Test with boundary values in the image frame. """
        result = get_3d_coordinates(self.K, 50, 640, 480)
        expected_x = (640 - 320) / 1000 * 50
        expected_y = (480 - 240) / 1000 * 50
        np.testing.assert_array_almost_equal(result, np.array([expected_x, expected_y, 50]))

    def test_negative_depth(self):
        """ Test with a negative depth to see if it handles incorrect input properly. """
        result = get_3d_coordinates(self.K, -100, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, -100]))

    def test_zero_depth(self):
        """ Test with zero depth which should lead to a zero-length vector. """
        result = get_3d_coordinates(self.K, 0, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, 0.0]))

    def test_non_integer_values(self):
        """ Test with non-integer pixel coordinates. """
        result = get_3d_coordinates(self.K, 100, 320.5, 240.5)
        expected_x = (320.5 - 320) / 1000 * 100
        expected_y = (240.5 - 240) / 1000 * 100
        np.testing.assert_array_almost_equal(result, np.array([expected_x, expected_y, 100]))
import numpy as np


def get_3d_coordinates(K, d, x, y):
    """Written by ChatGPT and fixed by me

    Args:
        K ((3,3) np.array): camera intrinsic matrix
        d (float): depth (distance along z-axis)
        x (float): pixel x coordinate
        y (float): pixel y coordinate

    Returns:
        (3,) np.array: x, y, z 3D point coordinates in camera RDF coordinates
    """
    # Step 1: Convert pixel coordinates to normalized device coordinates (NDC)
    cx = K[0, 2]
    cy = K[1, 2]
    fx = K[0, 0]
    fy = K[1, 1]

    NDC_x = (x - cx) / fx
    NDC_y = (y - cy) / fy

    # Step 2: Get the 3D world coordinates (W)
    W_x = NDC_x * d
    W_y = NDC_y * d
    W_z = d
    return np.array([W_x, W_y, W_z])