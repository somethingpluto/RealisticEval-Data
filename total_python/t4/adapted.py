import math


def quaternion_to_yaw(x, y, z, w):
    """
    Convert a quaternion into yaw (rotation around z-axis in radians)
    """
    return math.atan2(+2.0 * (w * z + x * y), +1.0 - 2.0 * (y * y + z * z))
