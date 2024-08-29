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
