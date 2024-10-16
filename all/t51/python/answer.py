import numpy as np


def transform_point_cloud_to_reference_frame(point_cloud, ref_frame_points):
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