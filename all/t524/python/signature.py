import numpy as np

def scale_point_cloud(point_cloud: np.ndarray, scale_factor: float) -> np.ndarray:
    """
    Scale the point cloud by a given factor.

    Args:
        point_cloud (np.ndarray): A N x 3 numpy array representing the 3D point cloud.
        scale_factor ( float): A float representing the scaling factor.

    Returns:
        np.ndarray: A N x 3 numpy array of the scaled point cloud.
    """