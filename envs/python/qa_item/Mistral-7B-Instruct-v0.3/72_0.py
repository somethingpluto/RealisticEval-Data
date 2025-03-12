import numpy as np

def convert_pixel_to_3d_coordinates(K, d, x, y):
    """
    Convert 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.

    Args:
        K (np.array): A (3, 3) camera intrinsic matrix, which includes focal lengths and optical center.
        d (float): Depth (distance along the z-axis) from the camera to the point in 3D space.
        x (float): The x coordinate of the pixel in 2D image space.
        y (float): The y coordinate of the pixel in 2D image space.

    Returns:
        np.array: A numpy array containing the 3D coordinates (x, y, z) in the camera's right-handed coordinate frame.
    """

    # Normalize the pixel coordinates
    x_norm = (x - K[2, 2]) / K[2, 0]
    y_norm = (y - K[2, 2]) / K[2, 1]

    # Calculate the 3D coordinates
    z = d * (x_norm / x_norm**2 + y_norm / y_norm**2 - 1)
    x = d * x_norm * z / K[0, 0]
    y = d * y_norm * z / K[1, 1]

    # Return the 3D coordinates as a numpy array
    return np.array([x, y, z])
import unittest

import numpy as np


class TestGet3DCoordinates(unittest.TestCase):
    def setUp(self):
        # Define a common intrinsic matrix for testing
        self.K = np.array([[1000, 0, 320],
                           [0, 1000, 240],
                           [0, 0, 1]])

    def test_center_coordinates(self):
        """ Test with center pixel coordinates where x and y should map to zero in NDC. """
        result = convert_pixel_to_3d_coordinates(self.K, 100, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, 100]))

    def test_boundary_coordinates(self):
        """ Test with boundary values in the image frame. """
        result = convert_pixel_to_3d_coordinates(self.K, 50, 640, 480)
        expected_x = (640 - 320) / 1000 * 50
        expected_y = (480 - 240) / 1000 * 50
        np.testing.assert_array_almost_equal(result, np.array([expected_x, expected_y, 50]))

    def test_negative_depth(self):
        """ Test with a negative depth to see if it handles incorrect input properly. """
        result = convert_pixel_to_3d_coordinates(self.K, -100, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, -100]))

    def test_zero_depth(self):
        """ Test with zero depth which should lead to a zero-length vector. """
        result = convert_pixel_to_3d_coordinates(self.K, 0, 320, 240)
        np.testing.assert_array_almost_equal(result, np.array([0.0, 0.0, 0.0]))

    def test_non_integer_values(self):
        """ Test with non-integer pixel coordinates. """
        result = convert_pixel_to_3d_coordinates(self.K, 100, 320.5, 240.5)
        expected_x = (320.5 - 320) / 1000 * 100
        expected_y = (240.5 - 240) / 1000 * 100
        np.testing.assert_array_almost_equal(result, np.array([expected_x, expected_y, 100]))

if __name__ == '__main__':
    unittest.main()