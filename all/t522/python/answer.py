import numpy as np

def rotate_point_cloud(point_cloud: np.ndarray, rotation_angle: float) -> np.ndarray:
    """
    Rotate the point cloud around the Y axis by a given angle.

    Parameters:
    - point_cloud: A N x 3 numpy array representing the 3D point cloud.
    - rotation_angle: The angle (in radians) to rotate the point cloud.

    Returns:
    - A N x 3 numpy array of the rotated point cloud.
    """
    # Create the rotation matrix for a rotation around the Y axis
    rotation_matrix = np.array([
        [np.cos(rotation_angle), 0, np.sin(rotation_angle)],
        [0, 1, 0],
        [-np.sin(rotation_angle), 0, np.cos(rotation_angle)]
    ])

    # Rotate the point cloud by multiplying with the rotation matrix
    rotated_point_cloud = np.dot(point_cloud, rotation_matrix)

    return rotated_point_cloud