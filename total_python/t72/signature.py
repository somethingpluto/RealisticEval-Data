def get_3d_coordinates(K, d, x, y):
    """
    converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
    Args:
        K ((3,3) np.array): camera intrinsic matrix
        d (float): depth (distance along z-axis)
        x (float): pixel x coordinate
        y (float): pixel y coordinate

    Returns:
        (3,) np.array: x, y, z 3D point coordinates in camera RDF coordinates
    """