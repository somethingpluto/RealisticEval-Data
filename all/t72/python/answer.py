import numpy as np


def convert_pixel_to_3d_coordinates(K, d, x, y):
    """Written by ChatGPT and fixed by me

    Args:
        K ((3,3) np.array): camera intrinsic matrix
        d (float): depth (distance along z-axis)
        x (float): pixel x coordinate
        y (float): pixel y coordinate

    Returns:
        (3,) np.array: x, y, z 3D point coordinates in camera RDF coordinates
    """
    # Step 1: Convert pixel coordinates to normalized device coordinates (NDC)
    cx = K[0, 2]
    cy = K[1, 2]
    fx = K[0, 0]
    fy = K[1, 1]

    NDC_x = (x - cx) / fx
    NDC_y = (y - cy) / fy

    # Step 2: Get the 3D world coordinates (W)
    W_x = NDC_x * d
    W_y = NDC_y * d
    W_z = d
    return np.array([W_x, W_y, W_z])