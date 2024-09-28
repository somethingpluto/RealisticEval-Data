import unittest

import numpy as np


class TestTranslatePointCloud(unittest.TestCase):

    def test_simple_translation(self):
        """Test a simple translation of a single point."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        translation_vector = np.array([1.0, 1.0, 1.0])
        expected_output = np.array([[2.0, 3.0, 4.0]])
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)

    def test_multiple_points_translation(self):
        """Test translation of multiple points."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        translation_vector = np.array([1.0, 2.0, 3.0])
        expected_output = np.array([[2.0, 4.0, 6.0], [5.0, 7.0, 9.0]])
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)

    def test_zero_translation(self):
        """Test translation by a zero vector (should return the same point cloud)."""
        point_cloud = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        translation_vector = np.array([0.0, 0.0, 0.0])
        expected_output = point_cloud  # No change expected
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)

    def test_negative_translation(self):
        """Test translation with negative values."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        translation_vector = np.array([-1.0, -2.0, -3.0])
        expected_output = np.array([[0.0, 0.0, 0.0]])
        np.testing.assert_array_almost_equal(translate_point_cloud(point_cloud, translation_vector), expected_output)

    def test_invalid_translation_vector(self):
        """Test handling of an invalid translation vector shape."""
        point_cloud = np.array([[1.0, 2.0, 3.0]])
        translation_vector = np.array([1.0, 2.0])  # Invalid shape, should raise an error
        with self.assertRaises(ValueError) as context:
            translate_point_cloud(point_cloud, translation_vector)
        self.assertEqual(str(context.exception), "translation_vector must be a 1D array of shape (3,)")