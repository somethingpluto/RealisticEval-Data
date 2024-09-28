import numpy as np


def rotate_point_cloud(point_cloud: np.ndarray, rotation_angle: float) -> np.ndarray:
    """
    Rotate the point cloud around the Y axis by a given angle.

    Args:
        point_cloud (np.ndarray): A N x 3 numpy array representing the 3D point cloud.
        rotation_angle (float): The angle (in radians) to rotate the point cloud.

    Returns:
        np.ndarray: A N x 3 numpy array of the rotated point cloud.
    """
