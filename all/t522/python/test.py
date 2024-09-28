import unittest

import numpy as np


class TestRotatePointCloud(unittest.TestCase):

    def test_no_rotation(self):
        """Test when rotation angle is 0 (should return the same point cloud)."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        rotation_angle = 0
        expected_output = point_cloud
        np.testing.assert_array_almost_equal(rotate_point_cloud(point_cloud, rotation_angle), expected_output)

    def test_180_degree_rotation(self):
        """Test rotation of 180 degrees (π radians) around Y axis."""
        point_cloud = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
        rotation_angle = np.pi  # 180 degrees
        expected_output = np.array([[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])  # [1,0,0] -> [-1,0,0]
        np.testing.assert_array_almost_equal(rotate_point_cloud(point_cloud, rotation_angle), expected_output)

    def test_full_rotation(self):
        """Test rotation of 360 degrees (2π radians) around Y axis (should return same point cloud)."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        rotation_angle = 2 * np.pi  # 360 degrees
        expected_output = point_cloud  # Should return the same point cloud
        np.testing.assert_array_almost_equal(rotate_point_cloud(point_cloud, rotation_angle), expected_output)

    def test_negative_rotation(self):
        """Test rotation with a negative angle (-90 degrees)."""
        point_cloud = np.array([[1.0, 0.0, 0.0]])
        rotation_angle = -np.pi / 2  # -90 degrees
        expected_output = np.array([[0.0, 0.0, -1.0]])  # [1,0,0] -> [0,0,-1]
        np.testing.assert_array_almost_equal(rotate_point_cloud(point_cloud, rotation_angle), expected_output)