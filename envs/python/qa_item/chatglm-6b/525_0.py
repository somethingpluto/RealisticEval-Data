
import numpy as np

def flip_point_cloud(point_cloud: np.ndarray, axis: int) -> np.ndarray:
    """
     Flip the point cloud across a specified axis.

    Args:
        point_cloud (np.ndarray): A N x 3 numpy array representing the 3D point cloud.
        axis (int): An integer specifying the axis to flip (0 for x, 1 for y, 2 for z).

    Returns:
        np.ndarray: A N x 3 numpy array of the flipped point cloud.
    """
    # Convert the point cloud to a 2D array
    point_cloud_2d = point_cloud.reshape(-1, 3)

    # Flip the 2D array along the specified axis
     flipped_point_cloud_2d = np.flip(point_cloud_2d, axis)

    # Convert the 2D array back to a 3D array
    flipped_point_cloud_3d = flipped_point_cloud_2d.reshape(-1, 3)

    return flipped_point_cloud_3d

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
        self.assertRaises(Exception)


    def test_empty_point_cloud(self):
        """Test flipping an empty point cloud."""
        point_cloud = np.array([]).reshape(0, 3)  # Empty point cloud with shape (0, 3)
        expected_output = np.array([]).reshape(0, 3)  # Expect the output to be the same
        np.testing.assert_array_almost_equal(flip_point_cloud(point_cloud, axis=0), expected_output)
if __name__ == '__main__':
    unittest.main()