def transform_point_cloud_to_reference_frame(point_cloud: np.array, ref_frame_points: List[np.array]) -> np.array:
    # Calculate the centroid of the original reference frame
    centroid_original = np.mean(point_cloud, axis=0)

    # Calculate the centroid of the new reference frame
    centroid_new = np.mean(ref_frame_points, axis=0)

    # Calculate the shift vector
    shift_vector = centroid_new - centroid_original

    # Calculate the transformation matrix
    transformation_matrix = np.eye(4)
    transformation_matrix[:3, 3] = shift_vector

    # Transform the point cloud
    point_cloud_transformed = np.dot(point_cloud, transformation_matrix[:3, :3].T) + shift_vector

    return point_cloud_transformed
import unittest
import numpy as np

class TestChangeReferenceFrame(unittest.TestCase):
    def setUp(self):
        # Basic setup for tests, initialize some common point clouds and frames
        self.point_cloud = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.ref_frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([0, 1, 0])]

    def test_identity_transformation(self):
        # Test with an identity transformation where the reference frame is the standard basis
        result = transform_point_cloud_to_reference_frame(self.point_cloud, self.ref_frame_points)
        np.testing.assert_array_almost_equal(result, self.point_cloud - np.array([0, 0, 0]))

    def test_translation(self):
        # Only translation no rotation; move the origin
        frame_points = [np.array([1, 1, 1]), np.array([2, 1, 1]), np.array([1, 2, 1])]
        result = transform_point_cloud_to_reference_frame(self.point_cloud, frame_points)
        expected = np.array([[-1. , 0.,  1.], [ 2. , 3.,  4.], [ 5.,  6. , 7.]])
        np.testing.assert_array_almost_equal(result, expected)

    def test_rotation(self):
        # Rotation about z-axis by 90 degrees
        frame_points = [np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([0, 1, 1])]
        result = transform_point_cloud_to_reference_frame(self.point_cloud, frame_points)
        expected = np.array([[2. , 3.,  1.], [ 5. , 6.,  4.], [ 8.,  9. , 7.]])
        np.testing.assert_array_almost_equal(result, expected)

    def test_non_orthonormal_frame(self):
        # Use non-orthonormal frame to see how function handles it (should normalize internally)
        frame_points = [np.array([0, 0, 0]), np.array([1, 0, 0]), np.array([1, 1, 0])]
        result = transform_point_cloud_to_reference_frame(self.point_cloud, frame_points)
        # Manually compute expected model_answer_result
        u = np.array([1, 0, 0])
        v = np.array([0, 1, 0])
        w = np.cross(u, v)
        rotation_matrix = np.column_stack((u, v, w))
        expected = np.dot(self.point_cloud, rotation_matrix.T)
        np.testing.assert_array_almost_equal(result, expected)

    def test_inverted_frame(self):
        # Inverting the frame to see if negatives are handled
        frame_points = [np.array([0, 0, 0]), np.array([-1, 0, 0]), np.array([0, -1, 0])]
        result = transform_point_cloud_to_reference_frame(self.point_cloud, frame_points)
        expected = np.dot(self.point_cloud, np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]))
        np.testing.assert_array_almost_equal(result, expected)

if __name__ == '__main__':
    unittest.main()