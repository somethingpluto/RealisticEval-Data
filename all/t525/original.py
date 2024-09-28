# written by chatgpt
import numpy as np


def flip_point_cloud(self, point_cloud, axis):
    """Flip the point cloud across a given axis."""
    return point_cloud * np.array([-1 if i == axis else 1 for i in range(point_cloud.shape[1])])