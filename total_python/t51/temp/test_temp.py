import unittest
import numpy as np

class TestChangeReferenceFrame(unittest.TestCase):
    def setUp(self):
        # Basic setup for tests, initialize some common point clouds and frames
        self.point_cloud = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.ref_frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 1, 0])]

    def test_identity_transformation(self):
        # Test with an identity transformation where the reference frame is the standard basis
        result = change_reference_frame(self.point_cloud, self.ref_frame_points)
        np.testing.assert_array_almost_equal(result, self.point_cloud - np.array([0, 0, 0]))

    def test_translation(self):
        # Only translation no rotation; move the origin
        frame_points = [np.array([1, 1, 1]), np.array([2, 1, 1]), np.array([1, 2, 1])]
        result = change_reference_frame(self.point_cloud, frame_points)
        expected = np.array([[-1. , 0.,  1.], [ 2. , 3.,  4.], [ 5.,  6. , 7.]])
        np.testing.assert_array_almost_equal(result, expected)

    def test_rotation(self):
        # Rotation about z-axis by 90 degrees
        frame_points = [np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([0, 1, 1])]
        result = change_reference_frame(self.point_cloud, frame_points)
        expected = np.array([[2. , 3.,  1.], [ 5. , 6.,  4.], [ 8.,  9. , 7.]])
        np.testing.assert_array_almost_equal(result, expected)

    def test_non_orthonormal_frame(self):
        # Use non-orthonormal frame to see how function handles it (should normalize internally)
        frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([1, 1, 0])]
        result = change_reference_frame(self.point_cloud, frame_points)
        # Manually compute expected result
        u = np.array([1, 0, 0])
        v = np.array([0, 1, 0])
        w = np.cross(u, v)
        rotation_matrix = np.column_stack((u, v, w))
        expected = np.dot(self.point_cloud, rotation_matrix.T)
        np.testing.assert_array_almost_equal(result, expected)

    def test_inverted_frame(self):
        # Inverting the frame to see if negatives are handled
        frame_points = [np.array([0, 0, 0]), np.array([-1, 0, 0]), np.array([0, -1, 0])]
        result = change_reference_frame(self.point_cloud, frame_points)
        expected = np.dot(self.point_cloud, np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]))
        np.testing.assert_array_almost_equal(result, expected)

import numpy as np


def change_reference_frame(point_cloud, ref_frame_points):
    """
    Transforms a point cloud to a new reference frame defined by three points.

    Parameters:
        point_cloud (np.array): The Nx3 array of points in the original reference frame.
        ref_frame_points (list): A list of three points (np.array), defining the new reference frame.

    Returns:
        np.array: Transformed point cloud in the new reference frame.
    """
    # Convert points to float to avoid type casting errors during operations
    point_cloud = point_cloud.astype(np.float64)
    ref_frame_points = [p.astype(np.float64) for p in ref_frame_points]

    # Unpack the three points defining the new reference frame
    A, B, C = ref_frame_points

    # Compute the new basis vectors
    u = B - A  # Vector from A to B
    w = np.cross(u, C - A)  # Orthogonal vector to the plane defined by A, B, and C
    v = np.cross(w, u)  # Vector orthogonal to both u and w

    # Normalize the basis vectors to form an orthonormal basis
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    w /= np.linalg.norm(w)

    # Construct the rotation matrix from the old basis to the new basis
    rotation_matrix = np.column_stack((u, v, w))

    # Calculate the translation vector to shift origin to A
    translation_vector = -np.dot(rotation_matrix, A)

    # Apply the rotation and translation to the point cloud
    transformed_point_cloud = np.dot(point_cloud - A, rotation_matrix) + translation_vector

    return transformed_point_cloud