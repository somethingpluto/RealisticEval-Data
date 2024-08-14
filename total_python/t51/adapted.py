import numpy as np


def define_transformation_matrix(p1, p2, p3):
    """
    Create a transformation matrix from three points.
    p1 is the new origin.
    p2 - p1 is the new x-axis.
    p3 - p1 is the new plane defined with x-axis.
    """
    origin = np.array(p1)
    x_axis = np.array(p2) - origin
    x_axis = x_axis / np.linalg.norm(x_axis)  # Normalize to make it unit vector

    temp_y_axis = np.array(p3) - origin
    z_axis = np.cross(x_axis, temp_y_axis)
    z_axis = z_axis / np.linalg.norm(z_axis)  # Normalize to make it unit vector

    y_axis = np.cross(z_axis, x_axis)

    # Create transformation matrix
    transformation_matrix = np.stack([x_axis, y_axis, z_axis, origin]).T
    transformation_matrix = np.vstack([transformation_matrix, [0, 0, 0, 1]])  # For homogeneous coordinates
    return transformation_matrix


def transform_point_cloud(points, transformation_matrix):
    """
    Transform a list of points using the transformation matrix.
    Points are expected as a list of tuples or lists.
    """
    points_homogeneous = np.hstack([points, np.ones((len(points), 1))])  # Convert to homogeneous coordinates
    transformed_points = points_homogeneous.dot(transformation_matrix.T)[:, :3]  # Apply transformation
    return transformed_points
