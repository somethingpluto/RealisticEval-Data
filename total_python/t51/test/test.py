import unittest
import numpy as np

class TestPointCloudTransformation(unittest.TestCase):
    def setUp(self):
        # Common setup for all tests
        self.p1 = [0, 0, 0]  # Default new origin
        self.p2 = [1, 0, 0]  # Default x-axis
        self.p3 = [0, 1, 0]  # Default y-axis (z-axis automatically calculated)

    def test_simple_shift(self):
        # Shift the origin without rotation
        points = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        expected_transformed_points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        transformation_matrix = define_transformation_matrix([1, 1, 1], [2, 1, 1], [1, 2, 1])
        transformed_points = transform_point_cloud(points, transformation_matrix)
        np.testing.assert_array_almost_equal(transformed_points, expected_transformed_points)

    def test_rotation(self):
        # Rotate around z-axis
        points = np.array([[1, 0, 0], [0, 1, 0]])
        expected_transformed_points = np.array([[0, 1, 0], [-1, 0, 0]])
        transformation_matrix = define_transformation_matrix(self.p1, [0, 1, 0], [0, 0, 1])
        transformed_points = transform_point_cloud(points, transformation_matrix)
        np.testing.assert_array_almost_equal(transformed_points, expected_transformed_points)

    def test_full_transformation(self):
        # Full transformation with shift and rotation
        points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        expected_transformed_points = np.array([[0, 0, 0], [-np.sqrt(2), 0, 0], [-2 * np.sqrt(2), 0, 0]])
        transformation_matrix = define_transformation_matrix([1, 1, 0], [0, 1, 0], [1, 0, 1])
        transformed_points = transform_point_cloud(points, transformation_matrix)
        np.testing.assert_array_almost_equal(transformed_points, expected_transformed_points)

    def test_identity_transformation(self):
        # Identity transformation (no change)
        points = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected_transformed_points = points
        transformation_matrix = define_transformation_matrix(self.p1, self.p2, self.p3)
        transformed_points = transform_point_cloud(points, transformation_matrix)
        np.testing.assert_array_almost_equal(transformed_points, expected_transformed_points)

    def test_complex_transformation(self):
        # Complex transformation with non-standard axes
        points = np.array([[0, 0, 0], [1, 1, 1], [2, 0, 0]])
        expected_transformed_points = np.array([[0, 0, 0], [1, 0, 0], [2, 0, 0]])
        transformation_matrix = define_transformation_matrix([0, 0, 0], [1, 1, 1], [1, -1, 0])
        transformed_points = transform_point_cloud(points, transformation_matrix)
        np.testing.assert_array_almost_equal(transformed_points, expected_transformed_points)