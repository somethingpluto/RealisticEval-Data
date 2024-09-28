import numpy as np


def flip_point_cloud(point_cloud: np.ndarray, axis: int) -> np.ndarray:
    """
    Flip the point cloud across a specified axis.

    Args:
        point_cloud (np.ndarray): A N x 3 numpy array representing the 3D point cloud.
        axis (int): An integer specifying the axis to flip (0 for x, 1 for y, 2 for z).

    Returns:
        np.ndarray: A N x 3 numpy array of the flipped point cloud.
    """
