import numpy as np


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
