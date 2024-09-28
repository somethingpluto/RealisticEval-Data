# written by chatgpt
import numpy as np


def rotate_point_cloud(self, point_cloud, rotation_angle):
    """Rotate the point cloud around the Y axis by a given angle."""
    rotation_matrix = np.array([
        [np.cos(rotation_angle), 0, np.sin(rotation_angle)],
        [0, 1, 0],
        [-np.sin(rotation_angle), 0, np.cos(rotation_angle)]
    ])
    return np.dot(point_cloud, rotation_matrix)