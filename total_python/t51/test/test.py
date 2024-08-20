import unittest
import numpy as np

class TestChangeReferenceFrame(unittest.TestCase):

    def setUp(self):
        # This method will be executed before each test function.
        # Define some common points and reference frames for testing.
        self.point_cloud = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        self.ref_frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 1, 0])]

    def test_identity_transformation(self):
        # Test with the reference frame being the standard basis, should not change the points
        expected = self.point_cloud.copy()
        result = change_reference_frame(self.point_cloud, self.ref_frame_points)
        np.testing.assert_array_almost_equal(result, expected)

    def test_translation(self):
        # Test only translation (no rotation)
        ref_frame_points = [np.array([1, 1, 1]), np.array([2, 1, 1]), np.array([1, 2, 1])]
        expected = np.array([
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ])
        result = change_reference_frame(self.point_cloud, ref_frame_points)
        np.testing.assert_array_almost_equal(result, expected)

    def test_rotation(self):
        # Test rotation around the z-axis by 90 degrees
        ref_frame_points = [np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
        expected = np.array([
            [-2, 1, 3],
            [-5, 4, 6],
            [-8, 7, 9]
        ])
        result = change_reference_frame(self.point_cloud, ref_frame_points)
        np.testing.assert_array_almost_equal(result, expected)

    def test_complex_transformation(self):
        # Test a combination of translation and rotation
        ref_frame_points = [np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([1, 0, 0])]
        expected = np.array([
            [2, -1, 3],
            [5, -4, 6],
            [8, -7, 9]
        ])
        result = change_reference_frame(self.point_cloud, ref_frame_points)
        np.testing.assert_array_almost_equal(result, expected)

    def test_no_change(self):
        # Test with the point cloud at the origin and minimal reference frame changes
        point_cloud = np.array([[0, 0, 0]])
        expected = np.array([[0, 0, 0]])
        result = change_reference_frame(point_cloud, self.ref_frame_points)
        np.testing.assert_array_almost_equal(result, expected)