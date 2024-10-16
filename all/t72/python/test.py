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
