import numpy as np

def scale_point_cloud(point_cloud: np.ndarray, scale_factor: float) -> np.ndarray:
    """
    Scale the point cloud by a given factor.

    Parameters:
    - point_cloud: A N x 3 numpy array representing the 3D point cloud.
    - scale_factor: A float representing the scaling factor.

    Returns:
    - A N x 3 numpy array of the scaled point cloud.
    """
    # Ensure point_cloud is a numpy array
    point_cloud = np.asarray(point_cloud)

    # Validate input shape
    if point_cloud.ndim != 2 or point_cloud.shape[1] != 3:
        raise ValueError("point_cloud must be a 2D array with shape (N, 3)")

    # Scale the point cloud by the given factor
    scaled_point_cloud = point_cloud * scale_factor

    return scaled_point_cloud