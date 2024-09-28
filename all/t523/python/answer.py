import numpy as np

def translate_point_cloud(point_cloud: np.ndarray, translation_vector: np.ndarray) -> np.ndarray:
    """
    Translate the point cloud by a given vector.

    Parameters:
    - point_cloud: A N x 3 numpy array representing the 3D point cloud.
    - translation_vector: A 1 x 3 numpy array or list representing the translation vector.

    Returns:
    - A N x 3 numpy array of the translated point cloud.
    """
    # Ensure the translation_vector is a numpy array for broadcasting
    translation_vector = np.asarray(translation_vector)

    # Check if translation_vector is of correct shape
    if translation_vector.shape != (3,):
        raise ValueError("translation_vector must be a 1D array of shape (3,)")

    # Translate the point cloud by adding the translation vector to each point
    translated_point_cloud = point_cloud + translation_vector

    return translated_point_cloud