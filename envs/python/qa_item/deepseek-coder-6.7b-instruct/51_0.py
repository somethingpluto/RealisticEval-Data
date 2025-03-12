from typing import List
import numpy as np

def transform_point_cloud_to_reference_frame(point_cloud: np.array, ref_frame_points: List[np.array]) -> np.array:
    """
    Transforms a point cloud to a new reference frame defined by three points.

    Parameters:
        point_cloud (np.array): The Nx3 array of points in the original reference frame.
        ref_frame_points (List): A list of three points (np.array), defining the new reference frame.

    Returns:
        np.array: Transformed point cloud in the new reference frame.
    """
    # Extract the three reference points
    p1, p2, p3 = ref_frame_points
    
    # Define the new origin (p1)
    new_origin = p1
    
    # Define the new x-axis (p2 - p1)
    new_x_axis = p2 - p1
    new_x_axis /= np.linalg.norm(new_x_axis)
    
    # Define the new y-axis (p3 - p1)
    new_y_axis = p3 - p1
    new_y_axis -= np.dot(new_y_axis, new_x_axis) * new_x_axis
    new_y_axis /= np.linalg.norm(new_y_axis)
    
    # Define the new z-axis (cross product of new x-axis and new y-axis)
    new_z_axis = np.cross(new_x_axis, new_y_axis)
    
    # Construct the transformation matrix
    R = np.array([new_x_axis, new_y_axis, new_z_axis]).T
    T = -np.dot(R, new_origin)
    
    # Apply the transformation to each point in the point cloud
    transformed_point_cloud = np.dot(point_cloud, R.T) + T
    
    return transformed_point_cloud
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