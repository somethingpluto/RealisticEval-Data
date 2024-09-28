import numpy as np


def translate_point_cloud(point_cloud: np.ndarray, translation_vector: np.ndarray) -> np.ndarray:
    """
    Translate the point cloud by a given vector.

    Args:
        point_cloud (np.ndarray): A N x 3 numpy array representing the 3D point cloud.
        translation_vector (np.ndarray): A 1 x 3 numpy array or list representing the translation vector.

    Returns:
        np.ndarray: A N x 3 numpy array of the translated point cloud.
    """
