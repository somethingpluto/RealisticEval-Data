import numpy as np


def convert_pixel_to_3d_coordinates(K: np.array, d: float, x: float, y: float) -> np.array:
    """
    Convert 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.

    Args:
        K (np.array): A (3, 3) camera intrinsic matrix, which includes focal lengths and optical center.
        d (float): Depth (distance along the z-axis) from the camera to the point in 3D space.
        x (float): The x coordinate of the pixel in 2D image space.
        y (float): The y coordinate of the pixel in 2D image space.

    Returns:
        np.array: A numpy array containing the 3D coordinates (x, y, z) in the camera's right-handed coordinate frame.
    """
