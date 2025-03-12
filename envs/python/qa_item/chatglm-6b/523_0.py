
import numpy as np

def translate_point_cloud(point_cloud: np.ndarray, translation_vector: np.ndarray) -> np.ndarray:
    """
    Translate the point cloud by a given vector.

    Args:
        point_cloud (np.ndarray): A N x 3 numpy array representing the 3D point cloud.
        translation_vector (np.ndarray): A 1 x 3 numpy array or list representing the translation vector.

    Returns:
        np.ndarray: A N x 3 numpy array of the translated point cloud.
    """
    # Convert the translation vector to a 1x3 numpy array or list
    translation_vector = translation_vector.reshape(1, 3)

    # Translate the point cloud by the vector
     translated_point_cloud = point_cloud.copy()
    translated_point_cloud[0, 0] = translation_vector[0]
    translated_point_cloud[0, 1] = translation_vector[1]
    translated_point_cloud[0, 2] = translation_vector[2]
    translated_point_cloud[1, 0] = translation_vector[3]
    translated_point_cloud[1, 1] = translation_vector[4]
    translated_point_cloud[1, 2] = translation_vector[5]
    translated_point_cloud[2, 0] = translation_vector[6]
    translated_point_cloud[2, 1] = translation_vector[7]
    translated_point_cloud[2, 2] = translation_vector[8]

    return translated_point_cloud

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
if __name__ == '__main__':
    unittest.main()