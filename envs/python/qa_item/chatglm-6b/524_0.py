
import numpy as np

def scale_point_cloud(point_cloud: np.ndarray, scale_factor: float) -> np.ndarray:
    """
    Scale the point cloud by a given factor.

    Args:
        point_cloud (np.ndarray): A N x 3 numpy array representing the 3D point cloud.
        scale_factor ( float): A float representing the scaling factor.

    Returns:
        np.ndarray: A N x 3 numpy array of the scaled point cloud.
    """
    # Convert the point cloud to a 3D array
    point_cloud_3d = np.array(point_cloud, dtype=np.float32)

    # Apply the scale factor to each element of the 3D array
    scaled_point_cloud_3d = np.dot(point_cloud_3d, np.array(scale_factor, dtype=np.float32))

    return scaled_point_cloud_3d

import unittest

import numpy as np


class TestScalePointCloud(unittest.TestCase):

    def test_simple_scaling(self):
        """Test scaling of a single point."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        scale_factor = 2.0
        expected_output = np.array([[2.0, 4.0, 6.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

    def test_multiple_points_scaling(self):
        """Test scaling of multiple points."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        scale_factor = 0.5
        expected_output = np.array([[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

    def test_zero_scaling(self):
        """Test scaling by a factor of zero (should return a point cloud of zeros)."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        scale_factor = 0.0
        expected_output = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

    def test_negative_scaling(self):
        """Test scaling with a negative factor."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        scale_factor = -2.0
        expected_output = np.array([[-2.0, -4.0, -6.0]])
        np.testing.assert_array_almost_equal(scale_point_cloud(point_cloud, scale_factor), expected_output)

if __name__ == '__main__':
    unittest.main()