import unittest

import numpy as np


class TestChangeReferenceFrame(unittest.TestCase):

    def test_standard_basis(self):
        # Points aligned with standard axes
        point_cloud = np.array([[1, 2, 3], [4, 5, 6], [-1, -1, -1]])
        ref_frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 1, 0])]
        transformed = change_reference_frame(point_cloud, ref_frame_points)
        expected = point_cloud  # No change expected in coordinates
        np.testing.assert_array_almost_equal(transformed, expected)

    def test_inverted_frame(self):
        # Flipping the reference frame
        point_cloud = np.array([[1, 2, 3], [4, 5, 6], [-1, -1, -1]])
        ref_frame_points = [np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([1, 0, 0])]
        transformed = change_reference_frame(point_cloud, ref_frame_points)
        expected = np.array([[2, 1, 3], [5, 4, 6], [-1, -1, -1]])  # Expect a flip in x and y coordinates
        np.testing.assert_array_almost_equal(transformed, expected)

    def test_collinear_points(self):
        # All reference points are collinear
        point_cloud = np.array([[1, 2, 3], [4, 5, 6]])
        ref_frame_points = [np.array([0, 0, 0]), np.array([1, 1, 1]), np.array([2, 2, 2])]
        with self.assertRaises(ValueError):  # Assuming function should raise an error
            change_reference_frame(point_cloud, ref_frame_points)

    def test_large_point_cloud(self):
        # Large number of points to test performance
        point_cloud = np.random.rand(1000, 3)  # 1000 random 3D points
        ref_frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 1, 0])]
        transformed = change_reference_frame(point_cloud, ref_frame_points)
        self.assertEqual(transformed.shape, point_cloud.shape)

    def test_origin_point_cloud(self):
        # Point cloud at the origin
        point_cloud = np.zeros((5, 3))
        ref_frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 1, 0])]
        transformed = change_reference_frame(point_cloud, ref_frame_points)
        expected = np.zeros((5, 3))
        np.testing.assert_array_almost_equal(transformed, expected)