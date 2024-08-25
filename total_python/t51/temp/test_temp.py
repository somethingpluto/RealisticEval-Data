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




def change_reference_frame(point_cloud, ref_frame_points):
    """
    Transforms a point cloud to a new reference frame defined by three points.

    Parameters:
    - point_cloud (np.ndarray): The Nx3 array of points representing the point cloud.
    - ref_frame_points (list of np.ndarray): A list containing three 3D points (A, B, C) that define the new reference frame.

    Returns:
    - np.ndarray: The transformed point cloud as an Nx3 array.
    """
    # Unpack the reference frame points
    A, B, C = ref_frame_points

    # Define the new basis vectors
    u = B - A  # Vector from A to B
    w = np.cross(u, C - A)  # Normal to the plane formed by vectors AB and AC
    v = np.cross(w, u)  # Orthogonal to both u and w

    # Normalize the basis vectors to create an orthonormal basis
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    w /= np.linalg.norm(w)

    # Construct the rotation matrix using the orthonormal basis vectors
    rotation_matrix = np.column_stack((u, v, w))

    # Compute the translation vector to shift the origin to point A
    translation_vector = -np.dot(rotation_matrix, A)

    # Apply the rotation and translation to the point cloud
    # Matrix multiplication is done with the transpose of the rotation matrix
    # because we are transforming the coordinates to the new basis
    transformed_point_cloud = np.dot(point_cloud - A, rotation_matrix)

    return transformed_point_cloud
