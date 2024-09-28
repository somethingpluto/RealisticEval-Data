import numpy as np


def flip_point_cloud(point_cloud: np.ndarray, axis: int) -> np.ndarray:
    """
    Flip the point cloud across a specified axis.

    Parameters:
    - point_cloud: A N x 3 numpy array representing the 3D point cloud.
    - axis: An integer specifying the axis to flip (0 for x, 1 for y, 2 for z).

    Returns:
    - A N x 3 numpy array of the flipped point cloud.
    """

    # Validate the axis input
    if axis not in [0, 1, 2]:
        raise ValueError("Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).")

    # Create a scaling factor array with -1 for the specified axis and 1 for others
    flip_factors = np.array([-1 if i == axis else 1 for i in range(point_cloud.shape[1])])

    # Flip the point cloud by multiplying with the scaling factor array
    flipped_point_cloud = point_cloud * flip_factors

    return flipped_point_cloud
