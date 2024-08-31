from typing import List

import numpy as np


def change_reference_frame(point_cloud: np.array, ref_frame_points: List[np.array]) -> np.array:
    """
    Transforms a point cloud to a new reference frame defined by three points.

    Parameters:
        point_cloud (np.array): The Nx3 array of points in the original reference frame.
        ref_frame_points (list): A list of three points (np.array), defining the new reference frame.

    Returns:
        np.array: Transformed point cloud in the new reference frame.
    """
