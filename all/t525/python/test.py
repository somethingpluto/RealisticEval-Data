import unittest

import numpy as np


class TestFlipPointCloud(unittest.TestCase):

    def test_flip_x_axis(self):
        """Test flipping the point cloud across the x-axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        expected_output = np.array([[1.0, -2.0, 3.0], [4.0, -5.0, 6.0]])
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=1), expected_output)

    def test_flip_y_axis(self):
        """Test flipping the point cloud across the y-axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        expected_output = np.array([[-1.0, 2.0, 3.0], [-4.0, 5.0, 6.0]])
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=0), expected_output)

    def test_flip_z_axis(self):
        """Test flipping the point cloud across the z-axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        expected_output = np.array([[1.0, 2.0, -3.0], [4.0, 5.0, -6.0]])
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=2), expected_output)

    def test_invalid_axis(self):
        """Test handling of an invalid axis."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        with self.assertRaises(ValueError) as context:
            flip_point_cloud(point_cloud, axis=3)  # Invalid axis
        self.assertEqual(str(context.exception), "Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).")

    def test_empty_point_cloud(self):
        """Test flipping an empty point cloud."""
        point_cloud = np.array([]).reshape(0, 3)  # Empty point cloud with shape (0, 3)
        expected_output = np.array([]).reshape(0, 3)  # Expect the output to be the same
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=0), expected_output)